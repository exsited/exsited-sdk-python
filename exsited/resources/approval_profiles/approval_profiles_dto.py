"""Typed views over the approval profile bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsApprovalProfile",
    "SettingsApprovalProfileList",
]


class SettingsApprovalProfile(Dto):
    """The settings approval profile body, under ``approval_profile``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/approval_profiles",
        "GET /api/{api_version}/settings/approval_profiles/{approval_profile_id}",
    )

    ENVELOPE_KEY = "approval_profile"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsApprovalProfileList(Dto):
    """One page of ``SettingsApprovalProfile`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/approval_profiles",)

    data: list[SettingsApprovalProfile] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
