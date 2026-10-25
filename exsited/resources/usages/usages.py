"""Usage endpoints, under ``/api/{api_version}/usages``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.usages import usages_urls
from exsited.resources.usages.usages_dto import Usage, UsageList, Usages, UsageUpdated

__all__ = [
    "get_usages",
    "create_usage",
    "get_usage",
    "delete_usage",
    "update_usage",
    "replace_usage",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

UsagePayload = Mapping[str, Any] | str | Dto


def get_usages(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[UsageList]:
    """List of usages - ``GET /usages``."""
    return client.send_get_request(
        usages_urls.USAGES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=UsageList,
    )


def create_usage(
    client: Any,
    payload: UsagePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Usages]:
    """Create bulk usages - ``POST /usages``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        usages_urls.USAGES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Usages,
    )


def get_usage(
    client: Any,
    usage_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Usage]:
    """Get multiple usages -
    ``GET /usages/{usage_id}``."""
    return client.send_get_request(
        usages_urls.USAGE,
        path_params={"usage_id": usage_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Usage,
    )


def delete_usage(
    client: Any,
    usage_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete usage - ``DELETE /usages/{usage_id}``."""
    return client.send_delete_request(
        usages_urls.USAGE,
        path_params={"usage_id": usage_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_usage(
    client: Any,
    usage_id: str,
    payload: UsagePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[UsageUpdated]:
    """Partial update usage - ``PATCH /usages/{usage_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        usages_urls.USAGE,
        path_params={"usage_id": usage_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=UsageUpdated,
    )


def replace_usage(
    client: Any,
    usage_id: str,
    payload: UsagePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[UsageUpdated]:
    """Full replace usage - ``PUT /usages/{usage_id}``."""
    _require_payload(payload)
    return client.send_put_request(
        usages_urls.USAGE,
        path_params={"usage_id": usage_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=UsageUpdated,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
