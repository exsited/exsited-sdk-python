"""Typed views over the purchase credit note application bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "PurchaseCreditNoteApplication",
    "PurchaseCreditNoteApplicationList",
    "PurchaseCreditNoteApplicationRead",
    "PurchaseCreditNoteApplicationReadDetail",
    "PurchaseCreditNoteApplicationReadPurchasePayment",
    "PurchaseCreditNoteApplicationReadCreatedBy",
    "PurchaseCreditNoteApplicationDetail",
    "PurchaseCreditNoteApplicationPurchasePayment",
    "PurchaseCreditNoteApplicationCreatedBy",
]


class PurchaseCreditNoteApplication(Dto):
    """The purchase credit note application body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_credit_note_applications",)

    amount: str | None = None
    created_by: PurchaseCreditNoteApplicationCreatedBy | None = None
    created_on: str | None = None
    credit_note_id: str | None = None
    date: str | None = None
    href: str | None = None
    id: str | None = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    payment_id: str | None = None
    purchase_credit_note: PurchaseCreditNoteApplicationDetail | None = None
    purchase_payment: PurchaseCreditNoteApplicationPurchasePayment | None = None
    remaining_balance: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseCreditNoteApplicationList(Dto):
    """One page of ``PurchaseCreditNoteApplication`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_credit_note_applications",)

    data: list[PurchaseCreditNoteApplication] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseCreditNoteApplicationRead(Dto):
    """The purchase credit note application read body, under
    ``purchase_credit_note_application``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_credit_note_applications/{purchase_credit_note_application_id}",
    )

    ENVELOPE_KEY = "purchase_credit_note_application"

    amount: str | None = None
    created_by: PurchaseCreditNoteApplicationReadCreatedBy | None = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    purchase_credit_note: PurchaseCreditNoteApplicationReadDetail | None = None
    purchase_payment: PurchaseCreditNoteApplicationReadPurchasePayment | None = None
    remaining_balance: str | None = None
    status: str | None = None
    version: int | None = None


class PurchaseCreditNoteApplicationReadDetail(Dto):
    """A :class:`PurchaseCreditNoteApplicationRead`'s ``purchase_credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteApplicationReadPurchasePayment(Dto):
    """A :class:`PurchaseCreditNoteApplicationRead`'s ``purchase_payment``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteApplicationReadCreatedBy(Dto):
    """A :class:`PurchaseCreditNoteApplicationRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteApplicationDetail(Dto):
    """A :class:`PurchaseCreditNoteApplication`'s ``purchase_credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteApplicationPurchasePayment(Dto):
    """A :class:`PurchaseCreditNoteApplication`'s ``purchase_payment``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseCreditNoteApplicationCreatedBy(Dto):
    """A :class:`PurchaseCreditNoteApplication`'s ``created_by``."""

    name: str | None = None
    object: str | None = None
