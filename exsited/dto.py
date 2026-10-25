"""The typed view over a body - what every DTO is built from."""

from __future__ import annotations

import re
import sys
import types
import typing
from types import MappingProxyType
from typing import Any, ClassVar, Mapping, TypeVar, get_args, get_origin, get_type_hints
from weakref import WeakKeyDictionary

from exsited.errors import SdkUsageError
from exsited.redaction import REDACTED, redact_snapshot, should_redact

__all__ = ["Dto"]

DtoSubclass = TypeVar("DtoSubclass", bound="Dto")

#: Class attributes that declare the shape rather than a field.
_DECLARATION_NAMES = ("ENVELOPE_KEY", "TOP_LEVEL")


class _Schema:
    """One DTO subclass's declaration, captured at class creation and kept off the class."""

    __slots__ = ("envelope_key", "top_level", "_declared", "_module", "_fields")

    def __init__(self, cls: type) -> None:
        self.envelope_key: str | None = getattr(cls, "ENVELOPE_KEY", None)
        self.top_level: tuple[str, ...] = tuple(getattr(cls, "TOP_LEVEL", ()) or ())
        # Base first, so a subclass's own annotation for a name wins.
        declared: dict[str, Any] = {}
        for base in reversed(cls.__mro__):
            declared.update(base.__dict__.get("__annotations__") or {})
        self._declared = declared
        self._module = cls.__module__
        self._fields: Mapping[str, Any] | None = None

    @property
    def fields(self) -> Mapping[str, Any]:
        """The canonical field-to-type mapping, resolved once; :meth:`Dto.fields` copies it."""
        if self._fields is None:
            self._fields = MappingProxyType(
                {
                    name: _unwrap_optional(annotation)
                    for name, annotation in self._resolve_declared().items()
                }
            )
        return self._fields

    def _resolve_declared(self) -> dict[str, Any]:
        """Resolve the captured annotation strings against the module that declared them."""
        declared = {
            name: annotation
            for name, annotation in self._declared.items()
            if not name.startswith("_")
            and name not in _DECLARATION_NAMES
            and not _declares_a_class_variable(annotation)
        }
        module = sys.modules.get(self._module)
        resolver = types.FunctionType(_EMPTY_CODE, getattr(module, "__dict__", {}) or {})
        resolver.__annotations__ = declared
        return get_type_hints(resolver, include_extras=False)


#: Anchored, so a type named ``ClassVariant`` stays a field; an aliased ``ClassVar`` is missed.
_CLASS_VAR_ANNOTATION = re.compile(r"^(?:typing\.)?ClassVar\s*(?:\[|$)")


def _declares_a_class_variable(annotation: Any) -> bool:
    """Whether one annotation says ``ClassVar``, declaring configuration rather than a field; a
    string is judged by its text, since resolving a ``ClassVar`` outside a class raises."""
    if isinstance(annotation, str):
        return _CLASS_VAR_ANNOTATION.match(annotation.strip()) is not None
    return typing.get_origin(annotation) is ClassVar


def _no_op() -> None:
    """The code object :meth:`_Schema._resolve_declared` borrows; never called."""


_EMPTY_CODE = _no_op.__code__

#: Weak, so a type made in a function is collectable; reached only through :func:`_schema_for`.
_SCHEMAS: "WeakKeyDictionary[type, _Schema]" = WeakKeyDictionary()


def _schema_for(cls: type) -> _Schema:
    """This type's frozen declaration, registered here if ``__init_subclass__`` never ran."""
    schema = _SCHEMAS.get(cls)
    if schema is None:
        schema = _Schema(cls)
        _SCHEMAS[cls] = schema
    return schema


def _unwrap_optional(annotation: Any) -> Any:
    """``X`` for an annotation written ``X | None``, else the annotation itself."""
    if get_origin(annotation) in (typing.Union, types.UnionType):
        rest = [arg for arg in get_args(annotation) if arg is not type(None)]
        if len(rest) == 1:
            return rest[0]
        return rest
    return annotation


class Dto:
    """Base for every typed view in this SDK."""

    ENVELOPE_KEY: ClassVar[str | None] = None
    TOP_LEVEL: ClassVar[tuple[str, ...]] = ()

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """Capture this subclass's declaration as the class is created, before anyone reaches it."""
        super().__init_subclass__(**kwargs)
        _SCHEMAS[cls] = _Schema(cls)

    @classmethod
    def fields(cls) -> Mapping[str, Any]:
        """This type's fields, in declaration order, mapped to the type each holds."""
        return MappingProxyType(dict(_schema_for(cls).fields))

    def __init__(self, **values: Any) -> None:
        """Build one, every field optional and anything not passed ``None``. An undeclared
        name is refused: absorbed, a typo would reach the application as a key it ignores."""
        fields = _schema_for(type(self)).fields
        unknown = sorted(set(values) - set(fields))
        if unknown:
            available = ", ".join(fields) or "no fields"
            raise SdkUsageError(
                f"{type(self).__name__} has no field {', '.join(unknown)}; it holds {available}"
            )
        for name in fields:
            setattr(self, name, values.get(name))

    @classmethod
    def from_map(cls: type[DtoSubclass], body: Mapping[str, Any]) -> DtoSubclass:
        """Read a decoded body - ``response.map``, or one record out of it - into this
        type, unwrapping :attr:`ENVELOPE_KEY` when present."""
        if not isinstance(body, Mapping):
            raise SdkUsageError(
                f"{cls.__name__}.from_map expects a decoded mapping body, got "
                f"{type(body).__name__} - a binary or empty body has no DTO"
            )

        schema = _schema_for(cls)
        source: dict[str, Any] = dict(body)
        if schema.envelope_key is not None:
            inner = source.get(schema.envelope_key)
            if isinstance(inner, Mapping):
                beside = {k: v for k, v in source.items() if k != schema.envelope_key}
                source = {**dict(inner), **beside}

        return cls(
            **{
                name: _read(source.get(name), declared)
                for name, declared in schema.fields.items()
                if name in source
            }
        )

    def to_map(self) -> dict[str, Any]:
        """Return the body this DTO stands for, envelope included."""
        schema = _schema_for(type(self))
        record: dict[str, Any] = {}
        beside: dict[str, Any] = {}
        for name in schema.fields:
            value = getattr(self, name, None)
            if value is None:
                continue
            (beside if name in schema.top_level else record)[name] = _write(value)

        body = {schema.envelope_key: record} if schema.envelope_key else dict(record)
        body.update(beside)
        return body

    def __eq__(self, other: Any) -> bool:
        """Equal when the same type carries the same field values."""
        if type(other) is not type(self):
            return NotImplemented
        return all(
            getattr(self, name, None) == getattr(other, name, None)
            for name in _schema_for(type(self)).fields
        )

    def __repr__(self) -> str:
        """A ``repr`` safe to print, secrets masked and unset fields omitted; an opaque value is
        summarised rather than rendered, so no caller ``__repr__`` runs."""
        shown = []
        for name in _schema_for(type(self)).fields:
            value = getattr(self, name, None)
            if value is None:
                continue
            rendered = repr(REDACTED) if should_redact(name) else _render_value(value)
            shown.append(f"{name}={rendered}")
        return f"{type(self).__name__}({', '.join(shown)})"


#: ``__init_subclass__`` fires for subclasses only, so the base registers its schema here.
_SCHEMAS[Dto] = _Schema(Dto)


def _render_value(value: Any) -> str:
    """One field value for :meth:`Dto.__repr__`; a nested DTO recurses, the rest is snapshotted."""
    if isinstance(value, Dto):
        return repr(value)
    if isinstance(value, list):
        return "[" + ", ".join(_render_value(item) for item in value) + "]"
    if isinstance(value, tuple):
        items = ", ".join(_render_value(item) for item in value)
        return f"({items},)" if len(value) == 1 else f"({items})"
    return repr(redact_snapshot(value))


def _read(value: Any, declared: Any) -> Any:
    """One value as its declared type, or ``None`` when it is not that type. Nothing is
    converted; the value is still in ``response.map``, untouched."""
    if value is None:
        return None

    origin = get_origin(declared)
    if origin in (list, tuple):
        if not isinstance(value, (list, tuple)):
            return None
        (item_type,) = get_args(declared) or (Any,)
        # Unwrapped as a field is, or an ``Address | None`` entry would never be an ``Address``.
        return [_read(item, _unwrap_optional(item_type)) for item in value]

    if origin in (dict, Mapping):
        # A JSON object's keys are strings, so only the value type is read.
        if not isinstance(value, Mapping):
            return None
        value_type = (get_args(declared) or (Any, Any))[-1]
        return {key: _read(item, _unwrap_optional(value_type)) for key, item in value.items()}

    if isinstance(declared, type) and issubclass(declared, Dto):
        return declared.from_map(value) if isinstance(value, Mapping) else None

    if declared is Any or isinstance(declared, list):
        return value

    if declared is float:
        # An integer is a float in JSON's number type; the one widening allowed.
        return (
            float(value)
            if isinstance(value, (int, float)) and not isinstance(value, bool)
            else None
        )
    if declared is int:
        return value if isinstance(value, int) and not isinstance(value, bool) else None
    if declared is bool:
        return value if isinstance(value, bool) else None

    # A generic with no reading rule is compared by its origin; one that is not a class passes.
    target = origin if origin is not None else declared
    if not isinstance(target, type):
        return value
    return value if isinstance(value, target) else None


def _write(value: Any) -> Any:
    """One value as the API receives it: a nested DTO becomes its record, a list is
    walked for nested DTOs, and everything else is itself."""
    if isinstance(value, Dto):
        record = value.to_map()
        # A nested DTO's own envelope would be a layer the application does not expect.
        envelope_key = _schema_for(type(value)).envelope_key
        return record[envelope_key] if envelope_key else record
    if isinstance(value, (list, tuple)):
        return [_write(item) for item in value]
    if isinstance(value, Mapping):
        return {key: _write(item) for key, item in value.items()}
    return value
