"""Fulfillment profile endpoints, under ``/api/{api_version}/settings/fulfillment_profiles``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.fulfillment_profiles import fulfillment_profiles_urls
from exsited.resources.fulfillment_profiles.fulfillment_profiles_dto import (
    SettingsFulfillmentProfile,
    SettingsFulfillmentProfileList,
)

__all__ = [
    "get_settings_fulfillment_profiles",
    "create_settings_fulfillment_profile",
    "get_settings_fulfillment_profile",
    "delete_settings_fulfillment_profile",
    "update_settings_fulfillment_profile",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

FulfillmentProfilePayload = Mapping[str, Any] | str | Dto


def get_settings_fulfillment_profiles(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFulfillmentProfileList]:
    """List fulfillment profiles - ``GET /settings/fulfillment_profiles``."""
    return client.send_get_request(
        fulfillment_profiles_urls.SETTINGS_FULFILLMENT_PROFILES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFulfillmentProfileList,
    )


def create_settings_fulfillment_profile(
    client: Any,
    payload: FulfillmentProfilePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFulfillmentProfile]:
    """Create a fulfillment profile - ``POST /settings/fulfillment_profiles``; ``statuses``
    needs one entry at least."""
    _require_payload(payload)
    return client.send_post_request(
        fulfillment_profiles_urls.SETTINGS_FULFILLMENT_PROFILES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFulfillmentProfile,
    )


def get_settings_fulfillment_profile(
    client: Any,
    fulfillment_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFulfillmentProfile]:
    """Get one fulfillment profile - ``GET
    /settings/fulfillment_profiles/{fulfillment_profile_id}``."""
    return client.send_get_request(
        fulfillment_profiles_urls.SETTINGS_FULFILLMENT_PROFILE,
        path_params={"fulfillment_profile_id": fulfillment_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFulfillmentProfile,
    )


def delete_settings_fulfillment_profile(
    client: Any,
    fulfillment_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a fulfillment profile - ``DELETE
    /settings/fulfillment_profiles/{fulfillment_profile_id}``."""
    return client.send_delete_request(
        fulfillment_profiles_urls.SETTINGS_FULFILLMENT_PROFILE,
        path_params={"fulfillment_profile_id": fulfillment_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_fulfillment_profile(
    client: Any,
    fulfillment_profile_id: str,
    payload: FulfillmentProfilePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFulfillmentProfile]:
    """Update a fulfillment profile - ``PATCH
    /settings/fulfillment_profiles/{fulfillment_profile_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        fulfillment_profiles_urls.SETTINGS_FULFILLMENT_PROFILE,
        path_params={"fulfillment_profile_id": fulfillment_profile_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFulfillmentProfile,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
