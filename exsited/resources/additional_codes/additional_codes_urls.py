"""Path templates and body keys for the additional code endpoints."""

from __future__ import annotations

SETTINGS_ADDITIONAL_CODES = "/api/{api_version}/settings/additional_codes"
SETTINGS_ADDITIONAL_CODE = "/api/{api_version}/settings/additional_codes/{additional_code_id}"

#: The key a listing's records sit under.
SETTINGS_ADDITIONAL_CODES_KEY = "data"

#: The envelope one record arrives under.
ADDITIONAL_CODE_KEY = "additional_code"
