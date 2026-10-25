"""Path templates and body keys for the designation endpoints."""

from __future__ import annotations

SETTINGS_DESIGNATIONS = "/api/{api_version}/settings/designations"
SETTINGS_DESIGNATION = "/api/{api_version}/settings/designations/{designation_id}"

#: The key a listing's records sit under.
SETTINGS_DESIGNATIONS_KEY = "data"

#: The envelope one record arrives under.
DESIGNATION_KEY = "designation"
