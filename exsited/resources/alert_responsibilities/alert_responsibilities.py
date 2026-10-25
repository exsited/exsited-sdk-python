"""Alert responsibility endpoints, under ``/api/{api_version}/settings/alert_responsibilities``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.alert_responsibilities import alert_responsibilities_urls

__all__ = [
    "get_settings_alert_responsibilities",
    "create_settings_alert_responsibility",
    "get_settings_alert_responsibility",
    "delete_settings_alert_responsibility",
    "update_settings_alert_responsibility",
]

AlertResponsibilityPayload = Mapping[str, Any] | str | Dto


def get_settings_alert_responsibilities(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List the alert responsibilities - ``GET /settings/alert_responsibilities``."""
    return client.send_get_request(
        alert_responsibilities_urls.SETTINGS_ALERT_RESPONSIBILITIES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_alert_responsibility(
    client: Any,
    payload: AlertResponsibilityPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create an alert responsibility; ``name`` is required -
    ``POST /settings/alert_responsibilities``."""
    _require_payload(payload)
    return client.send_post_request(
        alert_responsibilities_urls.SETTINGS_ALERT_RESPONSIBILITIES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_alert_responsibility(
    client: Any,
    alert_responsibility_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Read one alert responsibility by its ``ar_`` id -
    ``GET /settings/alert_responsibilities/{alert_responsibility_id}``."""
    return client.send_get_request(
        alert_responsibilities_urls.SETTINGS_ALERT_RESPONSIBILITY,
        path_params={"alert_responsibility_id": alert_responsibility_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_settings_alert_responsibility(
    client: Any,
    alert_responsibility_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an alert responsibility -
    ``DELETE /settings/alert_responsibilities/{alert_responsibility_id}``."""
    return client.send_delete_request(
        alert_responsibilities_urls.SETTINGS_ALERT_RESPONSIBILITY,
        path_params={"alert_responsibility_id": alert_responsibility_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_alert_responsibility(
    client: Any,
    alert_responsibility_id: str,
    payload: AlertResponsibilityPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update an alert responsibility's fields or its status -
    ``PATCH /settings/alert_responsibilities/{alert_responsibility_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        alert_responsibilities_urls.SETTINGS_ALERT_RESPONSIBILITY,
        path_params={"alert_responsibility_id": alert_responsibility_id},
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
