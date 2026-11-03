"""Typed views over the communication profile bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsCommunicationProfile",
    "SettingsCommunicationProfileList",
]


class SettingsCommunicationProfile(Dto):
    """The settings communication profile body, under ``communication_profile``."""


    ENVELOPE_KEY = "communication_profile"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsCommunicationProfileList(Dto):
    """One page of ``SettingsCommunicationProfile`` records, under ``data``."""


    data: list[SettingsCommunicationProfile] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
