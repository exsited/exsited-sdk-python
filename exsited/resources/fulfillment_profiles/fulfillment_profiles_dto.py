"""Typed views over the fulfillment profile bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsFulfillmentProfile",
    "SettingsFulfillmentProfileList",
]


class SettingsFulfillmentProfile(Dto):
    """The settings fulfillment profile body, under ``fulfillment_profile``."""


    ENVELOPE_KEY = "fulfillment_profile"

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
    version: int | None = None


class SettingsFulfillmentProfileList(Dto):
    """One page of ``SettingsFulfillmentProfile`` records, under ``data``."""


    data: list[SettingsFulfillmentProfile] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
