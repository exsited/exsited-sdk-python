"""Path templates and body keys for the application endpoints."""

from __future__ import annotations

SETTINGS_APPLICATIONS = "/api/{api_version}/settings/applications"
SETTINGS_APPLICATION = "/api/{api_version}/settings/applications/{application_id}"

#: The key a listing's records sit under.
SETTINGS_APPLICATIONS_KEY = "data"

#: The envelope one record arrives under.
APPLICATION_KEY = "application"
