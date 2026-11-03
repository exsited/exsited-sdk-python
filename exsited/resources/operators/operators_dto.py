"""Typed views over the operator bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsOperator",
    "SettingsOperatorList",
]


class SettingsOperator(Dto):
    """The operator body, under ``operator``. ``description``, ``created_by`` and
    ``last_updated_by`` are untyped."""


    ENVELOPE_KEY = "operator"

    created_by: Any = None
    created_on: str | None = None
    description: Any = None
    display_name: str | None = None
    email: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsOperatorList(Dto):
    """One page of ``SettingsOperator`` records, under ``data``."""


    data: list[SettingsOperator] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
