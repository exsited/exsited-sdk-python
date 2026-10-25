"""Exsited Python SDK - a thin, predictable HTTP layer."""

from __future__ import annotations

import logging

# The token cache and lock errors and warnings are declared beside the auth code they describe.
from exsited.auth.token_provider import (
    DegradedTokenCacheWarning,
    TokenProvider,
    TokenRecord,
    build_token_path,
)
from exsited.auth.token_store import (
    DegradedTokenLockWarning,
    FileTokenStore,
    MemoryTokenStore,
    SdkTokenCacheError,
    SdkTokenLockError,
    TokenStore,
    build_credentials_namespace,
    build_default_token_cache_path,
)
from exsited.client.api_response import ApiResponse, ErrorType, RequestInfo
from exsited.client.client_registry import (
    ClientRegistry,
    get_registered_instances,
    list_instance_names,
    register_instances,
)
from exsited.client.console import build_curl_command, render_exchange
from exsited.client.exsited_client import ExsitedClient, build_client
from exsited.client.pagination import iter_pages, iter_records
from exsited.client.resource_binding import (
    BoundResource,
    register_resource_module,
    registered_resource_names,
)
from exsited.config.auth_config import USE_DEFAULT_TOKEN_CACHE, AuthConfig
from exsited.config.sdk_config import (
    DEFAULT_RESPONSE_FORMAT,
    DEFAULT_RETRYABLE_HTTP_CODES,
    DEFAULT_UNSAFE_RETRYABLE_HTTP_CODES,
    RESPONSE_FORMAT_ENV_VAR,
    SDK_VERSION,
    VALID_RESPONSE_FORMATS,
    SdkConfig,
    read_client_name,
    select_credentials,
)
from exsited.dto import Dto
from exsited.errors import (
    DIAGNOSTICS_ENVIRONMENT_VARIABLE,
    InsecureTransportWarning,
    SdkAttributeError,
    SdkAuthError,
    SdkConfigError,
    SdkError,
    SdkUsageError,
    error_diagnostics_enabled,
    set_error_diagnostics,
)
from exsited.http.query_params import (
    FILTER_OPERATORS,
    LIST_OPERATORS,
    PRESENCE_OPERATORS,
    SortDirection,
    build_query_params,
    filter_param,
    filter_values,
    sort_param,
)
from exsited.http.retry_policy import RetryPolicy
from exsited.http.transport import Transport
from exsited.http.url_builder import build_url, substitute_path_params
from exsited.redaction import (
    CIRCULAR,
    MAX_REDACTION_DEPTH,
    REDACTED,
    SENSITIVE_KEY_MARKERS,
    TOO_DEEP,
    redact_mapping,
    redact_text,
    redact_value,
    should_redact,
)

__version__ = SDK_VERSION

# Also disables logging.lastResort.
logging.getLogger("exsited").addHandler(logging.NullHandler())

__all__ = [
    "__version__",
    "SDK_VERSION",
    "AuthConfig",
    "USE_DEFAULT_TOKEN_CACHE",
    "SdkConfig",
    "DEFAULT_RETRYABLE_HTTP_CODES",
    "DEFAULT_UNSAFE_RETRYABLE_HTTP_CODES",
    "DEFAULT_RESPONSE_FORMAT",
    "VALID_RESPONSE_FORMATS",
    "RESPONSE_FORMAT_ENV_VAR",
    "select_credentials",
    "read_client_name",
    "ExsitedClient",
    "build_client",
    "ClientRegistry",
    "register_instances",
    "list_instance_names",
    "get_registered_instances",
    "register_resource_module",
    "registered_resource_names",
    "BoundResource",
    "render_exchange",
    "build_curl_command",
    "iter_pages",
    "iter_records",
    "REDACTED",
    "SENSITIVE_KEY_MARKERS",
    "TOO_DEEP",
    "CIRCULAR",
    "MAX_REDACTION_DEPTH",
    "should_redact",
    "redact_value",
    "redact_mapping",
    "redact_text",
    "ApiResponse",
    "RequestInfo",
    "ErrorType",
    "Dto",
    "SdkError",
    "SdkConfigError",
    "SdkUsageError",
    "SdkAttributeError",
    "SdkAuthError",
    "SdkTokenCacheError",
    "SdkTokenLockError",
    "InsecureTransportWarning",
    "DegradedTokenLockWarning",
    "DegradedTokenCacheWarning",
    "error_diagnostics_enabled",
    "set_error_diagnostics",
    "DIAGNOSTICS_ENVIRONMENT_VARIABLE",
    "TokenProvider",
    "TokenRecord",
    "TokenStore",
    "MemoryTokenStore",
    "FileTokenStore",
    "build_credentials_namespace",
    "build_default_token_cache_path",
    "build_token_path",
    "Transport",
    "RetryPolicy",
    "SortDirection",
    "FILTER_OPERATORS",
    "PRESENCE_OPERATORS",
    "LIST_OPERATORS",
    "build_query_params",
    "filter_param",
    "filter_values",
    "sort_param",
    "build_url",
    "substitute_path_params",
]
