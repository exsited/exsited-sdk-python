"""HTTP execution: one session, timeouts, TLS, proxy and retries. A ``401`` returns like any
other status; refreshing the token is the client's job."""

from __future__ import annotations

import codecs
import json
import re
import time
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Mapping
from urllib.parse import urlencode

import requests
from requests.adapters import HTTPAdapter
from requests.utils import guess_filename, to_key_val_list
from urllib3.fields import RequestField
from urllib3.filepost import choose_boundary, encode_multipart_formdata

from exsited.client.api_response import (
    ApiResponse,
    ErrorType,
    RequestInfo,
    classify_error_type,
    is_json_media_type,
)
from exsited.config.sdk_config import (
    DEFAULT_MAX_UPLOAD_BYTES,
    DEFAULT_RESPONSE_FORMAT,
    DEFAULT_TIMEOUT_SECONDS,
    header_name_problem,
    header_value_problem,
)
from exsited.errors import SdkError, SdkUsageError
from exsited.http.query_params import (
    QueryPairs,
    group_query_pairs,
    materialise_query_params,
)
from exsited.http.retry_policy import (
    RetryPolicy,
    is_http_method_token,
    transport_failure_timed_out,
)
from exsited.http.url_builder import check_request_url
from exsited.redaction import redact_text

_JSON_CONTENT_TYPE = "application/json"
_MULTIPART_CONTENT_TYPE = "multipart/form-data"
_FORM_CONTENT_TYPE = "application/x-www-form-urlencoded"
_CONTENT_TYPE_HEADER = "Content-Type"
_UNKNOWN_PARAMETER_ERROR = "unknown_parameter"
_TEXT_CONTENT_TYPE_PREFIX = "text/"
#: Matched as a substring, not parsed: this runs on every response and must not raise.
_CHARSET_PARAMETER = "charset="

#: The one codec that cannot fail, so it recovers an unusable declared charset too.
_TEXT_FALLBACK_CHARSET = "iso-8859-1"

#: Methods the stale-echo workaround may resend; not ``DELETE``, whose effect a resend repeats.
_RESENDABLE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})

#: Step size only; the total is bounded by ``config.max_response_bytes``.
_RESPONSE_CHUNK_BYTES = 64 * 1024


def _ignore_progress(message: str) -> None:
    """Drop a progress message, for a transport built without a reporter."""


#: One parameter name inside an ``unknown query parameter(s): …`` message, not the whole item.
_PARAMETER_NAME_PATTERN = re.compile(r"[A-Za-z0-9_-]+")


@dataclass(frozen=True)
class PreparedBody:
    """One request body materialised to what the wire will carry: nothing on this record is a
    caller's object, and ``form_record``/``files`` carry labels and structure, never contents."""

    json_bytes: bytes | None
    form_bytes: bytes | None
    form_stream: Any
    form_record: Any
    files: Any
    multipart_bytes: bytes | None
    multipart_content_type: str | None
    labelled_json: bool
    replayable: bool

    @property
    def form_encoded(self) -> bool:
        """Whether the body is a form, which the recorded headers cannot say and ``curl`` needs."""
        return self.json_bytes is None and (
            self.form_bytes is not None or self.form_stream is not None
        )


def materialise_body(
    json_body: Any = None,
    form_data: Any = None,
    files: Any = None,
    *,
    max_upload_bytes: int = DEFAULT_MAX_UPLOAD_BYTES,
    max_prepare_seconds: float | None = DEFAULT_TIMEOUT_SECONDS,
) -> PreparedBody:
    """Freeze one caller-supplied payload into the bytes and containers that go out, before the
    token grant lets caller-owned state change under an already-validated request."""
    if json_body is not None and files is not None:
        raise SdkUsageError(
            "pass json_body or files, not both - a multipart body replaces "
            "the JSON one, so the JSON would be discarded unsent"
        )
    budget = _UploadBudget(max_upload_bytes, max_prepare_seconds)
    json_bytes = _encode_json_body(json_body)
    if json_bytes is not None:
        # After the encode, so what is bounded is what would be sent, not what encoding allocated.
        budget.spend(len(json_bytes), "the JSON body")
    # Before anything reads them: whichever reaches a one-shot container drains it.
    files, form_data = materialise_payload(files, form_data, budget)
    if files:
        parts, form_pairs = materialise_multipart_parts(files, form_data, budget)
        # After the parts are frozen: the delimiter is checked against the bytes it will delimit.
        boundary = choose_uncollided_boundary(parts)
        multipart_bytes = render_multipart_body(parts, boundary, budget)
        return PreparedBody(
            json_bytes=json_bytes,
            form_bytes=None,
            form_stream=None,
            form_record=group_query_pairs(form_pairs) if form_pairs else None,
            files=multipart_record(parts),
            multipart_bytes=multipart_bytes,
            multipart_content_type=f"{_MULTIPART_CONTENT_TYPE}; boundary={boundary}",
            labelled_json=False,
            replayable=True,
        )
    form_bytes, form_stream, form_record, replayable = _materialise_form(form_data, budget)
    return PreparedBody(
        json_bytes=json_bytes,
        form_bytes=form_bytes,
        form_stream=form_stream,
        form_record=form_record,
        files=files,
        multipart_bytes=None,
        multipart_content_type=None,
        labelled_json=json_bytes is not None,
        replayable=replayable,
    )


def _materialise_form(
    form_data: Any, budget: "_UploadBudget"
) -> tuple[bytes | None, Any, Any, bool]:
    """Freeze one form payload under ``requests``' rules; an iterable stays live, not replayable."""
    if form_data is None:
        return None, None, None, True
    if isinstance(form_data, (str, bytes)):
        budget.spend(_measured_length(form_data), "the form body")
        return None, form_data, None, True
    if isinstance(form_data, bytearray):
        # Copied, because a caller can edit a bytearray between attempts.
        budget.spend(len(form_data), "the form body")
        return None, bytes(form_data), None, True
    if hasattr(form_data, "read"):
        # Spooled: a handle merely held is one whose contents can change before the replay.
        return None, budget.take(form_data, "the form body"), None, True
    if not _is_urlencodable_form(form_data):
        # An iterable of chunks: consumed as it is sent, so one attempt is all there is.
        return None, form_data, None, False
    pairs = _form_pairs(form_data)
    encoded = urlencode(pairs, doseq=True).encode("ascii")
    budget.spend(len(encoded), "the form body")
    return encoded, None, group_query_pairs(pairs), True


def _is_urlencodable_form(form_data: Any) -> bool:
    if isinstance(form_data, Mapping):
        return True
    if hasattr(form_data, "read"):
        return False
    return isinstance(form_data, (list, tuple)) and _is_form_pairs(list(form_data))


def _form_pairs(form_data: Any) -> QueryPairs:
    pairs: list[tuple[str, str | bytes]] = []
    for name, value in to_key_val_list(form_data):
        values = (
            [value]
            if isinstance(value, (str, bytes, bytearray)) or not hasattr(value, "__iter__")
            else list(value)
        )
        for item in values:
            if item is None:
                continue
            pairs.append((_form_name(name), _form_value(item)))
    return tuple(pairs)


def _form_name(name: Any) -> str:
    if isinstance(name, (bytes, bytearray)):
        return bytes(name).decode("utf-8", "surrogateescape")
    return name if isinstance(name, str) else str(name)


def _form_value(value: Any) -> str | bytes:
    """The single place a form value's own object is asked for its text."""
    if isinstance(value, bytes):
        return value
    if isinstance(value, bytearray):
        return bytes(value)
    return value if isinstance(value, str) else str(value)


def _encode_json_body(json_body: Any) -> bytes | None:
    """A JSON body as bytes, a ``str`` verbatim: ``http.client`` would write text as Latin-1."""
    if json_body is None:
        return None
    if isinstance(json_body, str):
        return json_body.encode("utf-8")
    try:
        return json.dumps(json_body, allow_nan=False).encode("utf-8")
    except (TypeError, ValueError, RecursionError) as error:
        # ``RecursionError`` is a ``RuntimeError``, not a ``ValueError``.
        raise SdkUsageError(
            "json_body is not JSON-serialisable; pass mappings, lists, strings, "
            "numbers, booleans and None, or a Dto",
            detail=str(error),
            cause=error,
        ) from None


class Transport:
    """Sends requests and decodes responses; one session each, so clients cannot interfere."""

    def __init__(
        self,
        config: Any,
        *,
        retry_policy: RetryPolicy | None = None,
        session: requests.Session | None = None,
        on_progress: Callable[[str], None] | None = None,
    ) -> None:
        self._config = config
        # A private revalidated copy, so a caller editing theirs cannot change a running request.
        self._retry_policy = (
            RetryPolicy.snapshot(retry_policy)
            if retry_policy is not None
            else RetryPolicy.from_config(config)
        )
        # Without it a call in a read timeout looks like a hung process.
        self._on_progress = on_progress or _ignore_progress
        self._owns_session = session is None
        self._session = session or self._build_session(config)

    @staticmethod
    def _build_session(config: Any) -> requests.Session:
        session = requests.Session()
        # ``pool_block`` stays ``False``: ``pool_maxsize`` caps kept connections, not concurrency.
        adapter = HTTPAdapter(
            pool_connections=config.pool_maxsize,
            pool_maxsize=config.pool_maxsize,
            max_retries=0,
        )
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        if config.proxy_url:
            session.proxies = {"http": config.proxy_url, "https": config.proxy_url}
        return session

    @property
    def verify(self) -> Any:
        """The value handed to ``requests`` as ``verify``."""
        if self._config.ca_bundle:
            return self._config.ca_bundle
        return self._config.verify_ssl

    def send_http_request(
        self,
        http_method: str,
        url: str,
        *,
        params: Mapping[str, Any] | None = None,
        json_body: Any = None,
        form_data: Any = None,
        files: Any = None,
        headers: Mapping[str, str] | None = None,
        request_info_headers: Mapping[str, str] | None = None,
        request_info_body: Any = None,
        endpoint_template: str = "",
        response_format: str | None = None,
        dto_type: Any = None,
    ) -> ApiResponse:
        """Send one request to a fully built absolute ``url``, retrying per the policy; a ``3xx``
        is not followed, and the ``request_info_*`` arguments record nothing unless passed."""
        check_request_url(url)
        return self.send_prepared_request(
            http_method,
            url,
            materialise_body(
                json_body,
                form_data,
                files,
                max_upload_bytes=self._config.max_upload_bytes,
                max_prepare_seconds=self._config.timeout_seconds,
            ),
            params=params,
            headers=headers,
            request_info_headers=request_info_headers,
            request_info_body=request_info_body,
            endpoint_template=endpoint_template,
            response_format=response_format,
            dto_type=dto_type,
        )

    def send_prepared_request(
        self,
        http_method: str,
        url: str,
        body: PreparedBody,
        *,
        params: Mapping[str, Any] | QueryPairs | None = None,
        headers: Mapping[str, str] | None = None,
        request_info_headers: Mapping[str, str] | None = None,
        request_info_body: Any = None,
        endpoint_template: str = "",
        response_format: str | None = None,
        dto_type: Any = None,
    ) -> ApiResponse:
        """Send an already-materialised request, retrying per the policy."""
        # Again here: this method is public and reachable without ``build_url``.
        check_request_url(url)
        method = _request_method(http_method)
        check_request_headers(headers)
        # Outside the loop: a mapping read once per attempt is one that can differ between them.
        if body.labelled_json:
            request_headers: dict[str, str] | None = _with_content_type(headers, _JSON_CONTENT_TYPE)
        elif body.multipart_content_type is not None:
            request_headers = _own_content_type(headers, body.multipart_content_type)
        elif body.form_bytes is not None:
            request_headers = _with_content_type(headers, _FORM_CONTENT_TYPE)
        else:
            request_headers = dict(headers) if headers else None
        query = materialise_query_params(params)
        started = time.monotonic()
        attempt = 0
        requests_sent = 0
        stale_echo_resent = False
        last_exception: BaseException | None = None
        replayable = body.replayable

        while attempt < self._retry_policy.max_attempts:
            attempt += 1
            requests_sent += 1
            connect_timeout, read_timeout = self._config.timeout
            # The template, never the URL: this reaches a caller's callback and a log record.
            self._on_progress(
                f"{method} {endpoint_template or 'the request'} sending "
                f"(attempt {attempt}/{self._retry_policy.max_attempts}, "
                f"connect {connect_timeout:g}s, read {read_timeout:g}s)"
            )
            # A fresh ceiling per attempt: a retry is a new request, not a continuation.
            attempt_deadline = time.monotonic() + read_timeout
            raw_response = None
            try:
                raw_response = self._session.request(
                    method,
                    url,
                    params=query,
                    # ``data`` only: ``files=`` would redraw the boundary on every attempt.
                    data=_wire_body(body),
                    headers=request_headers,
                    timeout=self._config.timeout,
                    verify=self.verify,
                    # A followed redirect loses ``Authorization`` and returns a bare ``401``.
                    allow_redirects=False,
                    # Without it, ``requests`` buffers the whole body before any cap can apply.
                    stream=True,
                )

                if (
                    attempt < self._retry_policy.max_attempts
                    and replayable
                    and self._retry_policy.should_retry_status_code(
                        raw_response.status_code, method
                    )
                ):
                    delay = self._retry_policy.compute_backoff_seconds(
                        attempt, raw_response.headers.get("Retry-After")
                    )
                    self._on_progress(
                        f"{raw_response.status_code}; retrying in {delay:.1f}s "
                        f"(attempt {attempt + 1}/{self._retry_policy.max_attempts})"
                    )
                    # An unread body leaves its connection checked out of the pool.
                    raw_response.close()
                    time.sleep(delay)
                    continue

                request_info = self._request_info(
                    http_method=method,
                    url=url,
                    params=query,
                    attempt=requests_sent,
                    max_attempts=self._granted_attempts(stale_echo_resent),
                    started=started,
                    request_info_headers=request_info_headers,
                    request_info_body=request_info_body,
                    endpoint_template=endpoint_template,
                )
                # Inside the handler: ``stream=True`` defers the body, so a timeout raises here.
                self._read_body_within_the_cap(raw_response, request_info, attempt_deadline)
            except SdkError:
                # The size refusal is a verdict on the body: re-reading reads the same body.
                raise
            except Exception as exception:  # re-raised as SdkError below
                last_exception = exception
                if raw_response is not None:
                    raw_response.close()
                if (
                    attempt >= self._retry_policy.max_attempts
                    or not replayable
                    or not self._retry_policy.should_retry_after_exception(exception, method)
                ):
                    break
                delay = self._retry_policy.compute_backoff_seconds(attempt)
                self._on_progress(
                    f"{type(exception).__name__}; retrying in {delay:.1f}s "
                    f"(attempt {attempt + 1}/{self._retry_policy.max_attempts})"
                )
                time.sleep(delay)
                continue

            api_response = self._build_api_response(
                raw_response=raw_response,
                request_info=request_info,
                response_format=response_format,
                dto_type=dto_type,
            )

            if (
                not stale_echo_resent
                and replayable
                and method in _RESENDABLE_METHODS
                and self._detect_stale_parameter_echo(api_response, query)
            ):
                # Its own slot: disabling retry is not asking for somebody else's reply.
                stale_echo_resent = True
                attempt -= 1
                self._discard_pooled_connections()
                continue

            return api_response

        raise self._build_transport_error(
            exception=last_exception,
            http_method=method,
            url=url,
            params=query,
            attempt=requests_sent,
            max_attempts=self._granted_attempts(stale_echo_resent),
            started=started,
            request_info_headers=request_info_headers,
            request_info_body=request_info_body,
            endpoint_template=endpoint_template,
        )

    def _granted_attempts(self, stale_echo_resent: bool) -> int:
        """How many requests this call was allowed to send, including the stale-echo slot."""
        return self._retry_policy.max_attempts + (1 if stale_echo_resent else 0)

    def _detect_stale_parameter_echo(self, response: ApiResponse, params: QueryPairs) -> bool:
        """Detect a ``400`` belonging to somebody else's request: after a ``400`` the server can
        repeat it on the next request over that keep-alive connection, whatever that one sent."""
        # ``.map``, not ``.data``: this must not depend on the caller's display preference.
        body = response.map
        if response.status_code != 400 or not isinstance(body, dict):
            return False

        named_fields = _extract_error_fields(body)
        if not named_fields and body.get("error") == _UNKNOWN_PARAMETER_ERROR:
            # Scoped to unknown_parameter, the only code with stable wording.
            named_fields = _parse_unknown_parameter_message(body)
        if not named_fields:
            return False

        sent = {str(name).lower() for name, _ in params}
        if not sent:
            # With nothing sent the test is vacuous: any ``400`` carrying ``errors[]`` matches.
            return False
        return not (named_fields & sent)

    def _discard_pooled_connections(self) -> None:
        """Drop pooled connections without closing a session this instance does not own."""
        if self._owns_session:
            self._session.close()
            return
        for adapter in self._session.adapters.values():
            adapter.close()

    def close_transport(self) -> None:
        """Close the underlying session, if this instance created it."""
        if self._owns_session:
            self._session.close()

    def __enter__(self) -> "Transport":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close_transport()

    def _request_info(
        self,
        *,
        http_method: str,
        url: str,
        params: QueryPairs,
        attempt: int,
        max_attempts: int,
        started: float,
        request_info_headers: Mapping[str, str] | None,
        request_info_body: Any = None,
        endpoint_template: str = "",
    ) -> RequestInfo:
        return RequestInfo(
            client_name=self._config.client_name,
            api_version=self._config.api_version,
            http_method=http_method,
            url=url,
            # From the pairs that went out, so the record reports the query the wire carried.
            query_params=group_query_pairs(params),
            headers=dict(request_info_headers) if request_info_headers else {},
            body=request_info_body,
            attempt_count=attempt,
            max_attempts=max_attempts,
            elapsed_seconds=round(time.monotonic() - started, 4),
            endpoint_template=endpoint_template,
        )

    def _read_body_within_the_cap(
        self, raw_response: requests.Response, request_info: RequestInfo, deadline: float
    ) -> None:
        """Buffer the streamed body within the cap and deadline; peak memory is twice the cap."""
        cap = self._config.max_response_bytes
        declared = _declared_content_length(raw_response)
        if declared is not None and declared > cap:
            raw_response.close()
            raise self._refuse_oversized_body(request_info, cap, declared)
        body = bytearray()
        # One byte past the cap is all the refusal needs, so a small cap shrinks the step.
        chunks = raw_response.iter_content(min(_RESPONSE_CHUNK_BYTES, cap + 1))
        while True:
            _hold_the_read_inside_the_ceiling(raw_response, deadline, self._config.timeout[1])
            try:
                chunk = next(chunks)
            except StopIteration:
                break
            # Judged before the chunk is retained, so nothing over the cap is ever held.
            if len(body) + len(chunk) > cap:
                raw_response.close()
                raise self._refuse_oversized_body(request_info, cap, declared)
            body.extend(chunk)
        # Undone before the connection returns to the pool.
        _restore_read_timeout(raw_response, self._config.timeout[1])
        _seed_response_content(raw_response, bytes(body))

    def _refuse_oversized_body(
        self, request_info: RequestInfo, cap: int, declared: int | None
    ) -> SdkError:
        size = f" (Content-Length {declared})" if declared is not None else ""
        return SdkError(
            f"the response body is over the {cap}-byte max_response_bytes cap{size}, so "
            f"it was not buffered - raise max_response_bytes on the client if a body "
            f"this large is expected",
            error_type=ErrorType.UNKNOWN,
            raw_response=None,
            request_info=request_info,
        )

    def _build_api_response(
        self,
        *,
        raw_response: requests.Response,
        request_info: RequestInfo,
        response_format: str | None = None,
        dto_type: Any = None,
    ) -> ApiResponse:
        return ApiResponse(
            status_code=raw_response.status_code,
            data=decode_response_body(raw_response),
            headers=dict(raw_response.headers),
            content_type=raw_response.headers.get("Content-Type"),
            error_type=classify_error_type(raw_response.status_code),
            # Not a copy: these bytes are the only surviving trace of the server's formatting.
            raw_body=raw_response.content or None,
            response_format=response_format or DEFAULT_RESPONSE_FORMAT,
            dto_type=dto_type,
            request_info=request_info,
        )

    def _build_transport_error(
        self,
        *,
        exception: BaseException | None,
        http_method: str,
        url: str,
        params: QueryPairs,
        attempt: int,
        max_attempts: int,
        started: float,
        request_info_headers: Mapping[str, str] | None,
        request_info_body: Any = None,
        endpoint_template: str = "",
    ) -> SdkError:
        """A no-response failure named by class: the library's own text repeats ``path?query``."""
        # Off the policy's table: a read timeout arrives as a bare ``ConnectionError``.
        timed_out = exception is not None and transport_failure_timed_out(exception)
        error_type = ErrorType.TIMEOUT if timed_out else ErrorType.NETWORK
        request_info = self._request_info(
            http_method=http_method,
            url=url,
            params=params,
            attempt=attempt,
            max_attempts=max_attempts,
            started=started,
            request_info_headers=request_info_headers,
            request_info_body=request_info_body,
            endpoint_template=endpoint_template,
        )
        label = "timed out" if timed_out else "failed"
        named = type(exception).__name__ if exception is not None else "no exception recorded"
        return SdkError(
            f"the request {label} after {attempt} attempt(s) with {named}",
            error_type=error_type,
            # Redacted even here: ``urllib3`` puts the prepared ``path?query`` in its messages.
            raw_response=(redact_text(str(exception)) if exception is not None else None),
            request_info=request_info,
        )


def _hold_the_read_inside_the_ceiling(
    raw_response: requests.Response, deadline: float, ceiling_seconds: float
) -> None:
    """Refuse a body arriving past the ceiling, and shrink the next read to the time left."""
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise requests.exceptions.ReadTimeout(
            f"the response body was still arriving after the {ceiling_seconds:g}s "
            f"timeout_seconds ceiling on one attempt"
        )
    sock = _response_socket(raw_response)
    if sock is not None:
        sock.settimeout(remaining)


def _restore_read_timeout(raw_response: requests.Response, read_timeout: float) -> None:
    sock = _response_socket(raw_response)
    if sock is not None:
        try:
            sock.settimeout(read_timeout)
        except Exception:  # a closed socket has nothing to restore
            pass


def _response_socket(raw_response: requests.Response) -> Any:
    """The body's socket, or ``None`` for an unknown shape, leaving the per-read timeout."""
    connection = getattr(getattr(raw_response, "raw", None), "_connection", None)
    sock = getattr(connection, "sock", None)
    return sock if hasattr(sock, "settimeout") else None


def _declared_content_length(raw_response: requests.Response) -> int | None:
    """The response's own ``Content-Length``, or ``None`` when it declared none or nonsense."""
    try:
        declared = int(raw_response.headers.get("Content-Length", ""))
    except (TypeError, ValueError):
        return None
    return declared if declared >= 0 else None


def _seed_response_content(raw_response: requests.Response, body: bytes) -> None:
    """Hand ``requests`` the bytes read here, through its only setter: two private attributes."""
    raw_response._content = body
    raw_response._content_consumed = True


def _request_method(http_method: Any) -> str:
    """Upper-case the method, refusing a non-token: ``"GET /x HTTP/1.1"`` smuggles a request."""
    if not isinstance(http_method, str) or not http_method.strip():
        raise SdkUsageError(
            f"http_method: expected a non-blank string like 'GET', got {http_method!r}"
        )
    stripped = http_method.strip()
    if not is_http_method_token(stripped):
        raise SdkUsageError(
            f"http_method: {http_method!r} is not an HTTP method token - a method is one "
            f"or more of the characters RFC 9110 allows in a token, with no space, "
            f"control or separator in it"
        )
    return stripped.upper()


def _wire_body(body: PreparedBody) -> Any:
    """The one object handed to ``requests`` as the body; only a stream is not replayable."""
    if body.multipart_bytes is not None:
        return body.multipart_bytes
    if body.json_bytes is not None:
        return body.json_bytes
    return body.form_bytes if body.form_bytes is not None else body.form_stream


def _with_content_type(headers: Mapping[str, str] | None, content_type: str) -> dict[str, str]:
    """Label a body sent as raw bytes, which ``requests`` does only for one it encoded itself. A
    content type the caller set wins. Not for multipart - see :func:`_own_content_type`."""
    labelled = dict(headers or {})
    if not any(_names_content_type(name) for name in labelled):
        labelled[_CONTENT_TYPE_HEADER] = content_type
    return labelled


def _own_content_type(headers: Mapping[str, str] | None, content_type: str) -> dict[str, str]:
    """Label a multipart body, replacing the caller's type: only this one names the boundary."""
    labelled = {
        name: value for name, value in (headers or {}).items() if not _names_content_type(name)
    }
    labelled[_CONTENT_TYPE_HEADER] = content_type
    return labelled


def _names_content_type(name: Any) -> bool:
    if isinstance(name, bytes):
        name = name.decode("latin-1", "replace")
    return isinstance(name, str) and name.strip().lower() == _CONTENT_TYPE_HEADER.lower()


def _header_text(value: Any) -> str:
    """One header name or value as text, ``bytes`` decoded Latin-1 so each byte keeps its value."""
    if isinstance(value, bytes):
        return value.decode("latin-1")
    return _plain_text(value) if isinstance(value, str) else str(value)


def _plain_text(value: str) -> str:
    """One ``str`` as a plain ``str``: a subclass can show a grammar check one value and answer
    ``__str__``, which ``urllib3`` uses to render a part header, with another."""
    return value if type(value) is str else str.__str__(value)


def check_request_headers(headers: Mapping[str, str] | None) -> None:
    """Refuse a header this SDK will not put on the wire, by the grammar the client shares."""
    # Sorted by the decoded name but never re-indexed by it: a ``bytes`` name would ``KeyError``.
    entries = sorted((headers or {}).items(), key=lambda entry: _header_text(entry[0]))
    for raw_name, raw_value in entries:
        name = _header_text(raw_name)
        text = _header_text(raw_value)
        problem = header_name_problem(name) or header_value_problem(text)
        if problem:
            # ``ascii``, not ``!r``: ``repr`` leaves a high byte raw for a cp1252 console.
            raise SdkUsageError(
                f"header {ascii(name)}: not something this SDK will send - {problem}. "
                f"The value is not shown: it may be a credential"
            )


#: Characters that would forge a multipart part header, which ``urllib3`` 2 does not escape.
_MULTIPART_FORBIDDEN_CHARACTERS = {"\r": "a carriage return", "\n": "a newline", "\x00": "a NUL"}

#: Percent form, not backslash: under the WHATWG rule most servers follow, a backslash is ignored.
_MULTIPART_PARAM_ESCAPES = {'"': "%22", "\\": "%5C"}

_MULTIPART_SHAPE_PROBLEM = (
    "the multipart payload could not be read; pass files as a mapping of name to "
    "contents, or to a (filename, contents[, content_type[, headers]]) tuple"
)

#: Step size only; the total is bounded by ``config.max_upload_bytes``.
_SPOOL_CHUNK_BYTES = 64 * 1024

#: A ceiling so an impossible payload cannot loop; one draw costs 32 hexadecimal characters.
_BOUNDARY_ATTEMPTS = 8


def _refuse_multipart_label(what: str, value: Any) -> None:
    """Refuse CR, LF or NUL in a part header value, where a CR/LF pair starts another header."""
    if not isinstance(value, str):
        return
    for index, character in enumerate(value):
        named = _MULTIPART_FORBIDDEN_CHARACTERS.get(character)
        if named:
            raise SdkUsageError(
                f"{what} carries {named} at character {index}, which would forge a header "
                f"on the multipart part this SDK sends. The value is not shown: it may be "
                f"attacker-chosen. Strip CR, LF and NUL from an upload filename before "
                f"passing it on"
            )


def _escape_multipart_param(value: str) -> str:
    """Make one value safe inside a quoted ``Content-Disposition`` parameter; idempotent."""
    for character, escape in _MULTIPART_PARAM_ESCAPES.items():
        value = value.replace(character, escape)
    return value


def _label_text(what: str, value: Any) -> str:
    """One multipart label as the text that will be encoded, converted exactly once."""
    if isinstance(value, str):
        return _plain_text(value)
    if isinstance(value, (bytes, bytearray, memoryview)):
        try:
            return bytes(value).decode("utf-8")
        except UnicodeDecodeError:
            raise SdkUsageError(
                f"{what}: bytes that are not UTF-8, which is the encoding a multipart "
                f"label is read in. Decode it yourself and pass the text"
            ) from None
    raise SdkUsageError(f"{what}: must be text, got {type(value).__name__}")


def _files_entries(payload: Any) -> list[tuple[Any, Any]]:
    if isinstance(payload, Mapping):
        return list(payload.items())
    if isinstance(payload, (list, tuple)):
        return [
            (entry[0], entry[1])
            for entry in payload
            if isinstance(entry, (tuple, list)) and len(entry) == 2
        ]
    return []


def _files_key_values(files: Any) -> list[tuple[Any, Any]]:
    """A ``files`` container's entries, read as ``requests`` reads them, before the grant."""
    try:
        return [(field, value) for field, value in to_key_val_list(files or {})]
    except (TypeError, ValueError) as error:
        raise SdkUsageError(_MULTIPART_SHAPE_PROBLEM, detail=str(error), cause=error) from None


@dataclass(frozen=True)
class MultipartPart:
    """One multipart part owned end to end: labels copied once as text, ``data`` owned bytes."""

    field: str
    filename: str | None
    content_type: str | None
    headers: tuple[tuple[str, str], ...]
    data: bytes
    from_files: bool


@dataclass(frozen=True)
class _PartLabels:
    """One ``files`` entry's frozen labels, beside the object its contents will be read from."""

    field: str
    filename: str | None
    content_type: str | None
    headers: tuple[tuple[str, str], ...]
    source: Any


def materialise_multipart_parts(
    files: Any, form_data: Any, budget: "_UploadBudget"
) -> tuple[tuple[MultipartPart, ...], QueryPairs]:
    """Freeze one multipart payload into its parts in wire order, labels checked before any read."""
    form_pairs = _frozen_form_pairs(form_data)
    named = [
        (_label_text("a files part name", field), value)
        for field, value in _files_key_values(files)
    ]
    labels: dict[int, _PartLabels] = {}
    for index in sorted(range(len(named)), key=lambda position: named[position][0]):
        field, value = named[index]
        _refuse_multipart_label(f"a files part name of {len(field)} character(s)", field)
        labels[index] = _frozen_part_labels(field, value)
    for name, _ in sorted(form_pairs, key=lambda pair: pair[0]):
        _refuse_multipart_label(f"a formData name of {len(name)} character(s)", name)

    parts: list[MultipartPart] = []
    for name, value in form_pairs:
        described = f"the formData field {name!r}"
        parts.append(
            MultipartPart(
                field=name,
                filename=None,
                content_type=None,
                headers=(),
                data=budget.take(value, described),
                from_files=False,
            )
        )
    for index in range(len(named)):
        label = labels[index]
        if label.source is None:
            # ``requests`` drops a ``None`` part rather than sending an empty one.
            continue
        parts.append(
            MultipartPart(
                field=label.field,
                filename=label.filename,
                content_type=label.content_type,
                headers=label.headers,
                data=budget.take(label.source, f"the part {label.field!r}"),
                from_files=True,
            )
        )
    return tuple(parts), form_pairs


def _frozen_part_labels(field: str, value: Any) -> _PartLabels:
    """One ``files`` entry's labels, refused or escaped where they could forge a part header."""
    filename, source, content_type, part_headers = _files_entry_labels(field, value)
    _refuse_multipart_label(f"the filename on part '{field}'", filename)
    _refuse_multipart_label(f"the content type on part '{field}'", content_type)
    return _PartLabels(
        field=_escape_multipart_param(field),
        filename=None if filename is None else _escape_multipart_param(filename),
        content_type=content_type,
        headers=_frozen_part_headers(field, part_headers),
        source=source,
    )


def _files_entry_labels(field: str, value: Any) -> tuple[str | None, Any, str | None, Any]:
    """Filename, contents, type and headers of a ``files`` entry, in any ``requests`` shape."""
    if not isinstance(value, (tuple, list)):
        # ``guess_filename`` reads ``value.name``; asked once and kept.
        return (
            _label_text(f"the filename on part '{field}'", guess_filename(value) or field),
            value,
            None,
            None,
        )
    if not 2 <= len(value) <= 4:
        raise SdkUsageError(_MULTIPART_SHAPE_PROBLEM)
    filename = value[0]
    content_type = value[2] if len(value) >= 3 else None
    return (
        None if filename is None else _label_text(f"the filename on part '{field}'", filename),
        value[1],
        None
        if content_type is None
        else _label_text(f"the content type on part '{field}'", content_type),
        value[3] if len(value) == 4 else None,
    )


def _frozen_part_headers(field: str, part_headers: Any) -> tuple[tuple[str, str], ...]:
    """Refuse a custom part header this SDK will not send."""
    if part_headers is None:
        return ()
    entries = _files_entries(part_headers)
    if not entries and part_headers:
        raise SdkUsageError(
            f"the part headers on part '{field}': expected a mapping of header names to "
            f"values, or a sequence of (name, value) pairs, got "
            f"{type(part_headers).__name__}"
        )
    frozen: list[tuple[str, str]] = []
    for name, value in sorted(entries, key=lambda entry: _header_text(entry[0])):
        header = _header_text(name)
        text = _header_text(value)
        problem = header_name_problem(header) or header_value_problem(text)
        if problem:
            raise SdkUsageError(
                f"the part header {header!r} on part '{field}': not something this SDK "
                f"will send - {problem}. The value is not shown: it may be a credential"
            )
        frozen.append((header, text))
    return tuple(frozen)


def _frozen_form_pairs(form_data: Any) -> QueryPairs:
    """The form pairs sent as multipart parts, each value asked for its text once."""
    if form_data is None:
        return ()
    try:
        return _form_pairs(form_data)
    except (TypeError, ValueError) as error:
        raise SdkUsageError(
            "the form data beside a multipart body could not be read; pass it as a "
            "mapping of name to value, or as a sequence of (name, value) pairs",
            detail=str(error),
            cause=error,
        ) from None


def choose_uncollided_boundary(parts: tuple[MultipartPart, ...]) -> str:
    """Draw a delimiter that appears nowhere in the frozen parts, which it would otherwise split."""
    for _ in range(_BOUNDARY_ATTEMPTS):
        boundary = choose_boundary()
        if not _boundary_occurs_in(boundary, parts):
            return boundary
    raise SdkUsageError(
        f"no multipart boundary free of the payload could be drawn in "
        f"{_BOUNDARY_ATTEMPTS} attempts: every one of them already occurs in the parts "
        f"being sent, which cannot happen by chance. The request is refused rather than "
        f"sent under a delimiter its own contents would break"
    )


def _boundary_occurs_in(boundary: str, parts: tuple[MultipartPart, ...]) -> bool:
    """Whether a candidate delimiter occurs in a part's bytes or in a label in its header block."""
    delimiter = boundary.encode("utf-8")
    for part in parts:
        if delimiter in part.data:
            return True
        labels = [part.field, part.filename or "", part.content_type or ""]
        for name, value in part.headers:
            labels.append(name)
            labels.append(value)
        if any(boundary in label for label in labels):
            return True
    return False


def render_multipart_body(
    parts: tuple[MultipartPart, ...], boundary: str, budget: "_UploadBudget"
) -> bytes:
    """Render the frozen parts under *boundary* with ``urllib3``'s encoder, charging the framing."""
    fields = []
    for part in parts:
        field = _request_field(part)
        # ``--boundary\r\n``, the rendered header block, and the ``\r\n`` closing the part.
        framing = len(boundary) + 4 + len(field.render_headers().encode("utf-8")) + 2
        budget.spend(framing, f"the framing of part {part.field!r}")
        fields.append(field)
    # ``--boundary--\r\n``.
    budget.spend(len(boundary) + 6, "the closing delimiter")
    try:
        body, _ = encode_multipart_formdata(fields, boundary=boundary)
    except SdkUsageError:
        raise
    except Exception as error:  # reported as the caller mistake it is
        raise SdkUsageError(
            f"the multipart payload could not be encoded ({type(error).__name__}); pass "
            f"files as a mapping of name to contents, or to a "
            f"(filename, contents[, content_type[, headers]]) tuple",
            detail=str(error),
            cause=error,
        ) from None
    budget.refuse_if_over(len(body), "the rendered multipart body")
    return body


def _request_field(part: MultipartPart) -> RequestField:
    field = RequestField(
        name=part.field, data=part.data, filename=part.filename, headers=dict(part.headers)
    )
    field.make_multipart(content_type=part.content_type)
    return field


def multipart_record(parts: tuple[MultipartPart, ...]) -> tuple[tuple[str, tuple[Any, ...]], ...]:
    """What the request record reports about a multipart body: each file part's field name and
    labels, and none of its bytes. Form pairs go through :attr:`PreparedBody.form_record`."""
    return tuple(
        (part.field, (part.filename, None, part.content_type, dict(part.headers)))
        for part in parts
        if part.from_files
    )


class _UploadBudget:
    """What is left of ``max_upload_bytes`` and of the time while one body is materialised."""

    __slots__ = ("_cap", "_spent", "_deadline_seconds", "_deadline")

    def __init__(self, cap: int, deadline_seconds: float | None = None) -> None:
        self._cap = cap
        self._spent = 0
        self._deadline_seconds = deadline_seconds
        self._deadline = None if deadline_seconds is None else time.monotonic() + deadline_seconds

    def spend(self, size: int, described: str) -> None:
        """Account for a payload already in memory, refusing once the budget is gone."""
        self._spent += size
        if self._spent > self._cap:
            raise self._refuse(described)

    def refuse_if_over(self, size: int, described: str) -> None:
        """Refuse a rendered whole over the cap uncharged: its parts are already charged."""
        if size > self._cap:
            raise self._refuse(described)

    def take(self, source: Any, described: str) -> bytes:
        """One payload as owned bytes charged to the budget, so the record cannot change later."""
        if hasattr(source, "read"):
            return self._spool(source, described)
        data = _owned_bytes(source, described)
        self.spend(len(data), described)
        return data

    def _spool(self, handle: Any, described: str) -> bytes:
        """Read one handle into owned bytes, one byte past the budget so an overrun is detected."""
        remaining = self._cap - self._spent
        pieces: list[Any] = []
        taken = 0
        while taken <= remaining:
            self._refuse_a_late_read(described)
            piece = handle.read(min(_SPOOL_CHUNK_BYTES, remaining + 1 - taken))
            if not piece:
                break
            pieces.append(piece)
            taken += _measured_length(piece)
        data = _joined_pieces(pieces, described)
        if len(data) > remaining:
            raise self._refuse(described)
        self._spent += len(data)
        return data

    def _refuse_a_late_read(self, described: str) -> None:
        """Refuse to start another read once the preparation deadline is spent."""
        if self._deadline is None or time.monotonic() < self._deadline:
            return
        raise SdkError(
            f"the request body was still being read after the "
            f"{self._deadline_seconds:g}s timeout_seconds ceiling on preparing it, "
            f"reached at {described}. The deadline is tested between reads: a read the "
            f"operating system has already blocked cannot be interrupted from here",
            error_type=ErrorType.TIMEOUT,
        )

    def _refuse(self, described: str) -> SdkUsageError:
        return SdkUsageError(
            f"the request body is over the {self._cap}-byte max_upload_bytes cap, "
            f"reached at {described}; nothing about an upload streams - the bytes are "
            f"rendered once so that a retry sends the same body - so raise "
            f"max_upload_bytes on the client if a request this large is expected, and "
            f"budget the memory for it"
        )


def _owned_bytes(value: Any, described: str) -> bytes:
    """One in-memory payload copied into bytes this module owns."""
    if isinstance(value, bytes):
        # Immutable, so a reference to it is a copy in every way that matters.
        return value
    if isinstance(value, str):
        return value.encode("utf-8")
    if isinstance(value, bool):
        # Before the ``int`` arm, which would send ``True`` as ``1``.
        raise SdkUsageError(f"{described}: expected bytes, text or a file-like object, got bool")
    if isinstance(value, int):
        return str(value).encode("utf-8")
    try:
        return bytes(memoryview(value))
    except TypeError:
        raise SdkUsageError(
            f"{described}: expected bytes, text or a file-like object, got {type(value).__name__}"
        ) from None


def _joined_pieces(pieces: list[Any], described: str) -> bytes:
    """One spool's pieces as owned ``bytes``, text encoded once so a split character stays whole."""
    if not pieces:
        return b""
    if all(isinstance(piece, str) for piece in pieces):
        return "".join(pieces).encode("utf-8")
    return b"".join(_owned_bytes(piece, described) for piece in pieces)


def _measured_length(value: Any) -> int:
    """A payload's size in bytes, or ``0``; buffer protocol, as ``len()`` counts a view's items."""
    if isinstance(value, str):
        return len(value.encode("utf-8"))
    try:
        return memoryview(value).nbytes
    except TypeError:
        pass
    try:
        return len(value)
    except TypeError:
        return 0


def is_one_shot_container(value: Any) -> bool:
    """Whether this container is an iterable that inspecting would consume - a generator or a
    ``dict.items()`` view, both of which ``requests`` accepts. A stream is excluded."""
    return (
        isinstance(value, Iterable)
        and not isinstance(value, (str, bytes, bytearray, Mapping, tuple, list))
        and not hasattr(value, "read")
    )


def materialise_payload(
    files: Any, form_data: Any, budget: "_UploadBudget | None" = None
) -> tuple[Any, Any]:
    """Read a one-shot ``files`` or form-data container into something re-readable. A form one
    goes back behind an iterator unless its entries are pairs, which ``requests`` reads as such.
    With a ``budget`` its preparation deadline is tested between items, so a slow generator
    cannot hold the call open before the request has a timeout of its own."""
    if is_one_shot_container(files):
        files = _drained(files, budget, "draining the files container")
    if is_one_shot_container(form_data):
        entries = _drained(form_data, budget, "draining the form body")
        form_data = entries if _is_form_pairs(entries) else iter(entries)
    return files, form_data


def _drained(container: Any, budget: "_UploadBudget | None", described: str) -> list[Any]:
    if budget is None:
        return list(container)
    entries: list[Any] = []
    for entry in container:
        budget._refuse_a_late_read(described)
        entries.append(entry)
    return entries


def _is_form_pairs(entries: list[Any]) -> bool:
    """Whether every entry is a two-element sequence, as ``requests`` tests; empty qualifies."""
    return all(isinstance(entry, (tuple, list)) and len(entry) == 2 for entry in entries)


def _extract_error_fields(body: Mapping[str, Any]) -> set[str]:
    """The field names in a structured error body's ``errors[]``, lowered to match what was sent."""
    fields: set[str] = set()
    entries = body.get("errors")
    if isinstance(entries, Mapping):
        # The mapping form is keyed by field name: ``{"limit": "..."}``.
        for field_name in entries:
            name = str(field_name).strip().lower()
            if name:
                fields.add(name)
    elif isinstance(entries, (list, tuple)):
        for entry in entries:
            if isinstance(entry, Mapping) and entry.get("field"):
                fields.add(str(entry["field"]).strip().lower())
    return fields


def _parse_unknown_parameter_message(body: Mapping[str, Any]) -> set[str]:
    """Parse parameter names out of an ``unknown query parameter(s): a, b`` message, the fallback
    for an ``unknown_parameter`` body with no ``errors[]``."""
    fields: set[str] = set()
    message = str(body.get("message") or "")
    marker = "unknown query parameter(s):"
    if marker in message:
        for listed in message.split(marker, 1)[1].split(","):
            named = _PARAMETER_NAME_PATTERN.search(listed)
            if named:
                fields.add(named.group(0).lower())
    return fields


def decode_response_body(raw_response: requests.Response) -> Any:
    """Decode a response body by its ``Content-Type``, ``None`` for a ``204`` or empty body. Not
    an allowlist of binary types, which would run ``.text`` over the customer export's XLSX."""
    if raw_response.status_code == 204 or not raw_response.content:
        return None

    content_type = (raw_response.headers.get("Content-Type") or "").lower()
    # The rule :attr:`ApiResponse.json` reads, so what decodes here always has text there.
    if is_json_media_type(content_type):
        try:
            return raw_response.json()
        except RecursionError as error:
            raise _body_nested_too_deeply(raw_response, error) from None
        except ValueError:
            return _reparse_json_body(raw_response)
    if content_type.startswith(_TEXT_CONTENT_TYPE_PREFIX):
        return _decode_text_body(raw_response, content_type)
    return raw_response.content


def _reparse_json_body(raw_response: requests.Response) -> Any:
    """Try once more on a JSON body ``requests`` would not parse, falling back to its text: a BOM
    is the one failure worth it, a charset-less ``application/json`` being forced to ``utf-8``."""
    try:
        return json.loads(raw_response.content.decode("utf-8-sig"))
    except RecursionError as error:
        raise _body_nested_too_deeply(raw_response, error) from None
    except (UnicodeDecodeError, ValueError):
        return raw_response.text


def _body_nested_too_deeply(raw_response: requests.Response, error: RecursionError) -> SdkError:
    """The refusal for a JSON body no parse can get through: ``RecursionError`` is not a
    ``ValueError``, and left alone it escaped every ``except SdkError``."""
    return SdkError(
        "the response body is JSON nested too deeply for this interpreter to parse; "
        "the text as it arrived is on this error's raw_response",
        status_code=raw_response.status_code,
        error_type=ErrorType.UNKNOWN,
        raw_response=redact_text(raw_response.text),
        cause=error,
    )


def _decode_text_body(raw_response: requests.Response, content_type: str) -> str:
    """Decode a ``text/*`` body, assuming UTF-8 when no charset was declared: ``requests`` follows
    RFC 2616 and assumes ISO-8859-1, which mangles non-ASCII. A usable declared charset wins."""
    declared = _CHARSET_PARAMETER in content_type
    if declared and _names_a_codec(raw_response.encoding):
        return raw_response.text
    try:
        return raw_response.content.decode("utf-8")
    except UnicodeDecodeError:
        if declared:
            return raw_response.content.decode(_TEXT_FALLBACK_CHARSET)
        return raw_response.text


def _names_a_codec(encoding: str | None) -> bool:
    if not encoding:
        return False
    try:
        codecs.lookup(encoding)
    except LookupError:
        return False
    return True
