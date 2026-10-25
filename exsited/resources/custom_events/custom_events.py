"""Custom event endpoints, under ``/api/{api_version}/settings/custom_events``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.custom_events import custom_events_urls
from exsited.resources.custom_events.custom_events_dto import (
    SettingsCustomEvent,
    SettingsCustomEventList,
)

__all__ = [
    "get_settings_custom_events",
    "create_settings_custom_event",
    "get_settings_custom_event",
    "delete_settings_custom_event",
    "update_settings_custom_event",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

CustomEventPayload = Mapping[str, Any] | str | Dto


def get_settings_custom_events(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomEventList]:
    """List the custom events - ``GET /settings/custom_events``."""
    return client.send_get_request(
        custom_events_urls.SETTINGS_CUSTOM_EVENTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomEventList,
    )


def create_settings_custom_event(
    client: Any,
    payload: CustomEventPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a custom event; ``name`` and ``base_event``, an ``se_`` id, are required, and a
    message is added to every communication profile - ``POST /settings/custom_events``."""
    _require_payload(payload)
    return client.send_post_request(
        custom_events_urls.SETTINGS_CUSTOM_EVENTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_custom_event(
    client: Any,
    custom_event_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomEvent]:
    """Read one custom event by its ``ce_`` id -
    ``GET /settings/custom_events/{custom_event_id}``."""
    return client.send_get_request(
        custom_events_urls.SETTINGS_CUSTOM_EVENT,
        path_params={"custom_event_id": custom_event_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomEvent,
    )


def delete_settings_custom_event(
    client: Any,
    custom_event_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a custom event no workflow uses -
    ``DELETE /settings/custom_events/{custom_event_id}``."""
    return client.send_delete_request(
        custom_events_urls.SETTINGS_CUSTOM_EVENT,
        path_params={"custom_event_id": custom_event_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_custom_event(
    client: Any,
    custom_event_id: str,
    payload: CustomEventPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update a custom event's fields or its status -
    ``PATCH /settings/custom_events/{custom_event_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_events_urls.SETTINGS_CUSTOM_EVENT,
        path_params={"custom_event_id": custom_event_id},
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
