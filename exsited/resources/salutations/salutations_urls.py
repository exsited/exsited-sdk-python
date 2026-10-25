"""Path templates and body keys for the salutation endpoints."""

from __future__ import annotations

SETTINGS_SALUTATIONS = "/api/{api_version}/settings/salutations"
SETTINGS_SALUTATION = "/api/{api_version}/settings/salutations/{salutation_id}"

#: The key a listing's records sit under.
SETTINGS_SALUTATIONS_KEY = "data"

#: The envelope one record arrives under.
SALUTATION_KEY = "salutation"
