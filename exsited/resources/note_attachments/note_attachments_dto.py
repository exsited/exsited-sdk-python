"""Typed views over the note attachment bodies."""

from __future__ import annotations

from exsited.dto import Dto

__all__ = [
    "NoteAttachment",
]


class NoteAttachment(Dto):
    """The note attachment body, under ``note_attachment``; ``base64`` is the file itself."""

    MEASURED_FROM = ("GET /api/{api_version}/note_attachment/{attachment_uuid}",)

    ENVELOPE_KEY = "note_attachment"

    base64: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    size: int | None = None
