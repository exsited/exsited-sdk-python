"""Who you are and which instance you are talking to.

Only the credentials and where the resulting token is kept, so a credentials file
contains nothing but credentials; how the SDK *behaves* is
:class:`~exsited.config.sdk_config.SdkConfig`. See :class:`AuthConfig` for the
fields and an example.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, fields, replace
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from exsited.auth.token_store import (
    DEFAULT_TOKEN_CACHE_FILENAME,
    build_default_token_cache_path,
)
from exsited.errors import SdkConfigError
from exsited.redaction import redact_fields

DEFAULT_CLIENT_NAME = "default"
DEFAULT_GRANT_TYPE = "client_credentials"

REQUIRED_FIELDS = (
    "base_url",
    "client_id",
    "client_secret",
    "redirect_uri",
)

#: Every field that must be text, in declaration order so the batched report reads
#: top to bottom. All six reach the token-request body or the cache namespace,
#: which apply JSON encoding or ``len()`` to whatever arrives.
_TEXT_FIELDS = REQUIRED_FIELDS + ("client_name", "grant_type")


class _UseDefaultTokenCache:
    """Sentinel: resolve the platform's per-user cache path."""

    def __repr__(self) -> str:
        return "<platform default>"


#: Default for ``token_cache_path``: the token is cached in the platform's per-user
#: directory. Pass a path to move it, or ``None`` to keep it in memory only.
USE_DEFAULT_TOKEN_CACHE = _UseDefaultTokenCache()


@dataclass(frozen=True, repr=False)
class AuthConfig:
    """Credentials for one Exsited instance.

    Frozen and validated at construction; ``client_secret`` is redacted by ``repr``
    and ``str``, so an instance is safe to log.

    Four credentials, the four the token endpoint takes.

    :ivar base_url: instance URL, e.g.
        ``https://your-instance.myexsited.com``. Needs an ``http://`` or
        ``https://`` scheme and a host; a trailing ``/`` is stripped. An optional
        base path is allowed (for an instance mounted under a sub-path, e.g.
        ``https://host/store``), but a query string, a fragment or
        ``user:password@`` userinfo is refused, the last because ``requests`` turns
        it into a ``Basic`` header that replaces the bearer token. An explicit port
        is checked too.
    :ivar client_id: OAuth2 client id.
    :ivar client_secret: OAuth2 client secret. Redacted in ``repr``.
    :ivar redirect_uri: OAuth2 redirect uri; sent in the ``client_credentials``
        token request body, and omitted from the ``refresh_token`` one, which does
        not take it.
    :ivar client_name: label for this instance. Shown in logs and printed
        output, and how the instance is selected by name. Required: with several
        instances registered, two entries sharing an implicit name would collide.
    :ivar grant_type: sent as ``grant_type`` in the token request. Default
        ``"client_credentials"``, the value this API expects.
    :ivar token_cache_path: where the access and refresh tokens are cached.
        Defaults to the platform's per-user cache directory, so nothing lands in
        your working directory: ``%LOCALAPPDATA%\\exsited\\`` on Windows,
        ``~/Library/Caches/exsited/`` on macOS, else
        ``$XDG_CACHE_HOME/exsited/`` falling back to ``~/.cache/exsited/``.
        Pass a path to move it, or ``None`` to keep the token in memory for the life
        of the process. A blank string is refused rather than read as ``None``,
        since that is how an unset environment variable arrives, and so is an
        existing directory, where no write can land.

        An ``os.PathLike`` is decoded to text at construction, so the path validated
        here is the path written to; see :func:`_snapshot_path`.
        ``Path(config.token_cache_path)`` recovers a ``Path``.

        One path is safe to share between instances: entries are keyed by a
        fingerprint of ``base_url``, ``client_id``, ``client_secret`` and
        ``grant_type``, so identical credentials authenticate once between them, any
        difference gets its own entry, and two operators sharing one OAuth2 client
        are never handed each other's token.

    Example::

        AuthConfig(
            client_name="default",
            base_url=os.getenv("EXSITED_BASE_URL"),
            client_id=os.getenv("EXSITED_CLIENT_ID"),
            client_secret=os.getenv("EXSITED_CLIENT_SECRET"),
            redirect_uri=os.getenv("EXSITED_REDIRECT_URI"),
        )
    """

    base_url: str
    client_id: str
    client_secret: str
    redirect_uri: str
    # Required. ``DEFAULT_CLIENT_NAME`` is the implicit name only of a mapping block
    # that omits the key; see :func:`~exsited.config.sdk_config.read_client_name`.
    client_name: str

    grant_type: str = DEFAULT_GRANT_TYPE
    token_cache_path: Any = USE_DEFAULT_TOKEN_CACHE

    def __post_init__(self) -> None:
        object.__setattr__(self, "base_url", _normalise_base_url(self.base_url))
        # Before validation, and exactly once. See :func:`_snapshot_path`.
        object.__setattr__(
            self, "token_cache_path", _snapshot_path(self.token_cache_path)
        )
        # Validated before the sentinel is resolved: resolving it creates and chmods
        # a directory, which a config with no credentials should not leave behind.
        self._validate()
        if isinstance(self.token_cache_path, _UseDefaultTokenCache):
            try:
                resolved = build_default_token_cache_path(DEFAULT_TOKEN_CACHE_FILENAME)
            except OSError as error:
                # ``%LOCALAPPDATA%`` pointing at a regular file raises
                # ``FileExistsError``, which ``except SdkError`` does not catch.
                raise SdkConfigError(
                    f"instance {self.client_name}: token_cache_path: the default "
                    f"cache directory could not be created ({error}); pass a path, "
                    f"or None to keep the token in memory"
                ) from error
            object.__setattr__(self, "token_cache_path", resolved)

    def _validate(self) -> None:
        problems: list[str] = []

        # Types before values, and a mistyped field skips its value checks: a YAML
        # ``client_id: 12345`` would reach ``len(value)`` in
        # ``build_credentials_namespace``. A value is described by its type and never
        # echoed, since ``client_secret`` passes through here; ``None`` is left to the
        # blank checks below.
        mistyped: set[str] = set()
        for name in _TEXT_FIELDS:
            value = getattr(self, name, None)
            if value is not None and not isinstance(value, str):
                mistyped.add(name)
                problems.append(
                    f"{name}: expected a string, got {type(value).__name__}"
                )

        missing = [
            name
            for name in REQUIRED_FIELDS
            if name not in mistyped and not str(getattr(self, name, "") or "").strip()
        ]
        if missing:
            problems.append("missing required values: " + ", ".join(missing))

        if self.base_url and "base_url" not in mistyped:
            problems.extend(_problems_with_the_base_url(self.base_url))

        for name in ("client_name", "grant_type"):
            if name not in mistyped and not str(getattr(self, name) or "").strip():
                problems.append(f"{name}: must not be blank")

        # The field stays annotated ``Any`` - a Union errors under ``mypy --strict``
        # at every consumer - so this runtime check is where the contract lives.
        if not isinstance(
            self.token_cache_path, (str, os.PathLike, _UseDefaultTokenCache, type(None))
        ):
            problems.append(
                f"token_cache_path: expected a path or None, "
                f"got {self.token_cache_path!r}"
            )
        elif isinstance(self.token_cache_path, str) and not self.token_cache_path.strip():
            # Falsy, so ``if config.token_cache_path`` would choose MemoryTokenStore
            # and write nothing - what ``None`` is reserved for.
            # ``os.getenv("EXSITED_TOKEN_CACHE", "")`` is how an unset variable arrives.
            problems.append(
                "token_cache_path: must not be blank - pass None to keep the "
                "token in memory, or a path to cache it"
            )
        elif isinstance(self.token_cache_path, (str, os.PathLike)) and Path(
            self.token_cache_path
        ).is_dir():
            # Truthy, so FileTokenStore is chosen and every write then fails, which
            # ``TokenProvider`` swallows - one authentication per call. ``Path("")``
            # lands here, normalising to ``.``.
            problems.append(
                f"token_cache_path: {os.fspath(self.token_cache_path)!r} is an "
                f"existing directory, so nothing could be written to it - pass the "
                f"file to write, or None to keep the token in memory"
            )

        if problems:
            # Stripped: a whitespace-only name would label the report ``instance   :``.
            # Wrapped in ``str``, since a mistyped name reaches here too.
            label = str(self.client_name or "").strip() or "<unnamed>"
            raise SdkConfigError(f"instance {label}: " + "; ".join(problems))

    def with_overrides(self, **changes: Any) -> "AuthConfig":
        """Derive a new set of credentials from this one.

        :return: a new validated instance. This one is untouched.
        :raises SdkConfigError: an unknown field, or the result would be invalid.
        """
        unknown = set(changes) - {field.name for field in fields(self)}
        if unknown:
            raise SdkConfigError(f"unknown auth field(s): {', '.join(sorted(unknown))}")
        return replace(self, **changes)

    def __repr__(self) -> str:
        """Return a ``repr`` with credentials redacted, safe for logs and tracebacks."""
        shown = redact_fields(self, [field.name for field in fields(self)])
        return f"AuthConfig({', '.join(shown)})"

    __str__ = __repr__


def _snapshot_path(value: Any) -> Any:
    """Decode an ``os.PathLike`` to text once, so the stored path cannot change.

    An ``os.PathLike`` answers ``__fspath__`` afresh on every call, so kept as the
    object it could name one file to validation and another to
    :class:`~exsited.auth.token_store.FileTokenStore`.

    :return: the decoded text for a ``PathLike``; anything else (a ``str``, the
        sentinel, ``None``, or a wrong type) handed straight back for
        :meth:`AuthConfig._validate` to judge.
    """
    if not isinstance(value, os.PathLike):
        return value
    try:
        return os.fsdecode(value)
    except (TypeError, ValueError):
        # A ``__fspath__`` that answers with the wrong type. Handed back so the
        # type check below reports it rather than this raising mid-construction.
        return value


def _normalise_base_url(raw_value: Any) -> Any:
    """Trim a base URL, handing a value of the wrong type straight back.

    Not coerced, so :meth:`AuthConfig._validate` can report the type as an
    ``SdkConfigError`` rather than ``.strip()`` raising before validation runs.

    :return: the trimmed URL, or ``raw_value`` unchanged.
    """
    if not isinstance(raw_value, str):
        return raw_value
    return raw_value.strip().rstrip("/")


def _problems_with_the_base_url(base_url: str) -> list[str]:
    """Report every way a syntactically-present base URL is still unusable.

    :param base_url: the normalised, non-empty value.
    :return: the problems found, for the batched report.
    """
    try:
        parsed = urlparse(base_url)
    except ValueError as error:
        # ``Invalid IPv6 URL`` on an unclosed bracket: a malformed URL has to be a
        # config error, not the ``ValueError`` urllib raises.
        return [f"base_url: is not a URL ({error})"]
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        return [
            f"base_url: must start with http:// or https:// and include "
            f"a host, got {base_url!r}"
        ]
    problems = []
    if parsed.username is not None or parsed.password is not None:
        # ``requests`` turns userinfo into an ``Authorization: Basic`` header that
        # *replaces* the bearer token. The value is not echoed: it holds a password.
        problems.append(
            f"base_url: host {parsed.hostname} carries embedded credentials, which "
            f"would replace the bearer token; strip the userinfo"
        )
    problems.extend(_problems_with_the_port(parsed))
    if parsed.query or parsed.fragment or parsed.params:
        # Paths are appended by concatenation, so anything after the host puts the
        # path inside the query - ``https://host?a=1/api/v4/...`` - and every call
        # 404s with nothing pointing at base_url.
        problems.append(
            "base_url: must be the instance origin only, with no query string or "
            f"fragment, got {base_url!r}"
        )
    return problems


def _problems_with_the_port(parsed: Any) -> list[str]:
    """Report a port that is not one, for the batched report.

    ``urlparse`` accepts ``https://host:abc`` and ``https://host:99999`` and raises
    only when ``.port`` is read; unread here, a bad port would surface later as a
    ``NETWORK`` error naming the connection rather than the configuration.

    :param parsed: the ``urlparse`` result for the base URL.
    :return: at most one problem; empty when the URL names no port or a valid one.
    """
    try:
        port = parsed.port
    except ValueError as error:
        # The parser's own text, since it distinguishes a port that is not a number
        # from one that is out of range, and both spell the same operator mistake.
        return [
            f"base_url: {parsed.netloc!r} does not name a usable port ({error}); "
            f"a port is a number from 1 to 65535"
        ]
    if port is not None and not 1 <= port <= 65535:
        # Only ``:0`` reaches here: ``.port`` raises for everything else out of
        # range. It parses, and it is not a port anything can be reached on.
        return [
            f"base_url: port {port} is not a port that can be connected to; "
            f"a port is a number from 1 to 65535"
        ]
    return []
