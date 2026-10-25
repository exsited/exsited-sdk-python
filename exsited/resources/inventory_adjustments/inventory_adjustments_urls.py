"""Path templates and body keys for the inventory adjustment endpoints."""

from __future__ import annotations

INVENTORY_ADJUSTMENTS = "/api/{api_version}/inventory_adjustments"
INVENTORY_ADJUSTMENT = "/api/{api_version}/inventory_adjustments/{inventory_adjustment_id}"

#: The key a listing's records sit under.
INVENTORY_ADJUSTMENTS_KEY = "data"

#: The envelope one record arrives under.
INVENTORY_ADJUSTMENT_KEY = "inventory_adjustment"
