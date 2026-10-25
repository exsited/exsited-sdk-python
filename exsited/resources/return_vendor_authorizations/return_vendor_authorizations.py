"""Return vendor authorization endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.return_vendor_authorizations import return_vendor_authorizations_urls
from exsited.resources.return_vendor_authorizations.return_vendor_authorizations_dto import (
    ReturnVendorAuthorizationList,
    ReturnVendorAuthorizationView,
)

__all__ = [
    "get_return_vendor_authorizations",
    "create_return_vendor_authorization",
    "get_return_vendor_authorization",
    "update_return_vendor_authorization",
    "delete_return_vendor_authorization",
    "delete_return_vendor_authorization_note",
    "delete_return_vendor_authorization_note_file",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ReturnVendorAuthorizationPayload = Mapping[str, Any] | str | Dto


def get_return_vendor_authorizations(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnVendorAuthorizationList]:
    """List RVAs - ``GET /return_vendor_authorizations``."""
    return client.send_get_request(
        return_vendor_authorizations_urls.RETURN_VENDOR_AUTHORIZATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnVendorAuthorizationList,
    )


def create_return_vendor_authorization(
    client: Any,
    payload: ReturnVendorAuthorizationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnVendorAuthorizationView]:
    """Create RVA - ``POST /return_vendor_authorizations``, ``{"return_vendor_authorization":
    {"purchase_order", "lines": [{"purchase_order_line", "rva_qty"}]}}``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        return_vendor_authorizations_urls.RETURN_VENDOR_AUTHORIZATIONS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnVendorAuthorizationView,
    )


def get_return_vendor_authorization(
    client: Any,
    rva_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnVendorAuthorizationView]:
    """Get RVA - ``GET /return_vendor_authorizations/{rva_id}``, the ``rva_`` id or the code."""
    return client.send_get_request(
        return_vendor_authorizations_urls.RETURN_VENDOR_AUTHORIZATION,
        path_params={"rva_id": rva_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnVendorAuthorizationView,
    )


def update_return_vendor_authorization(
    client: Any,
    rva_id: str,
    payload: ReturnVendorAuthorizationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReturnVendorAuthorizationView]:
    """Edit RVA header - ``PATCH /return_vendor_authorizations/{rva_id}``, the ``rva_`` id or the
    code, ``{"return_vendor_authorization": {...}}`` of ``rva_date``, ``note`` and
    ``custom_attributes``."""
    _require_payload(payload)
    return client.send_patch_request(
        return_vendor_authorizations_urls.RETURN_VENDOR_AUTHORIZATION,
        path_params={"rva_id": rva_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReturnVendorAuthorizationView,
    )


def delete_return_vendor_authorization(
    client: Any,
    rva_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete draft RVA - ``DELETE /return_vendor_authorizations/{rva_id}``, the ``rva_`` id only;
    a code answers ``404``, and anything but a draft ``400`` ``stock_committed``."""
    return client.send_delete_request(
        return_vendor_authorizations_urls.RETURN_VENDOR_AUTHORIZATION,
        path_params={"rva_id": rva_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_return_vendor_authorization_note(
    client: Any,
    rva_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete RVA note - ``DELETE /return_vendor_authorizations/{rva_id}/notes/{note_id}``, the
    ``rva_`` id; no route lists or creates an RVA's notes."""
    return client.send_delete_request(
        return_vendor_authorizations_urls.RETURN_VENDOR_AUTHORIZATION_NOTE,
        path_params={"rva_id": rva_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_return_vendor_authorization_note_file(
    client: Any,
    rva_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete RVA note attachment -
    ``DELETE /return_vendor_authorizations/{rva_id}/notes/{note_id}/files/{file_id}``."""
    return client.send_delete_request(
        return_vendor_authorizations_urls.RETURN_VENDOR_AUTHORIZATION_NOTE_FILE,
        path_params={"rva_id": rva_id, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
