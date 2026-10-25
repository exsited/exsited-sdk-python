"""Pro-forma invoice endpoints, under ``/api/{api_version}/proforma_invoices``. The server lists
only the pro-forma invoices whose invoice status is active."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.proforma_invoices import proforma_invoices_urls

__all__ = [
    "get_proforma_invoices",
    "get_proforma_invoice",
    "delete_proforma_invoice",
    "create_proforma_invoice_payment",
]

ProformaInvoicePayload = Mapping[str, Any] | str | Dto


def get_proforma_invoices(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List pro-forma invoices - ``GET /proforma_invoices``; paged by cursor, under ``data``."""
    return client.send_get_request(
        proforma_invoices_urls.PROFORMA_INVOICES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_proforma_invoice(
    client: Any,
    proforma_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Retrieve one pro-forma invoice - ``GET /proforma_invoices/{proforma_id}``, by its code;
    under ``proforma_invoice``."""
    return client.send_get_request(
        proforma_invoices_urls.PROFORMA_INVOICE,
        path_params={"proforma_id": proforma_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_proforma_invoice(
    client: Any,
    proforma_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a pro-forma invoice - ``DELETE /proforma_invoices/{proforma_id}``; ``204``. A paid
    one is refused ``400`` ``already_paid``."""
    return client.send_delete_request(
        proforma_invoices_urls.PROFORMA_INVOICE,
        path_params={"proforma_id": proforma_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_proforma_invoice_payment(
    client: Any,
    proforma_id: str,
    payload: ProformaInvoicePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Pay a pro-forma invoice - ``POST /proforma_invoices/{proforma_id}/payments``, wrapped in
    ``payment``; ``201``, answering the new payment's code as ``payment.payment_id``."""
    _require_payload(payload)
    return client.send_post_request(
        proforma_invoices_urls.PROFORMA_INVOICE_PAYMENTS,
        path_params={"proforma_id": proforma_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
