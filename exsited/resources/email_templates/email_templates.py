"""Email template endpoints, under ``/api/{api_version}/settings/email_templates``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.email_templates import email_templates_urls
from exsited.resources.email_templates.email_templates_dto import (
    SettingsEmailTemplate,
    SettingsEmailTemplateList,
)

__all__ = [
    "get_settings_email_templates",
    "create_settings_email_template",
    "get_settings_email_template",
    "delete_settings_email_template",
    "update_settings_email_template",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

EmailTemplatePayload = Mapping[str, Any] | str | Dto


def get_settings_email_templates(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsEmailTemplateList]:
    """List the email templates shared across the instance - ``GET /settings/email_templates``."""
    return client.send_get_request(
        email_templates_urls.SETTINGS_EMAIL_TEMPLATES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsEmailTemplateList,
    )


def create_settings_email_template(
    client: Any,
    payload: EmailTemplatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsEmailTemplate]:
    """Create an email template; ``name`` is required, and ``cc`` and ``bcc`` are lists of
    addresses - ``POST /settings/email_templates``."""
    _require_payload(payload)
    return client.send_post_request(
        email_templates_urls.SETTINGS_EMAIL_TEMPLATES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsEmailTemplate,
    )


def get_settings_email_template(
    client: Any,
    email_template_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsEmailTemplate]:
    """Read one email template by its ``et_`` id -
    ``GET /settings/email_templates/{email_template_id}``."""
    return client.send_get_request(
        email_templates_urls.SETTINGS_EMAIL_TEMPLATE,
        path_params={"email_template_id": email_template_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsEmailTemplate,
    )


def delete_settings_email_template(
    client: Any,
    email_template_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an email template - ``DELETE /settings/email_templates/{email_template_id}``."""
    return client.send_delete_request(
        email_templates_urls.SETTINGS_EMAIL_TEMPLATE,
        path_params={"email_template_id": email_template_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_email_template(
    client: Any,
    email_template_id: str,
    payload: EmailTemplatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsEmailTemplate]:
    """Update an email template's fields or its content -
    ``PATCH /settings/email_templates/{email_template_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        email_templates_urls.SETTINGS_EMAIL_TEMPLATE,
        path_params={"email_template_id": email_template_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsEmailTemplate,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
