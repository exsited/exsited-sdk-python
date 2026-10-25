"""Custom attribute endpoints, under ``/api/{api_version}/custom_attributes``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.custom_attributes import custom_attributes_urls
from exsited.resources.custom_attributes.custom_attributes_dto import (
    CustomAttribute,
    CustomAttributeList,
    CustomAttributes,
)

__all__ = [
    "get_custom_attributes",
    "create_custom_attribute",
    "delete_custom_attribute",
    "get_custom_attribute",
    "update_custom_attribute",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

CustomAttributePayload = Mapping[str, Any] | str | Dto


def get_custom_attributes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomAttributeList]:
    """List all custom attributes - ``GET /custom_attributes``."""
    return client.send_get_request(
        custom_attributes_urls.CUSTOM_ATTRIBUTES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomAttributeList,
    )


def create_custom_attribute(
    client: Any,
    payload: CustomAttributePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomAttributes]:
    """Create custom attribute - ``POST /custom_attributes``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        custom_attributes_urls.CUSTOM_ATTRIBUTES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomAttributes,
    )


def delete_custom_attribute(
    client: Any,
    custom_attribute_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete custom attribute - ``DELETE /custom_attributes/{custom_attribute_id}``; answered
    ``204``."""
    return client.send_delete_request(
        custom_attributes_urls.CUSTOM_ATTRIBUTE,
        path_params={"custom_attribute_id": custom_attribute_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_custom_attribute(
    client: Any,
    custom_attribute_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomAttribute]:
    """Get custom attribute details - ``GET /custom_attributes/{custom_attribute_id}``."""
    return client.send_get_request(
        custom_attributes_urls.CUSTOM_ATTRIBUTE,
        path_params={"custom_attribute_id": custom_attribute_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomAttribute,
    )


def update_custom_attribute(
    client: Any,
    custom_attribute_id: str,
    payload: CustomAttributePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomAttribute]:
    """Update custom attribute - ``PATCH /custom_attributes/{custom_attribute_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_attributes_urls.CUSTOM_ATTRIBUTE,
        path_params={"custom_attribute_id": custom_attribute_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomAttribute,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
