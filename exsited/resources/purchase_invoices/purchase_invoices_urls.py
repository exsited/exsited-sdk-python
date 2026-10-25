"""Path templates and body keys for the purchase invoice endpoints."""

from __future__ import annotations

PURCHASE_INVOICES = "/api/{api_version}/purchase_invoices"
PURCHASE_INVOICES_NOTES = "/api/{api_version}/purchase_invoices/notes"
PURCHASE_INVOICE = "/api/{api_version}/purchase_invoices/{purchase_invoice_id}"
PURCHASE_INVOICE_AMEND = "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/amend"
PURCHASE_INVOICE_CANCEL = "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/cancel"
PURCHASE_INVOICE_INFORMATION = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/information"
)
PURCHASE_INVOICE_LINES = "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/lines"
PURCHASE_INVOICE_NOTES = "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes"
PURCHASE_INVOICE_PURCHASE_CREDIT_NOTE_APPLICATIONS = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/purchase_credit_note_applications"
)
#: Not scoped by the server: any application id answers under any purchase invoice that exists.
PURCHASE_INVOICE_PURCHASE_CREDIT_NOTE_APPLICATION = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}"
    "/purchase_credit_note_applications/{application_id}"
)
PURCHASE_INVOICE_PURCHASE_PAYMENTS = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/purchase_payments"
)
PURCHASE_INVOICE_REACTIVATE = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/reactivate"
)
PURCHASE_INVOICE_LINE = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/lines/{purchase_invoice_line_uuid}"
)
PURCHASE_INVOICE_NOTE = "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes/{note_id}"
PURCHASE_INVOICE_NOTE_FILES = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes/{note_id}/files"
)
PURCHASE_INVOICE_NOTE_FILE = (
    "/api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes/{note_id}/files/{file_id}"
)

#: The key a listing's records sit under.
PURCHASE_INVOICES_KEY = "data"
PURCHASE_INVOICES_NOTES_KEY = "data"
PURCHASE_INVOICE_NOTES_KEY = "data"
PURCHASE_INVOICE_PURCHASE_CREDIT_NOTE_APPLICATIONS_KEY = "data"
PURCHASE_INVOICE_PURCHASE_PAYMENTS_KEY = "data"

#: The envelope one record arrives under.
PURCHASE_INVOICE_KEY = "purchase_invoice"
WATCHERLIST_KEY = "watcherList"
PURCHASE_CREDIT_NOTE_APPLICATION_KEY = "purchase_credit_note_application"
