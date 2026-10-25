"""Purchase order endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.purchase_orders import purchase_orders_urls
from exsited.resources.purchase_orders.purchase_orders_dto import (
    PurchaseOrderInformation,
    PurchaseOrderKpis,
    PurchaseOrderLineList,
    PurchaseOrderLineRead,
    PurchaseOrderList,
    PurchaseOrderNote,
    PurchaseOrderNoteFile,
    PurchaseOrderNotes,
    PurchaseOrderNotesView,
    PurchaseOrderPurchaseInvoiceList,
    PurchaseOrderPurchaseInvoices,
    PurchaseOrderPurchasePaymentList,
    PurchaseOrderRead,
    PurchaseOrders,
    PurchaseOrdersNoteList,
    PurchaseOrderUpdated,
)

__all__ = [
    "get_purchase_orders",
    "create_purchase_order",
    "get_purchase_orders_notes",
    "delete_purchase_order",
    "update_purchase_order",
    "get_purchase_order",
    "cancel_purchase_order",
    "change_purchase_order",
    "get_purchase_order_information",
    "get_purchase_order_kpis",
    "get_purchase_order_lines",
    "get_purchase_order_notes",
    "create_purchase_order_note",
    "create_purchase_order_purchase_invoice",
    "get_purchase_order_purchase_invoices",
    "get_purchase_order_purchase_payments",
    "reactivate_purchase_order",
    "get_purchase_order_line",
    "delete_purchase_order_note",
    "get_purchase_order_note",
    "get_purchase_order_note_files",
    "get_purchase_order_note_file",
    "delete_purchase_order_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

PurchaseOrderPayload = Mapping[str, Any] | str | Dto


def get_purchase_orders(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderList]:
    """List purchase orders - ``GET /purchase_orders``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDERS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderList,
    )


def create_purchase_order(
    client: Any,
    payload: PurchaseOrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrders]:
    """With status DRAFT - ``POST /purchase_orders``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_orders_urls.PURCHASE_ORDERS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrders,
    )


def get_purchase_orders_notes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrdersNoteList]:
    """List all notes across POs - ``GET /purchase_orders/notes``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDERS_NOTES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrdersNoteList,
    )


def delete_purchase_order(
    client: Any,
    purchase_order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete purchase order - ``DELETE /purchase_orders/{purchase_order_id}``; answered ``204``."""
    return client.send_delete_request(
        purchase_orders_urls.PURCHASE_ORDER,
        path_params={"purchase_order_id": purchase_order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_purchase_order(
    client: Any,
    purchase_order_id: str,
    payload: PurchaseOrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderUpdated]:
    """Update purchase order - ``PATCH /purchase_orders/{purchase_order_id}``; answered ``202``."""
    _require_payload(payload)
    return client.send_patch_request(
        purchase_orders_urls.PURCHASE_ORDER,
        path_params={"purchase_order_id": purchase_order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderUpdated,
    )


def get_purchase_order(
    client: Any,
    purchase_order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderRead]:
    """Get single - ``GET /purchase_orders/{purchase_order_id}``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER,
        path_params={"purchase_order_id": purchase_order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderRead,
    )


def cancel_purchase_order(
    client: Any,
    purchase_order_id: str,
    payload: PurchaseOrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderRead]:
    """Cancel a purchase order - ``POST /purchase_orders/{purchase_order_id}/cancel``; answered
    ``204``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_orders_urls.PURCHASE_ORDER_CANCEL,
        path_params={"purchase_order_id": purchase_order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderRead,
    )


def change_purchase_order(
    client: Any,
    purchase_order_id: str,
    payload: PurchaseOrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderRead]:
    """Change purchase order - ``POST /purchase_orders/{purchase_order_id}/change``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_orders_urls.PURCHASE_ORDER_CHANGE,
        path_params={"purchase_order_id": purchase_order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderRead,
    )


def get_purchase_order_information(
    client: Any,
    purchase_order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderInformation]:
    """The information block of one purchase order -
    ``GET /purchase_orders/{purchase_order_id}/information``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_INFORMATION,
        path_params={"purchase_order_id": purchase_order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderInformation,
    )


def get_purchase_order_kpis(
    client: Any,
    purchase_order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderKpis]:
    """A purchase order's KPI block - ``GET /purchase_orders/{purchase_order_id}/kpis``, under
    ``purchase_order_kpis``; the same block ``get_purchase_order`` carries as ``kpis``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_KPIS,
        path_params={"purchase_order_id": purchase_order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderKpis,
    )


def get_purchase_order_lines(
    client: Any,
    purchase_order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderLineList]:
    """The lines of one purchase order - ``GET /purchase_orders/{purchase_order_id}/lines``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_LINES,
        path_params={"purchase_order_id": purchase_order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderLineList,
    )


def get_purchase_order_notes(
    client: Any,
    purchase_order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderNotes]:
    """List notes - ``GET /purchase_orders/{purchase_order_id}/notes``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_NOTES,
        path_params={"purchase_order_id": purchase_order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderNotes,
    )


def create_purchase_order_note(
    client: Any,
    purchase_order_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderNotesView]:
    """Create note - ``POST /purchase_orders/{purchase_order_id}/notes``;
    multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        purchase_orders_urls.PURCHASE_ORDER_NOTES,
        path_params={"purchase_order_id": purchase_order_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderNotesView,
    )


def create_purchase_order_purchase_invoice(
    client: Any,
    purchase_order_id: str,
    payload: PurchaseOrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderPurchaseInvoices]:
    """Create PI from PO -
    ``POST /purchase_orders/{purchase_order_id}/purchase_invoices``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_orders_urls.PURCHASE_ORDER_PURCHASE_INVOICES,
        path_params={"purchase_order_id": purchase_order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderPurchaseInvoices,
    )


def get_purchase_order_purchase_invoices(
    client: Any,
    purchase_order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderPurchaseInvoiceList]:
    """List linked invoices - ``GET /purchase_orders/{purchase_order_id}/purchase_invoices``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_PURCHASE_INVOICES,
        path_params={"purchase_order_id": purchase_order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderPurchaseInvoiceList,
    )


def get_purchase_order_purchase_payments(
    client: Any,
    purchase_order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderPurchasePaymentList]:
    """List linked payments - ``GET /purchase_orders/{purchase_order_id}/purchase_payments``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_PURCHASE_PAYMENTS,
        path_params={"purchase_order_id": purchase_order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderPurchasePaymentList,
    )


def reactivate_purchase_order(
    client: Any,
    purchase_order_id: str,
    payload: PurchaseOrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderRead]:
    """Reactivate a purchase order - ``POST /purchase_orders/{purchase_order_id}/reactivate``;
    answered ``204``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_orders_urls.PURCHASE_ORDER_REACTIVATE,
        path_params={"purchase_order_id": purchase_order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderRead,
    )


def get_purchase_order_line(
    client: Any,
    purchase_order_id: str,
    purchase_order_line_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderLineRead]:
    """One purchase order line -
    ``GET /purchase_orders/{purchase_order_id}/lines/{purchase_order_line_uuid}``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_LINE,
        path_params={
            "purchase_order_id": purchase_order_id,
            "purchase_order_line_uuid": purchase_order_line_uuid,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderLineRead,
    )


def delete_purchase_order_note(
    client: Any,
    purchase_order_id: str,
    purchase_order_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete note -
    ``DELETE /purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}``."""
    return client.send_delete_request(
        purchase_orders_urls.PURCHASE_ORDER_NOTE,
        path_params={
            "purchase_order_id": purchase_order_id,
            "purchase_order_note_id": purchase_order_note_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_purchase_order_note(
    client: Any,
    purchase_order_id: str,
    purchase_order_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderNote]:
    """Get specific note -
    ``GET /purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_NOTE,
        path_params={
            "purchase_order_id": purchase_order_id,
            "purchase_order_note_id": purchase_order_note_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderNote,
    )


def get_purchase_order_note_files(
    client: Any,
    purchase_order_id: str,
    purchase_order_note_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderNote]:
    """List note files -
    ``GET /purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}/files``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_NOTE_FILES,
        path_params={
            "purchase_order_id": purchase_order_id,
            "purchase_order_note_id": purchase_order_note_id,
        },
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderNote,
    )


def get_purchase_order_note_file(
    client: Any,
    purchase_order_id: str,
    purchase_order_note_id: str,
    purchase_order_file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderNoteFile]:
    """Get note file -
    ``GET /purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}/files/{purchase_order_file_id}``."""
    return client.send_get_request(
        purchase_orders_urls.PURCHASE_ORDER_NOTE_FILE,
        path_params={
            "purchase_order_id": purchase_order_id,
            "purchase_order_note_id": purchase_order_note_id,
            "purchase_order_file_id": purchase_order_file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderNoteFile,
    )


def delete_purchase_order_note_file(
    client: Any,
    purchase_order_id: str,
    purchase_order_note_id: str,
    purchase_order_file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one attachment -
    ``DELETE /purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}/files/{purchase_order_file_id}``,
    by the purchase order's code and the attachment's ``uuid``; ``204``."""
    return client.send_delete_request(
        purchase_orders_urls.PURCHASE_ORDER_NOTE_FILE,
        path_params={
            "purchase_order_id": purchase_order_id,
            "purchase_order_note_id": purchase_order_note_id,
            "purchase_order_file_id": purchase_order_file_id,
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
