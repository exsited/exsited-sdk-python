"""Return merchandise authorisation endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.return_merchandise_authorisations import (
    return_merchandise_authorisations_urls,
)
from exsited.resources.return_merchandise_authorisations.return_merchandise_authorisations_dto import (
    InvoiceReturnMerchandiseAuthorisationReceive,
    InvoiceReturnMerchandiseAuthorisationReceiveList,
    ReturnMerchandiseAuthorisationList,
    ReturnMerchandiseAuthorisationRead,
    ReturnMerchandiseAuthorisations,
)

__all__ = [
    "get_return_merchandise_authorisations",
    "create_return_merchandise_authorisation",
    "get_return_merchandise_authorisation",
    "get_invoice_return_merchandise_authorisation_receive",
    "get_invoice_return_merchandise_authorisation_receive_by_uuid",
    "update_return_merchandise_authorisation",
    "delete_return_merchandise_authorisation",
    "approve_return_merchandise_authorisation",
    "reject_return_merchandise_authorisation",
    "receive_return_merchandise_authorisation",
    "get_return_merchandise_authorisation_receive",
    "get_return_merchandise_authorisation_receive_by_uuid",
    "create_return_merchandise_authorisation_note",
    "get_return_merchandise_authorisation_notes",
    "get_return_merchandise_authorisation_note",
    "delete_return_merchandise_authorisation_note",
    "get_return_merchandise_authorisation_note_files",
    "get_return_merchandise_authorisation_note_file",
    "delete_return_merchandise_authorisation_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ReturnMerchandiseAuthorisationPayload = Mapping[str, Any] | str | Dto


def get_return_merchandise_authorisations(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnMerchandiseAuthorisationList]:
    """List of RMAs - ``GET /return_merchandise_authorisations``."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnMerchandiseAuthorisationList,
    )


def create_return_merchandise_authorisation(
    client: Any,
    payload: ReturnMerchandiseAuthorisationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnMerchandiseAuthorisations]:
    """Create RMA - ``POST /return_merchandise_authorisations``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATIONS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnMerchandiseAuthorisations,
    )


def get_return_merchandise_authorisation(
    client: Any,
    rma_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnMerchandiseAuthorisationRead]:
    """RMA details - ``GET /return_merchandise_authorisations/{rma_id}``."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION,
        path_params={"rma_id": rma_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnMerchandiseAuthorisationRead,
    )


def get_invoice_return_merchandise_authorisation_receive(
    client: Any,
    invoice_id: str,
    rma_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceReturnMerchandiseAuthorisationReceiveList]:
    """Receive all -
    ``GET /invoices/{invoice_id}/return_merchandise_authorisations/{rma_code}/receive``, by the
    RMA's code."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.INVOICE_RETURN_MERCHANDISE_AUTHORISATION_RECEIVE,
        path_params={"invoice_id": invoice_id, "rma_code": rma_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceReturnMerchandiseAuthorisationReceiveList,
    )


def get_invoice_return_merchandise_authorisation_receive_by_uuid(
    client: Any,
    invoice_id: str,
    rma_id: str,
    receive_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceReturnMerchandiseAuthorisationReceive]:
    """Receive single -
    ``GET /invoices/{invoice_id}/return_merchandise_authorisations/{rma_code}/receive/{receive_uuid}``,
    by the RMA's code."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.INVOICE_RETURN_MERCHANDISE_AUTHORISATION_RECEIVE_BY_UUID,
        path_params={"invoice_id": invoice_id, "rma_code": rma_id, "receive_uuid": receive_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceReturnMerchandiseAuthorisationReceive,
    )


def update_return_merchandise_authorisation(
    client: Any,
    rma_id: str,
    payload: ReturnMerchandiseAuthorisationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnMerchandiseAuthorisationRead]:
    """Update RMA - ``PATCH /return_merchandise_authorisations/{rma_id}``, the ``rma_`` id and
    ``{"return_merchandise_authorisation": {...}}`` of ``rma_date``, ``note`` and ``returns``."""
    _require_payload(payload)
    return client.send_patch_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION,
        path_params={"rma_id": rma_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnMerchandiseAuthorisationRead,
    )


def delete_return_merchandise_authorisation(
    client: Any,
    rma_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete RMA - ``DELETE /return_merchandise_authorisations/{rma_id}``, the ``rma_`` id; only
    a draft is deleted, anything else is refused ``400`` ``stock_committed``."""
    return client.send_delete_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION,
        path_params={"rma_id": rma_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def approve_return_merchandise_authorisation(
    client: Any,
    rma_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnMerchandiseAuthorisationRead]:
    """Approve RMA - ``POST /return_merchandise_authorisations/{rma_id}/approve``, no body; ``422``
    when the RMA holds no pending approval."""
    return client.send_post_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_APPROVE,
        path_params={"rma_id": rma_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnMerchandiseAuthorisationRead,
    )


def reject_return_merchandise_authorisation(
    client: Any,
    rma_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnMerchandiseAuthorisationRead]:
    """Reject RMA - ``POST /return_merchandise_authorisations/{rma_id}/reject``, no body; ``422``
    when the RMA holds no pending approval."""
    return client.send_post_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_REJECT,
        path_params={"rma_id": rma_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnMerchandiseAuthorisationRead,
    )


def receive_return_merchandise_authorisation(
    client: Any,
    rma_id: str,
    payload: ReturnMerchandiseAuthorisationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnMerchandiseAuthorisationRead]:
    """Receive returned stock - ``POST /return_merchandise_authorisations/{rma_id}/receive``,
    ``{"return_merchandise_authorisation": {"receive_returns": [{"uuid", "rma_receive_quantity"}]}}``."""
    _require_payload(payload)
    return client.send_post_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_RECEIVE,
        path_params={"rma_id": rma_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnMerchandiseAuthorisationRead,
    )


def get_return_merchandise_authorisation_receive(
    client: Any,
    rma_code: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceReturnMerchandiseAuthorisationReceiveList]:
    """List an RMA's receipts - ``GET /return_merchandise_authorisations/{rma_code}/receive``, by
    the RMA's code; an ``rma_`` id answers ``404``."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_RECEIVE_BY_CODE,
        path_params={"rma_code": rma_code},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceReturnMerchandiseAuthorisationReceiveList,
    )


def get_return_merchandise_authorisation_receive_by_uuid(
    client: Any,
    rma_code: str,
    receive_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceReturnMerchandiseAuthorisationReceive]:
    """Get one RMA receipt -
    ``GET /return_merchandise_authorisations/{rma_code}/receive/{receive_uuid}``, the ``rrma_`` id
    or the receipt's code, under ``receive_rma``."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_RECEIVE_BY_UUID,
        path_params={"rma_code": rma_code, "receive_uuid": receive_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InvoiceReturnMerchandiseAuthorisationReceive,
    )


def create_return_merchandise_authorisation_note(
    client: Any,
    rma_id: str,
    payload: ReturnMerchandiseAuthorisationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Add RMA note - ``POST /return_merchandise_authorisations/{rma_id}/notes``, the ``rma_`` id
    and a JSON ``{"note": {"note": "..."}}``, not a form; no attachment."""
    _require_payload(payload)
    return client.send_post_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_NOTES,
        path_params={"rma_id": rma_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_return_merchandise_authorisation_notes(
    client: Any,
    rma_code: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List RMA notes - ``GET /return_merchandise_authorisations/{rma_code}/notes``, by the RMA's
    code; an ``rma_`` id answers ``404``."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_NOTES_BY_CODE,
        path_params={"rma_code": rma_code},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_return_merchandise_authorisation_note(
    client: Any,
    rma_code: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get one RMA note - ``GET /return_merchandise_authorisations/{rma_code}/notes/{note_id}``, by
    the RMA's code."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_NOTE_BY_CODE,
        path_params={"rma_code": rma_code, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_return_merchandise_authorisation_note(
    client: Any,
    rma_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete RMA note - ``DELETE /return_merchandise_authorisations/{rma_id}/notes/{note_id}``,
    the ``rma_`` id; a code answers ``404``."""
    return client.send_delete_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_NOTE,
        path_params={"rma_id": rma_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_return_merchandise_authorisation_note_files(
    client: Any,
    rma_code: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List an RMA note's attachments -
    ``GET /return_merchandise_authorisations/{rma_code}/notes/{note_id}/files``, by the code."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_NOTE_FILES_BY_CODE,
        path_params={"rma_code": rma_code, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_return_merchandise_authorisation_note_file(
    client: Any,
    rma_code: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get one RMA note attachment -
    ``GET /return_merchandise_authorisations/{rma_code}/notes/{note_id}/files/{file_id}``."""
    return client.send_get_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_NOTE_FILE_BY_CODE,
        path_params={"rma_code": rma_code, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_return_merchandise_authorisation_note_file(
    client: Any,
    rma_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an RMA note attachment -
    ``DELETE /return_merchandise_authorisations/{rma_id}/notes/{note_id}/files/{file_id}``."""
    return client.send_delete_request(
        return_merchandise_authorisations_urls.RETURN_MERCHANDISE_AUTHORISATION_NOTE_FILE,
        path_params={"rma_id": rma_id, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
