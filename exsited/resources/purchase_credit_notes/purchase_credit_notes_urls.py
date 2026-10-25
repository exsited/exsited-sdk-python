"""Path templates and body keys for the purchase credit note endpoints."""

from __future__ import annotations

PURCHASE_CREDIT_NOTES = "/api/{api_version}/purchase_credit_notes"
PURCHASE_CREDIT_NOTE = "/api/{api_version}/purchase_credit_notes/{purchase_credit_note_id}"

#: These three take the ``pcn_`` id only; a code is refused ``400`` where the reads accept one.
PURCHASE_CREDIT_NOTE_APPLY = (
    "/api/{api_version}/purchase_credit_notes/{purchase_credit_note_id}/apply"
)
PURCHASE_CREDIT_NOTE_NOTES = (
    "/api/{api_version}/purchase_credit_notes/{purchase_credit_note_id}/notes"
)
PURCHASE_CREDIT_NOTE_NOTE = (
    "/api/{api_version}/purchase_credit_notes/{purchase_credit_note_id}/notes/{note_id}"
)

#: The key a listing's records sit under.
PURCHASE_CREDIT_NOTES_KEY = "data"

#: The envelope one record arrives under.
PURCHASE_CREDIT_NOTE_KEY = "purchase_credit_note"
NOTE_KEY = "note"

#: The two keys ``create_purchase_credit_note`` takes under ``purchase_credit_note``.
PURCHASE_CREDIT_NOTE_CREATE_KEYS = ("purchase_invoice_id", "amount")

#: The one key ``apply_purchase_credit_note`` takes under ``purchase_credit_note``; each entry
#: of it takes ``purchase_invoice_id`` and ``amount`` and nothing else.
PURCHASE_CREDIT_NOTE_APPLY_KEYS = ("purchase_invoices",)
