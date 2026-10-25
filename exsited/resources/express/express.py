"""Express endpoints, under ``/api/{api_version}/express``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.express import express_urls
from exsited.resources.express.express_dto import Express

__all__ = [
    "create_express",
]

ExpressPayload = Mapping[str, Any] | str | Dto


def create_express(
    client: Any,
    payload: ExpressPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Express]:
    """CUSTOMER_AND_SUPPLIER account type - ``POST /express``."""
    _require_payload(payload)
    return client.send_post_request(
        express_urls.EXPRESS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Express,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
