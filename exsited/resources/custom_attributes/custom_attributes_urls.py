"""Path templates and body keys for the custom attribute endpoints."""

from __future__ import annotations

CUSTOM_ATTRIBUTES = "/api/{api_version}/custom_attributes"
CUSTOM_ATTRIBUTE = "/api/{api_version}/custom_attributes/{custom_attribute_id}"

#: The key a listing's records sit under.
CUSTOM_ATTRIBUTES_KEY = "data"

#: The envelope one record arrives under.
CUSTOM_ATTRIBUTE_KEY = "custom_attribute"
