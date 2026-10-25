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

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/departments",
        "GET /api/{api_version}/settings/departments/{department_id}",
    )

    ENVELOPE_KEY = "department"

    code: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    division: SettingsDepartmentDivision | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsDepartmentList(Dto):
    """One page of ``SettingsDepartment`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/departments",)

    data: list[SettingsDepartment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsDepartmentDivision(Dto):
    """A :class:`SettingsDepartment`'s ``division``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None
