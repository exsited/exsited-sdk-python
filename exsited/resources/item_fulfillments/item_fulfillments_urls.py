"""Path templates and body keys for the item fulfillment endpoints."""

from __future__ import annotations

ITEM_FULFILLMENTS = "/api/{api_version}/item_fulfillments"
ITEM_FULFILLMENT = "/api/{api_version}/item_fulfillments/{fulfillment_id}"
ITEM_FULFILLMENT_NOTES = "/api/{api_version}/item_fulfillments/{fulfillment_id}/notes"
ITEM_FULFILLMENT_NOTE = "/api/{api_version}/item_fulfillments/{fulfillment_id}/notes/{note_id}"

#: The key a listing's records sit under.
ITEM_FULFILLMENTS_KEY = "data"
ITEM_FULFILLMENT_NOTES_KEY = "data"

#: The envelope one record arrives under.
INVOICE_KEY = "invoice"
ITEM_FULFILLMENT_KEY = "item_fulfillment"
