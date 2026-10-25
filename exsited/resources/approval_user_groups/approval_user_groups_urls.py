"""Path templates and body keys for the approval user group endpoints."""

from __future__ import annotations

SETTINGS_APPROVAL_USER_GROUPS = "/api/{api_version}/settings/approval_user_groups"
SETTINGS_APPROVAL_USER_GROUP = (
    "/api/{api_version}/settings/approval_user_groups/{approval_user_group_id}"
)

#: The key a listing's records sit under.
SETTINGS_APPROVAL_USER_GROUPS_KEY = "data"

#: The envelope one record arrives under.
APPROVAL_USER_GROUP_KEY = "approval_user_group"
