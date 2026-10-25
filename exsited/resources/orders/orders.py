"""Order endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.orders import orders_urls
from exsited.resources.orders.orders_dto import (
    AccountOrders,
    OrderBillingPreferences,
    OrderCustomObject,
    OrderDiscardDraft,
    OrderExtendTrial,
    OrderInformation,
    OrderItemFulfillment,
    OrderKpis,
    OrderLine,
    OrderList,
    OrderNoteFile,
    OrderNoteFileList,
    OrderNoteList,
    OrderNoteView,
    OrderPayment,
    OrderPaymentMethod,
    OrderPaymentMethods,
    OrderPdf,
    OrderQuotePartialInvoices,
    OrderRead,
)

__all__ = [
    "get_orders",
    "create_order",
    "get_order",
    "delete_order",
    "activate_order",
    "create_order_activate_draft",
    "get_order_billing_preferences",
    "update_order_billing_preferences",
    "replace_order_billing_preferences",
    "cancel_order",
    "change_order",
    "create_order_convert_to_order",
    "get_order_custom_objects",
    "get_order_custom_objects_instances",
    "create_order_discard_draft",
    "create_order_extend_trial",
    "get_order_information",
    "update_order_information",
    "get_order_item_fulfillments",
    "get_order_lines",
    "get_order_notes",
    "create_order_note",
    "get_order_payment_methods",
    "get_order_pdf",
    "reactivate_order",
    "create_order_relinquish",
    "update_order_line",
    "get_order_line",
    "delete_order_note",
    "get_order_note",
    "update_order_note",
    "get_order_payment_method",
    "update_order_line_billing_preferences",
    "replace_order_line_billing_preferences",
    "get_order_note_files",
    "get_order_note_file",
    "get_orders_notes",
    "preview_order",
    "create_order_express",
    "accept_order",
    "activate_order_invoice_from_dormant",
    "preview_order_change",
    "change_order_status",
    "adjust_order_contract",
    "preview_order_contract_adjustment",
    "downgrade_order",
    "preview_order_downgrade",
    "upgrade_order",
    "preview_order_upgrade",
    "terminate_order_trial",
    "delete_order_note_file",
    "get_order_custom_object",
    "get_order_custom_object_instance",
    "get_order_custom_objects_instance",
    "get_order_custom_objects_instance_instance",
    "get_order_item_fulfillment",
    "get_order_kpis",
    "get_order_payment",
    "get_order_quote_partial_invoices",
    "get_order_shipping_pdf",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

OrderPayload = Mapping[str, Any] | str | Dto


def get_orders(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderList]:
    """List of all orders - ``GET /orders``."""
    return client.send_get_request(
        orders_urls.ORDERS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderList,
    )


def create_order(
    client: Any,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Create order - ``POST /orders``; answered ``201``. A contract needs a recurring or metered
    item on a line."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDERS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def get_order(
    client: Any,
    order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Order details - ``GET /orders/{order_id}``."""
    return client.send_get_request(
        orders_urls.ORDER,
        path_params={"order_id": order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def delete_order(
    client: Any,
    order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete order - ``DELETE /orders/{order_id}``."""
    return client.send_delete_request(
        orders_urls.ORDER,
        path_params={"order_id": order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def activate_order(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Activate order - ``POST /orders/{order_id}/activate``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_ACTIVATE,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_order_activate_draft(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Activate draft order - ``POST /orders/{order_id}/activate_draft``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_ACTIVATE_DRAFT,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def get_order_billing_preferences(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderBillingPreferences]:
    """Billing preferences - ``GET /orders/{order_id}/billing_preferences``."""
    return client.send_get_request(
        orders_urls.ORDER_BILLING_PREFERENCES,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderBillingPreferences,
    )


def update_order_billing_preferences(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Update billing preferences - ``PATCH /orders/{order_id}/billing_preferences``."""
    _require_payload(payload)
    return client.send_patch_request(
        orders_urls.ORDER_BILLING_PREFERENCES,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def replace_order_billing_preferences(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Update billing preferences - ``PUT /orders/{order_id}/billing_preferences``."""
    _require_payload(payload)
    return client.send_put_request(
        orders_urls.ORDER_BILLING_PREFERENCES,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def cancel_order(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Cancel order - ``POST /orders/{order_id}/cancel``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_CANCEL,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def change_order(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Change order - ``POST /orders/{order_id}/change``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_CHANGE,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def create_order_convert_to_order(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Convert quote order - ``POST /orders/{order_id}/convert_to_order``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_CONVERT_TO_ORDER,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def get_order_custom_objects(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountOrders]:
    """List custom objects - ``GET /orders/{order_id}/custom_objects``."""
    return client.send_get_request(
        orders_urls.ORDER_CUSTOM_OBJECTS,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountOrders,
    )


def get_order_custom_objects_instances(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountOrders]:
    """List custom object instances - ``GET /orders/{order_id}/custom_objects_instances``."""
    return client.send_get_request(
        orders_urls.ORDER_CUSTOM_OBJECTS_INSTANCES,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountOrders,
    )


def create_order_discard_draft(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderDiscardDraft]:
    """Discard draft order - ``POST /orders/{order_id}/discard_draft``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_DISCARD_DRAFT,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderDiscardDraft,
    )


def create_order_extend_trial(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderExtendTrial]:
    """Extend trial - ``POST /orders/{order_id}/extend_trial``; the new window starts after the
    current trial ends."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_EXTEND_TRIAL,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderExtendTrial,
    )


def get_order_information(
    client: Any,
    order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderInformation]:
    """Order information - ``GET /orders/{order_id}/information``."""
    return client.send_get_request(
        orders_urls.ORDER_INFORMATION,
        path_params={"order_id": order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderInformation,
    )


def update_order_information(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Update order information - ``PATCH /orders/{order_id}/information``."""
    _require_payload(payload)
    return client.send_patch_request(
        orders_urls.ORDER_INFORMATION,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def get_order_item_fulfillments(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountOrders]:
    """List fulfillments - ``GET /orders/{order_id}/item_fulfillments``."""
    return client.send_get_request(
        orders_urls.ORDER_ITEM_FULFILLMENTS,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountOrders,
    )


def get_order_lines(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """List of order lines - ``GET /orders/{order_id}/lines``."""
    return client.send_get_request(
        orders_urls.ORDER_LINES,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def get_order_notes(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderNoteList]:
    """List notes - ``GET /orders/{order_id}/notes``."""
    return client.send_get_request(
        orders_urls.ORDER_NOTES,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderNoteList,
    )


def create_order_note(
    client: Any,
    order_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderNoteView]:
    """Create note - ``POST /orders/{order_id}/notes``;
    multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        orders_urls.ORDER_NOTES,
        path_params={"order_id": order_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderNoteView,
    )


def get_order_payment_methods(
    client: Any,
    order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderPaymentMethods]:
    """List order payment methods - ``GET /orders/{order_id}/payment_methods``."""
    return client.send_get_request(
        orders_urls.ORDER_PAYMENT_METHODS,
        path_params={"order_id": order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderPaymentMethods,
    )


def get_order_pdf(
    client: Any,
    order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderPdf]:
    """Order PDF - ``GET /orders/{order_id}/pdf``."""
    return client.send_get_request(
        orders_urls.ORDER_PDF,
        path_params={"order_id": order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderPdf,
    )


def reactivate_order(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Reactivate order - ``POST /orders/{order_id}/reactivate``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_REACTIVATE,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def create_order_relinquish(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Pre-order relinquish - ``POST /orders/{order_id}/relinquish``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_RELINQUISH,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def update_order_line(
    client: Any,
    order_id: str,
    line_uuid: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Update line information - ``PATCH /orders/{order_id}/lines/{line_uuid}``."""
    _require_payload(payload)
    return client.send_patch_request(
        orders_urls.ORDER_LINE,
        path_params={"order_id": order_id, "line_uuid": line_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def get_order_line(
    client: Any,
    order_id: str,
    line_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderLine]:
    """Single line details - ``GET /orders/{order_id}/lines/{line_uuid}``."""
    return client.send_get_request(
        orders_urls.ORDER_LINE,
        path_params={"order_id": order_id, "line_uuid": line_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderLine,
    )


def delete_order_note(
    client: Any,
    order_id: str,
    order_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete note - ``DELETE /orders/{order_id}/notes/{order_note_id}``."""
    return client.send_delete_request(
        orders_urls.ORDER_NOTE,
        path_params={"order_id": order_id, "order_note_id": order_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_order_note(
    client: Any,
    order_id: str,
    order_note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderNoteView]:
    """Get specific note - ``GET /orders/{order_id}/notes/{order_note_id}``."""
    return client.send_get_request(
        orders_urls.ORDER_NOTE,
        path_params={"order_id": order_id, "order_note_id": order_note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderNoteView,
    )


def update_order_note(
    client: Any,
    order_id: str,
    order_note_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderNoteView]:
    """Update note - ``PATCH /orders/{order_id}/notes/{order_note_id}``;
    multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_patch_request(
        orders_urls.ORDER_NOTE,
        path_params={"order_id": order_id, "order_note_id": order_note_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderNoteView,
    )


def get_order_payment_method(
    client: Any,
    order_id: str,
    payment_method_ref: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderPaymentMethod]:
    """Get single - ``GET /orders/{order_id}/payment_methods/{payment_method_ref}``."""
    return client.send_get_request(
        orders_urls.ORDER_PAYMENT_METHOD,
        path_params={"order_id": order_id, "payment_method_ref": payment_method_ref},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderPaymentMethod,
    )


def update_order_line_billing_preferences(
    client: Any,
    order_id: str,
    line_uuid: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Update line billing preferences -
    ``PATCH /orders/{order_id}/lines/{line_uuid}/billing_preferences``."""
    _require_payload(payload)
    return client.send_patch_request(
        orders_urls.ORDER_LINE_BILLING_PREFERENCES,
        path_params={"order_id": order_id, "line_uuid": line_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def replace_order_line_billing_preferences(
    client: Any,
    order_id: str,
    line_uuid: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Update line billing preferences -
    ``PUT /orders/{order_id}/lines/{line_uuid}/billing_preferences``."""
    _require_payload(payload)
    return client.send_put_request(
        orders_urls.ORDER_LINE_BILLING_PREFERENCES,
        path_params={"order_id": order_id, "line_uuid": line_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def get_order_note_files(
    client: Any,
    order_id: str,
    order_note_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderNoteFileList]:
    """List note files - ``GET /orders/{order_id}/notes/{order_note_id}/files``."""
    return client.send_get_request(
        orders_urls.ORDER_NOTE_FILES,
        path_params={"order_id": order_id, "order_note_id": order_note_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderNoteFileList,
    )


def get_order_note_file(
    client: Any,
    order_id: str,
    order_note_id: str,
    order_file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderNoteFile]:
    """Get note file - ``GET /orders/{order_id}/notes/{order_note_id}/files/{order_file_id}``."""
    return client.send_get_request(
        orders_urls.ORDER_NOTE_FILE,
        path_params={
            "order_id": order_id,
            "order_note_id": order_note_id,
            "order_file_id": order_file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderNoteFile,
    )


def get_orders_notes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderNoteList]:
    """List the notes of every order - ``GET /orders/notes``; not scoped to one order."""
    return client.send_get_request(
        orders_urls.ORDERS_NOTES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderNoteList,
    )


def preview_order(
    client: Any,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Price an order without creating it - ``POST /orders/preview``, the ``create_order`` body;
    ``201``, with no cart data in the answer. An ``account`` object still creates that account."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDERS_PREVIEW,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_order_express(
    client: Any,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create an order, and its invoice and payment if the body nests them, in one call -
    ``POST /orders/express``, the ``create_express`` body under ``account``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDERS_EXPRESS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def accept_order(
    client: Any,
    order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Accept an order's pending acceptance - ``POST /orders/{order_id}/accept``; no body sent.
    It raises an invoice and may require payment."""
    return client.send_post_request(
        orders_urls.ORDER_ACCEPT,
        path_params={"order_id": order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def activate_order_invoice_from_dormant(
    client: Any,
    order_id: str,
    invoice_uuid: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Activate a dormant invoice - ``POST /orders/{order_id}/activate_invoice_from_dormant/
    {invoice_uuid}``, body under ``activate``: ``due_date``, ``amount``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_ACTIVATE_INVOICE_FROM_DORMANT,
        path_params={"order_id": order_id, "invoice_uuid": invoice_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def preview_order_change(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderRead]:
    """Preview a change - ``POST /orders/{order_id}/change/preview``, the ``change_order`` body;
    nothing is changed, and the answer is the order as it stands."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_CHANGE_PREVIEW,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderRead,
    )


def change_order_status(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Trigger a workflow state - ``POST /orders/{order_id}/change_status``, body
    ``order.workflow_status``; it runs the workflow's connections."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_CHANGE_STATUS,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def adjust_order_contract(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Upgrade or downgrade by package rank - ``POST /orders/{order_id}/contract_adjustment``;
    the body is not wrapped: ``effective_date`` and ``lines``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_CONTRACT_ADJUSTMENT,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def preview_order_contract_adjustment(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Preview a contract adjustment - ``POST /orders/{order_id}/contract_adjustment/preview``,
    the ``adjust_order_contract`` body, not wrapped."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_CONTRACT_ADJUSTMENT_PREVIEW,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def downgrade_order(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Downgrade a contract - ``POST /orders/{order_id}/downgrade``; the body is not wrapped:
    ``effective_date`` and ``lines`` naming each ``charge_item_uuid`` and ``package_name``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_DOWNGRADE,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def preview_order_downgrade(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Preview a downgrade - ``POST /orders/{order_id}/downgrade/preview``, the
    ``downgrade_order`` body, not wrapped."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_DOWNGRADE_PREVIEW,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def upgrade_order(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Upgrade a contract - ``POST /orders/{order_id}/upgrade``; the body is not wrapped:
    ``effective_date`` and ``lines`` naming each ``charge_item_uuid`` and ``package_name``."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_UPGRADE,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def preview_order_upgrade(
    client: Any,
    order_id: str,
    payload: OrderPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Preview an upgrade - ``POST /orders/{order_id}/upgrade/preview``, the ``upgrade_order``
    body, not wrapped."""
    _require_payload(payload)
    return client.send_post_request(
        orders_urls.ORDER_UPGRADE_PREVIEW,
        path_params={"order_id": order_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def terminate_order_trial(
    client: Any,
    order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """End a contract's trial now - ``POST /orders/{order_id}/terminate_trial``; no body sent.
    It starts the contract."""
    return client.send_post_request(
        orders_urls.ORDER_TERMINATE_TRIAL,
        path_params={"order_id": order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_order_note_file(
    client: Any,
    order_id: str,
    order_note_id: str,
    order_file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a note attachment -
    ``DELETE /orders/{order_id}/notes/{order_note_id}/files/{order_file_id}``; ``204``."""
    return client.send_delete_request(
        orders_urls.ORDER_NOTE_FILE,
        path_params={
            "order_id": order_id,
            "order_note_id": order_note_id,
            "order_file_id": order_file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_order_custom_object(
    client: Any,
    order_id: str,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderCustomObject]:
    """One custom object with the order's instances of it -
    ``GET /orders/{order_id}/custom_objects/{custom_object_id}``."""
    return client.send_get_request(
        orders_urls.ORDER_CUSTOM_OBJECT,
        path_params={"order_id": order_id, "custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderCustomObject,
    )


def get_order_custom_object_instance(
    client: Any,
    order_id: str,
    custom_object_id: str,
    instance_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One custom object instance -
    ``GET /orders/{order_id}/custom_objects/{custom_object_id}/instances/{instance_id}``."""
    return client.send_get_request(
        orders_urls.ORDER_CUSTOM_OBJECT_INSTANCE,
        path_params={
            "order_id": order_id,
            "custom_object_id": custom_object_id,
            "instance_id": instance_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_order_custom_objects_instance(
    client: Any,
    order_id: str,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderCustomObject]:
    """The server's alias of ``get_order_custom_object`` -
    ``GET /orders/{order_id}/custom_objects_instances/{custom_object_id}``."""
    return client.send_get_request(
        orders_urls.ORDER_CUSTOM_OBJECTS_INSTANCE,
        path_params={"order_id": order_id, "custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderCustomObject,
    )


def get_order_custom_objects_instance_instance(
    client: Any,
    order_id: str,
    custom_object_id: str,
    instance_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """The server's alias of ``get_order_custom_object_instance`` - ``GET /orders/{order_id}/
    custom_objects_instances/{custom_object_id}/instances/{instance_id}``."""
    return client.send_get_request(
        orders_urls.ORDER_CUSTOM_OBJECTS_INSTANCE_INSTANCE,
        path_params={
            "order_id": order_id,
            "custom_object_id": custom_object_id,
            "instance_id": instance_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_order_item_fulfillment(
    client: Any,
    order_id: str,
    fulfillment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderItemFulfillment]:
    """One fulfillment - ``GET /orders/{order_id}/item_fulfillments/{fulfillment_id}``; the
    server does not check that the fulfillment belongs to the order."""
    return client.send_get_request(
        orders_urls.ORDER_ITEM_FULFILLMENT,
        path_params={"order_id": order_id, "fulfillment_id": fulfillment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderItemFulfillment,
    )


def get_order_kpis(
    client: Any,
    order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderKpis]:
    """An order's KPIs - ``GET /orders/{order_id}/kpis``, under ``order_kpis``."""
    return client.send_get_request(
        orders_urls.ORDER_KPIS,
        path_params={"order_id": order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderKpis,
    )


def get_order_payment(
    client: Any,
    order_id: str,
    payment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderPayment]:
    """One payment - ``GET /orders/{order_id}/payments/{payment_id}``; the server does not
    check that the payment belongs to the order."""
    return client.send_get_request(
        orders_urls.ORDER_PAYMENT,
        path_params={"order_id": order_id, "payment_id": payment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderPayment,
    )


def get_order_quote_partial_invoices(
    client: Any,
    order_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[OrderQuotePartialInvoices]:
    """The deposit and instalment invoices of a converted quote -
    ``GET /orders/{order_id}/quote_partial_invoices``; an unconverted quote answers ``400``."""
    return client.send_get_request(
        orders_urls.ORDER_QUOTE_PARTIAL_INVOICES,
        path_params={"order_id": order_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=OrderQuotePartialInvoices,
    )


def get_order_shipping_pdf(
    client: Any,
    order_id: str,
    shipping_line_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """A shipping line's PDF - ``GET /orders/{order_id}/shipping_pdf/{shipping_line_id}``;
    ``404`` until the line has a generated shipping PDF."""
    return client.send_get_request(
        orders_urls.ORDER_SHIPPING_PDF,
        path_params={"order_id": order_id, "shipping_line_id": shipping_line_id},
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
