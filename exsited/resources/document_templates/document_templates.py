"""Document template endpoints, under ``/api/{api_version}/settings/document_templates``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.document_templates import document_templates_urls
from exsited.resources.document_templates.document_templates_dto import (
    SettingsDocumentTemplate,
    SettingsDocumentTemplateList,
)

__all__ = [
    "get_settings_document_templates",
    "create_settings_document_template",
    "get_settings_document_template",
    "delete_settings_document_template",
    "update_settings_document_template",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

DocumentTemplatePayload = Mapping[str, Any] | str | Dto


def get_settings_document_templates(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDocumentTemplateList]:
    """List the document templates - ``GET /settings/document_templates``."""
    return client.send_get_request(
        document_templates_urls.SETTINGS_DOCUMENT_TEMPLATES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDocumentTemplateList,
    )


def create_settings_document_template(
    client: Any,
    payload: DocumentTemplatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDocumentTemplate]:
    """Create a document template; ``name`` and ``document_template_type``, such as
    ``PDF_DOCUMENT``, are required - ``POST /settings/document_templates``."""
    _require_payload(payload)
    return client.send_post_request(
        document_templates_urls.SETTINGS_DOCUMENT_TEMPLATES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDocumentTemplate,
    )


def get_settings_document_template(
    client: Any,
    document_template_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDocumentTemplate]:
    """Read one document template by its ``dt_`` id -
    ``GET /settings/document_templates/{document_template_id}``."""
    return client.send_get_request(
        document_templates_urls.SETTINGS_DOCUMENT_TEMPLATE,
        path_params={"document_template_id": document_template_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDocumentTemplate,
    )


def delete_settings_document_template(
    client: Any,
    document_template_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a document template -
    ``DELETE /settings/document_templates/{document_template_id}``."""
    return client.send_delete_request(
        document_templates_urls.SETTINGS_DOCUMENT_TEMPLATE,
        path_params={"document_template_id": document_template_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_document_template(
    client: Any,
    document_template_id: str,
    payload: DocumentTemplatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDocumentTemplate]:
    """Update a document template's fields or its content -
    ``PATCH /settings/document_templates/{document_template_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        document_templates_urls.SETTINGS_DOCUMENT_TEMPLATE,
        path_params={"document_template_id": document_template_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDocumentTemplate,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
