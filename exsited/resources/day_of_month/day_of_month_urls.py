"""Path templates and body keys for the day of month endpoints."""

from __future__ import annotations

SETTINGS_DAYS_OF_MONTH = "/api/{api_version}/settings/day_of_month"
SETTINGS_DAY_OF_MONTH = "/api/{api_version}/settings/day_of_month/{day_of_month_id}"

#: The key a listing's records sit under.
SETTINGS_DAYS_OF_MONTH_KEY = "data"

#: The envelope one record arrives under.
DAY_OF_MONTH_KEY = "day_of_month"
