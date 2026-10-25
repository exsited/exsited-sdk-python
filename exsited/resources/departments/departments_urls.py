"""Path templates and body keys for the department endpoints."""

from __future__ import annotations

SETTINGS_DEPARTMENTS = "/api/{api_version}/settings/departments"
SETTINGS_DEPARTMENT = "/api/{api_version}/settings/departments/{department_id}"

#: The key a listing's records sit under.
SETTINGS_DEPARTMENTS_KEY = "data"

#: The envelope one record arrives under.
DEPARTMENT_KEY = "department"
