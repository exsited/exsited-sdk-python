"""Typed views over the item fulfillment bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "ItemFulfillment",
    "ItemFulfillmentList",
    "ItemFulfillmentRead",
    "ItemFulfillmentReadList",
    "ItemFulfillments",
    "ItemFulfillmentUpdated",
    "ItemFulfillmentNotes",
    "ItemFulfillmentNote",
    "ItemFulfillmentNoteList",
    "ItemFulfillmentNoteRead",
    "ItemFulfillmentNoteAttachment",
    "ItemFulfillmentNoteWatcher",
    "ItemFulfillmentReadAccount",
    "ItemFulfillmentReadInvoice",
    "ItemFulfillmentReadRow",
    "ItemFulfillmentReadCreatedBy",
    "ItemFulfillmentReadLastUpdatedBy",
    "ItemFulfillmentsItemFulfillment",
    "ItemFulfillmentUpdatedDetail",
    "ItemFulfillmentNotesDetail",
    "ItemFulfillmentReadRowItem",
    "ItemFulfillmentAccount",
    "ItemFulfillmentInvoice",
    "ItemFulfillmentRow",
    "ItemFulfillmentCreatedBy",
    "ItemFulfillmentLastUpdatedBy",
    "ItemFulfillmentRowItem",
]


class ItemFulfillment(Dto):
    """The item fulfillment body."""


    account: ItemFulfillmentAccount | None = None
    code: str | None = None
    created_by: ItemFulfillmentCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: dict[str, Any] | None = None
    date: str | None = None
    delivery_status: Any = None
    fulfillment_completed: bool | None = None
    fulfillment_date: str | None = None
    fulfillment_note: str | None = None
    fulfillment_status: str | None = None
    fulfillments: list[ItemFulfillmentRow] | None = None
    href: str | None = None
    id: str | None = None
    invoice: ItemFulfillmentInvoice | None = None
    invoice_id: str | None = None
    last_updated_by: ItemFulfillmentLastUpdatedBy | None = None
    last_updated_on: str | None = None
    note: str | None = None
    object: str | None = None
    order: Any = None
    order_id: str | None = None
    status: str | None = None
    tracking_number: str | None = None
    uuid: str | None = None
    version: int | None = None


class ItemFulfillmentList(Dto):
    """One page of ``ItemFulfillment`` records, under ``data``; paged by offset."""


    data: list[ItemFulfillment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ItemFulfillmentRead(Dto):
    """The item fulfillment read body, under ``item_fulfillment``."""


    ENVELOPE_KEY = "item_fulfillment"

    account: ItemFulfillmentReadAccount | None = None
    code: str | None = None
    created_by: ItemFulfillmentReadCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: dict[str, Any] | None = None
    delivery_status: Any = None
    fulfillment_completed: bool | None = None
    fulfillment_date: str | None = None
    fulfillment_note: str | None = None
    fulfillment_status: str | None = None
    fulfillments: list[ItemFulfillmentReadRow] | None = None
    href: str | None = None
    id: str | None = None
    invoice: ItemFulfillmentReadInvoice | None = None
    last_updated_by: ItemFulfillmentReadLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    order: Any = None
    status: str | None = None
    tracking_number: str | None = None
    version: int | None = None


class ItemFulfillmentReadList(Dto):
    """One page of ``ItemFulfillmentRead`` records, under ``data``; paged by offset."""


    data: list[ItemFulfillmentRead] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ItemFulfillments(Dto):
    """The item fulfillments body, under ``invoice``."""


    ENVELOPE_KEY = "invoice"

    activity_logs: list[Any] | None = None
    item_fulfillment: ItemFulfillmentsItemFulfillment | None = None


class ItemFulfillmentUpdated(Dto):
    """The item fulfillment updated body."""


    item_fulfillment: ItemFulfillmentUpdatedDetail | None = None
    note: str | None = None
    status: str | None = None


class ItemFulfillmentNotes(Dto):
    """What ``create_item_fulfillment_note`` answers, under ``note``."""


    ENVELOPE_KEY = "note"

    href: str | None = None
    id: str | None = None
    item_fulfillment: ItemFulfillmentNotesDetail | None = None
    object: str | None = None


class ItemFulfillmentNote(Dto):
    """One fulfillment note as the notes listing and read answer it; the note is stored on the
    fulfillment's sale invoice."""

    attachments: list[ItemFulfillmentNoteAttachment] | None = None
    content: str | None = None
    created_by: ItemFulfillmentCreatedBy | None = None
    created_on: str | None = None
    group: Any = None
    href: str | None = None
    id: str | None = None
    item_fulfillment: ItemFulfillmentNotesDetail | None = None
    last_updated_by: Any = None
    last_updated_on: Any = None
    object: str | None = None
    user: Any = None
    version: int | None = None
    watchers: list[ItemFulfillmentNoteWatcher] | None = None


class ItemFulfillmentNoteAttachment(Dto):
    """One entry of a :class:`ItemFulfillmentNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class ItemFulfillmentNoteWatcher(Dto):
    """One entry of a :class:`ItemFulfillmentNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class ItemFulfillmentNoteList(Dto):
    """One page of ``ItemFulfillmentNote`` records, under ``data``."""


    data: list[ItemFulfillmentNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ItemFulfillmentNoteRead(Dto):
    """What ``get_item_fulfillment_note`` answers: the note under ``item_fulfillment.note``."""


    ENVELOPE_KEY = "item_fulfillment"

    note: ItemFulfillmentNote | None = None


class ItemFulfillmentReadAccount(Dto):
    """A :class:`ItemFulfillmentRead`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemFulfillmentReadInvoice(Dto):
    """A :class:`ItemFulfillmentRead`'s ``invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class ItemFulfillmentReadRow(Dto):
    """One entry of a :class:`ItemFulfillmentRead`'s ``fulfillments``."""

    fulfillment_index: int | None = None
    fulfillment_qty: float | None = None
    fulfillment_sent_qty: float | None = None
    id: str | None = None
    inventory_tracking: Any = None
    item: ItemFulfillmentReadRowItem | None = None
    object: str | None = None
    pending_return: float | None = None
    returned: float | None = None
    serving_status: str | None = None
    uom: str | None = None
    uom_precision: int | None = None


class ItemFulfillmentReadCreatedBy(Dto):
    """A :class:`ItemFulfillmentRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class ItemFulfillmentReadLastUpdatedBy(Dto):
    """A :class:`ItemFulfillmentRead`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class ItemFulfillmentsItemFulfillment(Dto):
    """A :class:`ItemFulfillments`'s ``item_fulfillment``."""

    activity_logs: list[Any] | None = None
    code: str | None = None
    fulfillment_date: str | None = None
    fulfillment_note: Any = None
    fulfillment_status: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class ItemFulfillmentUpdatedDetail(Dto):
    """A :class:`ItemFulfillmentUpdated`'s ``item_fulfillment``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class ItemFulfillmentNotesDetail(Dto):
    """A :class:`ItemFulfillmentNotes`'s ``item_fulfillment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class ItemFulfillmentReadRowItem(Dto):
    """A :class:`ItemFulfillmentReadRow`'s ``item``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemFulfillmentAccount(Dto):
    """A :class:`ItemFulfillment`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ItemFulfillmentInvoice(Dto):
    """A :class:`ItemFulfillment`'s ``invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class ItemFulfillmentRow(Dto):
    """One entry of a :class:`ItemFulfillment`'s ``fulfillments``."""

    fulfillment_index: int | None = None
    fulfillment_qty: float | None = None
    fulfillment_sent_qty: float | None = None
    id: str | None = None
    inventory_tracking: Any = None
    item: ItemFulfillmentRowItem | None = None
    object: str | None = None
    pending_return: float | None = None
    returned: float | None = None
    serving_status: str | None = None
    uom: str | None = None
    uom_precision: int | None = None


class ItemFulfillmentCreatedBy(Dto):
    """A :class:`ItemFulfillment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class ItemFulfillmentLastUpdatedBy(Dto):
    """A :class:`ItemFulfillment`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class ItemFulfillmentRowItem(Dto):
    """A :class:`ItemFulfillmentRow`'s ``item``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
