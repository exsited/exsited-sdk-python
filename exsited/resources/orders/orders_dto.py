"""Typed views over the order bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Order",
    "OrderList",
    "OrderNote",
    "OrderNoteList",
    "OrderRead",
    "OrderInformation",
    "AccountOrders",
    "OrderBillingPreferences",
    "OrderPaymentMethods",
    "OrderPdf",
    "OrderLine",
    "OrderNoteView",
    "OrderPaymentMethod",
    "OrderNoteFileList",
    "OrderNoteFile",
    "OrderDiscardDraft",
    "OrderExtendTrial",
    "AccountOrdersData",
    "OrderReadCurrency",
    "OrderReadTimeZone",
    "OrderReadCustomForm",
    "OrderReadManager",
    "OrderReadAccount",
    "OrderReadDiscountProfile",
    "OrderReadBillingAddress",
    "OrderReadShippingAddress",
    "OrderReadCommunicationPreference",
    "OrderReadContractProperties",
    "OrderReadBillingPreferences",
    "OrderReadCustomAttribute",
    "OrderReadLine",
    "OrderReadKpis",
    "OrderReadActivityLog",
    "OrderBillingPreferencesDetail",
    "OrderInformationCurrency",
    "OrderInformationTimeZone",
    "OrderInformationCustomForm",
    "OrderInformationManager",
    "OrderInformationAccount",
    "OrderInformationDiscountProfile",
    "OrderInformationBillingAddress",
    "OrderInformationShippingAddress",
    "OrderInformationCommunicationPreference",
    "OrderPaymentMethodsRow",
    "OrderPdfDetail",
    "OrderLineItem",
    "OrderLineItemPriceSnapshot",
    "OrderLineItemPriceTax",
    "OrderLineItemSaleTaxConfiguration",
    "OrderLineItemAccountingCode",
    "OrderLinePreOrderStockDetails",
    "OrderLineItemProperties",
    "OrderNoteViewDetail",
    "OrderNoteViewAttachment",
    "OrderNoteViewWatcher",
    "OrderNoteViewCreatedBy",
    "OrderNoteViewLastUpdatedBy",
    "OrderPaymentMethodDetail",
    "OrderNoteFileEntry",
    "AccountOrdersDataCurrency",
    "AccountOrdersDataTimeZone",
    "AccountOrdersDataCustomForm",
    "AccountOrdersDataManager",
    "AccountOrdersDataDetail",
    "AccountOrdersDataDiscountProfile",
    "AccountOrdersDataBillingAddress",
    "AccountOrdersDataShippingAddress",
    "AccountOrdersDataCommunicationPreference",
    "AccountOrdersDataBillingPreferences",
    "AccountOrdersDataContractProperties",
    "OrderCurrency",
    "OrderTimeZone",
    "OrderCustomForm",
    "OrderManager",
    "OrderSalesRep",
    "OrderShippingProfile",
    "OrderAccount",
    "OrderReferralAccount",
    "OrderDiscountProfile",
    "OrderBillingAddress",
    "OrderShippingAddress",
    "OrderCommunicationPreference",
    "OrderBillingPreferencesEntry",
    "OrderContractProperties",
    "OrderReadBillingPreferencesProformaProperties",
    "OrderReadLineItem",
    "OrderReadLineItemPriceSnapshot",
    "OrderReadLineItemPriceTax",
    "OrderReadLineItemSaleTaxConfiguration",
    "OrderReadLineItemAccountingCode",
    "OrderReadLineItemCustomAttribute",
    "OrderReadLinePreOrderStockDetails",
    "OrderReadLineItemProperties",
    "OrderReadLineBooking",
    "OrderBillingPreferencesDetailProformaProperties",
    "OrderNoteDetail",
    "OrderNoteAttachment",
    "OrderNoteWatcher",
    "OrderNoteCreatedBy",
    "OrderNoteLastUpdatedBy",
    "OrderPaymentMethodsRowProcessor",
    "OrderLineItemPriceSnapshotPricingRule",
    "OrderLineItemSaleTaxConfigurationTaxCode",
    "OrderPaymentMethodDetailProcessor",
    "AccountOrdersDataBillingPreferencesProformaProperties",
    "OrderBillingPreferencesEntryProformaProperties",
    "OrderReadLineItemPriceSnapshotPricingRule",
    "OrderReadLineItemSaleTaxConfigurationTaxCode",
    "OrderKpis",
    "OrderCustomObject",
    "OrderItemFulfillment",
    "OrderPayment",
    "OrderQuotePartialInvoices",
    "OrderItemFulfillmentAccount",
    "OrderItemFulfillmentCreatedBy",
    "OrderItemFulfillmentFulfillment",
    "OrderItemFulfillmentFulfillmentItem",
    "OrderItemFulfillmentInvoice",
    "OrderItemFulfillmentLastUpdatedBy",
    "OrderPaymentAccount",
    "OrderPaymentCreatedBy",
    "OrderPaymentInvoice",
    "OrderPaymentPaymentApplied",
]


class Order(Dto):
    """The order body."""

    MEASURED_FROM = ("GET /api/{api_version}/orders",)

    account: OrderAccount | None = None
    allow_contract: bool | None = None
    billing_address: OrderBillingAddress | None = None
    billing_preferences: OrderBillingPreferencesEntry | None = None
    billing_start_date: str | None = None
    billing_start_day_of_month: str | None = None
    communication_preferences: list[OrderCommunicationPreference] | None = None
    contract_properties: OrderContractProperties | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: OrderCurrency | None = None
    custom_form: OrderCustomForm | None = None
    customer_purchase_order_id: str | None = None
    description: str | None = None
    discount_profile: OrderDiscountProfile | None = None
    display_name: str | None = None
    id: str | None = None
    invoice_note: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    manager: OrderManager | None = None
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
    referral_account: OrderReferralAccount | None = None
    sales_rep: OrderSalesRep | None = None
    shipping_address: OrderShippingAddress | None = None
    shipping_cost: float | None = None
    shipping_profile: OrderShippingProfile | None = None
    status: str | None = None
    time_zone: OrderTimeZone | None = None
    version: int | None = None


class OrderList(Dto):
    """One page of ``Order`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders",)

    data: list[Order] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class OrderNote(Dto):
    """The order note body."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/notes",)

    attachments: list[OrderNoteAttachment] | None = None
    content: str | None = None
    created_by: OrderNoteCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: OrderNoteLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    order: OrderNoteDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[OrderNoteWatcher] | None = None


class OrderNoteList(Dto):
    """One page of ``OrderNote`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/notes",)

    data: list[OrderNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class OrderRead(Dto):
    """The order read body, under ``order``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/orders/{order_id}",
        "GET /api/{api_version}/orders/{order_id}/lines",
        "POST /api/{api_version}/orders",
        "POST /api/{api_version}/orders/{order_id}/activate_draft",
        "PATCH /api/{api_version}/orders/{order_id}/billing_preferences",
        "PUT /api/{api_version}/orders/{order_id}/billing_preferences",
        "POST /api/{api_version}/orders/{order_id}/cancel",
        "POST /api/{api_version}/orders/{order_id}/change",
        "POST /api/{api_version}/orders/{order_id}/convert_to_order",
        "PATCH /api/{api_version}/orders/{order_id}/information",
        "POST /api/{api_version}/orders/{order_id}/reactivate",
        "POST /api/{api_version}/orders/{order_id}/relinquish",
        "PATCH /api/{api_version}/orders/{order_id}/lines/{line_uuid}",
        "PATCH /api/{api_version}/orders/{order_id}/lines/{line_uuid}/billing_preferences",
        "PUT /api/{api_version}/orders/{order_id}/lines/{line_uuid}/billing_preferences",
        "POST /api/{api_version}/orders/{order_id}/change/preview",
    )

    ENVELOPE_KEY = "order"

    account: OrderReadAccount | None = None
    activity_logs: list[OrderReadActivityLog] | None = None
    allow_contract: bool | None = None
    billing_address: OrderReadBillingAddress | None = None
    billing_preferences: OrderReadBillingPreferences | None = None
    billing_start_date: str | None = None
    billing_start_day_of_month: str | None = None
    communication_preferences: list[OrderReadCommunicationPreference] | None = None
    contract_properties: OrderReadContractProperties | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: OrderReadCurrency | None = None
    custom_attributes: list[OrderReadCustomAttribute] | None = None
    custom_form: OrderReadCustomForm | None = None
    customer_purchase_order_id: str | None = None
    description: str | None = None
    discount_profile: OrderReadDiscountProfile | None = None
    display_name: str | None = None
    id: str | None = None
    invoice_note: str | None = None
    kpis: OrderReadKpis | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    lines: list[OrderReadLine] | None = None
    manager: OrderReadManager | None = None
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
    # Null in every record measured, so untyped.
    referral_account: Any = None
    # Null in every record measured, so untyped.
    sales_rep: Any = None
    shipping_address: OrderReadShippingAddress | None = None
    shipping_cost: float | None = None
    shipping_line_items: list[Any] | None = None
    # Null in every record measured, so untyped.
    shipping_profile: Any = None
    status: str | None = None
    subtotal: str | None = None
    tax: str | None = None
    time_zone: OrderReadTimeZone | None = None
    total: str | None = None
    version: int | None = None


class OrderInformation(Dto):
    """The order information body, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/information",)

    ENVELOPE_KEY = "order"

    account: OrderInformationAccount | None = None
    allow_contract: bool | None = None
    billing_address: OrderInformationBillingAddress | None = None
    billing_start_date: str | None = None
    billing_start_day_of_month: str | None = None
    communication_preferences: list[OrderInformationCommunicationPreference] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: OrderInformationCurrency | None = None
    custom_form: OrderInformationCustomForm | None = None
    # Null in every record measured, so untyped.
    customer_purchase_order_id: Any = None
    description: str | None = None
    discount_profile: OrderInformationDiscountProfile | None = None
    display_name: str | None = None
    id: str | None = None
    invoice_note: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    manager: OrderInformationManager | None = None
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
    # Null in every record measured, so untyped.
    referral_account: Any = None
    # Null in every record measured, so untyped.
    sales_rep: Any = None
    shipping_address: OrderInformationShippingAddress | None = None
    shipping_cost: float | None = None
    # Null in every record measured, so untyped.
    shipping_profile: Any = None
    status: str | None = None
    time_zone: OrderInformationTimeZone | None = None
    version: int | None = None


class AccountOrders(Dto):
    """The account orders body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/accounts/{account_id}/orders",
        "GET /api/{api_version}/orders/{order_id}/custom_objects",
        "GET /api/{api_version}/orders/{order_id}/custom_objects_instances",
        "GET /api/{api_version}/orders/{order_id}/item_fulfillments",
    )

    data: list[AccountOrdersData] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class OrderBillingPreferences(Dto):
    """The order billing preferences body, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/billing_preferences",)

    ENVELOPE_KEY = "order"

    billing_preferences: OrderBillingPreferencesDetail | None = None
    object: str | None = None


class OrderPaymentMethods(Dto):
    """What ``get_order_payment_methods`` answers, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/payment_methods",)

    ENVELOPE_KEY = "order"

    payment_methods: list[OrderPaymentMethodsRow] | None = None


class OrderPdf(Dto):
    """What ``get_order_pdf`` answers, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/pdf",)

    ENVELOPE_KEY = "order"

    pdf: OrderPdfDetail | None = None


class OrderLine(Dto):
    """What ``get_order_line`` answers, under ``order_line``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/lines/{line_uuid}",)

    ENVELOPE_KEY = "order_line"

    charge_item_uuid: str | None = None
    expected_delivery_date: str | None = None
    id: str | None = None
    item: OrderLineItem | None = None
    item_accounting_code: OrderLineItemAccountingCode | None = None
    item_charge_type: str | None = None
    item_custom_attributes: list[Any] | None = None
    item_description: str | None = None
    item_invoice_note: str | None = None
    item_order_quantity: int | None = None
    item_price_snapshot: OrderLineItemPriceSnapshot | None = None
    item_price_tax: OrderLineItemPriceTax | None = None
    item_properties: OrderLineItemProperties | None = None
    item_sale_tax_configuration: OrderLineItemSaleTaxConfiguration | None = None
    item_type: str | None = None
    object: str | None = None
    pre_order_stock_details: OrderLinePreOrderStockDetails | None = None
    shipping_cost: float | None = None
    subtotal: str | None = None
    tax: str | None = None
    tax_exempt_when_sold: bool | None = None
    total: str | None = None
    version: int | None = None


class OrderNoteView(Dto):
    """What ``get_order_note`` answers, under ``note``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/orders/{order_id}/notes/{order_note_id}",
        "POST /api/{api_version}/orders/{order_id}/notes",
        "PATCH /api/{api_version}/orders/{order_id}/notes/{order_note_id}",
    )

    ENVELOPE_KEY = "note"

    attachments: list[OrderNoteViewAttachment] | None = None
    content: str | None = None
    created_by: OrderNoteViewCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: OrderNoteViewLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    order: OrderNoteViewDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[OrderNoteViewWatcher] | None = None


class OrderPaymentMethod(Dto):
    """What ``get_order_payment_method`` answers, under ``order``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/orders/{order_id}/payment_methods/{payment_method_ref}",
    )

    ENVELOPE_KEY = "order"

    payment_method: OrderPaymentMethodDetail | None = None


class OrderNoteFileList(Dto):
    """One page of what ``get_order_note_files`` lists, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/notes/{order_note_id}/files",)

    data: list[OrderNoteFileEntry] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class OrderNoteFile(Dto):
    """What ``get_order_note_file`` answers, under ``file``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/orders/{order_id}/notes/{order_note_id}/files/{order_file_id}",
    )

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class OrderDiscardDraft(Dto):
    """What ``create_order_discard_draft`` answers, under ``order``."""

    MEASURED_FROM = ("POST /api/{api_version}/orders/{order_id}/discard_draft",)

    ENVELOPE_KEY = "order"

    message: str | None = None


class OrderExtendTrial(Dto):
    """What ``create_order_extend_trial`` answers, under ``order``."""

    MEASURED_FROM = ("POST /api/{api_version}/orders/{order_id}/extend_trial",)

    ENVELOPE_KEY = "order"

    message: str | None = None


class AccountOrdersData(Dto):
    """One entry of a :class:`AccountOrders`'s ``data``."""

    account: AccountOrdersDataDetail | None = None
    allow_contract: bool | None = None
    billing_address: AccountOrdersDataBillingAddress | None = None
    billing_preferences: AccountOrdersDataBillingPreferences | None = None
    billing_start_date: str | None = None
    billing_start_day_of_month: str | None = None
    communication_preferences: list[AccountOrdersDataCommunicationPreference] | None = None
    contract_properties: AccountOrdersDataContractProperties | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: AccountOrdersDataCurrency | None = None
    custom_form: AccountOrdersDataCustomForm | None = None
    customer_purchase_order_id: str | None = None
    description: str | None = None
    discount_profile: AccountOrdersDataDiscountProfile | None = None
    display_name: str | None = None
    id: str | None = None
    invoice_note: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    manager: AccountOrdersDataManager | None = None
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
    # Null in every record measured, so untyped.
    referral_account: Any = None
    # Null in every record measured, so untyped.
    sales_rep: Any = None
    shipping_address: AccountOrdersDataShippingAddress | None = None
    shipping_cost: float | None = None
    # Null in every record measured, so untyped.
    shipping_profile: Any = None
    status: str | None = None
    time_zone: AccountOrdersDataTimeZone | None = None
    version: int | None = None


class OrderReadCurrency(Dto):
    """A :class:`OrderRead`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderReadTimeZone(Dto):
    """A :class:`OrderRead`'s ``time_zone``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderReadCustomForm(Dto):
    """A :class:`OrderRead`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderReadManager(Dto):
    """A :class:`OrderRead`'s ``manager``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderReadAccount(Dto):
    """A :class:`OrderRead`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderReadDiscountProfile(Dto):
    """A :class:`OrderRead`'s ``discount_profile``."""

    amount: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    redemption_code: str | None = None
    type: str | None = None


class OrderReadBillingAddress(Dto):
    """A :class:`OrderRead`'s ``billing_address``."""

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


class OrderReadShippingAddress(Dto):
    """A :class:`OrderRead`'s ``shipping_address``."""

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


class OrderReadCommunicationPreference(Dto):
    """One entry of a :class:`OrderRead`'s ``communication_preferences``."""

    channel: str | None = None
    enabled: bool | None = None


class OrderReadContractProperties(Dto):
    """A :class:`OrderRead`'s ``contract_properties``, sent for a contract order."""

    allow_downgrade: bool | None = None
    allow_early_termination: bool | None = None
    allow_postponement: bool | None = None
    allow_trial: bool | None = None
    allow_upgrade: bool | None = None
    apply_early_termination_charge: bool | None = None
    auto_renewal_ends_on: str | None = None
    auto_renewal_require_customer_acceptance: bool | None = None
    auto_renewal_term: str | None = None
    early_termination_charge_type: str | None = None
    early_termination_minimum_period: str | None = None
    initial_contract_term: str | None = None
    renew_automatically: str | None = None
    require_customer_acceptance: bool | None = None
    requires_payment_method: bool | None = None
    start_contract_after_trial_ends: bool | None = None
    termination_accounting_code: str | None = None
    termination_fixed_charge: str | None = None
    termination_notice_period: str | None = None
    trial_end_date: str | None = None
    trial_period: str | None = None
    trial_requires_payment_method: bool | None = None


class OrderReadBillingPreferences(Dto):
    """A :class:`OrderRead`'s ``billing_preferences``."""

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
    proforma_properties: OrderReadBillingPreferencesProformaProperties | None = None


class OrderReadCustomAttribute(Dto):
    """One entry of a :class:`OrderRead`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | list[str] | None = None


class OrderReadLine(Dto):
    """One entry of a :class:`OrderRead`'s ``lines``."""

    booking: OrderReadLineBooking | None = None
    charge_item_uuid: str | None = None
    expected_delivery_date: str | None = None
    id: str | None = None
    item: OrderReadLineItem | None = None
    item_accounting_code: OrderReadLineItemAccountingCode | None = None
    item_charge_type: str | None = None
    item_custom_attributes: list[OrderReadLineItemCustomAttribute] | None = None
    item_description: str | None = None
    item_invoice_note: str | None = None
    item_order_quantity: int | None = None
    item_price_snapshot: OrderReadLineItemPriceSnapshot | None = None
    item_price_tax: OrderReadLineItemPriceTax | None = None
    item_properties: OrderReadLineItemProperties | None = None
    item_sale_tax_configuration: OrderReadLineItemSaleTaxConfiguration | None = None
    item_type: str | None = None
    object: str | None = None
    pre_order_stock_details: OrderReadLinePreOrderStockDetails | None = None
    shipping_cost: float | None = None
    subtotal: str | None = None
    tax: str | None = None
    tax_exempt_when_sold: bool | None = None
    total: str | None = None
    version: int | None = None


class OrderReadKpis(Dto):
    """A :class:`OrderRead`'s ``kpis``."""

    # Null in every record measured, so untyped.
    created_on: Any = None
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
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
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


class OrderReadActivityLog(Dto):
    """One entry of a :class:`OrderRead`'s ``activity_logs``."""

    activity: str | None = None


class OrderBillingPreferencesDetail(Dto):
    """A :class:`OrderBillingPreferences`'s ``billing_preferences``."""

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
    proforma_properties: OrderBillingPreferencesDetailProformaProperties | None = None


class OrderInformationCurrency(Dto):
    """A :class:`OrderInformation`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderInformationTimeZone(Dto):
    """A :class:`OrderInformation`'s ``time_zone``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderInformationCustomForm(Dto):
    """A :class:`OrderInformation`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderInformationManager(Dto):
    """A :class:`OrderInformation`'s ``manager``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderInformationAccount(Dto):
    """A :class:`OrderInformation`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderInformationDiscountProfile(Dto):
    """A :class:`OrderInformation`'s ``discount_profile``."""

    amount: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    redemption_code: str | None = None
    type: str | None = None


class OrderInformationBillingAddress(Dto):
    """A :class:`OrderInformation`'s ``billing_address``."""

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


class OrderInformationShippingAddress(Dto):
    """A :class:`OrderInformation`'s ``shipping_address``."""

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


class OrderInformationCommunicationPreference(Dto):
    """One entry of a :class:`OrderInformation`'s ``communication_preferences``."""

    channel: str | None = None
    enabled: bool | None = None


class OrderPaymentMethodsRow(Dto):
    """One entry of a :class:`OrderPaymentMethods`'s ``payment_methods``."""

    created_by: str | None = None
    created_on: str | None = None
    default: bool | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    last_used_at: Any = None
    object: str | None = None
    payment_count: int | None = None
    processor: OrderPaymentMethodsRowProcessor | None = None
    processor_type: str | None = None
    reference: str | None = None
    restricted_to_orders: bool | None = None
    specified_order_ids: str | None = None
    status: str | None = None
    version: int | None = None


class OrderPdfDetail(Dto):
    """A :class:`OrderPdf`'s ``pdf``."""

    download_url: str | None = None
    file_size: int | None = None
    id: str | None = None
    object: str | None = None
    preview_url: str | None = None


class OrderLineItem(Dto):
    """A :class:`OrderLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    uuid: str | None = None


class OrderLineItemPriceSnapshot(Dto):
    """A :class:`OrderLine`'s ``item_price_snapshot``."""

    pricing_rule: OrderLineItemPriceSnapshotPricingRule | None = None


class OrderLineItemPriceTax(Dto):
    """A :class:`OrderLine`'s ``item_price_tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: float | None = None


class OrderLineItemSaleTaxConfiguration(Dto):
    """A :class:`OrderLine`'s ``item_sale_tax_configuration``."""

    sale_price_is_based_on: str | None = None
    tax_code: OrderLineItemSaleTaxConfigurationTaxCode | None = None


class OrderLineItemAccountingCode(Dto):
    """A :class:`OrderLine`'s ``item_accounting_code``."""

    sales_revenue: str | None = None


class OrderLinePreOrderStockDetails(Dto):
    """A :class:`OrderLine`'s ``pre_order_stock_details``."""

    pending_reserve: str | None = None
    reserved: str | None = None
    sold: str | None = None


class OrderLineItemProperties(Dto):
    """A :class:`OrderLine`'s ``item_properties``."""

    charging_and_billing_alignment: str | None = None
    charging_start_date: str | None = None
    pro_rata_partial_pricing_period: str | None = None


class OrderNoteViewDetail(Dto):
    """A :class:`OrderNoteView`'s ``order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class OrderNoteViewAttachment(Dto):
    """One entry of a :class:`OrderNoteView`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class OrderNoteViewWatcher(Dto):
    """One entry of a :class:`OrderNoteView`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class OrderNoteViewCreatedBy(Dto):
    """A :class:`OrderNoteView`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class OrderNoteViewLastUpdatedBy(Dto):
    """A :class:`OrderNoteView`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class OrderPaymentMethodDetail(Dto):
    """A :class:`OrderPaymentMethod`'s ``payment_method``."""

    created_by: str | None = None
    created_on: str | None = None
    default: bool | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    last_used_at: Any = None
    object: str | None = None
    payment_count: int | None = None
    processor: OrderPaymentMethodDetailProcessor | None = None
    processor_type: str | None = None
    reference: str | None = None
    restricted_to_orders: bool | None = None
    specified_order_ids: str | None = None
    status: str | None = None
    version: int | None = None


class OrderNoteFileEntry(Dto):
    """One entry of a :class:`OrderNoteFileList`'s ``data``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class AccountOrdersDataCurrency(Dto):
    """A :class:`AccountOrdersData`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountOrdersDataTimeZone(Dto):
    """A :class:`AccountOrdersData`'s ``time_zone``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountOrdersDataCustomForm(Dto):
    """A :class:`AccountOrdersData`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountOrdersDataManager(Dto):
    """A :class:`AccountOrdersData`'s ``manager``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountOrdersDataDetail(Dto):
    """A :class:`AccountOrdersData`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountOrdersDataDiscountProfile(Dto):
    """A :class:`AccountOrdersData`'s ``discount_profile``."""

    amount: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    redemption_code: str | None = None
    type: str | None = None


class AccountOrdersDataBillingAddress(Dto):
    """A :class:`AccountOrdersData`'s ``billing_address``."""

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


class AccountOrdersDataShippingAddress(Dto):
    """A :class:`AccountOrdersData`'s ``shipping_address``."""

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


class AccountOrdersDataCommunicationPreference(Dto):
    """One entry of a :class:`AccountOrdersData`'s ``communication_preferences``."""

    channel: str | None = None
    enabled: bool | None = None


class AccountOrdersDataBillingPreferences(Dto):
    """A :class:`AccountOrdersData`'s ``billing_preferences``."""

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
    proforma_properties: AccountOrdersDataBillingPreferencesProformaProperties | None = None


class AccountOrdersDataContractProperties(Dto):
    """A :class:`AccountOrdersData`'s ``contract_properties``."""

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


class OrderCurrency(Dto):
    """A :class:`Order`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderTimeZone(Dto):
    """A :class:`Order`'s ``time_zone``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderCustomForm(Dto):
    """A :class:`Order`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderManager(Dto):
    """A :class:`Order`'s ``manager``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderSalesRep(Dto):
    """A :class:`Order`'s ``sales_rep``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderShippingProfile(Dto):
    """A :class:`Order`'s ``shipping_profile``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderAccount(Dto):
    """A :class:`Order`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderReferralAccount(Dto):
    """A :class:`Order`'s ``referral_account``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class OrderDiscountProfile(Dto):
    """A :class:`Order`'s ``discount_profile``."""

    amount: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    redemption_code: str | None = None
    type: str | None = None


class OrderBillingAddress(Dto):
    """A :class:`Order`'s ``billing_address``."""

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


class OrderShippingAddress(Dto):
    """A :class:`Order`'s ``shipping_address``."""

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


class OrderCommunicationPreference(Dto):
    """One entry of a :class:`Order`'s ``communication_preferences``."""

    channel: str | None = None
    enabled: bool | None = None


class OrderBillingPreferencesEntry(Dto):
    """A :class:`Order`'s ``billing_preferences``."""

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
    proforma_properties: OrderBillingPreferencesEntryProformaProperties | None = None


class OrderContractProperties(Dto):
    """A :class:`Order`'s ``contract_properties``."""

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


class OrderReadBillingPreferencesProformaProperties(Dto):
    """A :class:`OrderReadBillingPreferences`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    # Null in every record measured, so untyped.
    acceptance_term: Any = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class OrderReadLineItem(Dto):
    """A :class:`OrderReadLine`'s ``item``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    uuid: str | None = None


class OrderReadLineItemPriceSnapshot(Dto):
    """A :class:`OrderReadLine`'s ``item_price_snapshot``."""

    pricing_rule: OrderReadLineItemPriceSnapshotPricingRule | None = None


class OrderReadLineItemPriceTax(Dto):
    """A :class:`OrderReadLine`'s ``item_price_tax``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rate: float | None = None


class OrderReadLineItemSaleTaxConfiguration(Dto):
    """A :class:`OrderReadLine`'s ``item_sale_tax_configuration``."""

    sale_price_is_based_on: str | None = None
    tax_code: OrderReadLineItemSaleTaxConfigurationTaxCode | None = None


class OrderReadLineItemAccountingCode(Dto):
    """A :class:`OrderReadLine`'s ``item_accounting_code``."""

    sales_revenue: Any = None


class OrderReadLineItemCustomAttribute(Dto):
    """One entry of a :class:`OrderReadLine`'s ``item_custom_attributes``."""

    name: str | None = None
    value: str | list[str] | None = None


class OrderReadLinePreOrderStockDetails(Dto):
    """A :class:`OrderReadLine`'s ``pre_order_stock_details``."""

    pending_reserve: str | None = None
    reserved: str | None = None
    sold: str | None = None


class OrderReadLineItemProperties(Dto):
    """A :class:`OrderReadLine`'s ``item_properties``."""

    billing_mode: str | None = None
    charging_and_billing_alignment: str | None = None
    charging_period: str | None = None
    charging_start_date: str | None = None
    pro_rata_partial_charging_period: str | None = None
    pro_rata_partial_pricing_period: str | None = None


class OrderReadLineBooking(Dto):
    """A :class:`OrderReadLine`'s ``booking``."""

    booking_end_time: str | None = None
    booking_start_time: str | None = None
    labour_uuid: str | None = None


class OrderBillingPreferencesDetailProformaProperties(Dto):
    """A :class:`OrderBillingPreferencesDetail`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    # Null in every record measured, so untyped.
    acceptance_term: Any = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class OrderNoteDetail(Dto):
    """A :class:`OrderNote`'s ``order``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class OrderNoteAttachment(Dto):
    """One entry of a :class:`OrderNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class OrderNoteWatcher(Dto):
    """One entry of a :class:`OrderNote`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class OrderNoteCreatedBy(Dto):
    """A :class:`OrderNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class OrderNoteLastUpdatedBy(Dto):
    """A :class:`OrderNote`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class OrderPaymentMethodsRowProcessor(Dto):
    """A :class:`OrderPaymentMethodsRow`'s ``processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderLineItemPriceSnapshotPricingRule(Dto):
    """A :class:`OrderLineItemPriceSnapshot`'s ``pricing_rule``."""

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


class OrderLineItemSaleTaxConfigurationTaxCode(Dto):
    """A :class:`OrderLineItemSaleTaxConfiguration`'s ``tax_code``."""

    code: str | None = None
    link: str | None = None
    rate: str | None = None
    uuid: str | None = None


class OrderPaymentMethodDetailProcessor(Dto):
    """A :class:`OrderPaymentMethodDetail`'s ``processor``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountOrdersDataBillingPreferencesProformaProperties(Dto):
    """A :class:`AccountOrdersDataBillingPreferences`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    # Null in every record measured, so untyped.
    acceptance_term: Any = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class OrderBillingPreferencesEntryProformaProperties(Dto):
    """A :class:`OrderBillingPreferencesEntry`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    acceptance_term: str | None = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class OrderReadLineItemPriceSnapshotPricingRule(Dto):
    """A :class:`OrderReadLineItemPriceSnapshot`'s ``pricing_rule``."""

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


class OrderReadLineItemSaleTaxConfigurationTaxCode(Dto):
    """A :class:`OrderReadLineItemSaleTaxConfiguration`'s ``tax_code``."""

    code: str | None = None
    link: str | None = None
    rate: str | float | None = None
    uuid: str | None = None


class OrderKpis(Dto):
    """What ``get_order_kpis`` answers, under ``order_kpis``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/kpis",)

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


class OrderCustomObject(Dto):
    """One custom object with the order's instances of it, under ``custom_object``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/orders/{order_id}/custom_objects/{custom_object_id}",
        "GET /api/{api_version}/orders/{order_id}/custom_objects_instances/{custom_object_id}",
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


class OrderItemFulfillment(Dto):
    """What ``get_order_item_fulfillment`` answers, under ``item_fulfillment``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/item_fulfillments/{fulfillment_id}",)

    ENVELOPE_KEY = "item_fulfillment"

    account: OrderItemFulfillmentAccount | None = None
    code: str | None = None
    created_by: OrderItemFulfillmentCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: dict[str, Any] | None = None
    # Null in every record measured, so untyped.
    delivery_status: Any = None
    fulfillment_completed: bool | None = None
    fulfillment_date: str | None = None
    # Null in every record measured, so untyped.
    fulfillment_note: Any = None
    fulfillment_status: str | None = None
    fulfillments: list[OrderItemFulfillmentFulfillment] | None = None
    href: str | None = None
    id: str | None = None
    invoice: OrderItemFulfillmentInvoice | None = None
    last_updated_by: OrderItemFulfillmentLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    order: Any = None
    status: str | None = None
    tracking_number: str | None = None
    version: int | None = None


class OrderPayment(Dto):
    """What ``get_order_payment`` answers, under ``payment``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/payments/{payment_id}",)

    ENVELOPE_KEY = "payment"

    account: OrderPaymentAccount | None = None
    created_by: OrderPaymentCreatedBy | None = None
    created_on: str | None = None
    credit_applied: list[Any] | None = None
    custom_attributes: list[Any] | None = None
    gift_certificate_applied: list[Any] | None = None
    id: str | None = None
    invoices: list[OrderPaymentInvoice] | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    # Null in every record measured, so untyped.
    origin: Any = None
    payment_applied: list[OrderPaymentPaymentApplied] | None = None
    payment_note: str | None = None
    reconcile_status: str | None = None
    status: str | None = None
    version: int | None = None


class OrderQuotePartialInvoices(Dto):
    """What ``get_order_quote_partial_invoices`` answers, under ``order``."""

    MEASURED_FROM = ("GET /api/{api_version}/orders/{order_id}/quote_partial_invoices",)

    ENVELOPE_KEY = "order"

    partial_invoices: list[Any] | None = None


class OrderItemFulfillmentAccount(Dto):
    """A :class:`OrderItemFulfillment`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderItemFulfillmentCreatedBy(Dto):
    """A :class:`OrderItemFulfillment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class OrderItemFulfillmentFulfillment(Dto):
    """One entry of a :class:`OrderItemFulfillment`'s ``fulfillments``."""

    fulfillment_index: int | None = None
    fulfillment_qty: float | None = None
    fulfillment_sent_qty: float | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    inventory_tracking: Any = None
    item: OrderItemFulfillmentFulfillmentItem | None = None
    object: str | None = None
    pending_return: float | None = None
    # Null in every record measured, so untyped.
    returned: Any = None
    serving_status: str | None = None
    # Null in every record measured, so untyped.
    uom: Any = None
    # Null in every record measured, so untyped.
    uom_precision: Any = None


class OrderItemFulfillmentFulfillmentItem(Dto):
    """A :class:`OrderItemFulfillmentFulfillment`'s ``item``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderItemFulfillmentInvoice(Dto):
    """A :class:`OrderItemFulfillment`'s ``invoice``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class OrderItemFulfillmentLastUpdatedBy(Dto):
    """A :class:`OrderItemFulfillment`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class OrderPaymentAccount(Dto):
    """A :class:`OrderPayment`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class OrderPaymentCreatedBy(Dto):
    """A :class:`OrderPayment`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class OrderPaymentInvoice(Dto):
    """One entry of a :class:`OrderPayment`'s ``invoices``."""

    applied: str | None = None
    due_date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    outstanding: str | None = None
    total: str | None = None


class OrderPaymentPaymentApplied(Dto):
    """One entry of a :class:`OrderPayment`'s ``payment_applied``."""

    amount: str | None = None
    # Null in every record measured, so untyped.
    gateway_response: Any = None
    method: str | None = None
    processor: str | None = None
    reference: str | None = None
