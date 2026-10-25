"""Path templates and body keys for the approval endpoints."""

from __future__ import annotations

APPROVALS_ACCOUNT = "/api/{api_version}/approvals/account"
APPROVALS_SALEORDER = "/api/{api_version}/approvals/saleOrder"
APPROVALS_ACCOUNT_BY_UUID = "/api/{api_version}/approvals/account/{account_uuid}"
#: The entity is a body field here, not a path segment, so one route serves all 16.
APPROVALS_APPROVE = "/api/{api_version}/approvals/approve"
APPROVALS_REJECT = "/api/{api_version}/approvals/reject"

#: The envelope one record arrives under.
APPROVAL_KEY = "approval"

#: The key a listing's records sit under.
APPROVALS_ACCOUNT_KEY = "data"
APPROVALS_SALEORDER_KEY = "data"
