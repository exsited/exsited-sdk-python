"""Path templates and body keys for the unit of measurement endpoints."""

from __future__ import annotations

SETTINGS_UOMS = "/api/{api_version}/settings/uom"
SETTINGS_UOM = "/api/{api_version}/settings/uom/{uom_id}"

#: The key a listing's records sit under.
SETTINGS_UOMS_KEY = "data"

#: The envelope one record arrives under.
UOM_KEY = "uom"
