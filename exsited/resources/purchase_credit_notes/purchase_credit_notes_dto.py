"""Typed views over the purchase credit note bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "PurchaseCreditNote",
    "PurchaseCreditNoteList",
    "PurchaseCreditNoteRead",
    "PurchaseCreditNoteReadAccount",
    "PurchaseCreditNoteReadCurrency",
    "PurchaseCreditNoteReadPurchasePayment",
    "PurchaseCreditNoteReadPurchaseCreditNoteRow",
    "PurchaseCreditNoteReadCreatedBy",
    "PurchaseCreditNoteReadLastUpdatedBy",
    "PurchaseCreditNoteAccount",
    "PurchaseCreditNoteCurrency",
    "PurchaseCreditNotePurchasePayment",
    "PurchaseCreditNotePurchaseCreditNoteRow",
    "PurchaseCreditNoteCreatedBy",
    "PurchaseCreditNoteLastUpdatedBy",
    "PurchaseCreditNoteReadPurchaseCreditNoteRowPaymentMethod",
    "PurchaseCreditNoteReadPurchaseCreditNoteRowPaymentProcessor",
    "PurchaseCreditNotePurchaseCreditNoteRowPaymentMethod",
    "PurchaseCreditNotePurchaseCreditNoteRowPaymentProcessor",
    "PurchaseCreditNoteCreated",
    "PurchaseCreditNoteCreatedStatus",
]


class PurchaseCreditNote(Dto):
    """The purchase credit note body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_credit_notes",)

    account: PurchaseCreditNoteAccount | None = None
    amount: str | None = None
    code: str | None = None
    created_by: PurchaseCreditNoteCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseCreditNoteCurrency | None = None
    custom_attributes: list[Any] | None = None
    date: str | None = None
    href: str | None = None
    id: str | None = None
    initial_amount: str | None = None
    issue_date: str | None = None
    last_updated_by: PurchaseCreditNoteLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    payment_id: str | None = None
    purchase_credit_note_rows: list[PurchaseCreditNotePurchaseCreditNoteRow] | None = None
    purchase_payment: PurchaseCreditNotePurchasePayment | None = None
    refund_amount: str | None = None
    refundable: bool | None = None
    remaining_amount: str | None = None
    remaining_balance: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseCreditNoteList(Dto):
    """One page of ``PurchaseCreditNote`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_credit_notes",)

    data: list[PurchaseCreditNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseCreditNoteRead(Dto):
    """The purchase credit note read body, under ``purchase_credit_note``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_credit_notes/{purchase_credit_note_id}",
        "PATCH /api/{api_version}/purchase_credit_notes/{purchase_credit_note_id}",
    )

    ENVELOPE_KEY = "purchase_credit_note"

    account: PurchaseCreditNoteReadAccount | None = None
    code: str | None = None
    created_by: PurchaseCreditNoteReadCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseCreditNoteReadCurrency | None = None
    href: str | None = None
    id: str | None = None
    initial_amount: str | None = None
    issue_date: str | None = None
    last_updated_by: PurchaseCreditNoteReadLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    purchase_credit_note_rows: list[PurchaseCreditNoteReadPurchaseCreditNoteRow] | None = None
    purchase_payment: PurchaseCreditNoteReadPurchasePayment | None = None
    refund_amount: str | None = None
    refundable: bool | None = None
    remaining_amount: str | None = None
    status: Any = None
    version: int | None = None


class PurchaseCreditNoteReadAccount(Dto):
    """A :class:`PurchaseCreditNoteRead`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteReadCurrency(Dto):
    """A :class:`PurchaseCreditNoteRead`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteReadPurchasePayment(Dto):
    """A :class:`PurchaseCreditNoteRead`'s ``purchase_payment``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseCreditNoteReadPurchaseCreditNoteRow(Dto):
    """One entry of a :class:`PurchaseCreditNoteRead`'s ``purchase_credit_note_rows``."""

    credit_note_from_blank_method: str | None = None
    credit_note_from_credit_note: str | None = None
    credit_note_from_payment_method: str | None = None
    credit_note_total: str | None = None
    payment_method: PurchaseCreditNoteReadPurchaseCreditNoteRowPaymentMethod | None = None
    payment_processor: PurchaseCreditNoteReadPurchaseCreditNoteRowPaymentProcessor | None = None
    refund_from_blank_method: str | None = None
    refund_from_credit_note: str | None = None
    refund_from_payment_method: str | None = None
    refund_total: str | None = None


class PurchaseCreditNoteReadCreatedBy(Dto):
    """A :class:`PurchaseCreditNoteRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteReadLastUpdatedBy(Dto):
    """A :class:`PurchaseCreditNoteRead`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteAccount(Dto):
    """A :class:`PurchaseCreditNote`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteCurrency(Dto):
    """A :class:`PurchaseCreditNote`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNotePurchasePayment(Dto):
    """A :class:`PurchaseCreditNote`'s ``purchase_payment``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseCreditNotePurchaseCreditNoteRow(Dto):
    """One entry of a :class:`PurchaseCreditNote`'s ``purchase_credit_note_rows``."""

    credit_note_from_blank_method: str | None = None
    credit_note_from_credit_note: str | None = None
    credit_note_from_payment_method: str | None = None
    credit_note_total: str | None = None
    payment_method: PurchaseCreditNotePurchaseCreditNoteRowPaymentMethod | None = None
    payment_processor: PurchaseCreditNotePurchaseCreditNoteRowPaymentProcessor | None = None
    refund_from_blank_method: str | None = None
    refund_from_credit_note: str | None = None
    refund_from_payment_method: str | None = None
    refund_total: str | None = None


class PurchaseCreditNoteCreatedBy(Dto):
    """A :class:`PurchaseCreditNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteLastUpdatedBy(Dto):
    """A :class:`PurchaseCreditNote`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteReadPurchaseCreditNoteRowPaymentMethod(Dto):
    """A :class:`PurchaseCreditNoteReadPurchaseCreditNoteRow`'s ``payment_method``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteReadPurchaseCreditNoteRowPaymentProcessor(Dto):
    """A :class:`PurchaseCreditNoteReadPurchaseCreditNoteRow`'s ``payment_processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNotePurchaseCreditNoteRowPaymentMethod(Dto):
    """A :class:`PurchaseCreditNotePurchaseCreditNoteRow`'s ``payment_method``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNotePurchaseCreditNoteRowPaymentProcessor(Dto):
    """A :class:`PurchaseCreditNotePurchaseCreditNoteRow`'s ``payment_processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteCreated(Dto):
    """What ``create_purchase_credit_note`` answers, under ``purchase_credit_note``: a shorter body
    than the reads, and ``status`` an object where they send a string."""

    MEASURED_FROM = ("POST /api/{api_version}/purchase_credit_notes",)

    ENVELOPE_KEY = "purchase_credit_note"

    # Empty in every record measured, so its entries are untyped.
    activity_logs: list[Any] | None = None
    code: str | None = None
    href: str | None = None
    id: str | None = None
    initial_amount: str | None = None
    issue_date: str | None = None
    object: str | None = None
    remaining_amount: str | None = None
    status: PurchaseCreditNoteCreatedStatus | None = None
    version: int | None = None


class PurchaseCreditNoteCreatedStatus(Dto):
    """A :class:`PurchaseCreditNoteCreated`'s ``status``."""

    key: str | None = None
    value: str | None = None
