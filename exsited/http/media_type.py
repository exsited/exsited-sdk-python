"""``Content-Type`` validation: the RFC 9110 grammar and whether the label contradicts the body.
Unlike other header values, a ``Content-Type`` is echoed in refusals, bounded: it is a public
protocol label, and a refusal that hid it would not say which value was wrong."""

from __future__ import annotations

import re
import reprlib
from typing import Any

__all__ = [
    "CONTENT_TYPE_HEADER",
    "JSON_MEDIA_TYPE",
    "FORM_MEDIA_TYPE",
    "MULTIPART_MEDIA_TYPE",
    "is_media_type",
    "is_json_content_type",
    "media_type_of",
    "grammar_refusal",
    "body_conflict",
]

#: Header names are compared lowered.
CONTENT_TYPE_HEADER = "Content-Type"

JSON_MEDIA_TYPE = "application/json"
FORM_MEDIA_TYPE = "application/x-www-form-urlencoded"
MULTIPART_MEDIA_TYPE = "multipart/form-data"

#: RFC 6839 structured-suffix types such as ``application/problem+json`` are JSON too.
_JSON_SUFFIX = "+json"
_JSON_TREE = "application/"

#: RFC 9110 ``tchar`` spelled out, since ``\w`` would admit non-ASCII letters.
_TCHAR = r"[!#$%&'*+\-.^_`|~0-9A-Za-z]"
_TOKEN = f"{_TCHAR}+"
#: RFC 9110 ``quoted-string``; ``obs-text`` is U+0080-U+00FF, what latin-1 can carry.
_QUOTED_STRING = r'"(?:[\t \x21\x23-\x5B\x5D-\x7E\x80-\xFF]|\\[\t \x21-\x7E\x80-\xFF])*"'
_PARAMETER = f"{_TOKEN}=(?:{_TOKEN}|{_QUOTED_STRING})"
#: ``\Z``, not ``$``, which also matches before a trailing newline. An empty parameter
#: (``application/json;``) is refused, although RFC 9110 allows it.
_MEDIA_TYPE_PATTERN = re.compile(f"{_TOKEN}/{_TOKEN}(?:[ \t]*;[ \t]*{_PARAMETER})*\\Z")

#: The same bound :mod:`exsited.config.sdk_config` applies to the values it shows.
_BOUNDED_REPR = reprlib.Repr()
_BOUNDED_REPR.maxstring = 120
_BOUNDED_REPR.maxother = 120

_GRAMMAR_ADVICE = "type/subtype, optionally followed by '; parameter=value'"


def _bounded(value: Any) -> str:
    """``repr`` a value with its length bounded, for an error message."""
    return _BOUNDED_REPR.repr(value)


def is_media_type(value: Any) -> bool:
    """Whether ``value`` is an RFC 9110 media type. Whitespace is allowed only around a semicolon,
    since the value reaches the wire verbatim; case is not judged."""
    if not isinstance(value, str):
        return False
    return _MEDIA_TYPE_PATTERN.match(value) is not None


def media_type_of(value: str) -> str:
    """The lowered ``type/subtype`` of a valid ``Content-Type``, for comparison."""
    return value.split(";", 1)[0].strip().lower()


def grammar_refusal(where: str, value: Any) -> str:
    """The refusal for a ``Content-Type`` that is not a media type, shared by ``default_headers``
    and per-call ``headers``."""
    return (
        f"{where}: Content-Type must be a media type like 'application/json', got "
        f"{_bounded(value)} - {_GRAMMAR_ADVICE}"
    )


def body_conflict(
    value: str,
    where: str,
    *,
    has_json: bool,
    has_form: bool,
    has_files: bool,
) -> str | None:
    """Why this ``Content-Type`` cannot label the body the SDK encodes, or ``None``. A multipart
    body takes none, since the SDK writes the boundary; a form must be urlencoded; JSON must be a
    JSON type."""
    shown = _bounded(value)
    prefix = f"{where}: Content-Type {shown} cannot be sent with this request"
    media_type = media_type_of(value)

    if has_files:
        return (
            f"{prefix} - it sends files, so the body is multipart and the encoder "
            f"generates the boundary parameter that frames it. No Content-Type set "
            f"here can carry that boundary, so the server would be unable to parse "
            f"the body at all. Leave it unset and the SDK sets it, boundary included"
        )
    if has_form and media_type != FORM_MEDIA_TYPE:
        return (
            f"{prefix} - it sends form_data, which goes on the wire as "
            f"{FORM_MEDIA_TYPE}, so the body would be labelled as something it is "
            f"not. Send {FORM_MEDIA_TYPE}, or leave it unset and the SDK sets it"
        )
    if has_json and not _is_json_media_type(media_type):
        return (
            f"{prefix} - it sends json_body, which goes on the wire as "
            f"{JSON_MEDIA_TYPE}, so the body would be labelled as something it is "
            f"not. Send {JSON_MEDIA_TYPE}, or a vendor JSON type such as "
            f"application/vnd.api+json, or leave it unset and the SDK sets it"
        )
    return None


def is_json_content_type(content_type: Any) -> bool:
    """Whether a raw ``Content-Type`` labels a JSON body; ``False`` for anything not text."""
    if not isinstance(content_type, str):
        return False
    return _is_json_media_type(media_type_of(content_type))


def _is_json_media_type(media_type: str) -> bool:
    """``application/json`` or an ``application/...+json`` type; ``text/json`` is not one."""
    if media_type == JSON_MEDIA_TYPE:
        return True
    return (
        media_type.startswith(_JSON_TREE)
        and media_type.endswith(_JSON_SUFFIX)
        # ``application/+json`` has no subtype prefix, so it names nothing.
        and len(media_type) > len(_JSON_TREE) + len(_JSON_SUFFIX)
    )
