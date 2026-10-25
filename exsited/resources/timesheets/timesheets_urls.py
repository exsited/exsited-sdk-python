"""Path templates and body keys for the timesheet endpoints."""

from __future__ import annotations

TIMESHEETS = "/api/{api_version}/timesheets"
TIMESHEET = "/api/{api_version}/timesheets/{timesheet_id}"

#: The key a listing's records sit under.
TIMESHEETS_KEY = "data"
