"""Typed views over the approval user group bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsApprovalUserGroup",
    "SettingsApprovalUserGroupList",
]


class SettingsApprovalUserGroup(Dto):
    """The settings approval user group body, under ``approval_user_group``."""


    ENVELOPE_KEY = "approval_user_group"

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


class SettingsApprovalUserGroupList(Dto):
    """One page of ``SettingsApprovalUserGroup`` records, under ``data``."""


    data: list[SettingsApprovalUserGroup] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
