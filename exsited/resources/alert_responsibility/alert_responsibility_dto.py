"""Typed views over the alert responsibility bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "AlertResponsibility",
    "AlertResponsibilityList",
]


class AlertResponsibility(Dto):
    """The alert responsibility body, under ``alert_responsibility``; ``activity_logs`` comes on
    the create answer only."""


    ENVELOPE_KEY = "alert_responsibility"

    activity_logs: list[Any] | None = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class AlertResponsibilityList(Dto):
    """One page of ``AlertResponsibility`` records, under ``data``."""


    data: list[AlertResponsibility] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
