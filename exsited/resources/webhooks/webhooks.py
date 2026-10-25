"""Webhook endpoints, under ``/api/{api_version}/webhooks``."""

from __future__ import annotations

from typing import Any

from exsited.client.api_response import ApiResponse
from exsited.resources.webhooks import webhooks_urls

__all__ = [
    "get_webhook",
]


def get_webhook(
    client: Any,
    webhook_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One webhook delivery - ``GET /webhooks/{webhook_id}``, the ``whk_`` id a delivery carries;
    no route lists them, so ``.dto`` is None and the body is read through ``.map``."""
    return client.send_get_request(
        webhooks_urls.WEBHOOK,
        path_params={"webhook_id": webhook_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )
