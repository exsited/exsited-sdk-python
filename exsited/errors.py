"""Exception hierarchy for the Exsited SDK. The token cache and lock errors and their two
warnings are declared in :mod:`exsited.auth.token_store` and :mod:`exsited.auth.token_provider`,
which import this module, so they resolve here on first use."""

from __future__ import annotations

import importlib as _importlib
import os
import re
from typing import Any, Mapping

#: Includes U+2028 and U+2029, which would break the lines of :meth:`SdkError.explain`.
_CONTROL_CHARACTERS = re.compile(r"[\x00-\x1f\x7f-\x9f\u2028\u2029]")

DIAGNOSTICS_ENVIRONMENT_VARIABLE = "EXSITED_ERROR_DIAGNOSTICS"

_AFFIRMATIVE = frozenset({"1", "true", "yes", "on"})

_DIAGNOSTICS_REMEDY = (
    "call explain(diagnostics=True), or set EXSITED_ERROR_DIAGNOSTICS=1, for the "
    "API's message, the response body, the query values, the resolved URL, the "
    "path or origin this failure names and the native cause's own wording"
)


def _diagnostics_from_environment() -> bool:
    return (os.environ.get(DIAGNOSTICS_ENVIRONMENT_VARIABLE) or "").strip().lower() in _AFFIRMATIVE


#: Read at import, then only through the functions below, so a program can still change it.
_DIAGNOSTICS = [_diagnostics_from_environment()]


def error_diagnostics_enabled() -> bool:
    """Whether :meth:`SdkError.explain` includes its diagnostic tier by default."""
    return _DIAGNOSTICS[0]


def set_error_diagnostics(enabled: bool) -> bool:
    """Turn the diagnostic tier on or off process-wide, returning what it was so a
    diagnostic block can put it back."""
    previous = _DIAGNOSTICS[0]
    _DIAGNOSTICS[0] = bool(enabled)
    return previous


def _flatten(value: Any) -> str:
    """A server value as one escaped line, so a ``message`` cannot forge an ``explain`` field."""
    text = _safe_str(value)
    return _CONTROL_CHARACTERS.sub(
        lambda match: match.group().encode("unicode_escape").decode("ascii"), text
    )


def _safe_str(value: Any) -> str:
    for render in (str, repr):
        try:
            return render(value)
        except Exception:  # a display helper must not raise
            continue
    return f"<unrenderable {type(value).__name__}>"


class SdkError(Exception):
    """Base class for every error the SDK raises, and raised directly for any non-2xx that
    is not more specifically an authentication or usage problem."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        error_type: Any = None,
        raw_response: Any = None,
        response_headers: Mapping[str, str] | None = None,
        request_info: Any = None,
        detail: str | None = None,
        cause: BaseException | None = None,
        error_code: str | None = None,
        request_id: str | None = None,
        doc_url: str | None = None,
        field_errors: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        # Typed ``Any`` so this module stays a dependency leaf.
        self.error_type = error_type
        self.raw_response = raw_response
        # Empty rather than ``None``, so no reader needs a guard before a lookup.
        self.response_headers: dict[str, str] = dict(response_headers or {})
        self.request_info = request_info
        #: Names a value: a path, an origin, a native library's wording.
        self.detail = detail
        #: The native failure underneath, kept but never chained, so a traceback shows one message.
        self.cause = cause
        #: The v4 envelope's machine-readable ``code``, the thing to branch on.
        self.error_code = error_code
        #: The API's own id for the failed request, the handle to quote to support.
        self.request_id = request_id
        #: Documentation for ``error_code``, when the envelope carried one.
        self.doc_url = doc_url
        #: The envelope's per-field failures, unflattened; copied so the response cannot reach it.
        self.field_errors: list[dict[str, str]] = list(field_errors or [])
        self.errors: list[str] = []

    def add_error(self, error_message: str) -> "SdkError":
        """Append one field-level message and return this exception, so calls chain."""
        self.errors.append(error_message)
        return self

    def get_error_messages(self) -> list[str]:
        """The API's field-level messages; empty when it gave none, so read ``.message`` then."""
        return list(self.errors)

    def get_hint(self) -> str | None:
        """A one-line suggestion for this failure, or ``None``."""
        if self.status_code is None:
            return None
        return _HINTS_BY_STATUS.get(self.status_code)

    def explain(self, *, diagnostics: bool | None = None) -> str:
        """Return this failure as one printable block: a structural tier always, plus the
        data tier when ``diagnostics`` is on (``None`` defers to the process setting)."""
        include = error_diagnostics_enabled() if diagnostics is None else bool(diagnostics)
        lines = [str(self)]

        info = self.request_info
        detail = []
        if info is not None:
            attempts = getattr(info, "attempt_count", None)
            max_attempts = getattr(info, "max_attempts", None)
            elapsed = getattr(info, "elapsed_seconds", None)
            if attempts and max_attempts:
                detail.append(f"attempt : {attempts}/{max_attempts}")
            if elapsed is not None:
                detail.append(f"elapsed : {elapsed}s")
        if self.cause is not None:
            # The class name only: a native library's text can name a path, a host or a value.
            detail.append(f"cause   : {type(self.cause).__name__}")
        # The envelope's code and request id name the failure, never the data, so both stay.
        if self.error_code:
            detail.append(f"code    : {_flatten(self.error_code)}")
        if self.request_id:
            detail.append(f"request : {_flatten(self.request_id)}")
        hint = self.get_hint()
        if hint:
            detail.append(f"hint    : {hint}")
        lines += [f"  {line}" for line in detail]

        if not include:
            lines.append(f"  detail  : withheld - {_DIAGNOSTICS_REMEDY}")
            return "\n".join(lines)

        lines += [f"  {line}" for line in self._diagnostic_lines()]
        return "\n".join(lines)

    def _diagnostic_lines(self) -> list[str]:
        """The tier :meth:`explain` withholds by default; the raiser has already redacted it."""
        lines = []

        if self.detail:
            lines.append(f"detail  : {_flatten(self.detail)}")
        if self.cause is not None:
            lines.append(f"cause   : {type(self.cause).__name__}: {_flatten(self.cause)}")

        info = self.request_info
        if info is not None:
            url = getattr(info, "url", None)
            if url:
                lines.append(f"url     : {_flatten(_shorten_url(url))}")
            if getattr(info, "query_params", None):
                lines.append(f"params  : {dict(info.query_params)}")

        location = _redirect_target(self.response_headers)
        if location:
            lines.append(f"location: {_flatten(location)}")

        messages = self.get_error_messages()
        if messages:
            lines.append("reported:")
            lines += [f"  - {_flatten(message)}" for message in messages]

        if self.raw_response is not None:
            body = _flatten(self.raw_response)
            if len(body) > 500:
                body = body[:500] + f"... +{len(body) - 500} chars"
            lines.append(f"body    : {body}")

        return lines

    def __str__(self) -> str:
        """One line naming the status, the category, the call and this SDK's own reason."""
        parts = []
        if self.status_code:
            parts.append(str(self.status_code))
        if self.error_type is not None:
            parts.append(f"[{_flatten(self.error_type)}]")
        info = self.request_info
        if info is not None:
            method = getattr(info, "http_method", None)
            endpoint = getattr(info, "endpoint_template", None)
            if method and endpoint:
                parts.append(f"{_flatten(method)} {_flatten(endpoint)}")
        # A newline in this SDK's own ``message`` would break the one-line promise.
        reason = _flatten(self.message)
        return f"{' '.join(parts)} - {reason}" if parts else reason


_REDIRECT_STATUS_CODES = (301, 302, 303, 307, 308)

#: A signed ``Location`` arrives here redacted to ``?signature=***``, which ``build_url``
#: refuses, so the remedy names the *response* to re-issue from.
_REDIRECT_HINT = (
    "the API redirected and the SDK does not follow one - read the Location "
    "header off the response and decide whether to re-issue the call against it. "
    "The copy on this exception's response_headers has its secret query "
    "parameters redacted, so it is for reading and not for re-issuing: call again "
    "with raise_on_error off if you need the response itself"
)

_HINTS_BY_STATUS: dict[int, str] = {
    **{status: _REDIRECT_HINT for status in _REDIRECT_STATUS_CODES},
    400: (
        "the API rejected the request itself - check the payload shape and "
        "the query parameter names against the endpoint's docstring"
    ),
    401: (
        "credentials were rejected, or the token expired and could not be "
        "renewed - check client_id, client_secret and redirect_uri"
    ),
    403: "authenticated, but this client is not allowed to do that",
    404: "no such record - check the id you passed actually exists",
    405: "wrong HTTP method for this path",
    409: "conflicts with existing data, e.g. an email already in use",
    429: "rate limited - slow down, or raise max_retries so the SDK waits and retries for you",
    # 500 is absent from ``unsafe_retryable_http_codes``, so no write retries on one.
    500: (
        "the server failed. Retrying may help on a read; the SDK will not "
        "retry a write on a 500, because it cannot tell whether the server "
        "committed"
    ),
}


_LOCATION_HEADER = "location"


def _redirect_target(headers: Mapping[str, str]) -> str | None:
    """Return the ``Location`` a response named, whatever case it arrived in."""
    for name, value in headers.items():
        # ``str(name)``: a non-text key would take ``explain()`` down on ``.lower()``.
        if str(name).lower() == _LOCATION_HEADER:
            return value
    return None


def _shorten_url(url: str) -> str:
    """Drop the scheme and host, keeping the path that identifies the call."""
    marker = "://"
    if marker not in url:
        return url
    remainder = url.split(marker, 1)[1]
    return remainder[remainder.index("/") :] if "/" in remainder else url


class SdkConfigError(SdkError):
    """Configuration is missing or invalid, raised at construction time and listing every
    problem it found rather than the first."""


class SdkUsageError(SdkError):
    """The caller made a mistake the SDK detects before any network I/O."""


class SdkAttributeError(SdkUsageError, AttributeError):
    """A name that does not exist on a client or a bound resource."""


class SdkAuthError(SdkError):
    """Authentication failed."""


class InsecureTransportWarning(UserWarning):
    """Certificate verification is off, so responses cannot be trusted."""


_DECLARED_IN_AUTH = {
    "SdkTokenCacheError": "exsited.auth.token_store",
    "SdkTokenLockError": "exsited.auth.token_store",
    "DegradedTokenLockWarning": "exsited.auth.token_store",
    "DegradedTokenCacheWarning": "exsited.auth.token_provider",
}


def __getattr__(name: str) -> Any:
    """Resolve the auth-declared token types on first use; auth imports this module."""
    module = _DECLARED_IN_AUTH.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(_importlib.import_module(module), name)
