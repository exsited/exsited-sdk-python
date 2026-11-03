"""Typed views over the team bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsTeam",
    "SettingsTeamList",
]


class SettingsTeam(Dto):
    """The settings team body, under ``team``."""


    ENVELOPE_KEY = "team"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    managed_by: Any = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: Any = None


class SettingsTeamList(Dto):
    """One page of ``SettingsTeam`` records, under ``data``."""


    data: list[SettingsTeam] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
