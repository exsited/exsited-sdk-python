"""Path templates and body keys for the role endpoints."""

from __future__ import annotations

SETTINGS_ROLES = "/api/{api_version}/settings/roles"
SETTINGS_ROLE = "/api/{api_version}/settings/roles/{role_id}"

#: The key a listing's records sit under.
SETTINGS_ROLES_KEY = "data"

#: The envelope one record arrives under.
ROLE_KEY = "role"
