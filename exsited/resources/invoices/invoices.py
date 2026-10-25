"""Invoice endpoints, under ``/api/{api_version}``; three are reached through an account or
an order."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.accounts.accounts_dto import NoteFileList
from exsited.resources.credit_note_applications.credit_note_applications_dto import (
    CreditNoteApplicationRead,
)
from exsited.resources.invoices import invoices_urls
from exsited.resources.invoices.invoices_dto import (
    Invoice,
    InvoiceKpisRead,
    InvoiceLineRead,
    InvoiceLines,
    InvoiceList,
    InvoiceNote,
    InvoiceNoteFile,
    InvoiceNoteList,
    InvoicePdf,
)
from exsited.resources.item_fulfillments.item_fulfillments_dto import (
    ItemFulfillmentRead,
    ItemFulfillmentReadList,
)
from exsited.resources.return_merchandise_authorisations.return_merchandise_authorisations_dto import (
    InvoiceReturnMerchandiseAuthorisations,
    ReturnMerchandiseAuthorisationRead,
)

__all__ = [
    "get_invoices",
    "get_invoice",
    "get_invoice_information",
    "get_invoice_kpis",
    "get_invoice_lines",
    "get_invoice_line",
    "get_invoice_pdf",
    "create_invoice",
    "update_invoice_information",
    "amend_invoice",
    "cancel_invoice",
    "reactivate_invoice",
    "delete_invoice",
    "get_invoice_item_fulfillments",
    "get_invoice_item_fulfillment",
    "get_invoice_rmas",
    "get_invoice_rma",
    "get_invoice_credit_note_application",
    "get_invoice_custom_objects",
    "get_invoice_custom_object",
    "get_invoice_custom_object_instance",
    "get_invoice_notes",
    "get_invoice_note",
    "create_invoice_note",
    "delete_invoice_note",
    "get_invoice_note_files",
    "get_invoice_note_file",
    "delete_invoice_note_file",
    "get_order_invoices",
    "create_order_invoice",
]

#: A body as the API's own mapping, as JSON text, or as an ``invoices_dto`` type.
InvoicePayload = Mapping[str, Any] | str | Dto

#: The key a listing puts its records under, as ``invoices_urls.INVOICES_KEY`` names it.
RECORD_KEY = "data"


def get_invoices(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceList]:
    """List invoices - ``GET /invoices``. ``INVOICES_QUERY_PARAMS`` shape the listing; every other
    name is a ``filter_<field>``, and money reads back as text."""
    return client.send_get_request(
        invoices_urls.INVOICES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceList,
    )


def get_invoice(
    client: Any,
    invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Invoice]:
    """Retrieve one invoice - ``GET /invoices/{invoice_id}``, by its ``id``; the detail carries
    ``lines``, which a listing entry does not."""
    return client.send_get_request(
        invoices_urls.INVOICE,
        path_params={"invoice_id": invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Invoice,
    )


def get_invoice_information(
    client: Any,
    invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Invoice]:
    """Retrieve an invoice's core information - ``GET /invoices/{invoice_id}/information``."""
    return client.send_get_request(
        invoices_urls.INVOICE_INFORMATION,
        path_params={"invoice_id": invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Invoice,
    )


def get_invoice_kpis(
    client: Any,
    invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceKpisRead]:
    """An invoice's KPI block - ``GET /invoices/{invoice_id}/kpis``, under ``invoice_kpis``; the
    same block ``get_invoice`` carries as ``kpis``."""
    return client.send_get_request(
        invoices_urls.INVOICE_KPIS,
        path_params={"invoice_id": invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceKpisRead,
    )


def get_invoice_lines(
    client: Any,
    invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceLines]:
    """An invoice's lines - ``GET /invoices/{invoice_id}/lines``, under ``invoice.lines``; not a
    paged listing."""
    return client.send_get_request(
        invoices_urls.INVOICE_LINES,
        path_params={"invoice_id": invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceLines,
    )


def get_invoice_line(
    client: Any,
    invoice_id: str,
    line_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceLineRead]:
    """One invoice line - ``GET /invoices/{invoice_id}/lines/{line_id}``, under ``invoice.line``.
    The server ignores ``line_id`` and answers the invoice's first line."""
    return client.send_get_request(
        invoices_urls.INVOICE_LINE,
        path_params={"invoice_id": invoice_id, "line_id": line_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceLineRead,
    )


def get_invoice_pdf(
    client: Any,
    invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoicePdf]:
    """Ask for the invoice's PDF - ``GET /invoices/{invoice_id}/pdf``. It answers a JSON descriptor
    under ``invoice.pdf`` whose ``download_url`` holds the bytes."""
    return client.send_get_request(
        invoices_urls.INVOICE_PDF,
        path_params={"invoice_id": invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoicePdf,
    )


def create_invoice(
    client: Any,
    payload: InvoicePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Invoice]:
    """Create an invoice - ``POST /invoices``, wrapped in ``invoice``; ``price_tax_inclusive`` goes
    in as a boolean and reads back as text."""
    _require_payload(payload)
    return client.send_post_request(
        invoices_urls.INVOICES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Invoice,
    )


def update_invoice_information(
    client: Any,
    invoice_id: str,
    payload: InvoicePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Invoice]:
    """Update an invoice's core information - ``PATCH /invoices/{invoice_id}/information``; ``202``,
    accepted rather than applied."""
    _require_payload(payload)
    return client.send_patch_request(
        invoices_urls.INVOICE_INFORMATION,
        path_params={"invoice_id": invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Invoice,
    )


def amend_invoice(
    client: Any,
    invoice_id: str,
    payload: InvoicePayload | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Invoice]:
    """Amend an invoice - ``POST /invoices/{invoice_id}/amend``; ``201``, because an amendment is a
    new invoice. The body is optional."""
    return client.send_post_request(
        invoices_urls.INVOICE_AMEND,
        path_params={"invoice_id": invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Invoice,
    )


def cancel_invoice(
    client: Any,
    invoice_id: str,
    payload: InvoicePayload | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Invoice]:
    """Cancel an invoice - ``POST /invoices/{invoice_id}/cancel``; ``202``, and the body is
    optional."""
    return client.send_post_request(
        invoices_urls.INVOICE_CANCEL,
        path_params={"invoice_id": invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Invoice,
    )


def reactivate_invoice(
    client: Any,
    invoice_id: str,
    payload: InvoicePayload | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Invoice]:
    """Reactivate a cancelled invoice - ``POST /invoices/{invoice_id}/reactivate``; ``202``, and the
    body is optional."""
    return client.send_post_request(
        invoices_urls.INVOICE_REACTIVATE,
        path_params={"invoice_id": invoice_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Invoice,
    )


def delete_invoice(
    client: Any,
    invoice_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an invoice - ``DELETE /invoices/{invoice_id}``; ``200`` with a body, not ``204``."""
    return client.send_delete_request(
        invoices_urls.INVOICE,
        path_params={"invoice_id": invoice_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_invoice_item_fulfillments(
    client: Any,
    invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillmentReadList]:
    """List the fulfilments against an invoice - ``GET /invoices/{invoice_id}/item_fulfillments``,
    spelled with two Ls. Reads as the item fulfilment family's page view, measured from this
    path."""
    return client.send_get_request(
        invoices_urls.INVOICE_ITEM_FULFILLMENTS,
        path_params={"invoice_id": invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillmentReadList,
    )


def get_invoice_item_fulfillment(
    client: Any,
    invoice_id: str,
    fulfillment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillmentRead]:
    """Retrieve one fulfilment - ``GET /invoices/{invoice_id}/item_fulfillments/{fulfillment_id}``,
    under ``item_fulfillment``. Reads as the item fulfilment family's view of this path."""
    return client.send_get_request(
        invoices_urls.INVOICE_ITEM_FULFILLMENT,
        path_params={"invoice_id": invoice_id, "fulfillment_id": fulfillment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillmentRead,
    )


def get_invoice_rmas(
    client: Any,
    invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceReturnMerchandiseAuthorisations]:
    """List an invoice's return merchandise authorisations -
    ``GET /invoices/{invoice_id}/return_merchandise_authorisations``, British ``s``; the ``z`` is
    404."""
    return client.send_get_request(
        invoices_urls.INVOICE_RMAS,
        path_params={"invoice_id": invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceReturnMerchandiseAuthorisations,
    )


def get_invoice_rma(
    client: Any,
    invoice_id: str,
    rma_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnMerchandiseAuthorisationRead]:
    """Retrieve one return merchandise authorisation -
    ``GET /invoices/{invoice_id}/return_merchandise_authorisations/{rma_id}``."""
    return client.send_get_request(
        invoices_urls.INVOICE_RMA,
        path_params={"invoice_id": invoice_id, "rma_id": rma_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnMerchandiseAuthorisationRead,
    )


def get_invoice_credit_note_application(
    client: Any,
    invoice_id: str,
    credit_note_application_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteApplicationRead]:
    """One credit note application through an invoice -
    ``GET /invoices/{invoice_id}/credit_note_applications/{credit_note_application_id}``; not
    checked against the invoice, so any application answers under any invoice."""
    return client.send_get_request(
        invoices_urls.INVOICE_CREDIT_NOTE_APPLICATION,
        path_params={
            "invoice_id": invoice_id,
            "credit_note_application_id": credit_note_application_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteApplicationRead,
    )


def get_invoice_custom_objects(
    client: Any,
    invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """The custom objects defined for invoices - ``GET /invoices/{invoice_id}/custom_objects``; a
    paged listing, under ``data``."""
    return client.send_get_request(
        invoices_urls.INVOICE_CUSTOM_OBJECTS,
        path_params={"invoice_id": invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_invoice_custom_object(
    client: Any,
    invoice_id: str,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One custom object with this invoice's instances of it -
    ``GET /invoices/{invoice_id}/custom_objects/{custom_object_id}``."""
    return client.send_get_request(
        invoices_urls.INVOICE_CUSTOM_OBJECT,
        path_params={"invoice_id": invoice_id, "custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_invoice_custom_object_instance(
    client: Any,
    invoice_id: str,
    custom_object_id: str,
    instance_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One instance of a custom object on an invoice -
    ``GET /invoices/{invoice_id}/custom_objects/{custom_object_id}/instances/{instance_id}``."""
    return client.send_get_request(
        invoices_urls.INVOICE_CUSTOM_OBJECT_INSTANCE,
        path_params={
            "invoice_id": invoice_id,
            "custom_object_id": custom_object_id,
            "instance_id": instance_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_invoice_notes(
    client: Any,
    invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceNoteList]:
    """List an invoice's notes - ``GET /invoices/{invoice_id}/notes``; a paged listing, under
    ``data``."""
    return client.send_get_request(
        invoices_urls.INVOICE_NOTES,
        path_params={"invoice_id": invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceNoteList,
    )


def get_invoice_note(
    client: Any,
    invoice_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceNote]:
    """Retrieve one note - ``GET /invoices/{invoice_id}/notes/{note_id}``, by the ``id`` the listing
    hands out; under ``note``."""
    return client.send_get_request(
        invoices_urls.INVOICE_NOTE,
        path_params={"invoice_id": invoice_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceNote,
    )


def create_invoice_note(
    client: Any,
    invoice_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceNote]:
    """Attach a note to an invoice - ``POST /invoices/{invoice_id}/notes``; a form, the text as the
    ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        invoices_urls.INVOICE_NOTES,
        path_params={"invoice_id": invoice_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceNote,
    )


def delete_invoice_note(
    client: Any,
    invoice_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one note - ``DELETE /invoices/{invoice_id}/notes/{note_id}``."""
    return client.send_delete_request(
        invoices_urls.INVOICE_NOTE,
        path_params={"invoice_id": invoice_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_invoice_note_files(
    client: Any,
    invoice_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteFileList]:
    """List a note's attachments - ``GET /invoices/{invoice_id}/notes/{note_id}/files``."""
    return client.send_get_request(
        invoices_urls.INVOICE_NOTE_FILES,
        path_params={"invoice_id": invoice_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteFileList,
    )


def get_invoice_note_file(
    client: Any,
    invoice_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceNoteFile]:
    """Retrieve one attachment - ``GET /invoices/{invoice_id}/notes/{note_id}/files/{file_id}``;
    it answers a JSON descriptor of the
    file under ``file``, not the file's bytes."""
    return client.send_get_request(
        invoices_urls.INVOICE_NOTE_FILE,
        path_params={
            "invoice_id": invoice_id,
            "note_id": note_id,
            "file_id": file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceNoteFile,
    )


def delete_invoice_note_file(
    client: Any,
    invoice_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one attachment - ``DELETE /invoices/{invoice_id}/notes/{note_id}/files/{file_id}``, by
    the attachment's ``uuid``; ``204``."""
    return client.send_delete_request(
        invoices_urls.INVOICE_NOTE_FILE,
        path_params={"invoice_id": invoice_id, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_order_invoices(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceList]:
    """List one order's invoices - ``GET /orders/{order_id}/invoices``; the order envelope carrying
    ``invoices``."""
    return client.send_get_request(
        invoices_urls.ORDER_INVOICES,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceList,
    )


def create_order_invoice(
    client: Any,
    order_id: str,
    payload: InvoicePayload | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Invoice]:
    """Raise an invoice against an order - ``POST /orders/{order_id}/invoices``; ``201``, and the
    body is optional."""
    return client.send_post_request(
        invoices_urls.ORDER_INVOICES,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Invoice,
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
