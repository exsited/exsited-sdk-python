"""Obtaining and refreshing the OAuth2 access token.

Success here means any 2xx: the token endpoint may answer 200 or 201. It issues a
refresh token and honours the ``refresh_token`` grant, so a renewal tries that
first and falls back to a full ``client_credentials`` request.

The token comes from ``POST /api/v4/oauth2/token``, and the refresh grant uses the
same path. Pass ``token_path`` to :class:`TokenProvider` to point it elsewhere.
"""

from __future__ import annotations

import math
import re
import threading
import time
import warnings
from dataclasses import dataclass, fields
from typing import Any

from exsited.auth.token_store import SdkTokenCacheError
from exsited.errors import SdkAuthError, SdkError, SdkUsageError
from exsited.http.transport import Transport
from exsited.redaction import redact_fields, redact_mapping, redact_value

TOKEN_PATH_TEMPLATE = "/api/{api_version}/oauth2/token"

#: The API version the token endpoint lives under.
TOKEN_API_VERSION = "v4"

DEFAULT_TOKEN_TTL_SECONDS = 3600
EXPIRY_SKEW_SECONDS = 60

#: The longest lifetime accepted from the server, and the furthest ahead a cached expiry
#: is believed; a longer one is clamped. ``expires_at`` is stamped by the minting
#: machine's clock, so a clock running ahead can make an expired token look fresh, and
#: the bound leaves such a token to the ``401`` refresh-and-replay path.
MAX_TOKEN_TTL_SECONDS = 24 * 60 * 60

_REFRESH_GRANT_TYPE = "refresh_token"

#: The cache-write failures a paid-for token is kept through: ``OSError`` from the
#: filesystem, and :class:`~exsited.errors.SdkError` from a store reporting an
#: unreadable or unlockable cache. A ``TypeError`` is outside it: from a custom store
#: whose ``write_token_record`` signature has drifted it is a caller defect, and
#: absorbing it would turn caching off with nothing saying why.
_TOLERATED_WRITE_FAILURES = (OSError, SdkError)

#: RFC 6750 section 2.1 ``b64token``: what may stand after ``Bearer`` in an
#: ``Authorization`` header.
_BEARER_CREDENTIAL = re.compile(r"[A-Za-z0-9\-._~+/]+=*")

#: RFC 6749 section 5.1 with Appendix A.17, ``1*VSCHAR``: what may be sent as a field
#: of a token request. A different grammar from the one above: a refresh credential is a
#: request field, not a header value, so it keeps punctuation Bearer has no room for.
_REFRESH_CREDENTIAL = re.compile(r"[\x20-\x7e]+")


class DegradedTokenCacheWarning(UserWarning):
    """A token was obtained but could not be cached.

    The call itself succeeded; the next process pays for its own token. Its own
    category, so a caller on a read-only filesystem can silence exactly this::

        warnings.filterwarnings("ignore", category=DegradedTokenCacheWarning)
    """


def check_access_credential(value: Any) -> str:
    """Check a credential that will be put in an ``Authorization: Bearer`` header.

    It must be an RFC 6750 section 2.1 ``b64token``, and already text: a JSON number
    converted with ``str()`` would go out as a Bearer credential no server issued.

    :return: the value, unchanged, so this reads as a conversion at a call site.
    :raises SdkUsageError: it is not text, or not that grammar. Neither message says
        which character was wrong or where, because the value is a credential.
    """
    if not isinstance(value, str):
        raise SdkUsageError(
            f"access_token: expected the credential as text, got "
            f"{type(value).__name__}. A token is not converted from another type: "
            f"what would be sent is that type's rendering, which is not a credential"
        )
    if not _BEARER_CREDENTIAL.fullmatch(value):
        raise SdkUsageError(
            "access_token: is not a Bearer credential. RFC 6750 allows letters, "
            "digits and - . _ ~ + / with optional = padding at the end, and this SDK "
            "puts the value straight into an Authorization header; the value itself "
            "is not shown"
        )
    return value


def check_refresh_credential(value: Any) -> str:
    """Check a credential that will be sent as a field of a token request.

    RFC 6749 section 5.1 visible text, not the Bearer grammar: see
    :data:`_REFRESH_CREDENTIAL`.

    :return: the value, unchanged.
    :raises SdkUsageError: it is not text, or carries something outside that range.
        The value itself is never shown.
    """
    if not isinstance(value, str):
        raise SdkUsageError(
            f"refresh_token: expected the credential as text, got "
            f"{type(value).__name__}"
        )
    if not _REFRESH_CREDENTIAL.fullmatch(value):
        raise SdkUsageError(
            "refresh_token: is not a token-response value. RFC 6749 allows the "
            "visible ASCII range and a space, and this one carries something outside "
            "it - a control character, or a character with no defined encoding on "
            "this request; the value itself is not shown"
        )
    return value


def build_token_path(api_version: str = TOKEN_API_VERSION) -> str:
    """Build the token endpoint path.

    :param api_version: the version the token endpoint is served from, defaulting to
        :data:`TOKEN_API_VERSION`.

    Example::

        build_token_path()       # '/api/v4/oauth2/token'
    """
    return TOKEN_PATH_TEMPLATE.format(api_version=api_version)


def _redirect_refusal_message(status_code: int, headers: Any) -> str:
    """Say a token request answered with a redirect was refused, without the ``Location``."""
    location = next(
        (str(value) for name, value in (headers or {}).items() if str(name).lower() == "location"),
        "",
    )
    target = (
        "redirecting to its sign-in page"
        if "login" in location.split("?", 1)[0].lower()
        else "a redirect instead of a token"
    )
    return (
        "the token request was refused: check client_id, client_secret and redirect_uri "
        f"(the API answered {status_code}, {target})"
    )


@dataclass(frozen=True, repr=False)
class TokenRecord:
    """An access token and when it stops being usable.

    Both credentials are checked at construction, each against the grammar of where it
    is sent. Every route into a record meets here (a caller, a decoded grant, a cache
    entry), so a value that could not be sent is rejected where it enters.
    """

    access_token: str
    refresh_token: str | None
    expires_at: float
    #: How early to treat this token as expired. Per record: a token stated to live 30
    #: seconds would be stale on arrival under a 60-second skew.
    skew_seconds: float = EXPIRY_SKEW_SECONDS

    def __post_init__(self) -> None:
        """Check both credentials.

        :raises SdkUsageError: either credential is not text or not its grammar.
        """
        check_access_credential(self.access_token)
        if self.refresh_token is not None:
            check_refresh_credential(self.refresh_token)

    def needs_refresh(self, skew_seconds: float | None = None) -> bool:
        """Whether the token should be treated as expired.

        The skew expires a token early: two seconds left passes a naive check and then
        fails in flight.

        :param skew_seconds: treat the token as expired this long before it is. Defaults
            to the skew decided for this record when it was minted.
        """
        effective_skew = self.skew_seconds if skew_seconds is None else skew_seconds
        now = time.time()
        if self.expires_at - now > MAX_TOKEN_TTL_SECONDS:
            # Further ahead than any lifetime accepted here: the stamp came off another
            # clock. Refresh rather than believe it.
            return True
        return now >= (self.expires_at - effective_skew)

    def to_dict(self) -> dict[str, Any]:
        """Convert to the plain mapping a token store persists."""
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at,
            "skew_seconds": self.skew_seconds,
        }

    @classmethod
    def from_dict(cls, record: dict[str, Any] | None) -> "TokenRecord | None":
        """Rebuild from a stored mapping.

        :return: the record, or ``None`` when the store held nothing.
        :raises SdkTokenCacheError: an entry is there and is not a usable record; read as
            absent, a corrupt entry would hide behind an authentication on every call.
        """
        if not record:
            return None
        skew_seconds = record.get("skew_seconds")
        # ``bool`` is an ``int``, so a stored ``true`` would become a 1-second skew. An
        # unusable skew falls back rather than refusing the record: it is a tuning
        # value, not a credential, and the default is always safe.
        if (
            not isinstance(skew_seconds, (int, float))
            or isinstance(skew_seconds, bool)
            or not math.isfinite(skew_seconds)
            or skew_seconds < 0
        ):
            skew_seconds = EXPIRY_SKEW_SECONDS
        expires_at = record.get("expires_at")
        # ``isinstance`` passes for NaN and Infinity, so finiteness is checked too - no
        # comparison in :meth:`needs_refresh` can expire either.
        if (
            not isinstance(expires_at, (int, float))
            or isinstance(expires_at, bool)
            or not math.isfinite(expires_at)
        ):
            raise cls._corrupt_cache_entry(
                "expires_at is not a finite number of seconds"
            )
        refresh_token = record.get("refresh_token")
        try:
            # Not coerced: ``__post_init__`` checks both credentials, so a stored
            # ``access_token: 12345`` is refused rather than sent as ``Bearer 12345``.
            return cls(
                access_token=record.get("access_token"),
                refresh_token=refresh_token if refresh_token is not None else None,
                expires_at=float(expires_at),
                skew_seconds=min(float(skew_seconds), MAX_TOKEN_TTL_SECONDS),
            )
        except SdkUsageError as error:
            raise cls._corrupt_cache_entry(str(error)) from None

    @staticmethod
    def _corrupt_cache_entry(problem: str) -> SdkTokenCacheError:
        """:return: the refusal for a cached entry that cannot be used, to ``raise``."""
        return SdkTokenCacheError(
            f"the cached token record is not usable: {problem}. It is not read as "
            f"absent: an entry that exists and cannot be understood is a corrupt "
            f"cache, and reading it as empty would hide that behind an authentication "
            f"on every call. Clear the entry, or pass token_cache_path=None to keep "
            f"the token in memory"
        )

    def __repr__(self) -> str:
        """Return a ``repr`` with both tokens redacted, safe for logs and tracebacks."""
        shown = redact_fields(self, [field.name for field in fields(self)])
        return f"TokenRecord({', '.join(shown)})"

    __str__ = __repr__


class TokenProvider:
    """Fetches, caches and renews the access token.

    Concurrency is double-checked locking: an in-process lock, then the store's
    cross-process lock, re-reading the store inside each, so a worker that waited
    usually finds a fresh token and never calls the token endpoint.

    :param config: supplies credentials, base URL and API version.
    :param transport: used for the token request itself.
    :param token_store: where the token is cached.
    :param token_path: overrides the derived token path, for a deployment that mounts
        the endpoint somewhere unusual.
    """

    def __init__(
        self,
        config: Any,
        transport: Transport,
        token_store: Any,
        *,
        token_path: str | None = None,
    ) -> None:
        self._config = config
        self._transport = transport
        self._token_store = token_store
        # The token endpoint is built from ``TOKEN_API_VERSION``. See the module
        # docstring.
        self._token_path = token_path or build_token_path()
        self._thread_lock = threading.Lock()

    @property
    def token_url(self) -> str:
        """The absolute token endpoint URL: base URL joined with the token path."""
        return self._config.base_url + self._token_path

    def get_access_token(self) -> str:
        """Return a usable access token, fetching one only if needed.

        :raises SdkAuthError: the token endpoint rejected the credentials, or
            answered with something that cannot be sent as a credential.
        :raises SdkTokenCacheError: the cache is there and cannot be used; the
            alternative rewrites a file whose contents are unknown.
        """
        record = TokenRecord.from_dict(self._token_store.read_token_record())
        if record and not record.needs_refresh():
            return record.access_token
        return self._renew_access_token(
            stale_access_token=None, any_cached_token_will_do=True
        )

    def refresh_access_token(self, stale_access_token: str | None) -> str:
        """Replace a token that the API has just rejected.

        :param stale_access_token: the token that produced the ``401``. If the store
            already holds a different one, another worker refreshed first and that token
            is returned instead of fetching again. ``None`` means the caller cannot say
            which token failed, so the cached one is not trusted and a renewal always
            happens.
        :raises SdkAuthError: the token endpoint rejected the credentials.
        """
        return self._renew_access_token(
            stale_access_token=stale_access_token, any_cached_token_will_do=False
        )

    def clear_access_token(self) -> None:
        """Discard the cached token, forcing a fetch on the next call."""
        self._token_store.clear_token_record()

    def invalidate_access_token(self, dead_access_token: str | None) -> bool:
        """Evict a token the API has just refused, if the cache still holds it.

        For a ``401`` whose refresh did not happen: the cache is shared across processes,
        so a dead token left there would be read and sent by every one of them.

        A compare-and-clear: another worker may have written a live token since the
        ``401``, and on these credentials each new grant revokes the previous token.

        :param dead_access_token: the token that produced the ``401``. ``None`` names
            no token, so nothing is evicted.
        :return: whether an entry was removed.
        """
        if not dead_access_token:
            return False
        with self._thread_lock:
            with self._token_store.acquire_token_refresh_lock():
                record = TokenRecord.from_dict(self._token_store.read_token_record())
                if record is None or record.access_token != dead_access_token:
                    return False
                self._token_store.clear_token_record()
                return True

    def _renew_access_token(
        self, *, stale_access_token: str | None, any_cached_token_will_do: bool
    ) -> str:
        with self._thread_lock:
            with self._token_store.acquire_token_refresh_lock():
                record = TokenRecord.from_dict(self._token_store.read_token_record())
                if record and not record.needs_refresh():
                    # Any fresh token answers :meth:`get_access_token`. A refresh is
                    # replacing a token the API rejected, so it accepts only a
                    # *different* one, and none at all when none was named.
                    if any_cached_token_will_do or (
                        stale_access_token is not None
                        and record.access_token != stale_access_token
                    ):
                        return record.access_token

                new_record = None
                if record and record.refresh_token:
                    new_record = self._request_token_with_refresh_grant(record.refresh_token)
                if new_record is None:
                    new_record = self._request_token_with_credentials()

                try:
                    self._token_store.write_token_record(new_record.to_dict())
                except Warning:
                    # Ahead of the clause below: a ``Warning`` a caller escalated with
                    # ``simplefilter("error", ...)`` is a request to be told.
                    raise
                except _TOLERATED_WRITE_FAILURES:
                    # A token already paid for is kept when the cache will not take it.
                    warnings.warn(
                        "the access token could not be cached, so the next process "
                        "will obtain its own; the call itself succeeded",
                        DegradedTokenCacheWarning,
                        stacklevel=2,
                    )
                return new_record.access_token

    def _request_token_with_credentials(self) -> TokenRecord:
        response = self._transport.send_http_request(
            "POST",
            self.token_url,
            # Built by a call rather than held in a local, which a traceback would keep
            # reachable through ``tb_frame.f_locals`` with ``client_secret`` in the clear.
            json_body=self._credentials_payload(),
            headers=self._token_headers(),
        )
        if 300 <= response.status_code < 400:
            # Wrong credentials are answered with a redirect to the sign-in page rather
            # than a ``401``. The ``Location`` stays out of the message: its query string
            # can carry what was sent.
            raise SdkAuthError(
                _redirect_refusal_message(response.status_code, response.headers),
                status_code=response.status_code,
                error_type=response.error_type,
                raw_response=redact_value(response.data),
                response_headers=redact_mapping(response.headers),
                request_info=response.request_info,
            )
        if not response.succeeded:
            messages = response.get_error_messages()
            error = SdkAuthError(
                f"token request failed with {response.status_code}: "
                f"{messages[0] if messages else 'no detail'}",
                status_code=response.status_code,
                error_type=response.error_type,
                raw_response=redact_value(response.data),
                # This response never reaches the caller, so an unfollowed ``3xx``'s
                # ``Location`` survives only here. Redacted at the call site, as
                # ``raise_for_status`` does, so ``errors.py`` stays a leaf module.
                response_headers=redact_mapping(response.headers),
                request_info=response.request_info,
            )
            for message in messages:
                error.add_error(message)
            raise error
        return self._build_token_record(response.data, response)

    def _credentials_payload(self) -> dict[str, Any]:
        """Build the full-credentials token request body: the four fields the API takes."""
        return {
            "grant_type": self._config.grant_type,
            "client_id": self._config.client_id,
            "client_secret": self._config.client_secret,
            "redirect_uri": self._config.redirect_uri,
        }

    def _request_token_with_refresh_grant(self, refresh_token: str) -> TokenRecord | None:
        # No ``redirect_uri``: the refresh grant does not take one.
        payload = {
            "grant_type": _REFRESH_GRANT_TYPE,
            "client_id": self._config.client_id,
            "client_secret": self._config.client_secret,
            "refresh_token": refresh_token,
        }
        try:
            response = self._transport.send_http_request(
                "POST", self.token_url, json_body=payload, headers=self._token_headers()
            )
        except Exception:  # a failed refresh must fall back, not propagate
            return None
        if not response.succeeded:
            return None
        try:
            return self._build_token_record(
                response.data, response, previous_refresh_token=refresh_token
            )
        except SdkAuthError:
            return None

    def _token_headers(self) -> dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": self._config.user_agent,
        }

    def _build_token_record(
        self, body: Any, response: Any, *, previous_refresh_token: str | None = None
    ) -> TokenRecord:
        if not isinstance(body, dict) or not body.get("access_token"):
            raise SdkAuthError(
                "token response did not contain an access_token",
                status_code=response.status_code,
                raw_response=redact_value(body),
                request_info=response.request_info,
            )
        expires_in = body.get("expires_in")
        try:
            ttl_seconds = float(expires_in) if expires_in is not None else DEFAULT_TOKEN_TTL_SECONDS
        except (TypeError, ValueError):
            ttl_seconds = DEFAULT_TOKEN_TTL_SECONDS
        if not math.isfinite(ttl_seconds) or ttl_seconds <= 0:
            # ``float()`` and the JSON decoder both accept NaN and the infinities, and a
            # NaN expiry would read as fresh forever. A non-positive lifetime is expired
            # before it is returned.
            ttl_seconds = DEFAULT_TOKEN_TTL_SECONDS
        ttl_seconds = min(ttl_seconds, MAX_TOKEN_TTL_SECONDS)
        try:
            return TokenRecord(
                # Passed through, never ``str()``-ed: a JSON number is refused rather
                # than sent as ``Bearer 1234567890``.
                access_token=body["access_token"],
                # RFC 6749 §6 makes a new refresh token optional: without one, the one
                # already held is kept. Only the refresh path passes a previous token.
                refresh_token=body.get("refresh_token") or previous_refresh_token,
                expires_at=time.time() + ttl_seconds,
                # A lifetime shorter than the standing skew would leave no usable window.
                skew_seconds=min(EXPIRY_SKEW_SECONDS, ttl_seconds / 2),
            )
        except SdkUsageError as error:
            # An authentication failure, not a usage one: the grant answered with
            # something that cannot be sent as a credential.
            raise SdkAuthError(
                f"the token endpoint answered with a credential this SDK cannot "
                f"send - {error}",
                status_code=response.status_code,
                raw_response=redact_value(body),
                request_info=response.request_info,
            ) from None
