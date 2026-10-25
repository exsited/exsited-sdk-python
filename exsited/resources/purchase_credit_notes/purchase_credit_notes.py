"""Purchase credit note endpoints, under ``/api/{api_version}/purchase_credit_notes``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.purchase_credit_notes import purchase_credit_notes_urls
from exsited.resources.purchase_credit_notes.purchase_credit_notes_dto import (
    PurchaseCreditNoteCreated,
    PurchaseCreditNoteList,
    PurchaseCreditNoteRead,
)

__all__ = [
    "get_purchase_credit_notes",
    "get_purchase_credit_note",
    "create_purchase_credit_note",
    "update_purchase_credit_note",
    "delete_purchase_credit_note",
    "apply_purchase_credit_note",
    "create_purchase_credit_note_note",
    "delete_purchase_credit_note_note",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

PurchaseCreditNotePayload = Mapping[str, Any] | str | Dto


def get_purchase_credit_notes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteList]:
    """List purchase credit notes - ``GET /purchase_credit_notes``."""
    return client.send_get_request(
        purchase_credit_notes_urls.PURCHASE_CREDIT_NOTES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteList,
    )


def get_purchase_credit_note(
    client: Any,
    purchase_credit_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteRead]:
    """Get single - ``GET /purchase_credit_notes/{purchase_credit_note_id}``."""
    return client.send_get_request(
        purchase_credit_notes_urls.PURCHASE_CREDIT_NOTE,
        path_params={"purchase_credit_note_id": purchase_credit_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteRead,
    )


def create_purchase_credit_note(
    client: Any,
    payload: PurchaseCreditNotePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteCreated]:
    """Credit a purchase invoice - ``POST /purchase_credit_notes``, as
    ``{"purchase_credit_note": {purchase_invoice_id, amount}}``; ``201``, drawn from its payments."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_credit_notes_urls.PURCHASE_CREDIT_NOTES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteCreated,
    )


def update_purchase_credit_note(
    client: Any,
    purchase_credit_note_id: str,
    payload: PurchaseCreditNotePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteRead]:
    """Update - ``PATCH /purchase_credit_notes/{purchase_credit_note_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        purchase_credit_notes_urls.PURCHASE_CREDIT_NOTE,
        path_params={"purchase_credit_note_id": purchase_credit_note_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteRead,
    )


def delete_purchase_credit_note(
    client: Any,
    purchase_credit_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a purchase credit note - ``DELETE /purchase_credit_notes/{purchase_credit_note_id}``, by
    its ``pcn_`` id only; ``204``."""
    return client.send_delete_request(
        purchase_credit_notes_urls.PURCHASE_CREDIT_NOTE,
        path_params={"purchase_credit_note_id": purchase_credit_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def apply_purchase_credit_note(
    client: Any,
    purchase_credit_note_id: str,
    payload: PurchaseCreditNotePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteCreated]:
    """Apply credit to purchase invoices - ``POST /purchase_credit_notes/{purchase_credit_note_id}/apply``,
    under ``purchase_credit_note.purchase_invoices``; it records a purchase payment."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_credit_notes_urls.PURCHASE_CREDIT_NOTE_APPLY,
        path_params={"purchase_credit_note_id": purchase_credit_note_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteCreated,
    )


def create_purchase_credit_note_note(
    client: Any,
    purchase_credit_note_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Attach a note - ``POST /purchase_credit_notes/{purchase_credit_note_id}/notes``; a form, the
    text as the ``note`` field, and ``201``."""
    _require_note(note)
    return client.send_post_request(
        purchase_credit_notes_urls.PURCHASE_CREDIT_NOTE_NOTES,
        path_params={"purchase_credit_note_id": purchase_credit_note_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_purchase_credit_note_note(
    client: Any,
    purchase_credit_note_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one note - ``DELETE /purchase_credit_notes/{purchase_credit_note_id}/notes/{note_id}``,
    by the ``pcn_`` and ``note_`` ids; ``204``."""
    return client.send_delete_request(
        purchase_credit_notes_urls.PURCHASE_CREDIT_NOTE_NOTE,
        path_params={"purchase_credit_note_id": purchase_credit_note_id, "note_id": note_id},
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
