"""Booking endpoints, under ``/api/{api_version}/booking``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.bookings import bookings_urls
from exsited.resources.bookings.bookings_dto import (
    BookingBillingPreferencesView,
    BookingById,
    BookingCustomObject,
    BookingCustomObjectList,
    BookingInvoiceList,
    BookingItemFulfillment,
    BookingKpis,
    BookingLine,
    BookingList,
    BookingNoteList,
    BookingPaymentList,
    BookingPaymentMethod,
    BookingPaymentMethods,
    BookingPaymentView,
    BookingPdf,
    BookingQuotePartialInvoices,
)

__all__ = [
    "get_booking",
    "get_booking_by_id",
    "create_booking",
    "preview_booking",
    "delete_booking",
    "get_booking_notes",
    "get_booking_billing_preferences",
    "update_booking_billing_preferences",
    "change_booking",
    "preview_booking_change",
    "get_booking_information",
    "update_booking_information",
    "get_booking_lines",
    "get_booking_line",
    "update_booking_line",
    "update_booking_line_billing_preferences",
    "get_booking_custom_objects",
    "get_booking_custom_object",
    "get_booking_custom_object_instance",
    "get_booking_custom_objects_instances",
    "get_booking_custom_objects_instance",
    "get_booking_custom_objects_instance_instance",
    "get_booking_invoices",
    "get_booking_item_fulfillments",
    "get_booking_item_fulfillment",
    "get_booking_kpis",
    "get_booking_payment_methods",
    "get_booking_payment_method",
    "get_booking_payments",
    "get_booking_payment",
    "get_booking_pdf",
    "get_booking_quote_partial_invoices",
    "get_booking_shipping_pdf",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

BookingPayload = Mapping[str, Any] | str | Dto


def get_booking(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingList]:
    """List all bookings - ``GET /booking``."""
    return client.send_get_request(
        bookings_urls.BOOKING,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingList,
    )


def get_booking_by_id(
    client: Any,
    booking_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingById]:
    """Get single booking - ``GET /booking/{booking_id}``."""
    return client.send_get_request(
        bookings_urls.BOOKING_BY_ID,
        path_params={"booking_id": booking_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingById,
    )


def create_booking(
    client: Any,
    payload: BookingPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a booking - ``POST /booking``, the ``create_order`` body under ``order``; ``201``,
    answered under ``booking``. Each line needs a labour and its booking times."""
    _require_payload(payload)
    return client.send_post_request(
        bookings_urls.BOOKING,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def preview_booking(
    client: Any,
    payload: BookingPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Price a booking without creating it - ``POST /booking/preview``, the ``create_booking``
    body; ``201``, with no cart data in the answer, under ``booking``."""
    _require_payload(payload)
    return client.send_post_request(
        bookings_urls.BOOKING_PREVIEW,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_booking(
    client: Any,
    booking_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a booking - ``DELETE /booking/{booking_id}``; ``204``. The server deletes any
    order by this path, whatever its type."""
    return client.send_delete_request(
        bookings_urls.BOOKING_BY_ID,
        path_params={"booking_id": booking_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_booking_notes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingNoteList]:
    """List the notes of every order - ``GET /booking/notes``, the same list as
    ``orders.get_orders_notes``; ``/booking/{booking_id}/notes`` is refused."""
    return client.send_get_request(
        bookings_urls.BOOKING_NOTES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingNoteList,
    )


def get_booking_billing_preferences(
    client: Any,
    booking_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingBillingPreferencesView]:
    """A booking's billing preferences - ``GET /booking/{booking_id}/billing_preferences``."""
    return client.send_get_request(
        bookings_urls.BOOKING_BILLING_PREFERENCES,
        path_params={"booking_id": booking_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingBillingPreferencesView,
    )


def update_booking_billing_preferences(
    client: Any,
    booking_id: str,
    payload: BookingPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingById]:
    """Update a booking's billing preferences - ``PATCH /booking/{booking_id}/billing_preferences``,
    body ``order.billing_preferences``; answered with the whole booking under ``order``."""
    _require_payload(payload)
    return client.send_patch_request(
        bookings_urls.BOOKING_BILLING_PREFERENCES,
        path_params={"booking_id": booking_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingById,
    )


def change_booking(
    client: Any,
    booking_id: str,
    payload: BookingPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Change a booking - ``POST /booking/{booking_id}/change``, body under ``booking``:
    ``effective_date`` and ``lines``. Only a booking-type order is accepted."""
    _require_payload(payload)
    return client.send_post_request(
        bookings_urls.BOOKING_CHANGE,
        path_params={"booking_id": booking_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def preview_booking_change(
    client: Any,
    booking_id: str,
    payload: BookingPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Preview a booking change - ``POST /booking/{booking_id}/change/preview``, the
    ``change_booking`` body; nothing is changed."""
    _require_payload(payload)
    return client.send_post_request(
        bookings_urls.BOOKING_CHANGE_PREVIEW,
        path_params={"booking_id": booking_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_booking_information(
    client: Any,
    booking_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingById]:
    """A booking's header - ``GET /booking/{booking_id}/information``."""
    return client.send_get_request(
        bookings_urls.BOOKING_INFORMATION,
        path_params={"booking_id": booking_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingById,
    )


def update_booking_information(
    client: Any,
    booking_id: str,
    payload: BookingPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingById]:
    """Update a booking's header - ``PATCH /booking/{booking_id}/information``, body under
    ``order``; answered with the whole booking under ``order``."""
    _require_payload(payload)
    return client.send_patch_request(
        bookings_urls.BOOKING_INFORMATION,
        path_params={"booking_id": booking_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingById,
    )


def get_booking_lines(
    client: Any,
    booking_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingById]:
    """A booking with its lines - ``GET /booking/{booking_id}/lines``, under ``order``."""
    return client.send_get_request(
        bookings_urls.BOOKING_LINES,
        path_params={"booking_id": booking_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingById,
    )


def get_booking_line(
    client: Any,
    booking_id: str,
    line_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingLine]:
    """One booking line - ``GET /booking/{booking_id}/lines/{line_uuid}``, under ``order_line``."""
    return client.send_get_request(
        bookings_urls.BOOKING_LINE,
        path_params={"booking_id": booking_id, "line_uuid": line_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingLine,
    )


def update_booking_line(
    client: Any,
    booking_id: str,
    line_uuid: str,
    payload: BookingPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingById]:
    """Update a booking line - ``PATCH /booking/{booking_id}/lines/{line_uuid}``, body
    ``order.line``; answered with the whole booking under ``order``."""
    _require_payload(payload)
    return client.send_patch_request(
        bookings_urls.BOOKING_LINE,
        path_params={"booking_id": booking_id, "line_uuid": line_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingById,
    )


def update_booking_line_billing_preferences(
    client: Any,
    booking_id: str,
    line_uuid: str,
    payload: BookingPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingById]:
    """Update a line's billing preferences -
    ``PATCH /booking/{booking_id}/lines/{line_uuid}/billing_preferences``, body
    ``order.line.item_properties``, not ``billing_preferences``."""
    _require_payload(payload)
    return client.send_patch_request(
        bookings_urls.BOOKING_LINE_BILLING_PREFERENCES,
        path_params={"booking_id": booking_id, "line_uuid": line_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingById,
    )


def get_booking_custom_objects(
    client: Any,
    booking_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingCustomObjectList]:
    """List the custom objects orders use, with the booking's instances -
    ``GET /booking/{booking_id}/custom_objects``."""
    return client.send_get_request(
        bookings_urls.BOOKING_CUSTOM_OBJECTS,
        path_params={"booking_id": booking_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingCustomObjectList,
    )


def get_booking_custom_object(
    client: Any,
    booking_id: str,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingCustomObject]:
    """One custom object with the booking's instances of it -
    ``GET /booking/{booking_id}/custom_objects/{custom_object_id}``."""
    return client.send_get_request(
        bookings_urls.BOOKING_CUSTOM_OBJECT,
        path_params={"booking_id": booking_id, "custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingCustomObject,
    )


def get_booking_custom_object_instance(
    client: Any,
    booking_id: str,
    custom_object_id: str,
    instance_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One custom object instance -
    ``GET /booking/{booking_id}/custom_objects/{custom_object_id}/instances/{instance_id}``."""
    return client.send_get_request(
        bookings_urls.BOOKING_CUSTOM_OBJECT_INSTANCE,
        path_params={
            "booking_id": booking_id,
            "custom_object_id": custom_object_id,
            "instance_id": instance_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_booking_custom_objects_instances(
    client: Any,
    booking_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingCustomObjectList]:
    """The server's alias of ``get_booking_custom_objects`` -
    ``GET /booking/{booking_id}/custom_objects_instances``."""
    return client.send_get_request(
        bookings_urls.BOOKING_CUSTOM_OBJECTS_INSTANCES,
        path_params={"booking_id": booking_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingCustomObjectList,
    )


def get_booking_custom_objects_instance(
    client: Any,
    booking_id: str,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingCustomObject]:
    """The server's alias of ``get_booking_custom_object`` -
    ``GET /booking/{booking_id}/custom_objects_instances/{custom_object_id}``."""
    return client.send_get_request(
        bookings_urls.BOOKING_CUSTOM_OBJECTS_INSTANCE,
        path_params={"booking_id": booking_id, "custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingCustomObject,
    )


def get_booking_custom_objects_instance_instance(
    client: Any,
    booking_id: str,
    custom_object_id: str,
    instance_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """The server's alias of ``get_booking_custom_object_instance`` - ``GET /booking/
    {booking_id}/custom_objects_instances/{custom_object_id}/instances/{instance_id}``."""
    return client.send_get_request(
        bookings_urls.BOOKING_CUSTOM_OBJECTS_INSTANCE_INSTANCE,
        path_params={
            "booking_id": booking_id,
            "custom_object_id": custom_object_id,
            "instance_id": instance_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_booking_invoices(
    client: Any,
    booking_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingInvoiceList]:
    """List a booking's invoices - ``GET /booking/{booking_id}/invoices``."""
    return client.send_get_request(
        bookings_urls.BOOKING_INVOICES,
        path_params={"booking_id": booking_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingInvoiceList,
    )


def get_booking_item_fulfillments(
    client: Any,
    booking_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List a booking's fulfillments - ``GET /booking/{booking_id}/item_fulfillments``."""
    return client.send_get_request(
        bookings_urls.BOOKING_ITEM_FULFILLMENTS,
        path_params={"booking_id": booking_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_booking_item_fulfillment(
    client: Any,
    booking_id: str,
    fulfillment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingItemFulfillment]:
    """One fulfillment - ``GET /booking/{booking_id}/item_fulfillments/{fulfillment_id}``; the
    server does not check that the fulfillment belongs to the booking."""
    return client.send_get_request(
        bookings_urls.BOOKING_ITEM_FULFILLMENT,
        path_params={"booking_id": booking_id, "fulfillment_id": fulfillment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingItemFulfillment,
    )


def get_booking_kpis(
    client: Any,
    booking_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingKpis]:
    """A booking's KPIs - ``GET /booking/{booking_id}/kpis``, under ``order_kpis``."""
    return client.send_get_request(
        bookings_urls.BOOKING_KPIS,
        path_params={"booking_id": booking_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingKpis,
    )


def get_booking_payment_methods(
    client: Any,
    booking_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingPaymentMethods]:
    """The payment methods bound to a booking - ``GET /booking/{booking_id}/payment_methods``;
    ``404`` when none is."""
    return client.send_get_request(
        bookings_urls.BOOKING_PAYMENT_METHODS,
        path_params={"booking_id": booking_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingPaymentMethods,
    )


def get_booking_payment_method(
    client: Any,
    booking_id: str,
    payment_method_ref: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingPaymentMethod]:
    """One bound payment method, by its reference -
    ``GET /booking/{booking_id}/payment_methods/{payment_method_ref}``."""
    return client.send_get_request(
        bookings_urls.BOOKING_PAYMENT_METHOD,
        path_params={"booking_id": booking_id, "payment_method_ref": payment_method_ref},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingPaymentMethod,
    )


def get_booking_payments(
    client: Any,
    booking_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingPaymentList]:
    """List a booking's payments - ``GET /booking/{booking_id}/payments``."""
    return client.send_get_request(
        bookings_urls.BOOKING_PAYMENTS,
        path_params={"booking_id": booking_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingPaymentList,
    )


def get_booking_payment(
    client: Any,
    booking_id: str,
    payment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingPaymentView]:
    """One payment - ``GET /booking/{booking_id}/payments/{payment_id}``; the server does not
    check that the payment belongs to the booking."""
    return client.send_get_request(
        bookings_urls.BOOKING_PAYMENT,
        path_params={"booking_id": booking_id, "payment_id": payment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingPaymentView,
    )


def get_booking_pdf(
    client: Any,
    booking_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingPdf]:
    """A booking's PDF links - ``GET /booking/{booking_id}/pdf``."""
    return client.send_get_request(
        bookings_urls.BOOKING_PDF,
        path_params={"booking_id": booking_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingPdf,
    )


def get_booking_quote_partial_invoices(
    client: Any,
    booking_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[BookingQuotePartialInvoices]:
    """The deposit and instalment invoices of a converted quote -
    ``GET /booking/{booking_id}/quote_partial_invoices``."""
    return client.send_get_request(
        bookings_urls.BOOKING_QUOTE_PARTIAL_INVOICES,
        path_params={"booking_id": booking_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=BookingQuotePartialInvoices,
    )


def get_booking_shipping_pdf(
    client: Any,
    booking_id: str,
    shipping_line_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """A shipping line's PDF - ``GET /booking/{booking_id}/shipping_pdf/{shipping_line_id}``;
    ``404`` until the line has a generated shipping PDF."""
    return client.send_get_request(
        bookings_urls.BOOKING_SHIPPING_PDF,
        path_params={"booking_id": booking_id, "shipping_line_id": shipping_line_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
