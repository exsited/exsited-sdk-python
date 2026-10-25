"""Path templates and body keys for the task endpoints."""

from __future__ import annotations

TASKS = "/api/{api_version}/tasks"
TASK = "/api/{api_version}/tasks/{task_id}"
TASK_CHECKLIST = "/api/{api_version}/tasks/{task_id}/checklist"
TASK_CHECKLIST_BY_UUID = "/api/{api_version}/tasks/{task_id}/checklist/{task_checklist_uuid}"

#: The note routes resolve the task by its code (or its raw uuid), never by the ``wt_`` id,
#: which answers ``404``; ``{task_code}`` on all four is the code.
TASK_NOTES = "/api/{api_version}/tasks/{task_code}/notes"
TASK_NOTE = "/api/{api_version}/tasks/{task_code}/notes/{note_id}"
TASK_NOTE_FILES = "/api/{api_version}/tasks/{task_code}/notes/{note_id}/files"
TASK_NOTE_FILE = "/api/{api_version}/tasks/{task_code}/notes/{note_id}/files/{file_id}"

#: The key a listing's records sit under.
TASKS_KEY = "data"
TASK_NOTE_FILES_KEY = "data"

#: The envelope one record arrives under.
WORK_TASK_KEY = "work_task"
NOTE_KEY = "note"
FILE_KEY = "file"
