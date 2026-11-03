"""Operator endpoints, under ``/api/{api_version}/settings/operators``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.operators import operators_urls
from exsited.resources.operators.operators_dto import (
    SettingsOperator,
    SettingsOperatorList,
)

__all__ = [
    "get_settings_operators",
    "create_settings_operator",
    "get_settings_operator",
    "update_settings_operator",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

OperatorPayload = Mapping[str, Any] | str | Dto


def get_settings_operators(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOperatorList]:
    """List operators - ``GET /settings/operators``; paged by cursor."""
    return client.send_get_request(
        operators_urls.SETTINGS_OPERATORS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOperatorList,
    )


def create_settings_operator(
    client: Any,
    payload: OperatorPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOperator]:
    """Create an operator - ``POST /settings/operators``; ``201``. ``role`` and
    ``operator_group`` take dashed uuids."""
    _require_payload(payload)
    return client.send_post_request(
        operators_urls.SETTINGS_OPERATORS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOperator,
    )


def get_settings_operator(
    client: Any,
    operator_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOperator]:
    """Get one operator - ``GET /settings/operators/{operator_id}``."""
    return client.send_get_request(
        operators_urls.SETTINGS_OPERATOR,
        path_params={"operator_id": operator_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOperator,
    )


def update_settings_operator(
    client: Any,
    operator_id: str,
    payload: OperatorPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOperator]:
    """Update an operator - ``PATCH /settings/operators/{operator_id}``; ``description`` is
    refused as not understood."""
    _require_payload(payload)
    return client.send_patch_request(
        operators_urls.SETTINGS_OPERATOR,
        path_params={"operator_id": operator_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOperator,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
