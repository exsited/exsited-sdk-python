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


    ENVELOPE_KEY = "zone"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsZoneList(Dto):
    """One page of ``SettingsZone`` records, under ``data``."""


    data: list[SettingsZone] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
