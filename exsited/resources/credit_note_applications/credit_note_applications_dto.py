"""Typed views over the credit note application bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "CreditNoteApplication",
    "CreditNoteApplicationList",
    "CreditNoteApplicationRead",
    "InvoiceCreditNoteApplications",
    "CreditNoteApplicationReadDetail",
    "CreditNoteApplicationReadPayment",
    "CreditNoteApplicationReadRefund",
    "CreditNoteApplicationReadCreatedBy",
    "CreditNoteApplicationDetail",
    "CreditNoteApplicationPayment",
    "CreditNoteApplicationRefund",
    "CreditNoteApplicationCreatedBy",
]


class CreditNoteApplication(Dto):
    """The credit note application body."""

    MEASURED_FROM = ("GET /api/{api_version}/credit_note_applications",)

    amount: float | None = None
    created_by: CreditNoteApplicationCreatedBy | None = None
    created_on: str | None = None
    credit_note: CreditNoteApplicationDetail | None = None
    credit_note_id: str | None = None
    date: str | None = None
    href: str | None = None
    id: str | None = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    payment: CreditNoteApplicationPayment | None = None
    payment_id: str | None = None
    primaryId: int | None = None
    refund: CreditNoteApplicationRefund | None = None
    refund_id: str | None = None
    remaining_balance: float | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class CreditNoteApplicationList(Dto):
    """One page of ``CreditNoteApplication`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/credit_note_applications",)

    data: list[CreditNoteApplication] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class CreditNoteApplicationRead(Dto):
    """The credit note application read body, under ``credit_note_application``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/credit_note_applications/{credit_note_application_id}",
    )

    ENVELOPE_KEY = "credit_note_application"

    amount: float | None = None
    created_by: CreditNoteApplicationReadCreatedBy | None = None
    created_on: str | None = None
    credit_note: CreditNoteApplicationReadDetail | None = None
    href: str | None = None
    id: str | None = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    payment: CreditNoteApplicationReadPayment | None = None
    primaryId: int | None = None
    refund: CreditNoteApplicationReadRefund | None = None
    remaining_balance: float | None = None
    status: str | None = None
    version: int | None = None


class InvoiceCreditNoteApplications(Dto):
    """The invoice credit note applications body."""

    MEASURED_FROM = ("GET /api/{api_version}/invoices/{invoice_id}/credit_note_applications",)

    data: list[CreditNoteApplication] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class CreditNoteApplicationReadDetail(Dto):
    """A :class:`CreditNoteApplicationRead`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteApplicationReadPayment(Dto):
    """A :class:`CreditNoteApplicationRead`'s ``payment``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteApplicationReadRefund(Dto):
    """A :class:`CreditNoteApplicationRead`'s ``refund``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteApplicationReadCreatedBy(Dto):
    """A :class:`CreditNoteApplicationRead`'s ``created_by``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteApplicationDetail(Dto):
    """A :class:`CreditNoteApplication`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteApplicationPayment(Dto):
    """A :class:`CreditNoteApplication`'s ``payment``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteApplicationRefund(Dto):
    """A :class:`CreditNoteApplication`'s ``refund``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class CreditNoteApplicationCreatedBy(Dto):
    """A :class:`CreditNoteApplication`'s ``created_by``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None
