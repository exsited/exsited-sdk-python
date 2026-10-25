"""Typed views over the express bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto

__all__ = [
    "Express",
    "ExpressCurrency",
    "ExpressTimeZone",
    "ExpressCustomForm",
    "ExpressAccount",
    "ExpressBillingPreferences",
    "ExpressLine",
    "ExpressKpis",
    "ExpressActivityLog",
    "ExpressBillingPreferencesProformaProperties",
    "ExpressLineItem",
    "ExpressLineItemPriceSnapshot",
    "ExpressLineItemPriceTax",
    "ExpressLineItemSaleTaxConfiguration",
    "ExpressLineItemAccountingCode",
    "ExpressLinePreOrderStockDetails",
    "ExpressLineItemPriceSnapshotPricingRule",
    "ExpressLineItemSaleTaxConfigurationTaxCode",
]


class Express(Dto):
    """What ``create_express`` answers, under ``express``."""

    MEASURED_FROM = ("POST /api/{api_version}/express",)

    ENVELOPE_KEY = "express"

    account: ExpressAccount | None = None
    activity_logs: list[ExpressActivityLog] | None = None
    allow_contract: bool | None = None
    # Null in every record measured, so untyped.
    billing_address: Any = None
    billing_preferences: ExpressBillingPreferences | None = None
    billing_start_date: str | None = None
    communication_preferences: list[Any] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: ExpressCurrency | None = None
    custom_attributes: list[Any] | None = None
    custom_form: ExpressCustomForm | None = None
    # Null in every record measured, so untyped.
    customer_purchase_order_id: Any = None
    # Null in every record measured, so untyped.
    description: Any = None
    # Null in every record measured, so untyped.
    discount_profile: Any = None
    display_name: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    invoice_note: Any = None
    kpis: ExpressKpis | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    lines: list[ExpressLine] | None = None
    # Null in every record measured, so untyped.
    manager: Any = None
    name: str | None = None
    next_billing_from_date: str | None = None
    object: str | None = None
    order_start_date: str | None = None
    order_type: str | None = None
    # Null in every record measured, so untyped.
    origin: Any = None
    original_total: str | None = None
    pre_order: bool | None = None
    price_tax_inclusive: bool | None = None
    quote_converted: bool | None = None
    quote_order: bool | None = None
    # Null in every record measured, so untyped.
    referral_account: Any = None
    # Null in every record measured, so untyped.
    sales_rep: Any = None
    # Null in every record measured, so untyped.
    shipping_address: Any = None
    shipping_cost: float | None = None
    shipping_line_items: list[Any] | None = None
    # Null in every record measured, so untyped.
    shipping_profile: Any = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    time_zone: ExpressTimeZone | None = None
    total: str | None = None
    version: int | None = None


class ExpressCurrency(Dto):
    """A :class:`Express`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ExpressTimeZone(Dto):
    """A :class:`Express`'s ``time_zone``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ExpressCustomForm(Dto):
    """A :class:`Express`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ExpressAccount(Dto):
    """A :class:`Express`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ExpressBillingPreferences(Dto):
    """A :class:`Express`'s ``billing_preferences``."""

    billing_period: str | None = None
    communication_profile: str | None = None
    consolidate_invoice: bool | None = None
    fulfillment_mode: str | None = None
    fulfillment_term: str | None = None
    invoice_mode: str | None = None
    invoice_term: str | None = None
    payment_mode: str | None = None
    payment_processor: str | None = None
    payment_term: str | None = None
    payment_term_alignment: str | None = None
    proforma_properties: ExpressBillingPreferencesProformaProperties | None = None


class ExpressLine(Dto):
    """One entry of a :class:`Express`'s ``lines``."""

    charge_item_uuid: str | None = None
    expected_delivery_date: str | None = None
    id: str | None = None
    item: ExpressLineItem | None = None
    item_accounting_code: ExpressLineItemAccountingCode | None = None
    item_charge_type: str | None = None
    item_custom_attributes: list[Any] | None = None
    item_description: str | None = None
    item_invoice_note: str | None = None
    item_order_quantity: int | None = None
    item_price_snapshot: ExpressLineItemPriceSnapshot | None = None
    item_price_tax: ExpressLineItemPriceTax | None = None
    item_sale_tax_configuration: ExpressLineItemSaleTaxConfiguration | None = None
    item_type: str | None = None
    object: str | None = None
    pre_order_stock_details: ExpressLinePreOrderStockDetails | None = None
    shipping_cost: float | None = None
    subtotal: str | None = None
    tax: str | None = None
    tax_exempt_when_sold: bool | None = None
    total: str | None = None
    version: int | None = None


class ExpressKpis(Dto):
    """A :class:`Express`'s ``kpis``."""

    # Null in every record measured, so untyped.
    deleted_at: Any = None
    estimated_total: str | None = None
    # Null in every record measured, so untyped.
    last_cancelled_at: Any = None
    # Null in every record measured, so untyped.
    last_changed_at: Any = None
    # Null in every record measured, so untyped.
    last_invoice_issue_date: Any = None
    last_invoice_total: str | None = None
    # Null in every record measured, so untyped.
    last_reactivated_at: Any = None
    monthly_recurring_revenue: str | None = None
    # Null in every record measured, so untyped.
    next_invoice_issue_date: Any = None
    object: str | None = None
    # Null in every record measured, so untyped.
    start_date: Any = None
    total_collected: str | None = None
    total_due: str | None = None
    total_invoice: int | None = None
    total_outstanding: str | None = None
    total_revenue: str | None = None


class ExpressActivityLog(Dto):
    """One entry of a :class:`Express`'s ``activity_logs``."""

    activity: str | None = None


class ExpressBillingPreferencesProformaProperties(Dto):
    """A :class:`ExpressBillingPreferences`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    # Null in every record measured, so untyped.
    acceptance_term: Any = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class ExpressLineItem(Dto):
    """A :class:`ExpressLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    uuid: str | None = None


class ExpressLineItemPriceSnapshot(Dto):
    """A :class:`ExpressLine`'s ``item_price_snapshot``."""

    pricing_rule: ExpressLineItemPriceSnapshotPricingRule | None = None


class ExpressLineItemPriceTax(Dto):
    """A :class:`ExpressLine`'s ``item_price_tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: float | None = None


class ExpressLineItemSaleTaxConfiguration(Dto):
    """A :class:`ExpressLine`'s ``item_sale_tax_configuration``."""

    sale_price_is_based_on: str | None = None
    tax_code: ExpressLineItemSaleTaxConfigurationTaxCode | None = None


class ExpressLineItemAccountingCode(Dto):
    """A :class:`ExpressLine`'s ``item_accounting_code``."""

    sales_revenue: str | None = None


class ExpressLinePreOrderStockDetails(Dto):
    """A :class:`ExpressLine`'s ``pre_order_stock_details``."""

    pending_reserve: str | None = None
    reserved: str | None = None
    sold: str | None = None


class ExpressLineItemPriceSnapshotPricingRule(Dto):
    """A :class:`ExpressLineItemPriceSnapshot`'s ``pricing_rule``."""

    price: float | None = None
    price_period: str | None = None
    price_type: str | None = None
    pricing_level: str | None = None
    pricing_method: str | None = None
    pricing_schedule: str | None = None
    uom: str | None = None
    uuid: str | None = None
    version: str | None = None
    warehouse: str | None = None


class ExpressLineItemSaleTaxConfigurationTaxCode(Dto):
    """A :class:`ExpressLineItemSaleTaxConfiguration`'s ``tax_code``."""

    code: str | None = None
    link: str | None = None
    rate: str | None = None
    uuid: str | None = None
