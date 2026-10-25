"""Typed views over the approval bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "ApprovalsAccount",
    "ApprovalsAccountList",
    "ApprovalsSaleorder",
]


class ApprovalsAccount(Dto):
    """The approvals account body."""

    MEASURED_FROM = ("GET /api/{api_version}/approvals/account",)

    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    entity: str | None = None
    event: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class ApprovalsAccountList(Dto):
    """One page of ``ApprovalsAccount`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/approvals/account",)

    data: list[ApprovalsAccount] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ApprovalsSaleorder(Dto):
    """The approvals saleorder body."""

    MEASURED_FROM = ("GET /api/{api_version}/approvals/saleOrder",)

    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
