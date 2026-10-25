"""Path templates and body keys for the credit note application endpoints."""

from __future__ import annotations

CREDIT_NOTE_APPLICATIONS = "/api/{api_version}/credit_note_applications"
CREDIT_NOTE_APPLICATION = "/api/{api_version}/credit_note_applications/{credit_note_application_id}"
INVOICE_CREDIT_NOTE_APPLICATIONS = (
    "/api/{api_version}/invoices/{invoice_id}/credit_note_applications"
)

#: The key a listing's records sit under.
CREDIT_NOTE_APPLICATIONS_KEY = "data"
INVOICE_CREDIT_NOTE_APPLICATIONS_KEY = "data"

#: The envelope one record arrives under.
CREDIT_NOTE_APPLICATION_KEY = "credit_note_application"
