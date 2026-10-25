"""Path templates and body keys for the action script endpoints."""

from __future__ import annotations

ACTION_SCRIPTS = "/api/{api_version}/action_scripts"
ACTION_SCRIPT = "/api/{api_version}/action_scripts/{action_script_id}"

#: The key a listing's records sit under.
ACTION_SCRIPTS_KEY = "data"

#: The envelope one record arrives under.
ACTION_SCRIPT_KEY = "action_script"
