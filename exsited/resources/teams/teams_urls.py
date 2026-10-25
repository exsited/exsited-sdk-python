"""Path templates and body keys for the team endpoints."""

from __future__ import annotations

SETTINGS_TEAMS = "/api/{api_version}/settings/teams"
SETTINGS_TEAM = "/api/{api_version}/settings/teams/{team_id}"

#: The key a listing's records sit under.
SETTINGS_TEAMS_KEY = "data"

#: The envelope one record arrives under.
TEAM_KEY = "team"
