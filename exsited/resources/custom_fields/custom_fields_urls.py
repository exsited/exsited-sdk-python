"""Path templates and body keys for the custom field endpoints."""

from __future__ import annotations

SETTINGS_CUSTOM_FIELDS = "/api/{api_version}/settings/custom_fields"
SETTINGS_CUSTOM_FIELD = "/api/{api_version}/settings/custom_fields/{custom_field_id}"

#: The key a listing's records sit under.
SETTINGS_CUSTOM_FIELDS_KEY = "data"

#: The envelope one record arrives under.
CUSTOM_FIELD_KEY = "custom_field"
