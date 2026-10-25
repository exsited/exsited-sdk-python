"""Typed views over the receive term bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsReceiveTerm",
    "SettingsReceiveTermList",
]


class SettingsReceiveTerm(Dto):
    """The settings receive term body, under ``receive_term``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/receive_terms",
        "GET /api/{api_version}/settings/receive_terms/{receive_term_id}",
        "POST /api/{api_version}/settings/receive_terms",
        "PATCH /api/{api_version}/settings/receive_terms/{receive_term_id}",
    )

    ENVELOPE_KEY = "receive_term"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    duration: int | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    period: str | None = None
    status: str | None = None


class SettingsReceiveTermList(Dto):
    """One page of ``SettingsReceiveTerm`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/receive_terms",)

    data: list[SettingsReceiveTerm] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
