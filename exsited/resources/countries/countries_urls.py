"""Path templates and body keys for the country endpoints."""

from __future__ import annotations

SETTINGS_COUNTRIES = "/api/{api_version}/settings/countries"
SETTINGS_COUNTRY = "/api/{api_version}/settings/countries/{country_id}"

#: The key a listing's records sit under.
SETTINGS_COUNTRIES_KEY = "data"

#: The envelope one record arrives under.
COUNTRY_KEY = "country"
