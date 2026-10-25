"""Credit note endpoints, under ``/api/{api_version}/credit_notes``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.credit_notes import credit_notes_urls
from exsited.resources.credit_notes.credit_notes_dto import (
    CreditNoteApplications,
    CreditNoteItems,
    CreditNoteList,
    CreditNoteNote,
    CreditNoteNoteList,
    CreditNoteRead,
)

__all__ = [
    "get_credit_notes",
    "get_credit_note",
    "create_credit_note",
    "update_credit_note",
    "delete_credit_note",
    "apply_credit_note",
    "get_credit_note_items",
    "get_credit_note_credit_note_applications",
    "get_credit_note_notes",
    "get_credit_note_note",
    "create_credit_note_note",
    "delete_credit_note_note",
    "get_credit_note_note_files",
    "get_credit_note_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

CreditNotePayload = Mapping[str, Any] | str | Dto


def get_credit_notes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteList]:
    """List credit notes - ``GET /credit_notes``."""
    return client.send_get_request(
        credit_notes_urls.CREDIT_NOTES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteList,
    )


def get_credit_note(
    client: Any,
    credit_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteRead]:
    """Get single - ``GET /credit_notes/{credit_note_id}``."""
    return client.send_get_request(
        credit_notes_urls.CREDIT_NOTE,
        path_params={"credit_note_id": credit_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteRead,
    )


def create_credit_note(
    client: Any,
    payload: CreditNotePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Credit an invoice - ``POST /credit_notes``, ``{"credit_note": {invoice_id, amount}}``;
    ``201``. The amount is drawn from the invoice's active payments, oldest first."""
    _require_payload(payload)
    return client.send_post_request(
        credit_notes_urls.CREDIT_NOTES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_credit_note(
    client: Any,
    credit_note_id: str,
    payload: CreditNotePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteRead]:
    """Update credit note - ``PATCH /credit_notes/{credit_note_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        credit_notes_urls.CREDIT_NOTE,
        path_params={"credit_note_id": credit_note_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteRead,
    )


def delete_credit_note(
    client: Any,
    credit_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a credit note - ``DELETE /credit_notes/{credit_note_id}``, by ``cn_`` id or code;
    ``204``. A credit note with an active refund is refused ``400`` ``in_use``."""
    return client.send_delete_request(
        credit_notes_urls.CREDIT_NOTE,
        path_params={"credit_note_id": credit_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def apply_credit_note(
    client: Any,
    credit_note_id: str,
    payload: CreditNotePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Apply a credit note to invoices - ``POST /credit_notes/{credit_note_id}/apply``, under
    ``credit_note.invoices``; it records a payment against each, and answers the credit note."""
    _require_payload(payload)
    return client.send_post_request(
        credit_notes_urls.CREDIT_NOTE_APPLY,
        path_params={"credit_note_id": credit_note_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_credit_note_items(
    client: Any,
    credit_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteItems]:
    """A credit note's balance rows - ``GET /credit_notes/{credit_note_id}/items``, under
    ``credit_note.items``; not a paged listing."""
    return client.send_get_request(
        credit_notes_urls.CREDIT_NOTE_ITEMS,
        path_params={"credit_note_id": credit_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteItems,
    )


def get_credit_note_credit_note_applications(
    client: Any,
    credit_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteApplications]:
    """A credit note's applications - ``GET /credit_notes/{credit_note_id}/credit_note_applications``,
    under ``credit_note.applications``; not a paged listing."""
    return client.send_get_request(
        credit_notes_urls.CREDIT_NOTE_CREDIT_NOTE_APPLICATIONS,
        path_params={"credit_note_id": credit_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteApplications,
    )


def get_credit_note_notes(
    client: Any,
    credit_note_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteNoteList]:
    """List a credit note's notes - ``GET /credit_notes/{credit_note_id}/notes``; a paged listing,
    under ``data``."""
    return client.send_get_request(
        credit_notes_urls.CREDIT_NOTE_NOTES,
        path_params={"credit_note_id": credit_note_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteNoteList,
    )


def get_credit_note_note(
    client: Any,
    credit_note_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteNote]:
    """Retrieve one note - ``GET /credit_notes/{credit_note_id}/notes/{note_id}``, by its
    ``note_`` id; under ``note``."""
    return client.send_get_request(
        credit_notes_urls.CREDIT_NOTE_NOTE,
        path_params={"credit_note_id": credit_note_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteNote,
    )


def create_credit_note_note(
    client: Any,
    credit_note_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Attach a note to a credit note - ``POST /credit_notes/{credit_note_id}/notes``; a form, the
    text as the ``note`` field, and ``201``."""
    _require_note(note)
    return client.send_post_request(
        credit_notes_urls.CREDIT_NOTE_NOTES,
        path_params={"credit_note_id": credit_note_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_credit_note_note(
    client: Any,
    credit_note_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one note - ``DELETE /credit_notes/{credit_note_id}/notes/{note_id}``, by its
    ``note_`` id; ``204``."""
    return client.send_delete_request(
        credit_notes_urls.CREDIT_NOTE_NOTE,
        path_params={"credit_note_id": credit_note_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_credit_note_note_files(
    client: Any,
    credit_note_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List a note's attachments - ``GET /credit_notes/{credit_note_id}/notes/{note_id}/files``,
    under ``data``."""
    return client.send_get_request(
        credit_notes_urls.CREDIT_NOTE_NOTE_FILES,
        path_params={"credit_note_id": credit_note_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_credit_note_note_file(
    client: Any,
    credit_note_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Retrieve one attachment - ``GET /credit_notes/{credit_note_id}/notes/{note_id}/files/{file_id}``;
    a JSON descriptor under ``file``, not the file's bytes."""
    return client.send_get_request(
        credit_notes_urls.CREDIT_NOTE_NOTE_FILE,
        path_params={"credit_note_id": credit_note_id, "note_id": note_id, "file_id": file_id},
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
