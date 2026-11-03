"""Typed views over the charging period bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsChargingPeriod",
    "SettingsChargingPeriodList",
    "SettingsChargingPeriodTimePeriod",
]


class SettingsChargingPeriod(Dto):
    """The settings charging period body, under ``charging_period``."""


    ENVELOPE_KEY = "charging_period"

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
    time_period: SettingsChargingPeriodTimePeriod | None = None


class SettingsChargingPeriodList(Dto):
    """One page of ``SettingsChargingPeriod`` records, under ``data``."""


    data: list[SettingsChargingPeriod] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsChargingPeriodTimePeriod(Dto):
    """A :class:`SettingsChargingPeriod`'s ``time_period``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
