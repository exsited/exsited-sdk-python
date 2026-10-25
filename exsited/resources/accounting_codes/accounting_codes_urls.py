"""Path templates and body keys for the accounting code endpoints."""

from __future__ import annotations

SETTINGS_ACCOUNTING_CODES = "/api/{api_version}/settings/accounting_codes"
SETTINGS_ACCOUNTING_CODE = "/api/{api_version}/settings/accounting_codes/{accounting_code_id}"

#: The key a listing's records sit under.
SETTINGS_ACCOUNTING_CODES_KEY = "data"

#: The envelope one record arrives under.
ACCOUNTING_CODE_KEY = "accounting_code"
