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


    ENVELOPE_KEY = "billing_period"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    duration: int | None = None
    href: str | None = None
    id: str | None = None
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


    data: list[SettingsBillingPeriod] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
