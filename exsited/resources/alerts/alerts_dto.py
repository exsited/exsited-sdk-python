"""Typed views over the alert bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Alerts",
]


class Alerts(Dto):
    """The alerts body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/alerts",
        "GET /api/{api_version}/alerts/account/{account_id}",
        "GET /api/{api_version}/alerts/employee/{employee_id}",
        "GET /api/{api_version}/alerts/labour/{labour_id}",
    )

    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
