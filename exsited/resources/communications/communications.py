"""Communication endpoints, under ``/api/{api_version}/communications``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.communications import communications_urls

__all__ = [
    "send_email",
]

CommunicationPayload = Mapping[str, Any] | str | Dto


def send_email(
    client: Any,
    payload: CommunicationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Email a document - ``POST /communications/send_email``; the body names one of
    ``invoice``, ``purchase_invoice``, ``account_statement`` or ``payment``, each an ``id``
    beside ``to``, ``cc``, ``bcc``, ``subject``, ``body`` and ``template``. Sends real mail."""
    _require_payload(payload)
    return client.send_post_request(
        communications_urls.COMMUNICATIONS_SEND_EMAIL,
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
