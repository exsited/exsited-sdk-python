"""Typed views over the external database bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "ExternalDatabases",
    "ExternalDatabasesView",
    "ExternalDatabaseInsertRecord",
    "ExternalDatabaseSearch",
    "ExternalDatabaseUpdateRecordsUpdated",
]


class ExternalDatabases(Dto):
    """The external databases body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/external_databases",
        "GET /api/{api_version}/external_databases/{db_name}",
        "GET /api/{api_version}/external_databases/{db_name}/tables/{table_name}",
    )

    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ExternalDatabasesView(Dto):
    """What ``create_external_database`` answers, under ``external_database``."""

    MEASURED_FROM = ("POST /api/{api_version}/external_databases",)

    ENVELOPE_KEY = "external_database"

    activity_logs: list[Any] | None = None
    message: str | None = None
    name: str | None = None


class ExternalDatabaseInsertRecord(Dto):
    """What ``create_external_database_insert_record`` answers, under ``external_database``."""

    MEASURED_FROM = ("POST /api/{api_version}/external_databases/{db_name}/insert_records",)

    ENVELOPE_KEY = "external_database"

    inserted_data: list[Any] | None = None
    message: str | None = None
    success: bool | None = None


class ExternalDatabaseSearch(Dto):
    """What ``create_external_database_search`` answers, under ``external_database``."""

    MEASURED_FROM = ("POST /api/{api_version}/external_databases/{db_name}/search",)

    ENVELOPE_KEY = "external_database"

    count: int | None = None
    limit: int | None = None
    list: dict[str, Any] | None = None
    offset: int | None = None
    success: bool | None = None


class ExternalDatabaseUpdateRecordsUpdated(Dto):
    """What ``update_external_database_update_records`` answers, under ``external_database``."""

    MEASURED_FROM = ("PATCH /api/{api_version}/external_databases/{db_name}/update_records",)

    ENVELOPE_KEY = "external_database"

    message: str | None = None
