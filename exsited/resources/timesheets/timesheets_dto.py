"""Typed views over the timesheet bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Timesheet",
    "TimesheetList",
    "Timesheets",
    "TimesheetUpdated",
    "TimesheetsLabour",
    "TimesheetsSaleOrderItem",
    "TimesheetsSaleOrder",
    "TimesheetsCreatedBy",
    "TimesheetsActivityLog",
    "TimesheetUpdatedLabour",
    "TimesheetUpdatedSaleOrderItem",
    "TimesheetUpdatedSaleOrder",
    "TimesheetUpdatedCreatedBy",
    "TimesheetUpdatedLastUpdatedBy",
    "TimesheetLabour",
    "TimesheetSaleOrderItem",
    "TimesheetSaleOrder",
    "TimesheetCreatedBy",
    "TimesheetLastUpdatedBy",
]


class Timesheet(Dto):
    """The timesheet body."""

    MEASURED_FROM = ("GET /api/{api_version}/timesheets",)

    created_by: TimesheetCreatedBy | None = None
    created_on: str | None = None
    end_time: str | None = None
    href: str | None = None
    id: str | None = None
    labour: TimesheetLabour | None = None
    last_updated_by: TimesheetLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    sale_order: TimesheetSaleOrder | None = None
    sale_order_item: TimesheetSaleOrderItem | None = None
    start_time: str | None = None
    status: str | None = None
    version: int | None = None


class TimesheetList(Dto):
    """One page of ``Timesheet`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/timesheets",)

    data: list[Timesheet] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class Timesheets(Dto):
    """What ``create_timesheet`` and ``get_timesheet`` answer, under ``timesheet``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/timesheets",
        "GET /api/{api_version}/timesheets/{timesheet_id}",
    )

    ENVELOPE_KEY = "timesheet"

    activity_logs: list[TimesheetsActivityLog] | None = None
    created_by: TimesheetsCreatedBy | None = None
    created_on: str | None = None
    end_time: str | None = None
    href: str | None = None
    id: str | None = None
    labour: TimesheetsLabour | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    sale_order: TimesheetsSaleOrder | None = None
    sale_order_item: TimesheetsSaleOrderItem | None = None
    start_time: str | None = None
    status: str | None = None
    version: int | None = None


class TimesheetUpdated(Dto):
    """What ``update_timesheet`` answers, under ``timesheet``."""

    MEASURED_FROM = ("PATCH /api/{api_version}/timesheets/{timesheet_id}",)

    ENVELOPE_KEY = "timesheet"

    activity_logs: list[Any] | None = None
    created_by: TimesheetUpdatedCreatedBy | None = None
    created_on: str | None = None
    end_time: str | None = None
    href: str | None = None
    id: str | None = None
    labour: TimesheetUpdatedLabour | None = None
    last_updated_by: TimesheetUpdatedLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    sale_order: TimesheetUpdatedSaleOrder | None = None
    sale_order_item: TimesheetUpdatedSaleOrderItem | None = None
    start_time: str | None = None
    status: str | None = None
    version: int | None = None


class TimesheetsLabour(Dto):
    """A :class:`Timesheets`'s ``labour``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetsSaleOrderItem(Dto):
    """A :class:`Timesheets`'s ``sale_order_item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetsSaleOrder(Dto):
    """A :class:`Timesheets`'s ``sale_order``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetsCreatedBy(Dto):
    """A :class:`Timesheets`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class TimesheetsActivityLog(Dto):
    """One entry of a :class:`Timesheets`'s ``activity_logs``."""

    activity: str | None = None


class TimesheetUpdatedLabour(Dto):
    """A :class:`TimesheetUpdated`'s ``labour``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetUpdatedSaleOrderItem(Dto):
    """A :class:`TimesheetUpdated`'s ``sale_order_item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetUpdatedSaleOrder(Dto):
    """A :class:`TimesheetUpdated`'s ``sale_order``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetUpdatedCreatedBy(Dto):
    """A :class:`TimesheetUpdated`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class TimesheetUpdatedLastUpdatedBy(Dto):
    """A :class:`TimesheetUpdated`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class TimesheetLabour(Dto):
    """A :class:`Timesheet`'s ``labour``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetSaleOrderItem(Dto):
    """A :class:`Timesheet`'s ``sale_order_item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetSaleOrder(Dto):
    """A :class:`Timesheet`'s ``sale_order``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class TimesheetCreatedBy(Dto):
    """A :class:`Timesheet`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class TimesheetLastUpdatedBy(Dto):
    """A :class:`Timesheet`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None
