"""Additional code endpoints, under ``/api/{api_version}/settings/additional_codes``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.additional_codes import additional_codes_urls
from exsited.resources.additional_codes.additional_codes_dto import (
    SettingsAdditionalCode,
    SettingsAdditionalCodeList,
)

__all__ = [
    "get_settings_additional_codes",
    "create_settings_additional_code",
    "get_settings_additional_code",
    "delete_settings_additional_code",
    "update_settings_additional_code",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

AdditionalCodePayload = Mapping[str, Any] | str | Dto


def get_settings_additional_codes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAdditionalCodeList]:
    """List the additional codes, the data sets of purchase order lines -
    ``GET /settings/additional_codes``."""
    return client.send_get_request(
        additional_codes_urls.SETTINGS_ADDITIONAL_CODES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAdditionalCodeList,
    )


def create_settings_additional_code(
    client: Any,
    payload: AdditionalCodePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAdditionalCode]:
    """Create an additional code; ``name`` is required - ``POST /settings/additional_codes``."""
    _require_payload(payload)
    return client.send_post_request(
        additional_codes_urls.SETTINGS_ADDITIONAL_CODES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAdditionalCode,
    )


def get_settings_additional_code(
    client: Any,
    additional_code_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAdditionalCode]:
    """Read one additional code by its ``ac_`` id -
    ``GET /settings/additional_codes/{additional_code_id}``."""
    return client.send_get_request(
        additional_codes_urls.SETTINGS_ADDITIONAL_CODE,
        path_params={"additional_code_id": additional_code_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAdditionalCode,
    )


def delete_settings_additional_code(
    client: Any,
    additional_code_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an additional code - ``DELETE /settings/additional_codes/{additional_code_id}``."""
    return client.send_delete_request(
        additional_codes_urls.SETTINGS_ADDITIONAL_CODE,
        path_params={"additional_code_id": additional_code_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_additional_code(
    client: Any,
    additional_code_id: str,
    payload: AdditionalCodePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update an additional code's fields or its status -
    ``PATCH /settings/additional_codes/{additional_code_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        additional_codes_urls.SETTINGS_ADDITIONAL_CODE,
        path_params={"additional_code_id": additional_code_id},
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
