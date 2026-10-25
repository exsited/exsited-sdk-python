"""Approval endpoints, under ``/api/{api_version}/approvals``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.approvals import approvals_urls
from exsited.resources.approvals.approvals_dto import ApprovalsAccountList, ApprovalsSaleorder

__all__ = [
    "get_approvals_account",
    "get_approvals_saleorder",
    "get_approvals_account_by_uuid",
    "approve_approval",
    "reject_approval",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ApprovalPayload = Mapping[str, Any] | str | Dto


def get_approvals_account(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ApprovalsAccountList]:
    """List account approvals - ``GET /approvals/account``."""
    return client.send_get_request(
        approvals_urls.APPROVALS_ACCOUNT,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ApprovalsAccountList,
    )


def get_approvals_saleorder(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ApprovalsSaleorder]:
    """List sale order approvals - ``GET /approvals/saleOrder``."""
    return client.send_get_request(
        approvals_urls.APPROVALS_SALEORDER,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ApprovalsSaleorder,
    )


def get_approvals_account_by_uuid(
    client: Any,
    account_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get single account approval - ``GET /approvals/account/{account_uuid}``."""
    return client.send_get_request(
        approvals_urls.APPROVALS_ACCOUNT_BY_UUID,
        path_params={"account_uuid": account_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def approve_approval(
    client: Any,
    payload: ApprovalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Approve a pending approval - ``POST /approvals/approve``, ``{"approval": {"entity",
    "resource_id", "note"}}`` for any of the 16 entities; it runs the held action."""
    _require_payload(payload)
    return client.send_post_request(
        approvals_urls.APPROVALS_APPROVE,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def reject_approval(
    client: Any,
    payload: ApprovalPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Reject a pending approval - ``POST /approvals/reject``, the same ``{"approval": {"entity",
    "resource_id", "note"}}`` body as ``approve_approval``."""
    _require_payload(payload)
    return client.send_post_request(
        approvals_urls.APPROVALS_REJECT,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
