"""Path templates and body keys for the usage endpoints."""

from __future__ import annotations

USAGES = "/api/{api_version}/usages"
USAGE = "/api/{api_version}/usages/{usage_id}"

#: The key a listing's records sit under.
USAGES_KEY = "data"

#: The envelope one record arrives under.
USAGE_KEY = "usage"
