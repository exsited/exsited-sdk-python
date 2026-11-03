"""Typed views over the unit of measurement bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsUom",
    "SettingsUomList",
]


class SettingsUom(Dto):
    """The settings unit of measurement body, under ``uom``."""


    ENVELOPE_KEY = "uom"

    created_by: Any = None
    created_on: str | None = None
    custom_type: Any = None
    decimal_places: int | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    rounding: str | None = None
    status: str | None = None
    type: str | None = None
    type_display_text: str | None = None


class SettingsUomList(Dto):
    """One page of ``SettingsUom`` records, under ``data``."""


    data: list[SettingsUom] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
