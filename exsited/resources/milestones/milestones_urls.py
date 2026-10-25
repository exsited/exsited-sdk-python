"""Path templates and body keys for the milestone endpoints."""

from __future__ import annotations

MILESTONES = "/api/{api_version}/milestones"
MILESTONES_ACCOUNT_BY_ID = "/api/{api_version}/milestones/account/{account_id}"
MILESTONES_LABOUR_BY_ID = "/api/{api_version}/milestones/labour/{labour_id}"
MILESTONES_EMPLOYEE_BY_CODE = "/api/{api_version}/milestones/employee/{employee_code}"
MILESTONE = "/api/{api_version}/milestones/{milestone_uuid}"

#: The key a listing's records sit under.
MILESTONES_ACCOUNT_BY_ID_KEY = "data"
MILESTONES_EMPLOYEE_BY_CODE_KEY = "data"
MILESTONES_KEY = "data"

#: The envelope one record arrives under.
MILESTONE_KEY = "milestone"
