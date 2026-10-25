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

    MEASURED_FROM = ("POST /api/{api_version}/purchase_express",)

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
    # Null in every record measured, so untyped.
    expected_completion_date: Any = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    is_price_tax_inclusive: Any = None
    issue_date: str | None = None
    kpis: PurchaseExpressKpis | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    operational_status: str | None = None
    # Null in every record measured, so untyped.
    origin: Any = None
    paid_amount: str | None = None
    # Null in every record measured, so untyped.
    purchase_order_note: Any = None
    # Null in every record measured, so untyped.
    sale_order: Any = None
    status: str | None = None
    subtotal: str | None = None
    # Null in every record measured, so untyped.
    supplier_invoice_id: Any = None
    tax_total: str | None = None
    total: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
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
