"""Path templates and body keys for the item receipt endpoints."""

from __future__ import annotations

ITEM_RECEIPTS = "/api/{api_version}/item_receipts"
ITEM_RECEIPT = "/api/{api_version}/item_receipts/{item_receipt_id}"
ITEM_RECEIPT_NOTE = "/api/{api_version}/item_receipts/{item_receipt_id}/notes/{note_id}"
PURCHASE_ORDER_ITEM_RECEIPTS = (
    "/api/{api_version}/purchase_orders/{purchase_order_id}/item_receipts"
)

#: The key a listing's records sit under.
ITEM_RECEIPTS_KEY = "data"

#: The envelope one record arrives under.
ITEM_RECEIPT_KEY = "item_receipt"
PURCHASE_ORDER_KEY = "purchase_order"
