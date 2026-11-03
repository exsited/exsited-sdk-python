"""Path templates and body keys for the operator group endpoints."""

from __future__ import annotations

SETTINGS_OPERATOR_GROUPS = "/api/{api_version}/settings/operator_groups"
SETTINGS_OPERATOR_GROUP = "/api/{api_version}/settings/operator_groups/{operator_group_id}"

#: The key a listing's records sit under.
SETTINGS_OPERATOR_GROUPS_KEY = "data"

#: The envelope one record arrives under.
OPERATOR_GROUP_KEY = "operator_group"
