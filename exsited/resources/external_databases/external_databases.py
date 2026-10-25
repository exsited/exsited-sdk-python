"""External database endpoints, under ``/api/{api_version}/external_databases``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.external_databases import external_databases_urls
from exsited.resources.external_databases.external_databases_dto import (
    ExternalDatabaseInsertRecord,
    ExternalDatabases,
    ExternalDatabaseSearch,
    ExternalDatabasesView,
    ExternalDatabaseUpdateRecordsUpdated,
)

__all__ = [
    "get_external_databases",
    "create_external_database",
    "get_external_database",
    "create_external_database_insert_record",
    "create_external_database_search",
    "update_external_database_update_records",
    "get_external_database_table",
]

ExternalDatabasePayload = Mapping[str, Any] | str | Dto


def get_external_databases(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ExternalDatabases]:
    """List databases - ``GET /external_databases``."""
    return client.send_get_request(
        external_databases_urls.EXTERNAL_DATABASES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ExternalDatabases,
    )


def create_external_database(
    client: Any,
    payload: ExternalDatabasePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ExternalDatabasesView]:
    """Create a database and its tables - ``POST /external_databases``."""
    _require_payload(payload)
    return client.send_post_request(
        external_databases_urls.EXTERNAL_DATABASES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ExternalDatabasesView,
    )


def get_external_database(
    client: Any,
    db_name: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ExternalDatabases]:
    """Get single database - ``GET /external_databases/{db_name}``."""
    return client.send_get_request(
        external_databases_urls.EXTERNAL_DATABASE,
        path_params={"db_name": db_name},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ExternalDatabases,
    )


def create_external_database_insert_record(
    client: Any,
    db_name: str,
    payload: ExternalDatabasePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ExternalDatabaseInsertRecord]:
    """Insert records - ``POST /external_databases/{db_name}/insert_records``."""
    _require_payload(payload)
    return client.send_post_request(
        external_databases_urls.EXTERNAL_DATABASE_INSERT_RECORDS,
        path_params={"db_name": db_name},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ExternalDatabaseInsertRecord,
    )


def create_external_database_search(
    client: Any,
    db_name: str,
    payload: ExternalDatabasePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ExternalDatabaseSearch]:
    """Search records - ``POST /external_databases/{db_name}/search``."""
    _require_payload(payload)
    return client.send_post_request(
        external_databases_urls.EXTERNAL_DATABASE_SEARCH,
        path_params={"db_name": db_name},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ExternalDatabaseSearch,
    )


def update_external_database_update_records(
    client: Any,
    db_name: str,
    payload: ExternalDatabasePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ExternalDatabaseUpdateRecordsUpdated]:
    """Update records - ``PATCH /external_databases/{db_name}/update_records``."""
    _require_payload(payload)
    return client.send_patch_request(
        external_databases_urls.EXTERNAL_DATABASE_UPDATE_RECORDS,
        path_params={"db_name": db_name},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ExternalDatabaseUpdateRecordsUpdated,
    )


def get_external_database_table(
    client: Any,
    db_name: str,
    table_name: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ExternalDatabases]:
    """Get table columns - ``GET /external_databases/{db_name}/tables/{table_name}``."""
    return client.send_get_request(
        external_databases_urls.EXTERNAL_DATABASE_TABLE,
        path_params={"db_name": db_name, "table_name": table_name},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ExternalDatabases,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
