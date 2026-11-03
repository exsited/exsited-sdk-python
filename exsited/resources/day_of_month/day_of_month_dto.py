"""Typed views over the day of month bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsDayOfMonth",
    "SettingsDayOfMonthList",
]


class SettingsDayOfMonth(Dto):
    """The settings day of month body, under ``day_of_month``."""


    ENVELOPE_KEY = "day_of_month"

    created_by: Any = None
    created_on: str | None = None
    day: int | None = None
    description: Any = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsDayOfMonthList(Dto):
    """One page of ``SettingsDayOfMonth`` records, under ``data``."""


    data: list[SettingsDayOfMonth] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
