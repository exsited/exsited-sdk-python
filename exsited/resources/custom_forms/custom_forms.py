"""Custom form endpoints, under ``/api/{api_version}/settings/custom_forms``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.custom_forms import custom_forms_urls
from exsited.resources.custom_forms.custom_forms_dto import (
    SettingsCustomForm,
    SettingsCustomFormList,
)

__all__ = [
    "get_settings_custom_forms",
    "create_settings_custom_form",
    "get_settings_custom_form",
    "delete_settings_custom_form",
    "update_settings_custom_form",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

CustomFormPayload = Mapping[str, Any] | str | Dto


def get_settings_custom_forms(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomFormList]:
    """List the custom forms - ``GET /settings/custom_forms``."""
    return client.send_get_request(
        custom_forms_urls.SETTINGS_CUSTOM_FORMS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomFormList,
    )


def create_settings_custom_form(
    client: Any,
    payload: CustomFormPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomForm]:
    """Create a custom form; ``name`` and ``setting_group``, a setting group name such as
    ``ACCOUNT``, are required - ``POST /settings/custom_forms``."""
    _require_payload(payload)
    return client.send_post_request(
        custom_forms_urls.SETTINGS_CUSTOM_FORMS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomForm,
    )


def get_settings_custom_form(
    client: Any,
    custom_form_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomForm]:
    """Read one custom form by its ``cf_`` id - ``GET /settings/custom_forms/{custom_form_id}``."""
    return client.send_get_request(
        custom_forms_urls.SETTINGS_CUSTOM_FORM,
        path_params={"custom_form_id": custom_form_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomForm,
    )


def delete_settings_custom_form(
    client: Any,
    custom_form_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a custom form that is not system generated -
    ``DELETE /settings/custom_forms/{custom_form_id}``."""
    return client.send_delete_request(
        custom_forms_urls.SETTINGS_CUSTOM_FORM,
        path_params={"custom_form_id": custom_form_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_custom_form(
    client: Any,
    custom_form_id: str,
    payload: CustomFormPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCustomForm]:
    """Update a custom form's name, display name, description or users -
    ``PATCH /settings/custom_forms/{custom_form_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_forms_urls.SETTINGS_CUSTOM_FORM,
        path_params={"custom_form_id": custom_form_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCustomForm,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
