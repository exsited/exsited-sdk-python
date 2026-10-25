"""Typed views over the note group bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "NoteGroup",
    "NoteGroupList",
    "NoteGroupNotes",
]


class NoteGroup(Dto):
    """The note group body, under ``note_group``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/note_groups",
        "GET /api/{api_version}/note_groups/{note_group_id}",
        "POST /api/{api_version}/note_groups",
        "PATCH /api/{api_version}/note_groups/{note_group_id}",
    )

    ENVELOPE_KEY = "note_group"

    activity_logs: list[Any] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class NoteGroupList(Dto):
    """One page of ``NoteGroup`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/note_groups",)

    data: list[NoteGroup] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class NoteGroupNotes(Dto):
    """The note group notes body."""

    MEASURED_FROM = ("GET /api/{api_version}/note_groups/{note_group_id}/notes",)

    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
