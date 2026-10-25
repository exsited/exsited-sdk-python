"""Typed views over the item receipt bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "ItemReceipt",
    "ItemReceiptList",
    "ItemReceipts",
    "ItemReceiptUpdated",
    "PurchaseOrderItemReceipts",
    "ItemReceiptPurchaseOrder",
    "ItemReceiptLine",
    "ItemReceiptCreatedBy",
    "ItemReceiptLastUpdatedBy",
    "ItemReceiptUpdatedPurchaseOrder",
    "ItemReceiptUpdatedLine",
    "ItemReceiptUpdatedCreatedBy",
    "ItemReceiptUpdatedLastUpdatedBy",
    "ItemReceiptLinePurchaseOrderLine",
    "ItemReceiptLineDetail",
    "ItemReceiptLineUom",
    "ItemReceiptLineWarehouse",
    "ItemReceiptUpdatedLinePurchaseOrderLine",
    "ItemReceiptUpdatedLineDetail",
    "ItemReceiptUpdatedLineUom",
    "ItemReceiptUpdatedLineWarehouse",
]


class ItemReceipt(Dto):
    """The item receipt body, under ``item_receipt``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/item_receipts",
        "GET /api/{api_version}/item_receipts/{item_receipt_id}",
    )

    ENVELOPE_KEY = "item_receipt"

    code: str | None = None
    created_by: ItemReceiptCreatedBy | None = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: ItemReceiptLastUpdatedBy | None = None
    last_updated_on: str | None = None
    lines: list[ItemReceiptLine] | None = None
    object: str | None = None
    purchase_order: ItemReceiptPurchaseOrder | None = None
    receipt_date: str | None = None
    receipt_note: str | None = None
    receipt_status: str | None = None
    receive_completed: bool | None = None
    status: str | None = None
    tracking_number: str | None = None
    version: int | None = None


class ItemReceiptList(Dto):
    """One page of ``ItemReceipt`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/item_receipts",)

    data: list[ItemReceipt] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ItemReceipts(Dto):
    """The item receipts body, under ``item-receipt``; measured from the v4 collection, not the
    instance, so read ``.map`` when a field is unexpectedly None."""

    MEASURED_FROM = ("POST /api/{api_version}/item_receipts",)

    ENVELOPE_KEY = "item-receipt"

    activity_logs: list[Any] | None = None
    created_by: str | None = None
    created_on: str | None = None
    date: str | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    note: str | None = None
    purchase_order_id: str | None = None
    receipt_status: str | None = None
    receipts: list[Any] | None = None
    tracking_number: str | None = None
    uuid: str | None = None
    version: str | None = None


class ItemReceiptUpdated(Dto):
    """The item receipt updated body, under ``item_receipt``."""

    MEASURED_FROM = ("PATCH /api/{api_version}/item_receipts/{item_receipt_id}",)

    ENVELOPE_KEY = "item_receipt"

    code: str | None = None
    created_by: ItemReceiptUpdatedCreatedBy | None = None
    created_on: str | None = None
    date: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: ItemReceiptUpdatedLastUpdatedBy | None = None
    last_updated_on: str | None = None
    lines: list[ItemReceiptUpdatedLine] | None = None
    note: str | None = None
    object: str | None = None
    purchase_order: ItemReceiptUpdatedPurchaseOrder | None = None
    purchase_order_id: str | None = None
    receipt_date: str | None = None
    # Null in every record measured, so untyped.
    receipt_note: Any = None
    receipt_status: str | None = None
    receipts: list[Any] | None = None
    receive_completed: bool | None = None
    status: str | None = None
    tracking_number: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseOrderItemReceipts(Dto):
    """The purchase order item receipts body, under ``purchase_order``; measured from the v4
    collection, not the instance, so read ``.map`` when a field is unexpectedly None."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders/{purchase_order_id}/item_receipts",)

    ENVELOPE_KEY = "purchase_order"

    item_receipts: list[Any] | None = None
    pagination: dict[str, Any] | None = None


class ItemReceiptPurchaseOrder(Dto):
    """A :class:`ItemReceipt`'s ``purchase_order``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class ItemReceiptLine(Dto):
    """One entry of a :class:`ItemReceipt`'s ``lines``."""

    item: ItemReceiptLineDetail | None = None
    pending_return_quantity: float | None = None
    purchase_order_line: ItemReceiptLinePurchaseOrderLine | None = None
    receipt_quantity: float | None = None
    received_quantity: float | None = None
    returned_quantity: float | None = None
    uom: ItemReceiptLineUom | None = None
    warehouse: ItemReceiptLineWarehouse | None = None


class ItemReceiptCreatedBy(Dto):
    """A :class:`ItemReceipt`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class ItemReceiptLastUpdatedBy(Dto):
    """A :class:`ItemReceipt`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class ItemReceiptUpdatedPurchaseOrder(Dto):
    """A :class:`ItemReceiptUpdated`'s ``purchase_order``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class ItemReceiptUpdatedLine(Dto):
    """One entry of a :class:`ItemReceiptUpdated`'s ``lines``."""

    item: ItemReceiptUpdatedLineDetail | None = None
    pending_return_quantity: float | None = None
    purchase_order_line: ItemReceiptUpdatedLinePurchaseOrderLine | None = None
    receipt_quantity: float | None = None
    received_quantity: float | None = None
    returned_quantity: float | None = None
    uom: ItemReceiptUpdatedLineUom | None = None
    warehouse: ItemReceiptUpdatedLineWarehouse | None = None


class ItemReceiptUpdatedCreatedBy(Dto):
    """A :class:`ItemReceiptUpdated`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class ItemReceiptUpdatedLastUpdatedBy(Dto):
    """A :class:`ItemReceiptUpdated`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class ItemReceiptLinePurchaseOrderLine(Dto):
    """A :class:`ItemReceiptLine`'s ``purchase_order_line``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemReceiptLineDetail(Dto):
    """A :class:`ItemReceiptLine`'s ``item``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemReceiptLineUom(Dto):
    """A :class:`ItemReceiptLine`'s ``uom``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemReceiptLineWarehouse(Dto):
    """A :class:`ItemReceiptLine`'s ``warehouse``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemReceiptUpdatedLinePurchaseOrderLine(Dto):
    """A :class:`ItemReceiptUpdatedLine`'s ``purchase_order_line``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemReceiptUpdatedLineDetail(Dto):
    """A :class:`ItemReceiptUpdatedLine`'s ``item``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemReceiptUpdatedLineUom(Dto):
    """A :class:`ItemReceiptUpdatedLine`'s ``uom``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemReceiptUpdatedLineWarehouse(Dto):
    """A :class:`ItemReceiptUpdatedLine`'s ``warehouse``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
