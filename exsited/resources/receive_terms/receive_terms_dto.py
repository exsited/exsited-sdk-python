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


    ENVELOPE_KEY = "receive_term"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    duration: int | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    period: str | None = None
    status: str | None = None


class SettingsReceiveTermList(Dto):
    """One page of ``SettingsReceiveTerm`` records, under ``data``."""


    data: list[SettingsReceiveTerm] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
