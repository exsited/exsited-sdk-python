"""Path templates and body keys for the workflow endpoints."""

from __future__ import annotations

SETTINGS_WORKFLOWS = "/api/{api_version}/settings/workflows"
SETTINGS_WORKFLOW = "/api/{api_version}/settings/workflows/{workflow_id}"

#: The key a listing's records sit under.
SETTINGS_WORKFLOWS_KEY = "data"

#: The envelope one record arrives under.
WORKFLOW_KEY = "workflow"
