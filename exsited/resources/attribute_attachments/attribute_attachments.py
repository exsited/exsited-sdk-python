"""Attribute attachment endpoints, under ``/api/{api_version}/attribute_attachment``."""

from __future__ import annotations

from typing import Any

from exsited.client.api_response import ApiResponse
from exsited.resources.attribute_attachments import attribute_attachments_urls

__all__ = [
    "get_attribute_attachment",
]


def get_attribute_attachment(
    client: Any,
    file_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """A custom attribute's file as base64 - ``GET /attribute_attachment/{file_uuid}``, the uuid
    an account's file attribute links to; answered as ``{"base64": ...}`` with no envelope."""
    return client.send_get_request(
        attribute_attachments_urls.ATTRIBUTE_ATTACHMENT,
        path_params={"file_uuid": file_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )
