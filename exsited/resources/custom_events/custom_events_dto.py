"""Typed views over the custom event bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsCustomEvent",
    "SettingsCustomEventList",
]


class SettingsCustomEvent(Dto):
    """The settings custom event body, under ``custom_event``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/custom_events",
        "GET /api/{api_version}/settings/custom_events/{custom_event_id}",
    )

    ENVELOPE_KEY = "custom_event"

    base_event: bool | None = None
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


class SettingsCustomEventList(Dto):
    """One page of ``SettingsCustomEvent`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/custom_events",)

    data: list[SettingsCustomEvent] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
