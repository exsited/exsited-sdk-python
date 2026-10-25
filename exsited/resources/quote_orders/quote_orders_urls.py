"""Path templates and body keys for the quote order endpoints."""

from __future__ import annotations

# The server serves this one read under quote_orders; a quote itself is read, written and
# converted under /orders. A quote_order_id that is not a quote answers 404.
QUOTE_ORDER_INVOICES = "/api/{api_version}/quote_orders/{quote_order_id}/invoices"

#: The key a listing's records sit under.
QUOTE_ORDER_INVOICES_KEY = "data"
