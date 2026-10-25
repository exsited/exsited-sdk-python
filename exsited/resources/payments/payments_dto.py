"""Typed views over the payment bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Payment",
    "PaymentList",
    "PaymentNote",
    "PaymentNoteList",
    "PaymentsNote",
    "PaymentsNoteList",
    "PaymentRead",
    "AccountPayments",
    "PaymentNoteRead",
    "PaymentNoteFile",
    "PaymentNotes",
    "PaymentReadAccount",
    "PaymentReadPaymentApplied",
    "PaymentReadCreditApplied",
    "PaymentReadGiftCertificateApplied",
    "PaymentReadInvoice",
    "PaymentReadCustomAttribute",
    "PaymentReadCreatedBy",
    "PaymentReadLastUpdatedBy",
    "PaymentNoteReadDetail",
    "PaymentNotesDetail",
    "PaymentNotesAttachment",
    "PaymentNotesWatcher",
    "PaymentNotesCreatedBy",
    "PaymentAccount",
    "PaymentPaymentApplied",
    "PaymentCreditApplied",
    "PaymentGiftCertificateApplied",
    "PaymentInvoice",
    "PaymentCreatedBy",
    "PaymentLastUpdatedBy",
    "PaymentsNoteAttachment",
    "PaymentsNoteWatcher",
    "PaymentsNoteCreatedBy",
    "PaymentNoteDetail",
    "PaymentNoteAttachment",
    "PaymentNoteWatcher",
    "PaymentNoteCreatedBy",
    "PaymentNoteReadDetailPayment",
    "PaymentNoteReadDetailAttachment",
    "PaymentNoteReadDetailWatcher",
    "PaymentNoteReadDetailCreatedBy",
]


class Payment(Dto):
    """The payment body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/invoices/{invoice_id}/payments",
        "GET /api/{api_version}/orders/{order_id}/payments",
        "GET /api/{api_version}/payments",
    )

    account: PaymentAccount | None = None
    created_by: PaymentCreatedBy | None = None
    created_on: str | None = None
    credit_applied: list[PaymentCreditApplied] | None = None
    gift_certificate_applied: list[PaymentGiftCertificateApplied] | None = None
    id: str | None = None
    invoices: list[PaymentInvoice] | None = None
    last_updated_by: PaymentLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    payment_applied: list[PaymentPaymentApplied] | None = None
    payment_note: str | None = None
    reconcile_status: str | None = None
    status: str | None = None
    version: int | None = None


class PaymentList(Dto):
    """One page of ``Payment`` records, under ``data``; paged by offset."""

    MEASURED_FROM = (
        "GET /api/{api_version}/invoices/{invoice_id}/payments",
        "GET /api/{api_version}/orders/{order_id}/payments",
        "GET /api/{api_version}/payments",
    )

    data: list[Payment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PaymentNote(Dto):
    """The payment note body."""

    MEASURED_FROM = ("GET /api/{api_version}/payments/{payment_id}/notes",)

    attachments: list[PaymentNoteAttachment] | None = None
    content: str | None = None
    created_by: PaymentNoteCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    payment: PaymentNoteDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PaymentNoteWatcher] | None = None


class PaymentNoteList(Dto):
    """One page of ``PaymentNote`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/payments/{payment_id}/notes",)

    data: list[PaymentNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PaymentsNote(Dto):
    """The payments note body."""

    MEASURED_FROM = ("GET /api/{api_version}/payments/notes",)

    attachments: list[PaymentsNoteAttachment] | None = None
    content: str | None = None
    created_by: PaymentsNoteCreatedBy | None = None
    created_on: str | None = None
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
    watchers: list[PaymentsNoteWatcher] | None = None


class PaymentsNoteList(Dto):
    """One page of ``PaymentsNote`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/payments/notes",)

    data: list[PaymentsNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PaymentRead(Dto):
    """The payment read body, under ``payment``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/payments/{payment_id}",
        "PATCH /api/{api_version}/payments/{payment_id}",
    )

    ENVELOPE_KEY = "payment"

    account: PaymentReadAccount | None = None
    activity_logs: list[Any] | None = None
    created_by: PaymentReadCreatedBy | None = None
    created_on: str | None = None
    credit_applied: list[PaymentReadCreditApplied] | None = None
    custom_attributes: list[PaymentReadCustomAttribute] | None = None
    gift_certificate_applied: list[PaymentReadGiftCertificateApplied] | None = None
    id: str | None = None
    invoices: list[PaymentReadInvoice] | None = None
    last_updated_by: PaymentReadLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    payment_applied: list[PaymentReadPaymentApplied] | None = None
    payment_note: str | None = None
    reconcile_status: str | None = None
    status: str | None = None
    version: int | None = None


class AccountPayments(Dto):
    """The account payments body."""

    MEASURED_FROM = ("GET /api/{api_version}/accounts/{account_id}/payments",)

    data: list[Payment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PaymentNoteRead(Dto):
    """The payment note read body, under ``payment``."""

    MEASURED_FROM = ("GET /api/{api_version}/payments/{payment_id}/notes/{payment_note_id}",)

    ENVELOPE_KEY = "payment"

    note: PaymentNoteReadDetail | None = None


class PaymentNoteFile(Dto):
    """What ``get_payment_note_file`` answers, under ``file``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/payments/{payment_id}/notes/{payment_note_id}/files/{payment_file_id}",
    )

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PaymentNotes(Dto):
    """What ``create_payment_note`` answers, under ``note``."""

    MEASURED_FROM = ("POST /api/{api_version}/payments/{payment_id}/notes",)

    ENVELOPE_KEY = "note"

    attachments: list[PaymentNotesAttachment] | None = None
    content: str | None = None
    created_by: PaymentNotesCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    payment: PaymentNotesDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PaymentNotesWatcher] | None = None


class PaymentReadAccount(Dto):
    """A :class:`PaymentRead`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PaymentReadPaymentApplied(Dto):
    """One entry of a :class:`PaymentRead`'s ``payment_applied``."""

    amount: str | None = None
    # Null in every record measured, so untyped.
    gateway_response: Any = None
    method: str | None = None
    processor: str | None = None
    reference: str | None = None


class PaymentReadCreditApplied(Dto):
    """One entry of a :class:`PaymentRead`'s ``credit_applied``."""

    amount: str | None = None
    code: str | None = None


class PaymentReadGiftCertificateApplied(Dto):
    """One entry of a :class:`PaymentRead`'s ``gift_certificate_applied``."""

    amount: str | None = None
    code: str | None = None


class PaymentReadInvoice(Dto):
    """One entry of a :class:`PaymentRead`'s ``invoices``."""

    applied: str | None = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    total: str | None = None


class PaymentReadCustomAttribute(Dto):
    """One entry of a :class:`PaymentRead`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class PaymentReadCreatedBy(Dto):
    """A :class:`PaymentRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PaymentReadLastUpdatedBy(Dto):
    """A :class:`PaymentRead`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PaymentNoteReadDetail(Dto):
    """A :class:`PaymentNoteRead`'s ``note``."""

    attachments: list[PaymentNoteReadDetailAttachment] | None = None
    content: str | None = None
    created_by: PaymentNoteReadDetailCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    payment: PaymentNoteReadDetailPayment | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PaymentNoteReadDetailWatcher] | None = None


class PaymentNotesDetail(Dto):
    """A :class:`PaymentNotes`'s ``payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PaymentNotesAttachment(Dto):
    """One entry of a :class:`PaymentNotes`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PaymentNotesWatcher(Dto):
    """One entry of a :class:`PaymentNotes`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PaymentNotesCreatedBy(Dto):
    """A :class:`PaymentNotes`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PaymentAccount(Dto):
    """A :class:`Payment`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PaymentPaymentApplied(Dto):
    """One entry of a :class:`Payment`'s ``payment_applied``."""

    amount: str | None = None
    # Null in every record measured, so untyped.
    gateway_response: Any = None
    method: str | None = None
    processor: str | None = None
    reference: str | None = None


class PaymentCreditApplied(Dto):
    """One entry of a :class:`Payment`'s ``credit_applied``."""

    amount: str | None = None
    code: str | None = None


class PaymentGiftCertificateApplied(Dto):
    """One entry of a :class:`Payment`'s ``gift_certificate_applied``."""

    amount: str | None = None
    code: str | None = None


class PaymentInvoice(Dto):
    """One entry of a :class:`Payment`'s ``invoices``."""

    applied: str | None = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    total: str | None = None


class PaymentCreatedBy(Dto):
    """A :class:`Payment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PaymentLastUpdatedBy(Dto):
    """A :class:`Payment`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PaymentsNoteAttachment(Dto):
    """One entry of a :class:`PaymentsNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PaymentsNoteWatcher(Dto):
    """One entry of a :class:`PaymentsNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PaymentsNoteCreatedBy(Dto):
    """A :class:`PaymentsNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PaymentNoteDetail(Dto):
    """A :class:`PaymentNote`'s ``payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PaymentNoteAttachment(Dto):
    """One entry of a :class:`PaymentNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PaymentNoteWatcher(Dto):
    """One entry of a :class:`PaymentNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PaymentNoteCreatedBy(Dto):
    """A :class:`PaymentNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PaymentNoteReadDetailPayment(Dto):
    """A :class:`PaymentNoteReadDetail`'s ``payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PaymentNoteReadDetailAttachment(Dto):
    """One entry of a :class:`PaymentNoteReadDetail`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PaymentNoteReadDetailWatcher(Dto):
    """One entry of a :class:`PaymentNoteReadDetail`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PaymentNoteReadDetailCreatedBy(Dto):
    """A :class:`PaymentNoteReadDetail`'s ``created_by``."""

    name: str | None = None
    object: str | None = None
