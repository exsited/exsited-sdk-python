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

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/shipping_rules",
        "GET /api/{api_version}/settings/shipping_rules/{shipping_rule_id}",
        "POST /api/{api_version}/settings/shipping_rules",
        "PATCH /api/{api_version}/settings/shipping_rules/{shipping_rule_id}",
    )

    ENVELOPE_KEY = "shipping_rule"

    configuration: SettingsShippingRuleConfiguration | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    shipping_class: Any = None
    status: str | None = None
    version: int | None = None


class SettingsShippingRuleList(Dto):
    """One page of ``SettingsShippingRule`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/shipping_rules",)

    data: list[SettingsShippingRule] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsShippingRuleConfiguration(Dto):
    """A :class:`SettingsShippingRule`'s ``configuration``."""

    # Null in every record measured, so untyped.
    rate: Any = None
    # Empty in every record measured, so untyped.
    zones: list[Any] | None = None
