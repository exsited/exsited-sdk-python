"""Typed views over the usage bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Usage",
    "UsageList",
    "Usages",
    "UsageUpdated",
    "UsageChargeItem",
    "UsageCustomAttribute",
    "UsageCreatedBy",
    "UsageLastUpdatedBy",
    "UsagesDetail",
    "UsageUpdatedDetail",
    "UsagesDetailSuccess",
    "UsagesDetailFailed",
]


class Usage(Dto):
    """The usage body, under ``usage``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/usages",
        "GET /api/{api_version}/usages/{usage_id}",
    )

    ENVELOPE_KEY = "usage"

    charge_item: UsageChargeItem | None = None
    charging_end_date: str | None = None
    charging_period: str | None = None
    charging_start_date: str | None = None
    created_by: UsageCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: list[UsageCustomAttribute] | None = None
    end_time: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: UsageLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    quantity: float | None = None
    # Null in every record measured, so untyped.
    source: Any = None
    start_time: str | None = None
    status: str | None = None
    type: str | None = None
    # Null in every record measured, so untyped.
    uom: Any = None
    version: int | None = None


class UsageList(Dto):
    """One page of ``Usage`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/usages",)

    data: list[Usage] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class Usages(Dto):
    """The usages body, under ``usage``."""

    MEASURED_FROM = ("POST /api/{api_version}/usages",)

    ENVELOPE_KEY = "usage"

    activity_logs: list[Any] | None = None
    charge_item_name: str | None = None
    charge_item_uuid: str | None = None
    charge_status: str | None = None
    charging_period: str | None = None
    created_by: str | None = None
    created_on: str | None = None
    custom_attributes: list[Any] | None = None
    end_time: str | None = None
    event_id: str | None = None
    failed: list[Any] | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    object: str | None = None
    quantity: str | None = None
    source: str | None = None
    start_time: str | None = None
    success: list[Any] | None = None
    type: str | None = None
    uom: str | None = None
    usages: UsagesDetail | None = None
    uuid: str | None = None
    version: str | None = None


class UsageUpdated(Dto):
    """The usage updated body."""

    MEASURED_FROM = (
        "PATCH /api/{api_version}/usages/{usage_id}",
        "PUT /api/{api_version}/usages/{usage_id}",
    )

    note: str | None = None
    status: str | None = None
    usage: UsageUpdatedDetail | None = None


class UsageChargeItem(Dto):
    """A :class:`Usage`'s ``charge_item``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None


class UsageCustomAttribute(Dto):
    """One entry of a :class:`Usage`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class UsageCreatedBy(Dto):
    """A :class:`Usage`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class UsageLastUpdatedBy(Dto):
    """A :class:`Usage`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class UsagesDetail(Dto):
    """A :class:`Usages`'s ``usages``."""

    activity_logs: list[Any] | None = None
    failed: list[UsagesDetailFailed] | None = None
    success: list[UsagesDetailSuccess] | None = None


class UsageUpdatedDetail(Dto):
    """A :class:`UsageUpdated`'s ``usage``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class UsagesDetailSuccess(Dto):
    """One entry of a :class:`UsagesDetail`'s ``success``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class UsagesDetailFailed(Dto):
    """One entry of a :class:`UsagesDetail`'s ``failed``."""

    charge_item_id: str | None = None
    charging_period: str | None = None
    error: dict[str, Any] | None = None
