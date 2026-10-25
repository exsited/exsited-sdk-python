"""Path templates and body keys for the purchase credit note application endpoints."""

from __future__ import annotations

PURCHASE_CREDIT_NOTE_APPLICATIONS = "/api/{api_version}/purchase_credit_note_applications"
PURCHASE_CREDIT_NOTE_APPLICATION = (
    "/api/{api_version}/purchase_credit_note_applications/{purchase_credit_note_application_id}"
)

#: The key a listing's records sit under.
PURCHASE_CREDIT_NOTE_APPLICATIONS_KEY = "data"

#: The envelope one record arrives under.
PURCHASE_CREDIT_NOTE_APPLICATION_KEY = "purchase_credit_note_application"
