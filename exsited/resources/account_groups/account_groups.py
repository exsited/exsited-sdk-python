"""Account group endpoints, under ``/api/{api_version}/settings/account_groups``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.account_groups import account_groups_urls
from exsited.resources.account_groups.account_groups_dto import (
    SettingsAccountGroup,
    SettingsAccountGroupList,
)

__all__ = [
    "get_settings_account_groups",
    "create_settings_account_group",
    "get_settings_account_group",
    "delete_settings_account_group",
    "update_settings_account_group",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

AccountGroupPayload = Mapping[str, Any] | str | Dto


def get_settings_account_groups(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAccountGroupList]:
    """List the account groups - ``GET /settings/account_groups``."""
    return client.send_get_request(
        account_groups_urls.SETTINGS_ACCOUNT_GROUPS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAccountGroupList,
    )


def create_settings_account_group(
    client: Any,
    payload: AccountGroupPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAccountGroup]:
    """Create an account group; ``name`` is required - ``POST /settings/account_groups``."""
    _require_payload(payload)
    return client.send_post_request(
        account_groups_urls.SETTINGS_ACCOUNT_GROUPS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAccountGroup,
    )


def get_settings_account_group(
    client: Any,
    account_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAccountGroup]:
    """Read one account group by its ``ag_`` id -
    ``GET /settings/account_groups/{account_group_id}``."""
    return client.send_get_request(
        account_groups_urls.SETTINGS_ACCOUNT_GROUP,
        path_params={"account_group_id": account_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAccountGroup,
    )


def delete_settings_account_group(
    client: Any,
    account_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an account group no account uses -
    ``DELETE /settings/account_groups/{account_group_id}``."""
    return client.send_delete_request(
        account_groups_urls.SETTINGS_ACCOUNT_GROUP,
        path_params={"account_group_id": account_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_account_group(
    client: Any,
    account_group_id: str,
    payload: AccountGroupPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update an account group's fields or its status -
    ``PATCH /settings/account_groups/{account_group_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        account_groups_urls.SETTINGS_ACCOUNT_GROUP,
        path_params={"account_group_id": account_group_id},
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
