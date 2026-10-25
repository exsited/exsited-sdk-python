"""Shipping rule endpoints, under ``/api/{api_version}/settings/shipping_rules``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.shipping_rules import shipping_rules_urls
from exsited.resources.shipping_rules.shipping_rules_dto import (
    SettingsShippingRule,
    SettingsShippingRuleList,
)

__all__ = [
    "get_settings_shipping_rules",
    "create_settings_shipping_rule",
    "get_settings_shipping_rule",
    "delete_settings_shipping_rule",
    "update_settings_shipping_rule",
    "create_settings_shipping_rule_configuration",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ShippingRulePayload = Mapping[str, Any] | str | Dto


def get_settings_shipping_rules(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingRuleList]:
    """List shipping rules - ``GET /settings/shipping_rules``."""
    return client.send_get_request(
        shipping_rules_urls.SETTINGS_SHIPPING_RULES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingRuleList,
    )


def create_settings_shipping_rule(
    client: Any,
    payload: ShippingRulePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingRule]:
    """Create a shipping rule - ``POST /settings/shipping_rules``."""
    _require_payload(payload)
    return client.send_post_request(
        shipping_rules_urls.SETTINGS_SHIPPING_RULES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingRule,
    )


def get_settings_shipping_rule(
    client: Any,
    shipping_rule_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingRule]:
    """Get one shipping rule - ``GET /settings/shipping_rules/{shipping_rule_id}``."""
    return client.send_get_request(
        shipping_rules_urls.SETTINGS_SHIPPING_RULE,
        path_params={"shipping_rule_id": shipping_rule_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingRule,
    )


def delete_settings_shipping_rule(
    client: Any,
    shipping_rule_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a shipping rule - ``DELETE /settings/shipping_rules/{shipping_rule_id}``."""
    return client.send_delete_request(
        shipping_rules_urls.SETTINGS_SHIPPING_RULE,
        path_params={"shipping_rule_id": shipping_rule_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_shipping_rule(
    client: Any,
    shipping_rule_id: str,
    payload: ShippingRulePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingRule]:
    """Update a shipping rule - ``PATCH /settings/shipping_rules/{shipping_rule_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        shipping_rules_urls.SETTINGS_SHIPPING_RULE,
        path_params={"shipping_rule_id": shipping_rule_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingRule,
    )


def create_settings_shipping_rule_configuration(
    client: Any,
    shipping_rule_id: str,
    payload: ShippingRulePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsShippingRule]:
    """Set a shipping rule's zones, rate and tiers - ``POST
    /settings/shipping_rules/{shipping_rule_id}/configuration``; each ``zones[].zone`` is the
    zone's dashed uuid, not its prefixed id, and the body sits under ``configuration``."""
    _require_payload(payload)
    return client.send_post_request(
        shipping_rules_urls.SETTINGS_SHIPPING_RULE_CONFIGURATION,
        path_params={"shipping_rule_id": shipping_rule_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsShippingRule,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
