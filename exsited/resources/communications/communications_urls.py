"""Path templates and body keys for the communication endpoints."""

from __future__ import annotations

COMMUNICATIONS_SEND_EMAIL = "/api/{api_version}/communications/send_email"

#: The one key the body names, which picks the document the email carries.
SEND_EMAIL_DOCUMENT_KEYS = ("invoice", "purchase_invoice", "account_statement", "payment")

#: The envelope one record arrives under.
EMAIL_KEY = "email"
