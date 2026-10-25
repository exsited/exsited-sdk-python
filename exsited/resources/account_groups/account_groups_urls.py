"""Path templates and body keys for the account group endpoints."""

from __future__ import annotations

SETTINGS_ACCOUNT_GROUPS = "/api/{api_version}/settings/account_groups"
SETTINGS_ACCOUNT_GROUP = "/api/{api_version}/settings/account_groups/{account_group_id}"

#: The key a listing's records sit under.
SETTINGS_ACCOUNT_GROUPS_KEY = "data"

#: The envelope one record arrives under.
ACCOUNT_GROUP_KEY = "account_group"
