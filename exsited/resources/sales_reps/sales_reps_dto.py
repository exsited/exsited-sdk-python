"""Typed views over the sales rep bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsSalesRep",
    "SettingsSalesRepList",
]


class SettingsSalesRep(Dto):
    """The settings sales rep body, under ``sales_rep``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/sales_reps",
        "GET /api/{api_version}/settings/sales_reps/{sales_rep_id}",
    )

    ENVELOPE_KEY = "sales_rep"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    email_address: str | None = None
    first_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_name: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsSalesRepList(Dto):
    """One page of ``SettingsSalesRep`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/sales_reps",)

    data: list[SettingsSalesRep] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
