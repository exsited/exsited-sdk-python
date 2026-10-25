"""Path templates and body keys for the receive term endpoints."""

from __future__ import annotations

SETTINGS_RECEIVE_TERMS = "/api/{api_version}/settings/receive_terms"
SETTINGS_RECEIVE_TERM = "/api/{api_version}/settings/receive_terms/{receive_term_id}"

#: The key a listing's records sit under.
SETTINGS_RECEIVE_TERMS_KEY = "data"

#: The envelope one record arrives under.
RECEIVE_TERM_KEY = "receive_term"
