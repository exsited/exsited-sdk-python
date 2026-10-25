"""Invoice term endpoints, under ``/api/{api_version}/settings/invoice_terms``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.invoice_terms import invoice_terms_urls
from exsited.resources.invoice_terms.invoice_terms_dto import (
    SettingsInvoiceTerm,
    SettingsInvoiceTermList,
    SettingsInvoiceTermWrite,
)

__all__ = [
    "get_settings_invoice_terms",
    "create_settings_invoice_term",
    "get_settings_invoice_term",
    "delete_settings_invoice_term",
    "update_settings_invoice_term",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

InvoiceTermPayload = Mapping[str, Any] | str | Dto


def get_settings_invoice_terms(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsInvoiceTermList]:
    """List invoice terms - ``GET /settings/invoice_terms``."""
    return client.send_get_request(
        invoice_terms_urls.SETTINGS_INVOICE_TERMS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsInvoiceTermList,
    )


def create_settings_invoice_term(
    client: Any,
    payload: InvoiceTermPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsInvoiceTermWrite]:
    """Create an invoice term - ``POST /settings/invoice_terms``; the answer is flat, where a
    read nests ``duration``."""
    _require_payload(payload)
    return client.send_post_request(
        invoice_terms_urls.SETTINGS_INVOICE_TERMS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsInvoiceTermWrite,
    )


def get_settings_invoice_term(
    client: Any,
    invoice_term_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsInvoiceTerm]:
    """Get one invoice term - ``GET /settings/invoice_terms/{invoice_term_id}``."""
    return client.send_get_request(
        invoice_terms_urls.SETTINGS_INVOICE_TERM,
        path_params={"invoice_term_id": invoice_term_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsInvoiceTerm,
    )


def delete_settings_invoice_term(
    client: Any,
    invoice_term_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an invoice term - ``DELETE /settings/invoice_terms/{invoice_term_id}``."""
    return client.send_delete_request(
        invoice_terms_urls.SETTINGS_INVOICE_TERM,
        path_params={"invoice_term_id": invoice_term_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_invoice_term(
    client: Any,
    invoice_term_id: str,
    payload: InvoiceTermPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsInvoiceTermWrite]:
    """Update or enable/disable an invoice term - ``PATCH
    /settings/invoice_terms/{invoice_term_id}``; the answer is flat, where a read nests
    ``duration``."""
    _require_payload(payload)
    return client.send_patch_request(
        invoice_terms_urls.SETTINGS_INVOICE_TERM,
        path_params={"invoice_term_id": invoice_term_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsInvoiceTermWrite,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
