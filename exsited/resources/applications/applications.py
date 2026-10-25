"""Application endpoints, under ``/api/{api_version}/settings/applications``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.applications import applications_urls
from exsited.resources.applications.applications_dto import (
    SettingsApplication,
    SettingsApplicationList,
)

__all__ = [
    "get_settings_applications",
    "create_settings_application",
    "get_settings_application",
    "delete_settings_application",
    "update_settings_application",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ApplicationPayload = Mapping[str, Any] | str | Dto


def get_settings_applications(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApplicationList]:
    """List the OAuth applications - ``GET /settings/applications``."""
    return client.send_get_request(
        applications_urls.SETTINGS_APPLICATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApplicationList,
    )


def create_settings_application(
    client: Any,
    payload: ApplicationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApplication]:
    """Create an OAuth application; ``name`` and ``redirect_url`` are required, and the client id
    and secret are generated server side and never answered - ``POST /settings/applications``."""
    _require_payload(payload)
    return client.send_post_request(
        applications_urls.SETTINGS_APPLICATIONS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApplication,
    )


def get_settings_application(
    client: Any,
    application_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApplication]:
    """Read one OAuth application by its ``app_`` id -
    ``GET /settings/applications/{application_id}``."""
    return client.send_get_request(
        applications_urls.SETTINGS_APPLICATION,
        path_params={"application_id": application_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApplication,
    )


def delete_settings_application(
    client: Any,
    application_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an OAuth application - ``DELETE /settings/applications/{application_id}``."""
    return client.send_delete_request(
        applications_urls.SETTINGS_APPLICATION,
        path_params={"application_id": application_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_application(
    client: Any,
    application_id: str,
    payload: ApplicationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsApplication]:
    """Update an OAuth application's fields or its status -
    ``PATCH /settings/applications/{application_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        applications_urls.SETTINGS_APPLICATION,
        path_params={"application_id": application_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsApplication,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
