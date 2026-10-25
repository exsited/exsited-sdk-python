"""Refund endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.accounts.accounts_dto import NoteFileList
from exsited.resources.refunds import refunds_urls
from exsited.resources.refunds.refunds_dto import (
    Refund,
    RefundList,
    RefundNote,
    RefundNoteFile,
    RefundNoteList,
    RefundUpdated,
)

__all__ = [
    "get_refunds",
    "delete_refund",
    "get_refund",
    "update_refund",
    "create_credit_note_refund",
    "get_refund_notes",
    "get_refund_note",
    "create_refund_note",
    "delete_refund_note",
    "get_refund_note_files",
    "get_refund_note_file",
    "delete_refund_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

RefundPayload = Mapping[str, Any] | str | Dto


def get_refunds(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RefundList]:
    """List - ``GET /refunds``."""
    return client.send_get_request(
        refunds_urls.REFUNDS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RefundList,
    )


def delete_refund(
    client: Any,
    refund_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete refund - ``DELETE /refunds/{refund_id}``; answered ``204``."""
    return client.send_delete_request(
        refunds_urls.REFUND,
        path_params={"refund_id": refund_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_refund(
    client: Any,
    refund_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Refund]:
    """Get single - ``GET /refunds/{refund_id}``."""
    return client.send_get_request(
        refunds_urls.REFUND,
        path_params={"refund_id": refund_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Refund,
    )


def update_refund(
    client: Any,
    refund_id: str,
    payload: RefundPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RefundUpdated]:
    """Update refund - ``PATCH /refunds/{refund_id}``; answered ``202``."""
    _require_payload(payload)
    return client.send_patch_request(
        refunds_urls.REFUND,
        path_params={"refund_id": refund_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RefundUpdated,
    )


def create_credit_note_refund(
    client: Any,
    credit_note_id: str,
    payload: RefundPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RefundUpdated]:
    """Create refund - ``POST /credit_notes/{credit_note_id}/refunds``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        refunds_urls.CREDIT_NOTE_REFUNDS,
        path_params={"credit_note_id": credit_note_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RefundUpdated,
    )


def get_refund_notes(
    client: Any,
    refund_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RefundNoteList]:
    """List a refund's notes - ``GET /refunds/{refund_id}/notes``; a paged listing, under
    ``data``."""
    return client.send_get_request(
        refunds_urls.REFUND_NOTES,
        path_params={"refund_id": refund_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RefundNoteList,
    )


def get_refund_note(
    client: Any,
    refund_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RefundNote]:
    """Retrieve one note - ``GET /refunds/{refund_id}/notes/{note_id}``, by its ``note_`` id;
    under ``note``."""
    return client.send_get_request(
        refunds_urls.REFUND_NOTE,
        path_params={"refund_id": refund_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RefundNote,
    )


def create_refund_note(
    client: Any,
    refund_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RefundNote]:
    """Attach a note to a refund - ``POST /refunds/{refund_id}/notes``; a form, the text as the
    ``note`` field, and ``201`` under ``note``."""
    _require_note(note)
    return client.send_post_request(
        refunds_urls.REFUND_NOTES,
        path_params={"refund_id": refund_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RefundNote,
    )


def delete_refund_note(
    client: Any,
    refund_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one note - ``DELETE /refunds/{refund_id}/notes/{note_id}``; ``204``. The server
    checks ``CREATE_REFUND_NOTE`` here, not a delete permission."""
    return client.send_delete_request(
        refunds_urls.REFUND_NOTE,
        path_params={"refund_id": refund_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_refund_note_files(
    client: Any,
    refund_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteFileList]:
    """List a note's attachments - ``GET /refunds/{refund_id}/notes/{note_id}/files``, under
    ``data``."""
    return client.send_get_request(
        refunds_urls.REFUND_NOTE_FILES,
        path_params={"refund_id": refund_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteFileList,
    )


def get_refund_note_file(
    client: Any,
    refund_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RefundNoteFile]:
    """Retrieve one attachment - ``GET /refunds/{refund_id}/notes/{note_id}/files/{file_id}``, by
    the attachment's ``uuid``; a JSON descriptor under ``file``, not the file's bytes."""
    return client.send_get_request(
        refunds_urls.REFUND_NOTE_FILE,
        path_params={"refund_id": refund_id, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RefundNoteFile,
    )


def delete_refund_note_file(
    client: Any,
    refund_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one attachment - ``DELETE /refunds/{refund_id}/notes/{note_id}/files/{file_id}``, by
    the attachment's ``uuid``; ``204``."""
    return client.send_delete_request(
        refunds_urls.REFUND_NOTE_FILE,
        path_params={"refund_id": refund_id, "note_id": note_id, "file_id": file_id},
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
