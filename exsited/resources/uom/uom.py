"""Unit of measurement endpoints, under ``/api/{api_version}/settings/uom``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.uom import uom_urls
from exsited.resources.uom.uom_dto import (
    SettingsUom,
    SettingsUomList,
)

__all__ = [
    "get_settings_uoms",
    "create_settings_uom",
    "get_settings_uom",
    "delete_settings_uom",
    "update_settings_uom",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

UomPayload = Mapping[str, Any] | str | Dto


def get_settings_uoms(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsUomList]:
    """List units of measurement - ``GET /settings/uom``."""
    return client.send_get_request(
        uom_urls.SETTINGS_UOMS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsUomList,
    )


def create_settings_uom(
    client: Any,
    payload: UomPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a unit of measurement - ``POST /settings/uom``; answers
    ``400`` ``validation_error``, naming no field, to every valid body."""
    _require_payload(payload)
    return client.send_post_request(
        uom_urls.SETTINGS_UOMS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_uom(
    client: Any,
    uom_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsUom]:
    """Get one unit of measurement - ``GET /settings/uom/{uom_id}``."""
    return client.send_get_request(
        uom_urls.SETTINGS_UOM,
        path_params={"uom_id": uom_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsUom,
    )


def delete_settings_uom(
    client: Any,
    uom_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a unit of measurement - ``DELETE /settings/uom/{uom_id}``."""
    return client.send_delete_request(
        uom_urls.SETTINGS_UOM,
        path_params={"uom_id": uom_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_uom(
    client: Any,
    uom_id: str,
    payload: UomPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update or enable/disable a unit of measurement - ``PATCH /settings/uom/{uom_id}``;
    ``status`` takes active or inactive."""
    _require_payload(payload)
    return client.send_patch_request(
        uom_urls.SETTINGS_UOM,
        path_params={"uom_id": uom_id},
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
