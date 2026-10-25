"""Typed views over the zone bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsZone",
    "SettingsZoneList",
]


class SettingsZone(Dto):
    """The settings zone body, under ``zone``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/zones",
        "GET /api/{api_version}/settings/zones/{zone_id}",
        "POST /api/{api_version}/settings/zones",
        "PATCH /api/{api_version}/settings/zones/{zone_id}",
    )

    ENVELOPE_KEY = "zone"

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


class SettingsZoneList(Dto):
    """One page of ``SettingsZone`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/zones",)

    data: list[SettingsZone] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
