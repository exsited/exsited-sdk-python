"""Typed views over the salutation bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsSalutation",
    "SettingsSalutationList",
]


class SettingsSalutation(Dto):
    """The settings salutation body, under ``salutation``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/salutations",
        "GET /api/{api_version}/settings/salutations/{salutation_id}",
        "POST /api/{api_version}/settings/salutations",
        "PATCH /api/{api_version}/settings/salutations/{salutation_id}",
    )

    ENVELOPE_KEY = "salutation"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsSalutationList(Dto):
    """One page of ``SettingsSalutation`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/salutations",)

    data: list[SettingsSalutation] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
