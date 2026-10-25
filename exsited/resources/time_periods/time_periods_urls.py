"""Path templates and body keys for the time period endpoints."""

from __future__ import annotations

SETTINGS_TIME_PERIODS = "/api/{api_version}/settings/time_periods"
SETTINGS_TIME_PERIOD = "/api/{api_version}/settings/time_periods/{time_period_id}"

#: The key a listing's records sit under.
SETTINGS_TIME_PERIODS_KEY = "data"

#: The envelope one record arrives under.
TIME_PERIOD_KEY = "time_period"
