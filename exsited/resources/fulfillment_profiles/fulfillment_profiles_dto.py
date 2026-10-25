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

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/fulfillment_profiles",
        "GET /api/{api_version}/settings/fulfillment_profiles/{fulfillment_profile_id}",
        "POST /api/{api_version}/settings/fulfillment_profiles",
        "PATCH /api/{api_version}/settings/fulfillment_profiles/{fulfillment_profile_id}",
    )

    ENVELOPE_KEY = "fulfillment_profile"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsFulfillmentProfileList(Dto):
    """One page of ``SettingsFulfillmentProfile`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/fulfillment_profiles",)

    data: list[SettingsFulfillmentProfile] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
