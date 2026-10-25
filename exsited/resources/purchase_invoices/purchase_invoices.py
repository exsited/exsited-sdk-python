"""Purchase invoice endpoints, under ``/api/{api_version}``. There is no ``pdf`` endpoint: v4 answers
``GET /purchase_invoices/{purchase_invoice_id}/pdf`` with a ``400``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.purchase_credit_note_applications.purchase_credit_note_applications_dto import (
    PurchaseCreditNoteApplicationRead,
)
from exsited.resources.purchase_invoices import purchase_invoices_urls
from exsited.resources.purchase_invoices.purchase_invoices_dto import (
    AccountPurchaseInvoices,
    PurchaseInvoice,
    PurchaseInvoiceCancel,
    PurchaseInvoiceInformation,
    PurchaseInvoiceLine,
    PurchaseInvoiceLines,
    PurchaseInvoiceList,
    PurchaseInvoiceNoteFile,
    PurchaseInvoiceNoteList,
    PurchaseInvoiceNoteRead,
    PurchaseInvoiceNotes,
    PurchaseInvoiceNoteUpdated,
    PurchaseInvoicePurchasePaymentList,
    PurchaseInvoiceRead,
    PurchaseInvoicesNoteList,
)

__all__ = [
    "get_purchase_invoices",
    "create_purchase_invoice",
    "get_purchase_invoices_notes",
    "delete_purchase_invoice",
    "get_purchase_invoice",
    "amend_purchase_invoice",
    "cancel_purchase_invoice",
    "get_purchase_invoice_information",
    "update_purchase_invoice_information",
    "get_purchase_invoice_lines",
    "get_purchase_invoice_notes",
    "create_purchase_invoice_note",
    "get_purchase_invoice_purchase_credit_note_applications",
    "get_purchase_invoice_purchase_credit_note_application",
    "get_purchase_invoice_purchase_payments",
    "reactivate_purchase_invoice",
    "get_purchase_invoice_line",
    "update_purchase_invoice_note",
    "get_purchase_invoice_note",
    "delete_purchase_invoice_note",
    "get_purchase_invoice_note_files",
    "get_purchase_invoice_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

PurchaseInvoicePayload = Mapping[str, Any] | str | Dto


def get_purchase_invoices(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceList]:
    """List purchase invoices - ``GET /purchase_invoices``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceList,
    )


def create_purchase_invoice(
    client: Any,
    payload: PurchaseInvoicePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceRead]:
    """Create - ``POST /purchase_invoices``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_invoices_urls.PURCHASE_INVOICES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceRead,
    )


def get_purchase_invoices_notes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoicesNoteList]:
    """List all notes - ``GET /purchase_invoices/notes``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICES_NOTES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoicesNoteList,
    )


def delete_purchase_invoice(
    client: Any,
    purchase_invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete purchase invoice - ``DELETE /purchase_invoices/{purchase_invoice_id}``."""
    return client.send_delete_request(
        purchase_invoices_urls.PURCHASE_INVOICE,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_purchase_invoice(
    client: Any,
    purchase_invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceRead]:
    """Get single - ``GET /purchase_invoices/{purchase_invoice_id}``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceRead,
    )


def amend_purchase_invoice(
    client: Any,
    purchase_invoice_id: str,
    payload: PurchaseInvoicePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceRead]:
    """Amend purchase invoice - ``POST /purchase_invoices/{purchase_invoice_id}/amend``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_invoices_urls.PURCHASE_INVOICE_AMEND,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceRead,
    )


def cancel_purchase_invoice(
    client: Any,
    purchase_invoice_id: str,
    payload: PurchaseInvoicePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceCancel]:
    """Cancel purchase invoice - ``POST /purchase_invoices/{purchase_invoice_id}/cancel``; answered
    ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_invoices_urls.PURCHASE_INVOICE_CANCEL,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceCancel,
    )


def get_purchase_invoice_information(
    client: Any,
    purchase_invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoice]:
    """Purchase invoice information -
    ``GET /purchase_invoices/{purchase_invoice_id}/information``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_INFORMATION,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoice,
    )


def update_purchase_invoice_information(
    client: Any,
    purchase_invoice_id: str,
    payload: PurchaseInvoicePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceInformation]:
    """Update purchase invoice information -
    ``PATCH /purchase_invoices/{purchase_invoice_id}/information``."""
    _require_payload(payload)
    return client.send_patch_request(
        purchase_invoices_urls.PURCHASE_INVOICE_INFORMATION,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceInformation,
    )


def get_purchase_invoice_lines(
    client: Any,
    purchase_invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceLines]:
    """List purchase invoice lines - ``GET /purchase_invoices/{purchase_invoice_id}/lines``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_LINES,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceLines,
    )


def get_purchase_invoice_notes(
    client: Any,
    purchase_invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceNoteList]:
    """List purchase invoice notes - ``GET /purchase_invoices/{purchase_invoice_id}/notes``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_NOTES,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceNoteList,
    )


def create_purchase_invoice_note(
    client: Any,
    purchase_invoice_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceNotes]:
    """Create note - ``POST /purchase_invoices/{purchase_invoice_id}/notes``;
    multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        purchase_invoices_urls.PURCHASE_INVOICE_NOTES,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceNotes,
    )


def get_purchase_invoice_purchase_credit_note_applications(
    client: Any,
    purchase_invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountPurchaseInvoices]:
    """List purchase invoice purchase credit note applications -
    ``GET /purchase_invoices/{purchase_invoice_id}/purchase_credit_note_applications``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_PURCHASE_CREDIT_NOTE_APPLICATIONS,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountPurchaseInvoices,
    )


def get_purchase_invoice_purchase_credit_note_application(
    client: Any,
    purchase_invoice_id: str,
    application_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteApplicationRead]:
    """One purchase credit note application through a purchase invoice -
    ``GET /purchase_invoices/{purchase_invoice_id}/purchase_credit_note_applications/{application_id}``;
    not checked against the invoice, so any application answers under any invoice."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_PURCHASE_CREDIT_NOTE_APPLICATION,
        path_params={"purchase_invoice_id": purchase_invoice_id, "application_id": application_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteApplicationRead,
    )


def get_purchase_invoice_purchase_payments(
    client: Any,
    purchase_invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoicePurchasePaymentList]:
    """List purchase invoice purchase payments -
    ``GET /purchase_invoices/{purchase_invoice_id}/purchase_payments``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_PURCHASE_PAYMENTS,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoicePurchasePaymentList,
    )


def reactivate_purchase_invoice(
    client: Any,
    purchase_invoice_id: str,
    payload: PurchaseInvoicePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceRead]:
    """Reactivate purchase invoice -
    ``POST /purchase_invoices/{purchase_invoice_id}/reactivate``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_invoices_urls.PURCHASE_INVOICE_REACTIVATE,
        path_params={"purchase_invoice_id": purchase_invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceRead,
    )


def get_purchase_invoice_line(
    client: Any,
    purchase_invoice_id: str,
    purchase_invoice_line_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceLine]:
    """Get single -
    ``GET /purchase_invoices/{purchase_invoice_id}/lines/{purchase_invoice_line_uuid}``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_LINE,
        path_params={
            "purchase_invoice_id": purchase_invoice_id,
            "purchase_invoice_line_uuid": purchase_invoice_line_uuid,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceLine,
    )


def update_purchase_invoice_note(
    client: Any,
    purchase_invoice_id: str,
    note_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceNoteUpdated]:
    """Update note - ``PATCH /purchase_invoices/{purchase_invoice_id}/notes/{note_id}``;
    multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_patch_request(
        purchase_invoices_urls.PURCHASE_INVOICE_NOTE,
        path_params={"purchase_invoice_id": purchase_invoice_id, "note_id": note_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceNoteUpdated,
    )


def get_purchase_invoice_note(
    client: Any,
    purchase_invoice_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceNoteRead]:
    """Get single - ``GET /purchase_invoices/{purchase_invoice_id}/notes/{note_id}``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_NOTE,
        path_params={"purchase_invoice_id": purchase_invoice_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceNoteRead,
    )


def delete_purchase_invoice_note(
    client: Any,
    purchase_invoice_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete purchase invoice note -
    ``DELETE /purchase_invoices/{purchase_invoice_id}/notes/{note_id}``; answered ``204``."""
    return client.send_delete_request(
        purchase_invoices_urls.PURCHASE_INVOICE_NOTE,
        path_params={"purchase_invoice_id": purchase_invoice_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_purchase_invoice_note_files(
    client: Any,
    purchase_invoice_id: str,
    note_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceNoteRead]:
    """List purchase invoice note files -
    ``GET /purchase_invoices/{purchase_invoice_id}/notes/{note_id}/files``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_NOTE_FILES,
        path_params={"purchase_invoice_id": purchase_invoice_id, "note_id": note_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceNoteRead,
    )


def get_purchase_invoice_note_file(
    client: Any,
    purchase_invoice_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseInvoiceNoteFile]:
    """Get single -
    ``GET /purchase_invoices/{purchase_invoice_id}/notes/{note_id}/files/{file_id}``."""
    return client.send_get_request(
        purchase_invoices_urls.PURCHASE_INVOICE_NOTE_FILE,
        path_params={
            "purchase_invoice_id": purchase_invoice_id,
            "note_id": note_id,
            "file_id": file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseInvoiceNoteFile,
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
