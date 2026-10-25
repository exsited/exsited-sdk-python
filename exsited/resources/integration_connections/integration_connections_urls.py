"""Path templates and body keys for the integration connection endpoints."""

from __future__ import annotations

INTEGRATION_CONNECTIONS = "/api/{api_version}/integration_connections"
INTEGRATION_CONNECTION = "/api/{api_version}/integration_connections/{integration_connection_id}"

#: The key a listing's records sit under.
INTEGRATION_CONNECTIONS_KEY = "data"
