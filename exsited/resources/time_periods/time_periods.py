"""Time period endpoints, under ``/api/{api_version}/settings/time_periods``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.time_periods import time_periods_urls
from exsited.resources.time_periods.time_periods_dto import (
    SettingsTimePeriod,
    SettingsTimePeriodList,
)

__all__ = [
    "get_settings_time_periods",
    "create_settings_time_period",
    "get_settings_time_period",
    "delete_settings_time_period",
    "update_settings_time_period",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

TimePeriodPayload = Mapping[str, Any] | str | Dto


def get_settings_time_periods(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTimePeriodList]:
    """List time periods - ``GET /settings/time_periods``."""
    return client.send_get_request(
        time_periods_urls.SETTINGS_TIME_PERIODS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTimePeriodList,
    )


def create_settings_time_period(
    client: Any,
    payload: TimePeriodPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTimePeriod]:
    """Create a time period - ``POST /settings/time_periods``; ``period`` is sent upper case and
    answered lower case."""
    _require_payload(payload)
    return client.send_post_request(
        time_periods_urls.SETTINGS_TIME_PERIODS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTimePeriod,
    )


def get_settings_time_period(
    client: Any,
    time_period_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTimePeriod]:
    """Get one time period - ``GET /settings/time_periods/{time_period_id}``."""
    return client.send_get_request(
        time_periods_urls.SETTINGS_TIME_PERIOD,
        path_params={"time_period_id": time_period_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTimePeriod,
    )


def delete_settings_time_period(
    client: Any,
    time_period_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a time period - ``DELETE /settings/time_periods/{time_period_id}``."""
    return client.send_delete_request(
        time_periods_urls.SETTINGS_TIME_PERIOD,
        path_params={"time_period_id": time_period_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_time_period(
    client: Any,
    time_period_id: str,
    payload: TimePeriodPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTimePeriod]:
    """Update or enable/disable a time period - ``PATCH
    /settings/time_periods/{time_period_id}``; ``status`` takes active or inactive."""
    _require_payload(payload)
    return client.send_patch_request(
        time_periods_urls.SETTINGS_TIME_PERIOD,
        path_params={"time_period_id": time_period_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTimePeriod,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
