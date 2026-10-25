"""Typed views over the designation bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsDesignation",
    "SettingsDesignationList",
]


class SettingsDesignation(Dto):
    """The settings designation body, under ``designation``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/designations",
        "GET /api/{api_version}/settings/designations/{designation_id}",
    )

    ENVELOPE_KEY = "designation"

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


class SettingsDesignationList(Dto):
    """One page of ``SettingsDesignation`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/designations",)

    data: list[SettingsDesignation] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
