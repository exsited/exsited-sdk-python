"""Typed views over the additional code bodies."""

from __future__ import annotations

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsAdditionalCode",
    "SettingsAdditionalCodeList",
]


class SettingsAdditionalCode(Dto):
    """The settings additional code body, under ``additional_code``."""


    ENVELOPE_KEY = "additional_code"

    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsAdditionalCodeList(Dto):
    """One page of ``SettingsAdditionalCode`` records, under ``data``."""


    data: list[SettingsAdditionalCode] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
