"""Path templates and body keys for the custom form endpoints."""

from __future__ import annotations

SETTINGS_CUSTOM_FORMS = "/api/{api_version}/settings/custom_forms"
SETTINGS_CUSTOM_FORM = "/api/{api_version}/settings/custom_forms/{custom_form_id}"

#: The key a listing's records sit under.
SETTINGS_CUSTOM_FORMS_KEY = "data"

#: The envelope one record arrives under.
CUSTOM_FORM_KEY = "custom_form"
