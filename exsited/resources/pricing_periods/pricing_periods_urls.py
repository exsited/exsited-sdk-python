"""Path templates and body keys for the pricing period endpoints."""

from __future__ import annotations

SETTINGS_PRICING_PERIODS = "/api/{api_version}/settings/pricing_periods"
SETTINGS_PRICING_PERIOD = "/api/{api_version}/settings/pricing_periods/{pricing_period_id}"

#: The key a listing's records sit under.
SETTINGS_PRICING_PERIODS_KEY = "data"

#: The envelope one record arrives under.
PRICING_PERIOD_KEY = "pricing_period"
