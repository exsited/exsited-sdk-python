"""Path templates and body keys for the note group endpoints."""

from __future__ import annotations

NOTE_GROUPS = "/api/{api_version}/note_groups"
NOTE_GROUP = "/api/{api_version}/note_groups/{note_group_id}"
NOTE_GROUP_NOTES = "/api/{api_version}/note_groups/{note_group_id}/notes"
NOTE_GROUP_NOTES_BY_USER = "/api/{api_version}/note_groups/{note_group_id}/notes/user/{note_user}"

#: The key a listing's records sit under.
NOTE_GROUPS_KEY = "data"
NOTE_GROUP_NOTES_KEY = "data"
NOTE_GROUP_NOTES_BY_USER_KEY = "data"

#: The envelope one record arrives under.
NOTE_GROUP_KEY = "note_group"
