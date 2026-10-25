"""Path templates and body keys for the shipping package endpoints."""

from __future__ import annotations

SETTINGS_SHIPPING_PACKAGES = "/api/{api_version}/settings/shipping_packages"
SETTINGS_SHIPPING_PACKAGE = "/api/{api_version}/settings/shipping_packages/{shipping_package_id}"

#: The key a listing's records sit under.
SETTINGS_SHIPPING_PACKAGES_KEY = "data"

#: The envelope one record arrives under.
SHIPPING_PACKAGE_KEY = "shipping_package"
