"""Operator group endpoints, under ``/api/{api_version}/settings/operator_groups``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.operator_groups import operator_groups_urls
from exsited.resources.operator_groups.operator_groups_dto import (
    SettingsOperatorGroup,
    SettingsOperatorGroupList,
)

__all__ = [
    "get_settings_operator_groups",
    "create_settings_operator_group",
    "get_settings_operator_group",
    "delete_settings_operator_group",
    "update_settings_operator_group",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

OperatorGroupPayload = Mapping[str, Any] | str | Dto


def get_settings_operator_groups(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOperatorGroupList]:
    """List operator groups - ``GET /settings/operator_groups``; paged by cursor."""
    return client.send_get_request(
        operator_groups_urls.SETTINGS_OPERATOR_GROUPS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOperatorGroupList,
    )


def create_settings_operator_group(
    client: Any,
    payload: OperatorGroupPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOperatorGroup]:
    """Create an operator group - ``POST /settings/operator_groups``; ``201``. ``role`` is required
    and takes the role's dashed uuid, its ``rol_`` id being refused."""
    _require_payload(payload)
    return client.send_post_request(
        operator_groups_urls.SETTINGS_OPERATOR_GROUPS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOperatorGroup,
    )


def get_settings_operator_group(
    client: Any,
    operator_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOperatorGroup]:
    """Get one operator group - ``GET /settings/operator_groups/{operator_group_id}``."""
    return client.send_get_request(
        operator_groups_urls.SETTINGS_OPERATOR_GROUP,
        path_params={"operator_group_id": operator_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOperatorGroup,
    )


def delete_settings_operator_group(
    client: Any,
    operator_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an operator group - ``DELETE /settings/operator_groups/{operator_group_id}``;
    answered ``204``."""
    return client.send_delete_request(
        operator_groups_urls.SETTINGS_OPERATOR_GROUP,
        path_params={"operator_group_id": operator_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_operator_group(
    client: Any,
    operator_group_id: str,
    payload: OperatorGroupPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOperatorGroup]:
    """Update an operator group - ``PATCH /settings/operator_groups/{operator_group_id}``; the
    answer names ``role`` as a reference carrying the dashed uuid."""
    _require_payload(payload)
    return client.send_patch_request(
        operator_groups_urls.SETTINGS_OPERATOR_GROUP,
        path_params={"operator_group_id": operator_group_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOperatorGroup,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
