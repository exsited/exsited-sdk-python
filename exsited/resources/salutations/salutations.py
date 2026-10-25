"""Salutation endpoints, under ``/api/{api_version}/settings/salutations``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.salutations import salutations_urls
from exsited.resources.salutations.salutations_dto import (
    SettingsSalutation,
    SettingsSalutationList,
)

__all__ = [
    "get_settings_salutations",
    "create_settings_salutation",
    "get_settings_salutation",
    "delete_settings_salutation",
    "update_settings_salutation",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

SalutationPayload = Mapping[str, Any] | str | Dto


def get_settings_salutations(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsSalutationList]:
    """List salutations - ``GET /settings/salutations``."""
    return client.send_get_request(
        salutations_urls.SETTINGS_SALUTATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsSalutationList,
    )


def create_settings_salutation(
    client: Any,
    payload: SalutationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsSalutation]:
    """Create a salutation - ``POST /settings/salutations``."""
    _require_payload(payload)
    return client.send_post_request(
        salutations_urls.SETTINGS_SALUTATIONS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsSalutation,
    )


def get_settings_salutation(
    client: Any,
    salutation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsSalutation]:
    """Get one salutation - ``GET /settings/salutations/{salutation_id}``."""
    return client.send_get_request(
        salutations_urls.SETTINGS_SALUTATION,
        path_params={"salutation_id": salutation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsSalutation,
    )


def delete_settings_salutation(
    client: Any,
    salutation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a salutation - ``DELETE /settings/salutations/{salutation_id}``."""
    return client.send_delete_request(
        salutations_urls.SETTINGS_SALUTATION,
        path_params={"salutation_id": salutation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_salutation(
    client: Any,
    salutation_id: str,
    payload: SalutationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsSalutation]:
    """Update a salutation - ``PATCH /settings/salutations/{salutation_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        salutations_urls.SETTINGS_SALUTATION,
        path_params={"salutation_id": salutation_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsSalutation,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
