"""Path templates and body keys for the employee endpoints."""

from __future__ import annotations

EMPLOYEES = "/api/{api_version}/employees"
EMPLOYEE = "/api/{api_version}/employees/{employee_id}"

#: The key a listing's records sit under.
EMPLOYEES_KEY = "data"

#: The envelope one record arrives under.
EMPLOYEE_KEY = "employee"
