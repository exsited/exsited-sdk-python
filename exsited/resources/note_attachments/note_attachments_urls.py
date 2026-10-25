"""Path templates and body keys for the note attachment endpoints."""

from __future__ import annotations

#: Singular on the wire, and not scoped to the note's owner.
NOTE_ATTACHMENT = "/api/{api_version}/note_attachment/{attachment_uuid}"

#: The envelope one record arrives under.
NOTE_ATTACHMENT_KEY = "note_attachment"
