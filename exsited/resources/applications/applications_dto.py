"""Typed views over the application bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsApplication",
    "SettingsApplicationList",
]


class SettingsApplication(Dto):
    """The settings application body, under ``application``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/applications",
        "GET /api/{api_version}/settings/applications/{application_id}",
        "POST /api/{api_version}/settings/applications",
        "PATCH /api/{api_version}/settings/applications/{application_id}",
    )

    ENVELOPE_KEY = "application"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsApplicationList(Dto):
    """One page of ``SettingsApplication`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/applications",)

    data: list[SettingsApplication] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
