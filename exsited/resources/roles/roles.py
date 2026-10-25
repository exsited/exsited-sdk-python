"""Role endpoints, under ``/api/{api_version}/settings/roles``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.roles import roles_urls
from exsited.resources.roles.roles_dto import (
    SettingsRole,
    SettingsRoleList,
)

__all__ = [
    "get_settings_roles",
    "create_settings_role",
    "get_settings_role",
    "delete_settings_role",
    "update_settings_role",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

RolePayload = Mapping[str, Any] | str | Dto


def get_settings_roles(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsRoleList]:
    """List roles - ``GET /settings/roles``."""
    return client.send_get_request(
        roles_urls.SETTINGS_ROLES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsRoleList,
    )


def create_settings_role(
    client: Any,
    payload: RolePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a role - ``POST /settings/roles``; on develop_work the role is saved and the
    answer is then a 500, from a lookup that does not exist."""
    _require_payload(payload)
    return client.send_post_request(
        roles_urls.SETTINGS_ROLES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_role(
    client: Any,
    role_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsRole]:
    """Get one role - ``GET /settings/roles/{role_id}``."""
    return client.send_get_request(
        roles_urls.SETTINGS_ROLE,
        path_params={"role_id": role_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsRole,
    )


def delete_settings_role(
    client: Any,
    role_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a role - ``DELETE /settings/roles/{role_id}``; a system role is refused."""
    return client.send_delete_request(
        roles_urls.SETTINGS_ROLE,
        path_params={"role_id": role_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_role(
    client: Any,
    role_id: str,
    payload: RolePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update or enable/disable a role - ``PATCH /settings/roles/{role_id}``; on develop_work
    the change is saved and the answer is then a 500, from a lookup that does not exist."""
    _require_payload(payload)
    return client.send_patch_request(
        roles_urls.SETTINGS_ROLE,
        path_params={"role_id": role_id},
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
