"""Typed views over the custom field bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsCustomField",
    "SettingsCustomFieldList",
]


class SettingsCustomField(Dto):
    """The settings custom field body, under ``custom_field``."""


    ENVELOPE_KEY = "custom_field"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    is_mandatory: bool | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    type: str | None = None
    version: int | None = None


class SettingsCustomFieldList(Dto):
    """One page of ``SettingsCustomField`` records, under ``data``."""


    data: list[SettingsCustomField] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
