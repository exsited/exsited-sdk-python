"""Path templates and body keys for the booking endpoints."""

from __future__ import annotations

BOOKING = "/api/{api_version}/booking"
BOOKING_BY_ID = "/api/{api_version}/booking/{booking_id}"

# Literal second segments, read by the server in the slot a booking id takes.
BOOKING_NOTES = "/api/{api_version}/booking/notes"
BOOKING_PREVIEW = "/api/{api_version}/booking/preview"

# Every other POST /booking/{booking_id}/{word} falls through to create, so change is the only
# transition the path holds.
BOOKING_CHANGE = "/api/{api_version}/booking/{booking_id}/change"
BOOKING_CHANGE_PREVIEW = "/api/{api_version}/booking/{booking_id}/change/preview"

BOOKING_BILLING_PREFERENCES = "/api/{api_version}/booking/{booking_id}/billing_preferences"
BOOKING_INFORMATION = "/api/{api_version}/booking/{booking_id}/information"
BOOKING_LINES = "/api/{api_version}/booking/{booking_id}/lines"
BOOKING_LINE = "/api/{api_version}/booking/{booking_id}/lines/{line_uuid}"
BOOKING_LINE_BILLING_PREFERENCES = (
    "/api/{api_version}/booking/{booking_id}/lines/{line_uuid}/billing_preferences"
)
# custom_objects_instances is the server's alias of custom_objects and answers the same bodies.
BOOKING_CUSTOM_OBJECTS = "/api/{api_version}/booking/{booking_id}/custom_objects"
BOOKING_CUSTOM_OBJECT = "/api/{api_version}/booking/{booking_id}/custom_objects/{custom_object_id}"
BOOKING_CUSTOM_OBJECT_INSTANCE = (
    "/api/{api_version}/booking/{booking_id}/custom_objects/{custom_object_id}"
    "/instances/{instance_id}"
)
BOOKING_CUSTOM_OBJECTS_INSTANCES = (
    "/api/{api_version}/booking/{booking_id}/custom_objects_instances"
)
BOOKING_CUSTOM_OBJECTS_INSTANCE = (
    "/api/{api_version}/booking/{booking_id}/custom_objects_instances/{custom_object_id}"
)
BOOKING_CUSTOM_OBJECTS_INSTANCE_INSTANCE = (
    "/api/{api_version}/booking/{booking_id}/custom_objects_instances/{custom_object_id}"
    "/instances/{instance_id}"
)
BOOKING_INVOICES = "/api/{api_version}/booking/{booking_id}/invoices"
BOOKING_ITEM_FULFILLMENTS = "/api/{api_version}/booking/{booking_id}/item_fulfillments"
BOOKING_ITEM_FULFILLMENT = (
    "/api/{api_version}/booking/{booking_id}/item_fulfillments/{fulfillment_id}"
)
BOOKING_KPIS = "/api/{api_version}/booking/{booking_id}/kpis"
BOOKING_PAYMENT_METHODS = "/api/{api_version}/booking/{booking_id}/payment_methods"
BOOKING_PAYMENT_METHOD = (
    "/api/{api_version}/booking/{booking_id}/payment_methods/{payment_method_ref}"
)
BOOKING_PAYMENTS = "/api/{api_version}/booking/{booking_id}/payments"
BOOKING_PAYMENT = "/api/{api_version}/booking/{booking_id}/payments/{payment_id}"
BOOKING_PDF = "/api/{api_version}/booking/{booking_id}/pdf"
BOOKING_QUOTE_PARTIAL_INVOICES = "/api/{api_version}/booking/{booking_id}/quote_partial_invoices"
BOOKING_SHIPPING_PDF = "/api/{api_version}/booking/{booking_id}/shipping_pdf/{shipping_line_id}"

#: The key a listing's records sit under.
BOOKING_KEY = "data"

#: The envelope one record arrives under.
ORDER_KEY = "order"
