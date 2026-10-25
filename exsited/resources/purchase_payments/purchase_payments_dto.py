"""Typed views over the purchase payment bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "PurchasePayment",
    "PurchasePaymentList",
    "PurchasePaymentRead",
    "PurchasePaymentNote",
    "PurchasePaymentNoteList",
    "PurchasePaymentUpdated",
    "PurchasePayments",
    "AccountPurchasePayments",
    "PurchasePaymentNotes",
    "PurchasePaymentNoteRead",
    "PurchasePaymentNoteFile",
    "PurchasePaymentReadAccount",
    "PurchasePaymentReadCurrency",
    "PurchasePaymentReadPaymentMethodApplication",
    "PurchasePaymentReadCreditNoteApplication",
    "PurchasePaymentReadPurchaseInvoiceApplication",
    "PurchasePaymentReadCreatedBy",
    "PurchasePaymentReadLastUpdatedBy",
    "PurchasePaymentNoteReadDetail",
    "PurchasePaymentNoteReadData",
    "PurchasePaymentsAccount",
    "PurchasePaymentsCurrency",
    "PurchasePaymentsPaymentMethodApplication",
    "PurchasePaymentsCreditNoteApplication",
    "PurchasePaymentsPurchaseInvoiceApplication",
    "PurchasePaymentsCreatedBy",
    "PurchasePaymentsActivityLog",
    "PurchasePaymentUpdatedAccount",
    "PurchasePaymentUpdatedCurrency",
    "PurchasePaymentUpdatedPaymentMethodApplication",
    "PurchasePaymentUpdatedPurchaseInvoiceApplication",
    "PurchasePaymentUpdatedCreatedBy",
    "PurchasePaymentUpdatedLastUpdatedBy",
    "PurchasePaymentNotesNote",
    "PurchasePaymentAccount",
    "PurchasePaymentCurrency",
    "PurchasePaymentPaymentMethodApplication",
    "PurchasePaymentCreditNoteApplication",
    "PurchasePaymentPurchaseInvoiceApplication",
    "PurchasePaymentCreatedBy",
    "PurchasePaymentLastUpdatedBy",
    "PurchasePaymentReadPaymentMethodApplicationDetail",
    "PurchasePaymentReadPaymentMethodApplicationPaymentProcessor",
    "PurchasePaymentReadCreditNoteApplicationPurchaseCreditNote",
    "PurchasePaymentReadPurchaseInvoiceApplicationDetail",
    "PurchasePaymentNoteDetail",
    "PurchasePaymentNoteAttachment",
    "PurchasePaymentNoteWatcher",
    "PurchasePaymentNoteCreatedBy",
    "PurchasePaymentNoteReadDetailPurchasePayment",
    "PurchasePaymentNoteReadDetailAttachment",
    "PurchasePaymentNoteReadDetailWatcher",
    "PurchasePaymentNoteReadDetailCreatedBy",
    "PurchasePaymentsPaymentMethodApplicationDetail",
    "PurchasePaymentsPaymentMethodApplicationPaymentProcessor",
    "PurchasePaymentsCreditNoteApplicationPurchaseCreditNote",
    "PurchasePaymentsPurchaseInvoiceApplicationDetail",
    "PurchasePaymentUpdatedPaymentMethodApplicationDetail",
    "PurchasePaymentUpdatedPaymentMethodApplicationPaymentProcessor",
    "PurchasePaymentUpdatedPurchaseInvoiceApplicationDetail",
    "PurchasePaymentNotesNoteDetail",
    "PurchasePaymentNotesNoteAttachment",
    "PurchasePaymentNotesNoteWatcher",
    "PurchasePaymentNotesNoteCreatedBy",
    "PurchasePaymentPaymentMethodApplicationDetail",
    "PurchasePaymentPaymentMethodApplicationPaymentProcessor",
    "PurchasePaymentCreditNoteApplicationPurchaseCreditNote",
    "PurchasePaymentPurchaseInvoiceApplicationDetail",
    "PurchasePaymentNoteUpdated",
    "PurchasePaymentNoteUpdatedAttachment",
    "PurchasePaymentNoteUpdatedPurchasePayment",
    "PurchasePaymentNoteUpdatedUser",
]


class PurchasePayment(Dto):
    """The purchase payment body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_payments",)

    account: PurchasePaymentAccount | None = None
    code: str | None = None
    created_by: PurchasePaymentCreatedBy | None = None
    created_on: str | None = None
    credit_note_applications: list[PurchasePaymentCreditNoteApplication] | None = None
    credit_note_total: str | None = None
    currency: PurchasePaymentCurrency | None = None
    custom_attributes: list[Any] | None = None
    custom_objects: list[Any] | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchasePaymentLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    paid_total: str | None = None
    payment_date: str | None = None
    payment_method_applications: list[PurchasePaymentPaymentMethodApplication] | None = None
    payment_note: str | None = None
    # Null in every record measured, so untyped.
    payment_reference: Any = None
    purchase_credit_applied: list[Any] | None = None
    purchase_invoice_applications: list[PurchasePaymentPurchaseInvoiceApplication] | None = None
    purchase_invoices: list[Any] | None = None
    purchase_order_id: str | None = None
    purchase_payment_applied: list[Any] | None = None
    purchase_payment_date: str | None = None
    purchase_payment_note: str | None = None
    status: str | None = None
    total_applied: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchasePaymentList(Dto):
    """One page of ``PurchasePayment`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_payments",)

    data: list[PurchasePayment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchasePaymentRead(Dto):
    """The purchase payment read body, under ``purchase_payment``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/purchase_payments",
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_payments",
        "GET /api/{api_version}/purchase_payments/{purchase_payment_id}",
    )

    ENVELOPE_KEY = "purchase_payment"

    account: PurchasePaymentReadAccount | None = None
    code: str | None = None
    created_by: PurchasePaymentReadCreatedBy | None = None
    created_on: str | None = None
    credit_note_applications: list[PurchasePaymentReadCreditNoteApplication] | None = None
    credit_note_total: str | None = None
    currency: PurchasePaymentReadCurrency | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchasePaymentReadLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    paid_total: str | None = None
    payment_date: str | None = None
    payment_method_applications: list[PurchasePaymentReadPaymentMethodApplication] | None = None
    payment_note: str | None = None
    # Null in every record measured, so untyped.
    payment_reference: Any = None
    purchase_invoice_applications: list[PurchasePaymentReadPurchaseInvoiceApplication] | None = None
    status: str | None = None
    version: int | None = None


class PurchasePaymentNote(Dto):
    """The purchase payment note body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_payments/{purchase_payment_id}/notes",)

    attachments: list[PurchasePaymentNoteAttachment] | None = None
    content: str | None = None
    created_by: PurchasePaymentNoteCreatedBy | None = None
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
    purchase_payment: PurchasePaymentNoteDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchasePaymentNoteWatcher] | None = None


class PurchasePaymentNoteList(Dto):
    """One page of ``PurchasePaymentNote`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_payments/{purchase_payment_id}/notes",)

    data: list[PurchasePaymentNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchasePaymentUpdated(Dto):
    """The purchase payment updated body, under ``purchase_payment``."""

    MEASURED_FROM = ("PATCH /api/{api_version}/purchase_payments/{purchase_payment_id}",)

    ENVELOPE_KEY = "purchase_payment"

    account: PurchasePaymentUpdatedAccount | None = None
    activity_logs: list[Any] | None = None
    code: str | None = None
    created_by: PurchasePaymentUpdatedCreatedBy | None = None
    created_on: str | None = None
    credit_note_applications: list[Any] | None = None
    credit_note_total: str | None = None
    currency: PurchasePaymentUpdatedCurrency | None = None
    custom_attributes: list[Any] | None = None
    custom_objects: list[Any] | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchasePaymentUpdatedLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    paid_total: str | None = None
    payment_date: str | None = None
    payment_method_applications: list[PurchasePaymentUpdatedPaymentMethodApplication] | None = None
    payment_note: str | None = None
    # Null in every record measured, so untyped.
    payment_reference: Any = None
    purchase_credit_applied: list[Any] | None = None
    purchase_invoice_applications: list[PurchasePaymentUpdatedPurchaseInvoiceApplication] | None = (
        None
    )
    purchase_invoices: list[Any] | None = None
    purchase_order_id: str | None = None
    purchase_payment_applied: list[Any] | None = None
    purchase_payment_date: str | None = None
    purchase_payment_note: str | None = None
    status: str | None = None
    total_applied: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchasePayments(Dto):
    """The purchase payments body, under ``purchase_payment``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/purchase_invoices/{purchase_invoice_id}/purchase_payments",
        "POST /api/{api_version}/purchase_payments",
    )

    ENVELOPE_KEY = "purchase_payment"

    account: PurchasePaymentsAccount | None = None
    activity_logs: list[PurchasePaymentsActivityLog] | None = None
    code: str | None = None
    created_by: PurchasePaymentsCreatedBy | None = None
    created_on: str | None = None
    credit_note_applications: list[PurchasePaymentsCreditNoteApplication] | None = None
    credit_note_total: str | None = None
    currency: PurchasePaymentsCurrency | None = None
    custom_attributes: list[Any] | None = None
    custom_objects: list[Any] | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    paid_total: str | None = None
    payment_date: str | None = None
    payment_method_applications: list[PurchasePaymentsPaymentMethodApplication] | None = None
    payment_note: str | None = None
    # Null in every record measured, so untyped.
    payment_reference: Any = None
    purchase_credit_applied: list[Any] | None = None
    purchase_invoice_applications: list[PurchasePaymentsPurchaseInvoiceApplication] | None = None
    purchase_invoices: list[Any] | None = None
    purchase_order_id: str | None = None
    purchase_payment_applied: list[Any] | None = None
    purchase_payment_date: str | None = None
    purchase_payment_note: str | None = None
    status: str | None = None
    total_applied: str | None = None
    uuid: str | None = None
    version: int | None = None


class AccountPurchasePayments(Dto):
    """The account purchase payments body."""

    MEASURED_FROM = ("GET /api/{api_version}/accounts/{account_id}/purchase_payments",)

    data: list[PurchasePayment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchasePaymentNotes(Dto):
    """The purchase payment notes body, under ``files``."""

    MEASURED_FROM = ("POST /api/{api_version}/purchase_payments/{purchase_payment_id}/notes",)

    ENVELOPE_KEY = "files"

    link: str | None = None
    name: str | None = None
    note: PurchasePaymentNotesNote | None = None
    uuid: str | None = None
    version: str | None = None


class PurchasePaymentNoteRead(Dto):
    """The purchase payment note read body, under ``purchase_payment``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_payments/{purchase_payment_id}/notes/{pp_note_id}",
        "GET /api/{api_version}/purchase_payments/{purchase_payment_id}/notes/{pp_note_id}/files",
    )

    ENVELOPE_KEY = "purchase_payment"

    data: list[PurchasePaymentNoteReadData] | None = None
    note: PurchasePaymentNoteReadDetail | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchasePaymentNoteFile(Dto):
    """What ``get_purchase_payment_note_file`` answers, under ``file``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_payments/{purchase_payment_id}/notes/{pp_note_id}/files/{file_id}",
    )

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchasePaymentReadAccount(Dto):
    """A :class:`PurchasePaymentRead`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentReadCurrency(Dto):
    """A :class:`PurchasePaymentRead`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentReadPaymentMethodApplication(Dto):
    """One entry of a :class:`PurchasePaymentRead`'s ``payment_method_applications``."""

    amount: str | None = None
    payment_method: PurchasePaymentReadPaymentMethodApplicationDetail | None = None
    payment_processor: PurchasePaymentReadPaymentMethodApplicationPaymentProcessor | None = None
    reference: str | None = None


class PurchasePaymentReadCreditNoteApplication(Dto):
    """One entry of a :class:`PurchasePaymentRead`'s ``credit_note_applications``."""

    amount: str | None = None
    purchase_credit_note: PurchasePaymentReadCreditNoteApplicationPurchaseCreditNote | None = None


class PurchasePaymentReadPurchaseInvoiceApplication(Dto):
    """One entry of a :class:`PurchasePaymentRead`'s ``purchase_invoice_applications``."""

    applied: str | None = None
    due_date: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    purchase_invoice: PurchasePaymentReadPurchaseInvoiceApplicationDetail | None = None
    total: str | None = None


class PurchasePaymentReadCreatedBy(Dto):
    """A :class:`PurchasePaymentRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentReadLastUpdatedBy(Dto):
    """A :class:`PurchasePaymentRead`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentNoteReadDetail(Dto):
    """A :class:`PurchasePaymentNoteRead`'s ``note``."""

    attachments: list[PurchasePaymentNoteReadDetailAttachment] | None = None
    content: str | None = None
    created_by: PurchasePaymentNoteReadDetailCreatedBy | None = None
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
    purchase_payment: PurchasePaymentNoteReadDetailPurchasePayment | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchasePaymentNoteReadDetailWatcher] | None = None


class PurchasePaymentNoteReadData(Dto):
    """One entry of a :class:`PurchasePaymentNoteRead`'s ``data``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchasePaymentsAccount(Dto):
    """A :class:`PurchasePayments`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentsCurrency(Dto):
    """A :class:`PurchasePayments`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentsPaymentMethodApplication(Dto):
    """One entry of a :class:`PurchasePayments`'s ``payment_method_applications``."""

    amount: str | None = None
    payment_method: PurchasePaymentsPaymentMethodApplicationDetail | None = None
    payment_processor: PurchasePaymentsPaymentMethodApplicationPaymentProcessor | None = None
    reference: str | None = None


class PurchasePaymentsCreditNoteApplication(Dto):
    """One entry of a :class:`PurchasePayments`'s ``credit_note_applications``."""

    amount: str | None = None
    purchase_credit_note: PurchasePaymentsCreditNoteApplicationPurchaseCreditNote | None = None


class PurchasePaymentsPurchaseInvoiceApplication(Dto):
    """One entry of a :class:`PurchasePayments`'s ``purchase_invoice_applications``."""

    applied: str | None = None
    due_date: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    purchase_invoice: PurchasePaymentsPurchaseInvoiceApplicationDetail | None = None
    total: str | None = None


class PurchasePaymentsCreatedBy(Dto):
    """A :class:`PurchasePayments`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentsActivityLog(Dto):
    """One entry of a :class:`PurchasePayments`'s ``activity_logs``."""

    activity: str | None = None


class PurchasePaymentUpdatedAccount(Dto):
    """A :class:`PurchasePaymentUpdated`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentUpdatedCurrency(Dto):
    """A :class:`PurchasePaymentUpdated`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentUpdatedPaymentMethodApplication(Dto):
    """One entry of a :class:`PurchasePaymentUpdated`'s ``payment_method_applications``."""

    amount: str | None = None
    payment_method: PurchasePaymentUpdatedPaymentMethodApplicationDetail | None = None
    payment_processor: PurchasePaymentUpdatedPaymentMethodApplicationPaymentProcessor | None = None
    # Null in every record measured, so untyped.
    reference: Any = None


class PurchasePaymentUpdatedPurchaseInvoiceApplication(Dto):
    """One entry of a :class:`PurchasePaymentUpdated`'s ``purchase_invoice_applications``."""

    applied: str | None = None
    due_date: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    purchase_invoice: PurchasePaymentUpdatedPurchaseInvoiceApplicationDetail | None = None
    total: str | None = None


class PurchasePaymentUpdatedCreatedBy(Dto):
    """A :class:`PurchasePaymentUpdated`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentUpdatedLastUpdatedBy(Dto):
    """A :class:`PurchasePaymentUpdated`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentNotesNote(Dto):
    """A :class:`PurchasePaymentNotes`'s ``note``."""

    attachments: list[PurchasePaymentNotesNoteAttachment] | None = None
    content: str | None = None
    created_by: PurchasePaymentNotesNoteCreatedBy | None = None
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
    purchase_payment: PurchasePaymentNotesNoteDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchasePaymentNotesNoteWatcher] | None = None


class PurchasePaymentAccount(Dto):
    """A :class:`PurchasePayment`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentCurrency(Dto):
    """A :class:`PurchasePayment`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentPaymentMethodApplication(Dto):
    """One entry of a :class:`PurchasePayment`'s ``payment_method_applications``."""

    amount: str | None = None
    payment_method: PurchasePaymentPaymentMethodApplicationDetail | None = None
    payment_processor: PurchasePaymentPaymentMethodApplicationPaymentProcessor | None = None
    reference: str | None = None


class PurchasePaymentCreditNoteApplication(Dto):
    """One entry of a :class:`PurchasePayment`'s ``credit_note_applications``."""

    amount: str | None = None
    purchase_credit_note: PurchasePaymentCreditNoteApplicationPurchaseCreditNote | None = None


class PurchasePaymentPurchaseInvoiceApplication(Dto):
    """One entry of a :class:`PurchasePayment`'s ``purchase_invoice_applications``."""

    applied: str | None = None
    due_date: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    purchase_invoice: PurchasePaymentPurchaseInvoiceApplicationDetail | None = None
    total: str | None = None


class PurchasePaymentCreatedBy(Dto):
    """A :class:`PurchasePayment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentLastUpdatedBy(Dto):
    """A :class:`PurchasePayment`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentReadPaymentMethodApplicationDetail(Dto):
    """A :class:`PurchasePaymentReadPaymentMethodApplication`'s ``payment_method``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentReadPaymentMethodApplicationPaymentProcessor(Dto):
    """A :class:`PurchasePaymentReadPaymentMethodApplication`'s ``payment_processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentReadCreditNoteApplicationPurchaseCreditNote(Dto):
    """A :class:`PurchasePaymentReadCreditNoteApplication`'s ``purchase_credit_note``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentReadPurchaseInvoiceApplicationDetail(Dto):
    """A :class:`PurchasePaymentReadPurchaseInvoiceApplication`'s ``purchase_invoice``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentNoteDetail(Dto):
    """A :class:`PurchasePaymentNote`'s ``purchase_payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentNoteAttachment(Dto):
    """One entry of a :class:`PurchasePaymentNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchasePaymentNoteWatcher(Dto):
    """One entry of a :class:`PurchasePaymentNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchasePaymentNoteCreatedBy(Dto):
    """A :class:`PurchasePaymentNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentNoteReadDetailPurchasePayment(Dto):
    """A :class:`PurchasePaymentNoteReadDetail`'s ``purchase_payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentNoteReadDetailAttachment(Dto):
    """One entry of a :class:`PurchasePaymentNoteReadDetail`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchasePaymentNoteReadDetailWatcher(Dto):
    """One entry of a :class:`PurchasePaymentNoteReadDetail`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchasePaymentNoteReadDetailCreatedBy(Dto):
    """A :class:`PurchasePaymentNoteReadDetail`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentsPaymentMethodApplicationDetail(Dto):
    """A :class:`PurchasePaymentsPaymentMethodApplication`'s ``payment_method``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentsPaymentMethodApplicationPaymentProcessor(Dto):
    """A :class:`PurchasePaymentsPaymentMethodApplication`'s ``payment_processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentsCreditNoteApplicationPurchaseCreditNote(Dto):
    """A :class:`PurchasePaymentsCreditNoteApplication`'s ``purchase_credit_note``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentsPurchaseInvoiceApplicationDetail(Dto):
    """A :class:`PurchasePaymentsPurchaseInvoiceApplication`'s ``purchase_invoice``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentUpdatedPaymentMethodApplicationDetail(Dto):
    """A :class:`PurchasePaymentUpdatedPaymentMethodApplication`'s ``payment_method``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentUpdatedPaymentMethodApplicationPaymentProcessor(Dto):
    """A :class:`PurchasePaymentUpdatedPaymentMethodApplication`'s ``payment_processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentUpdatedPurchaseInvoiceApplicationDetail(Dto):
    """A :class:`PurchasePaymentUpdatedPurchaseInvoiceApplication`'s ``purchase_invoice``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentNotesNoteDetail(Dto):
    """A :class:`PurchasePaymentNotesNote`'s ``purchase_payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentNotesNoteAttachment(Dto):
    """One entry of a :class:`PurchasePaymentNotesNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchasePaymentNotesNoteWatcher(Dto):
    """One entry of a :class:`PurchasePaymentNotesNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchasePaymentNotesNoteCreatedBy(Dto):
    """A :class:`PurchasePaymentNotesNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchasePaymentPaymentMethodApplicationDetail(Dto):
    """A :class:`PurchasePaymentPaymentMethodApplication`'s ``payment_method``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentPaymentMethodApplicationPaymentProcessor(Dto):
    """A :class:`PurchasePaymentPaymentMethodApplication`'s ``payment_processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchasePaymentCreditNoteApplicationPurchaseCreditNote(Dto):
    """A :class:`PurchasePaymentCreditNoteApplication`'s ``purchase_credit_note``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentPurchaseInvoiceApplicationDetail(Dto):
    """A :class:`PurchasePaymentPurchaseInvoiceApplication`'s ``purchase_invoice``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentNoteUpdated(Dto):
    """What ``update_purchase_payment_note`` answers, under ``note``."""

    MEASURED_FROM = (
        "PATCH /api/{api_version}/purchase_payments/{purchase_payment_id}/notes/{pp_note_id}",
    )

    ENVELOPE_KEY = "note"

    attachments: list[PurchasePaymentNoteUpdatedAttachment] | None = None
    content: str | None = None
    created_by: PurchasePaymentNoteUpdatedUser | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchasePaymentNoteUpdatedUser | None = None
    last_updated_on: str | None = None
    object: str | None = None
    purchase_payment: PurchasePaymentNoteUpdatedPurchasePayment | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    # Empty in every record measured, so its entries are untyped.
    watchers: list[Any] | None = None


class PurchasePaymentNoteUpdatedAttachment(Dto):
    """One entry of a :class:`PurchasePaymentNoteUpdated`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchasePaymentNoteUpdatedPurchasePayment(Dto):
    """A :class:`PurchasePaymentNoteUpdated`'s ``purchase_payment``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchasePaymentNoteUpdatedUser(Dto):
    """A :class:`PurchasePaymentNoteUpdated`'s ``created_by`` and ``last_updated_by``."""

    name: str | None = None
    object: str | None = None
