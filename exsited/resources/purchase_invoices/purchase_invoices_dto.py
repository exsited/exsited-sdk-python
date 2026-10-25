"""Typed views over the purchase invoice bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "PurchaseInvoice",
    "PurchaseInvoiceList",
    "PurchaseInvoicePurchasePayment",
    "PurchaseInvoicePurchasePaymentList",
    "PurchaseInvoiceNote",
    "PurchaseInvoiceNoteList",
    "PurchaseInvoicesNote",
    "PurchaseInvoicesNoteList",
    "PurchaseInvoiceRead",
    "AccountPurchaseInvoices",
    "PurchaseInvoiceInformation",
    "PurchaseInvoiceCancel",
    "PurchaseInvoiceNotes",
    "PurchaseInvoiceLines",
    "PurchaseInvoiceLine",
    "PurchaseInvoiceNoteRead",
    "PurchaseInvoiceNoteFile",
    "PurchaseInvoiceNoteUpdated",
    "AccountPurchaseInvoicesData",
    "PurchaseInvoiceReadCurrency",
    "PurchaseInvoiceReadAccount",
    "PurchaseInvoiceReadPurchaseOrder",
    "PurchaseInvoiceReadCreatedBy",
    "PurchaseInvoiceReadLastUpdatedBy",
    "PurchaseInvoiceReadCustomAttribute",
    "PurchaseInvoiceReadLine",
    "PurchaseInvoiceReadKpis",
    "PurchaseInvoiceCurrency",
    "PurchaseInvoiceAccount",
    "PurchaseInvoicePurchaseOrder",
    "PurchaseInvoiceCreatedBy",
    "PurchaseInvoiceLastUpdatedBy",
    "PurchaseInvoiceLinesRow",
    "PurchaseInvoiceLineDetail",
    "PurchaseInvoiceNoteReadDetail",
    "PurchaseInvoiceNoteReadData",
    "PurchaseInvoiceInformationCurrency",
    "PurchaseInvoiceInformationAccount",
    "PurchaseInvoiceInformationCreatedBy",
    "PurchaseInvoiceInformationLastUpdatedBy",
    "PurchaseInvoiceInformationLine",
    "PurchaseInvoiceInformationKpis",
    "PurchaseInvoiceCancelDetail",
    "PurchaseInvoiceNotesNote",
    "PurchaseInvoiceNoteUpdatedDetail",
    "PurchaseInvoiceNoteUpdatedCreatedBy",
    "PurchaseInvoiceNoteUpdatedLastUpdatedBy",
    "AccountPurchaseInvoicesDataCurrency",
    "AccountPurchaseInvoicesDataDetail",
    "AccountPurchaseInvoicesDataPurchaseOrder",
    "AccountPurchaseInvoicesDataCreatedBy",
    "AccountPurchaseInvoicesDataLastUpdatedBy",
    "AccountPurchaseInvoicesDataPurchaseCreditNote",
    "AccountPurchaseInvoicesDataPurchasePayment",
    "PurchaseInvoicesNoteWatcher",
    "PurchaseInvoicesNoteCreatedBy",
    "PurchaseInvoicesNoteLastUpdatedBy",
    "PurchaseInvoiceReadLineItem",
    "PurchaseInvoiceLinesRowItem",
    "PurchaseInvoiceLineDetailItem",
    "PurchaseInvoicePurchasePaymentAccount",
    "PurchaseInvoicePurchasePaymentCurrency",
    "PurchaseInvoicePurchasePaymentPaymentMethodApplication",
    "PurchaseInvoicePurchasePaymentCreditNoteApplication",
    "PurchaseInvoicePurchasePaymentPurchaseInvoiceApplication",
    "PurchaseInvoicePurchasePaymentCreatedBy",
    "PurchaseInvoicePurchasePaymentLastUpdatedBy",
    "PurchaseInvoiceNoteDetail",
    "PurchaseInvoiceNoteAttachment",
    "PurchaseInvoiceNoteWatcher",
    "PurchaseInvoiceNoteCreatedBy",
    "PurchaseInvoiceNoteLastUpdatedBy",
    "PurchaseInvoiceNoteReadDetailPurchaseInvoice",
    "PurchaseInvoiceNoteReadDetailAttachment",
    "PurchaseInvoiceNoteReadDetailWatcher",
    "PurchaseInvoiceNoteReadDetailCreatedBy",
    "PurchaseInvoiceInformationLineItem",
    "PurchaseInvoiceCancelDetailCurrency",
    "PurchaseInvoiceCancelDetailAccount",
    "PurchaseInvoiceCancelDetailCreatedBy",
    "PurchaseInvoiceCancelDetailLastUpdatedBy",
    "PurchaseInvoiceCancelDetailLine",
    "PurchaseInvoiceCancelDetailKpis",
    "PurchaseInvoiceNotesNoteDetail",
    "PurchaseInvoiceNotesNoteAttachment",
    "PurchaseInvoiceNotesNoteWatcher",
    "PurchaseInvoiceNotesNoteCreatedBy",
    "PurchaseInvoicePurchasePaymentPaymentMethodApplicationDetail",
    "PurchaseInvoicePurchasePaymentPaymentMethodApplicationPaymentProcessor",
    "PurchaseInvoicePurchasePaymentCreditNoteApplicationPurchaseCreditNote",
    "PurchaseInvoicePurchasePaymentPurchaseInvoiceApplicationDetail",
    "PurchaseInvoiceCancelDetailLineItem",
]


class PurchaseInvoice(Dto):
    """The purchase invoice body, under ``purchase_invoice``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices",
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/information",
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_invoices",
    )

    ENVELOPE_KEY = "purchase_invoice"

    account: PurchaseInvoiceAccount | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    created_by: PurchaseInvoiceCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseInvoiceCurrency | None = None
    # Null in every record measured, so untyped.
    custom_form: Any = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    last_updated_by: PurchaseInvoiceLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    payment_status: str | None = None
    price_tax_inclusive: bool | None = None
    purchase_order: PurchaseInvoicePurchaseOrder | None = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseInvoiceList(Dto):
    """One page of ``PurchaseInvoice`` records, under ``data``; paged by offset."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices",
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_invoices",
    )

    data: list[PurchaseInvoice] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseInvoicePurchasePayment(Dto):
    """The purchase invoice purchase payment body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/purchase_payments",
    )

    account: PurchaseInvoicePurchasePaymentAccount | None = None
    code: str | None = None
    created_by: PurchaseInvoicePurchasePaymentCreatedBy | None = None
    created_on: str | None = None
    credit_note_applications: list[PurchaseInvoicePurchasePaymentCreditNoteApplication] | None = (
        None
    )
    credit_note_total: str | None = None
    currency: PurchaseInvoicePurchasePaymentCurrency | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchaseInvoicePurchasePaymentLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    paid_total: str | None = None
    payment_date: str | None = None
    payment_method_applications: (
        list[PurchaseInvoicePurchasePaymentPaymentMethodApplication] | None
    ) = None
    payment_note: str | None = None
    # Null in every record measured, so untyped.
    payment_reference: Any = None
    purchase_invoice_applications: (
        list[PurchaseInvoicePurchasePaymentPurchaseInvoiceApplication] | None
    ) = None
    status: str | None = None
    version: int | None = None


class PurchaseInvoicePurchasePaymentList(Dto):
    """One page of ``PurchaseInvoicePurchasePayment`` records, under ``data``; paged by offset."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/purchase_payments",
    )

    data: list[PurchaseInvoicePurchasePayment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseInvoiceNote(Dto):
    """The purchase invoice note body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes",)

    attachments: list[PurchaseInvoiceNoteAttachment] | None = None
    content: str | None = None
    created_by: PurchaseInvoiceNoteCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchaseInvoiceNoteLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    purchase_invoice: PurchaseInvoiceNoteDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchaseInvoiceNoteWatcher] | None = None


class PurchaseInvoiceNoteList(Dto):
    """One page of ``PurchaseInvoiceNote`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes",)

    data: list[PurchaseInvoiceNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseInvoicesNote(Dto):
    """The purchase invoices note body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_invoices/notes",)

    attachments: list[Any] | None = None
    content: str | None = None
    created_by: PurchaseInvoicesNoteCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchaseInvoicesNoteLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchaseInvoicesNoteWatcher] | None = None


class PurchaseInvoicesNoteList(Dto):
    """One page of ``PurchaseInvoicesNote`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_invoices/notes",)

    data: list[PurchaseInvoicesNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseInvoiceRead(Dto):
    """The purchase invoice read body, under ``purchase_invoice``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}",
        "POST /api/{api_version}/purchase_invoices",
        "POST /api/{api_version}/purchase_invoices/{purchase_invoice_id}/amend",
        "POST /api/{api_version}/purchase_invoices/{purchase_invoice_id}/reactivate",
        "POST /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_invoices",
    )

    ENVELOPE_KEY = "purchase_invoice"

    account: PurchaseInvoiceReadAccount | None = None
    activity_logs: list[Any] | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    created_by: PurchaseInvoiceReadCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseInvoiceReadCurrency | None = None
    custom_attributes: list[PurchaseInvoiceReadCustomAttribute] | None = None
    # Null in every record measured, so untyped.
    custom_form: Any = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    kpis: PurchaseInvoiceReadKpis | None = None
    last_updated_by: PurchaseInvoiceReadLastUpdatedBy | None = None
    last_updated_on: str | None = None
    lines: list[PurchaseInvoiceReadLine] | None = None
    object: str | None = None
    origin: str | None = None
    payment_status: str | None = None
    price_tax_inclusive: bool | None = None
    purchase_order: PurchaseInvoiceReadPurchaseOrder | None = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None


class AccountPurchaseInvoices(Dto):
    """The account purchase invoices body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/accounts/{account_id}/purchase_invoices",
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/purchase_credit_note_applications",
    )

    data: list[AccountPurchaseInvoicesData] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseInvoiceInformation(Dto):
    """The purchase invoice information body, under ``purchase_invoice``."""

    MEASURED_FROM = (
        "PATCH /api/{api_version}/purchase_invoices/{purchase_invoice_id}/information",
    )

    ENVELOPE_KEY = "purchase_invoice"

    account: PurchaseInvoiceInformationAccount | None = None
    activity_logs: list[Any] | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    created_by: PurchaseInvoiceInformationCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseInvoiceInformationCurrency | None = None
    custom_attributes: list[Any] | None = None
    # Null in every record measured, so untyped.
    custom_form: Any = None
    due_date: str | None = None
    id: str | None = None
    invoice_note: str | None = None
    issue_date: str | None = None
    kpis: PurchaseInvoiceInformationKpis | None = None
    last_updated_by: PurchaseInvoiceInformationLastUpdatedBy | None = None
    last_updated_on: str | None = None
    lines: list[PurchaseInvoiceInformationLine] | None = None
    object: str | None = None
    origin: str | None = None
    payment_status: str | None = None
    price_tax_inclusive: bool | None = None
    # Null in every record measured, so untyped.
    purchase_order: Any = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseInvoiceCancel(Dto):
    """The purchase invoice cancel body."""

    MEASURED_FROM = ("POST /api/{api_version}/purchase_invoices/{purchase_invoice_id}/cancel",)

    activity_logs: list[Any] | None = None
    event_uuid: str | None = None
    purchase_invoice: PurchaseInvoiceCancelDetail | None = None


class PurchaseInvoiceNotes(Dto):
    """The purchase invoice notes body, under ``watcherList``."""

    MEASURED_FROM = ("POST /api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes",)

    ENVELOPE_KEY = "watcherList"

    external_watchers: list[Any] | None = None
    internal_watchers: list[Any] | None = None
    note: PurchaseInvoiceNotesNote | None = None


class PurchaseInvoiceLines(Dto):
    """The purchase invoice lines body, under ``purchase_invoice``."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/lines",)

    ENVELOPE_KEY = "purchase_invoice"

    lines: list[PurchaseInvoiceLinesRow] | None = None
    object: str | None = None


class PurchaseInvoiceLine(Dto):
    """The purchase invoice line body, under ``purchase_invoice``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/lines/{purchase_invoice_line_uuid}",
    )

    ENVELOPE_KEY = "purchase_invoice"

    line: PurchaseInvoiceLineDetail | None = None
    object: str | None = None


class PurchaseInvoiceNoteRead(Dto):
    """The purchase invoice note read body, under ``purchase_invoice``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes/{note_id}",
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes/{note_id}/files",
    )

    ENVELOPE_KEY = "purchase_invoice"

    data: list[PurchaseInvoiceNoteReadData] | None = None
    note: PurchaseInvoiceNoteReadDetail | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseInvoiceNoteFile(Dto):
    """What ``get_purchase_invoice_note_file`` answers, under ``file``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes/{note_id}/files/{file_id}",
    )

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseInvoiceNoteUpdated(Dto):
    """What ``update_purchase_invoice_note`` answers, under ``note``."""

    MEASURED_FROM = (
        "PATCH /api/{api_version}/purchase_invoices/{purchase_invoice_id}/notes/{note_id}",
    )

    ENVELOPE_KEY = "note"

    attachments: list[Any] | None = None
    content: str | None = None
    created_by: PurchaseInvoiceNoteUpdatedCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchaseInvoiceNoteUpdatedLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    purchase_invoice: PurchaseInvoiceNoteUpdatedDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[Any] | None = None


class AccountPurchaseInvoicesData(Dto):
    """One entry of a :class:`AccountPurchaseInvoices`'s ``data``."""

    account: AccountPurchaseInvoicesDataDetail | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    amount: str | None = None
    created_by: AccountPurchaseInvoicesDataCreatedBy | None = None
    created_on: str | None = None
    currency: AccountPurchaseInvoicesDataCurrency | None = None
    # Null in every record measured, so untyped.
    custom_form: Any = None
    due_date: str | None = None
    href: str | None = None
    id: str | None = None
    issue_date: str | None = None
    last_updated_by: AccountPurchaseInvoicesDataLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    payment_status: str | None = None
    price_tax_inclusive: bool | None = None
    purchase_credit_note: AccountPurchaseInvoicesDataPurchaseCreditNote | None = None
    purchase_order: AccountPurchaseInvoicesDataPurchaseOrder | None = None
    purchase_payment: AccountPurchaseInvoicesDataPurchasePayment | None = None
    remaining_balance: str | None = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseInvoiceReadCurrency(Dto):
    """A :class:`PurchaseInvoiceRead`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceReadAccount(Dto):
    """A :class:`PurchaseInvoiceRead`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceReadPurchaseOrder(Dto):
    """A :class:`PurchaseInvoiceRead`'s ``purchase_order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseInvoiceReadCreatedBy(Dto):
    """A :class:`PurchaseInvoiceRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceReadLastUpdatedBy(Dto):
    """A :class:`PurchaseInvoiceRead`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceReadCustomAttribute(Dto):
    """One entry of a :class:`PurchaseInvoiceRead`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class PurchaseInvoiceReadLine(Dto):
    """One entry of a :class:`PurchaseInvoiceRead`'s ``lines``."""

    accounting_code: str | None = None
    id: str | None = None
    item: PurchaseInvoiceReadLineItem | None = None
    object: str | None = None
    quantity: int | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uom: str | None = None
    version: int | None = None
    warehouse: str | None = None


class PurchaseInvoiceReadKpis(Dto):
    """A :class:`PurchaseInvoiceRead`'s ``kpis``."""

    credit_applied: str | None = None
    credit_issued: str | None = None
    # Null in every record measured, so untyped.
    deleted_on: Any = None
    # Null in every record measured, so untyped.
    last_amended_on: Any = None
    # Null in every record measured, so untyped.
    last_cancelled_on: Any = None
    # Null in every record measured, so untyped.
    last_payment_date: Any = None
    # Null in every record measured, so untyped.
    last_reactivated_on: Any = None
    object: str | None = None
    outstanding: str | None = None
    overdue: str | None = None
    payment_applied: str | None = None
    # Null in every record measured, so untyped.
    voided_on: Any = None


class PurchaseInvoiceCurrency(Dto):
    """A :class:`PurchaseInvoice`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceAccount(Dto):
    """A :class:`PurchaseInvoice`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoicePurchaseOrder(Dto):
    """A :class:`PurchaseInvoice`'s ``purchase_order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseInvoiceCreatedBy(Dto):
    """A :class:`PurchaseInvoice`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceLastUpdatedBy(Dto):
    """A :class:`PurchaseInvoice`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceLinesRow(Dto):
    """One entry of a :class:`PurchaseInvoiceLines`'s ``lines``."""

    accounting_code: str | None = None
    id: str | None = None
    item: PurchaseInvoiceLinesRowItem | None = None
    object: str | None = None
    quantity: int | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uom: str | None = None
    version: int | None = None
    warehouse: str | None = None


class PurchaseInvoiceLineDetail(Dto):
    """A :class:`PurchaseInvoiceLine`'s ``line``."""

    accounting_code: str | None = None
    id: str | None = None
    item: PurchaseInvoiceLineDetailItem | None = None
    object: str | None = None
    quantity: int | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uom: str | None = None
    version: int | None = None
    warehouse: str | None = None


class PurchaseInvoiceNoteReadDetail(Dto):
    """A :class:`PurchaseInvoiceNoteRead`'s ``note``."""

    attachments: list[PurchaseInvoiceNoteReadDetailAttachment] | None = None
    content: str | None = None
    created_by: PurchaseInvoiceNoteReadDetailCreatedBy | None = None
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
    purchase_invoice: PurchaseInvoiceNoteReadDetailPurchaseInvoice | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchaseInvoiceNoteReadDetailWatcher] | None = None


class PurchaseInvoiceNoteReadData(Dto):
    """One entry of a :class:`PurchaseInvoiceNoteRead`'s ``data``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseInvoiceInformationCurrency(Dto):
    """A :class:`PurchaseInvoiceInformation`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceInformationAccount(Dto):
    """A :class:`PurchaseInvoiceInformation`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceInformationCreatedBy(Dto):
    """A :class:`PurchaseInvoiceInformation`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceInformationLastUpdatedBy(Dto):
    """A :class:`PurchaseInvoiceInformation`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceInformationLine(Dto):
    """One entry of a :class:`PurchaseInvoiceInformation`'s ``lines``."""

    accounting_code: str | None = None
    id: str | None = None
    item: PurchaseInvoiceInformationLineItem | None = None
    object: str | None = None
    quantity: int | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uom: str | None = None
    version: int | None = None
    warehouse: str | None = None


class PurchaseInvoiceInformationKpis(Dto):
    """A :class:`PurchaseInvoiceInformation`'s ``kpis``."""

    credit_applied: str | None = None
    credit_issued: str | None = None
    # Null in every record measured, so untyped.
    deleted_on: Any = None
    # Null in every record measured, so untyped.
    last_amended_on: Any = None
    # Null in every record measured, so untyped.
    last_cancelled_on: Any = None
    # Null in every record measured, so untyped.
    last_payment_date: Any = None
    # Null in every record measured, so untyped.
    last_reactivated_on: Any = None
    object: str | None = None
    outstanding: str | None = None
    overdue: str | None = None
    payment_applied: str | None = None
    # Null in every record measured, so untyped.
    voided_on: Any = None


class PurchaseInvoiceCancelDetail(Dto):
    """A :class:`PurchaseInvoiceCancel`'s ``purchase_invoice``."""

    account: PurchaseInvoiceCancelDetailAccount | None = None
    activity_logs: list[Any] | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    created_by: PurchaseInvoiceCancelDetailCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseInvoiceCancelDetailCurrency | None = None
    custom_attributes: list[Any] | None = None
    # Null in every record measured, so untyped.
    custom_form: Any = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    kpis: PurchaseInvoiceCancelDetailKpis | None = None
    last_updated_by: PurchaseInvoiceCancelDetailLastUpdatedBy | None = None
    last_updated_on: str | None = None
    lines: list[PurchaseInvoiceCancelDetailLine] | None = None
    object: str | None = None
    origin: str | None = None
    payment_status: str | None = None
    price_tax_inclusive: bool | None = None
    # Null in every record measured, so untyped.
    purchase_order: Any = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseInvoiceNotesNote(Dto):
    """A :class:`PurchaseInvoiceNotes`'s ``note``."""

    attachments: list[PurchaseInvoiceNotesNoteAttachment] | None = None
    content: str | None = None
    created_by: PurchaseInvoiceNotesNoteCreatedBy | None = None
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
    purchase_invoice: PurchaseInvoiceNotesNoteDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchaseInvoiceNotesNoteWatcher] | None = None


class PurchaseInvoiceNoteUpdatedDetail(Dto):
    """A :class:`PurchaseInvoiceNoteUpdated`'s ``purchase_invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseInvoiceNoteUpdatedCreatedBy(Dto):
    """A :class:`PurchaseInvoiceNoteUpdated`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceNoteUpdatedLastUpdatedBy(Dto):
    """A :class:`PurchaseInvoiceNoteUpdated`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class AccountPurchaseInvoicesDataCurrency(Dto):
    """A :class:`AccountPurchaseInvoicesData`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountPurchaseInvoicesDataDetail(Dto):
    """A :class:`AccountPurchaseInvoicesData`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountPurchaseInvoicesDataPurchaseOrder(Dto):
    """A :class:`AccountPurchaseInvoicesData`'s ``purchase_order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class AccountPurchaseInvoicesDataCreatedBy(Dto):
    """A :class:`AccountPurchaseInvoicesData`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class AccountPurchaseInvoicesDataLastUpdatedBy(Dto):
    """A :class:`AccountPurchaseInvoicesData`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class AccountPurchaseInvoicesDataPurchaseCreditNote(Dto):
    """A :class:`AccountPurchaseInvoicesData`'s ``purchase_credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountPurchaseInvoicesDataPurchasePayment(Dto):
    """A :class:`AccountPurchaseInvoicesData`'s ``purchase_payment``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoicesNoteWatcher(Dto):
    """One entry of a :class:`PurchaseInvoicesNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchaseInvoicesNoteCreatedBy(Dto):
    """A :class:`PurchaseInvoicesNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoicesNoteLastUpdatedBy(Dto):
    """A :class:`PurchaseInvoicesNote`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceReadLineItem(Dto):
    """A :class:`PurchaseInvoiceReadLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceLinesRowItem(Dto):
    """A :class:`PurchaseInvoiceLinesRow`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceLineDetailItem(Dto):
    """A :class:`PurchaseInvoiceLineDetail`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoicePurchasePaymentAccount(Dto):
    """A :class:`PurchaseInvoicePurchasePayment`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoicePurchasePaymentCurrency(Dto):
    """A :class:`PurchaseInvoicePurchasePayment`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoicePurchasePaymentPaymentMethodApplication(Dto):
    """One entry of a :class:`PurchaseInvoicePurchasePayment`'s ``payment_method_applications``."""

    amount: str | None = None
    payment_method: PurchaseInvoicePurchasePaymentPaymentMethodApplicationDetail | None = None
    payment_processor: (
        PurchaseInvoicePurchasePaymentPaymentMethodApplicationPaymentProcessor | None
    ) = None
    reference: str | None = None


class PurchaseInvoicePurchasePaymentCreditNoteApplication(Dto):
    """One entry of a :class:`PurchaseInvoicePurchasePayment`'s ``credit_note_applications``."""

    amount: str | None = None
    purchase_credit_note: (
        PurchaseInvoicePurchasePaymentCreditNoteApplicationPurchaseCreditNote | None
    ) = None


class PurchaseInvoicePurchasePaymentPurchaseInvoiceApplication(Dto):
    """One entry of a :class:`PurchaseInvoicePurchasePayment`'s
    ``purchase_invoice_applications``."""

    applied: str | None = None
    due_date: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    purchase_invoice: PurchaseInvoicePurchasePaymentPurchaseInvoiceApplicationDetail | None = None
    total: str | None = None


class PurchaseInvoicePurchasePaymentCreatedBy(Dto):
    """A :class:`PurchaseInvoicePurchasePayment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoicePurchasePaymentLastUpdatedBy(Dto):
    """A :class:`PurchaseInvoicePurchasePayment`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceNoteDetail(Dto):
    """A :class:`PurchaseInvoiceNote`'s ``purchase_invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseInvoiceNoteAttachment(Dto):
    """One entry of a :class:`PurchaseInvoiceNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseInvoiceNoteWatcher(Dto):
    """One entry of a :class:`PurchaseInvoiceNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchaseInvoiceNoteCreatedBy(Dto):
    """A :class:`PurchaseInvoiceNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceNoteLastUpdatedBy(Dto):
    """A :class:`PurchaseInvoiceNote`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceNoteReadDetailPurchaseInvoice(Dto):
    """A :class:`PurchaseInvoiceNoteReadDetail`'s ``purchase_invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseInvoiceNoteReadDetailAttachment(Dto):
    """One entry of a :class:`PurchaseInvoiceNoteReadDetail`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseInvoiceNoteReadDetailWatcher(Dto):
    """One entry of a :class:`PurchaseInvoiceNoteReadDetail`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchaseInvoiceNoteReadDetailCreatedBy(Dto):
    """A :class:`PurchaseInvoiceNoteReadDetail`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceInformationLineItem(Dto):
    """A :class:`PurchaseInvoiceInformationLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceCancelDetailCurrency(Dto):
    """A :class:`PurchaseInvoiceCancelDetail`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceCancelDetailAccount(Dto):
    """A :class:`PurchaseInvoiceCancelDetail`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoiceCancelDetailCreatedBy(Dto):
    """A :class:`PurchaseInvoiceCancelDetail`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceCancelDetailLastUpdatedBy(Dto):
    """A :class:`PurchaseInvoiceCancelDetail`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoiceCancelDetailLine(Dto):
    """One entry of a :class:`PurchaseInvoiceCancelDetail`'s ``lines``."""

    accounting_code: str | None = None
    id: str | None = None
    item: PurchaseInvoiceCancelDetailLineItem | None = None
    object: str | None = None
    quantity: int | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uom: str | None = None
    version: int | None = None
    warehouse: str | None = None


class PurchaseInvoiceCancelDetailKpis(Dto):
    """A :class:`PurchaseInvoiceCancelDetail`'s ``kpis``."""

    credit_applied: str | None = None
    credit_issued: str | None = None
    # Null in every record measured, so untyped.
    deleted_on: Any = None
    # Null in every record measured, so untyped.
    last_amended_on: Any = None
    # Null in every record measured, so untyped.
    last_cancelled_on: Any = None
    # Null in every record measured, so untyped.
    last_payment_date: Any = None
    # Null in every record measured, so untyped.
    last_reactivated_on: Any = None
    object: str | None = None
    outstanding: str | None = None
    overdue: str | None = None
    payment_applied: str | None = None
    # Null in every record measured, so untyped.
    voided_on: Any = None


class PurchaseInvoiceNotesNoteDetail(Dto):
    """A :class:`PurchaseInvoiceNotesNote`'s ``purchase_invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseInvoiceNotesNoteAttachment(Dto):
    """One entry of a :class:`PurchaseInvoiceNotesNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseInvoiceNotesNoteWatcher(Dto):
    """One entry of a :class:`PurchaseInvoiceNotesNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchaseInvoiceNotesNoteCreatedBy(Dto):
    """A :class:`PurchaseInvoiceNotesNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseInvoicePurchasePaymentPaymentMethodApplicationDetail(Dto):
    """A :class:`PurchaseInvoicePurchasePaymentPaymentMethodApplication`'s ``payment_method``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoicePurchasePaymentPaymentMethodApplicationPaymentProcessor(Dto):
    """A :class:`PurchaseInvoicePurchasePaymentPaymentMethodApplication`'s ``payment_processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseInvoicePurchasePaymentCreditNoteApplicationPurchaseCreditNote(Dto):
    """A :class:`PurchaseInvoicePurchasePaymentCreditNoteApplication`'s ``purchase_credit_note``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseInvoicePurchasePaymentPurchaseInvoiceApplicationDetail(Dto):
    """A :class:`PurchaseInvoicePurchasePaymentPurchaseInvoiceApplication`'s
    ``purchase_invoice``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseInvoiceCancelDetailLineItem(Dto):
    """A :class:`PurchaseInvoiceCancelDetailLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
