"""Alert responsibility endpoints, under ``/api/{api_version}/alert_responsibility``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.alert_responsibility import alert_responsibility_urls
from exsited.resources.alert_responsibility.alert_responsibility_dto import (
    AlertResponsibility,
    AlertResponsibilityList,
)

__all__ = [
    "get_alert_responsibilities",
    "get_alert_responsibility",
    "create_alert_responsibility",
    "update_alert_responsibility",
    "delete_alert_responsibility",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

AlertResponsibilityPayload = Mapping[str, Any] | str | Dto


def get_alert_responsibilities(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AlertResponsibilityList]:
    """List alert responsibilities - ``GET /alert_responsibility``, the singular path the
    workflow services serve."""
    return client.send_get_request(
        alert_responsibility_urls.ALERT_RESPONSIBILITIES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AlertResponsibilityList,
    )


def get_alert_responsibility(
    client: Any,
    alert_responsibility_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AlertResponsibility]:
    """One alert responsibility - ``GET /alert_responsibility/{alert_responsibility_id}``; the
    ``ar_`` id or the raw uuid."""
    return client.send_get_request(
        alert_responsibility_urls.ALERT_RESPONSIBILITY,
        path_params={"alert_responsibility_id": alert_responsibility_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AlertResponsibility,
    )


def create_alert_responsibility(
    client: Any,
    payload: AlertResponsibilityPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AlertResponsibility]:
    """Create an alert responsibility - ``POST /alert_responsibility``, under
    ``alert_responsibility``; ``name`` is required and unique, beside ``display_name`` and
    ``description`` only."""
    _require_payload(payload)
    return client.send_post_request(
        alert_responsibility_urls.ALERT_RESPONSIBILITIES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AlertResponsibility,
    )


def update_alert_responsibility(
    client: Any,
    alert_responsibility_id: str,
    payload: AlertResponsibilityPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AlertResponsibility]:
    """Update an alert responsibility - ``PATCH /alert_responsibility/{alert_responsibility_id}``;
    ``status`` may move between ``active`` and ``inactive`` beside the three create keys."""
    _require_payload(payload)
    return client.send_patch_request(
        alert_responsibility_urls.ALERT_RESPONSIBILITY,
        path_params={"alert_responsibility_id": alert_responsibility_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AlertResponsibility,
    )


def delete_alert_responsibility(
    client: Any,
    alert_responsibility_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an alert responsibility - ``DELETE /alert_responsibility/{alert_responsibility_id}``,
    a soft delete; the id must be the ``ar_`` one."""
    return client.send_delete_request(
        alert_responsibility_urls.ALERT_RESPONSIBILITY,
        path_params={"alert_responsibility_id": alert_responsibility_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
