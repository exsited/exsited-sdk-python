"""Typed views over the event bodies."""

from __future__ import annotations

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Event",
    "EventList",
]


class Event(Dto):
    """The event body, under ``event``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/events",
        "GET /api/{api_version}/events/{event_uuid}",
        "POST /api/{api_version}/events/{event_uuid}/remove",
    )

    ENVELOPE_KEY = "event"

    created_on: str | None = None
    event_name: str | None = None
    executed_on: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None
    resource_type: str | None = None
    resource_uuid: str | None = None
    scheduled_to_execute_on: str | None = None
    status: str | None = None


class EventList(Dto):
    """One page of ``Event`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/events",)

    data: list[Event] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
