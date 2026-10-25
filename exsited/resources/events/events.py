"""Event endpoints, under ``/api/{api_version}/events``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.events import events_urls
from exsited.resources.events.events_dto import Event, EventList

__all__ = [
    "get_events",
    "get_event",
    "create_event_execute",
    "create_event_remove",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

EventPayload = Mapping[str, Any] | str | Dto


def get_events(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[EventList]:
    """List all events - ``GET /events``."""
    return client.send_get_request(
        events_urls.EVENTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=EventList,
    )


def get_event(
    client: Any,
    event_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Event]:
    """Get single event - ``GET /events/{event_uuid}``."""
    return client.send_get_request(
        events_urls.EVENT,
        path_params={"event_uuid": event_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Event,
    )


def create_event_execute(
    client: Any,
    event_uuid: str,
    payload: EventPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Execute event - ``POST /events/{event_uuid}/execute``."""
    _require_payload(payload)
    return client.send_post_request(
        events_urls.EVENT_EXECUTE,
        path_params={"event_uuid": event_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_event_remove(
    client: Any,
    event_uuid: str,
    payload: EventPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Event]:
    """Remove event - ``POST /events/{event_uuid}/remove``."""
    _require_payload(payload)
    return client.send_post_request(
        events_urls.EVENT_REMOVE,
        path_params={"event_uuid": event_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Event,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
