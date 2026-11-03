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


    ENVELOPE_KEY = "shipping_package"

    created_by: Any = None
    created_on: str | None = None
    cubic: Any = None
    cubic_uom: Any = None
    description: str | None = None
    display_name: str | None = None
    height: float | None = None
    height_uom: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    length: float | None = None
    length_uom: Any = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    weight: float | None = None
    weight_uom: Any = None
    width: float | None = None
    width_uom: Any = None


class SettingsShippingPackageList(Dto):
    """One page of ``SettingsShippingPackage`` records, under ``data``."""


    data: list[SettingsShippingPackage] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
