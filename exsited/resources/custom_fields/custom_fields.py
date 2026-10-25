"""Custom field endpoints, under ``/api/{api_version}/settings/custom_fields``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.custom_fields import custom_fields_urls
from exsited.resources.custom_fields.custom_fields_dto import (
    SettingsCustomField,
    SettingsCustomFieldList,
)

__all__ = [
    "get_settings_custom_fields",
    "get_settings_custom_field",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_settings_custom_fields(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomFieldList]:
    """List the custom fields - ``GET /settings/custom_fields``."""
    return client.send_get_request(
        custom_fields_urls.SETTINGS_CUSTOM_FIELDS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomFieldList,
    )


def get_settings_custom_field(
    client: Any,
    custom_field_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomField]:
    """Read one custom field by its ``cfld_`` id -
    ``GET /settings/custom_fields/{custom_field_id}``."""
    return client.send_get_request(
        custom_fields_urls.SETTINGS_CUSTOM_FIELD,
        path_params={"custom_field_id": custom_field_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomField,
    )
