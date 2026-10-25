"""Where an access token lives between calls.

A store persists and locks, and moves plain dicts so it never imports the provider.

* :class:`FileTokenStore` - a JSON file plus a lock, shared across processes and the
  default, at the per-user cache path from :func:`build_default_token_cache_path`. It
  persists a refresh token, usable long after the access token expires.
* :class:`MemoryTokenStore` - per-process, per-instance, nothing on disk. Selected
  by passing ``token_cache_path=None``.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import sys
import tempfile
import threading
import time
import warnings
from abc import ABC, abstractmethod
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

from exsited.errors import SdkConfigError, SdkError

#: The cache filename, imported by :mod:`exsited.config.auth_config` so it and the
#: default of :func:`build_default_token_cache_path` cannot disagree. The directory is
#: shared, so the language in the name keeps this file apart from any other client's.
DEFAULT_TOKEN_CACHE_FILENAME = "exsited_python_token.json"

#: The most of the cache file this SDK will read; a larger file is refused. Any process
#: running as this user can write the file, so an unbounded read would let it decide the
#: memory cost. One entry is under 1 KB, about 9 KB with two 4 KB credentials, so a
#: megabyte holds far more credential sets than a machine has.
MAX_TOKEN_CACHE_BYTES = 1024 * 1024

_LOCK_SUFFIX = ".lock"
_LOCK_TIMEOUT_SECONDS = 30
_LOCK_POLL_SECONDS = 0.05
_DEFAULT_NAMESPACE = "default"
_REPLACE_RETRY_ATTEMPTS = 5
_REPLACE_RETRY_INITIAL_SECONDS = 0.01

_LOGGER = logging.getLogger("exsited.auth.token_store")


class SdkTokenCacheError(SdkError):
    """The token cache file is present and cannot be used.

    Distinct from an absent cache, which costs one authentication. Read as empty, the
    next write would rebuild the file from ``{}`` and delete every other namespace's
    token. Declared here, beside the cache, and an :class:`~exsited.errors.SdkError`.
    """


class SdkTokenLockError(SdkError):
    """The cross-process lock over the token cache could not be taken.

    Raised rather than running the refresh anyway: two processes refreshing at once
    overwrite each other's entry in a file they share.
    """


class DegradedTokenLockWarning(UserWarning):
    """The token cache could not be locked across processes.

    Accompanies :class:`SdkTokenLockError` on a channel a caller can filter or
    escalate, because the package installs a ``NullHandler`` and nothing it logs is
    visible on shipped defaults::

        warnings.filterwarnings("error", category=DegradedTokenLockWarning)
    """


class _CachePathGuard:
    """The in-process half of the lock over one cache path.

    One instance per cache file, shared by every store pointed at that file, so two
    clients built from one set of credentials coordinate.
    """

    __slots__ = ("lock", "depth", "degradation_announced")

    def __init__(self) -> None:
        self.lock = threading.RLock()
        self.depth = 0
        #: Whether the current unbroken run of lock refusals has already been announced,
        #: so a permanently unlockable path does not warn on every call.
        self.degradation_announced = False


#: Keyed by folded text rather than by ``Path``, so that a relative path, a symlink and
#: a difference in case on Windows all find the one guard for the file they name.
_GUARDS_BY_CACHE_PATH: dict[str, _CachePathGuard] = {}
_GUARDS_REGISTRY_LOCK = threading.Lock()


def _resolve_cache_path(file_path: str) -> Path:
    """The absolute real file a cache path names, resolved once and kept.

    Resolved, a later ``os.chdir`` cannot move the I/O away from the guard and the lock
    sidecar, and two spellings of one file share one guard.
    """
    return Path(os.path.realpath(str(file_path)))


def _guard_key(path: Path) -> str:
    """The key one cache path's guard is filed under, folded so every spelling meets."""
    return os.path.normcase(os.path.realpath(str(path)))


def _guard_for_path(path: Path) -> _CachePathGuard:
    key = _guard_key(path)
    with _GUARDS_REGISTRY_LOCK:
        guard = _GUARDS_BY_CACHE_PATH.get(key)
        if guard is None:
            guard = _CachePathGuard()
            _GUARDS_BY_CACHE_PATH[key] = guard
        return guard


def build_credentials_namespace(
    base_url: str,
    client_id: str,
    client_secret: str = "",
    auth_string: str = "",
    grant_type: str = "",
) -> str:
    """Fingerprint a set of credentials, for keying a shared token file.

    Derived from every value that decides *which principal the server mints for*, so
    identical credentials share one cached token and any difference gets its own entry:
    ``client_secret`` because a token minted under a rotated secret is not the new
    secret's. ``redirect_uri`` is sent by the token request but selects no token.

    ``auth_string`` is never passed here, since v4 takes no such credential; dropping it
    from the material would change every existing fingerprint.

    Each value is fed in with its length rather than joined on a separator, which would
    be forgeable: ``"secret"`` then ``"alice|extra"`` would key as ``"secret|alice"``
    then ``"extra"``. Values are hashed rather than stored, and the ``"v4"`` prefix
    keeps an entry written under another scheme from being read as this one.

    :return: a short, stable key.

    Example::

        build_credentials_namespace(
            "https://dev-api.exsited.com", "abc", "secret",
            grant_type="client_credentials",
        )
    """
    material = "".join(
        f"{len(value)}:{value}"
        for value in ("v4", base_url, client_id, client_secret, auth_string, grant_type)
    )
    digest = hashlib.sha256(material.encode("utf-8"))
    return digest.hexdigest()[:16]


def build_default_token_cache_path(
    filename: str = DEFAULT_TOKEN_CACHE_FILENAME,
) -> str:
    """Return the conventional per-user cache path for this platform.

    Keeps tokens out of the working directory, where a token is one ``.gitignore``
    mistake from being committed.

    ``%LOCALAPPDATA%\\exsited\\`` on Windows,
    ``~/Library/Caches/exsited/`` on macOS, else
    ``$XDG_CACHE_HOME/exsited/`` falling back to ``~/.cache/exsited/``.
    When the environment names no home directory (a Windows service, a container), the
    platform temporary directory stands in, so the result is absolute.

    :return: an absolute path. The directory is created if missing.

    Example::

        AuthConfig(
            client_name=..., base_url=...,
            token_cache_path=build_default_token_cache_path(),
        )
    """
    if sys.platform == "win32":
        root = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    elif sys.platform == "darwin":
        root = os.path.join(os.path.expanduser("~"), "Library", "Caches")
    else:
        root = os.environ.get("XDG_CACHE_HOME") or os.path.join(
            os.path.expanduser("~"), ".cache"
        )
    if not os.path.isabs(root):
        # ``expanduser`` hands back a literal ``'~'`` when there is no home to expand,
        # which would put a ``~`` directory holding a refresh token in the working directory.
        root = tempfile.gettempdir()
    directory = Path(root) / "exsited"
    directory.mkdir(parents=True, exist_ok=True)
    _restrict_to_owner(directory)
    return str(directory / filename)


def _restrict_to_owner(path: Path) -> None:
    """Best-effort ``0600``/``0700`` so only this user can read the tokens.

    A no-op on Windows, where inherited NTFS ACLs govern access rather than POSIX mode
    bits; this SDK neither tightens nor inspects them.
    """
    try:
        os.chmod(path, 0o700 if path.is_dir() else 0o600)
    except (OSError, NotImplementedError):
        pass


class TokenStore(ABC):
    """Interface for token persistence and refresh coordination."""

    @abstractmethod
    def read_token_record(self) -> dict[str, Any] | None:
        """Return the stored token, or ``None`` when absent or unreadable."""

    @abstractmethod
    def write_token_record(self, record: dict[str, Any]) -> None:
        """Persist a token, replacing whatever was there."""

    @abstractmethod
    def clear_token_record(self) -> None:
        """Discard the stored token. A no-op when there is none."""

    @abstractmethod
    @contextmanager
    def acquire_token_refresh_lock(self) -> Iterator[None]:
        """Hold the refresh lock for the duration of the block.

        Only one worker fetches a new token; the others wait.
        """


class MemoryTokenStore(TokenStore):
    """In-process token storage, isolated per instance.

    Two clients with their own stores never share a token.
    """

    def __init__(self) -> None:
        self._record: dict[str, Any] | None = None
        self._lock = threading.RLock()

    def read_token_record(self) -> dict[str, Any] | None:
        """Return a copy of the stored token, or ``None``.

        Copied, so callers cannot mutate the store in place.
        """
        with self._lock:
            return dict(self._record) if self._record else None

    def write_token_record(self, record: dict[str, Any]) -> None:
        """Store a token in memory."""
        with self._lock:
            self._record = dict(record)

    def clear_token_record(self) -> None:
        """Forget the stored token."""
        with self._lock:
            self._record = None

    @contextmanager
    def acquire_token_refresh_lock(self) -> Iterator[None]:
        """Serialise refreshes across threads in this process."""
        with self._lock:
            yield


class FileTokenStore(TokenStore):
    """Token storage in a JSON file, safe to share across processes.

    * The lock is a sidecar file, ``<path>.lock``: locking the data file in ``'w'``
      mode truncates it before the lock is honoured.
    * Writes are atomic, a temporary file in the same directory then ``os.replace``,
      retried briefly on Windows; see :meth:`_replace_the_token_file`.
    * Every mutation takes the cross-process lock itself, since each rewrites the whole
      file from a snapshot. The lock is reentrant.
    * The lock fails closed: with no cross-process lock to take, a mutation raises
      :class:`SdkTokenLockError`.
    * An unusable cache file is refused, not read as empty; see
      :class:`SdkTokenCacheError`.
    * One guard per cache path, resolved at construction, whatever spelling of the
      path a store was built with.

    One file is safe to share between instances: tokens are keyed by ``namespace``, a
    fingerprint of the credentials (see :func:`build_credentials_namespace`).

    :param file_path: where to keep the tokens, e.g. ``".exsited_token.json"``.
        Resolved to an absolute real path at construction, so a later ``os.chdir``
        cannot move the I/O. Parent directories are created as needed.
    :param namespace: which entry in the file belongs to this store. Use
        :func:`build_credentials_namespace`. ``None`` uses a shared ``"default"`` entry,
        correct only when nothing else writes there.
    """

    def __init__(self, file_path: str, namespace: str | None = None) -> None:
        # Resolved once, and the sidecar derived from the resolved path, so the lock and
        # the data it protects stay in one directory.
        self._path = _resolve_cache_path(file_path)
        self._lock_path = Path(str(self._path) + _LOCK_SUFFIX)
        self._namespace = namespace or _DEFAULT_NAMESPACE
        # Per cache path, not per instance: see :class:`_CachePathGuard`.
        self._guard = _guard_for_path(self._path)
        if self._path.parent and not self._path.parent.exists():
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
            except OSError as error:
                # A parent that is a regular file raises ``FileExistsError``, which is
                # not an ``SdkError``.
                raise SdkConfigError(
                    f"token_cache_path: the directory for {self._path} could not be "
                    f"created ({error}); pass a path whose parent exists, or None to "
                    f"keep the token in memory"
                ) from error

    def read_token_record(self) -> dict[str, Any] | None:
        """Read the stored token.

        Only this store's namespace is returned. A missing or empty file reads as
        ``None``: no token cached, one extra authentication.

        :raises SdkTokenCacheError: the file is there and cannot be read or parsed.
            Not ``None``, which means absent: a mutation rebuilt from ``None`` would
            discard every other namespace's token.
        """
        with self._guard.lock:
            entry = self._read_all_namespaces().get(self._namespace)
            return dict(entry) if isinstance(entry, dict) else None

    def write_token_record(self, record: dict[str, Any]) -> None:
        """Write the token atomically, leaving other namespaces intact.

        :raises SdkTokenCacheError: the existing file could not be read, so the
            snapshot this write would rebuild it from is not the file's contents.
        :raises SdkTokenLockError: the cache could not be locked across processes.
        """
        with self.acquire_token_refresh_lock():
            stored = self._read_all_namespaces()
            stored[self._namespace] = dict(record)
            self._write_all_namespaces(stored)

    def _write_all_namespaces(self, stored: dict[str, Any]) -> None:
        with self._guard.lock:
            directory = self._path.parent if str(self._path.parent) else Path(".")
            directory.mkdir(parents=True, exist_ok=True)
            handle, temporary_path = tempfile.mkstemp(
                dir=str(directory), prefix=self._path.name, suffix=".tmp"
            )
            try:
                with os.fdopen(handle, "w", encoding="utf-8") as stream:
                    json.dump(stored, stream)
                self._replace_the_token_file(temporary_path)
                _restrict_to_owner(self._path)
            except BaseException:
                try:
                    os.unlink(temporary_path)
                except OSError:
                    pass
                raise

    def _replace_the_token_file(self, temporary_path: str) -> None:
        """Move the written temporary file into place, retrying on Windows.

        On win32, one process reading the token file makes another's
        ``os.replace`` fail with ``[WinError 5] Access is denied``, because Python's
        ``open`` does not ask for ``FILE_SHARE_DELETE``; it clears in milliseconds. POSIX
        renames over an open file, so the retry is skipped there.

        Bounded at :data:`_REPLACE_RETRY_ATTEMPTS` attempts with a wait doubling from
        :data:`_REPLACE_RETRY_INITIAL_SECONDS`, roughly 150 ms at worst. The last failure
        is raised unchanged: the same ``WinError 5`` covers a directory this account may
        not write to.

        :raises OSError: the replace failed for any reason other than a Windows sharing
            denial, or was still denied after the last attempt.
        """
        for attempt in range(_REPLACE_RETRY_ATTEMPTS):
            try:
                os.replace(temporary_path, self._path)
                return
            except PermissionError:
                if sys.platform != "win32" or attempt == _REPLACE_RETRY_ATTEMPTS - 1:
                    raise
                time.sleep(_REPLACE_RETRY_INITIAL_SECONDS * (2 ** attempt))

    def clear_token_record(self) -> None:
        """Drop this store's entry, leaving other instances' tokens alone.

        The lock sidecar is never removed, only the data file: the sidecar is the lock's
        identity, and a waiter holding a lock on an unlinked sidecar would share the
        critical section with a process that created a fresh one.

        :raises SdkTokenCacheError: the file could not be read, so which other
            namespaces it holds is unknown and rewriting it would discard them.
        :raises SdkTokenLockError: the cache could not be locked across processes.
        """
        with self.acquire_token_refresh_lock():
            stored = self._read_all_namespaces()
            if stored.pop(self._namespace, None) is None:
                return
            if stored:
                self._write_all_namespaces(stored)
            else:
                try:
                    self._path.unlink()
                except (FileNotFoundError, OSError):
                    pass

    def _read_all_namespaces(self) -> dict[str, Any]:
        """Every namespace in the cache file, or ``{}`` only when there is none there.

        ``{}`` means this file holds nothing, true of a missing file and of an empty one,
        and both mutations rebuild the whole file from what this returns. Anything else
        (unreadable, not UTF-8, not JSON, not an object, larger than the ceiling) raises,
        since rebuilding from ``{}`` would discard every other namespace's token.
        """
        try:
            content = self._read_within_the_ceiling()
        except FileNotFoundError:
            return {}
        except ValueError as error:
            # ``UnicodeDecodeError`` is a ``ValueError``: bytes are there and they are
            # not this file's text. PowerShell's ``>`` writes UTF-16, for one.
            raise self._refuse_the_cache_file("is not UTF-8 text", error) from None
        except OSError as error:
            raise self._refuse_the_cache_file("could not be read", error) from None
        if not content.strip():
            return {}
        try:
            stored = json.loads(content)
        except (ValueError, RecursionError) as error:
            # ``RecursionError`` covers JSON nested past the interpreter's limit.
            raise self._refuse_the_cache_file("does not hold valid JSON", error) from None
        if not isinstance(stored, dict):
            raise self._refuse_the_cache_file(
                f"holds a JSON {type(stored).__name__} where an object of credential "
                f"namespaces was expected",
                None,
            )
        return stored

    def _read_within_the_ceiling(self) -> str:
        """The cache file's text, read one byte past :data:`MAX_TOKEN_CACHE_BYTES`.

        One byte past is enough to know the file is over the ceiling without holding the
        whole of it.
        """
        with self._path.open("rb") as handle:
            raw = handle.read(MAX_TOKEN_CACHE_BYTES + 1)
        if len(raw) > MAX_TOKEN_CACHE_BYTES:
            raise self._refuse_the_cache_file(
                f"is larger than the {MAX_TOKEN_CACHE_BYTES}-byte ceiling this SDK "
                f"reads it to, so it was not loaded",
                None,
            )
        # ``UnicodeDecodeError`` is a ``ValueError``, which the caller renders as the
        # "is not UTF-8 text" refusal.
        return raw.decode("utf-8")

    def _refuse_the_cache_file(
        self, problem: str, error: Exception | None
    ) -> SdkTokenCacheError:
        """The one refusal for a cache file that cannot be used.

        :return: the exception, for the caller to ``raise``, so the raise site reads as
            a raise and the traceback starts there.
        """
        native = ""
        if error is not None:
            # ``strerror`` before ``str`` for an ``OSError``: the latter repeats the
            # path, which is already in the message.
            native = f": {getattr(error, 'strerror', None) or error}"
        return SdkTokenCacheError(
            f"the token cache {problem}. It is not read as empty: this file is keyed "
            f"by credentials namespace and is meant to be shared, so rewriting it from "
            f"an empty snapshot would discard every other namespace in it. Repair or "
            f"move the file, or pass token_cache_path=None to keep the token in "
            f"memory. Path: {self._path}{native}"
        )

    @contextmanager
    def acquire_token_refresh_lock(self) -> Iterator[None]:
        """Serialise refreshes across threads and processes.

        Reentrant, like :meth:`MemoryTokenStore.acquire_token_refresh_lock`. The OS file
        lock is not: on Windows, ``msvcrt.locking`` on a handle this process already
        holds raises ``AlreadyLocked``, so the file lock is taken at the outermost level
        only, per cache path, and the depth counted on that path's
        :class:`_CachePathGuard`.

        It fails closed. With ``portalocker`` missing, a sidecar that cannot be opened,
        or a wait past :data:`_LOCK_TIMEOUT_SECONDS`, the block does not run: a lock only
        this process can see does not stop the process next to it.

        :raises SdkTokenLockError: there is no cross-process lock to hold. The first
            refusal in an unbroken run also logs and raises a
            :class:`DegradedTokenLockWarning`, so a caller who catches the exception
            broadly can still find out which of the three conditions it was.
        """
        with self._guard.lock:
            if self._guard.depth > 0:
                with self._nested_in_the_held_lock():
                    yield
                return

            try:
                import portalocker
            except ImportError:
                raise self._refuse_the_lock(
                    "portalocker is not installed, so there is no portable file lock "
                    "to take"
                ) from None

            try:
                self._lock_path.parent.mkdir(parents=True, exist_ok=True)
                lock_handle = open(self._lock_path, "a", encoding="utf-8")
            except OSError as error:
                # A cache directory this process cannot write to - a read-only
                # container filesystem, a service account with no access to
                # LOCALAPPDATA - has no sidecar to lock.
                raise self._refuse_the_lock(
                    f"the lock file {self._lock_path} could not be opened "
                    f"({error.strerror or error})"
                ) from None

            with lock_handle:
                if not self._lock_sidecar(lock_handle, portalocker):
                    raise self._refuse_the_lock(
                        f"another process held the lock for longer than "
                        f"{_LOCK_TIMEOUT_SECONDS}s"
                    )
                # Re-armed on every success, so a condition that comes back after a
                # recovery is announced again.
                self._guard.degradation_announced = False
                self._guard.depth += 1
                try:
                    yield
                finally:
                    self._guard.depth -= 1
                    portalocker.unlock(lock_handle)

    def _refuse_the_lock(self, reason: str) -> SdkTokenLockError:
        """Announce the degradation once per unbroken run, and return the refusal.

        :return: the exception, for the caller to ``raise``.
        """
        refusal = SdkTokenLockError(
            f"the token cache could not be locked across processes, so the operation "
            f"was refused rather than run without exclusion: {reason}. Two processes "
            f"sharing this file would otherwise write it at the same time and "
            f"overwrite each other's entry. Pass token_cache_path=None to keep the "
            f"token in memory, or point token_cache_path at a filesystem where "
            f"locking works. Path: {self._path}"
        )
        if self._guard.degradation_announced:
            return refusal
        _LOGGER.warning("%s", refusal.message)
        warnings.warn(refusal.message, DegradedTokenLockWarning, stacklevel=2)
        # Latched after the warning: under ``simplefilter("error", ...)`` the line above
        # raises, and latching first would leave every later refusal silent.
        self._guard.degradation_announced = True
        return refusal

    def _lock_sidecar(self, lock_handle: Any, portalocker: Any) -> bool:
        """Take the OS lock on the sidecar, giving up after a deadline.

        ``portalocker.lock`` accepts no timeout, so the deadline is polled with
        ``LOCK_NB``; the lock spans the whole token exchange, so a worker stopped at a
        breakpoint would otherwise stall every other process.

        :param portalocker: the imported module, passed in so the optional import stays
            in one place.
        :return: ``True`` once the lock is held, ``False`` if the deadline passed.
        """
        deadline = time.monotonic() + _LOCK_TIMEOUT_SECONDS
        while True:
            try:
                portalocker.lock(lock_handle, portalocker.LOCK_EX | portalocker.LOCK_NB)
                return True
            except portalocker.exceptions.BaseLockException:
                if time.monotonic() >= deadline:
                    return False
                time.sleep(_LOCK_POLL_SECONDS)

    @contextmanager
    def _nested_in_the_held_lock(self) -> Iterator[None]:
        """Count the nesting depth and yield, without taking the OS file lock again.

        Only for a nested acquisition, where an outer level on this same cache path
        already holds the file lock.
        """
        self._guard.depth += 1
        try:
            yield
        finally:
            self._guard.depth -= 1
