"""Typed views over the pricing period bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsPricingPeriod",
    "SettingsPricingPeriodList",
    "SettingsPricingPeriodTimePeriod",
]


class SettingsPricingPeriod(Dto):
    """The settings pricing period body, under ``pricing_period``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/pricing_periods",
        "GET /api/{api_version}/settings/pricing_periods/{pricing_period_id}",
        "POST /api/{api_version}/settings/pricing_periods",
        "PATCH /api/{api_version}/settings/pricing_periods/{pricing_period_id}",
    )

    ENVELOPE_KEY = "pricing_period"

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
    time_period: SettingsPricingPeriodTimePeriod | None = None


class SettingsPricingPeriodList(Dto):
    """One page of ``SettingsPricingPeriod`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/pricing_periods",)

    data: list[SettingsPricingPeriod] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsPricingPeriodTimePeriod(Dto):
    """A :class:`SettingsPricingPeriod`'s ``time_period``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
