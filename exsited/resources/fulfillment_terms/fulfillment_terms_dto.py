"""Typed views over the fulfillment term bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsFulfillmentTerm",
    "SettingsFulfillmentTermList",
]


class SettingsFulfillmentTerm(Dto):
    """The settings fulfillment term body, under ``fulfillment_term``."""


    ENVELOPE_KEY = "fulfillment_term"

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


class SettingsFulfillmentTermList(Dto):
    """One page of ``SettingsFulfillmentTerm`` records, under ``data``."""


    data: list[SettingsFulfillmentTerm] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
