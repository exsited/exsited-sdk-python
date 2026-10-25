"""Pricing period endpoints, under ``/api/{api_version}/settings/pricing_periods``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.pricing_periods import pricing_periods_urls
from exsited.resources.pricing_periods.pricing_periods_dto import (
    SettingsPricingPeriod,
    SettingsPricingPeriodList,
)

__all__ = [
    "get_settings_pricing_periods",
    "create_settings_pricing_period",
    "get_settings_pricing_period",
    "delete_settings_pricing_period",
    "update_settings_pricing_period",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

PricingPeriodPayload = Mapping[str, Any] | str | Dto


def get_settings_pricing_periods(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPricingPeriodList]:
    """List pricing periods - ``GET /settings/pricing_periods``; ``time_period`` reads null
    here, whatever the record holds."""
    return client.send_get_request(
        pricing_periods_urls.SETTINGS_PRICING_PERIODS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPricingPeriodList,
    )


def create_settings_pricing_period(
    client: Any,
    payload: PricingPeriodPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPricingPeriod]:
    """Create a pricing period - ``POST /settings/pricing_periods``."""
    _require_payload(payload)
    return client.send_post_request(
        pricing_periods_urls.SETTINGS_PRICING_PERIODS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPricingPeriod,
    )


def get_settings_pricing_period(
    client: Any,
    pricing_period_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPricingPeriod]:
    """Get one pricing period - ``GET /settings/pricing_periods/{pricing_period_id}``;
    ``time_period`` reads null here, whatever the record holds."""
    return client.send_get_request(
        pricing_periods_urls.SETTINGS_PRICING_PERIOD,
        path_params={"pricing_period_id": pricing_period_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPricingPeriod,
    )


def delete_settings_pricing_period(
    client: Any,
    pricing_period_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a pricing period - ``DELETE /settings/pricing_periods/{pricing_period_id}``."""
    return client.send_delete_request(
        pricing_periods_urls.SETTINGS_PRICING_PERIOD,
        path_params={"pricing_period_id": pricing_period_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_pricing_period(
    client: Any,
    pricing_period_id: str,
    payload: PricingPeriodPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPricingPeriod]:
    """Update or enable/disable a pricing period - ``PATCH
    /settings/pricing_periods/{pricing_period_id}``; ``status`` takes active or inactive."""
    _require_payload(payload)
    return client.send_patch_request(
        pricing_periods_urls.SETTINGS_PRICING_PERIOD,
        path_params={"pricing_period_id": pricing_period_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPricingPeriod,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
