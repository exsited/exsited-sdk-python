"""Designation endpoints, under ``/api/{api_version}/settings/designations``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.designations import designations_urls
from exsited.resources.designations.designations_dto import (
    SettingsDesignation,
    SettingsDesignationList,
)

__all__ = [
    "get_settings_designations",
    "create_settings_designation",
    "get_settings_designation",
    "delete_settings_designation",
    "update_settings_designation",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

DesignationPayload = Mapping[str, Any] | str | Dto


def get_settings_designations(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDesignationList]:
    """List the designations - ``GET /settings/designations``."""
    return client.send_get_request(
        designations_urls.SETTINGS_DESIGNATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDesignationList,
    )


def create_settings_designation(
    client: Any,
    payload: DesignationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a designation; ``name`` is required - ``POST /settings/designations``."""
    _require_payload(payload)
    return client.send_post_request(
        designations_urls.SETTINGS_DESIGNATIONS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_designation(
    client: Any,
    designation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDesignation]:
    """Read one designation by its ``des_`` id - ``GET /settings/designations/{designation_id}``."""
    return client.send_get_request(
        designations_urls.SETTINGS_DESIGNATION,
        path_params={"designation_id": designation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDesignation,
    )


def delete_settings_designation(
    client: Any,
    designation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a designation - ``DELETE /settings/designations/{designation_id}``."""
    return client.send_delete_request(
        designations_urls.SETTINGS_DESIGNATION,
        path_params={"designation_id": designation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_designation(
    client: Any,
    designation_id: str,
    payload: DesignationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update a designation's name, display name or description -
    ``PATCH /settings/designations/{designation_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        designations_urls.SETTINGS_DESIGNATION,
        path_params={"designation_id": designation_id},
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
