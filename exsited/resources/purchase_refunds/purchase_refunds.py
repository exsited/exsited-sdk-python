"""Purchase refund endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.purchase_refunds import purchase_refunds_urls
from exsited.resources.purchase_refunds.purchase_refunds_dto import (
    PurchaseRefund,
    PurchaseRefunds,
)

__all__ = [
    "get_purchase_refunds",
    "get_purchase_refund",
    "create_purchase_credit_note_purchase_refund",
    "update_purchase_refund",
    "delete_purchase_refund",
]

PurchaseRefundPayload = Mapping[str, Any] | str | Dto


def get_purchase_refunds(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseRefunds]:
    """List purchase refunds - ``GET /purchase_refunds``."""
    return client.send_get_request(
        purchase_refunds_urls.PURCHASE_REFUNDS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseRefunds,
    )


def get_purchase_refund(
    client: Any,
    purchase_refund_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseRefund]:
    """Get single - ``GET /purchase_refunds/{purchase_refund_id}``."""
    return client.send_get_request(
        purchase_refunds_urls.PURCHASE_REFUND,
        path_params={"purchase_refund_id": purchase_refund_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseRefund,
    )


def create_purchase_credit_note_purchase_refund(
    client: Any,
    purchase_credit_note_id: str,
    payload: PurchaseRefundPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseRefund]:
    """Refund from a purchase credit note -
    ``POST /purchase_credit_notes/{purchase_credit_note_id}/purchase_refunds``; ``201``, as
    ``get_purchase_refund`` reads it. ``payment_method`` is the supplier's method reference."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_refunds_urls.PURCHASE_CREDIT_NOTE_PURCHASE_REFUNDS,
        path_params={"purchase_credit_note_id": purchase_credit_note_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseRefund,
    )


def update_purchase_refund(
    client: Any,
    purchase_refund_id: str,
    payload: PurchaseRefundPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseRefund]:
    """Edit a refund's reference, note, date or attributes - ``PATCH /purchase_refunds/{purchase_refund_id}``,
    wrapped in ``purchase_refund``; the amount cannot change."""
    _require_payload(payload)
    return client.send_patch_request(
        purchase_refunds_urls.PURCHASE_REFUND,
        path_params={"purchase_refund_id": purchase_refund_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseRefund,
    )


def delete_purchase_refund(
    client: Any,
    purchase_refund_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a refund - ``DELETE /purchase_refunds/{purchase_refund_id}``, by its code;
    ``204``."""
    return client.send_delete_request(
        purchase_refunds_urls.PURCHASE_REFUND,
        path_params={"purchase_refund_id": purchase_refund_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
