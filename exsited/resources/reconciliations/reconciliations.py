"""Reconciliation endpoints, under ``/api/{api_version}/reconciliations``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.reconciliations import reconciliations_urls

__all__ = [
    "get_reconciliation_sale_payments",
    "get_reconciliation_sale_refunds",
]


def get_reconciliation_sale_payments(
    client: Any,
    reconciliation_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List the payments in a reconciliation -
    ``GET /reconciliations/{reconciliation_id}/sale_payments``; the uuid or the numeric id."""
    return client.send_get_request(
        reconciliations_urls.RECONCILIATION_SALE_PAYMENTS,
        path_params={"reconciliation_id": reconciliation_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_reconciliation_sale_refunds(
    client: Any,
    reconciliation_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List the refunds in a reconciliation -
    ``GET /reconciliations/{reconciliation_id}/sale_refunds``; the uuid or the numeric id."""
    return client.send_get_request(
        reconciliations_urls.RECONCILIATION_SALE_REFUNDS,
        path_params={"reconciliation_id": reconciliation_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )
