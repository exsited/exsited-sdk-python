"""Typed views over the account group bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsAccountGroup",
    "SettingsAccountGroupList",
    "SettingsAccountGroupStateRule",
]


class SettingsAccountGroup(Dto):
    """The settings account group body, under ``account_group``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/account_groups",
        "GET /api/{api_version}/settings/account_groups/{account_group_id}",
        "POST /api/{api_version}/settings/account_groups",
    )

    ENVELOPE_KEY = "account_group"

    # Null in every record measured, so untyped.
    accounting_code: Any = None
    # Present but empty on every record measured, so the element type is unknown.
    custom_attributes: list[Any] | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    invoice_account_media: list[str] | None = None
    # Null in every record measured, so untyped.
    managed_by: Any = None
    name: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    pricing_level: Any = None
    state_rule: SettingsAccountGroupStateRule | None = None
    status: str | None = None


class SettingsAccountGroupList(Dto):
    """One page of ``SettingsAccountGroup`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/account_groups",)

    data: list[SettingsAccountGroup] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsAccountGroupStateRule(Dto):
    """A :class:`SettingsAccountGroup`'s ``state_rule``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None
