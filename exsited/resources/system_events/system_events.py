"""System event endpoints, under ``/api/{api_version}/settings/system_events``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.system_events import system_events_urls
from exsited.resources.system_events.system_events_dto import (
    SettingsSystemEvent,
    SettingsSystemEventList,
)

__all__ = [
    "get_settings_system_events",
    "get_settings_system_event",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_settings_system_events(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsSystemEventList]:
    """List the base system events - ``GET /settings/system_events``; reference data, read only."""
    return client.send_get_request(
        system_events_urls.SETTINGS_SYSTEM_EVENTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsSystemEventList,
    )


def get_settings_system_event(
    client: Any,
    system_event_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsSystemEvent]:
    """Get one system event - ``GET /settings/system_events/{system_event_id}``."""
    return client.send_get_request(
        system_events_urls.SETTINGS_SYSTEM_EVENT,
        path_params={"system_event_id": system_event_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsSystemEvent,
    )
