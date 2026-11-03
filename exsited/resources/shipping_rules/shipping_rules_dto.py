"""Typed views over the shipping rule bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsShippingRule",
    "SettingsShippingRuleList",
    "SettingsShippingRuleConfiguration",
]


class SettingsShippingRule(Dto):
    """The settings shipping rule body, under ``shipping_rule``."""


    ENVELOPE_KEY = "shipping_rule"

    configuration: SettingsShippingRuleConfiguration | None = None
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    shipping_class: Any = None
    status: str | None = None
    version: int | None = None


class SettingsShippingRuleList(Dto):
    """One page of ``SettingsShippingRule`` records, under ``data``."""


    data: list[SettingsShippingRule] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsShippingRuleConfiguration(Dto):
    """A :class:`SettingsShippingRule`'s ``configuration``."""

    rate: Any = None
    zones: list[Any] | None = None
