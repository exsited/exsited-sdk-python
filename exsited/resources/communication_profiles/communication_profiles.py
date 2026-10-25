"""Communication profile endpoints, under ``/api/{api_version}/settings/communication_profiles``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.communication_profiles import communication_profiles_urls
from exsited.resources.communication_profiles.communication_profiles_dto import (
    SettingsCommunicationProfile,
    SettingsCommunicationProfileList,
)

__all__ = [
    "get_settings_communication_profiles",
    "create_settings_communication_profile",
    "get_settings_communication_profile",
    "delete_settings_communication_profile",
    "update_settings_communication_profile",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

CommunicationProfilePayload = Mapping[str, Any] | str | Dto


def get_settings_communication_profiles(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCommunicationProfileList]:
    """List the communication profiles - ``GET /settings/communication_profiles``."""
    return client.send_get_request(
        communication_profiles_urls.SETTINGS_COMMUNICATION_PROFILES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCommunicationProfileList,
    )


def create_settings_communication_profile(
    client: Any,
    payload: CommunicationProfilePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a communication profile; ``name`` is required, and its messages are copied from
    ``copy_from`` or else from the default profile - ``POST /settings/communication_profiles``."""
    _require_payload(payload)
    return client.send_post_request(
        communication_profiles_urls.SETTINGS_COMMUNICATION_PROFILES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_communication_profile(
    client: Any,
    communication_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCommunicationProfile]:
    """Read one communication profile by its ``cmp_`` id -
    ``GET /settings/communication_profiles/{communication_profile_id}``."""
    return client.send_get_request(
        communication_profiles_urls.SETTINGS_COMMUNICATION_PROFILE,
        path_params={"communication_profile_id": communication_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCommunicationProfile,
    )


def delete_settings_communication_profile(
    client: Any,
    communication_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a communication profile that is not the default -
    ``DELETE /settings/communication_profiles/{communication_profile_id}``."""
    return client.send_delete_request(
        communication_profiles_urls.SETTINGS_COMMUNICATION_PROFILE,
        path_params={"communication_profile_id": communication_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_communication_profile(
    client: Any,
    communication_profile_id: str,
    payload: CommunicationProfilePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update a communication profile's fields and channel settings -
    ``PATCH /settings/communication_profiles/{communication_profile_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        communication_profiles_urls.SETTINGS_COMMUNICATION_PROFILE,
        path_params={"communication_profile_id": communication_profile_id},
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
