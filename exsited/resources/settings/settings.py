"""Settings endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.settings import settings_urls
from exsited.resources.settings.settings_dto import (
    CustomObjectList,
    Settings,
    SettingsCurrencyList,
    SettingsCurrencyRead,
    SettingsCustomLogicScript,
    SettingsCustomLogicScripts,
    SettingsCustomLogicScriptSaved,
    SettingsCustomObjectCustomize,
    SettingsCustomObjectDefinitionList,
    SettingsCustomObjectDefinitionRead,
    SettingsCustomObjects,
    SettingsDiscountProfileList,
    SettingsDiscountProfileRead,
    SettingsFieldSettingList,
    SettingsFieldSettingRead,
    SettingsFieldSettingsItem,
    SettingsGeneralSettings,
    SettingsGeneralSettingsItemUpdated,
    SettingsItemGroupList,
    SettingsItemGroups,
    SettingsPaymentProcessorList,
    SettingsPaymentProcessorRead,
    SettingsPaymentProcessorSaved,
    SettingsPaymentTermCreated,
    SettingsPaymentTermList,
    SettingsPaymentTermRead,
    SettingsPaymentTermUpdated,
    SettingsPricingLevelCreated,
    SettingsPricingLevelList,
    SettingsPricingLevelRead,
    SettingsShippingProfileList,
    SettingsShippingProfileRead,
    SettingsTaxList,
    SettingsTaxRead,
    SettingsTimeZoneList,
    SettingsTimeZoneRead,
    SettingsVariationList,
    SettingsVariations,
    SettingsWarehouseList,
    SettingsWarehouseRead,
)

__all__ = [
    "get_custom_objects",
    "get_settings",
    "get_custom_object",
    "get_settings_currencies",
    "get_settings_custom_logic_scripts",
    "create_settings_custom_object",
    "get_settings_discount_profiles",
    "get_settings_item_groups",
    "create_settings_item_group",
    "get_settings_payment_processors",
    "get_settings_payment_terms",
    "get_settings_pricing_levels",
    "get_settings_shipping_profiles",
    "get_settings_taxes",
    "get_settings_time_zones",
    "get_settings_variations",
    "create_settings_variation",
    "get_settings_warehouses",
    "get_settings_currency",
    "get_settings_custom_logic_script",
    "delete_settings_custom_object",
    "update_settings_custom_object",
    "update_settings_field_settings_account",
    "update_settings_field_settings_item",
    "update_settings_general_settings_account",
    "update_settings_general_settings_item",
    "delete_settings_item_group",
    "get_settings_item_group",
    "update_settings_item_group",
    "get_settings_time_zone",
    "get_settings_variation",
    "update_settings_variation",
    "create_settings_custom_object_customize",
    "create_settings_item_group_billing_preference",
    "get_settings_custom_objects",
    "get_settings_custom_object",
    "create_custom_object",
    "update_custom_object",
    "delete_custom_object",
    "create_settings_currency",
    "update_settings_currency",
    "create_settings_custom_logic_script",
    "update_settings_custom_logic_script",
    "delete_settings_custom_logic_script",
    "create_settings_discount_profile",
    "get_settings_discount_profile",
    "update_settings_discount_profile",
    "delete_settings_discount_profile",
    "get_settings_field_settings",
    "get_settings_field_setting",
    "get_settings_general_settings",
    "get_settings_general_setting",
    "update_settings_general_settings_dashboard",
    "update_settings_general_settings_date_and_time",
    "update_settings_general_settings_display",
    "update_settings_general_settings_general",
    "update_settings_general_settings_labour",
    "update_settings_general_settings_order",
    "update_settings_general_settings_portal",
    "update_settings_general_settings_purchase",
    "update_settings_general_settings_security",
    "update_settings_general_settings_transaction",
    "create_settings_payment_processor",
    "get_settings_payment_processor",
    "update_settings_payment_processor",
    "delete_settings_payment_processor",
    "create_settings_payment_term",
    "get_settings_payment_term",
    "update_settings_payment_term",
    "delete_settings_payment_term",
    "create_settings_pricing_level",
    "get_settings_pricing_level",
    "update_settings_pricing_level",
    "delete_settings_pricing_level",
    "create_settings_shipping_profile",
    "get_settings_shipping_profile",
    "update_settings_shipping_profile",
    "delete_settings_shipping_profile",
    "create_settings_warehouse",
    "get_settings_warehouse",
    "update_settings_warehouse",
    "delete_settings_warehouse",
    "create_settings_tax",
    "get_settings_tax",
    "update_settings_tax",
    "delete_settings_variation",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

SettingsPayload = Mapping[str, Any] | str | Dto


def get_custom_objects(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomObjectList]:
    """Custom object definitions - ``GET /custom_objects``."""
    return client.send_get_request(
        settings_urls.CUSTOM_OBJECTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomObjectList,
    )


def get_settings(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Settings]:
    """All settings - ``GET /settings``."""
    return client.send_get_request(
        settings_urls.SETTINGS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Settings,
    )


def get_custom_object(
    client: Any,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomObjects]:
    """Single custom object definition - ``GET /custom_objects/{custom_object_id}``."""
    return client.send_get_request(
        settings_urls.CUSTOM_OBJECT,
        path_params={"custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomObjects,
    )


def get_settings_currencies(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCurrencyList]:
    """List currencies - ``GET /settings/currencies``."""
    return client.send_get_request(
        settings_urls.SETTINGS_CURRENCIES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCurrencyList,
    )


def get_settings_custom_logic_scripts(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomLogicScripts]:
    """List custom logic scripts - ``GET /settings/custom_logic_scripts``."""
    return client.send_get_request(
        settings_urls.SETTINGS_CUSTOM_LOGIC_SCRIPTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomLogicScripts,
    )


def create_settings_custom_object(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomObjects]:
    """Create custom object - ``POST /settings/custom_objects``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_CUSTOM_OBJECTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomObjects,
    )


def get_settings_discount_profiles(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDiscountProfileList]:
    """List discount profiles - ``GET /settings/discount_profiles``."""
    return client.send_get_request(
        settings_urls.SETTINGS_DISCOUNT_PROFILES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDiscountProfileList,
    )


def get_settings_item_groups(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsItemGroupList]:
    """List item groups - ``GET /settings/item_groups``."""
    return client.send_get_request(
        settings_urls.SETTINGS_ITEM_GROUPS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsItemGroupList,
    )


def create_settings_item_group(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsItemGroups]:
    """Create item group - ``POST /settings/item_groups``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_ITEM_GROUPS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsItemGroups,
    )


def get_settings_payment_processors(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPaymentProcessorList]:
    """List payment processors - ``GET /settings/payment_processors``."""
    return client.send_get_request(
        settings_urls.SETTINGS_PAYMENT_PROCESSORS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPaymentProcessorList,
    )


def get_settings_payment_terms(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPaymentTermList]:
    """List payment terms - ``GET /settings/payment_terms``."""
    return client.send_get_request(
        settings_urls.SETTINGS_PAYMENT_TERMS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPaymentTermList,
    )


def get_settings_pricing_levels(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPricingLevelList]:
    """List pricing levels - ``GET /settings/pricing_levels``."""
    return client.send_get_request(
        settings_urls.SETTINGS_PRICING_LEVELS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPricingLevelList,
    )


def get_settings_shipping_profiles(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingProfileList]:
    """List shipping profiles - ``GET /settings/shipping_profiles``."""
    return client.send_get_request(
        settings_urls.SETTINGS_SHIPPING_PROFILES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingProfileList,
    )


def get_settings_taxes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTaxList]:
    """List taxes - ``GET /settings/taxes``."""
    return client.send_get_request(
        settings_urls.SETTINGS_TAXES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTaxList,
    )


def get_settings_time_zones(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTimeZoneList]:
    """List time zones - ``GET /settings/time_zones``."""
    return client.send_get_request(
        settings_urls.SETTINGS_TIME_ZONES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTimeZoneList,
    )


def get_settings_variations(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsVariationList]:
    """List variations - ``GET /settings/variations``."""
    return client.send_get_request(
        settings_urls.SETTINGS_VARIATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsVariationList,
    )


def create_settings_variation(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsVariations]:
    """Create variation - ``POST /settings/variations``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_VARIATIONS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsVariations,
    )


def get_settings_warehouses(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsWarehouseList]:
    """List warehouses - ``GET /settings/warehouses``."""
    return client.send_get_request(
        settings_urls.SETTINGS_WAREHOUSES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsWarehouseList,
    )


def get_settings_currency(
    client: Any,
    currency_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCurrencyRead]:
    """Get single - ``GET /settings/currencies/{currency_id}``."""
    return client.send_get_request(
        settings_urls.SETTINGS_CURRENCY,
        path_params={"currency_id": currency_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCurrencyRead,
    )


def get_settings_custom_logic_script(
    client: Any,
    custom_logic_script_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomLogicScript]:
    """Get single - ``GET /settings/custom_logic_scripts/{custom_logic_script_id}``."""
    return client.send_get_request(
        settings_urls.SETTINGS_CUSTOM_LOGIC_SCRIPT,
        path_params={"custom_logic_script_id": custom_logic_script_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomLogicScript,
    )


def delete_settings_custom_object(
    client: Any,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete custom object - ``DELETE /settings/custom_objects/{custom_object_id}``; answered
    ``204``."""
    return client.send_delete_request(
        settings_urls.SETTINGS_CUSTOM_OBJECT,
        path_params={"custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_custom_object(
    client: Any,
    custom_object_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomObjects]:
    """Update custom object - ``PATCH /settings/custom_objects/{custom_object_id}``; answered
    ``202``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_CUSTOM_OBJECT,
        path_params={"custom_object_id": custom_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomObjects,
    )


def update_settings_field_settings_account(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFieldSettingsItem]:
    """Update account field settings - ``PATCH /settings/field_settings/account``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_FIELD_SETTINGS_ACCOUNT,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFieldSettingsItem,
    )


def update_settings_field_settings_item(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFieldSettingsItem]:
    """Update item field settings - ``PATCH /settings/field_settings/item``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_FIELD_SETTINGS_ITEM,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFieldSettingsItem,
    )


def update_settings_general_settings_account(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFieldSettingsItem]:
    """Update account general settings - ``PATCH /settings/general_settings/account``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_ACCOUNT,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFieldSettingsItem,
    )


def update_settings_general_settings_item(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettingsItemUpdated]:
    """Update item general settings - ``PATCH /settings/general_settings/item``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_ITEM,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettingsItemUpdated,
    )


def delete_settings_item_group(
    client: Any,
    item_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete item group - ``DELETE /settings/item_groups/{item_group_id}``; answered ``204``."""
    return client.send_delete_request(
        settings_urls.SETTINGS_ITEM_GROUP,
        path_params={"item_group_id": item_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_item_group(
    client: Any,
    item_group_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsItemGroups]:
    """Get single - ``GET /settings/item_groups/{item_group_id}``."""
    return client.send_get_request(
        settings_urls.SETTINGS_ITEM_GROUP,
        path_params={"item_group_id": item_group_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsItemGroups,
    )


def update_settings_item_group(
    client: Any,
    item_group_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsItemGroups]:
    """Update item group - ``PATCH /settings/item_groups/{item_group_id}``; answered ``202``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_ITEM_GROUP,
        path_params={"item_group_id": item_group_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsItemGroups,
    )


def get_settings_time_zone(
    client: Any,
    time_zone_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTimeZoneRead]:
    """Get single - ``GET /settings/time_zones/{time_zone_id}``."""
    return client.send_get_request(
        settings_urls.SETTINGS_TIME_ZONE,
        path_params={"time_zone_id": time_zone_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTimeZoneRead,
    )


def get_settings_variation(
    client: Any,
    variation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsVariations]:
    """Get single - ``GET /settings/variations/{variation_id}``."""
    return client.send_get_request(
        settings_urls.SETTINGS_VARIATION,
        path_params={"variation_id": variation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsVariations,
    )


def update_settings_variation(
    client: Any,
    variation_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsVariations]:
    """Update variation - ``PATCH /settings/variations/{variation_id}``; answered ``202``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_VARIATION,
        path_params={"variation_id": variation_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsVariations,
    )


def create_settings_custom_object_customize(
    client: Any,
    custom_object_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomObjectCustomize]:
    """Customize attributes - ``POST /settings/custom_objects/{custom_object_id}/customize``;
    answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_CUSTOM_OBJECT_CUSTOMIZE,
        path_params={"custom_object_id": custom_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomObjectCustomize,
    )


def create_settings_item_group_billing_preference(
    client: Any,
    item_group_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsItemGroups]:
    """Update billing preferences -
    ``POST /settings/item_groups/{item_group_id}/billing_preferences``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_ITEM_GROUP_BILLING_PREFERENCES,
        path_params={"item_group_id": item_group_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsItemGroups,
    )


def get_settings_custom_objects(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomObjectDefinitionList]:
    """List custom object definitions - ``GET /settings/custom_objects``; enabled definitions
    only."""
    return client.send_get_request(
        settings_urls.SETTINGS_CUSTOM_OBJECTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomObjectDefinitionList,
    )


def get_settings_custom_object(
    client: Any,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomObjectDefinitionRead]:
    """Get one custom object definition - ``GET /settings/custom_objects/{custom_object_id}``, under
    ``custom_object``."""
    return client.send_get_request(
        settings_urls.SETTINGS_CUSTOM_OBJECT,
        path_params={"custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomObjectDefinitionRead,
    )


def create_custom_object(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomObjects]:
    """Create a custom object schema - ``POST /custom_objects``; answered ``201``, under
    ``custom_object``. ``name`` is required and must be unused."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.CUSTOM_OBJECTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomObjects,
    )


def update_custom_object(
    client: Any,
    custom_object_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomObjects]:
    """Update a custom object schema - ``PATCH /custom_objects/{custom_object_id}``, under
    ``custom_object``. ``use_in``, ``relation`` and ``custom_component`` are refused."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.CUSTOM_OBJECT,
        path_params={"custom_object_id": custom_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomObjects,
    )


def delete_custom_object(
    client: Any,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a custom object schema - ``DELETE /custom_objects/{custom_object_id}``; answered
    ``204``."""
    return client.send_delete_request(
        settings_urls.CUSTOM_OBJECT,
        path_params={"custom_object_id": custom_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_currency(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a currency - ``POST /settings/currencies``; answered ``201``, under ``currency``.
    ``code`` and ``country`` are required, and v4 has no route that deletes a currency."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_CURRENCIES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_currency(
    client: Any,
    currency_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update a currency - ``PATCH /settings/currencies/{currency_id}``, under ``currency``. Only
    ``rounding``, ``cash_rounding_interval``, ``conversion_rate`` and ``status`` are accepted."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_CURRENCY,
        path_params={"currency_id": currency_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_custom_logic_script(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomLogicScriptSaved]:
    """Create a custom logic script - ``POST /settings/custom_logic_scripts``; answered ``201``.
    ``name``, ``type`` and ``code`` are required, and ``code`` is validated but not stored."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_CUSTOM_LOGIC_SCRIPTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomLogicScriptSaved,
    )


def update_settings_custom_logic_script(
    client: Any,
    custom_logic_script_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomLogicScriptSaved]:
    """Update a custom logic script -
    ``PATCH /settings/custom_logic_scripts/{custom_logic_script_id}``; ``code`` is refused."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_CUSTOM_LOGIC_SCRIPT,
        path_params={"custom_logic_script_id": custom_logic_script_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomLogicScriptSaved,
    )


def delete_settings_custom_logic_script(
    client: Any,
    custom_logic_script_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Soft-delete a custom logic script -
    ``DELETE /settings/custom_logic_scripts/{custom_logic_script_id}``; ``204``."""
    return client.send_delete_request(
        settings_urls.SETTINGS_CUSTOM_LOGIC_SCRIPT,
        path_params={"custom_logic_script_id": custom_logic_script_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_discount_profile(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDiscountProfileRead]:
    """Create a discount profile - ``POST /settings/discount_profiles``; ``201``. Times go as
    ``YYYY-MM-DD HH:mm`` and the accounting code must be a discount one, or it is a ``500``."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_DISCOUNT_PROFILES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDiscountProfileRead,
    )


def get_settings_discount_profile(
    client: Any,
    discount_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDiscountProfileRead]:
    """Get one discount profile - ``GET /settings/discount_profiles/{discount_profile_id}``, under
    ``discount_profile``."""
    return client.send_get_request(
        settings_urls.SETTINGS_DISCOUNT_PROFILE,
        path_params={"discount_profile_id": discount_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDiscountProfileRead,
    )


def update_settings_discount_profile(
    client: Any,
    discount_profile_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDiscountProfileRead]:
    """Update a discount profile - ``PATCH /settings/discount_profiles/{discount_profile_id}``,
    under ``discount_profile``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_DISCOUNT_PROFILE,
        path_params={"discount_profile_id": discount_profile_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDiscountProfileRead,
    )


def delete_settings_discount_profile(
    client: Any,
    discount_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a discount profile - ``DELETE /settings/discount_profiles/{discount_profile_id}``;
    answered ``204``."""
    return client.send_delete_request(
        settings_urls.SETTINGS_DISCOUNT_PROFILE,
        path_params={"discount_profile_id": discount_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_field_settings(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFieldSettingList]:
    """List field settings - ``GET /settings/field_settings``; paged by cursor, and
    ``include_total=true`` is refused."""
    return client.send_get_request(
        settings_urls.SETTINGS_FIELD_SETTINGS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFieldSettingList,
    )


def get_settings_field_setting(
    client: Any,
    field_setting_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFieldSettingRead]:
    """Get one field setting - ``GET /settings/field_settings/{field_setting_id}``, under
    ``field_setting``."""
    return client.send_get_request(
        settings_urls.SETTINGS_FIELD_SETTING,
        path_params={"field_setting_id": field_setting_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFieldSettingRead,
    )


def get_settings_general_settings(
    client: Any,
    group: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Read one group of general settings - ``GET /settings/general_settings/{group}``, under
    ``general_settings``; ``group`` is one of the twelve the server names, any case."""
    return client.send_get_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_GROUP,
        path_params={"group": group},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def get_settings_general_setting(
    client: Any,
    group: str,
    general_setting_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One general setting row - ``GET /settings/general_settings/{group}/{general_setting_id}``; no
    v4 answer carries a ``gs_`` id."""
    return client.send_get_request(
        settings_urls.SETTINGS_GENERAL_SETTING,
        path_params={"group": group, "general_setting_id": general_setting_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_general_settings_dashboard(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the dashboard group - ``PATCH /settings/general_settings/dashboard``. Flags are stored
    as ``"1"``/``"0"`` and read back raw, so a ``"true"`` cannot be restored."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_DASHBOARD,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_date_and_time(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the date and time group - ``PATCH /settings/general_settings/date_and_time``; the save
    also pushes the organisation to the catalogue processor."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_DATE_AND_TIME,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_display(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the display group - ``PATCH /settings/general_settings/display``. Column lists sent as
    the strings the read serves are ignored: the save reads arrays."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_DISPLAY,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_general(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the general group - ``PATCH /settings/general_settings/general``. It also resets
    ``accountingPeriod``, ``fiscalYear`` and six more settings no route can write back."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_GENERAL,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_labour(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the labour general settings - ``PATCH /settings/general_settings/labour``; answers the
    group as ``GET`` reads it, under ``general_settings``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_LABOUR,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_order(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the order group - ``PATCH /settings/general_settings/order``, which reads ``order``
    and ``product`` from ``general_settings``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_ORDER,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_portal(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the portal group - ``PATCH /settings/general_settings/portal``. With
    ``enableCustomerPortal`` off, any write also turns every portal login off."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_PORTAL,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_purchase(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the purchase general settings - ``PATCH /settings/general_settings/purchase``; answers
    the group as ``GET`` reads it, under ``general_settings``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_PURCHASE,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_security(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the security group - ``PATCH /settings/general_settings/security``. Send flags as
    ``"1"``/``"0"``: the ``"true"`` the read serves is stored as false."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_SECURITY,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def update_settings_general_settings_transaction(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsGeneralSettings]:
    """Update the transaction general settings - ``PATCH /settings/general_settings/transaction``;
    answers the group as ``GET`` reads it, under ``general_settings``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_GENERAL_SETTINGS_TRANSACTION,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsGeneralSettings,
    )


def create_settings_payment_processor(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPaymentProcessorSaved]:
    """Create an offline payment processor - ``POST /settings/payment_processors``; ``201``. Refused
    unless ``credentials.maximumRetryOnFailure`` is ``"0"`` or ``"1"``."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_PAYMENT_PROCESSORS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPaymentProcessorSaved,
    )


def get_settings_payment_processor(
    client: Any,
    payment_processor_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPaymentProcessorRead]:
    """Get one payment processor - ``GET /settings/payment_processors/{payment_processor_id}``,
    under ``payment_processor``."""
    return client.send_get_request(
        settings_urls.SETTINGS_PAYMENT_PROCESSOR,
        path_params={"payment_processor_id": payment_processor_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPaymentProcessorRead,
    )


def update_settings_payment_processor(
    client: Any,
    payment_processor_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPaymentProcessorSaved]:
    """Update a payment processor - ``PATCH /settings/payment_processors/{payment_processor_id}``;
    refused, like the create, without ``credentials.maximumRetryOnFailure``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_PAYMENT_PROCESSOR,
        path_params={"payment_processor_id": payment_processor_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPaymentProcessorSaved,
    )


def delete_settings_payment_processor(
    client: Any,
    payment_processor_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a payment processor - ``DELETE /settings/payment_processors/{payment_processor_id}``;
    answered ``204``. The default processor is refused."""
    return client.send_delete_request(
        settings_urls.SETTINGS_PAYMENT_PROCESSOR,
        path_params={"payment_processor_id": payment_processor_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_payment_term(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPaymentTermCreated]:
    """Create a payment term - ``POST /settings/payment_terms``; answered ``201`` with a flat
    ``period`` and ``duration`` where the read nests them. A sent ``status`` is not applied."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_PAYMENT_TERMS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPaymentTermCreated,
    )


def get_settings_payment_term(
    client: Any,
    payment_term_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPaymentTermRead]:
    """Get one payment term - ``GET /settings/payment_terms/{payment_term_id}``, under
    ``payment_term``."""
    return client.send_get_request(
        settings_urls.SETTINGS_PAYMENT_TERM,
        path_params={"payment_term_id": payment_term_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPaymentTermRead,
    )


def update_settings_payment_term(
    client: Any,
    payment_term_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPaymentTermUpdated]:
    """Update a payment term - ``PATCH /settings/payment_terms/{payment_term_id}``, under
    ``payment_term``; the answer adds ``display_order`` to the read's fields."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_PAYMENT_TERM,
        path_params={"payment_term_id": payment_term_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPaymentTermUpdated,
    )


def delete_settings_payment_term(
    client: Any,
    payment_term_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a payment term - ``DELETE /settings/payment_terms/{payment_term_id}``; answered
    ``204``."""
    return client.send_delete_request(
        settings_urls.SETTINGS_PAYMENT_TERM,
        path_params={"payment_term_id": payment_term_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_pricing_level(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPricingLevelCreated]:
    """Create a pricing level - ``POST /settings/pricing_levels``; answered ``201``, under
    ``pricing_level``. ``name`` is required, and a sent ``status`` is not applied."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_PRICING_LEVELS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPricingLevelCreated,
    )


def get_settings_pricing_level(
    client: Any,
    pricing_level_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPricingLevelRead]:
    """Get one pricing level - ``GET /settings/pricing_levels/{pricing_level_id}``, under
    ``pricing_level``."""
    return client.send_get_request(
        settings_urls.SETTINGS_PRICING_LEVEL,
        path_params={"pricing_level_id": pricing_level_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPricingLevelRead,
    )


def update_settings_pricing_level(
    client: Any,
    pricing_level_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsPricingLevelRead]:
    """Update a pricing level - ``PATCH /settings/pricing_levels/{pricing_level_id}``, under
    ``pricing_level``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_PRICING_LEVEL,
        path_params={"pricing_level_id": pricing_level_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsPricingLevelRead,
    )


def delete_settings_pricing_level(
    client: Any,
    pricing_level_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a pricing level - ``DELETE /settings/pricing_levels/{pricing_level_id}``; answered
    ``204``. The default level is refused."""
    return client.send_delete_request(
        settings_urls.SETTINGS_PRICING_LEVEL,
        path_params={"pricing_level_id": pricing_level_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_shipping_profile(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingProfileRead]:
    """Create a shipping profile - ``POST /settings/shipping_profiles``; ``201``. ``name`` and
    ``shipping_type`` are required, and ``FIXED`` needs ``fixed_amount``."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_SHIPPING_PROFILES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingProfileRead,
    )


def get_settings_shipping_profile(
    client: Any,
    shipping_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingProfileRead]:
    """Get one shipping profile - ``GET /settings/shipping_profiles/{shipping_profile_id}``, under
    ``shipping_profile``."""
    return client.send_get_request(
        settings_urls.SETTINGS_SHIPPING_PROFILE,
        path_params={"shipping_profile_id": shipping_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingProfileRead,
    )


def update_settings_shipping_profile(
    client: Any,
    shipping_profile_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update a shipping profile - ``PATCH /settings/shipping_profiles/{shipping_profile_id}``.
    Answers ``500``, so it names no view."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_SHIPPING_PROFILE,
        path_params={"shipping_profile_id": shipping_profile_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_settings_shipping_profile(
    client: Any,
    shipping_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a shipping profile - ``DELETE /settings/shipping_profiles/{shipping_profile_id}``;
    answered ``204``."""
    return client.send_delete_request(
        settings_urls.SETTINGS_SHIPPING_PROFILE,
        path_params={"shipping_profile_id": shipping_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_warehouse(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsWarehouseRead]:
    """Create a warehouse - ``POST /settings/warehouses``; answered ``201``. ``name`` and
    ``country`` are required, and the answer's ``country`` reads null although it was stored."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_WAREHOUSES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsWarehouseRead,
    )


def get_settings_warehouse(
    client: Any,
    warehouse_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsWarehouseRead]:
    """Get one warehouse - ``GET /settings/warehouses/{warehouse_id}``, under ``warehouse``."""
    return client.send_get_request(
        settings_urls.SETTINGS_WAREHOUSE,
        path_params={"warehouse_id": warehouse_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsWarehouseRead,
    )


def update_settings_warehouse(
    client: Any,
    warehouse_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsWarehouseRead]:
    """Update a warehouse - ``PATCH /settings/warehouses/{warehouse_id}``, under ``warehouse``; the
    answer's ``country`` reads null although the record has one."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_WAREHOUSE,
        path_params={"warehouse_id": warehouse_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsWarehouseRead,
    )


def delete_settings_warehouse(
    client: Any,
    warehouse_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a warehouse - ``DELETE /settings/warehouses/{warehouse_id}``; answered ``204``."""
    return client.send_delete_request(
        settings_urls.SETTINGS_WAREHOUSE,
        path_params={"warehouse_id": warehouse_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_tax(
    client: Any,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a country tax - ``POST /settings/taxes``; answered ``201``, under ``tax``. ``code``
    and ``country`` are required, and v4 has no route that deletes a tax."""
    _require_payload(payload)
    return client.send_post_request(
        settings_urls.SETTINGS_TAXES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_tax(
    client: Any,
    tax_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTaxRead]:
    """Get one tax - ``GET /settings/taxes/{tax_id}``, under ``tax``."""
    return client.send_get_request(
        settings_urls.SETTINGS_TAX,
        path_params={"tax_id": tax_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTaxRead,
    )


def update_settings_tax(
    client: Any,
    tax_id: str,
    payload: SettingsPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update, enable or disable a tax - ``PATCH /settings/taxes/{tax_id}``, under ``tax``."""
    _require_payload(payload)
    return client.send_patch_request(
        settings_urls.SETTINGS_TAX,
        path_params={"tax_id": tax_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_settings_variation(
    client: Any,
    variation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a variation - ``DELETE /settings/variations/{variation_id}``; answered ``204``."""
    return client.send_delete_request(
        settings_urls.SETTINGS_VARIATION,
        path_params={"variation_id": variation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
