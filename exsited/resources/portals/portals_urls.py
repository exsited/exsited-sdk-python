"""Path templates and body keys for the portal endpoints."""

from __future__ import annotations

PORTAL_ACTIVATE = "/api/{api_version}/portal/activate"
PORTAL_CHANGE = "/api/{api_version}/portal/change"
PORTAL_CHANGE_PASSWORD = "/api/{api_version}/portal/change_password"
PORTAL_LOGIN = "/api/{api_version}/portal/login"
PORTAL_RESET = "/api/{api_version}/portal/reset"
PORTAL_RESET_LINK = "/api/{api_version}/portal/reset_link"
PORTAL_VALIDATE = "/api/{api_version}/portal/validate"

#: The envelope one record arrives under.
PORTAL_KEY = "portal"
