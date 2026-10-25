"""Path templates and body keys for the event endpoints."""

from __future__ import annotations

EVENTS = "/api/{api_version}/events"
EVENT = "/api/{api_version}/events/{event_uuid}"
EVENT_EXECUTE = "/api/{api_version}/events/{event_uuid}/execute"
EVENT_REMOVE = "/api/{api_version}/events/{event_uuid}/remove"

#: The key a listing's records sit under.
EVENTS_KEY = "data"

#: The envelope one record arrives under.
EVENT_KEY = "event"
