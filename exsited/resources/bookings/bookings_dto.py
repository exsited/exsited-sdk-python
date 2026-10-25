"""Typed views over the booking bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Booking",
    "BookingList",
    "BookingById",
    "BookingByIdCurrency",
    "BookingByIdTimeZone",
    "BookingByIdCustomForm",
    "BookingByIdManager",
    "BookingByIdAccount",
    "BookingByIdBillingAddress",
    "BookingByIdCommunicationPreference",
    "BookingByIdBillingPreferences",
    "BookingByIdCustomAttribute",
    "BookingByIdLine",
    "BookingByIdKpis",
    "BookingCurrency",
    "BookingTimeZone",
    "BookingCustomForm",
    "BookingManager",
    "BookingSalesRep",
    "BookingShippingProfile",
    "BookingAccount",
    "BookingReferralAccount",
    "BookingDiscountProfile",
    "BookingBillingAddress",
    "BookingShippingAddress",
    "BookingCommunicationPreference",
    "BookingBillingPreferences",
    "BookingContractProperties",
    "BookingByIdBillingPreferencesProformaProperties",
    "BookingByIdLineItem",
    "BookingByIdLineItemPriceSnapshot",
    "BookingByIdLineItemPriceTax",
    "BookingByIdLineItemSaleTaxConfiguration",
    "BookingByIdLineItemAccountingCode",
    "BookingByIdLinePreOrderStockDetails",
    "BookingByIdLineItemProperties",
    "BookingBillingPreferencesProformaProperties",
    "BookingByIdLineItemPriceSnapshotPricingRule",
    "BookingByIdLineItemSaleTaxConfigurationTaxCode",
    "BookingNoteList",
    "BookingBillingPreferencesView",
    "BookingLine",
    "BookingCustomObjectList",
    "BookingCustomObject",
    "BookingInvoiceList",
    "BookingItemFulfillment",
    "BookingKpis",
    "BookingPaymentMethods",
    "BookingPaymentMethod",
    "BookingPaymentList",
    "BookingPaymentView",
    "BookingPdf",
    "BookingQuotePartialInvoices",
    "BookingNote",
    "BookingNoteAttachment",
    "BookingNoteCreatedBy",
    "BookingNoteLastUpdatedBy",
    "BookingNoteWatcher",
    "BookingBillingPreferencesDetail",
    "BookingBillingPreferencesDetailProformaProperties",
    "BookingLineItem",
    "BookingLineItemAccountingCode",
    "BookingLineItemPriceSnapshot",
    "BookingLineItemPriceSnapshotPricingRule",
    "BookingLineItemPriceTax",
    "BookingLineItemSaleTaxConfiguration",
    "BookingLineItemSaleTaxConfigurationTaxCode",
    "BookingLinePreOrderStockDetails",
    "BookingLineItemProperties",
    "BookingCustomObjectEntry",
    "BookingInvoice",
    "BookingInvoiceAccount",
    "BookingInvoiceCreatedBy",
    "BookingInvoiceCurrency",
    "BookingInvoiceCustomForm",
    "BookingInvoiceOrder",
    "BookingItemFulfillmentAccount",
    "BookingItemFulfillmentCreatedBy",
    "BookingItemFulfillmentFulfillment",
    "BookingItemFulfillmentFulfillmentItem",
    "BookingItemFulfillmentInvoice",
    "BookingItemFulfillmentLastUpdatedBy",
    "BookingPaymentMethodsPaymentMethod",
    "BookingPaymentMethodsPaymentMethodProcessor",
    "BookingPaymentMethodPaymentMethod",
    "BookingPaymentMethodPaymentMethodProcessor",
    "BookingPayment",
    "BookingPaymentAccount",
    "BookingPaymentCreatedBy",
    "BookingPaymentInvoice",
    "BookingPaymentPaymentApplied",
    "BookingPaymentViewAccount",
    "BookingPaymentViewCreatedBy",
    "BookingPaymentViewInvoice",
    "BookingPaymentViewPaymentApplied",
    "BookingPdfPdf",
]


class Booking(Dto):
    """The booking body."""

    MEASURED_FROM = ("GET /api/{api_version}/booking",)

    account: BookingAccount | None = None
    allow_contract: bool | None = None
    billing_address: BookingBillingAddress | None = None
    billing_preferences: BookingBillingPreferences | None = None
    billing_start_date: str | None = None
    billing_start_day_of_month: str | None = None
    communication_preferences: list[BookingCommunicationPreference] | None = None
    contract_properties: BookingContractProperties | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: BookingCurrency | None = None
    custom_form: BookingCustomForm | None = None
    customer_purchase_order_id: str | None = None
    description: str | None = None
    discount_profile: BookingDiscountProfile | None = None
    display_name: str | None = None
    id: str | None = None
    invoice_note: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    manager: BookingManager | None = None
    name: str | None = None
    next_billing_from_date: str | None = None
    next_billing_from_date_utc: str | None = None
    object: str | None = None
    order_start_date: str | None = None
    order_type: str | None = None
    origin: str | None = None
    original_total: str | None = None
    pre_order: bool | None = None
    price_tax_inclusive: bool | None = None
    quote_converted: bool | None = None
    quote_order: bool | None = None
    referral_account: BookingReferralAccount | None = None
    sales_rep: BookingSalesRep | None = None
    shipping_address: BookingShippingAddress | None = None
    shipping_cost: float | None = None
    shipping_profile: BookingShippingProfile | None = None
    status: str | None = None
    time_zone: BookingTimeZone | None = None
    version: int | None = None


class BookingList(Dto):
    """One page of ``Booking`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking",)

    data: list[Booking] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class BookingById(Dto):
    """The booking by id body, under ``order``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/booking/{booking_id}",
        "GET /api/{api_version}/booking/{booking_id}/information",
        "GET /api/{api_version}/booking/{booking_id}/lines",
        "PATCH /api/{api_version}/booking/{booking_id}/information",
        "PATCH /api/{api_version}/booking/{booking_id}/billing_preferences",
        "PATCH /api/{api_version}/booking/{booking_id}/lines/{line_uuid}",
        "PATCH /api/{api_version}/booking/{booking_id}/lines/{line_uuid}/billing_preferences",
    )

    ENVELOPE_KEY = "order"

    account: BookingByIdAccount | None = None
    # Empty in every record measured; sent by the writes, not by the reads.
    activity_logs: list[Any] | None = None
    allow_contract: bool | None = None
    billing_address: BookingByIdBillingAddress | None = None
    billing_preferences: BookingByIdBillingPreferences | None = None
    billing_start_date: str | None = None
    communication_preferences: list[BookingByIdCommunicationPreference] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: BookingByIdCurrency | None = None
    custom_attributes: list[BookingByIdCustomAttribute] | None = None
    custom_form: BookingByIdCustomForm | None = None
    customer_purchase_order_id: str | None = None
    description: str | None = None
    # Null in every record measured, so untyped.
    discount_profile: Any = None
    display_name: str | None = None
    id: str | None = None
    invoice_note: str | None = None
    kpis: BookingByIdKpis | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    lines: list[BookingByIdLine] | None = None
    manager: BookingByIdManager | None = None
    name: str | None = None
    next_billing_from_date: str | None = None
    next_billing_from_date_utc: str | None = None
    object: str | None = None
    order_start_date: str | None = None
    order_type: str | None = None
    origin: str | None = None
    # Null in every record measured, so untyped.
    original_total: Any = None
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
    time_zone: BookingByIdTimeZone | None = None
    total: str | None = None
    version: int | None = None


class BookingByIdCurrency(Dto):
    """A :class:`BookingById`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingByIdTimeZone(Dto):
    """A :class:`BookingById`'s ``time_zone``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingByIdCustomForm(Dto):
    """A :class:`BookingById`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingByIdManager(Dto):
    """A :class:`BookingById`'s ``manager``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingByIdAccount(Dto):
    """A :class:`BookingById`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingByIdBillingAddress(Dto):
    """A :class:`BookingById`'s ``billing_address``."""

    address_line_1: str | None = None
    address_line_2: str | None = None
    # Null in every record measured, so untyped.
    address_line_3: Any = None
    # Null in every record measured, so untyped.
    address_line_4: Any = None
    # Null in every record measured, so untyped.
    address_line_5: Any = None
    city: str | None = None
    country: str | None = None
    name: str | None = None
    postal_code: str | None = None
    state: str | None = None


class BookingByIdCommunicationPreference(Dto):
    """One entry of a :class:`BookingById`'s ``communication_preferences``."""

    channel: str | None = None
    enabled: bool | None = None


class BookingByIdBillingPreferences(Dto):
    """A :class:`BookingById`'s ``billing_preferences``."""

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
    proforma_properties: BookingByIdBillingPreferencesProformaProperties | None = None


class BookingByIdCustomAttribute(Dto):
    """One entry of a :class:`BookingById`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: Any = None


class BookingByIdLine(Dto):
    """One entry of a :class:`BookingById`'s ``lines``."""

    charge_item_uuid: str | None = None
    expected_delivery_date: str | None = None
    id: str | None = None
    item: BookingByIdLineItem | None = None
    item_accounting_code: BookingByIdLineItemAccountingCode | None = None
    item_charge_type: str | None = None
    item_custom_attributes: list[Any] | None = None
    item_description: str | None = None
    item_invoice_note: str | None = None
    item_order_quantity: int | None = None
    item_price_snapshot: BookingByIdLineItemPriceSnapshot | None = None
    item_price_tax: BookingByIdLineItemPriceTax | None = None
    item_properties: BookingByIdLineItemProperties | None = None
    item_sale_tax_configuration: BookingByIdLineItemSaleTaxConfiguration | None = None
    item_type: str | None = None
    object: str | None = None
    pre_order_stock_details: BookingByIdLinePreOrderStockDetails | None = None
    shipping_cost: float | None = None
    subtotal: str | None = None
    tax: str | None = None
    tax_exempt_when_sold: bool | None = None
    total: str | None = None
    version: int | None = None


class BookingByIdKpis(Dto):
    """A :class:`BookingById`'s ``kpis``."""

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


class BookingCurrency(Dto):
    """A :class:`Booking`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingTimeZone(Dto):
    """A :class:`Booking`'s ``time_zone``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingCustomForm(Dto):
    """A :class:`Booking`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingManager(Dto):
    """A :class:`Booking`'s ``manager``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingSalesRep(Dto):
    """A :class:`Booking`'s ``sales_rep``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingShippingProfile(Dto):
    """A :class:`Booking`'s ``shipping_profile``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingAccount(Dto):
    """A :class:`Booking`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingReferralAccount(Dto):
    """A :class:`Booking`'s ``referral_account``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class BookingDiscountProfile(Dto):
    """A :class:`Booking`'s ``discount_profile``."""

    amount: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    redemption_code: str | None = None
    type: str | None = None


class BookingBillingAddress(Dto):
    """A :class:`Booking`'s ``billing_address``."""

    address_line_1: str | None = None
    address_line_2: str | None = None
    address_line_3: str | None = None
    address_line_4: str | None = None
    address_line_5: str | None = None
    city: str | None = None
    country: str | None = None
    name: str | None = None
    postal_code: str | None = None
    state: str | None = None


class BookingShippingAddress(Dto):
    """A :class:`Booking`'s ``shipping_address``."""

    address_line_1: str | None = None
    address_line_2: str | None = None
    address_line_3: str | None = None
    address_line_4: str | None = None
    address_line_5: str | None = None
    city: str | None = None
    country: str | None = None
    name: str | None = None
    postal_code: str | None = None
    state: str | None = None


class BookingCommunicationPreference(Dto):
    """One entry of a :class:`Booking`'s ``communication_preferences``."""

    channel: str | None = None
    enabled: bool | None = None


class BookingBillingPreferences(Dto):
    """A :class:`Booking`'s ``billing_preferences``."""

    billing_period: str | None = None
    communication_profile: str | None = None
    consolidate_invoice: bool | None = None
    consolidate_key: str | None = None
    fulfillment_mode: str | None = None
    fulfillment_term: str | None = None
    invoice_mode: str | None = None
    invoice_term: str | None = None
    payment_mode: str | None = None
    payment_processor: str | None = None
    payment_term: str | None = None
    payment_term_alignment: str | None = None
    proforma_properties: BookingBillingPreferencesProformaProperties | None = None


class BookingContractProperties(Dto):
    """A :class:`Booking`'s ``contract_properties``."""

    allow_downgrade: bool | None = None
    allow_downgrade_charge: bool | None = None
    allow_early_termination: bool | None = None
    allow_postponement: bool | None = None
    allow_trial: bool | None = None
    allow_upgrade: bool | None = None
    auto_renewal_ends_on: str | None = None
    auto_renewal_require_customer_acceptance: bool | None = None
    auto_renewal_term: str | None = None
    downgrade_charge_fixed: str | None = None
    downgrade_charge_type: str | None = None
    initial_contract_term: str | None = None
    period_before_downgrade: str | None = None
    renew_automatically: str | None = None
    require_customer_acceptance: bool | None = None
    requires_payment_method: bool | None = None
    termination_accounting_code: str | None = None
    termination_notice_period: str | None = None


class BookingByIdBillingPreferencesProformaProperties(Dto):
    """A :class:`BookingByIdBillingPreferences`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    # Null in every record measured, so untyped.
    acceptance_term: Any = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class BookingByIdLineItem(Dto):
    """A :class:`BookingByIdLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    uuid: str | None = None


class BookingByIdLineItemPriceSnapshot(Dto):
    """A :class:`BookingByIdLine`'s ``item_price_snapshot``."""

    pricing_rule: BookingByIdLineItemPriceSnapshotPricingRule | None = None


class BookingByIdLineItemPriceTax(Dto):
    """A :class:`BookingByIdLine`'s ``item_price_tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: float | None = None


class BookingByIdLineItemSaleTaxConfiguration(Dto):
    """A :class:`BookingByIdLine`'s ``item_sale_tax_configuration``."""

    sale_price_is_based_on: str | None = None
    tax_code: BookingByIdLineItemSaleTaxConfigurationTaxCode | None = None


class BookingByIdLineItemAccountingCode(Dto):
    """A :class:`BookingByIdLine`'s ``item_accounting_code``."""

    sales_revenue: Any = None


class BookingByIdLinePreOrderStockDetails(Dto):
    """A :class:`BookingByIdLine`'s ``pre_order_stock_details``."""

    pending_reserve: str | None = None
    reserved: str | None = None
    sold: str | None = None


class BookingByIdLineItemProperties(Dto):
    """A :class:`BookingByIdLine`'s ``item_properties``."""

    billing_mode: str | None = None
    charging_and_billing_alignment: str | None = None
    charging_start_date: str | None = None
    pro_rata_partial_pricing_period: str | None = None


class BookingBillingPreferencesProformaProperties(Dto):
    """A :class:`BookingBillingPreferences`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    # Null in every record measured, so untyped.
    acceptance_term: Any = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class BookingByIdLineItemPriceSnapshotPricingRule(Dto):
    """A :class:`BookingByIdLineItemPriceSnapshot`'s ``pricing_rule``."""

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


class BookingByIdLineItemSaleTaxConfigurationTaxCode(Dto):
    """A :class:`BookingByIdLineItemSaleTaxConfiguration`'s ``tax_code``."""

    code: str | None = None
    link: str | None = None
    rate: str | float | None = None
    uuid: str | None = None


class BookingNoteList(Dto):
    """One page of every order's notes, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/notes",)

    data: list[BookingNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class BookingBillingPreferencesView(Dto):
    """What ``get_booking_billing_preferences`` answers, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/billing_preferences",)

    ENVELOPE_KEY = "order"

    billing_preferences: BookingBillingPreferencesDetail | None = None
    object: str | None = None


class BookingCustomObjectList(Dto):
    """One page of the custom objects orders use, under ``data``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/booking/{booking_id}/custom_objects",
        "GET /api/{api_version}/booking/{booking_id}/custom_objects_instances",
    )

    data: list[BookingCustomObjectEntry] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class BookingCustomObject(Dto):
    """One custom object with the booking's instances of it, under ``custom_object``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/booking/{booking_id}/custom_objects/{custom_object_id}",
        "GET /api/{api_version}/booking/{booking_id}/custom_objects_instances/{custom_object_id}",
    )

    ENVELOPE_KEY = "custom_object"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    custom_component: Any = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    instances: list[Any] | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    pagination: Pagination | None = None
    relation: str | None = None
    use_in: str | None = None


class BookingInvoiceList(Dto):
    """One page of a booking's invoices, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/invoices",)

    data: list[BookingInvoice] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class BookingItemFulfillment(Dto):
    """What ``get_booking_item_fulfillment`` answers, under ``item_fulfillment``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/booking/{booking_id}/item_fulfillments/{fulfillment_id}",
    )

    ENVELOPE_KEY = "item_fulfillment"

    account: BookingItemFulfillmentAccount | None = None
    code: str | None = None
    created_by: BookingItemFulfillmentCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: dict[str, Any] | None = None
    # Null in every record measured, so untyped.
    delivery_status: Any = None
    fulfillment_completed: bool | None = None
    fulfillment_date: str | None = None
    # Null in every record measured, so untyped.
    fulfillment_note: Any = None
    fulfillment_status: str | None = None
    fulfillments: list[BookingItemFulfillmentFulfillment] | None = None
    href: str | None = None
    id: str | None = None
    invoice: BookingItemFulfillmentInvoice | None = None
    last_updated_by: BookingItemFulfillmentLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    order: Any = None
    status: str | None = None
    tracking_number: str | None = None
    version: int | None = None


class BookingKpis(Dto):
    """What ``get_booking_kpis`` answers, under ``order_kpis``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/kpis",)

    ENVELOPE_KEY = "order_kpis"

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


class BookingPaymentMethods(Dto):
    """What ``get_booking_payment_methods`` answers, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/payment_methods",)

    ENVELOPE_KEY = "order"

    payment_methods: list[BookingPaymentMethodsPaymentMethod] | None = None


class BookingPaymentMethod(Dto):
    """What ``get_booking_payment_method`` answers, under ``order``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/booking/{booking_id}/payment_methods/{payment_method_ref}",
    )

    ENVELOPE_KEY = "order"

    payment_method: BookingPaymentMethodPaymentMethod | None = None


class BookingPaymentList(Dto):
    """One page of a booking's payments, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/payments",)

    data: list[BookingPayment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class BookingPaymentView(Dto):
    """What ``get_booking_payment`` answers, under ``payment``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/payments/{payment_id}",)

    ENVELOPE_KEY = "payment"

    account: BookingPaymentViewAccount | None = None
    created_by: BookingPaymentViewCreatedBy | None = None
    created_on: str | None = None
    credit_applied: list[Any] | None = None
    custom_attributes: list[Any] | None = None
    gift_certificate_applied: list[Any] | None = None
    id: str | None = None
    invoices: list[BookingPaymentViewInvoice] | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    # Null in every record measured, so untyped.
    origin: Any = None
    payment_applied: list[BookingPaymentViewPaymentApplied] | None = None
    payment_note: str | None = None
    reconcile_status: str | None = None
    status: str | None = None
    version: int | None = None


class BookingPdf(Dto):
    """What ``get_booking_pdf`` answers, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/pdf",)

    ENVELOPE_KEY = "order"

    pdf: BookingPdfPdf | None = None


class BookingQuotePartialInvoices(Dto):
    """What ``get_booking_quote_partial_invoices`` answers, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/quote_partial_invoices",)

    ENVELOPE_KEY = "order"

    partial_invoices: list[Any] | None = None


class BookingNote(Dto):
    """One entry of a :class:`BookingNoteList`'s ``data``."""

    attachments: list[BookingNoteAttachment] | None = None
    content: str | None = None
    created_by: BookingNoteCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: BookingNoteLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[BookingNoteWatcher] | None = None


class BookingNoteAttachment(Dto):
    """One entry of a :class:`BookingNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class BookingNoteCreatedBy(Dto):
    """A :class:`BookingNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class BookingNoteLastUpdatedBy(Dto):
    """A :class:`BookingNote`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class BookingNoteWatcher(Dto):
    """One entry of a :class:`BookingNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class BookingBillingPreferencesDetail(Dto):
    """A :class:`BookingBillingPreferencesView`'s ``billing_preferences``."""

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
    proforma_properties: BookingBillingPreferencesDetailProformaProperties | None = None


class BookingBillingPreferencesDetailProformaProperties(Dto):
    """A :class:`BookingBillingPreferencesDetail`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    # Null in every record measured, so untyped.
    acceptance_term: Any = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class BookingCustomObjectEntry(Dto):
    """One entry of a :class:`BookingCustomObjectList`'s ``data``."""

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    custom_component: Any = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    relation: str | None = None
    use_in: str | None = None


class BookingInvoice(Dto):
    """One entry of a :class:`BookingInvoiceList`'s ``data``."""

    account: BookingInvoiceAccount | None = None
    alternate_billing_end_date: str | None = None
    alternate_billing_start_date: str | None = None
    alternate_due_date: str | None = None
    alternate_issue_date: str | None = None
    billing_end_date: str | None = None
    billing_start_date: str | None = None
    created_by: BookingInvoiceCreatedBy | None = None
    created_on: str | None = None
    currency: BookingInvoiceCurrency | None = None
    custom_form: BookingInvoiceCustomForm | None = None
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
    order: BookingInvoiceOrder | None = None
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


class BookingInvoiceAccount(Dto):
    """A :class:`BookingInvoice`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingInvoiceCreatedBy(Dto):
    """A :class:`BookingInvoice`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class BookingInvoiceCurrency(Dto):
    """A :class:`BookingInvoice`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingInvoiceCustomForm(Dto):
    """A :class:`BookingInvoice`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingInvoiceOrder(Dto):
    """A :class:`BookingInvoice`'s ``order``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingItemFulfillmentAccount(Dto):
    """A :class:`BookingItemFulfillment`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingItemFulfillmentCreatedBy(Dto):
    """A :class:`BookingItemFulfillment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class BookingItemFulfillmentFulfillment(Dto):
    """One entry of a :class:`BookingItemFulfillment`'s ``fulfillments``."""

    fulfillment_index: int | None = None
    fulfillment_qty: float | None = None
    fulfillment_sent_qty: float | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    inventory_tracking: Any = None
    item: BookingItemFulfillmentFulfillmentItem | None = None
    object: str | None = None
    pending_return: float | None = None
    # Null in every record measured, so untyped.
    returned: Any = None
    serving_status: str | None = None
    # Null in every record measured, so untyped.
    uom: Any = None
    # Null in every record measured, so untyped.
    uom_precision: Any = None


class BookingItemFulfillmentFulfillmentItem(Dto):
    """A :class:`BookingItemFulfillmentFulfillment`'s ``item``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingItemFulfillmentInvoice(Dto):
    """A :class:`BookingItemFulfillment`'s ``invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class BookingItemFulfillmentLastUpdatedBy(Dto):
    """A :class:`BookingItemFulfillment`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class BookingPaymentMethodsPaymentMethod(Dto):
    """One entry of a :class:`BookingPaymentMethods`'s ``payment_methods``."""

    created_by: str | None = None
    created_on: str | None = None
    default: bool | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    last_used_at: str | None = None
    object: str | None = None
    payment_count: int | None = None
    processor: BookingPaymentMethodsPaymentMethodProcessor | None = None
    processor_type: str | None = None
    reference: str | None = None
    restricted_to_orders: bool | None = None
    specified_order_ids: str | None = None
    status: str | None = None
    version: int | None = None


class BookingPaymentMethodsPaymentMethodProcessor(Dto):
    """A :class:`BookingPaymentMethodsPaymentMethod`'s ``processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingPaymentMethodPaymentMethod(Dto):
    """A :class:`BookingPaymentMethod`'s ``payment_method``."""

    created_by: str | None = None
    created_on: str | None = None
    default: bool | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    last_used_at: str | None = None
    object: str | None = None
    payment_count: int | None = None
    processor: BookingPaymentMethodPaymentMethodProcessor | None = None
    processor_type: str | None = None
    reference: str | None = None
    restricted_to_orders: bool | None = None
    specified_order_ids: str | None = None
    status: str | None = None
    version: int | None = None


class BookingPaymentMethodPaymentMethodProcessor(Dto):
    """A :class:`BookingPaymentMethodPaymentMethod`'s ``processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingPayment(Dto):
    """One entry of a :class:`BookingPaymentList`'s ``data``."""

    account: BookingPaymentAccount | None = None
    created_by: BookingPaymentCreatedBy | None = None
    created_on: str | None = None
    credit_applied: list[Any] | None = None
    gift_certificate_applied: list[Any] | None = None
    id: str | None = None
    invoices: list[BookingPaymentInvoice] | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    # Null in every record measured, so untyped.
    origin: Any = None
    payment_applied: list[BookingPaymentPaymentApplied] | None = None
    payment_note: str | None = None
    reconcile_status: str | None = None
    status: str | None = None
    version: int | None = None


class BookingPaymentAccount(Dto):
    """A :class:`BookingPayment`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingPaymentCreatedBy(Dto):
    """A :class:`BookingPayment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class BookingPaymentInvoice(Dto):
    """One entry of a :class:`BookingPayment`'s ``invoices``."""

    applied: str | None = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    total: str | None = None


class BookingPaymentPaymentApplied(Dto):
    """One entry of a :class:`BookingPayment`'s ``payment_applied``."""

    amount: str | None = None
    # Null in every record measured, so untyped.
    gateway_response: Any = None
    method: str | None = None
    processor: str | None = None
    reference: str | None = None


class BookingPaymentViewAccount(Dto):
    """A :class:`BookingPaymentView`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class BookingPaymentViewCreatedBy(Dto):
    """A :class:`BookingPaymentView`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class BookingPaymentViewInvoice(Dto):
    """One entry of a :class:`BookingPaymentView`'s ``invoices``."""

    applied: str | None = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    total: str | None = None


class BookingPaymentViewPaymentApplied(Dto):
    """One entry of a :class:`BookingPaymentView`'s ``payment_applied``."""

    amount: str | None = None
    # Null in every record measured, so untyped.
    gateway_response: Any = None
    method: str | None = None
    processor: str | None = None
    reference: str | None = None


class BookingPdfPdf(Dto):
    """A :class:`BookingPdf`'s ``pdf``."""

    download_url: str | None = None
    file_size: int | None = None
    id: str | None = None
    object: str | None = None
    preview_url: str | None = None


class BookingLine(Dto):
    """What ``get_booking_line`` answers, under ``order_line``."""

    MEASURED_FROM = ("GET /api/{api_version}/booking/{booking_id}/lines/{line_uuid}",)

    ENVELOPE_KEY = "order_line"

    charge_item_uuid: str | None = None
    expected_delivery_date: str | None = None
    id: str | None = None
    item: BookingLineItem | None = None
    item_accounting_code: BookingLineItemAccountingCode | None = None
    item_charge_type: str | None = None
    item_custom_attributes: list[Any] | None = None
    item_description: str | None = None
    item_invoice_note: str | None = None
    item_order_quantity: int | None = None
    item_price_snapshot: BookingLineItemPriceSnapshot | None = None
    item_price_tax: BookingLineItemPriceTax | None = None
    item_properties: BookingLineItemProperties | None = None
    item_sale_tax_configuration: BookingLineItemSaleTaxConfiguration | None = None
    item_type: str | None = None
    object: str | None = None
    pre_order_stock_details: BookingLinePreOrderStockDetails | None = None
    shipping_cost: float | None = None
    subtotal: str | None = None
    tax: str | None = None
    tax_exempt_when_sold: bool | None = None
    total: str | None = None
    version: int | None = None


class BookingLineItem(Dto):
    """A :class:`BookingLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    uuid: str | None = None


class BookingLineItemAccountingCode(Dto):
    """A :class:`BookingLine`'s ``item_accounting_code``."""

    sales_revenue: str | None = None


class BookingLineItemPriceSnapshot(Dto):
    """A :class:`BookingLine`'s ``item_price_snapshot``."""

    pricing_rule: BookingLineItemPriceSnapshotPricingRule | None = None


class BookingLineItemPriceSnapshotPricingRule(Dto):
    """A :class:`BookingLineItemPriceSnapshot`'s ``pricing_rule``."""

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


class BookingLineItemPriceTax(Dto):
    """A :class:`BookingLine`'s ``item_price_tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: float | None = None


class BookingLineItemProperties(Dto):
    """A :class:`BookingLine`'s ``item_properties``."""

    billing_mode: str | None = None
    charging_and_billing_alignment: str | None = None
    charging_start_date: str | None = None
    pro_rata_partial_pricing_period: str | None = None


class BookingLineItemSaleTaxConfiguration(Dto):
    """A :class:`BookingLine`'s ``item_sale_tax_configuration``."""

    sale_price_is_based_on: str | None = None
    tax_code: BookingLineItemSaleTaxConfigurationTaxCode | None = None


class BookingLineItemSaleTaxConfigurationTaxCode(Dto):
    """A :class:`BookingLineItemSaleTaxConfiguration`'s ``tax_code``."""

    code: str | None = None
    link: str | None = None
    rate: str | None = None
    uuid: str | None = None


class BookingLinePreOrderStockDetails(Dto):
    """A :class:`BookingLine`'s ``pre_order_stock_details``."""

    pending_reserve: str | None = None
    reserved: str | None = None
    sold: str | None = None
