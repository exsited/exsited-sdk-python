"""Charging period endpoints, under ``/api/{api_version}/settings/charging_periods``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.charging_periods import charging_periods_urls
from exsited.resources.charging_periods.charging_periods_dto import (
    SettingsChargingPeriod,
    SettingsChargingPeriodList,
)

__all__ = [
    "get_settings_charging_periods",
    "create_settings_charging_period",
    "get_settings_charging_period",
    "delete_settings_charging_period",
    "update_settings_charging_period",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ChargingPeriodPayload = Mapping[str, Any] | str | Dto


def get_settings_charging_periods(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsChargingPeriodList]:
    """List the charging periods - ``GET /settings/charging_periods``."""
    return client.send_get_request(
        charging_periods_urls.SETTINGS_CHARGING_PERIODS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsChargingPeriodList,
    )


def create_settings_charging_period(
    client: Any,
    payload: ChargingPeriodPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsChargingPeriod]:
    """Create a charging period; ``name``, ``display_name`` and ``time_period``, a ``tp_`` id,
    are required - ``POST /settings/charging_periods``."""
    _require_payload(payload)
    return client.send_post_request(
        charging_periods_urls.SETTINGS_CHARGING_PERIODS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsChargingPeriod,
    )


def get_settings_charging_period(
    client: Any,
    charging_period_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsChargingPeriod]:
    """Read one charging period by its ``cp_`` id -
    ``GET /settings/charging_periods/{charging_period_id}``."""
    return client.send_get_request(
        charging_periods_urls.SETTINGS_CHARGING_PERIOD,
        path_params={"charging_period_id": charging_period_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsChargingPeriod,
    )


def delete_settings_charging_period(
    client: Any,
    charging_period_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a charging period - ``DELETE /settings/charging_periods/{charging_period_id}``."""
    return client.send_delete_request(
        charging_periods_urls.SETTINGS_CHARGING_PERIOD,
        path_params={"charging_period_id": charging_period_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_charging_period(
    client: Any,
    charging_period_id: str,
    payload: ChargingPeriodPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsChargingPeriod]:
    """Update a charging period's fields or its status -
    ``PATCH /settings/charging_periods/{charging_period_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        charging_periods_urls.SETTINGS_CHARGING_PERIOD,
        path_params={"charging_period_id": charging_period_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsChargingPeriod,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
