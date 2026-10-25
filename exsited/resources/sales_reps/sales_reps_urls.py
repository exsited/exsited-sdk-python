"""Path templates and body keys for the sales rep endpoints."""

from __future__ import annotations

SETTINGS_SALES_REPS = "/api/{api_version}/settings/sales_reps"
SETTINGS_SALES_REP = "/api/{api_version}/settings/sales_reps/{sales_rep_id}"

#: The key a listing's records sit under.
SETTINGS_SALES_REPS_KEY = "data"

#: The envelope one record arrives under.
SALES_REP_KEY = "sales_rep"
