"""Purchase credit note application endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.purchase_credit_note_applications import (
    purchase_credit_note_applications_urls,
)
from exsited.resources.purchase_credit_note_applications.purchase_credit_note_applications_dto import (
    PurchaseCreditNoteApplicationList,
    PurchaseCreditNoteApplicationRead,
)

__all__ = [
    "get_purchase_credit_note_applications",
    "get_purchase_credit_note_application",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_purchase_credit_note_applications(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteApplicationList]:
    """List purchase credit note applications - ``GET /purchase_credit_note_applications``."""
    return client.send_get_request(
        purchase_credit_note_applications_urls.PURCHASE_CREDIT_NOTE_APPLICATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteApplicationList,
    )


def get_purchase_credit_note_application(
    client: Any,
    purchase_credit_note_application_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[PurchaseCreditNoteApplicationRead]:
    """Get single -
    ``GET /purchase_credit_note_applications/{purchase_credit_note_application_id}``."""
    return client.send_get_request(
        purchase_credit_note_applications_urls.PURCHASE_CREDIT_NOTE_APPLICATION,
        path_params={"purchase_credit_note_application_id": purchase_credit_note_application_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=PurchaseCreditNoteApplicationRead,
    )
