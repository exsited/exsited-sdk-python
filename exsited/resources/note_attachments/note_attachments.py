"""Note attachment endpoints, under ``/api/{api_version}/note_attachment``."""

from __future__ import annotations

from typing import Any

from exsited.client.api_response import ApiResponse
from exsited.resources.note_attachments import note_attachments_urls
from exsited.resources.note_attachments.note_attachments_dto import NoteAttachment

__all__ = [
    "get_note_attachment",
]


def get_note_attachment(
    client: Any,
    attachment_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteAttachment]:
    """Any note's attachment as base64 - ``GET /note_attachment/{attachment_uuid}``, the ``uuid`` a
    note's ``attachments`` entry carries, whatever the note is attached to."""
    return client.send_get_request(
        note_attachments_urls.NOTE_ATTACHMENT,
        path_params={"attachment_uuid": attachment_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteAttachment,
    )
