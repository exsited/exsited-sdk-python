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

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/approval_user_groups",
        "GET /api/{api_version}/settings/approval_user_groups/{approval_user_group_id}",
        "POST /api/{api_version}/settings/approval_user_groups",
        "PATCH /api/{api_version}/settings/approval_user_groups/{approval_user_group_id}",
    )

    ENVELOPE_KEY = "approval_user_group"

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


class SettingsApprovalUserGroupList(Dto):
    """One page of ``SettingsApprovalUserGroup`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/approval_user_groups",)

    data: list[SettingsApprovalUserGroup] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
