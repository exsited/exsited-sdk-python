"""Typed views over the system event bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsSystemEvent",
    "SettingsSystemEventList",
]


class SettingsSystemEvent(Dto):
    """The settings system event body, under ``system_event``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/system_events",
        "GET /api/{api_version}/settings/system_events/{system_event_id}",
    )

    ENVELOPE_KEY = "system_event"

    base_event: bool | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsSystemEventList(Dto):
    """One page of ``SettingsSystemEvent`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/system_events",)

    data: list[SettingsSystemEvent] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
