"""Payment endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.accounts.accounts_dto import NoteFileList
from exsited.resources.payments import payments_urls
from exsited.resources.payments.payments_dto import (
    PaymentList,
    PaymentNoteFile,
    PaymentNoteList,
    PaymentNoteRead,
    PaymentNotes,
    PaymentRead,
    PaymentsNoteList,
)

__all__ = [
    "get_payments",
    "get_payments_notes",
    "create_payment",
    "delete_payment",
    "update_payment",
    "get_payment",
    "get_invoice_payments",
    "get_invoice_payment",
    "get_order_payments",
    "get_payment_notes",
    "create_payment_note",
    "get_payment_note",
    "delete_payment_note",
    "get_payment_note_files",
    "get_payment_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

PaymentPayload = Mapping[str, Any] | str | Dto


def get_payments(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentList]:
    """List payments - ``GET /payments``."""
    return client.send_get_request(
        payments_urls.PAYMENTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentList,
    )


def get_payments_notes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentsNoteList]:
    """List all notes across payments - ``GET /payments/notes``."""
    return client.send_get_request(
        payments_urls.PAYMENTS_NOTES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentsNoteList,
    )


def create_payment(
    client: Any,
    payload: PaymentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentRead]:
    """Record a payment - ``POST /payments``, wrapped in ``payment``; ``201``, answered as
    ``get_payment`` reads it. A ``payment_applied`` processor with a card token charges the card."""
    _require_payload(payload)
    return client.send_post_request(
        payments_urls.PAYMENTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentRead,
    )


def delete_payment(
    client: Any,
    payment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete payment - ``DELETE /payments/{payment_id}``; answered ``204``."""
    return client.send_delete_request(
        payments_urls.PAYMENT,
        path_params={"payment_id": payment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_payment(
    client: Any,
    payment_id: str,
    payload: PaymentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentRead]:
    """Update payment information - ``PATCH /payments/{payment_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        payments_urls.PAYMENT,
        path_params={"payment_id": payment_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentRead,
    )


def get_payment(
    client: Any,
    payment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentRead]:
    """Get single - ``GET /payments/{payment_id}``."""
    return client.send_get_request(
        payments_urls.PAYMENT,
        path_params={"payment_id": payment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentRead,
    )


def get_invoice_payments(
    client: Any,
    invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentList]:
    """List invoice payments - ``GET /invoices/{invoice_id}/payments``."""
    return client.send_get_request(
        payments_urls.INVOICE_PAYMENTS,
        path_params={"invoice_id": invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentList,
    )


def get_invoice_payment(
    client: Any,
    invoice_id: str,
    payment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentRead]:
    """Retrieve one payment through an invoice - ``GET /invoices/{invoice_id}/payments/{payment_id}``;
    the payment is not checked against the invoice, only the invoice's existence is."""
    return client.send_get_request(
        payments_urls.INVOICE_PAYMENT,
        path_params={"invoice_id": invoice_id, "payment_id": payment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentRead,
    )


def get_order_payments(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentList]:
    """List order payments - ``GET /orders/{order_id}/payments``."""
    return client.send_get_request(
        payments_urls.ORDER_PAYMENTS,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentList,
    )


def get_payment_notes(
    client: Any,
    payment_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentNoteList]:
    """List notes - ``GET /payments/{payment_id}/notes``."""
    return client.send_get_request(
        payments_urls.PAYMENT_NOTES,
        path_params={"payment_id": payment_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentNoteList,
    )


def create_payment_note(
    client: Any,
    payment_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentNotes]:
    """Create note - ``POST /payments/{payment_id}/notes``;
    multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        payments_urls.PAYMENT_NOTES,
        path_params={"payment_id": payment_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentNotes,
    )


def get_payment_note(
    client: Any,
    payment_id: str,
    payment_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentNoteRead]:
    """Get specific note - ``GET /payments/{payment_id}/notes/{payment_note_id}``."""
    return client.send_get_request(
        payments_urls.PAYMENT_NOTE,
        path_params={"payment_id": payment_id, "payment_note_id": payment_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentNoteRead,
    )


def delete_payment_note(
    client: Any,
    payment_id: str,
    payment_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete note -
    ``DELETE /payments/{payment_id}/notes/{payment_note_id}``."""
    return client.send_delete_request(
        payments_urls.PAYMENT_NOTE,
        path_params={"payment_id": payment_id, "payment_note_id": payment_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_payment_note_files(
    client: Any,
    payment_id: str,
    payment_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteFileList]:
    """List a note's attachments - ``GET /payments/{payment_id}/notes/{payment_note_id}/files``,
    under ``data``."""
    return client.send_get_request(
        payments_urls.PAYMENT_NOTE_FILES,
        path_params={"payment_id": payment_id, "payment_note_id": payment_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteFileList,
    )


def get_payment_note_file(
    client: Any,
    payment_id: str,
    payment_note_id: str,
    payment_file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PaymentNoteFile]:
    """Get note file -
    ``GET /payments/{payment_id}/notes/{payment_note_id}/files/{payment_file_id}``."""
    return client.send_get_request(
        payments_urls.PAYMENT_NOTE_FILE,
        path_params={
            "payment_id": payment_id,
            "payment_note_id": payment_note_id,
            "payment_file_id": payment_file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PaymentNoteFile,
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
