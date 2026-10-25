"""Typed views over the billing period bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsBillingPeriod",
    "SettingsBillingPeriodList",
]


class SettingsBillingPeriod(Dto):
    """The settings billing period body, under ``billing_period``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/billing_periods",
        "GET /api/{api_version}/settings/billing_periods/{billing_period_id}",
        "POST /api/{api_version}/settings/billing_periods",
        "PATCH /api/{api_version}/settings/billing_periods/{billing_period_id}",
    )

    ENVELOPE_KEY = "billing_period"

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
    ordering: int | None = None
    period: str | None = None
    status: str | None = None
    time_period: str | None = None


class SettingsBillingPeriodList(Dto):
    """One page of ``SettingsBillingPeriod`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/billing_periods",)

    data: list[SettingsBillingPeriod] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
