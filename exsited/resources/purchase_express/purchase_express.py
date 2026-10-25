"""Purchase express endpoints, under ``/api/{api_version}/purchase_express``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.purchase_express import purchase_express_urls
from exsited.resources.purchase_express.purchase_express_dto import PurchaseExpress

__all__ = [
    "create_purchase_express",
]

PurchaseExpressPayload = Mapping[str, Any] | str | Dto


def create_purchase_express(
    client: Any,
    payload: PurchaseExpressPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseExpress]:
    """Create a purchase order, and its purchase invoice and payment if the body nests them, in
    one call - ``POST /purchase_express``, body ``account.purchase_order``; ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        purchase_express_urls.PURCHASE_EXPRESS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseExpress,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
