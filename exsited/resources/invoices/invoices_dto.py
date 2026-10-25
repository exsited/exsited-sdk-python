"""Typed views over the invoice bodies. The money fields are strings (``"12.00"``);
``version``, ``discount_amount``, ``price_tax_inclusive`` and the two user stamps read as the
instance sends them: an ``int``, a ``float``, a ``bool`` and two user views."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "InvoiceCurrency",
    "InvoiceCustomForm",
    "AccountingCode",
    "LineTax",
    "InvoiceLine",
    "CustomAttribute",
    "InvoiceKpis",
    "LastPayment",
    "InvoiceNote",
    "ItemFulfillment",
    "InvoicePagination",
    "Invoice",
    "InvoiceList",
    "InvoiceNoteList",
    "InvoiceCreate",
    "InvoiceInformationUpdate",
    "InvoiceCancel",
    "InvoicePdf",
    "InvoiceNoteFile",
    "InvoiceAccount",
    "InvoiceOrder",
    "InvoiceCreatedBy",
    "InvoiceLastUpdatedBy",
    "InvoiceActivityLog",
    "InvoicePdfDetail",
    "InvoiceNoteDetail",
    "InvoiceNoteAttachment",
    "InvoiceNoteWatcher",
    "InvoiceNoteCreatedBy",
    "InvoiceLineItem",
    "InvoiceKpisRead",
    "InvoiceLines",
    "InvoiceLineRead",
]


class InvoiceCurrency(Dto):
    """An invoice's currency. Never null."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    code: str | None = None
    href: str | None = None


class InvoiceCustomForm(Dto):
    """The custom form the invoice was created under."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    href: str | None = None


class AccountingCode(Dto):
    """The accounting code on a line. Present on all lines measured."""

    sales_revenue: str | None = None


class LineTax(Dto):
    """The tax block on a line. Present on all lines measured."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    #: A ``float``, 12 of 12 measured. The exception in a family of stringly typed money.
    rate: float | None = None
    amount: str | None = None
    href: str | None = None


class InvoiceLine(Dto):
    """One line of an invoice."""

    object: str | None = None
    id: str | None = None
    version: int | None = None
    #: A ``{object, id, name, href}`` reference to the item.
    item: InvoiceLineItem | None = None
    item_id: str | None = None
    item_uuid: str | None = None
    item_name: str | None = None
    item_uom: str | None = None
    item_warehouse: str | None = None
    #: Not sent on any of the 12 lines measured; it reads ``None`` until a serialised item
    #: appears.
    item_serial_or_batch_number: str | None = None
    item_order_quantity: int | None = None
    item_charge_type: str | None = None
    item_custom_attributes: list[Any] | None = None
    pricing_snapshot_price: float | None = None
    pricing_snapshot_uuid: str | None = None
    #: Set on 46 of 130 - a recurring line only.
    charging_start_date: str | None = None
    charging_end_date: str | None = None
    alternate_charging_start_date: str | None = None
    alternate_charging_end_date: str | None = None
    subtotal: str | None = None
    total: str | None = None
    tax: LineTax | None = None
    accounting_code: AccountingCode | None = None


class CustomAttribute(Dto):
    """One custom attribute."""

    name: str | None = None
    value: Any = None


class InvoiceKpis(Dto):
    """The KPI block. Measured 268 times, never null."""

    credit_applied: str | None = None
    credit_issued: str | None = None
    payment_applied: str | None = None
    last_payment_date: str | None = None
    last_amended_on: str | None = None
    last_cancelled_on: str | None = None
    last_reactivated_on: str | None = None
    deleted_on: str | None = None
    voided_on: str | None = None
    #: String on 198 blocks, int on 70. Untyped for that reason.
    outstanding: Any = None
    #: Int on 252 blocks, string on 16. Untyped for that reason.
    overdue: Any = None


class LastPayment(Dto):
    """The most recent payment against the invoice."""

    uuid: str | None = None
    id: str | None = None
    date: str | None = None
    amount: str | None = None
    created_on: str | None = None


class InvoiceNote(Dto):
    """One note on an invoice."""

    ENVELOPE_KEY = "note"

    object: str | None = None
    id: str | None = None
    href: str | None = None
    content: str | None = None
    #: An ``int``, 10 of 10 measured.
    version: int | None = None
    #: A ``{object, id, name, href}`` reference to the invoice the note is on.
    invoice: InvoiceNoteDetail | None = None
    #: Null on all 10 measured. Untyped rather than guessed at.
    group: Any = None
    #: Null on all 10 measured.
    user: Any = None
    attachments: list[InvoiceNoteAttachment] | None = None
    #: The wire key; ``watcherList`` is never sent.
    watchers: list[InvoiceNoteWatcher] | None = None
    created_on: str | None = None
    #: A ``{object, name}`` user block, 10 of 10 measured.
    created_by: InvoiceNoteCreatedBy | None = None
    #: Null on all 10 measured.
    last_updated_on: Any = None
    #: Null on all 10 measured.
    last_updated_by: Any = None


class ItemFulfillment(Dto):
    """One fulfilment against an invoice, measured 4 times from the v4 collection, not the instance."""

    uuid: str | None = None
    id: str | None = None
    version: str | None = None
    invoice_id: str | None = None
    order_id: str | None = None
    date: str | None = None
    status: str | None = None
    note: str | None = None
    tracking_number: str | None = None
    created_on: str | None = None
    created_by: str | None = None
    last_updated_on: str | None = None
    last_updated_by: str | None = None
    fulfillments: list[Any] | None = None


#: The paging block on an invoice listing: the shared type, which covers both shapes v4 serves.
InvoicePagination = Pagination


class Invoice(Dto):
    """One invoice."""

    ENVELOPE_KEY = "invoice"

    id: str | None = None
    uuid: str | None = None
    version: int | None = None
    status: str | None = None
    type: str | None = None
    origin: str | None = None
    payment_status: str | None = None

    account_id: str | None = None
    #: Present on 16 of 286 - the listing carries it, the detail read does not.
    account_name: str | None = None
    order_id: str | None = None
    customer_purchase_order_id: str | None = None
    invoice_note: str | None = None

    issue_date: str | None = None
    due_date: str | None = None
    alternate_issue_date: str | None = None
    alternate_due_date: str | None = None
    #: The four billing dates arrive on 50 of 286 - a recurring invoice only.
    billing_start_date: str | None = None
    billing_end_date: str | None = None
    alternate_billing_start_date: str | None = None
    alternate_billing_end_date: str | None = None

    # Money is text on the wire, except ``discount_amount``.
    subtotal: str | None = None
    tax: str | None = None
    tax_total: str | None = None
    total: str | None = None
    due: str | None = None
    paid: str | None = None
    discount_amount: float | None = None
    shipping_cost: str | None = None
    credit_applied: str | None = None
    credit_issued: str | None = None
    payment_applied: str | None = None
    outstanding: str | None = None
    price_tax_inclusive: bool | None = None
    recurring_rate_count: str | None = None
    usage_rate_count: str | None = None

    currency: InvoiceCurrency | None = None
    custom_form: InvoiceCustomForm | None = None
    kpis: InvoiceKpis | None = None
    #: Null on 202 of 270 - an unpaid invoice has none.
    last_payment: LastPayment | None = None

    created_on: str | None = None
    created_by: InvoiceCreatedBy | None = None
    last_updated_on: str | None = None
    last_updated_by: InvoiceLastUpdatedBy | None = None

    lines: list[InvoiceLine] | None = None
    custom_attributes: list[CustomAttribute] | None = None
    custom_objects: list[Any] | None = None
    activity_logs: list[InvoiceActivityLog] | None = None
    notes: list[InvoiceNote] | None = None
    item_fulfillments: list[ItemFulfillment] | None = None
    return_merchandise_authorisations: list[Any] | None = None
    account: InvoiceAccount | None = None
    object: str | None = None
    order: InvoiceOrder | None = None


class InvoiceList(Dto):
    """One page of ``Invoice`` records, under ``data``."""

    data: list[Invoice] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class InvoiceNoteList(Dto):
    """A listing of an invoice's notes, under the ordinary list envelope."""

    data: list[InvoiceNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class InvoiceCreate(Dto):
    """The body ``create_invoice`` takes, under an ``invoice`` envelope."""

    ENVELOPE_KEY = "invoice"

    account_id: str | None = None
    issue_date: str | None = None
    due_date: str | None = None
    currency: str | None = None
    lines: list[Any] | None = None
    name: str | None = None
    display_name: str | None = None
    description: str | None = None
    invoice_note: str | None = None
    origin: str | None = None
    #: The write spelling: a real boolean. Reads back as ``"true"``.
    price_tax_inclusive: bool | None = None


class InvoiceInformationUpdate(Dto):
    """The body ``update_invoice_information`` takes."""

    ENVELOPE_KEY = "invoice"

    invoice_note: str | None = None
    customer_purchase_order_id: str | None = None


class InvoiceCancel(Dto):
    """The body ``cancel_invoice`` takes, if any."""

    ENVELOPE_KEY = "invoice"

    effective_date: str | None = None


class InvoicePdf(Dto):
    """What ``get_invoice_pdf`` answers, under ``invoice``."""

    ENVELOPE_KEY = "invoice"

    pdf: InvoicePdfDetail | None = None


class InvoiceNoteFile(Dto):
    """What ``get_invoice_note_file`` answers, under ``file``."""

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class InvoiceAccount(Dto):
    """A :class:`Invoice`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class InvoiceOrder(Dto):
    """A :class:`Invoice`'s ``order``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class InvoiceCreatedBy(Dto):
    """A :class:`Invoice`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class InvoiceLastUpdatedBy(Dto):
    """A :class:`Invoice`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class InvoiceActivityLog(Dto):
    """One entry of a :class:`Invoice`'s ``activity_logs``."""

    activity: str | None = None


class InvoicePdfDetail(Dto):
    """A :class:`InvoicePdf`'s ``pdf``."""

    download_url: str | None = None
    file_size: int | None = None
    id: str | None = None
    object: str | None = None
    preview_url: str | None = None


class InvoiceNoteDetail(Dto):
    """A :class:`InvoiceNote`'s ``invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class InvoiceNoteAttachment(Dto):
    """One entry of a :class:`InvoiceNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class InvoiceNoteWatcher(Dto):
    """One entry of a :class:`InvoiceNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class InvoiceNoteCreatedBy(Dto):
    """A :class:`InvoiceNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class InvoiceLineItem(Dto):
    """A :class:`InvoiceLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class InvoiceKpisRead(InvoiceKpis):
    """What ``get_invoice_kpis`` answers, under ``invoice_kpis``: the block an invoice carries as
    ``kpis``, with an ``object`` beside it. Measured on 2 invoices."""

    ENVELOPE_KEY = "invoice_kpis"

    object: str | None = None


class InvoiceLines(Dto):
    """What ``get_invoice_lines`` answers, under ``invoice``: its ``object`` and ``lines``, and
    nothing else of the invoice."""

    ENVELOPE_KEY = "invoice"

    object: str | None = None
    lines: list[InvoiceLine] | None = None


class InvoiceLineRead(Dto):
    """What ``get_invoice_line`` answers, under ``invoice``: its ``object`` and one ``line``."""

    ENVELOPE_KEY = "invoice"

    object: str | None = None
    line: InvoiceLine | None = None
