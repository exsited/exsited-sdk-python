"""Path templates and body keys for the report endpoints."""

from __future__ import annotations

REPORTS_ACCOUNTS_ACCOUNT_OVERVIEW = "/api/{api_version}/reports/accounts/account_overview"
REPORTS_INVOICES_INVOICE_OVERVIEW = "/api/{api_version}/reports/invoices/invoice_overview"
REPORTS_ORDERS_ORDER_OVERVIEW = "/api/{api_version}/reports/orders/order_overview"
REPORTS_PURCHASE_INVOICES_PURCHASE_INVOICE_OVERVIEW = (
    "/api/{api_version}/reports/purchase_invoices/purchase_invoice_overview"
)
REPORTS_PURCHASE_ORDERS_PURCHASE_ORDER_OVERVIEW = (
    "/api/{api_version}/reports/purchase_orders/purchase_order_overview"
)
REPORTS_PURCHASE_TRANSACTIONS_PURCHASE_PAYMENT_AND_REFUND_OVERVIEW = (
    "/api/{api_version}/reports/purchase_transactions/purchase_payment_and_refund_overview"
)
REPORTS_TRANSACTIONS_PAYMENT_AND_REFUND_OVERVIEW = (
    "/api/{api_version}/reports/transactions/payment_and_refund_overview"
)

#: The envelope one record arrives under.
REPORT_KEY = "report"
