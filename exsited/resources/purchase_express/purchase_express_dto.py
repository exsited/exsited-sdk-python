"""Typed views over the purchase express bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto

__all__ = [
    "PurchaseExpress",
    "PurchaseExpressAccount",
    "PurchaseExpressCreatedBy",
    "PurchaseExpressCurrency",
    "PurchaseExpressCustomForm",
    "PurchaseExpressKpis",
]


class PurchaseExpress(Dto):
    """What ``create_purchase_express`` answers, under ``purchase_express``."""


    ENVELOPE_KEY = "purchase_express"

    account: PurchaseExpressAccount | None = None
    activity_logs: list[Any] | None = None
    bill_total: str | None = None
    code: str | None = None
    created_by: PurchaseExpressCreatedBy | None = None
    created_on: str | None = None
    currency: PurchaseExpressCurrency | None = None
    custom_attributes: list[Any] | None = None
    custom_form: PurchaseExpressCustomForm | None = None
    due_date: str | None = None
    due_total: str | None = None
    expected_completion_date: Any = None
    href: str | None = None
    id: str | None = None
    is_price_tax_inclusive: Any = None
    issue_date: str | None = None
    kpis: PurchaseExpressKpis | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    operational_status: str | None = None
    origin: Any = None
    paid_amount: str | None = None
    purchase_order_note: Any = None
    sale_order: Any = None
    status: str | None = None
    subtotal: str | None = None
    supplier_invoice_id: Any = None
    tax_total: str | None = None
    total: str | None = None
    version: int | None = None
    warehouse: Any = None


class PurchaseExpressAccount(Dto):
    """A :class:`PurchaseExpress`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseExpressCreatedBy(Dto):
    """A :class:`PurchaseExpress`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseExpressCurrency(Dto):
    """A :class:`PurchaseExpress`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseExpressCustomForm(Dto):
    """A :class:`PurchaseExpress`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseExpressKpis(Dto):
    """A :class:`PurchaseExpress`'s ``kpis``."""

    estimated_total: str | None = None
    issue_date: Any = None
    last_cancelled_on: Any = None
    last_changed_on: Any = None
    last_deleted_on: Any = None
    last_invoice_issue_date: Any = None
    last_invoice_total: str | None = None
    last_reactivated_on: Any = None
    object: str | None = None
    total_expense: str | None = None
    total_outstanding: str | None = None
    total_overdue: str | None = None
    total_purchase_invoice: int | None = None
