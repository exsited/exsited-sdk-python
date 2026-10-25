"""Shipping package endpoints, under ``/api/{api_version}/settings/shipping_packages``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.shipping_packages import shipping_packages_urls
from exsited.resources.shipping_packages.shipping_packages_dto import (
    SettingsShippingPackage,
    SettingsShippingPackageList,
)

__all__ = [
    "get_settings_shipping_packages",
    "create_settings_shipping_package",
    "get_settings_shipping_package",
    "delete_settings_shipping_package",
    "update_settings_shipping_package",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ShippingPackagePayload = Mapping[str, Any] | str | Dto


def get_settings_shipping_packages(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingPackageList]:
    """List shipping packages - ``GET /settings/shipping_packages``."""
    return client.send_get_request(
        shipping_packages_urls.SETTINGS_SHIPPING_PACKAGES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingPackageList,
    )


def create_settings_shipping_package(
    client: Any,
    payload: ShippingPackagePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingPackage]:
    """Create a shipping package - ``POST /settings/shipping_packages``; a ``*_uom`` is the
    unit's bare uuid, not its prefixed id."""
    _require_payload(payload)
    return client.send_post_request(
        shipping_packages_urls.SETTINGS_SHIPPING_PACKAGES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingPackage,
    )


def get_settings_shipping_package(
    client: Any,
    shipping_package_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingPackage]:
    """Get one shipping package - ``GET /settings/shipping_packages/{shipping_package_id}``."""
    return client.send_get_request(
        shipping_packages_urls.SETTINGS_SHIPPING_PACKAGE,
        path_params={"shipping_package_id": shipping_package_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingPackage,
    )


def delete_settings_shipping_package(
    client: Any,
    shipping_package_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a shipping package - ``DELETE /settings/shipping_packages/{shipping_package_id}``."""
    return client.send_delete_request(
        shipping_packages_urls.SETTINGS_SHIPPING_PACKAGE,
        path_params={"shipping_package_id": shipping_package_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_shipping_package(
    client: Any,
    shipping_package_id: str,
    payload: ShippingPackagePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingPackage]:
    """Update a shipping package - ``PATCH /settings/shipping_packages/{shipping_package_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        shipping_packages_urls.SETTINGS_SHIPPING_PACKAGE,
        path_params={"shipping_package_id": shipping_package_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingPackage,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
