"""Typed views over the settings bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsDiscountProfile",
    "SettingsDiscountProfileList",
    "SettingsPaymentProcessor",
    "SettingsPaymentProcessorList",
    "SettingsShippingProfile",
    "SettingsShippingProfileList",
    "SettingsPricingLevel",
    "SettingsPricingLevelList",
    "SettingsTimeZone",
    "SettingsTimeZoneList",
    "SettingsWarehouse",
    "SettingsWarehouseList",
    "SettingsCurrency",
    "SettingsCurrencyList",
    "SettingsItemGroup",
    "SettingsItemGroupList",
    "CustomObject",
    "CustomObjectList",
    "SettingsTax",
    "SettingsTaxList",
    "SettingsVariation",
    "SettingsVariationList",
    "SettingsPaymentTerm",
    "SettingsPaymentTermList",
    "SettingsItemGroups",
    "SettingsCustomLogicScript",
    "SettingsCurrencyRead",
    "SettingsCustomObjectCustomize",
    "SettingsCustomObjects",
    "SettingsVariations",
    "SettingsTimeZoneRead",
    "SettingsCustomLogicScripts",
    "Settings",
    "SettingsFieldSettingsItem",
    "SettingsGeneralSettingsItemUpdated",
    "SettingsResource",
    "SettingsCurrencyReadCountry",
    "SettingsItemGroupsAccountingCode",
    "SettingsCustomObjectCustomizeConfiguration",
    "SettingsFieldSettingsItemGeneralSettings",
    "SettingsFieldSettingsItemData",
    "SettingsGeneralSettingsItemUpdatedDetail",
    "SettingsGeneralSettingsItemUpdatedProduct",
    "SettingsCurrencyCountry",
    "SettingsDiscountProfileAccountingCode",
    "SettingsDiscountProfileTaxCode",
    "SettingsItemGroupAccountingCode",
    "SettingsPaymentProcessorCurrency",
    "SettingsPaymentProcessorAccountingCode",
    "SettingsPaymentTermDuration",
    "SettingsPricingLevelTaxCode",
    "SettingsShippingProfileTaxRule",
    "SettingsShippingProfileAccountingCode",
    "SettingsTaxCountry",
    "SettingsTaxCountryTaxByState",
    "SettingsWarehouseCountry",
    "SettingsCustomObjectCustomizeConfigurationAttribute",
    "SettingsFieldSettingsItemGeneralSettingsAccount",
    "SettingsGeneralSettingsItemUpdatedDetailAvailableChargeTypes",
    "SettingsGeneralSettingsItemUpdatedDetailAvailablePricingMethods",
    "SettingsGeneralSettingsItemUpdatedDetailItemGrouping",
    "SettingsGeneralSettingsItemUpdatedDetailItemManagement",
    "SettingsGeneralSettingsItemUpdatedDetailUseVolumePricing",
    "SettingsGeneralSettingsItemUpdatedDetailPricingPeriodCanVaryFromChargingPeriod",
    "SettingsGeneralSettingsItemUpdatedDetailSalePriceEnteredIsInclusiveOfTax",
    "SettingsGeneralSettingsItemUpdatedDetailPurchasePriceEnteredIsInclusiveOfTax",
    "SettingsGeneralSettingsItemUpdatedDetailInventoryAdjustmentRules",
    "SettingsGeneralSettingsItemUpdatedDetailPreOrder",
    "SettingsFieldSettingsItemGeneralSettingsAccountAccountGrouping",
    "SettingsFieldSettingsItemGeneralSettingsAccountCreationOfSubsidiaryAccount",
    "SettingsFieldSettingsItemGeneralSettingsAccountAccountManagement",
    "SettingsFieldSettingsItemGeneralSettingsAccountSalesRepTrackingAtAccountLevel",
    "SettingsFieldSettingsItemGeneralSettingsAccountReferralTrackingAtAccountLevel",
    "SettingsFieldSettingsItemGeneralSettingsAccountBillingContact",
    "SettingsFieldSettingsItemGeneralSettingsAccountShippingContact",
    "SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact1",
    "SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact2",
    "SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact3",
    "SettingsGeneralSettingsItemUpdatedDetailPurchasePriceEnteredIsInclusiveOfTaxDetail",
    "SettingsCustomObjectDefinition",
    "SettingsPaymentProcessorSaved",
    "SettingsPaymentProcessorSavedCurrency",
    "SettingsPaymentTermCreated",
    "SettingsPricingLevelCreated",
    "SettingsGeneralSettings",
    "SettingsGeneralSettingsDashboard",
    "SettingsGeneralSettingsDateAndTime",
    "SettingsGeneralSettingsLabour",
    "SettingsGeneralSettingsOrder",
    "SettingsGeneralSettingsOrderOrderManagement",
    "SettingsGeneralSettingsOrderReferralTrackingAtOrderLevel",
    "SettingsGeneralSettingsOrderSalesRepTrackingAtOrderLevel",
    "SettingsGeneralSettingsPortal",
    "SettingsGeneralSettingsPurchase",
    "SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseCreditNoteFields",
    "SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseInvoiceFields",
    "SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchasePaymentFields",
    "SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseRefundFields",
    "SettingsGeneralSettingsSecurity",
    "SettingsGeneralSettingsTransaction",
    "SettingsGeneralSettingsTransactionAllowModificationOfFollowingCreditNoteFields",
    "SettingsGeneralSettingsTransactionAllowModificationOfFollowingInvoiceFields",
    "SettingsGeneralSettingsTransactionAllowModificationOfFollowingPaymentFields",
    "SettingsGeneralSettingsTransactionAllowModificationOfFollowingRefundFields",
    "SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreference",
    "SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceEmail",
    "SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferencePostalMail",
    "SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceTextMessage",
    "SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceVoiceMail",
    "SettingsGeneralSettingsTransactionDefaultAccountingCodes",
    "SettingsCustomObjectDefinitionList",
    "SettingsCustomObjectDefinitionRead",
    "SettingsDiscountProfileRead",
    "SettingsPaymentProcessorRead",
    "SettingsPaymentTermRead",
    "SettingsPricingLevelRead",
    "SettingsShippingProfileRead",
    "SettingsTaxRead",
    "SettingsWarehouseRead",
    "SettingsFieldSettingList",
    "SettingsFieldSettingRead",
    "SettingsCustomLogicScriptSaved",
    "SettingsPaymentTermUpdated",
]


class SettingsDiscountProfile(Dto):
    """The settings discount profile body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/discount_profiles",)

    accounting_code: SettingsDiscountProfileAccountingCode | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    discount_type: str | None = None
    display_name: str | None = None
    end_time: str | None = None
    fixed_amount: float | None = None
    href: str | None = None
    id: str | None = None
    invoice_note: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    max_use_per_account: int | None = None
    max_use_per_order: int | None = None
    max_use_total: int | None = None
    name: str | None = None
    object: str | None = None
    owner_type: str | None = None
    percentage_amount: float | None = None
    price_is_inclusive_of_discount: bool | None = None
    priority: int | None = None
    redemption_required: bool | None = None
    stackable: bool | None = None
    start_time: str | None = None
    status: str | None = None
    tax_code: SettingsDiscountProfileTaxCode | None = None
    version: int | None = None


class SettingsDiscountProfileList(Dto):
    """One page of ``SettingsDiscountProfile`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/discount_profiles",)

    data: list[SettingsDiscountProfile] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsPaymentProcessor(Dto):
    """The settings payment processor body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/payment_processors",)

    accounting_code: SettingsPaymentProcessorAccountingCode | None = None
    conversion_rate: float | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: SettingsPaymentProcessorCurrency | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    disconnected: bool | None = None
    display_name: str | None = None
    gateway_type: str | None = None
    href: str | None = None
    id: str | None = None
    integration_state: str | None = None
    is_default: bool | None = None
    is_foreign_currency: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    provider: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsPaymentProcessorList(Dto):
    """One page of ``SettingsPaymentProcessor`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/payment_processors",)

    data: list[SettingsPaymentProcessor] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsShippingProfile(Dto):
    """The settings shipping profile body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/shipping_profiles",)

    accounting_code: SettingsShippingProfileAccountingCode | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    fixed_amount: float | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    integration_connection: Any = None
    invoice_note: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    price_tax_inclusive: bool | None = None
    sales_tax_rate: float | None = None
    shipping_type: str | None = None
    status: str | None = None
    tax_exempt: bool | None = None
    tax_rule: SettingsShippingProfileTaxRule | None = None
    version: int | None = None


class SettingsShippingProfileList(Dto):
    """One page of ``SettingsShippingProfile`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/shipping_profiles",)

    data: list[SettingsShippingProfile] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsPricingLevel(Dto):
    """The settings pricing level body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/pricing_levels",)

    # Null in every record measured, so untyped.
    built_in_item: Any = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    is_default: Any = None
    is_tax_inclusive: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    ordering: int | None = None
    status: str | None = None
    tax_code: SettingsPricingLevelTaxCode | None = None
    tax_exempt: bool | None = None
    tax_inclusive_based_on: str | None = None


class SettingsPricingLevelList(Dto):
    """One page of ``SettingsPricingLevel`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/pricing_levels",)

    data: list[SettingsPricingLevel] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsTimeZone(Dto):
    """The settings time zone body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/time_zones",)

    code: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    dst_enabled: bool | None = None
    hour: int | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    minute: int | None = None
    name: str | None = None
    object: str | None = None
    offset: int | None = None
    positive: bool | None = None
    status: str | None = None
    time_zone_pattern: str | None = None


class SettingsTimeZoneList(Dto):
    """One page of ``SettingsTimeZone`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/time_zones",)

    data: list[SettingsTimeZone] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsWarehouse(Dto):
    """The settings warehouse body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/warehouses",)

    city: str | None = None
    country: SettingsWarehouseCountry | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    is_default: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    post_code: str | None = None
    state: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsWarehouseList(Dto):
    """One page of ``SettingsWarehouse`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/warehouses",)

    data: list[SettingsWarehouse] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsCurrency(Dto):
    """The settings currency body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/currencies",)

    cash_rounding_interval: float | None = None
    code: str | None = None
    conversion_rate: float | None = None
    country: SettingsCurrencyCountry | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    decimal_places: int | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    rounding: str | None = None
    status: str | None = None
    symbol: str | None = None


class SettingsCurrencyList(Dto):
    """One page of ``SettingsCurrency`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/currencies",)

    data: list[SettingsCurrency] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsItemGroup(Dto):
    """The settings item group body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/item_groups",)

    accounting_code: SettingsItemGroupAccountingCode | None = None
    code: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsItemGroupList(Dto):
    """One page of ``SettingsItemGroup`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/item_groups",)

    data: list[SettingsItemGroup] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class CustomObject(Dto):
    """The custom object body."""

    MEASURED_FROM = ("GET /api/{api_version}/custom_objects",)

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    custom_component: Any = None
    description: str | None = None
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


class CustomObjectList(Dto):
    """One page of ``CustomObject`` records, under ``data``; paged by offset."""

    MEASURED_FROM = (
        "GET /api/{api_version}/custom_objects",
        "GET /api/{api_version}/accounts/{account_id}/custom_objects",
    )

    data: list[CustomObject] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsTax(Dto):
    """The settings tax body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/taxes",)

    code: str | None = None
    country: SettingsTaxCountry | None = None
    country_tax_by_states: list[SettingsTaxCountryTaxByState] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    rate: float | None = None
    status: str | None = None


class SettingsTaxList(Dto):
    """One page of ``SettingsTax`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/taxes",)

    data: list[SettingsTax] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsVariation(Dto):
    """The settings variation body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/variations",)

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsVariationList(Dto):
    """One page of ``SettingsVariation`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/variations",)

    data: list[SettingsVariation] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsPaymentTerm(Dto):
    """The settings payment term body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/payment_terms",)

    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    duration: SettingsPaymentTermDuration | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsPaymentTermList(Dto):
    """One page of ``SettingsPaymentTerm`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/payment_terms",)

    data: list[SettingsPaymentTerm] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsItemGroups(Dto):
    """The settings item groups body, under ``item_group``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/settings/item_groups",
        "GET /api/{api_version}/settings/item_groups/{item_group_id}",
        "PATCH /api/{api_version}/settings/item_groups/{item_group_id}",
        "POST /api/{api_version}/settings/item_groups/{item_group_id}/billing_preferences",
    )

    ENVELOPE_KEY = "item_group"

    accounting_code: SettingsItemGroupsAccountingCode | None = None
    billing_preferences: dict[str, Any] | None = None
    code: str | None = None
    created_by: str | None = None
    created_on: str | None = None
    custom_attributes: list[Any] | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    image_uri: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    manager: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class SettingsCustomLogicScript(Dto):
    """The settings custom logic script body, under ``custom_logic_script``; measured from the v4
    collection, not the instance, so read ``.map`` when a field is unexpectedly None."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/custom_logic_scripts/{custom_logic_script_id}",
    )

    ENVELOPE_KEY = "custom_logic_script"

    action_name: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
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
    object_name: str | None = None
    status: str | None = None
    type: str | None = None


class SettingsCurrencyRead(Dto):
    """The settings currency read body, under ``currency``: the record the listing serves."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/currencies/{currency_id}",)

    ENVELOPE_KEY = "currency"

    cash_rounding_interval: float | None = None
    code: str | None = None
    conversion_rate: float | None = None
    country: SettingsCurrencyReadCountry | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    decimal_places: int | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    rounding: str | None = None
    status: str | None = None
    symbol: str | None = None


class SettingsCustomObjectCustomize(Dto):
    """The settings custom object customize body, under ``custom_object``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/settings/custom_objects/{custom_object_id}/customize",
    )

    ENVELOPE_KEY = "custom_object"

    configuration: SettingsCustomObjectCustomizeConfiguration | None = None
    created: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    relation: str | None = None
    status: str | None = None
    updated: str | None = None
    use_in: str | None = None
    uuid: str | None = None


class SettingsCustomObjects(Dto):
    """The settings custom objects body, under ``custom_object``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/custom_objects/{custom_object_id}",
        "POST /api/{api_version}/settings/custom_objects",
        "PATCH /api/{api_version}/settings/custom_objects/{custom_object_id}",
    )

    ENVELOPE_KEY = "custom_object"

    created: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    custom_component: Any = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    relation: str | None = None
    status: str | None = None
    updated: str | None = None
    use_in: str | None = None
    uuid: str | None = None


class SettingsVariations(Dto):
    """The settings variations body, under ``variation``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/settings/variations",
        "GET /api/{api_version}/settings/variations/{variation_id}",
        "PATCH /api/{api_version}/settings/variations/{variation_id}",
    )

    ENVELOPE_KEY = "variation"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    options: list[Any] | None = None
    status: str | None = None
    uuid: str | None = None


class SettingsTimeZoneRead(Dto):
    """The settings time zone read body, under ``time_zone``: the record the listing serves."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/time_zones/{time_zone_id}",)

    ENVELOPE_KEY = "time_zone"

    code: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    dst_enabled: bool | None = None
    hour: int | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    minute: int | None = None
    name: str | None = None
    object: str | None = None
    offset: int | None = None
    positive: bool | None = None
    status: str | None = None
    time_zone_pattern: str | None = None


class SettingsCustomLogicScripts(Dto):
    """The settings custom logic scripts body."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/custom_logic_scripts",)

    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class Settings(Dto):
    """The settings body, under ``settings``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings",)

    ENVELOPE_KEY = "settings"

    object: str | None = None
    resources: list[SettingsResource] | None = None


class SettingsFieldSettingsItem(Dto):
    """The settings field settings item body."""

    MEASURED_FROM = (
        "PATCH /api/{api_version}/settings/field_settings/account",
        "PATCH /api/{api_version}/settings/field_settings/item",
        "PATCH /api/{api_version}/settings/general_settings/account",
    )

    data: list[SettingsFieldSettingsItemData] | None = None
    general_settings: SettingsFieldSettingsItemGeneralSettings | None = None
    message: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    pagination: Any = None
    url: str | None = None


class SettingsGeneralSettingsItemUpdated(Dto):
    """What ``update_settings_general_settings_item`` answers, under ``general_settings``."""

    MEASURED_FROM = ("PATCH /api/{api_version}/settings/general_settings/item",)

    ENVELOPE_KEY = "general_settings"

    item: SettingsGeneralSettingsItemUpdatedDetail | None = None
    product: SettingsGeneralSettingsItemUpdatedProduct | None = None


class SettingsResource(Dto):
    """One entry of a :class:`Settings`'s ``resources``."""

    href: str | None = None
    name: str | None = None


class SettingsCurrencyReadCountry(Dto):
    """A :class:`SettingsCurrencyRead`'s ``country``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsItemGroupsAccountingCode(Dto):
    """A :class:`SettingsItemGroups`'s ``accounting_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsCustomObjectCustomizeConfiguration(Dto):
    """A :class:`SettingsCustomObjectCustomize`'s ``configuration``."""

    attributes: list[SettingsCustomObjectCustomizeConfigurationAttribute] | None = None


class SettingsFieldSettingsItemGeneralSettings(Dto):
    """A :class:`SettingsFieldSettingsItem`'s ``general_settings``."""

    account: SettingsFieldSettingsItemGeneralSettingsAccount | None = None


class SettingsFieldSettingsItemData(Dto):
    """One entry of a :class:`SettingsFieldSettingsItem`'s ``data``."""

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_code: str | None = None
    # Null in every record measured, so untyped.
    editable: Any = None
    enabled: bool | None = None
    entity: str | None = None
    field_name: str | None = None
    field_type: str | None = None
    global_search: bool | None = None
    group_key: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    mandatory: bool | None = None
    # Null in every record measured, so untyped.
    note: Any = None
    object: str | None = None
    sort_order: int | None = None


class SettingsGeneralSettingsItemUpdatedDetail(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdated`'s ``item``."""

    available_charge_types: SettingsGeneralSettingsItemUpdatedDetailAvailableChargeTypes | None = (
        None
    )
    available_pricing_methods: (
        SettingsGeneralSettingsItemUpdatedDetailAvailablePricingMethods | None
    ) = None
    charging_period_can_vary_from_billing_period: str | None = None
    charging_start_date_can_vary_from_billing_start_date: str | None = None
    enable_back_order: str | None = None
    enable_batch_tracking: str | None = None
    enable_bundle_item: str | None = None
    enable_direct_cost_item: str | None = None
    enable_family_cost_item: str | None = None
    enable_fixed_asset_item: str | None = None
    enable_gift_certificate_based_item: str | None = None
    enable_inventory_costing: str | None = None
    enable_inventory_management: str | None = None
    enable_pricing_profile: str | None = None
    enable_purchase: str | None = None
    enable_sales: str | None = None
    enable_serialization: str | None = None
    enable_supplier_management: str | None = None
    enable_variation: str | None = None
    enable_variation_based_item: str | None = None
    enable_warehouse_management: str | None = None
    enable_workflow_approval_for_item: str | None = None
    inventory_adjustment_rules: (
        SettingsGeneralSettingsItemUpdatedDetailInventoryAdjustmentRules | None
    ) = None
    item_grouping: SettingsGeneralSettingsItemUpdatedDetailItemGrouping | None = None
    item_management: SettingsGeneralSettingsItemUpdatedDetailItemManagement | None = None
    pre_order: SettingsGeneralSettingsItemUpdatedDetailPreOrder | None = None
    pricing_period_can_vary_from_charging_period: (
        SettingsGeneralSettingsItemUpdatedDetailPricingPeriodCanVaryFromChargingPeriod | None
    ) = None
    purchase_price_entered_is_inclusive_of_tax: (
        SettingsGeneralSettingsItemUpdatedDetailPurchasePriceEnteredIsInclusiveOfTax | None
    ) = None
    require_name_to_be_unique: str | None = None
    sale_price_entered_is_inclusive_of_tax: (
        SettingsGeneralSettingsItemUpdatedDetailSalePriceEnteredIsInclusiveOfTax | None
    ) = None
    use_on_sale_price: str | None = None
    use_pricing_level: str | None = None
    use_scheduling_of_future_pricing: str | None = None
    use_shipping_profile: str | None = None
    use_volume_pricing: SettingsGeneralSettingsItemUpdatedDetailUseVolumePricing | None = None


class SettingsGeneralSettingsItemUpdatedProduct(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdated`'s ``product``."""

    allow_item_sell_multi_quantity: str | None = None
    allow_plan_sell_multi_quantity: str | None = None
    allow_product_sell_multi_quantity: str | None = None
    allow_rate_sell_multi_quantity: str | None = None
    item_quantity_use: str | None = None
    plan_quantity_use: str | None = None
    product_quantity_use: str | None = None
    rate_quantity_use: str | None = None


class SettingsCurrencyCountry(Dto):
    """A :class:`SettingsCurrency`'s ``country``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsDiscountProfileAccountingCode(Dto):
    """A :class:`SettingsDiscountProfile`'s ``accounting_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsDiscountProfileTaxCode(Dto):
    """A :class:`SettingsDiscountProfile`'s ``tax_code``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class SettingsItemGroupAccountingCode(Dto):
    """A :class:`SettingsItemGroup`'s ``accounting_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsPaymentProcessorCurrency(Dto):
    """A :class:`SettingsPaymentProcessor`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsPaymentProcessorAccountingCode(Dto):
    """A :class:`SettingsPaymentProcessor`'s ``accounting_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsPaymentTermDuration(Dto):
    """A :class:`SettingsPaymentTerm`'s ``duration``."""

    count: int | None = None
    period: str | None = None


class SettingsPricingLevelTaxCode(Dto):
    """A :class:`SettingsPricingLevel`'s ``tax_code``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class SettingsShippingProfileTaxRule(Dto):
    """A :class:`SettingsShippingProfile`'s ``tax_rule``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class SettingsShippingProfileAccountingCode(Dto):
    """A :class:`SettingsShippingProfile`'s ``accounting_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsTaxCountry(Dto):
    """A :class:`SettingsTax`'s ``country``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsTaxCountryTaxByState(Dto):
    """One entry of a :class:`SettingsTax`'s ``country_tax_by_states``."""

    created_on: str | None = None
    id: str | None = None
    last_updated_on: str | None = None
    object: str | None = None
    rate: float | None = None
    # Null in every record measured, so untyped.
    state: Any = None
    status: str | None = None


class SettingsWarehouseCountry(Dto):
    """A :class:`SettingsWarehouse`'s ``country``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsCustomObjectCustomizeConfigurationAttribute(Dto):
    """One entry of a :class:`SettingsCustomObjectCustomizeConfiguration`'s ``attributes``."""

    name: str | None = None
    order: int | None = None


class SettingsFieldSettingsItemGeneralSettingsAccount(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettings`'s ``account``."""

    account_grouping: SettingsFieldSettingsItemGeneralSettingsAccountAccountGrouping | None = None
    account_management: SettingsFieldSettingsItemGeneralSettingsAccountAccountManagement | None = (
        None
    )
    additional_contact_1: (
        SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact1 | None
    ) = None
    additional_contact_2: (
        SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact2 | None
    ) = None
    additional_contact_3: (
        SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact3 | None
    ) = None
    billing_contact: SettingsFieldSettingsItemGeneralSettingsAccountBillingContact | None = None
    creation_of_subsidiary_account: (
        SettingsFieldSettingsItemGeneralSettingsAccountCreationOfSubsidiaryAccount | None
    ) = None
    enable_workflow_approval_for_account: str | None = None
    referral_tracking_at_account_level: (
        SettingsFieldSettingsItemGeneralSettingsAccountReferralTrackingAtAccountLevel | None
    ) = None
    require_email_address_for_account: str | None = None
    require_name_to_be_unique: str | None = None
    sales_rep_tracking_at_account_level: (
        SettingsFieldSettingsItemGeneralSettingsAccountSalesRepTrackingAtAccountLevel | None
    ) = None
    send_communication_as_groups: str | None = None
    shipping_contact: SettingsFieldSettingsItemGeneralSettingsAccountShippingContact | None = None
    unique_email_address_for_account: str | None = None
    unique_email_address_for_contacts: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailAvailableChargeTypes(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s ``available_charge_types``."""

    metered: str | None = None
    one_off: str | None = None
    recurring: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailAvailablePricingMethods(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s ``available_pricing_methods``."""

    discount_based: str | None = None
    markup_based: str | None = None
    standard: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailItemGrouping(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s ``item_grouping``."""

    # Null in every record measured, so untyped.
    default_group: Any = None
    enabled: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailItemManagement(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s ``item_management``."""

    # Null in every record measured, so untyped.
    default_manager: Any = None
    enabled: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailUseVolumePricing(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s ``use_volume_pricing``."""

    all_units_fixed_pricing: str | None = None
    all_units_per_unit_pricing: str | None = None
    enabled: str | None = None
    incremental_fixed_pricing: str | None = None
    incremental_per_unit_pricing: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailPricingPeriodCanVaryFromChargingPeriod(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s
    ``pricing_period_can_vary_from_charging_period``."""

    # Null in every record measured, so untyped.
    default_pricing_period: Any = None
    enabled: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailSalePriceEnteredIsInclusiveOfTax(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s
    ``sale_price_entered_is_inclusive_of_tax``."""

    enabled: str | None = None
    # Null in every record measured, so untyped.
    tax: Any = None
    tax_included_in_sales_price_is_based_on: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailPurchasePriceEnteredIsInclusiveOfTax(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s
    ``purchase_price_entered_is_inclusive_of_tax``."""

    enabled: str | None = None
    tax: (
        SettingsGeneralSettingsItemUpdatedDetailPurchasePriceEnteredIsInclusiveOfTaxDetail | None
    ) = None


class SettingsGeneralSettingsItemUpdatedDetailInventoryAdjustmentRules(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s ``inventory_adjustment_rules``."""

    quantity_available_for_sale: str | None = None
    quantity_available_for_sale_determination: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailPreOrder(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetail`'s ``pre_order``."""

    enabled: str | None = None
    number_of_period: str | None = None
    period: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountAccountGrouping(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s ``account_grouping``."""

    # Null in every record measured, so untyped.
    default_group: Any = None
    enabled: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountCreationOfSubsidiaryAccount(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s
    ``creation_of_subsidiary_account``."""

    # Null in every record measured, so untyped.
    default_group: Any = None
    enabled: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountAccountManagement(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s ``account_management``."""

    # Null in every record measured, so untyped.
    default_manager: Any = None
    enabled: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountSalesRepTrackingAtAccountLevel(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s
    ``sales_rep_tracking_at_account_level``."""

    # Null in every record measured, so untyped.
    default_sales_rep_tracking: Any = None
    enabled: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountReferralTrackingAtAccountLevel(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s
    ``referral_tracking_at_account_level``."""

    # Null in every record measured, so untyped.
    default_referral_tracking: Any = None
    enabled: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountBillingContact(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s ``billing_contact``."""

    display_name: str | None = None
    enabled: str | None = None
    require_email_address_for_billing_contact: str | None = None
    type: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountShippingContact(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s ``shipping_contact``."""

    display_name: str | None = None
    enabled: str | None = None
    require_email_address_for_shipping_contact: str | None = None
    type: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact1(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s ``additional_contact_1``."""

    display_name: str | None = None
    enabled: str | None = None
    require_email_address_for_additional_contact_1: str | None = None
    type: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact2(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s ``additional_contact_2``."""

    display_name: str | None = None
    enabled: str | None = None
    require_email_address_for_additional_contact_2: str | None = None
    type: str | None = None


class SettingsFieldSettingsItemGeneralSettingsAccountAdditionalContact3(Dto):
    """A :class:`SettingsFieldSettingsItemGeneralSettingsAccount`'s ``additional_contact_3``."""

    display_name: str | None = None
    enabled: str | None = None
    require_email_address_for_additional_contact_3: str | None = None
    type: str | None = None


class SettingsGeneralSettingsItemUpdatedDetailPurchasePriceEnteredIsInclusiveOfTaxDetail(Dto):
    """A :class:`SettingsGeneralSettingsItemUpdatedDetailPurchasePriceEnteredIsInclusiveOfTax`'s
    ``tax``."""

    uuid: str | None = None


class SettingsCustomObjectDefinition(Dto):
    """One custom object definition, as ``/settings/custom_objects`` serves it."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/custom_objects",
        "GET /api/{api_version}/settings/custom_objects/{custom_object_id}",
    )

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    relation: str | None = None
    status: str | None = None
    use_in: str | None = None


class SettingsCustomObjectDefinitionList(Dto):
    """One page of ``SettingsCustomObjectDefinition`` records, under ``data``; paged by cursor."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/custom_objects",)

    data: list[SettingsCustomObjectDefinition] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsCustomObjectDefinitionRead(SettingsCustomObjectDefinition):
    """One custom object definition, under ``custom_object``: the record the listing serves."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/custom_objects/{custom_object_id}",)

    ENVELOPE_KEY = "custom_object"


class SettingsDiscountProfileRead(SettingsDiscountProfile):
    """One discount profile, under ``discount_profile``: the record the listing serves."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/discount_profiles/{discount_profile_id}",
        "POST /api/{api_version}/settings/discount_profiles",
        "PATCH /api/{api_version}/settings/discount_profiles/{discount_profile_id}",
    )

    ENVELOPE_KEY = "discount_profile"


class SettingsPaymentProcessorRead(SettingsPaymentProcessor):
    """One payment processor, under ``payment_processor``: the record the listing serves."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/payment_processors/{payment_processor_id}",)

    ENVELOPE_KEY = "payment_processor"


class SettingsPaymentTermRead(SettingsPaymentTerm):
    """One payment term, under ``payment_term``: the record the listing serves."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/payment_terms/{payment_term_id}",)

    ENVELOPE_KEY = "payment_term"


class SettingsPricingLevelRead(SettingsPricingLevel):
    """One pricing level, under ``pricing_level``: the record the listing serves."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/pricing_levels/{pricing_level_id}",
        "PATCH /api/{api_version}/settings/pricing_levels/{pricing_level_id}",
    )

    ENVELOPE_KEY = "pricing_level"


class SettingsShippingProfileRead(SettingsShippingProfile):
    """One shipping profile, under ``shipping_profile``: the record the listing serves."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/shipping_profiles/{shipping_profile_id}",
        "POST /api/{api_version}/settings/shipping_profiles",
    )

    ENVELOPE_KEY = "shipping_profile"


class SettingsTaxRead(SettingsTax):
    """One tax, under ``tax``: the record the listing serves."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/taxes/{tax_id}",)

    ENVELOPE_KEY = "tax"


class SettingsWarehouseRead(SettingsWarehouse):
    """One warehouse, under ``warehouse``: the record the listing serves."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/warehouses/{warehouse_id}",
        "POST /api/{api_version}/settings/warehouses",
        "PATCH /api/{api_version}/settings/warehouses/{warehouse_id}",
    )

    ENVELOPE_KEY = "warehouse"


class SettingsFieldSettingList(Dto):
    """One page of ``SettingsFieldSettingsItemData`` records, under ``data``; paged by cursor."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/field_settings",)

    data: list[SettingsFieldSettingsItemData] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsFieldSettingRead(SettingsFieldSettingsItemData):
    """One field setting, under ``field_setting``: the record the listing serves."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/field_settings/{field_setting_id}",)

    ENVELOPE_KEY = "field_setting"


class SettingsCustomLogicScriptSaved(SettingsCustomLogicScript):
    """What the custom logic script writes answer, under ``custom_logic_script``: the read's fields
    and ``code``, which the server does not store."""

    MEASURED_FROM = (
        "POST /api/{api_version}/settings/custom_logic_scripts",
        "PATCH /api/{api_version}/settings/custom_logic_scripts/{custom_logic_script_id}",
    )

    ENVELOPE_KEY = "custom_logic_script"

    # Null in every record measured, so untyped.
    code: Any = None


class SettingsPaymentTermUpdated(SettingsPaymentTermRead):
    """What ``update_settings_payment_term`` answers, under ``payment_term``: the read's fields and
    ``display_order``."""

    MEASURED_FROM = ("PATCH /api/{api_version}/settings/payment_terms/{payment_term_id}",)

    ENVELOPE_KEY = "payment_term"

    display_order: int | None = None


class SettingsPaymentProcessorSaved(Dto):
    """What ``create_settings_payment_processor`` answers, under ``payment_processor``: ``gateway_name`` and ``credentials`` where the read has ``provider``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/settings/payment_processors",
        "PATCH /api/{api_version}/settings/payment_processors/{payment_processor_id}",
    )

    ENVELOPE_KEY = "payment_processor"

    # Null in every record measured, so untyped.
    accounting_code: Any = None
    conversion_rate: float | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    credentials: Any = None
    currency: SettingsPaymentProcessorSavedCurrency | None = None
    description: str | None = None
    disconnected: bool | None = None
    display_name: str | None = None
    gateway_name: str | None = None
    gateway_type: str | None = None
    href: str | None = None
    id: str | None = None
    integration_state: str | None = None
    is_default: bool | None = None
    is_foreign_currency: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    provider: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsPaymentProcessorSavedCurrency(Dto):
    """A :class:`SettingsPaymentProcessorSaved`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsPaymentTermCreated(Dto):
    """What ``create_settings_payment_term`` answers, under ``payment_term``: a flat ``period`` and ``duration`` where the read nests them."""

    MEASURED_FROM = ("POST /api/{api_version}/settings/payment_terms",)

    ENVELOPE_KEY = "payment_term"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    duration: int | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    ordering: Any = None
    period: str | None = None
    status: str | None = None


class SettingsPricingLevelCreated(Dto):
    """What ``create_settings_pricing_level`` answers, under ``pricing_level``: ``price_tax_inclusive`` where the read has three tax fields."""

    MEASURED_FROM = ("POST /api/{api_version}/settings/pricing_levels",)

    ENVELOPE_KEY = "pricing_level"

    # Null in every record measured, so untyped.
    built_in_item: Any = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    is_default: Any = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    ordering: int | None = None
    # Null in every record measured, so untyped.
    price_tax_inclusive: Any = None
    status: str | None = None
    # Null in every record measured, so untyped.
    tax_exempt: Any = None


class SettingsGeneralSettings(Dto):
    """One group of general settings, under ``general_settings``, keyed by the group; ``item`` and ``order`` also carry ``product``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/general_settings/{group}",)

    ENVELOPE_KEY = "general_settings"

    account: SettingsFieldSettingsItemGeneralSettingsAccount | None = None
    dashboard: SettingsGeneralSettingsDashboard | None = None
    date_and_time: SettingsGeneralSettingsDateAndTime | None = None
    # Keys are the instance's own setting names, so a mapping.
    display: dict[str, Any] | None = None
    # Keys are the instance's own setting names, so a mapping.
    general: dict[str, Any] | None = None
    item: SettingsGeneralSettingsItemUpdatedDetail | None = None
    labour: SettingsGeneralSettingsLabour | None = None
    order: SettingsGeneralSettingsOrder | None = None
    portal: SettingsGeneralSettingsPortal | None = None
    product: SettingsGeneralSettingsItemUpdatedProduct | None = None
    purchase: SettingsGeneralSettingsPurchase | None = None
    security: SettingsGeneralSettingsSecurity | None = None
    transaction: SettingsGeneralSettingsTransaction | None = None


class SettingsGeneralSettingsDashboard(Dto):
    """A :class:`SettingsGeneralSettings`'s ``dashboard``."""

    accounting: str | None = None
    # Null in every record measured, so untyped.
    defaultDashboard: Any = None
    executive: str | None = None
    finance: str | None = None
    production: str | None = None
    purchase: str | None = None
    sales: str | None = None


class SettingsGeneralSettingsDateAndTime(Dto):
    """A :class:`SettingsGeneralSettings`'s ``date_and_time``."""

    date_format: str | None = None
    # Null in every record measured, so untyped.
    first_day_of_week: Any = None
    time_format: str | None = None
    time_zone: str | None = None


class SettingsGeneralSettingsLabour(Dto):
    """A :class:`SettingsGeneralSettings`'s ``labour``."""

    require_email_address_for_labour: str | None = None
    unique_email_address: str | None = None
    unique_labour_name: str | None = None


class SettingsGeneralSettingsOrder(Dto):
    """A :class:`SettingsGeneralSettings`'s ``order``."""

    allow_name_to_be_changed_in_order: str | None = None
    allow_unit_price_to_be_changed_in_order: str | None = None
    default_fulfillment_status: str | None = None
    # Null in every record measured, so untyped.
    default_shipping_profile: Any = None
    displayed_price_is_inclusive_of_tax: str | None = None
    enable_booking: str | None = None
    enable_last_sale_price_look_up_for_an_account: str | None = None
    enable_order_backdating: str | None = None
    enable_quote: str | None = None
    order_management: SettingsGeneralSettingsOrderOrderManagement | None = None
    referral_tracking_at_order_level: (
        SettingsGeneralSettingsOrderReferralTrackingAtOrderLevel | None
    ) = None
    sales_rep_tracking_at_order_level: (
        SettingsGeneralSettingsOrderSalesRepTrackingAtOrderLevel | None
    ) = None
    use_global_warehouse: str | None = None


class SettingsGeneralSettingsOrderOrderManagement(Dto):
    """A :class:`SettingsGeneralSettingsOrder`'s ``order_management``."""

    # Null in every record measured, so untyped.
    default_manager: Any = None
    enabled: str | None = None


class SettingsGeneralSettingsOrderReferralTrackingAtOrderLevel(Dto):
    """A :class:`SettingsGeneralSettingsOrder`'s ``referral_tracking_at_order_level``."""

    # Null in every record measured, so untyped.
    default_referral_tracking: Any = None
    enabled: str | None = None


class SettingsGeneralSettingsOrderSalesRepTrackingAtOrderLevel(Dto):
    """A :class:`SettingsGeneralSettingsOrder`'s ``sales_rep_tracking_at_order_level``."""

    # Null in every record measured, so untyped.
    default_sales_rep_tracking: Any = None
    enabled: str | None = None


class SettingsGeneralSettingsPortal(Dto):
    """A :class:`SettingsGeneralSettings`'s ``portal``."""

    # Keys are the instance's own setting names, so a mapping.
    contacts: dict[str, Any] | None = None
    enableCustomerPortal: str | None = None
    enableInviteToActivePortalForContact: str | None = None
    enableSpecifyPortalPasswordForContact: str | None = None
    # Keys are the instance's own setting names, so a mapping.
    settings: dict[str, Any] | None = None


class SettingsGeneralSettingsPurchase(Dto):
    """A :class:`SettingsGeneralSettings`'s ``purchase``."""

    allow_modification_of_following_purchase_credit_note_fields: (
        SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseCreditNoteFields | None
    ) = None
    allow_modification_of_following_purchase_invoice_fields: (
        SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseInvoiceFields | None
    ) = None
    allow_modification_of_following_purchase_payment_fields: (
        SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchasePaymentFields | None
    ) = None
    allow_modification_of_following_purchase_refund_fields: (
        SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseRefundFields | None
    ) = None
    enable_last_purchase_price_look_up: str | None = None
    enable_purchase_quote: str | None = None
    enable_workflow_approval_for_purchase_credit_note: str | None = None
    enable_workflow_approval_for_purchase_invoice: str | None = None
    enable_workflow_approval_for_purchase_order: str | None = None
    enable_workflow_approval_for_purchase_payment: str | None = None
    enable_workflow_approval_for_purchase_refund: str | None = None
    inventory_is_adjusted_when: str | None = None
    supplier_invoice_id_should_be_unique: str | None = None
    use_global_warehouse: str | None = None


class SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseCreditNoteFields(Dto):
    """A :class:`SettingsGeneralSettingsPurchase`'s ``allow_modification_of_following_purchase_credit_note_fields``."""

    refundable: str | None = None


class SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseInvoiceFields(Dto):
    """A :class:`SettingsGeneralSettingsPurchase`'s ``allow_modification_of_following_purchase_invoice_fields``."""

    due_date: str | None = None
    issue_date: str | None = None


class SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchasePaymentFields(Dto):
    """A :class:`SettingsGeneralSettingsPurchase`'s ``allow_modification_of_following_purchase_payment_fields``."""

    payment_date: str | None = None
    payment_processor: str | None = None
    payment_reference: str | None = None


class SettingsGeneralSettingsPurchaseAllowModificationOfFollowingPurchaseRefundFields(Dto):
    """A :class:`SettingsGeneralSettingsPurchase`'s ``allow_modification_of_following_purchase_refund_fields``."""

    refund_date: str | None = None
    refund_reference: str | None = None


class SettingsGeneralSettingsSecurity(Dto):
    """A :class:`SettingsGeneralSettings`'s ``security``."""

    enable_force_session_expire: str | None = None
    enable_two_factor_authentication: str | None = None
    implementerLogin: str | None = None
    session_expire_limit_hour: str | None = None


class SettingsGeneralSettingsTransaction(Dto):
    """A :class:`SettingsGeneralSettings`'s ``transaction``."""

    # Null in every record measured, so untyped.
    accounting_method: Any = None
    allow_modification_of_following_credit_note_fields: (
        SettingsGeneralSettingsTransactionAllowModificationOfFollowingCreditNoteFields | None
    ) = None
    allow_modification_of_following_invoice_fields: (
        SettingsGeneralSettingsTransactionAllowModificationOfFollowingInvoiceFields | None
    ) = None
    allow_modification_of_following_payment_fields: (
        SettingsGeneralSettingsTransactionAllowModificationOfFollowingPaymentFields | None
    ) = None
    allow_modification_of_following_refund_fields: (
        SettingsGeneralSettingsTransactionAllowModificationOfFollowingRefundFields | None
    ) = None
    available_mediums_for_communication_preference: (
        SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreference | None
    ) = None
    create_negative_charge_to_accommodate_adjustment_required_for_order_cancel_or_change: (
        str | None
    ) = None
    default_accounting_codes: SettingsGeneralSettingsTransactionDefaultAccountingCodes | None = None
    # Null in every record measured, so untyped.
    default_shipping_profile: Any = None
    disable_notification_for_invoice_with_charges_of_zero_amount: str | None = None
    displayed_price_is_inclusive_of_tax: str | None = None
    enable_creation_of_automatic_payment_surcharge: str | None = None
    enable_discount_profile: str | None = None
    update_current_invoice_to_include_charge_adjustments: str | None = None
    update_invoice_to_include_current_payment_surcharge: str | None = None


class SettingsGeneralSettingsTransactionAllowModificationOfFollowingCreditNoteFields(Dto):
    """A :class:`SettingsGeneralSettingsTransaction`'s ``allow_modification_of_following_credit_note_fields``."""

    credit_note_date: str | None = None
    refundable: str | None = None


class SettingsGeneralSettingsTransactionAllowModificationOfFollowingInvoiceFields(Dto):
    """A :class:`SettingsGeneralSettingsTransaction`'s ``allow_modification_of_following_invoice_fields``."""

    billing_period: str | None = None
    charge_period: str | None = None
    due_date: str | None = None
    issue_date: str | None = None


class SettingsGeneralSettingsTransactionAllowModificationOfFollowingPaymentFields(Dto):
    """A :class:`SettingsGeneralSettingsTransaction`'s ``allow_modification_of_following_payment_fields``."""

    payment_date: str | None = None
    payment_processor: str | None = None
    payment_reference: str | None = None


class SettingsGeneralSettingsTransactionAllowModificationOfFollowingRefundFields(Dto):
    """A :class:`SettingsGeneralSettingsTransaction`'s ``allow_modification_of_following_refund_fields``."""

    refund_date: str | None = None
    refund_reference: str | None = None


class SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreference(Dto):
    """A :class:`SettingsGeneralSettingsTransaction`'s ``available_mediums_for_communication_preference``."""

    email: (
        SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceEmail | None
    ) = None
    postal_mail: (
        SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferencePostalMail
        | None
    ) = None
    text_message: (
        SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceTextMessage
        | None
    ) = None
    voice_mail: (
        SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceVoiceMail | None
    ) = None


class SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceEmail(Dto):
    """A :class:`SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreference`'s ``email``."""

    default: str | None = None
    enabled: str | None = None


class SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferencePostalMail(Dto):
    """A :class:`SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreference`'s ``postal_mail``."""

    default: str | None = None
    enabled: str | None = None


class SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceTextMessage(Dto):
    """A :class:`SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreference`'s ``text_message``."""

    default: str | None = None
    enabled: str | None = None


class SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreferenceVoiceMail(Dto):
    """A :class:`SettingsGeneralSettingsTransactionAvailableMediumsForCommunicationPreference`'s ``voice_mail``."""

    default: str | None = None
    enabled: str | None = None


class SettingsGeneralSettingsTransactionDefaultAccountingCodes(Dto):
    """A :class:`SettingsGeneralSettingsTransaction`'s ``default_accounting_codes``."""

    account_payable: str | None = None
    account_receivable: str | None = None
    cash_and_cash_equivalent: str | None = None
    cost_of_goods_sold: str | None = None
    credit_note_payable: str | None = None
    deduction: str | None = None
    event_charge: str | None = None
    inventory: str | None = None
    payment_surcharge: str | None = None
    rounding: str | None = None
    sales_revenue: str | None = None
    tax: str | None = None
