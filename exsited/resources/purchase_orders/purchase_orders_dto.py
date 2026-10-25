"""Typed views over the purchase order bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "PurchaseOrderLine",
    "PurchaseOrderLineList",
    "PurchaseOrder",
    "PurchaseOrderList",
    "PurchaseOrderPurchaseInvoice",
    "PurchaseOrderPurchaseInvoiceList",
    "PurchaseOrderPurchasePayment",
    "PurchaseOrderPurchasePaymentList",
    "PurchaseOrdersNote",
    "PurchaseOrdersNoteList",
    "PurchaseOrderRead",
    "PurchaseOrderUpdated",
    "PurchaseOrders",
    "PurchaseOrderInformation",
    "AccountPurchaseOrders",
    "PurchaseOrderNotes",
    "PurchaseOrderNote",
    "PurchaseOrderLineRead",
    "PurchaseOrderNoteFile",
    "PurchaseOrderNotesView",
    "PurchaseOrderPurchaseInvoices",
    "PurchaseOrderReadAccount",
    "PurchaseOrderReadCurrency",
    "PurchaseOrderReadCustomAttribute",
    "PurchaseOrderReadCustomForm",
    "PurchaseOrderReadKpis",
    "PurchaseOrderReadCreatedBy",
    "PurchaseOrderReadLastUpdatedBy",
    "PurchaseOrderInformationCustomAttribute",
    "PurchaseOrderInformationCustomForm",
    "PurchaseOrderInformationCreatedBy",
    "PurchaseOrderInformationLastUpdatedBy",
    "PurchaseOrderLineReadDetail",
    "PurchaseOrderNotesData",
    "PurchaseOrderNoteDetail",
    "PurchaseOrderNoteData",
    "PurchaseOrdersAccount",
    "PurchaseOrdersCurrency",
    "PurchaseOrdersCustomForm",
    "PurchaseOrdersKpis",
    "PurchaseOrdersCreatedBy",
    "PurchaseOrderUpdatedAccount",
    "PurchaseOrderUpdatedCurrency",
    "PurchaseOrderUpdatedCustomForm",
    "PurchaseOrderUpdatedKpis",
    "PurchaseOrderUpdatedCreatedBy",
    "PurchaseOrderUpdatedLastUpdatedBy",
    "PurchaseOrderNotesViewDetail",
    "PurchaseOrderNotesViewAttachment",
    "PurchaseOrderNotesViewWatcher",
    "PurchaseOrderNotesViewCreatedBy",
    "PurchaseOrderPurchaseInvoicesCurrency",
    "PurchaseOrderPurchaseInvoicesAccount",
    "PurchaseOrderPurchaseInvoicesDetail",
    "PurchaseOrderPurchaseInvoicesCreatedBy",
    "PurchaseOrderPurchaseInvoicesLine",
    "PurchaseOrderPurchaseInvoicesKpis",
    "PurchaseOrderAccount",
    "PurchaseOrderCurrency",
    "PurchaseOrderCustomForm",
    "PurchaseOrderCreatedBy",
    "PurchaseOrderLastUpdatedBy",
    "PurchaseOrdersNoteWatcher",
    "PurchaseOrdersNoteCreatedBy",
    "PurchaseOrderLineItem",
    "PurchaseOrderLineUom",
    "PurchaseOrderLineWarehouse",
    "PurchaseOrderLineTax",
    "PurchaseOrderLineItemPriceSnapshot",
    "PurchaseOrderLineItemPriceTax",
    "PurchaseOrderLineItemPurchaseTaxConfiguration",
    "PurchaseOrderLineItemAccountingCode",
    "PurchaseOrderLineItemPurchaseAccountingCode",
    "PurchaseOrderLineReadDetailItem",
    "PurchaseOrderLineReadDetailUom",
    "PurchaseOrderLineReadDetailWarehouse",
    "PurchaseOrderLineReadDetailTax",
    "PurchaseOrderLineReadDetailItemPriceSnapshot",
    "PurchaseOrderLineReadDetailItemPriceTax",
    "PurchaseOrderLineReadDetailItemPurchaseTaxConfiguration",
    "PurchaseOrderLineReadDetailItemAccountingCode",
    "PurchaseOrderLineReadDetailItemPurchaseAccountingCode",
    "PurchaseOrderPurchaseInvoiceCurrency",
    "PurchaseOrderPurchaseInvoiceAccount",
    "PurchaseOrderPurchaseInvoiceDetail",
    "PurchaseOrderPurchaseInvoiceCreatedBy",
    "PurchaseOrderPurchaseInvoiceLastUpdatedBy",
    "PurchaseOrderPurchasePaymentAccount",
    "PurchaseOrderPurchasePaymentCurrency",
    "PurchaseOrderPurchasePaymentPaymentMethodApplication",
    "PurchaseOrderPurchasePaymentCreditNoteApplication",
    "PurchaseOrderPurchasePaymentPurchaseInvoiceApplication",
    "PurchaseOrderPurchasePaymentCreatedBy",
    "PurchaseOrderPurchasePaymentLastUpdatedBy",
    "PurchaseOrderNotesDataDetail",
    "PurchaseOrderNotesDataAttachment",
    "PurchaseOrderNotesDataWatcher",
    "PurchaseOrderNotesDataCreatedBy",
    "PurchaseOrderNoteDetailPurchaseOrder",
    "PurchaseOrderNoteDetailAttachment",
    "PurchaseOrderNoteDetailWatcher",
    "PurchaseOrderNoteDetailCreatedBy",
    "PurchaseOrderPurchaseInvoicesLineItem",
    "PurchaseOrderLineItemPriceSnapshotPricingRule",
    "PurchaseOrderLineItemPurchaseTaxConfigurationTaxCode",
    "PurchaseOrderLineReadDetailItemPriceSnapshotPricingRule",
    "PurchaseOrderLineReadDetailItemPurchaseTaxConfigurationTaxCode",
    "PurchaseOrderPurchasePaymentPaymentMethodApplicationDetail",
    "PurchaseOrderPurchasePaymentPaymentMethodApplicationPaymentProcessor",
    "PurchaseOrderPurchasePaymentCreditNoteApplicationPurchaseCreditNote",
    "PurchaseOrderPurchasePaymentPurchaseInvoiceApplicationDetail",
    "PurchaseOrderKpis",
]


class PurchaseOrderLine(Dto):
    """The purchase order line body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders/{purchase_order_id}/lines",)

    created_on: str | None = None
    flat_discount: float | None = None
    href: str | None = None
    id: str | None = None
    is_price_tax_inclusive: bool | None = None
    is_tax_exempt: bool | None = None
    item: PurchaseOrderLineItem | None = None
    item_accounting_code: PurchaseOrderLineItemAccountingCode | None = None
    item_discount_amount: float | None = None
    item_expected_completion_date: str | None = None
    # Null in every record measured, so untyped.
    item_invoice_note: Any = None
    item_price_snapshot: PurchaseOrderLineItemPriceSnapshot | None = None
    item_price_tax: PurchaseOrderLineItemPriceTax | None = None
    item_price_tax_exempt: bool | None = None
    item_purchase_accounting_code: PurchaseOrderLineItemPurchaseAccountingCode | None = None
    item_purchase_tax_configuration: PurchaseOrderLineItemPurchaseTaxConfiguration | None = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    price: float | None = None
    # Null in every record measured, so untyped.
    purchase_line_note: Any = None
    quantity: int | None = None
    sort_index: int | None = None
    status: str | None = None
    subtotal: str | None = None
    tax: PurchaseOrderLineTax | None = None
    tax_total: str | None = None
    total: str | None = None
    uom: PurchaseOrderLineUom | None = None
    version: int | None = None
    warehouse: PurchaseOrderLineWarehouse | None = None


class PurchaseOrderLineList(Dto):
    """One page of ``PurchaseOrderLine`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders/{purchase_order_id}/lines",)

    data: list[PurchaseOrderLine] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseOrder(Dto):
    """The purchase order body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders",)

    account: PurchaseOrderAccount | None = None
    bill_total: str | None = None
    code: str | None = None
    created_by: PurchaseOrderCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseOrderCurrency | None = None
    custom_attributes: list[Any] | None = None
    custom_form: PurchaseOrderCustomForm | None = None
    due_date: str | None = None
    due_total: str | None = None
    expected_completion_date: str | None = None
    href: str | None = None
    id: str | None = None
    is_price_tax_inclusive: bool | None = None
    issue_date: str | None = None
    last_updated_by: PurchaseOrderLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    operational_status: str | None = None
    origin: str | None = None
    paid_amount: str | None = None
    purchase_order_note: str | None = None
    # Null in every record measured, so untyped.
    sale_order: Any = None
    status: str | None = None
    subtotal: str | None = None
    supplier_invoice_id: str | None = None
    tax_total: str | None = None
    total: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    warehouse: Any = None


class PurchaseOrderList(Dto):
    """One page of ``PurchaseOrder`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders",)

    data: list[PurchaseOrder] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseOrderPurchaseInvoice(Dto):
    """The purchase order purchase invoice body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_invoices",
    )

    account: PurchaseOrderPurchaseInvoiceAccount | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    created_by: PurchaseOrderPurchaseInvoiceCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseOrderPurchaseInvoiceCurrency | None = None
    # Null in every record measured, so untyped.
    custom_form: Any = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    last_updated_by: PurchaseOrderPurchaseInvoiceLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    payment_status: str | None = None
    price_tax_inclusive: bool | None = None
    purchase_order: PurchaseOrderPurchaseInvoiceDetail | None = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseOrderPurchaseInvoiceList(Dto):
    """One page of ``PurchaseOrderPurchaseInvoice`` records, under ``data``; paged by offset."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_invoices",
    )

    data: list[PurchaseOrderPurchaseInvoice] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseOrderPurchasePayment(Dto):
    """The purchase order purchase payment body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_payments",
    )

    account: PurchaseOrderPurchasePaymentAccount | None = None
    code: str | None = None
    created_by: PurchaseOrderPurchasePaymentCreatedBy | None = None
    created_on: str | None = None
    credit_note_applications: list[PurchaseOrderPurchasePaymentCreditNoteApplication] | None = None
    credit_note_total: str | None = None
    currency: PurchaseOrderPurchasePaymentCurrency | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: PurchaseOrderPurchasePaymentLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    origin: str | None = None
    paid_total: str | None = None
    payment_date: str | None = None
    payment_method_applications: (
        list[PurchaseOrderPurchasePaymentPaymentMethodApplication] | None
    ) = None
    payment_note: str | None = None
    # Null in every record measured, so untyped.
    payment_reference: Any = None
    purchase_invoice_applications: (
        list[PurchaseOrderPurchasePaymentPurchaseInvoiceApplication] | None
    ) = None
    status: str | None = None
    version: int | None = None


class PurchaseOrderPurchasePaymentList(Dto):
    """One page of ``PurchaseOrderPurchasePayment`` records, under ``data``; paged by offset."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_payments",
    )

    data: list[PurchaseOrderPurchasePayment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseOrdersNote(Dto):
    """The purchase orders note body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders/notes",)

    attachments: list[Any] | None = None
    content: str | None = None
    created_by: PurchaseOrdersNoteCreatedBy | None = None
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
    watchers: list[PurchaseOrdersNoteWatcher] | None = None


class PurchaseOrdersNoteList(Dto):
    """One page of ``PurchaseOrdersNote`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders/notes",)

    data: list[PurchaseOrdersNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseOrderRead(Dto):
    """The purchase order read body, under ``purchase_order``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}",
        "POST /api/{api_version}/purchase_orders/{purchase_order_id}/change",
        "POST /api/{api_version}/purchase_orders/{purchase_order_id}/cancel",
        "POST /api/{api_version}/purchase_orders/{purchase_order_id}/reactivate",
    )

    ENVELOPE_KEY = "purchase_order"

    account: PurchaseOrderReadAccount | None = None
    activity_logs: list[Any] | None = None
    bill_total: str | None = None
    code: str | None = None
    created_by: PurchaseOrderReadCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseOrderReadCurrency | None = None
    custom_attributes: list[PurchaseOrderReadCustomAttribute] | None = None
    custom_form: PurchaseOrderReadCustomForm | None = None
    due_date: str | None = None
    due_total: str | None = None
    expected_completion_date: str | None = None
    href: str | None = None
    id: str | None = None
    is_price_tax_inclusive: bool | None = None
    issue_date: str | None = None
    kpis: PurchaseOrderReadKpis | None = None
    last_updated_by: PurchaseOrderReadLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    operational_status: str | None = None
    origin: str | None = None
    paid_amount: str | None = None
    purchase_order_note: str | None = None
    # Null in every record measured, so untyped.
    sale_order: Any = None
    status: str | None = None
    subtotal: str | None = None
    supplier_invoice_id: str | None = None
    tax_total: str | None = None
    total: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    warehouse: Any = None


class PurchaseOrderUpdated(Dto):
    """The purchase order updated body, under ``purchase_order``."""

    MEASURED_FROM = ("PATCH /api/{api_version}/purchase_orders/{purchase_order_id}",)

    ENVELOPE_KEY = "purchase_order"

    account: PurchaseOrderUpdatedAccount | None = None
    account_id: str | None = None
    activity_logs: list[Any] | None = None
    bill_total: str | None = None
    code: str | None = None
    created_by: PurchaseOrderUpdatedCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseOrderUpdatedCurrency | None = None
    custom_attributes: list[Any] | None = None
    custom_form: PurchaseOrderUpdatedCustomForm | None = None
    custom_objects: list[Any] | None = None
    due_date: str | None = None
    due_total: str | None = None
    expected_completion_date: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    is_price_tax_inclusive: Any = None
    issue_date: str | None = None
    kpis: PurchaseOrderUpdatedKpis | None = None
    last_updated_by: PurchaseOrderUpdatedLastUpdatedBy | None = None
    last_updated_on: str | None = None
    lines: list[Any] | None = None
    object: str | None = None
    operational_status: str | None = None
    origin: str | None = None
    paid_amount: str | None = None
    price_tax_inclusive: str | None = None
    purchase_order_note: str | None = None
    # Null in every record measured, so untyped.
    sale_order: Any = None
    sale_order_id: str | None = None
    status: str | None = None
    subtotal: str | None = None
    supplier_invoice_id: str | None = None
    tax: str | None = None
    tax_total: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    warehouse: Any = None


class PurchaseOrders(Dto):
    """The purchase orders body, under ``purchase_order``."""

    MEASURED_FROM = ("POST /api/{api_version}/purchase_orders",)

    ENVELOPE_KEY = "purchase_order"

    account: PurchaseOrdersAccount | None = None
    account_id: str | None = None
    activity_logs: list[Any] | None = None
    bill_total: str | None = None
    code: str | None = None
    created_by: PurchaseOrdersCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseOrdersCurrency | None = None
    custom_attributes: list[Any] | None = None
    custom_form: PurchaseOrdersCustomForm | None = None
    custom_objects: list[Any] | None = None
    due_date: str | None = None
    due_total: str | None = None
    expected_completion_date: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    is_price_tax_inclusive: Any = None
    issue_date: str | None = None
    kpis: PurchaseOrdersKpis | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    lines: list[Any] | None = None
    object: str | None = None
    operational_status: str | None = None
    origin: str | None = None
    paid_amount: str | None = None
    price_tax_inclusive: str | None = None
    purchase_order_note: str | None = None
    # Null in every record measured, so untyped.
    sale_order: Any = None
    status: str | None = None
    subtotal: str | None = None
    supplier_invoice_id: str | None = None
    tax: str | None = None
    tax_total: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    warehouse: Any = None


class PurchaseOrderInformation(Dto):
    """The purchase order information body, under ``purchase_order``."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders/{purchase_order_id}/information",)

    ENVELOPE_KEY = "purchase_order"

    bill_total: str | None = None
    code: str | None = None
    created_by: PurchaseOrderInformationCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: list[PurchaseOrderInformationCustomAttribute] | None = None
    custom_form: PurchaseOrderInformationCustomForm | None = None
    due_date: str | None = None
    due_total: str | None = None
    expected_completion_date: str | None = None
    href: str | None = None
    id: str | None = None
    is_price_tax_inclusive: bool | None = None
    issue_date: str | None = None
    last_updated_by: PurchaseOrderInformationLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    operational_status: str | None = None
    origin: str | None = None
    paid_amount: str | None = None
    purchase_order_note: str | None = None
    status: str | None = None
    subtotal: str | None = None
    supplier_invoice_id: str | None = None
    tax_total: str | None = None
    total: str | None = None
    version: int | None = None


class AccountPurchaseOrders(Dto):
    """The account purchase orders body."""

    MEASURED_FROM = ("GET /api/{api_version}/accounts/{account_id}/purchase_orders",)

    data: list[PurchaseOrder] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseOrderNotes(Dto):
    """The purchase order notes body, under ``purchase_order``."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders/{purchase_order_id}/notes",)

    ENVELOPE_KEY = "purchase_order"

    data: list[PurchaseOrderNotesData] | None = None
    notes: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseOrderNote(Dto):
    """The purchase order note body, under ``purchase_order``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}",
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}/files",
    )

    ENVELOPE_KEY = "purchase_order"

    data: list[PurchaseOrderNoteData] | None = None
    note: PurchaseOrderNoteDetail | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class PurchaseOrderLineRead(Dto):
    """The purchase order line read body, under ``purchase_order``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/lines/{purchase_order_line_uuid}",
    )

    ENVELOPE_KEY = "purchase_order"

    line: dict[str, Any] | None = None
    purchase_order_line: PurchaseOrderLineReadDetail | None = None


class PurchaseOrderNoteFile(Dto):
    """What ``get_purchase_order_note_file`` answers, under ``file``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/purchase_orders/{purchase_order_id}/notes/{purchase_order_note_id}/files/{purchase_order_file_id}",
    )

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseOrderNotesView(Dto):
    """What ``create_purchase_order_note`` answers, under ``note``."""

    MEASURED_FROM = ("POST /api/{api_version}/purchase_orders/{purchase_order_id}/notes",)

    ENVELOPE_KEY = "note"

    attachments: list[PurchaseOrderNotesViewAttachment] | None = None
    content: str | None = None
    created_by: PurchaseOrderNotesViewCreatedBy | None = None
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
    purchase_order: PurchaseOrderNotesViewDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchaseOrderNotesViewWatcher] | None = None


class PurchaseOrderPurchaseInvoices(Dto):
    """What ``create_purchase_order_purchase_invoice`` answers, under ``purchase_invoice``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/purchase_orders/{purchase_order_id}/purchase_invoices",
    )

    ENVELOPE_KEY = "purchase_invoice"

    account: PurchaseOrderPurchaseInvoicesAccount | None = None
    activity_logs: list[Any] | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    created_by: PurchaseOrderPurchaseInvoicesCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseOrderPurchaseInvoicesCurrency | None = None
    custom_attributes: list[Any] | None = None
    # Null in every record measured, so untyped.
    custom_form: Any = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    kpis: PurchaseOrderPurchaseInvoicesKpis | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    lines: list[PurchaseOrderPurchaseInvoicesLine] | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    origin: Any = None
    payment_status: str | None = None
    price_tax_inclusive: bool | None = None
    purchase_order: PurchaseOrderPurchaseInvoicesDetail | None = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseOrderReadAccount(Dto):
    """A :class:`PurchaseOrderRead`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderReadCurrency(Dto):
    """A :class:`PurchaseOrderRead`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderReadCustomAttribute(Dto):
    """One entry of a :class:`PurchaseOrderRead`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class PurchaseOrderReadCustomForm(Dto):
    """A :class:`PurchaseOrderRead`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderReadKpis(Dto):
    """A :class:`PurchaseOrderRead`'s ``kpis``."""

    estimated_total: str | None = None
    # Null in every record measured, so untyped.
    issue_date: Any = None
    # Null in every record measured, so untyped.
    last_cancelled_on: Any = None
    # Null in every record measured, so untyped.
    last_changed_on: Any = None
    # Null in every record measured, so untyped.
    last_deleted_on: Any = None
    # Null in every record measured, so untyped.
    last_invoice_issue_date: Any = None
    last_invoice_total: str | None = None
    # Null in every record measured, so untyped.
    last_reactivated_on: Any = None
    object: str | None = None
    total_expense: str | None = None
    total_outstanding: str | None = None
    total_overdue: str | None = None
    total_purchase_invoice: int | None = None


class PurchaseOrderReadCreatedBy(Dto):
    """A :class:`PurchaseOrderRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderReadLastUpdatedBy(Dto):
    """A :class:`PurchaseOrderRead`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderInformationCustomAttribute(Dto):
    """One entry of a :class:`PurchaseOrderInformation`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class PurchaseOrderInformationCustomForm(Dto):
    """A :class:`PurchaseOrderInformation`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderInformationCreatedBy(Dto):
    """A :class:`PurchaseOrderInformation`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderInformationLastUpdatedBy(Dto):
    """A :class:`PurchaseOrderInformation`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderLineReadDetail(Dto):
    """A :class:`PurchaseOrderLineRead`'s ``purchase_order_line``."""

    created_on: str | None = None
    flat_discount: float | None = None
    href: str | None = None
    id: str | None = None
    is_price_tax_inclusive: bool | None = None
    is_tax_exempt: bool | None = None
    item: PurchaseOrderLineReadDetailItem | None = None
    item_accounting_code: PurchaseOrderLineReadDetailItemAccountingCode | None = None
    item_discount_amount: float | None = None
    item_expected_completion_date: str | None = None
    # Null in every record measured, so untyped.
    item_invoice_note: Any = None
    item_price_snapshot: PurchaseOrderLineReadDetailItemPriceSnapshot | None = None
    item_price_tax: PurchaseOrderLineReadDetailItemPriceTax | None = None
    item_price_tax_exempt: bool | None = None
    item_purchase_accounting_code: PurchaseOrderLineReadDetailItemPurchaseAccountingCode | None = (
        None
    )
    item_purchase_tax_configuration: (
        PurchaseOrderLineReadDetailItemPurchaseTaxConfiguration | None
    ) = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    price: float | None = None
    # Null in every record measured, so untyped.
    purchase_line_note: Any = None
    quantity: int | None = None
    sort_index: int | None = None
    status: str | None = None
    subtotal: str | None = None
    tax: PurchaseOrderLineReadDetailTax | None = None
    tax_total: str | None = None
    total: str | None = None
    uom: PurchaseOrderLineReadDetailUom | None = None
    version: int | None = None
    warehouse: PurchaseOrderLineReadDetailWarehouse | None = None


class PurchaseOrderNotesData(Dto):
    """One entry of a :class:`PurchaseOrderNotes`'s ``data``."""

    attachments: list[PurchaseOrderNotesDataAttachment] | None = None
    content: str | None = None
    created_by: PurchaseOrderNotesDataCreatedBy | None = None
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
    purchase_order: PurchaseOrderNotesDataDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchaseOrderNotesDataWatcher] | None = None


class PurchaseOrderNoteDetail(Dto):
    """A :class:`PurchaseOrderNote`'s ``note``."""

    attachments: list[PurchaseOrderNoteDetailAttachment] | None = None
    content: str | None = None
    created_by: PurchaseOrderNoteDetailCreatedBy | None = None
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
    purchase_order: PurchaseOrderNoteDetailPurchaseOrder | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[PurchaseOrderNoteDetailWatcher] | None = None


class PurchaseOrderNoteData(Dto):
    """One entry of a :class:`PurchaseOrderNote`'s ``data``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseOrdersAccount(Dto):
    """A :class:`PurchaseOrders`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrdersCurrency(Dto):
    """A :class:`PurchaseOrders`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrdersCustomForm(Dto):
    """A :class:`PurchaseOrders`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrdersKpis(Dto):
    """A :class:`PurchaseOrders`'s ``kpis``."""

    estimated_total: str | None = None
    # Null in every record measured, so untyped.
    issue_date: Any = None
    # Null in every record measured, so untyped.
    last_cancelled_on: Any = None
    # Null in every record measured, so untyped.
    last_changed_on: Any = None
    # Null in every record measured, so untyped.
    last_deleted_on: Any = None
    # Null in every record measured, so untyped.
    last_invoice_issue_date: Any = None
    last_invoice_total: str | None = None
    # Null in every record measured, so untyped.
    last_reactivated_on: Any = None
    object: str | None = None
    total_expense: str | None = None
    total_outstanding: str | None = None
    total_overdue: str | None = None
    total_purchase_invoice: int | None = None


class PurchaseOrdersCreatedBy(Dto):
    """A :class:`PurchaseOrders`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderUpdatedAccount(Dto):
    """A :class:`PurchaseOrderUpdated`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderUpdatedCurrency(Dto):
    """A :class:`PurchaseOrderUpdated`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderUpdatedCustomForm(Dto):
    """A :class:`PurchaseOrderUpdated`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderUpdatedKpis(Dto):
    """A :class:`PurchaseOrderUpdated`'s ``kpis``."""

    estimated_total: str | None = None
    # Null in every record measured, so untyped.
    issue_date: Any = None
    # Null in every record measured, so untyped.
    last_cancelled_on: Any = None
    # Null in every record measured, so untyped.
    last_changed_on: Any = None
    # Null in every record measured, so untyped.
    last_deleted_on: Any = None
    # Null in every record measured, so untyped.
    last_invoice_issue_date: Any = None
    last_invoice_total: str | None = None
    # Null in every record measured, so untyped.
    last_reactivated_on: Any = None
    object: str | None = None
    total_expense: str | None = None
    total_outstanding: str | None = None
    total_overdue: str | None = None
    total_purchase_invoice: int | None = None


class PurchaseOrderUpdatedCreatedBy(Dto):
    """A :class:`PurchaseOrderUpdated`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderUpdatedLastUpdatedBy(Dto):
    """A :class:`PurchaseOrderUpdated`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderNotesViewDetail(Dto):
    """A :class:`PurchaseOrderNotesView`'s ``purchase_order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseOrderNotesViewAttachment(Dto):
    """One entry of a :class:`PurchaseOrderNotesView`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseOrderNotesViewWatcher(Dto):
    """One entry of a :class:`PurchaseOrderNotesView`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchaseOrderNotesViewCreatedBy(Dto):
    """A :class:`PurchaseOrderNotesView`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoicesCurrency(Dto):
    """A :class:`PurchaseOrderPurchaseInvoices`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoicesAccount(Dto):
    """A :class:`PurchaseOrderPurchaseInvoices`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoicesDetail(Dto):
    """A :class:`PurchaseOrderPurchaseInvoices`'s ``purchase_order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoicesCreatedBy(Dto):
    """A :class:`PurchaseOrderPurchaseInvoices`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoicesLine(Dto):
    """One entry of a :class:`PurchaseOrderPurchaseInvoices`'s ``lines``."""

    accounting_code: str | None = None
    id: str | None = None
    item: PurchaseOrderPurchaseInvoicesLineItem | None = None
    object: str | None = None
    quantity: int | None = None
    subtotal: str | None = None
    tax: str | None = None
    total: str | None = None
    uom: str | None = None
    version: int | None = None
    warehouse: str | None = None


class PurchaseOrderPurchaseInvoicesKpis(Dto):
    """A :class:`PurchaseOrderPurchaseInvoices`'s ``kpis``."""

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


class PurchaseOrderAccount(Dto):
    """A :class:`PurchaseOrder`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderCurrency(Dto):
    """A :class:`PurchaseOrder`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderCustomForm(Dto):
    """A :class:`PurchaseOrder`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderCreatedBy(Dto):
    """A :class:`PurchaseOrder`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderLastUpdatedBy(Dto):
    """A :class:`PurchaseOrder`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrdersNoteWatcher(Dto):
    """One entry of a :class:`PurchaseOrdersNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchaseOrdersNoteCreatedBy(Dto):
    """A :class:`PurchaseOrdersNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderLineItem(Dto):
    """A :class:`PurchaseOrderLine`'s ``item``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineUom(Dto):
    """A :class:`PurchaseOrderLine`'s ``uom``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineWarehouse(Dto):
    """A :class:`PurchaseOrderLine`'s ``warehouse``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineTax(Dto):
    """A :class:`PurchaseOrderLine`'s ``tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineItemPriceSnapshot(Dto):
    """A :class:`PurchaseOrderLine`'s ``item_price_snapshot``."""

    pricing_rule: PurchaseOrderLineItemPriceSnapshotPricingRule | None = None


class PurchaseOrderLineItemPriceTax(Dto):
    """A :class:`PurchaseOrderLine`'s ``item_price_tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: float | None = None


class PurchaseOrderLineItemPurchaseTaxConfiguration(Dto):
    """A :class:`PurchaseOrderLine`'s ``item_purchase_tax_configuration``."""

    purchase_price_is_tax_inclusive: bool | None = None
    tax_code: PurchaseOrderLineItemPurchaseTaxConfigurationTaxCode | None = None
    tax_exempt_when_purchase: bool | None = None


class PurchaseOrderLineItemAccountingCode(Dto):
    """A :class:`PurchaseOrderLine`'s ``item_accounting_code``."""

    cost_of_goods_sold: str | None = None


class PurchaseOrderLineItemPurchaseAccountingCode(Dto):
    """A :class:`PurchaseOrderLine`'s ``item_purchase_accounting_code``."""

    cost_of_goods_sold: str | None = None


class PurchaseOrderLineReadDetailItem(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``item``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineReadDetailUom(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``uom``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineReadDetailWarehouse(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``warehouse``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineReadDetailTax(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineReadDetailItemPriceSnapshot(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``item_price_snapshot``."""

    pricing_rule: PurchaseOrderLineReadDetailItemPriceSnapshotPricingRule | None = None


class PurchaseOrderLineReadDetailItemPriceTax(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``item_price_tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: float | None = None


class PurchaseOrderLineReadDetailItemPurchaseTaxConfiguration(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``item_purchase_tax_configuration``."""

    purchase_price_is_tax_inclusive: bool | None = None
    tax_code: PurchaseOrderLineReadDetailItemPurchaseTaxConfigurationTaxCode | None = None
    tax_exempt_when_purchase: bool | None = None


class PurchaseOrderLineReadDetailItemAccountingCode(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``item_accounting_code``."""

    cost_of_goods_sold: str | None = None


class PurchaseOrderLineReadDetailItemPurchaseAccountingCode(Dto):
    """A :class:`PurchaseOrderLineReadDetail`'s ``item_purchase_accounting_code``."""

    cost_of_goods_sold: str | None = None


class PurchaseOrderPurchaseInvoiceCurrency(Dto):
    """A :class:`PurchaseOrderPurchaseInvoice`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoiceAccount(Dto):
    """A :class:`PurchaseOrderPurchaseInvoice`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoiceDetail(Dto):
    """A :class:`PurchaseOrderPurchaseInvoice`'s ``purchase_order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoiceCreatedBy(Dto):
    """A :class:`PurchaseOrderPurchaseInvoice`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoiceLastUpdatedBy(Dto):
    """A :class:`PurchaseOrderPurchaseInvoice`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchasePaymentAccount(Dto):
    """A :class:`PurchaseOrderPurchasePayment`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchasePaymentCurrency(Dto):
    """A :class:`PurchaseOrderPurchasePayment`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchasePaymentPaymentMethodApplication(Dto):
    """One entry of a :class:`PurchaseOrderPurchasePayment`'s ``payment_method_applications``."""

    amount: str | None = None
    payment_method: PurchaseOrderPurchasePaymentPaymentMethodApplicationDetail | None = None
    payment_processor: (
        PurchaseOrderPurchasePaymentPaymentMethodApplicationPaymentProcessor | None
    ) = None
    reference: str | None = None


class PurchaseOrderPurchasePaymentCreditNoteApplication(Dto):
    """One entry of a :class:`PurchaseOrderPurchasePayment`'s ``credit_note_applications``."""

    amount: str | None = None
    purchase_credit_note: (
        PurchaseOrderPurchasePaymentCreditNoteApplicationPurchaseCreditNote | None
    ) = None


class PurchaseOrderPurchasePaymentPurchaseInvoiceApplication(Dto):
    """One entry of a :class:`PurchaseOrderPurchasePayment`'s ``purchase_invoice_applications``."""

    applied: str | None = None
    due_date: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    purchase_invoice: PurchaseOrderPurchasePaymentPurchaseInvoiceApplicationDetail | None = None
    total: str | None = None


class PurchaseOrderPurchasePaymentCreatedBy(Dto):
    """A :class:`PurchaseOrderPurchasePayment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchasePaymentLastUpdatedBy(Dto):
    """A :class:`PurchaseOrderPurchasePayment`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderNotesDataDetail(Dto):
    """A :class:`PurchaseOrderNotesData`'s ``purchase_order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseOrderNotesDataAttachment(Dto):
    """One entry of a :class:`PurchaseOrderNotesData`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseOrderNotesDataWatcher(Dto):
    """One entry of a :class:`PurchaseOrderNotesData`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchaseOrderNotesDataCreatedBy(Dto):
    """A :class:`PurchaseOrderNotesData`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderNoteDetailPurchaseOrder(Dto):
    """A :class:`PurchaseOrderNoteDetail`'s ``purchase_order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseOrderNoteDetailAttachment(Dto):
    """One entry of a :class:`PurchaseOrderNoteDetail`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class PurchaseOrderNoteDetailWatcher(Dto):
    """One entry of a :class:`PurchaseOrderNoteDetail`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class PurchaseOrderNoteDetailCreatedBy(Dto):
    """A :class:`PurchaseOrderNoteDetail`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchaseInvoicesLineItem(Dto):
    """A :class:`PurchaseOrderPurchaseInvoicesLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderLineItemPriceSnapshotPricingRule(Dto):
    """A :class:`PurchaseOrderLineItemPriceSnapshot`'s ``pricing_rule``."""

    price: float | None = None
    price_type: str | None = None
    pricing_version: str | None = None
    uom: str | None = None
    uuid: str | None = None
    version: str | None = None


class PurchaseOrderLineItemPurchaseTaxConfigurationTaxCode(Dto):
    """A :class:`PurchaseOrderLineItemPurchaseTaxConfiguration`'s ``tax_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: str | None = None


class PurchaseOrderLineReadDetailItemPriceSnapshotPricingRule(Dto):
    """A :class:`PurchaseOrderLineReadDetailItemPriceSnapshot`'s ``pricing_rule``."""

    price: float | None = None
    price_type: str | None = None
    pricing_version: str | None = None
    uom: str | None = None
    uuid: str | None = None
    version: str | None = None


class PurchaseOrderLineReadDetailItemPurchaseTaxConfigurationTaxCode(Dto):
    """A :class:`PurchaseOrderLineReadDetailItemPurchaseTaxConfiguration`'s ``tax_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: str | None = None


class PurchaseOrderPurchasePaymentPaymentMethodApplicationDetail(Dto):
    """A :class:`PurchaseOrderPurchasePaymentPaymentMethodApplication`'s ``payment_method``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchasePaymentPaymentMethodApplicationPaymentProcessor(Dto):
    """A :class:`PurchaseOrderPurchasePaymentPaymentMethodApplication`'s ``payment_processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseOrderPurchasePaymentCreditNoteApplicationPurchaseCreditNote(Dto):
    """A :class:`PurchaseOrderPurchasePaymentCreditNoteApplication`'s ``purchase_credit_note``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseOrderPurchasePaymentPurchaseInvoiceApplicationDetail(Dto):
    """A :class:`PurchaseOrderPurchasePaymentPurchaseInvoiceApplication`'s ``purchase_invoice``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class PurchaseOrderKpis(PurchaseOrderReadKpis):
    """What ``get_purchase_order_kpis`` answers, under ``purchase_order_kpis``: the block a purchase
    order carries as ``kpis``. Measured on 2 purchase orders."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_orders/{purchase_order_id}/kpis",)

    ENVELOPE_KEY = "purchase_order_kpis"
