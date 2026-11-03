"""Typed views over the role bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsRole",
    "SettingsRoleList",
]


class SettingsRole(Dto):
    """The settings role body, under ``role``."""


    ENVELOPE_KEY = "role"

    created_by: Any = None
    created_on: str | None = None
    description: Any = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    is_system_role: bool | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsRoleList(Dto):
    """One page of ``SettingsRole`` records, under ``data``."""


    data: list[SettingsRole] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
