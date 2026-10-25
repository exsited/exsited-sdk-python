"""Path templates and body keys for the purchase order endpoints."""

from __future__ import annotations

PURCHASE_ORDERS = "/api/{api_version}/purchase_orders"
PURCHASE_ORDERS_NOTES = "/api/{api_version}/purchase_orders/notes"
PURCHASE_ORDER = "/api/{api_version}/purchase_orders/{purchase_order_id}"
PURCHASE_ORDER_CANCEL = "/api/{api_version}/purchase_orders/{purchase_order_id}/cancel"
PURCHASE_ORDER_CHANGE = "/api/{api_version}/purchase_orders/{purchase_order_id}/change"
PURCHASE_ORDER_INFORMATION = "/api/{api_version}/purchase_orders/{purchase_order_id}/information"
PURCHASE_ORDER_KPIS = "/api/{api_version}/purchase_orders/{purchase_order_id}/kpis"
PURCHASE_ORDER_LINES = "/api/{api_version}/purchase_orders/{purchase_order_id}/lines"
PURCHASE_ORDER_NOTES = "/api/{api_version}/purchase_orders/{purchase_order_id}/notes"
PURCHASE_ORDER_PURCHASE_INVOICES = (
    "/api/{api_version}/purchase_orders/{purchase_order_id}/purchase_invoices"
)
PURCHASE_ORDER_PURCHASE_PAYMENTS = (
    "/api/{api_version}/purchase_orders/{purchase_order_id}/purchase_payments"
)
PURCHASE_ORDER_REACTIVATE = "/api/{api_version}/purchase_orders/{purchase_order_id}/reactivate"
PURCHASE_ORDER_LINE = (
    "/api/{api_version}/purchase_orders/{purchase_order_id}/lines/{purchase_order_line_uuid}"
)
PURCHASE_ORDER_NOTE = (
    "/api/{api_version}/purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}"
)
PURCHASE_ORDER_NOTE_FILES = (
    "/api/{api_version}/purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}/files"
)
PURCHASE_ORDER_NOTE_FILE = "/api/{api_version}/purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}/files/{purchase_order_file_id}"

#: The key a listing's records sit under.
PURCHASE_ORDERS_KEY = "data"
PURCHASE_ORDERS_NOTES_KEY = "data"
PURCHASE_ORDER_LINES_KEY = "data"
PURCHASE_ORDER_PURCHASE_INVOICES_KEY = "data"
PURCHASE_ORDER_PURCHASE_PAYMENTS_KEY = "data"

#: The envelope one record arrives under.
PURCHASE_ORDER_KEY = "purchase_order"
PURCHASE_ORDER_KPIS_KEY = "purchase_order_kpis"
