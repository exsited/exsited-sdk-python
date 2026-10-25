"""Note group endpoints, under ``/api/{api_version}/note_groups``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.note_groups import note_groups_urls
from exsited.resources.note_groups.note_groups_dto import NoteGroup, NoteGroupList, NoteGroupNotes

__all__ = [
    "get_note_groups",
    "create_note_group",
    "delete_note_group",
    "get_note_group",
    "update_note_group",
    "get_note_group_notes",
    "get_note_group_notes_by_user",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

NoteGroupPayload = Mapping[str, Any] | str | Dto


def get_note_groups(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteGroupList]:
    """List note groups - ``GET /note_groups``."""
    return client.send_get_request(
        note_groups_urls.NOTE_GROUPS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteGroupList,
    )


def create_note_group(
    client: Any,
    payload: NoteGroupPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteGroup]:
    """Create note group - ``POST /note_groups``."""
    _require_payload(payload)
    return client.send_post_request(
        note_groups_urls.NOTE_GROUPS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteGroup,
    )


def delete_note_group(
    client: Any,
    note_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete note group - ``DELETE /note_groups/{note_group_id}``."""
    return client.send_delete_request(
        note_groups_urls.NOTE_GROUP,
        path_params={"note_group_id": note_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_note_group(
    client: Any,
    note_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteGroup]:
    """Get note group - ``GET /note_groups/{note_group_id}``."""
    return client.send_get_request(
        note_groups_urls.NOTE_GROUP,
        path_params={"note_group_id": note_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteGroup,
    )


def update_note_group(
    client: Any,
    note_group_id: str,
    payload: NoteGroupPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteGroup]:
    """Update note group - ``PATCH /note_groups/{note_group_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        note_groups_urls.NOTE_GROUP,
        path_params={"note_group_id": note_group_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteGroup,
    )


def get_note_group_notes(
    client: Any,
    note_group_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteGroupNotes]:
    """List group notes - ``GET /note_groups/{note_group_id}/notes``."""
    return client.send_get_request(
        note_groups_urls.NOTE_GROUP_NOTES,
        path_params={"note_group_id": note_group_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteGroupNotes,
    )


def get_note_group_notes_by_user(
    client: Any,
    note_group_id: str,
    note_user: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List a group's notes as one of its users sees them -
    ``GET /note_groups/{note_group_id}/notes/user/{note_user}``; ``note_user`` is the note user's
    uuid or what it was added as: an entity's uuid, or a manual user's email address."""
    return client.send_get_request(
        note_groups_urls.NOTE_GROUP_NOTES_BY_USER,
        path_params={"note_group_id": note_group_id, "note_user": note_user},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
