"""Path templates and body keys for the email template endpoints."""

from __future__ import annotations

SETTINGS_EMAIL_TEMPLATES = "/api/{api_version}/settings/email_templates"
SETTINGS_EMAIL_TEMPLATE = "/api/{api_version}/settings/email_templates/{email_template_id}"

#: The key a listing's records sit under.
SETTINGS_EMAIL_TEMPLATES_KEY = "data"

#: The envelope one record arrives under.
EMAIL_TEMPLATE_KEY = "email_template"
