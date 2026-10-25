"""Typed views over the time period bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsTimePeriod",
    "SettingsTimePeriodList",
]


class SettingsTimePeriod(Dto):
    """The settings time period body, under ``time_period``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/time_periods",
        "GET /api/{api_version}/settings/time_periods/{time_period_id}",
        "POST /api/{api_version}/settings/time_periods",
        "PATCH /api/{api_version}/settings/time_periods/{time_period_id}",
    )

    ENVELOPE_KEY = "time_period"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    duration: int | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    period: str | None = None
    status: str | None = None


class SettingsTimePeriodList(Dto):
    """One page of ``SettingsTimePeriod`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/time_periods",)

    data: list[SettingsTimePeriod] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
