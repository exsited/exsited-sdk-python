"""Report endpoints, under ``/api/{api_version}/reports``.
It has no listing, so it exports no ``RECORD_KEY``: every endpoint answers one aggregate."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.reports import reports_urls
from exsited.resources.reports.reports_dto import (
    ReportsAccountsAccountOverview,
    ReportsInvoicesInvoiceOverview,
    ReportsOrdersOrderOverview,
    ReportsPurchaseInvoicesPurchaseInvoiceOverview,
    ReportsPurchaseOrdersPurchaseOrderOverview,
    ReportsPurchaseTransactionsPurchasePaymentAndRefundOverview,
    ReportsTransactionsPaymentAndRefundOverview,
)

__all__ = [
    "get_reports_accounts_account_overview",
    "get_reports_invoices_invoice_overview",
    "get_reports_orders_order_overview",
    "get_reports_purchase_invoices_purchase_invoice_overview",
    "get_reports_purchase_orders_purchase_order_overview",
    "get_reports_purchase_transactions_purchase_payment_and_refund_overview",
    "get_reports_transactions_payment_and_refund_overview",
]


def get_reports_accounts_account_overview(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReportsAccountsAccountOverview]:
    """Account overview report - ``GET /reports/accounts/account_overview``."""
    return client.send_get_request(
        reports_urls.REPORTS_ACCOUNTS_ACCOUNT_OVERVIEW,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReportsAccountsAccountOverview,
    )


def get_reports_invoices_invoice_overview(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReportsInvoicesInvoiceOverview]:
    """Invoice overview report - ``GET /reports/invoices/invoice_overview``."""
    return client.send_get_request(
        reports_urls.REPORTS_INVOICES_INVOICE_OVERVIEW,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReportsInvoicesInvoiceOverview,
    )


def get_reports_orders_order_overview(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReportsOrdersOrderOverview]:
    """Order overview report - ``GET /reports/orders/order_overview``."""
    return client.send_get_request(
        reports_urls.REPORTS_ORDERS_ORDER_OVERVIEW,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReportsOrdersOrderOverview,
    )


def get_reports_purchase_invoices_purchase_invoice_overview(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReportsPurchaseInvoicesPurchaseInvoiceOverview]:
    """Purchase invoice overview report -
    ``GET /reports/purchase_invoices/purchase_invoice_overview``."""
    return client.send_get_request(
        reports_urls.REPORTS_PURCHASE_INVOICES_PURCHASE_INVOICE_OVERVIEW,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReportsPurchaseInvoicesPurchaseInvoiceOverview,
    )


def get_reports_purchase_orders_purchase_order_overview(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReportsPurchaseOrdersPurchaseOrderOverview]:
    """Purchase order overview report - ``GET /reports/purchase_orders/purchase_order_overview``."""
    return client.send_get_request(
        reports_urls.REPORTS_PURCHASE_ORDERS_PURCHASE_ORDER_OVERVIEW,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReportsPurchaseOrdersPurchaseOrderOverview,
    )


def get_reports_purchase_transactions_purchase_payment_and_refund_overview(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReportsPurchaseTransactionsPurchasePaymentAndRefundOverview]:
    """Purchase payment and refund overview report -
    ``GET /reports/purchase_transactions/purchase_payment_and_refund_overview``."""
    return client.send_get_request(
        reports_urls.REPORTS_PURCHASE_TRANSACTIONS_PURCHASE_PAYMENT_AND_REFUND_OVERVIEW,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReportsPurchaseTransactionsPurchasePaymentAndRefundOverview,
    )


def get_reports_transactions_payment_and_refund_overview(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ReportsTransactionsPaymentAndRefundOverview]:
    """Payment and refund overview report -
    ``GET /reports/transactions/payment_and_refund_overview``."""
    return client.send_get_request(
        reports_urls.REPORTS_TRANSACTIONS_PAYMENT_AND_REFUND_OVERVIEW,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ReportsTransactionsPaymentAndRefundOverview,
    )
