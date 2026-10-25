"""Typed views over the shipping package bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsShippingPackage",
    "SettingsShippingPackageList",
]


class SettingsShippingPackage(Dto):
    """The settings shipping package body, under ``shipping_package``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/shipping_packages",
        "GET /api/{api_version}/settings/shipping_packages/{shipping_package_id}",
        "POST /api/{api_version}/settings/shipping_packages",
        "PATCH /api/{api_version}/settings/shipping_packages/{shipping_package_id}",
    )

    ENVELOPE_KEY = "shipping_package"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    cubic: Any = None
    # Null in every record measured, so untyped.
    cubic_uom: Any = None
    description: str | None = None
    display_name: str | None = None
    height: float | None = None
    # Null in every record measured, so untyped.
    height_uom: Any = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    length: float | None = None
    # Null in every record measured, so untyped.
    length_uom: Any = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    weight: float | None = None
    # Null in every record measured, so untyped.
    weight_uom: Any = None
    width: float | None = None
    # Null in every record measured, so untyped.
    width_uom: Any = None


class SettingsShippingPackageList(Dto):
    """One page of ``SettingsShippingPackage`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/shipping_packages",)

    data: list[SettingsShippingPackage] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
