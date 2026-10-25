"""Billing period endpoints, under ``/api/{api_version}/settings/billing_periods``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.billing_periods import billing_periods_urls
from exsited.resources.billing_periods.billing_periods_dto import (
    SettingsBillingPeriod,
    SettingsBillingPeriodList,
)

__all__ = [
    "get_settings_billing_periods",
    "create_settings_billing_period",
    "get_settings_billing_period",
    "delete_settings_billing_period",
    "update_settings_billing_period",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

BillingPeriodPayload = Mapping[str, Any] | str | Dto


def get_settings_billing_periods(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsBillingPeriodList]:
    """List the billing periods - ``GET /settings/billing_periods``."""
    return client.send_get_request(
        billing_periods_urls.SETTINGS_BILLING_PERIODS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsBillingPeriodList,
    )


def create_settings_billing_period(
    client: Any,
    payload: BillingPeriodPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsBillingPeriod]:
    """Create a billing period; ``name`` and ``time_period`` are required, and ``time_period`` is
    the time period's hyphenated uuid, not its ``tp_`` id - ``POST /settings/billing_periods``."""
    _require_payload(payload)
    return client.send_post_request(
        billing_periods_urls.SETTINGS_BILLING_PERIODS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsBillingPeriod,
    )


def get_settings_billing_period(
    client: Any,
    billing_period_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsBillingPeriod]:
    """Read one billing period by its ``bp_`` id -
    ``GET /settings/billing_periods/{billing_period_id}``."""
    return client.send_get_request(
        billing_periods_urls.SETTINGS_BILLING_PERIOD,
        path_params={"billing_period_id": billing_period_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsBillingPeriod,
    )


def delete_settings_billing_period(
    client: Any,
    billing_period_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a billing period - ``DELETE /settings/billing_periods/{billing_period_id}``."""
    return client.send_delete_request(
        billing_periods_urls.SETTINGS_BILLING_PERIOD,
        path_params={"billing_period_id": billing_period_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_billing_period(
    client: Any,
    billing_period_id: str,
    payload: BillingPeriodPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsBillingPeriod]:
    """Update a billing period; the answer carries ``time_period`` in place of ``period`` and
    ``duration`` - ``PATCH /settings/billing_periods/{billing_period_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        billing_periods_urls.SETTINGS_BILLING_PERIOD,
        path_params={"billing_period_id": billing_period_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsBillingPeriod,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
