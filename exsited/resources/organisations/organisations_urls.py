"""Path templates and body keys for the organisation endpoints."""

from __future__ import annotations

SETTINGS_ORGANISATIONS = "/api/{api_version}/settings/organisations"
SETTINGS_ORGANISATION = "/api/{api_version}/settings/organisations/{organisation_id}"

#: The key a listing's records sit under.
SETTINGS_ORGANISATIONS_KEY = "data"

#: The envelope one record arrives under.
ORGANIZATION_KEY = "organization"
