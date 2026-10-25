"""Several instances open at once, one cached authenticated client each; most callers want
:func:`~exsited.client.exsited_client.build_client` instead."""

from __future__ import annotations

import copy
import re
import threading
from typing import Any, Mapping, Sequence

from exsited.client.exsited_client import ExsitedClient
from exsited.config.auth_config import DEFAULT_CLIENT_NAME
from exsited.config.sdk_config import SdkConfig, read_client_name
from exsited.errors import SdkError, SdkUsageError

#: The label an unnamed entry is listed under, refused as a name so it is never ambiguous.
_INDEX_LABEL_PATTERN = re.compile(r"<index \d+>")


def _read_instance_blocks(credentials: Any, entry_point: str) -> list[Any]:
    """Validate the shape of a credentials argument and return it as a list; a single
    mapping is refused explicitly, since ``list()`` would iterate its *keys*."""
    if isinstance(credentials, (Mapping, str, bytes)):
        raise SdkUsageError(
            f"{entry_point} takes a list of instances, not a single "
            f"{type(credentials).__name__}; wrap the single block in a list: "
            f"{entry_point}([block])"
        )
    try:
        blocks = list(credentials)
    except TypeError:
        raise SdkUsageError(
            f"{entry_point} takes a list of instances; {type(credentials).__name__} is not iterable"
        ) from None
    if not blocks:
        raise SdkUsageError(f"{entry_point} needs at least one credentials block")
    return blocks


def _index_declared_names(blocks: Sequence[Any]) -> dict[str, int]:
    """Map each declared ``client_name`` to its position, rejecting collisions; a ``"default"``
    spelled out beside an unnamed entry would make two selectors differ."""
    declared: dict[str, int] = {}
    unnamed: int | None = None
    for index, block in enumerate(blocks):
        name = read_client_name(block)
        if name is None:
            if unnamed is None:
                unnamed = index
            continue
        if name in declared:
            raise SdkUsageError(_describe_name_collision(name, declared[name], index))
        declared[name] = index

    if unnamed is not None and DEFAULT_CLIENT_NAME in declared:
        positions = sorted((unnamed, declared[DEFAULT_CLIENT_NAME]))
        raise SdkUsageError(
            _describe_name_collision(DEFAULT_CLIENT_NAME, *positions, implicit=True)
        )
    return declared


def _describe_name_collision(name: str, first: int, second: int, *, implicit: bool = False) -> str:
    note = f"; an entry that omits client_name is named {DEFAULT_CLIENT_NAME!r}" if implicit else ""
    return (
        f"two instances share client_name {name!r} (positions {first} and "
        f"{second}){note}; names must be unique so one can be told from the other"
    )


def _copy_blocks(blocks: Sequence[Any]) -> list[Any]:
    """Copy a block list so a caller cannot edit a registration through it."""
    return [copy.deepcopy(block) if isinstance(block, Mapping) else block for block in blocks]


class ClientRegistry:
    """A collection of clients, one per instance, built on first use. The first credential block
    is the default; mapping blocks are copied, so later edits change nothing here."""

    def __init__(self, credentials: Sequence[Any]) -> None:
        # Copied now: a client is built on first use, and must match the label listed for it.
        blocks = _copy_blocks(_read_instance_blocks(credentials, "ClientRegistry"))
        self._credentials = blocks
        self._names = _index_declared_names(blocks)
        # Recorded once, so the listing cannot disagree with what ``resolve_index`` accepts.
        self._labels = [
            read_client_name(block) or f"<index {index}>" for index, block in enumerate(blocks)
        ]
        self._clients: dict[int, ExsitedClient] = {}
        self._supplied: set[int] = set()
        self._lock = threading.Lock()

    def resolve_index(self, name: int | str | None = None) -> int:
        """Turn a selector into a position: ``None`` for the first entry, an ``int``
        position, or a ``str`` matching an entry's ``client_name``."""
        if name is None:
            return 0
        if isinstance(name, int) and not isinstance(name, bool):
            if -len(self._credentials) <= name < len(self._credentials):
                return name % len(self._credentials)
            raise SdkUsageError(
                f"no instance at index {name}; {len(self._credentials)} "
                f"registered (0-{len(self._credentials) - 1})"
            )
        if name in self._names:
            return self._names[name]
        available = ", ".join(self.list_client_names())
        raise SdkUsageError(f"unknown instance {name!r}; registered: {available}")

    def get_client(self, name: int | str | None = None) -> ExsitedClient:
        """A client, built on first use; the selector is as :meth:`resolve_index` takes it."""
        index = self.resolve_index(name)
        with self._lock:
            client = self._clients.get(index)
            if client is None:
                config = SdkConfig.from_credentials(self._credentials, index)
                client = ExsitedClient(config)
                self._clients[index] = client
            return client

    def add_client(self, name: str, client: ExsitedClient) -> None:
        """Register a pre-built client under a name - a non-blank string that is not an
        ``<index n>`` position label. The registry never closes what it did not build."""
        if not isinstance(name, str) or not name.strip():
            raise SdkUsageError(
                f"add_client needs a non-blank str name; got {name!r}. Anything "
                f"else cannot be passed back to get_client - an int selects a "
                f"position, so it would never reach the client at all"
            )
        if _INDEX_LABEL_PATTERN.fullmatch(name):
            raise SdkUsageError(
                f"{name!r} is the label an entry with no client_name already "
                f"carries; pick a name that cannot collide with a position"
            )
        with self._lock:
            # ``self._labels`` is checked as well because the two are built apart.
            if name in self._names or name in self._labels:
                raise SdkUsageError(f"instance {name!r} is already registered")
            self._credentials.append(client.config)
            index = len(self._credentials) - 1
            self._names[name] = index
            self._labels.append(name)
            self._clients[index] = client
            self._supplied.add(index)

    def list_client_names(self) -> tuple[str, ...]:
        """One label per registered instance, default first; an entry without a ``client_name`` is
        ``<index n>``, lining up with the positions :meth:`get_client` accepts."""
        return tuple(self._labels)

    def close_all_clients(self) -> None:
        """Close every client this registry built, not one handed in by :meth:`add_client`; each
        is attempted and all are dropped, so one failure leaks nothing behind it."""
        with self._lock:
            built = [index for index in sorted(self._clients) if index not in self._supplied]
            failures: list[str] = []
            first: Exception | None = None
            try:
                for index in built:
                    try:
                        self._clients[index].close_client()
                    except Exception as failure:
                        label = self._labels[index]
                        failures.append(f"{label}: {type(failure).__name__}: {failure}")
                        if first is None:
                            first = failure
            finally:
                for index in built:
                    self._clients.pop(index, None)

        if first is not None:
            raise SdkError(
                f"{len(failures)} of {len(built)} clients failed to close "
                f"({'; '.join(failures)}); all of them were attempted and "
                f"dropped, so the registry is usable again"
            ) from first

    def __enter__(self) -> "ClientRegistry":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close_all_clients()


_registered_instances: list[Any] = []
_registration_lock = threading.Lock()


def register_instances(credentials: Sequence[Any]) -> None:
    """Register every instance this process can talk to, as :class:`ClientRegistry` takes them;
    the first is the default, and mapping blocks are copied."""
    blocks = _read_instance_blocks(credentials, "register_instances")
    _index_declared_names(blocks)

    with _registration_lock:
        _registered_instances.clear()
        _registered_instances.extend(_copy_blocks(blocks))


def get_registered_instances() -> list[Any]:
    """Return the list :func:`register_instances` was given, first entry the default, as a
    fresh list, so normalising what you get back cannot rewrite the registration."""
    with _registration_lock:
        if not _registered_instances:
            raise SdkUsageError(
                "no instances registered - call register_instances([...]) first, "
                "or pass credentials= to build_client()"
            )
        return _copy_blocks(_registered_instances)


def list_instance_names() -> tuple[str, ...]:
    """Return one label per registered instance, default first; an entry without a
    ``client_name`` appears as ``<index n>``."""
    return tuple(
        read_client_name(block) or f"<index {index}>"
        for index, block in enumerate(get_registered_instances())
    )
