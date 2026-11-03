"""Path templates and body keys for the user settings endpoints."""

from __future__ import annotations

USER_SETTINGS = "/api/{api_version}/user_settings/{user_id}"
USER_SETTINGS_PROFILE_IMAGE = "/api/{api_version}/user_settings/{user_id}/profile_image"

#: The envelope one record arrives under.
USER_SETTINGS_KEY = "user_settings"
