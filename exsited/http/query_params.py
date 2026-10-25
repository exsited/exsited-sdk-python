"""Query parameter normalisation, and the v4 filter and sort spellings."""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, Iterable, Mapping, Sequence

from exsited.errors import SdkUsageError
from exsited.redaction import MAX_REDACTION_DEPTH

#: One materialised query: ``(name, value)`` pairs in wire order, each part ``str`` or ``bytes``.
QueryPairs = tuple[tuple[str, "str | bytes"], ...]


__all__ = [
    "QueryPairs",
    "SortDirection",
    "FILTER_OPERATORS",
    "PRESENCE_OPERATORS",
    "LIST_OPERATORS",
    "build_query_params",
    "materialise_query_params",
    "group_query_pairs",
    "filter_param",
    "filter_values",
    "sort_param",
]


class SortDirection(str, Enum):
    """Sort direction for a v4 ``sort`` value built by :func:`sort_param`, ``-`` meaning
    descending; v4 has no ``direction`` parameter, and one sent is ignored."""

    ASC = "asc"
    DESC = "desc"


#: Every operator v4 spells into a filter name; ``eq`` has no suffix.
FILTER_OPERATORS = (
    "eq",
    "neq",
    "in",
    "nin",
    "contains",
    "not_contains",
    "starts_with",
    "gt",
    "gte",
    "lt",
    "lte",
    "has_value",
    "does_not_have_value",
)

#: Operators that read no value: pair the name with ``True``, never ``None``.
PRESENCE_OPERATORS = frozenset({"has_value", "does_not_have_value"})

#: Operators whose value is one comma separated list, built by :func:`filter_values`.
LIST_OPERATORS = frozenset({"in", "nin"})

_FILTER_PREFIX = "filter"


def filter_param(field: str, operator: str = "eq", *, prefix: str = _FILTER_PREFIX) -> str:
    """The query parameter name for one v4 filter: ``filter_<field>`` for equality and
    ``filter_<field>_<operator>`` otherwise. Only the operator is checked; whether a field's
    type takes it is the API's to answer, with a ``400`` naming the allowed operators."""
    if not isinstance(field, str) or not field.strip():
        raise SdkUsageError(f"filter field: expected a field name like 'status', got {field!r}")
    if operator not in FILTER_OPERATORS:
        raise SdkUsageError(
            f"filter operator {operator!r}: expected one of {', '.join(FILTER_OPERATORS)}"
        )
    stem = f"{prefix}_{field.strip()}"
    return stem if operator == "eq" else f"{stem}_{operator}"


def filter_values(values: Iterable[Any]) -> str:
    """The value of an ``in`` or ``nin`` filter: members comma separated in one key, since a list
    would repeat the key, which v4 answers ``200`` with the wrong rows. A member holding a comma,
    a ``None`` member, a set and an empty list are refused."""
    if isinstance(values, (str, bytes, bytearray)) or not isinstance(values, Iterable):
        raise SdkUsageError(
            f"filter values: expected a list of values like ['ACTIVE', 'INACTIVE'], "
            f"got {type(values).__name__}"
        )
    if isinstance(values, (set, frozenset)):
        raise SdkUsageError(
            "filter values: a set has no order, so the value it produces changes "
            "between runs; pass a list or a tuple in the order the values should "
            "be sent"
        )

    rendered: list[str] = []
    for value in values:
        if value is None:
            raise SdkUsageError(
                "filter values: a member is None, which has no value to match; "
                "drop it, or use the 'does_not_have_value' operator if what was "
                "meant is 'this field is unset'"
            )
        if isinstance(value, Iterable) and not isinstance(value, (str, bytes, bytearray)):
            raise SdkUsageError(
                "filter values: a member is itself a sequence; this builds one "
                "comma separated value, so flatten it to a list of scalars"
            )
        text = _normalise_query_value(value, "filter values", set(), 1)
        text = text if isinstance(text, str) else str(text)
        if "," in text:
            raise SdkUsageError(
                "filter values: a member contains a comma, which the API reads as "
                "the separator between two values, so it would match something "
                "other than what was asked for",
                detail=f"the member is {text!r}",
            )
        rendered.append(text)

    if not rendered:
        raise SdkUsageError(
            "filter values: expected at least one value; an empty 'in' filter is "
            "sent as 'filter_<field>_in=' and answered 200 with no rows, which "
            "reads as 'nothing matched' rather than as the mistake it is"
        )
    return ",".join(rendered)


def sort_param(field: str, direction: SortDirection | str = SortDirection.ASC) -> str:
    """A v4 ``sort`` value: the field, prefixed with ``-`` for a descending sort."""
    if not isinstance(field, str) or not field.strip():
        raise SdkUsageError(f"sort field: expected a field name like 'created_on', got {field!r}")
    resolved = direction.value if isinstance(direction, SortDirection) else direction
    if resolved not in (SortDirection.ASC.value, SortDirection.DESC.value):
        raise SdkUsageError(
            f"sort direction {direction!r}: expected "
            f"{SortDirection.ASC.value!r} or {SortDirection.DESC.value!r}"
        )
    field = field.strip()
    return field if resolved == SortDirection.ASC.value else f"-{field}"


def build_query_params(params: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Normalise query parameter values for the wire; keys pass through untouched."""
    if params is None:
        return {}
    if not isinstance(params, Mapping):
        # A list value already repeats the key, so point there rather than accept a second shape.
        raise SdkUsageError(
            f"query params: expected a mapping of names to values, got "
            f"{type(params).__name__}; to send one name twice give it a list, as "
            f"in {{'limit': [5, 6]}}"
        )

    normalised: dict[str, Any] = {}
    for key, value in params.items():
        if value is None:
            continue
        normalised[key] = _normalise_query_value(value, key, set(), 0)
    return normalised


def _normalise_query_value(value: Any, key: str, seen: set[int], depth: int) -> Any:
    """Normalise one value, rejecting a nested mapping at whatever depth it sits, since
    ``requests`` encodes one inside a list as its first *key*."""
    if depth >= MAX_REDACTION_DEPTH:
        raise SdkUsageError(
            f"query param {key!r}: nested more than {MAX_REDACTION_DEPTH} levels "
            f"deep, which is too deep to encode in a query string"
        )
    if isinstance(value, Mapping):
        raise SdkUsageError(
            f"query param {key!r}: nested objects cannot be encoded in a query "
            f"string; flatten it or send it in the body"
        )
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, Enum):
        return _normalise_query_value(value.value, key, seen, depth)
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, (set, frozenset)):
        # No order, so the query string it produces would change between runs.
        raise SdkUsageError(
            f"query param {key!r}: a set has no order, so the query string it "
            f"produces changes between runs; pass a list or a tuple in the order "
            f"the values should be sent"
        )
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes, bytearray)):
        # Any iterable: a generator drained by the first attempt would leave a retry without it.
        if id(value) in seen:
            raise SdkUsageError(
                f"query param {key!r}: the value refers to itself, so it has no "
                f"finite query-string encoding"
            )
        if depth >= 1:
            # ``requests`` would flatten one level, sending a request other than the one described.
            raise SdkUsageError(
                f"query param {key!r}: a sequence inside a sequence has no "
                f"query-string encoding; flatten it to one list of scalars"
            )
        return [
            _normalise_query_value(entry, key, seen | {id(value)}, depth + 1)
            for entry in value
            if entry is not None
        ]
    return value


def materialise_query_params(params: Any) -> QueryPairs:
    """Freeze a normalised query into the wire pairs, from a mapping or already-made pairs."""
    if not params:
        return ()
    pairs: list[tuple[str, str | bytes]] = []
    for name, value in _query_entries(params):
        rendered = _wire_text(name)
        values = (
            [value]
            if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Iterable)
            else list(value)
        )
        for item in values:
            if item is None:
                continue
            pairs.append((rendered, _wire_value(item)))
    return tuple(pairs)


def group_query_pairs(pairs: QueryPairs) -> dict[str, Any]:
    """The materialised pairs as the mapping a request record reports: one entry per name, a
    repeated name collecting its values into a list. The wire order is kept."""
    grouped: dict[str, Any] = {}
    for name, value in pairs:
        if name not in grouped:
            grouped[name] = value
            continue
        held = grouped[name]
        grouped[name] = [*held, value] if isinstance(held, list) else [held, value]
    return grouped


def _query_entries(params: Any) -> list[tuple[Any, Any]]:
    if isinstance(params, Mapping):
        return list(params.items())
    if isinstance(params, Sequence) and not isinstance(params, (str, bytes, bytearray)):
        return [
            (entry[0], entry[1])
            for entry in params
            if isinstance(entry, (tuple, list)) and len(entry) == 2
        ]
    raise SdkUsageError(
        f"query params: expected a mapping of names to values or a sequence of "
        f"(name, value) pairs, got {type(params).__name__}"
    )


def _wire_text(value: Any) -> str:
    """One name as its wire text, ``bytes`` decoded with a lossless fallback."""
    if isinstance(value, (bytes, bytearray)):
        return bytes(value).decode("utf-8", "surrogateescape")
    return value if isinstance(value, str) else str(value)


def _wire_value(value: Any) -> str | bytes:
    """One value as wire ``str`` or ``bytes``; the one place a caller's object gives its text."""
    if isinstance(value, bytes):
        return value
    if isinstance(value, bytearray):
        return bytes(value)
    return value if isinstance(value, str) else str(value)
