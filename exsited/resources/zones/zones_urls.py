"""Path templates and body keys for the zone endpoints."""

from __future__ import annotations

SETTINGS_ZONES = "/api/{api_version}/settings/zones"
SETTINGS_ZONE = "/api/{api_version}/settings/zones/{zone_id}"

#: The key a listing's records sit under.
SETTINGS_ZONES_KEY = "data"

#: The envelope one record arrives under.
ZONE_KEY = "zone"
