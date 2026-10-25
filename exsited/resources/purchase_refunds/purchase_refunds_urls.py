"""Path templates and body keys for the purchase refund endpoints."""

from __future__ import annotations

PURCHASE_REFUNDS = "/api/{api_version}/purchase_refunds"
#: ``{purchase_refund_id}`` is the refund's code; the writes match nothing else.
PURCHASE_REFUND = "/api/{api_version}/purchase_refunds/{purchase_refund_id}"

#: A purchase refund is raised against a purchase credit note, never at ``/purchase_refunds``.
PURCHASE_CREDIT_NOTE_PURCHASE_REFUNDS = (
    "/api/{api_version}/purchase_credit_notes/{purchase_credit_note_id}/purchase_refunds"
)

#: The key a listing's records sit under.
PURCHASE_REFUNDS_KEY = "data"

#: The envelope one record arrives under.
PURCHASE_REFUND_KEY = "purchase_refund"

#: The keys ``update_purchase_refund`` takes under ``purchase_refund``; any other is a ``400``.
PURCHASE_REFUND_UPDATE_KEYS = ("alternate_date", "reference", "note", "custom_attributes")
