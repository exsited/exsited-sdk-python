"""Path templates and body keys for the system event endpoints."""

from __future__ import annotations

SETTINGS_SYSTEM_EVENTS = "/api/{api_version}/settings/system_events"
SETTINGS_SYSTEM_EVENT = "/api/{api_version}/settings/system_events/{system_event_id}"

#: The key a listing's records sit under.
SETTINGS_SYSTEM_EVENTS_KEY = "data"

#: The envelope one record arrives under.
SYSTEM_EVENT_KEY = "system_event"
