"""Path templates and body keys for the charging period endpoints."""

from __future__ import annotations

SETTINGS_CHARGING_PERIODS = "/api/{api_version}/settings/charging_periods"
SETTINGS_CHARGING_PERIOD = "/api/{api_version}/settings/charging_periods/{charging_period_id}"

#: The key a listing's records sit under.
SETTINGS_CHARGING_PERIODS_KEY = "data"

#: The envelope one record arrives under.
CHARGING_PERIOD_KEY = "charging_period"
