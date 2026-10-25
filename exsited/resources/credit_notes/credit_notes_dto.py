"""Typed views over the credit note bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "CreditNote",
    "CreditNoteList",
    "CreditNoteRead",
    "CreditNoteReadAccount",
    "CreditNoteReadCurrency",
    "CreditNoteReadPayment",
    "CreditNoteReadInvoice",
    "CreditNoteReadCustomAttribute",
    "CreditNoteReadCreatedBy",
    "CreditNoteReadLastUpdatedBy",
    "CreditNoteAccount",
    "CreditNoteCurrency",
    "CreditNotePayment",
    "CreditNoteInvoice",
    "CreditNoteCustomAttribute",
    "CreditNoteCreatedBy",
    "CreditNoteLastUpdatedBy",
    "CreditNoteItems",
    "CreditNoteItem",
    "CreditNoteApplications",
    "CreditNoteNote",
    "CreditNoteNoteList",
    "CreditNoteNoteDetail",
    "CreditNoteNoteCreatedBy",
]


class CreditNote(Dto):
    """The credit note body."""

    MEASURED_FROM = ("GET /api/{api_version}/credit_notes",)

    account: CreditNoteAccount | None = None
    account_id: str | None = None
    amount: str | None = None
    code: str | None = None
    created_by: CreditNoteCreatedBy | None = None
    created_on: str | None = None
    currency: CreditNoteCurrency | None = None
    custom_attributes: list[CreditNoteCustomAttribute] | None = None
    custom_objects: list[Any] | None = None
    date: str | None = None
    href: str | None = None
    id: str | None = None
    initial_amount: str | None = None
    invoice_id: str | None = None
    invoices: list[CreditNoteInvoice] | None = None
    issue_date: str | None = None
    last_updated_by: CreditNoteLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    payment: CreditNotePayment | None = None
    payment_id: str | None = None
    refund_amount: str | None = None
    refundable: bool | None = None
    remaining_amount: str | None = None
    remaining_balance: str | None = None
    status: str | None = None
    updated_by: str | None = None
    updated_on: str | None = None
    uuid: str | None = None
    version: int | None = None


class CreditNoteList(Dto):
    """One page of ``CreditNote`` records, under ``data``; paged by offset."""

    MEASURED_FROM = (
        "GET /api/{api_version}/credit_notes",
        "GET /api/{api_version}/accounts/{account_id}/credit_notes",
    )

    data: list[CreditNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class CreditNoteRead(Dto):
    """The credit note read body, under ``credit_note``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/credit_notes/{credit_note_id}",
        "PATCH /api/{api_version}/credit_notes/{credit_note_id}",
    )

    ENVELOPE_KEY = "credit_note"

    account: CreditNoteReadAccount | None = None
    code: str | None = None
    created_by: CreditNoteReadCreatedBy | None = None
    created_on: str | None = None
    currency: CreditNoteReadCurrency | None = None
    custom_attributes: list[CreditNoteReadCustomAttribute] | None = None
    href: str | None = None
    id: str | None = None
    initial_amount: str | None = None
    invoices: list[CreditNoteReadInvoice] | None = None
    issue_date: str | None = None
    last_updated_by: CreditNoteReadLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    payment: CreditNoteReadPayment | None = None
    refund_amount: str | None = None
    refundable: bool | None = None
    remaining_amount: str | None = None
    status: str | None = None
    version: int | None = None


class CreditNoteReadAccount(Dto):
    """A :class:`CreditNoteRead`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteReadCurrency(Dto):
    """A :class:`CreditNoteRead`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteReadPayment(Dto):
    """A :class:`CreditNoteRead`'s ``payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class CreditNoteReadInvoice(Dto):
    """One entry of a :class:`CreditNoteRead`'s ``invoices``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class CreditNoteReadCustomAttribute(Dto):
    """One entry of a :class:`CreditNoteRead`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: Any = None


class CreditNoteReadCreatedBy(Dto):
    """A :class:`CreditNoteRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class CreditNoteReadLastUpdatedBy(Dto):
    """A :class:`CreditNoteRead`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class CreditNoteAccount(Dto):
    """A :class:`CreditNote`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteCurrency(Dto):
    """A :class:`CreditNote`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNotePayment(Dto):
    """A :class:`CreditNote`'s ``payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class CreditNoteInvoice(Dto):
    """One entry of a :class:`CreditNote`'s ``invoices``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class CreditNoteCustomAttribute(Dto):
    """One entry of a :class:`CreditNote`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: Any = None


class CreditNoteCreatedBy(Dto):
    """A :class:`CreditNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class CreditNoteLastUpdatedBy(Dto):
    """A :class:`CreditNote`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class CreditNoteItems(Dto):
    """A credit note's balance rows, under ``credit_note``."""

    MEASURED_FROM = ("GET /api/{api_version}/credit_notes/{credit_note_id}/items",)

    ENVELOPE_KEY = "credit_note"

    href: str | None = None
    items: list[CreditNoteItem] | None = None
    object: str | None = None


class CreditNoteItem(Dto):
    """One entry of a :class:`CreditNoteItems`'s ``items``: what was credited and refunded, by
    source, each amount a string."""

    credit_note_from_blank_method: str | None = None
    credit_note_from_credit_note: str | None = None
    credit_note_from_gift_certificate: str | None = None
    credit_note_from_invoice_credit: str | None = None
    credit_note_from_payment_method: str | None = None
    credit_note_total: str | None = None
    # Null in every record measured, so untyped.
    invoice: Any = None
    object: str | None = None
    refund_from_blank_method: str | None = None
    refund_from_credit_note: str | None = None
    refund_from_gift_certificate: str | None = None
    refund_from_invoice_credit: str | None = None
    refund_from_payment_method: str | None = None
    refund_total: str | None = None


class CreditNoteApplications(Dto):
    """A credit note's applications, under ``credit_note``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/credit_notes/{credit_note_id}/credit_note_applications",
    )

    ENVELOPE_KEY = "credit_note"

    # Empty in every record measured, so its entries are untyped.
    applications: list[Any] | None = None
    href: str | None = None
    object: str | None = None


class CreditNoteNote(Dto):
    """One note on a credit note, under ``note``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/credit_notes/{credit_note_id}/notes",
        "GET /api/{api_version}/credit_notes/{credit_note_id}/notes/{note_id}",
    )

    ENVELOPE_KEY = "note"

    # Empty in every record measured, so its entries are untyped.
    attachments: list[Any] | None = None
    content: str | None = None
    created_by: CreditNoteNoteCreatedBy | None = None
    created_on: str | None = None
    credit_note: CreditNoteNoteDetail | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    # Empty in every record measured, so its entries are untyped.
    watchers: list[Any] | None = None


class CreditNoteNoteList(Dto):
    """One page of ``CreditNoteNote`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/credit_notes/{credit_note_id}/notes",)

    data: list[CreditNoteNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class CreditNoteNoteDetail(Dto):
    """A :class:`CreditNoteNote`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class CreditNoteNoteCreatedBy(Dto):
    """A :class:`CreditNoteNote`'s ``created_by``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None
