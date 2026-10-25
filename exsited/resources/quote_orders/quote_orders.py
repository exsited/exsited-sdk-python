"""Quote order endpoints, under ``/api/{api_version}/quote_orders``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.quote_orders import quote_orders_urls
from exsited.resources.quote_orders.quote_orders_dto import QuoteOrderInvoiceList

__all__ = [
    "get_quote_order_invoices",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_quote_order_invoices(
    client: Any,
    quote_order_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[QuoteOrderInvoiceList]:
    """List the invoices raised from a quote - ``GET /quote_orders/{quote_order_id}/invoices``;
    an order that is not a quote answers ``404``."""
    return client.send_get_request(
        quote_orders_urls.QUOTE_ORDER_INVOICES,
        path_params={"quote_order_id": quote_order_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=QuoteOrderInvoiceList,
    )
