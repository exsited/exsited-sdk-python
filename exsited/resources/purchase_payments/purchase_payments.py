"""Purchase payment endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.purchase_credit_notes.purchase_credit_notes_dto import (
    PurchaseCreditNoteList,
)
from exsited.resources.purchase_payments import purchase_payments_urls
from exsited.resources.purchase_payments.purchase_payments_dto import (
    PurchasePaymentList,
    PurchasePaymentNoteFile,
    PurchasePaymentNoteList,
    PurchasePaymentNoteRead,
    PurchasePaymentNotes,
    PurchasePaymentNoteUpdated,
    PurchasePaymentRead,
    PurchasePayments,
    PurchasePaymentUpdated,
)

__all__ = [
    "get_purchase_payments",
    "create_purchase_payment",
    "delete_purchase_payment",
    "get_purchase_payment",
    "update_purchase_payment",
    "create_purchase_invoice_purchase_payment",
    "get_purchase_payment_purchase_credit_notes",
    "get_purchase_payment_notes",
    "create_purchase_payment_note",
    "get_purchase_payment_note",
    "update_purchase_payment_note",
    "delete_purchase_payment_note",
    "get_purchase_payment_note_files",
    "get_purchase_payment_note_file",
    "delete_purchase_payment_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

PurchasePaymentPayload = Mapping[str, Any] | str | Dto


def get_purchase_payments(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentList]:
    """List purchase payments - ``GET /purchase_payments``."""
    return client.send_get_request(
        purchase_payments_urls.PURCHASE_PAYMENTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentList,
    )


def create_purchase_payment(
    client: Any,
    payload: PurchasePaymentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePayments]:
    """Create purchase payment - ``POST /purchase_payments``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_payments_urls.PURCHASE_PAYMENTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePayments,
    )


def delete_purchase_payment(
    client: Any,
    purchase_payment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete purchase payment - ``DELETE /purchase_payments/{purchase_payment_id}``."""
    return client.send_delete_request(
        purchase_payments_urls.PURCHASE_PAYMENT,
        path_params={"purchase_payment_id": purchase_payment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_purchase_payment(
    client: Any,
    purchase_payment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentRead]:
    """Get single - ``GET /purchase_payments/{purchase_payment_id}``."""
    return client.send_get_request(
        purchase_payments_urls.PURCHASE_PAYMENT,
        path_params={"purchase_payment_id": purchase_payment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentRead,
    )


def update_purchase_payment(
    client: Any,
    purchase_payment_id: str,
    payload: PurchasePaymentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentUpdated]:
    """Update purchase payment - ``PATCH /purchase_payments/{purchase_payment_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        purchase_payments_urls.PURCHASE_PAYMENT,
        path_params={"purchase_payment_id": purchase_payment_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentUpdated,
    )


def create_purchase_invoice_purchase_payment(
    client: Any,
    purchase_invoice_id: str,
    payload: PurchasePaymentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePayments]:
    """PI-scoped payment - ``POST /purchase_invoices/{purchase_invoice_id}/purchase_payments``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_payments_urls.PURCHASE_INVOICE_PURCHASE_PAYMENTS,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePayments,
    )


def get_purchase_payment_purchase_credit_notes(
    client: Any,
    purchase_payment_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteList]:
    """The purchase credit notes a payment raised -
    ``GET /purchase_payments/{purchase_payment_id}/purchase_credit_notes``; a paged listing."""
    return client.send_get_request(
        purchase_payments_urls.PURCHASE_PAYMENT_PURCHASE_CREDIT_NOTES,
        path_params={"purchase_payment_id": purchase_payment_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteList,
    )


def get_purchase_payment_notes(
    client: Any,
    purchase_payment_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentNoteList]:
    """List purchase payment notes - ``GET /purchase_payments/{purchase_payment_id}/notes``."""
    return client.send_get_request(
        purchase_payments_urls.PURCHASE_PAYMENT_NOTES,
        path_params={"purchase_payment_id": purchase_payment_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentNoteList,
    )


def create_purchase_payment_note(
    client: Any,
    purchase_payment_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentNotes]:
    """Create note - ``POST /purchase_payments/{purchase_payment_id}/notes``;
    multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        purchase_payments_urls.PURCHASE_PAYMENT_NOTES,
        path_params={"purchase_payment_id": purchase_payment_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentNotes,
    )


def get_purchase_payment_note(
    client: Any,
    purchase_payment_id: str,
    pp_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentNoteRead]:
    """Get single - ``GET /purchase_payments/{purchase_payment_id}/notes/{pp_note_id}``."""
    return client.send_get_request(
        purchase_payments_urls.PURCHASE_PAYMENT_NOTE,
        path_params={"purchase_payment_id": purchase_payment_id, "pp_note_id": pp_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentNoteRead,
    )


def update_purchase_payment_note(
    client: Any,
    purchase_payment_id: str,
    pp_note_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentNoteUpdated]:
    """Update a note - ``PATCH /purchase_payments/{purchase_payment_id}/notes/{pp_note_id}``; a
    form, the text as the ``note`` field, answered under ``note``."""
    _require_note(note)
    return client.send_patch_request(
        purchase_payments_urls.PURCHASE_PAYMENT_NOTE,
        path_params={"purchase_payment_id": purchase_payment_id, "pp_note_id": pp_note_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentNoteUpdated,
    )


def delete_purchase_payment_note(
    client: Any,
    purchase_payment_id: str,
    pp_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete purchase payment note -
    ``DELETE /purchase_payments/{purchase_payment_id}/notes/{pp_note_id}``; answered ``204``."""
    return client.send_delete_request(
        purchase_payments_urls.PURCHASE_PAYMENT_NOTE,
        path_params={"purchase_payment_id": purchase_payment_id, "pp_note_id": pp_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_purchase_payment_note_files(
    client: Any,
    purchase_payment_id: str,
    pp_note_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentNoteRead]:
    """List purchase payment note files -
    ``GET /purchase_payments/{purchase_payment_id}/notes/{pp_note_id}/files``."""
    return client.send_get_request(
        purchase_payments_urls.PURCHASE_PAYMENT_NOTE_FILES,
        path_params={"purchase_payment_id": purchase_payment_id, "pp_note_id": pp_note_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentNoteRead,
    )


def get_purchase_payment_note_file(
    client: Any,
    purchase_payment_id: str,
    pp_note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchasePaymentNoteFile]:
    """Get single -
    ``GET /purchase_payments/{purchase_payment_id}/notes/{pp_note_id}/files/{file_id}``."""
    return client.send_get_request(
        purchase_payments_urls.PURCHASE_PAYMENT_NOTE_FILE,
        path_params={
            "purchase_payment_id": purchase_payment_id,
            "pp_note_id": pp_note_id,
            "file_id": file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchasePaymentNoteFile,
    )


def delete_purchase_payment_note_file(
    client: Any,
    purchase_payment_id: str,
    pp_note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one attachment -
    ``DELETE /purchase_payments/{purchase_payment_id}/notes/{pp_note_id}/files/{file_id}``, by the
    attachment's ``uuid``; ``204``."""
    return client.send_delete_request(
        purchase_payments_urls.PURCHASE_PAYMENT_NOTE_FILE,
        path_params={
            "purchase_payment_id": purchase_payment_id,
            "pp_note_id": pp_note_id,
            "file_id": file_id,
        },
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
