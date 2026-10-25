"""Path templates and body keys for the document template endpoints."""

from __future__ import annotations

SETTINGS_DOCUMENT_TEMPLATES = "/api/{api_version}/settings/document_templates"
SETTINGS_DOCUMENT_TEMPLATE = "/api/{api_version}/settings/document_templates/{document_template_id}"

#: The key a listing's records sit under.
SETTINGS_DOCUMENT_TEMPLATES_KEY = "data"

#: The envelope one record arrives under.
DOCUMENT_TEMPLATE_KEY = "document_template"
