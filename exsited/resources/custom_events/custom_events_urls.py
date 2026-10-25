"""Path templates and body keys for the custom event endpoints."""

from __future__ import annotations

SETTINGS_CUSTOM_EVENTS = "/api/{api_version}/settings/custom_events"
SETTINGS_CUSTOM_EVENT = "/api/{api_version}/settings/custom_events/{custom_event_id}"

#: The key a listing's records sit under.
SETTINGS_CUSTOM_EVENTS_KEY = "data"

#: The envelope one record arrives under.
CUSTOM_EVENT_KEY = "custom_event"
