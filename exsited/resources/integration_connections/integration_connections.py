"""Integration connection endpoints, under ``/api/{api_version}/integration_connections``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.integration_connections import integration_connections_urls
from exsited.resources.integration_connections.integration_connections_dto import (
    IntegrationConnections,
)

__all__ = [
    "get_integration_connections",
    "get_integration_connection",
]


def get_integration_connections(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[IntegrationConnections]:
    """List connections - ``GET /integration_connections``; filter by status with
    ``filter_status`` (``filter_param("status")``): ACTIVE, INACTIVE or DISCONNECTED."""
    return client.send_get_request(
        integration_connections_urls.INTEGRATION_CONNECTIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=IntegrationConnections,
    )


def get_integration_connection(
    client: Any,
    integration_connection_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get single - ``GET /integration_connections/{integration_connection_id}``."""
    return client.send_get_request(
        integration_connections_urls.INTEGRATION_CONNECTION,
        path_params={"integration_connection_id": integration_connection_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )
