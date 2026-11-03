"""Typed views over the application bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsApplication",
    "SettingsApplicationList",
]


class SettingsApplication(Dto):
    """The settings application body, under ``application``."""


    ENVELOPE_KEY = "application"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsApplicationList(Dto):
    """One page of ``SettingsApplication`` records, under ``data``."""


    data: list[SettingsApplication] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
