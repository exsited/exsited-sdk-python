"""Credit note application endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.credit_note_applications import credit_note_applications_urls
from exsited.resources.credit_note_applications.credit_note_applications_dto import (
    CreditNoteApplicationList,
    CreditNoteApplicationRead,
    InvoiceCreditNoteApplications,
)

__all__ = [
    "get_credit_note_applications",
    "get_credit_note_application",
    "get_invoice_credit_note_applications",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_credit_note_applications(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteApplicationList]:
    """List credit note applications - ``GET /credit_note_applications``."""
    return client.send_get_request(
        credit_note_applications_urls.CREDIT_NOTE_APPLICATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteApplicationList,
    )


def get_credit_note_application(
    client: Any,
    credit_note_application_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteApplicationRead]:
    """Get single - ``GET /credit_note_applications/{credit_note_application_id}``."""
    return client.send_get_request(
        credit_note_applications_urls.CREDIT_NOTE_APPLICATION,
        path_params={"credit_note_application_id": credit_note_application_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CreditNoteApplicationRead,
    )


def get_invoice_credit_note_applications(
    client: Any,
    invoice_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceCreditNoteApplications]:
    """List invoice credit note applications -
    ``GET /invoices/{invoice_id}/credit_note_applications``."""
    return client.send_get_request(
        credit_note_applications_urls.INVOICE_CREDIT_NOTE_APPLICATIONS,
        path_params={"invoice_id": invoice_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceCreditNoteApplications,
    )
