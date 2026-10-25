"""Typed views over the inventory adjustment bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "InventoryAdjustment",
    "InventoryAdjustmentList",
]


class InventoryAdjustment(Dto):
    """The inventory adjustment body, under ``inventory_adjustment``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/inventory_adjustments",
        "GET /api/{api_version}/inventory_adjustments/{inventory_adjustment_id}",
        "GET /api/{api_version}/items/{item_id}/inventory_adjustments",
    )

    ENVELOPE_KEY = "inventory_adjustment"

    adjustment_amount: str | None = None
    adjustment_type: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    item_id: str | None = None
    item_name: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    quantity_available: str | None = None
    quantity_on_hand: str | None = None
    quantity_on_order: str | None = None
    quantity_on_purchase_return: str | None = None
    quantity_on_reserve: str | None = None
    quantity_on_return: str | None = None
    quantity_promised: str | None = None
    reference: str | None = None
    status: str | None = None
    warehouse_name: str | None = None


class InventoryAdjustmentList(Dto):
    """One page of ``InventoryAdjustment`` records, under ``data``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/inventory_adjustments",
        "GET /api/{api_version}/items/{item_id}/inventory_adjustments",
    )

    data: list[InventoryAdjustment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
