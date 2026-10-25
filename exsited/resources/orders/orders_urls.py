"""Path templates and body keys for the order endpoints."""

from __future__ import annotations

ORDERS = "/api/{api_version}/orders"
ORDER = "/api/{api_version}/orders/{order_id}"
ORDER_ACTIVATE = "/api/{api_version}/orders/{order_id}/activate"
ORDER_ACTIVATE_DRAFT = "/api/{api_version}/orders/{order_id}/activate_draft"
ORDER_BILLING_PREFERENCES = "/api/{api_version}/orders/{order_id}/billing_preferences"
ORDER_CANCEL = "/api/{api_version}/orders/{order_id}/cancel"
ORDER_CHANGE = "/api/{api_version}/orders/{order_id}/change"
ORDER_CONVERT_TO_ORDER = "/api/{api_version}/orders/{order_id}/convert_to_order"
ORDER_CUSTOM_OBJECTS = "/api/{api_version}/orders/{order_id}/custom_objects"
ORDER_CUSTOM_OBJECTS_INSTANCES = "/api/{api_version}/orders/{order_id}/custom_objects_instances"
ORDER_DISCARD_DRAFT = "/api/{api_version}/orders/{order_id}/discard_draft"
ORDER_EXTEND_TRIAL = "/api/{api_version}/orders/{order_id}/extend_trial"
ORDER_INFORMATION = "/api/{api_version}/orders/{order_id}/information"
ORDER_ITEM_FULFILLMENTS = "/api/{api_version}/orders/{order_id}/item_fulfillments"
ORDER_LINES = "/api/{api_version}/orders/{order_id}/lines"
ORDER_NOTES = "/api/{api_version}/orders/{order_id}/notes"
ORDER_PAYMENT_METHODS = "/api/{api_version}/orders/{order_id}/payment_methods"
ORDER_PDF = "/api/{api_version}/orders/{order_id}/pdf"
ORDER_REACTIVATE = "/api/{api_version}/orders/{order_id}/reactivate"
ORDER_RELINQUISH = "/api/{api_version}/orders/{order_id}/relinquish"
ORDER_LINE = "/api/{api_version}/orders/{order_id}/lines/{line_uuid}"
ORDER_NOTE = "/api/{api_version}/orders/{order_id}/notes/{order_note_id}"
ORDER_PAYMENT_METHOD = "/api/{api_version}/orders/{order_id}/payment_methods/{payment_method_ref}"
ORDER_LINE_BILLING_PREFERENCES = (
    "/api/{api_version}/orders/{order_id}/lines/{line_uuid}/billing_preferences"
)
ORDER_NOTE_FILES = "/api/{api_version}/orders/{order_id}/notes/{order_note_id}/files"
ORDER_NOTE_FILE = "/api/{api_version}/orders/{order_id}/notes/{order_note_id}/files/{order_file_id}"

# Literal second segments. The server reads "notes", "preview" and "express" in the slot an order
# id takes, so each is its own path rather than an order id.
ORDERS_NOTES = "/api/{api_version}/orders/notes"
ORDERS_PREVIEW = "/api/{api_version}/orders/preview"
ORDERS_EXPRESS = "/api/{api_version}/orders/express"

# State transitions. Only a trailing "preview" is special: any other word in that slot runs the
# real operation, so each preview is a path of its own.
ORDER_ACCEPT = "/api/{api_version}/orders/{order_id}/accept"
ORDER_ACTIVATE_INVOICE_FROM_DORMANT = (
    "/api/{api_version}/orders/{order_id}/activate_invoice_from_dormant/{invoice_uuid}"
)
ORDER_CHANGE_PREVIEW = "/api/{api_version}/orders/{order_id}/change/preview"
ORDER_CHANGE_STATUS = "/api/{api_version}/orders/{order_id}/change_status"
ORDER_CONTRACT_ADJUSTMENT = "/api/{api_version}/orders/{order_id}/contract_adjustment"
ORDER_CONTRACT_ADJUSTMENT_PREVIEW = (
    "/api/{api_version}/orders/{order_id}/contract_adjustment/preview"
)
ORDER_DOWNGRADE = "/api/{api_version}/orders/{order_id}/downgrade"
ORDER_DOWNGRADE_PREVIEW = "/api/{api_version}/orders/{order_id}/downgrade/preview"
ORDER_UPGRADE = "/api/{api_version}/orders/{order_id}/upgrade"
ORDER_UPGRADE_PREVIEW = "/api/{api_version}/orders/{order_id}/upgrade/preview"
ORDER_TERMINATE_TRIAL = "/api/{api_version}/orders/{order_id}/terminate_trial"

# Sub-reads. custom_objects_instances is the server's alias of custom_objects, one case in its
# dispatcher, and answers the same bodies.
ORDER_CUSTOM_OBJECT = "/api/{api_version}/orders/{order_id}/custom_objects/{custom_object_id}"
ORDER_CUSTOM_OBJECT_INSTANCE = (
    "/api/{api_version}/orders/{order_id}/custom_objects/{custom_object_id}/instances/{instance_id}"
)
ORDER_CUSTOM_OBJECTS_INSTANCE = (
    "/api/{api_version}/orders/{order_id}/custom_objects_instances/{custom_object_id}"
)
ORDER_CUSTOM_OBJECTS_INSTANCE_INSTANCE = (
    "/api/{api_version}/orders/{order_id}/custom_objects_instances/{custom_object_id}"
    "/instances/{instance_id}"
)
ORDER_ITEM_FULFILLMENT = "/api/{api_version}/orders/{order_id}/item_fulfillments/{fulfillment_id}"
ORDER_KPIS = "/api/{api_version}/orders/{order_id}/kpis"
ORDER_PAYMENT = "/api/{api_version}/orders/{order_id}/payments/{payment_id}"
ORDER_QUOTE_PARTIAL_INVOICES = "/api/{api_version}/orders/{order_id}/quote_partial_invoices"
ORDER_SHIPPING_PDF = "/api/{api_version}/orders/{order_id}/shipping_pdf/{shipping_line_id}"

#: The key a listing's records sit under.
ORDERS_KEY = "data"
ORDER_CUSTOM_OBJECTS_INSTANCES_KEY = "data"
ORDER_CUSTOM_OBJECTS_KEY = "data"
ORDER_ITEM_FULFILLMENTS_KEY = "data"
ORDER_NOTES_KEY = "data"

#: The envelope one record arrives under.
ORDER_KEY = "order"
