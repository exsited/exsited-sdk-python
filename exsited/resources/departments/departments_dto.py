"""Typed views over the department bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsDepartment",
    "SettingsDepartmentList",
    "SettingsDepartmentDivision",
]


class SettingsDepartment(Dto):
    """The settings department body, under ``department``."""


    ENVELOPE_KEY = "department"

    code: str | None = None
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    division: SettingsDepartmentDivision | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsDepartmentList(Dto):
    """One page of ``SettingsDepartment`` records, under ``data``."""


    data: list[SettingsDepartment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsDepartmentDivision(Dto):
    """A :class:`SettingsDepartment`'s ``division``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None
