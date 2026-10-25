"""Path templates and body keys for the communication profile endpoints."""

from __future__ import annotations

SETTINGS_COMMUNICATION_PROFILES = "/api/{api_version}/settings/communication_profiles"
SETTINGS_COMMUNICATION_PROFILE = (
    "/api/{api_version}/settings/communication_profiles/{communication_profile_id}"
)

#: The key a listing's records sit under.
SETTINGS_COMMUNICATION_PROFILES_KEY = "data"

#: The envelope one record arrives under.
COMMUNICATION_PROFILE_KEY = "communication_profile"
