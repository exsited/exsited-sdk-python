"""Path templates and body keys for the purchase payment endpoints."""

from __future__ import annotations

PURCHASE_PAYMENTS = "/api/{api_version}/purchase_payments"
PURCHASE_PAYMENT = "/api/{api_version}/purchase_payments/{purchase_payment_id}"
PURCHASE_INVOICE_PURCHASE_PAYMENTS = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/purchase_payments"
)
PURCHASE_PAYMENT_PURCHASE_CREDIT_NOTES = (
    "/api/{api_version}/purchase_payments/{purchase_payment_id}/purchase_credit_notes"
)
PURCHASE_PAYMENT_NOTES = "/api/{api_version}/purchase_payments/{purchase_payment_id}/notes"
PURCHASE_PAYMENT_NOTE = (
    "/api/{api_version}/purchase_payments/{purchase_payment_id}/notes/{pp_note_id}"
)
PURCHASE_PAYMENT_NOTE_FILES = (
    "/api/{api_version}/purchase_payments/{purchase_payment_id}/notes/{pp_note_id}/files"
)
PURCHASE_PAYMENT_NOTE_FILE = (
    "/api/{api_version}/purchase_payments/{purchase_payment_id}/notes/{pp_note_id}/files/{file_id}"
)

#: The key a listing's records sit under.
PURCHASE_INVOICE_PURCHASE_PAYMENTS_KEY = "data"
PURCHASE_PAYMENTS_KEY = "data"
PURCHASE_PAYMENT_NOTES_KEY = "data"
PURCHASE_PAYMENT_PURCHASE_CREDIT_NOTES_KEY = "data"

#: The envelope one record arrives under.
FILES_KEY = "files"
NOTE_KEY = "note"
PURCHASE_PAYMENT_KEY = "purchase_payment"
