"""Item receipt endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.item_receipts import item_receipts_urls
from exsited.resources.item_receipts.item_receipts_dto import (
    ItemReceipt,
    ItemReceiptList,
    ItemReceipts,
    ItemReceiptUpdated,
    PurchaseOrderItemReceipts,
)

__all__ = [
    "get_item_receipts",
    "create_item_receipt",
    "update_item_receipt",
    "get_item_receipt",
    "get_purchase_order_item_receipts",
    "delete_item_receipt",
    "delete_item_receipt_note",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ItemReceiptPayload = Mapping[str, Any] | str | Dto


def get_item_receipts(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemReceiptList]:
    """List item receipts - ``GET /item_receipts``."""
    return client.send_get_request(
        item_receipts_urls.ITEM_RECEIPTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemReceiptList,
    )


def create_item_receipt(
    client: Any,
    payload: ItemReceiptPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemReceipts]:
    """Create item receipt - ``POST /item_receipts``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        item_receipts_urls.ITEM_RECEIPTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemReceipts,
    )


def update_item_receipt(
    client: Any,
    item_receipt_id: str,
    payload: ItemReceiptPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemReceiptUpdated]:
    """Update item receipt - ``PATCH /item_receipts/{item_receipt_id}``; answered ``202``."""
    _require_payload(payload)
    return client.send_patch_request(
        item_receipts_urls.ITEM_RECEIPT,
        path_params={"item_receipt_id": item_receipt_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemReceiptUpdated,
    )


def get_item_receipt(
    client: Any,
    item_receipt_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemReceipt]:
    """Get single - ``GET /item_receipts/{item_receipt_id}``."""
    return client.send_get_request(
        item_receipts_urls.ITEM_RECEIPT,
        path_params={"item_receipt_id": item_receipt_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemReceipt,
    )


def get_purchase_order_item_receipts(
    client: Any,
    purchase_order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseOrderItemReceipts]:
    """List purchase order item receipts -
    ``GET /purchase_orders/{purchase_order_id}/item_receipts``."""
    return client.send_get_request(
        item_receipts_urls.PURCHASE_ORDER_ITEM_RECEIPTS,
        path_params={"purchase_order_id": purchase_order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseOrderItemReceipts,
    )


def delete_item_receipt(
    client: Any,
    item_receipt_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete item receipt - ``DELETE /item_receipts/{item_receipt_id}``, by its ``ir_`` id;
    refused ``400`` ``stock_committed`` once the receipt is completed."""
    return client.send_delete_request(
        item_receipts_urls.ITEM_RECEIPT,
        path_params={"item_receipt_id": item_receipt_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_item_receipt_note(
    client: Any,
    item_receipt_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete item receipt note - ``DELETE /item_receipts/{item_receipt_id}/notes/{note_id}``,
    ``ir_`` and ``note_`` ids; no route lists or creates a receipt's notes."""
    return client.send_delete_request(
        item_receipts_urls.ITEM_RECEIPT_NOTE,
        path_params={"item_receipt_id": item_receipt_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
