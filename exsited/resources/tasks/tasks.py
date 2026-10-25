"""Task endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.tasks import tasks_urls
from exsited.resources.tasks.tasks_dto import (
    TaskList,
    TaskNoteList,
    TaskView,
)

__all__ = [
    "get_tasks",
    "delete_task",
    "get_task",
    "update_task",
    "get_task_checklist",
    "create_task_checklist",
    "get_task_notes",
    "create_task_note",
    "get_task_checklist_by_uuid",
    "delete_task_note",
    "create_task",
    "update_task_checklist_by_uuid",
    "delete_task_checklist_by_uuid",
    "get_task_note",
    "update_task_note",
    "get_task_note_files",
    "get_task_note_file",
    "delete_task_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

TaskPayload = Mapping[str, Any] | str | Dto


def get_tasks(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskList]:
    """List all tasks - ``GET /tasks``."""
    return client.send_get_request(
        tasks_urls.TASKS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskList,
    )


def delete_task(
    client: Any,
    task_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete task - ``DELETE /tasks/{task_id}``."""
    return client.send_delete_request(
        tasks_urls.TASK,
        path_params={"task_id": task_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_task(
    client: Any,
    task_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskView]:
    """Get single task - ``GET /tasks/{task_id}``."""
    return client.send_get_request(
        tasks_urls.TASK,
        path_params={"task_id": task_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskView,
    )


def update_task(
    client: Any,
    task_id: str,
    payload: TaskPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskView]:
    """Update task - ``PATCH /tasks/{task_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        tasks_urls.TASK,
        path_params={"task_id": task_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskView,
    )


def get_task_checklist(
    client: Any,
    task_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskView]:
    """List checklist items - ``GET /tasks/{task_id}/checklist``."""
    return client.send_get_request(
        tasks_urls.TASK_CHECKLIST,
        path_params={"task_id": task_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskView,
    )


def create_task_checklist(
    client: Any,
    task_id: str,
    payload: TaskPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskView]:
    """Add checklist item - ``POST /tasks/{task_id}/checklist``."""
    _require_payload(payload)
    return client.send_post_request(
        tasks_urls.TASK_CHECKLIST,
        path_params={"task_id": task_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskView,
    )


def get_task_notes(
    client: Any,
    task_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskNoteList]:
    """List task notes - ``GET /tasks/{task_code}/notes``, by the task's code."""
    return client.send_get_request(
        tasks_urls.TASK_NOTES,
        path_params={"task_code": task_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskNoteList,
    )


def create_task_note(
    client: Any,
    task_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Add note - ``POST /tasks/{task_code}/notes``; multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        tasks_urls.TASK_NOTES,
        path_params={"task_code": task_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_task_checklist_by_uuid(
    client: Any,
    task_id: str,
    task_checklist_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskView]:
    """Get single checklist item - ``GET /tasks/{task_id}/checklist/{task_checklist_uuid}``."""
    return client.send_get_request(
        tasks_urls.TASK_CHECKLIST_BY_UUID,
        path_params={"task_id": task_id, "task_checklist_uuid": task_checklist_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskView,
    )


def delete_task_note(
    client: Any,
    task_id: str,
    task_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete note - ``DELETE /tasks/{task_code}/notes/{note_id}``; ``task_id`` is the task's
    code, since the note routes answer ``404`` for a ``wt_`` id."""
    return client.send_delete_request(
        tasks_urls.TASK_NOTE,
        path_params={"task_code": task_id, "note_id": task_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_task(
    client: Any,
    payload: TaskPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskView]:
    """Create task - ``POST /tasks``, ``{"work_task": {...}}``, ``name`` required and unknown keys
    refused; ``201`` with the task as ``get_task`` reads it."""
    _require_payload(payload)
    return client.send_post_request(
        tasks_urls.TASKS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskView,
    )


def update_task_checklist_by_uuid(
    client: Any,
    task_id: str,
    task_checklist_uuid: str,
    payload: TaskPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TaskView]:
    """Edit one checklist item - ``PATCH /tasks/{task_id}/checklist/{task_checklist_uuid}``,
    ``{"checklist": {...}}``; the task's id or code, and the whole task back."""
    _require_payload(payload)
    return client.send_patch_request(
        tasks_urls.TASK_CHECKLIST_BY_UUID,
        path_params={"task_id": task_id, "task_checklist_uuid": task_checklist_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TaskView,
    )


def delete_task_checklist_by_uuid(
    client: Any,
    task_id: str,
    task_checklist_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one checklist item - ``DELETE /tasks/{task_id}/checklist/{task_checklist_uuid}``;
    ``409`` once the item is ``COMPLETED``."""
    return client.send_delete_request(
        tasks_urls.TASK_CHECKLIST_BY_UUID,
        path_params={"task_id": task_id, "task_checklist_uuid": task_checklist_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_task_note(
    client: Any,
    task_code: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get one note - ``GET /tasks/{task_code}/notes/{note_id}``, by the task's code; a ``wt_``
    id answers ``404``."""
    return client.send_get_request(
        tasks_urls.TASK_NOTE,
        path_params={"task_code": task_code, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_task_note(
    client: Any,
    task_code: str,
    note_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update a note's text - ``PATCH /tasks/{task_code}/notes/{note_id}``; a form, as the create
    is, by the task's code."""
    _require_note(note)
    return client.send_patch_request(
        tasks_urls.TASK_NOTE,
        path_params={"task_code": task_code, "note_id": note_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_task_note_files(
    client: Any,
    task_code: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List a note's attachments - ``GET /tasks/{task_code}/notes/{note_id}/files``, by the task's
    code."""
    return client.send_get_request(
        tasks_urls.TASK_NOTE_FILES,
        path_params={"task_code": task_code, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_task_note_file(
    client: Any,
    task_code: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get one attachment - ``GET /tasks/{task_code}/notes/{note_id}/files/{file_id}``, the
    ``uuid`` the files listing gives; a JSON descriptor under ``file``, not the bytes."""
    return client.send_get_request(
        tasks_urls.TASK_NOTE_FILE,
        path_params={"task_code": task_code, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_task_note_file(
    client: Any,
    task_code: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one attachment - ``DELETE /tasks/{task_code}/notes/{note_id}/files/{file_id}``, by
    the task's code and the file's ``uuid``."""
    return client.send_delete_request(
        tasks_urls.TASK_NOTE_FILE,
        path_params={"task_code": task_code, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )


def _require_note(note: Any) -> None:
    # A None note would go out as the text "None" and be stored as the note.
    if note is None:
        raise SdkUsageError(
            "note is required: the note text is the body of this request, and "
            "None would be encoded as the string 'None' and stored as the note"
        )
