"""Path templates and body keys for the external database endpoints."""

from __future__ import annotations

EXTERNAL_DATABASES = "/api/{api_version}/external_databases"
EXTERNAL_DATABASE = "/api/{api_version}/external_databases/{db_name}"
EXTERNAL_DATABASE_INSERT_RECORDS = "/api/{api_version}/external_databases/{db_name}/insert_records"
EXTERNAL_DATABASE_SEARCH = "/api/{api_version}/external_databases/{db_name}/search"
EXTERNAL_DATABASE_UPDATE_RECORDS = "/api/{api_version}/external_databases/{db_name}/update_records"
EXTERNAL_DATABASE_TABLE = "/api/{api_version}/external_databases/{db_name}/tables/{table_name}"

#: The key a listing's records sit under.
EXTERNAL_DATABASES_KEY = "data"
EXTERNAL_DATABASE_KEY = "data"
