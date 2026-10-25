"""Path templates and body keys for the credit note endpoints."""

from __future__ import annotations

CREDIT_NOTES = "/api/{api_version}/credit_notes"
CREDIT_NOTE = "/api/{api_version}/credit_notes/{credit_note_id}"
CREDIT_NOTE_APPLY = "/api/{api_version}/credit_notes/{credit_note_id}/apply"
CREDIT_NOTE_ITEMS = "/api/{api_version}/credit_notes/{credit_note_id}/items"
CREDIT_NOTE_CREDIT_NOTE_APPLICATIONS = (
    "/api/{api_version}/credit_notes/{credit_note_id}/credit_note_applications"
)
CREDIT_NOTE_NOTES = "/api/{api_version}/credit_notes/{credit_note_id}/notes"
CREDIT_NOTE_NOTE = "/api/{api_version}/credit_notes/{credit_note_id}/notes/{note_id}"
CREDIT_NOTE_NOTE_FILES = "/api/{api_version}/credit_notes/{credit_note_id}/notes/{note_id}/files"
CREDIT_NOTE_NOTE_FILE = (
    "/api/{api_version}/credit_notes/{credit_note_id}/notes/{note_id}/files/{file_id}"
)

#: The key a listing's records sit under.
CREDIT_NOTES_KEY = "data"
CREDIT_NOTE_NOTES_KEY = "data"
CREDIT_NOTE_NOTE_FILES_KEY = "data"

#: The envelope one record arrives under. ``items`` and ``credit_note_applications`` answer
#: under ``credit_note`` too, carrying only ``object``, ``href`` and their own list.
CREDIT_NOTE_KEY = "credit_note"
NOTE_KEY = "note"
FILE_KEY = "file"

#: The two keys ``create_credit_note`` takes under ``credit_note``; any other is a ``400``.
CREDIT_NOTE_CREATE_KEYS = ("invoice_id", "amount")

#: The one key ``apply_credit_note`` takes under ``credit_note``; each entry of it takes
#: ``invoice_id`` and ``amount`` and nothing else.
CREDIT_NOTE_APPLY_KEYS = ("invoices",)
