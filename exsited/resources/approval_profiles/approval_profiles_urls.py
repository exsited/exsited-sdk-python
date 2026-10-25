"""Path templates and body keys for the approval profile endpoints."""

from __future__ import annotations

SETTINGS_APPROVAL_PROFILES = "/api/{api_version}/settings/approval_profiles"
SETTINGS_APPROVAL_PROFILE = "/api/{api_version}/settings/approval_profiles/{approval_profile_id}"

#: The key a listing's records sit under.
SETTINGS_APPROVAL_PROFILES_KEY = "data"

#: The envelope one record arrives under.
APPROVAL_PROFILE_KEY = "approval_profile"
