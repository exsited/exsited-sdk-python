"""Path templates and body keys for the payment endpoints."""

from __future__ import annotations

PAYMENTS = "/api/{api_version}/payments"
PAYMENTS_NOTES = "/api/{api_version}/payments/notes"
PAYMENT = "/api/{api_version}/payments/{payment_id}"
INVOICE_PAYMENTS = "/api/{api_version}/invoices/{invoice_id}/payments"
ORDER_PAYMENTS = "/api/{api_version}/orders/{order_id}/payments"
PAYMENT_NOTES = "/api/{api_version}/payments/{payment_id}/notes"
PAYMENT_NOTE = "/api/{api_version}/payments/{payment_id}/notes/{payment_note_id}"
PAYMENT_NOTE_FILES = "/api/{api_version}/payments/{payment_id}/notes/{payment_note_id}/files"
#: One payment by an invoice. The server does not scope it: any payment id answers under any
#: invoice that exists.
INVOICE_PAYMENT = "/api/{api_version}/invoices/{invoice_id}/payments/{payment_id}"
PAYMENT_NOTE_FILE = (
    "/api/{api_version}/payments/{payment_id}/notes/{payment_note_id}/files/{payment_file_id}"
)

#: The key a listing's records sit under.
INVOICE_PAYMENTS_KEY = "data"
ORDER_PAYMENTS_KEY = "data"
PAYMENTS_KEY = "data"
PAYMENTS_NOTES_KEY = "data"
PAYMENT_NOTES_KEY = "data"
PAYMENT_NOTE_FILES_KEY = "data"

#: The envelope one record arrives under.
PAYMENT_KEY = "payment"

#: The keys ``create_payment`` takes under ``payment``; any other is a ``400``.
PAYMENT_CREATE_KEYS = (
    "id",
    "date",
    "origin",
    "payment_note",
    "note",
    "invoices",
    "payment_applied",
    "credit_applied",
    "gift_certificates",
    "custom_attributes",
)
