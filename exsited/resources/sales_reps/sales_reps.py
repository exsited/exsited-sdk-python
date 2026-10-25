"""Sales rep endpoints, under ``/api/{api_version}/settings/sales_reps``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.sales_reps import sales_reps_urls
from exsited.resources.sales_reps.sales_reps_dto import (
    SettingsSalesRep,
    SettingsSalesRepList,
)

__all__ = [
    "get_settings_sales_reps",
    "create_settings_sales_rep",
    "get_settings_sales_rep",
    "delete_settings_sales_rep",
    "update_settings_sales_rep",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

SalesRepPayload = Mapping[str, Any] | str | Dto


def get_settings_sales_reps(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsSalesRepList]:
    """List sales reps - ``GET /settings/sales_reps``."""
    return client.send_get_request(
        sales_reps_urls.SETTINGS_SALES_REPS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsSalesRepList,
    )


def create_settings_sales_rep(
    client: Any,
    payload: SalesRepPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a sales rep - ``POST /settings/sales_reps``; answers ``400``
    ``validation_error``, naming no field, to every valid body."""
    _require_payload(payload)
    return client.send_post_request(
        sales_reps_urls.SETTINGS_SALES_REPS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_sales_rep(
    client: Any,
    sales_rep_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsSalesRep]:
    """Get one sales rep - ``GET /settings/sales_reps/{sales_rep_id}``."""
    return client.send_get_request(
        sales_reps_urls.SETTINGS_SALES_REP,
        path_params={"sales_rep_id": sales_rep_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsSalesRep,
    )


def delete_settings_sales_rep(
    client: Any,
    sales_rep_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a sales rep - ``DELETE /settings/sales_reps/{sales_rep_id}``."""
    return client.send_delete_request(
        sales_reps_urls.SETTINGS_SALES_REP,
        path_params={"sales_rep_id": sales_rep_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_sales_rep(
    client: Any,
    sales_rep_id: str,
    payload: SalesRepPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update or enable/disable a sales rep - ``PATCH /settings/sales_reps/{sales_rep_id}``;
    ``status`` takes active or inactive."""
    _require_payload(payload)
    return client.send_patch_request(
        sales_reps_urls.SETTINGS_SALES_REP,
        path_params={"sales_rep_id": sales_rep_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
