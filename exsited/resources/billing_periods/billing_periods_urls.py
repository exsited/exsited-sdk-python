"""Path templates and body keys for the billing period endpoints."""

from __future__ import annotations

SETTINGS_BILLING_PERIODS = "/api/{api_version}/settings/billing_periods"
SETTINGS_BILLING_PERIOD = "/api/{api_version}/settings/billing_periods/{billing_period_id}"

#: The key a listing's records sit under.
SETTINGS_BILLING_PERIODS_KEY = "data"

#: The envelope one record arrives under.
BILLING_PERIOD_KEY = "billing_period"
