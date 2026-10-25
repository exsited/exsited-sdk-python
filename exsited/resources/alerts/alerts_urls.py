"""Path templates and body keys for the alert endpoints."""

from __future__ import annotations

ALERTS = "/api/{api_version}/alerts"
ALERT = "/api/{api_version}/alerts/{alert_id}"
ALERTS_ACCOUNT_BY_ID = "/api/{api_version}/alerts/account/{account_id}"
ALERTS_EMPLOYEE_BY_ID = "/api/{api_version}/alerts/employee/{employee_id}"
ALERTS_LABOUR_BY_ID = "/api/{api_version}/alerts/labour/{labour_id}"

#: The key a listing's records sit under.
ALERTS_ACCOUNT_BY_ID_KEY = "data"
ALERTS_KEY = "data"
