"""Approval user group endpoints, under ``/api/{api_version}/settings/approval_user_groups``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.approval_user_groups import approval_user_groups_urls
from exsited.resources.approval_user_groups.approval_user_groups_dto import (
    SettingsApprovalUserGroup,
    SettingsApprovalUserGroupList,
)

__all__ = [
    "get_settings_approval_user_groups",
    "create_settings_approval_user_group",
    "get_settings_approval_user_group",
    "delete_settings_approval_user_group",
    "update_settings_approval_user_group",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ApprovalUserGroupPayload = Mapping[str, Any] | str | Dto


def get_settings_approval_user_groups(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApprovalUserGroupList]:
    """List the approval user groups - ``GET /settings/approval_user_groups``."""
    return client.send_get_request(
        approval_user_groups_urls.SETTINGS_APPROVAL_USER_GROUPS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApprovalUserGroupList,
    )


def create_settings_approval_user_group(
    client: Any,
    payload: ApprovalUserGroupPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApprovalUserGroup]:
    """Create an approval user group; ``name`` is required -
    ``POST /settings/approval_user_groups``."""
    _require_payload(payload)
    return client.send_post_request(
        approval_user_groups_urls.SETTINGS_APPROVAL_USER_GROUPS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApprovalUserGroup,
    )


def get_settings_approval_user_group(
    client: Any,
    approval_user_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApprovalUserGroup]:
    """Read one approval user group by its ``aug_`` id -
    ``GET /settings/approval_user_groups/{approval_user_group_id}``."""
    return client.send_get_request(
        approval_user_groups_urls.SETTINGS_APPROVAL_USER_GROUP,
        path_params={"approval_user_group_id": approval_user_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApprovalUserGroup,
    )


def delete_settings_approval_user_group(
    client: Any,
    approval_user_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an approval user group -
    ``DELETE /settings/approval_user_groups/{approval_user_group_id}``."""
    return client.send_delete_request(
        approval_user_groups_urls.SETTINGS_APPROVAL_USER_GROUP,
        path_params={"approval_user_group_id": approval_user_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_approval_user_group(
    client: Any,
    approval_user_group_id: str,
    payload: ApprovalUserGroupPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApprovalUserGroup]:
    """Update an approval user group's name, display name or description -
    ``PATCH /settings/approval_user_groups/{approval_user_group_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        approval_user_groups_urls.SETTINGS_APPROVAL_USER_GROUP,
        path_params={"approval_user_group_id": approval_user_group_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApprovalUserGroup,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
