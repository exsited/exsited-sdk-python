"""Typed views over the country bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsCountry",
    "SettingsCountryList",
]


class SettingsCountry(Dto):
    """The settings country body, under ``country``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/countries",
        "GET /api/{api_version}/settings/countries/{country_id}",
        "PATCH /api/{api_version}/settings/countries/{country_id}",
    )

    ENVELOPE_KEY = "country"

    code: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    default_area_code: Any = None
    default_city: str | None = None
    default_post_code: str | None = None
    default_state: str | None = None
    description: str | None = None
    display_name: str | None = None
    flag_exists: bool | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsCountryList(Dto):
    """One page of ``SettingsCountry`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/countries",)

    data: list[SettingsCountry] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
