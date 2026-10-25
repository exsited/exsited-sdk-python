"""Inventory adjustment endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.inventory_adjustments import inventory_adjustments_urls
from exsited.resources.inventory_adjustments.inventory_adjustments_dto import (
    InventoryAdjustment,
    InventoryAdjustmentList,
)

__all__ = [
    "get_inventory_adjustments",
    "get_inventory_adjustment",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_inventory_adjustments(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InventoryAdjustmentList]:
    """List all - ``GET /inventory_adjustments``."""
    return client.send_get_request(
        inventory_adjustments_urls.INVENTORY_ADJUSTMENTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InventoryAdjustmentList,
    )


def get_inventory_adjustment(
    client: Any,
    inventory_adjustment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InventoryAdjustment]:
    """Get single - ``GET /inventory_adjustments/{inventory_adjustment_id}``."""
    return client.send_get_request(
        inventory_adjustments_urls.INVENTORY_ADJUSTMENT,
        path_params={"inventory_adjustment_id": inventory_adjustment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InventoryAdjustment,
    )
