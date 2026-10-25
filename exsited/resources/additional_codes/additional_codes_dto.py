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

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/additional_codes",
        "GET /api/{api_version}/settings/additional_codes/{additional_code_id}",
        "POST /api/{api_version}/settings/additional_codes",
    )

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

    MEASURED_FROM = ("GET /api/{api_version}/settings/additional_codes",)

    data: list[SettingsAdditionalCode] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
