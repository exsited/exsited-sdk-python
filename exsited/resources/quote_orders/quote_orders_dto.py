"""Typed views over the quote order bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "QuoteOrderInvoiceList",
    "QuoteOrderInvoice",
    "QuoteOrderInvoiceAccount",
    "QuoteOrderInvoiceCreatedBy",
    "QuoteOrderInvoiceCurrency",
    "QuoteOrderInvoiceCustomForm",
    "QuoteOrderInvoiceOrder",
]


class QuoteOrderInvoiceList(Dto):
    """One page of a quote's invoices, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/quote_orders/{quote_order_id}/invoices",)

    data: list[QuoteOrderInvoice] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class QuoteOrderInvoice(Dto):
    """One entry of a :class:`QuoteOrderInvoiceList`'s ``data``."""

    account: QuoteOrderInvoiceAccount | None = None
    alternate_billing_end_date: str | None = None
    alternate_billing_start_date: str | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    billing_end_date: str | None = None
    billing_start_date: str | None = None
    created_by: QuoteOrderInvoiceCreatedBy | None = None
    created_on: str | None = None
    currency: QuoteOrderInvoiceCurrency | None = None
    custom_form: QuoteOrderInvoiceCustomForm | None = None
    # Null in every record measured, so untyped.
    customer_purchase_order_id: Any = None
    discount_amount: float | None = None
    due: str | None = None
    due_date: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    invoice_note: Any = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_payment: Any = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    order: QuoteOrderInvoiceOrder | None = None
    # Null in every record measured, so untyped.
    origin: Any = None
    paid: str | None = None
    payment_status: str | None = None
    price_tax_inclusive: bool | None = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    tax_total: str | None = None
    total: str | None = None
    type: str | None = None
    version: int | None = None


class QuoteOrderInvoiceAccount(Dto):
    """A :class:`QuoteOrderInvoice`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class QuoteOrderInvoiceCreatedBy(Dto):
    """A :class:`QuoteOrderInvoice`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class QuoteOrderInvoiceCurrency(Dto):
    """A :class:`QuoteOrderInvoice`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class QuoteOrderInvoiceCustomForm(Dto):
    """A :class:`QuoteOrderInvoice`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class QuoteOrderInvoiceOrder(Dto):
    """A :class:`QuoteOrderInvoice`'s ``order``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
