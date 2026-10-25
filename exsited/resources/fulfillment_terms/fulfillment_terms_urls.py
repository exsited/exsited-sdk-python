"""Path templates and body keys for the fulfillment term endpoints."""

from __future__ import annotations

SETTINGS_FULFILLMENT_TERMS = "/api/{api_version}/settings/fulfillment_terms"
SETTINGS_FULFILLMENT_TERM = "/api/{api_version}/settings/fulfillment_terms/{fulfillment_term_id}"

#: The key a listing's records sit under.
SETTINGS_FULFILLMENT_TERMS_KEY = "data"

#: The envelope one record arrives under.
FULFILLMENT_TERM_KEY = "fulfillment_term"
