"""Approval profile endpoints, under ``/api/{api_version}/settings/approval_profiles``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.approval_profiles import approval_profiles_urls
from exsited.resources.approval_profiles.approval_profiles_dto import (
    SettingsApprovalProfile,
    SettingsApprovalProfileList,
)

__all__ = [
    "get_settings_approval_profiles",
    "create_settings_approval_profile",
    "get_settings_approval_profile",
    "delete_settings_approval_profile",
    "update_settings_approval_profile",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ApprovalProfilePayload = Mapping[str, Any] | str | Dto


def get_settings_approval_profiles(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApprovalProfileList]:
    """List the approval profiles - ``GET /settings/approval_profiles``."""
    return client.send_get_request(
        approval_profiles_urls.SETTINGS_APPROVAL_PROFILES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApprovalProfileList,
    )


def create_settings_approval_profile(
    client: Any,
    payload: ApprovalProfilePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create an approval profile; ``name``, ``entity``, ``event``, ``approver_type`` and
    ``approver`` are required - ``POST /settings/approval_profiles``."""
    _require_payload(payload)
    return client.send_post_request(
        approval_profiles_urls.SETTINGS_APPROVAL_PROFILES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_approval_profile(
    client: Any,
    approval_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApprovalProfile]:
    """Read one approval profile by its ``ap_`` id -
    ``GET /settings/approval_profiles/{approval_profile_id}``."""
    return client.send_get_request(
        approval_profiles_urls.SETTINGS_APPROVAL_PROFILE,
        path_params={"approval_profile_id": approval_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApprovalProfile,
    )


def delete_settings_approval_profile(
    client: Any,
    approval_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an approval profile that is not in use -
    ``DELETE /settings/approval_profiles/{approval_profile_id}``."""
    return client.send_delete_request(
        approval_profiles_urls.SETTINGS_APPROVAL_PROFILE,
        path_params={"approval_profile_id": approval_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_approval_profile(
    client: Any,
    approval_profile_id: str,
    payload: ApprovalProfilePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update an approval profile's fields or its status -
    ``PATCH /settings/approval_profiles/{approval_profile_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        approval_profiles_urls.SETTINGS_APPROVAL_PROFILE,
        path_params={"approval_profile_id": approval_profile_id},
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
