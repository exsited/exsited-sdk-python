"""Path templates and body keys for the shipping rule endpoints."""

from __future__ import annotations

SETTINGS_SHIPPING_RULES = "/api/{api_version}/settings/shipping_rules"
SETTINGS_SHIPPING_RULE = "/api/{api_version}/settings/shipping_rules/{shipping_rule_id}"
SETTINGS_SHIPPING_RULE_CONFIGURATION = (
    "/api/{api_version}/settings/shipping_rules/{shipping_rule_id}/configuration"
)

#: The key a listing's records sit under.
SETTINGS_SHIPPING_RULES_KEY = "data"

#: The envelope one record arrives under.
SHIPPING_RULE_KEY = "shipping_rule"

#: The envelope a configuration is sent under.
CONFIGURATION_KEY = "configuration"
