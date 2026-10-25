"""Secret handling - the single place that decides what counts as a secret."""

from __future__ import annotations

import copy
import json
import re
from typing import Any, Mapping
from urllib.parse import unquote_plus, urlsplit, urlunsplit

__all__ = [
    "REDACTED",
    "TOO_DEEP",
    "CIRCULAR",
    "MAX_REDACTION_DEPTH",
    "SENSITIVE_KEY_MARKERS",
    "should_redact",
    "redact_value",
    "redact_snapshot",
    "redact_mapping",
    "redact_text",
]

#: What a redacted value is replaced with.
REDACTED = "***"

#: What replaces a structure nested deeper than :data:`MAX_REDACTION_DEPTH`.
TOO_DEEP = "<...>"

#: What replaces a container that contains itself.
CIRCULAR = "<circular>"

#: How deep :func:`redact_value` walks before writing :data:`TOO_DEEP` instead.
MAX_REDACTION_DEPTH = 64

#: A key is secret when its name contains one of these, ignoring case and separators.
SENSITIVE_KEY_MARKERS = (
    "secret",
    "password",
    "passphrase",
    "passwd",
    "pwd",
    "token",
    "bearer",
    "jwt",
    "authorization",
    "authstring",
    "apikey",
    "assertion",
    "credential",
    # PKCE: ``code_verifier`` is a credential for the length of one exchange.
    "verifier",
    # Response-side names, which arrive from the server rather than from a payload.
    "cookie",
    "session",
    "signature",
    "privatekey",
    # Payment instruments a billing API's bodies carry. Not bare ``accountnumber``: this
    # API's ``account_number`` is the Exsited account identifier a caller has to read.
    "cardnumber",
    "cvv",
    "cvc",
    "iban",
    "bankaccountnumber",
)

#: Trailing words meaning a field describes a secret, e.g. ``passwordChangedAt``. Kept short:
#: under-redaction leaks, where over-redaction only costs readability.
_NON_SECRET_TAIL_WORDS = frozenset(
    {
        "amount",
        "at",
        "consent",
        "count",
        "duration",
        # ``customer_password_expired`` is a boolean on every detail record.
        "expired",
        "level",
        # A path *names* where a secret is kept: ``tokencachepath``.
        "path",
        "policy",
        "remaining",
        "status",
        "type",
    }
)

#: Leading words for a boolean about a secret; whole words, so ``hashedPassword`` stays redacted.
_NON_SECRET_LEAD_WORDS = frozenset({"has", "is", "was"})

#: Splits a name at punctuation and at camel-case humps.
_KEY_WORD_BOUNDARY = re.compile(r"[^A-Za-z0-9]+|(?<=[a-z0-9])(?=[A-Z])")


def _key_words(key: Any) -> list[str]:
    return [word.lower() for word in _KEY_WORD_BOUNDARY.split(str(key)) if word]


#: The markers as one separator-free word each, so the scan is a substring test.
_NORMALISED_MARKERS = tuple({"".join(_key_words(marker)) for marker in SENSITIVE_KEY_MARKERS})


def should_redact(key: str) -> bool:
    """Whether a key's name means its value must not be shown - ``"client_secret"`` and
    ``"X-Auth-Token"`` yes, ``"passwordChangedAt"`` no."""
    words = _key_words(key)
    if words and (words[0] in _NON_SECRET_LEAD_WORDS or words[-1] in _NON_SECRET_TAIL_WORDS):
        return False
    normalised = "".join(words)
    return any(marker in normalised for marker in _NORMALISED_MARKERS)


def redact_value(value: Any) -> Any:
    """Rebuild a JSON-shaped value with secret-looking entries replaced by :data:`REDACTED`, for
    display only: opaque leaves are shared, not inspected. Keep with :func:`redact_snapshot`."""
    return _redact(value, 0, set(), _redact_leaf)


def redact_snapshot(value: Any) -> Any:
    """Redact a value down to something safe to keep, log and render: a non-JSON leaf becomes a
    type-and-size summary such as ``<bytes of 4096>``, so no caller ``__repr__`` ever runs."""
    return _redact(value, 0, set(), _summarise_leaf)


def _redact(value: Any, depth: int, seen: set[int], leaf: Any) -> Any:
    """Walk one level, bounded by depth and by open containers, so cycles degrade to a marker."""
    if isinstance(value, (Mapping, list, tuple)):
        if depth >= MAX_REDACTION_DEPTH:
            return TOO_DEEP
        identity = id(value)
        if identity in seen:
            return CIRCULAR
        seen.add(identity)
        try:
            if isinstance(value, Mapping):
                return {
                    key: (
                        REDACTED
                        if should_redact(str(key))
                        else _redact(item, depth + 1, seen, leaf)
                    )
                    for key, item in value.items()
                }
            items = [_redact_entry(item, depth + 1, seen, leaf) for item in value]
            # Type preserved: a list would put a shape into a tuple field's ``repr``.
            return tuple(items) if isinstance(value, tuple) else items
        finally:
            seen.discard(identity)
    if isinstance(value, str):
        # In the order a value nests them: JSON-as-text, then any URL in the result.
        return _redact_urls(_redact_json_text(value, depth, seen, leaf))
    return leaf(value)


def _redact_entry(entry: Any, depth: int, seen: set[int], leaf: Any) -> Any:
    """Redact one sequence entry, honouring a ``(name, value)`` pair - judging mapping
    keys alone would print ``('X-Api-Key', 's3cret')``."""
    if (
        isinstance(entry, (list, tuple))
        and len(entry) == 2
        and isinstance(entry[0], str)
        and should_redact(entry[0])
    ):
        return (entry[0], REDACTED) if isinstance(entry, tuple) else [entry[0], REDACTED]
    return _redact(entry, depth, seen, leaf)


def _redact_json_text(text: str, depth: int, seen: set[int], leaf: Any) -> str:
    """Redact a JSON document that arrived as text, rewritten only when a secret was found."""
    if not text.lstrip().startswith(("{", "[")):
        return text
    try:
        parsed = json.loads(text)
    except (ValueError, RecursionError):
        # A truncated body still carries what was sent, so its secret-named values are scrubbed.
        return _scrub_json_pairs(text)
    redacted = _redact(parsed, depth + 1, seen, leaf)
    if redacted == parsed:
        return text
    return json.dumps(redacted, ensure_ascii=False)


#: Where a ``"name":`` begins a pair in JSON-ish text that will not parse; the name is
#: unrolled so a long string cannot be rescanned from every offset.
_JSON_NAME = re.compile(r'"(?P<name>[^"\\]*(?:\\.[^"\\]*)*)"(?P<gap>\s*:\s*)')

#: The same pair with both quotes backslash-escaped, a JSON document nested in a string;
#: unrolled so an unterminated run is not re-partitioned every way before it fails.
_JSON_NAME_ESCAPED = re.compile(r'\\"(?P<name>[^"\\]*(?:\\[^"][^"\\]*)*)\\"(?P<gap>\s*:\s*)')

#: What ends an unquoted scalar: a number, ``true``, ``false`` or ``null``.
_SCALAR_END = re.compile(r"[,}\]\s]")


def _end_of_json_value(text: str, start: int, quote: str) -> int:
    """Index just past the value at ``start``, whatever its shape; a truncated value ends at the
    end of the text."""
    if start >= len(text):
        return start
    if text.startswith(quote, start):
        return _end_of_json_string(text, start, quote)
    if text[start] in "{[":
        depth = 0
        index = start
        while index < len(text):
            if text.startswith(quote, index):
                index = _end_of_json_string(text, index, quote)
                continue
            character = text[index]
            if character in "{[":
                depth += 1
            elif character in "}]":
                depth -= 1
                if depth == 0:
                    return index + 1
            index += 1
        return len(text)
    match = _SCALAR_END.search(text, start)
    return match.start() if match else len(text)


def _end_of_json_string(text: str, start: int, quote: str) -> int:
    """Index just past the string at ``start``, or the end when unterminated."""
    index = start + len(quote)
    while index < len(text):
        # The delimiter first: an escaped ``\\"`` closing delimiter itself opens with a backslash.
        if text.startswith(quote, index):
            return index + len(quote)
        if text[index] == "\\":
            index += 2
            continue
        index += 1
    return len(text)


def _scrub_json_pairs(text: str) -> str:
    """Redact every secret-named value in JSON-ish text that would not parse, plain or escaped
    one level; everything else is left as it arrived."""
    for pattern, quote in ((_JSON_NAME, '"'), (_JSON_NAME_ESCAPED, '\\"')):
        out: list[str] = []
        cursor = 0
        position = 0
        while True:
            match = pattern.search(text, position)
            if match is None:
                break
            if not should_redact(match.group("name")):
                # After the match, not inside it, so the scan stays linear.
                position = match.end()
                continue
            end = _end_of_json_value(text, match.end(), quote)
            out.append(text[cursor : match.end()])
            out.append(f"{quote}{REDACTED}{quote}")
            cursor = end
            position = end
        out.append(text[cursor:])
        text = "".join(out)
    return text


def _redact_leaf(value: Any) -> Any:
    """Copy a leaf if that is cheap and possible, and never fail trying; a stream is
    summarised, copying one either raising or duplicating its whole buffer."""
    if hasattr(value, "read"):
        return _summarise_leaf(value)
    try:
        return copy.copy(value)
    except Exception:  # an opaque leaf has no secret to hide
        return value


def _summarise_leaf(value: Any) -> Any:
    """One leaf as something safe to keep: a JSON scalar unchanged - immutable, so keeping
    it is keeping a snapshot - and anything else as its type and size."""
    if value is None or isinstance(value, (bool, int, float)):
        return value
    size = _leaf_size(value)
    name = type(value).__name__
    return f"<{name}>" if size is None else f"<{name} of {size}>"


def _leaf_size(value: Any) -> int | None:
    """An opaque leaf's size, or ``None``; ``nbytes`` first, as a ``memoryview`` counts items."""
    for attribute in ("nbytes", "__len__"):
        try:
            measure = getattr(value, attribute, None)
            if measure is None:
                continue
            size = measure() if callable(measure) else measure
            if isinstance(size, int) and not isinstance(size, bool) and size >= 0:
                return size
        except Exception:  # a display helper must not raise
            continue
    return None


def redact_mapping(headers: Mapping[str, str] | None) -> dict[str, str]:
    """Redact a flat mapping such as headers: ``{"Authorization": "Bearer abc"}`` becomes
    ``{"Authorization": "***"}``, and a URL-shaped value loses its secrets too."""
    if not headers:
        return {}
    return {
        key: (REDACTED if should_redact(key) else _redact_urls(value))
        for key, value in headers.items()
    }


#: A URL-shaped run inside a longer value, judged per run as a ``Link`` carries two. The
#: scheme repeat is bounded so the match stays linear over text that was never a URL.
_URL_RUN = re.compile(r"[A-Za-z][A-Za-z0-9+.\-]{0,31}://[^\s<>\"']*")

#: A schemeless ``/path?query`` or ``/path#fragment``, as ``urllib3`` puts in its messages.
_PATH_QUERY_RUN = re.compile(r"/[^\s<>\"'?#]*[?#][^\s<>\"']+")


#: A scheme-relative ``//user:pass@host``, which neither pattern above reaches; ``:`` is
#: excluded from the password half so there is one partition and the scan stays linear.
_AUTHORITY_RUN = re.compile(r"(?<!:)//[^\s<>\"'/?#@]*:[^\s<>\"'/?#@:]*@[^\s<>\"'/?#]*")


def redact_text(value: str) -> str:
    """Redact every URL, every schemeless ``path?query`` and every scheme-relative userinfo inside
    free text, touching only each run's credentials, query and fragment. A pass whose delimiter
    is absent cannot match, so it is skipped."""
    cleaned = value
    if "://" in cleaned:
        cleaned = _URL_RUN.sub(lambda match: _redact_one_url(match.group(0)), cleaned)
    if "?" in cleaned or "#" in cleaned:
        cleaned = _PATH_QUERY_RUN.sub(lambda match: _redact_one_url(match.group(0)), cleaned)
    if "@" in cleaned:
        cleaned = _AUTHORITY_RUN.sub(
            lambda match: "//" + _redact_userinfo(match.group(0)[2:]), cleaned
        )
    return cleaned


def _redact_urls(value: Any) -> Any:
    """Redact the secrets a URL can carry, in every URL a string value contains: the name
    check alone is blind to these - ``Location`` carries no marker."""
    if not isinstance(value, str):
        return value
    return redact_text(value)


def _redact_one_url(url: str) -> str:
    """Redact one URL's userinfo password, query and fragment."""
    try:
        split = urlsplit(url)
    except ValueError:
        # ``Invalid IPv6 URL`` on an unclosed bracket: scrubbed by hand, not handed back.
        return _redact_unparsed_url(url)
    netloc = _redact_userinfo(split.netloc)
    query = _redact_query_string(split.query)
    fragment = _redact_query_string(split.fragment)
    if (netloc, query, fragment) == (split.netloc, split.query, split.fragment):
        return url
    return urlunsplit(split._replace(netloc=netloc, query=query, fragment=fragment))


#: The userinfo of a run ``urlsplit`` refused, found textually.
_USERINFO_IN_TEXT = re.compile(r"(//[^\s<>\"'/?#@]*:)([^\s<>\"'/?#@]*)(@)")


def _redact_unparsed_url(url: str) -> str:
    """Redact a run ``urlsplit`` refused, splitting on the delimiters by hand and judging each
    parameter by the same rule as a parsed URL."""
    body, hash_sign, fragment = url.partition("#")
    path, question, query = body.partition("?")
    path = _USERINFO_IN_TEXT.sub(lambda match: f"{match.group(1)}{REDACTED}{match.group(3)}", path)
    return (
        path
        + question
        + (_redact_query_string(query) if question else "")
        + hash_sign
        + (_redact_query_string(fragment) if hash_sign else "")
    )


def _redact_userinfo(netloc: str) -> str:
    """Replace the password in a ``user:password@host`` netloc, keeping the user visible;
    ``requests`` sends the pair as ``Basic``, so it is a live credential."""
    userinfo, at_sign, host = netloc.rpartition("@")
    if not at_sign or ":" not in userinfo:
        return netloc
    user = userinfo.partition(":")[0]
    return f"{user}:{REDACTED}@{host}"


def _redact_query_string(query: str) -> str:
    """Replace the value of every secret-named parameter in a query string, in place: parsing and
    re-encoding is lossy, ``?q=b%20c`` coming back as ``?q=b+c``."""
    if not query:
        return query
    rewritten = []
    matched = False
    for chunk in query.split("&"):
        name, separator, _ = chunk.partition("=")
        if separator and should_redact(unquote_plus(name)):
            rewritten.append(f"{name}={REDACTED}")
            matched = True
        else:
            rewritten.append(chunk)
    return "&".join(rewritten) if matched else query


def redact_fields(instance: Any, field_names: Any) -> list[str]:
    """One ``name=value`` string per named field for a ``repr``, secret-named fields redacted and
    the rest walked, since ``default_headers`` can carry ``X-Api-Key``."""
    shown = []
    for name in field_names:
        value = getattr(instance, name, None)
        if value and should_redact(name):
            value = REDACTED
        else:
            value = redact_snapshot(value)
        shown.append(f"{name}={value!r}")
    return shown
