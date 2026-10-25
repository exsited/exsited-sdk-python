"""Client layer: the response record, the client, and the multi-client registry."""

from __future__ import annotations

from typing import Any

from exsited.client.api_response import ApiResponse, ErrorType, RequestInfo

_LAZY_EXPORTS = {
    "ExsitedClient": "exsited.client.exsited_client",
    "build_client": "exsited.client.exsited_client",
    "register_resource_module": "exsited.client.resource_binding",
    "BoundResource": "exsited.client.resource_binding",
    "ClientRegistry": "exsited.client.client_registry",
    "render_exchange": "exsited.client.console",
    "build_curl_command": "exsited.client.console",
}

__all__ = [
    "ApiResponse",
    "ErrorType",
    "RequestInfo",
    *_LAZY_EXPORTS,
]


def __getattr__(name: str) -> Any:
    """Resolve a lazily exported name on first access."""
    module_path = _LAZY_EXPORTS.get(name)
    if module_path is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    from importlib import import_module

    return getattr(import_module(module_path), name)


def __dir__() -> list[str]:
    return sorted(__all__)
