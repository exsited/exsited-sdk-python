"""Portal endpoints, under ``/api/{api_version}/portal``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.portals import portals_urls
from exsited.resources.portals.portals_dto import PortalChangePassword, PortalLogin, PortalResetLink

__all__ = [
    "activate_portal",
    "create_portal_change_password",
    "create_portal_login",
    "create_portal_reset",
    "create_portal_reset_link",
    "create_portal_validate",
    "set_portal_password",
]

PortalPayload = Mapping[str, Any] | str | Dto


def activate_portal(
    client: Any,
    payload: PortalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Activate portal account - ``POST /portal/activate``."""
    _require_payload(payload)
    return client.send_post_request(
        portals_urls.PORTAL_ACTIVATE,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_portal_change_password(
    client: Any,
    payload: PortalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PortalChangePassword]:
    """Change password - ``POST /portal/change_password``."""
    _require_payload(payload)
    return client.send_post_request(
        portals_urls.PORTAL_CHANGE_PASSWORD,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PortalChangePassword,
    )


def create_portal_login(
    client: Any,
    payload: PortalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PortalLogin]:
    """Portal login - ``POST /portal/login``."""
    _require_payload(payload)
    return client.send_post_request(
        portals_urls.PORTAL_LOGIN,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PortalLogin,
    )


def create_portal_reset(
    client: Any,
    payload: PortalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Reset password - ``POST /portal/reset``."""
    _require_payload(payload)
    return client.send_post_request(
        portals_urls.PORTAL_RESET,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_portal_reset_link(
    client: Any,
    payload: PortalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PortalResetLink]:
    """Request reset link - ``POST /portal/reset_link``."""
    _require_payload(payload)
    return client.send_post_request(
        portals_urls.PORTAL_RESET_LINK,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PortalResetLink,
    )


def create_portal_validate(
    client: Any,
    payload: PortalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Validate account - ``POST /portal/validate``."""
    _require_payload(payload)
    return client.send_post_request(
        portals_urls.PORTAL_VALIDATE,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def set_portal_password(
    client: Any,
    payload: PortalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Set a portal password by email - ``POST /portal/change``, ``{"portal": {"email",
    "password"}}``; no current password is asked, and it answers ``202``."""
    _require_payload(payload)
    return client.send_post_request(
        portals_urls.PORTAL_CHANGE,
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
