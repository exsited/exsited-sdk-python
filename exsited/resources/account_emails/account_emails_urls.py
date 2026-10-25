"""Path templates and body keys for the account email endpoints."""

from __future__ import annotations

ACCOUNT_COMMUNICATIONS_EMAIL = (
    "/api/{api_version}/accounts/{account_id}/communications/emails/{email_uuid}"
)

#: The envelope one record arrives under.
EMAIL_KEY = "email"
