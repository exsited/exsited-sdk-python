"""Path templates and body keys for the refund endpoints."""

from __future__ import annotations

REFUNDS = "/api/{api_version}/refunds"
REFUND = "/api/{api_version}/refunds/{refund_id}"
CREDIT_NOTE_REFUNDS = "/api/{api_version}/credit_notes/{credit_note_id}/refunds"

#: A refund's notes. ``{refund_id}`` is the refund's code, as ``get_refunds`` hands it out.
REFUND_NOTES = "/api/{api_version}/refunds/{refund_id}/notes"
REFUND_NOTE = "/api/{api_version}/refunds/{refund_id}/notes/{note_id}"
REFUND_NOTE_FILES = "/api/{api_version}/refunds/{refund_id}/notes/{note_id}/files"
REFUND_NOTE_FILE = "/api/{api_version}/refunds/{refund_id}/notes/{note_id}/files/{file_id}"

#: The key a listing's records sit under.
REFUNDS_KEY = "data"
REFUND_NOTES_KEY = "data"
REFUND_NOTE_FILES_KEY = "data"

#: The envelope one record arrives under.
REFUND_KEY = "refund"
NOTE_KEY = "note"
FILE_KEY = "file"
