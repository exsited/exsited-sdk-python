"""Day of month endpoints, under ``/api/{api_version}/settings/day_of_month``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.day_of_month import day_of_month_urls
from exsited.resources.day_of_month.day_of_month_dto import (
    SettingsDayOfMonth,
    SettingsDayOfMonthList,
)

__all__ = [
    "get_settings_days_of_month",
    "get_settings_day_of_month",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_settings_days_of_month(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDayOfMonthList]:
    """List the days of the month a date can be aligned to - ``GET /settings/day_of_month``."""
    return client.send_get_request(
        day_of_month_urls.SETTINGS_DAYS_OF_MONTH,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDayOfMonthList,
    )


def get_settings_day_of_month(
    client: Any,
    day_of_month_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDayOfMonth]:
    """Read one day of the month by its ``dom_`` id -
    ``GET /settings/day_of_month/{day_of_month_id}``."""
    return client.send_get_request(
        day_of_month_urls.SETTINGS_DAY_OF_MONTH,
        path_params={"day_of_month_id": day_of_month_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDayOfMonth,
    )
