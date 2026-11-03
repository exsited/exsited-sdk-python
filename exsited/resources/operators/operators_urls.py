"""Path templates and body keys for the operator endpoints."""

from __future__ import annotations

SETTINGS_OPERATORS = "/api/{api_version}/settings/operators"
SETTINGS_OPERATOR = "/api/{api_version}/settings/operators/{operator_id}"

#: The key a listing's records sit under.
SETTINGS_OPERATORS_KEY = "data"

#: The envelope one record arrives under.
OPERATOR_KEY = "operator"
