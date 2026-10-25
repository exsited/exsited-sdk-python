"""Gift certificate endpoints, under ``/api/{api_version}/gift_certificates``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.gift_certificates import gift_certificates_urls
from exsited.resources.gift_certificates.gift_certificates_dto import (
    GiftCertificate,
    GiftCertificateAllocationRead,
    GiftCertificateAllocations,
    GiftCertificateList,
    GiftCertificateTransactionList,
    GiftCertificateTransactionRead,
)

__all__ = [
    "get_gift_certificates",
    "create_gift_certificate",
    "delete_gift_certificate",
    "get_gift_certificate",
    "update_gift_certificate",
    "amend_gift_certificate",
    "allocate_gift_certificate",
    "deallocate_gift_certificate",
    "get_gift_certificate_allocations",
    "get_gift_certificate_allocation",
    "get_gift_certificate_transactions",
    "get_gift_certificate_transaction",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

GiftCertificatePayload = Mapping[str, Any] | str | Dto


def get_gift_certificates(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificateList]:
    """List all - ``GET /gift_certificates``."""
    return client.send_get_request(
        gift_certificates_urls.GIFT_CERTIFICATES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificateList,
    )


def create_gift_certificate(
    client: Any,
    payload: GiftCertificatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificate]:
    """Create - ``POST /gift_certificates``."""
    _require_payload(payload)
    return client.send_post_request(
        gift_certificates_urls.GIFT_CERTIFICATES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificate,
    )


def delete_gift_certificate(
    client: Any,
    gc_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete - ``DELETE /gift_certificates/{gc_id}``."""
    return client.send_delete_request(
        gift_certificates_urls.GIFT_CERTIFICATE,
        path_params={"gc_id": gc_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_gift_certificate(
    client: Any,
    gc_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificate]:
    """Single detail - ``GET /gift_certificates/{gc_id}``."""
    return client.send_get_request(
        gift_certificates_urls.GIFT_CERTIFICATE,
        path_params={"gc_id": gc_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificate,
    )


def update_gift_certificate(
    client: Any,
    gc_id: str,
    payload: GiftCertificatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificate]:
    """Update - ``PATCH /gift_certificates/{gc_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        gift_certificates_urls.GIFT_CERTIFICATE,
        path_params={"gc_id": gc_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificate,
    )


def amend_gift_certificate(
    client: Any,
    gc_id: str,
    payload: GiftCertificatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificate]:
    """Set a new balance - ``POST /gift_certificates/{gc_id}/amend``, as
    ``{"gift_certificate": {"new_balance": ...}}``; a balance below the used amount is a ``400``."""
    _require_payload(payload)
    return client.send_post_request(
        gift_certificates_urls.GIFT_CERTIFICATE_AMEND,
        path_params={"gc_id": gc_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificate,
    )


def allocate_gift_certificate(
    client: Any,
    gc_id: str,
    payload: GiftCertificatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificate]:
    """Allocate to an account - ``POST /gift_certificates/{gc_id}/allocations``, as
    ``{"gift_certificate": {"account": {"code": ...}}}``; ``200``, not ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        gift_certificates_urls.GIFT_CERTIFICATE_ALLOCATIONS,
        path_params={"gc_id": gc_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificate,
    )


def deallocate_gift_certificate(
    client: Any,
    gc_id: str,
    payload: GiftCertificatePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificate]:
    """Take an allocation back from an account - ``POST /gift_certificates/{gc_id}/deallocations``,
    with the same body ``allocate_gift_certificate`` takes."""
    _require_payload(payload)
    return client.send_post_request(
        gift_certificates_urls.GIFT_CERTIFICATE_DEALLOCATIONS,
        path_params={"gc_id": gc_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificate,
    )


def get_gift_certificate_allocations(
    client: Any,
    gc_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificateAllocations]:
    """List gift certificate allocations - ``GET /gift_certificates/{gc_id}/allocations``."""
    return client.send_get_request(
        gift_certificates_urls.GIFT_CERTIFICATE_ALLOCATIONS,
        path_params={"gc_id": gc_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificateAllocations,
    )


def get_gift_certificate_allocation(
    client: Any,
    gc_id: str,
    allocation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificateAllocationRead]:
    """Retrieve one allocation - ``GET /gift_certificates/{gc_id}/allocations/{allocation_id}``,
    under ``gift_certificate_allocation``."""
    return client.send_get_request(
        gift_certificates_urls.GIFT_CERTIFICATE_ALLOCATION,
        path_params={"gc_id": gc_id, "allocation_id": allocation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificateAllocationRead,
    )


def get_gift_certificate_transactions(
    client: Any,
    gc_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificateTransactionList]:
    """List gift certificate transactions - ``GET /gift_certificates/{gc_id}/transactions``."""
    return client.send_get_request(
        gift_certificates_urls.GIFT_CERTIFICATE_TRANSACTIONS,
        path_params={"gc_id": gc_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificateTransactionList,
    )


def get_gift_certificate_transaction(
    client: Any,
    gc_id: str,
    transaction_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[GiftCertificateTransactionRead]:
    """Retrieve one transaction - ``GET /gift_certificates/{gc_id}/transactions/{transaction_id}``,
    under ``gift_certificate_transaction``."""
    return client.send_get_request(
        gift_certificates_urls.GIFT_CERTIFICATE_TRANSACTION,
        path_params={"gc_id": gc_id, "transaction_id": transaction_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=GiftCertificateTransactionRead,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
