"""Typed views over the report bodies."""

from __future__ import annotations

from exsited.dto import Dto

__all__ = [
    "ReportsAccountsAccountOverview",
    "ReportsInvoicesInvoiceOverview",
    "ReportsOrdersOrderOverview",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverview",
    "ReportsPurchaseOrdersPurchaseOrderOverview",
    "ReportsPurchaseTransactionsPurchasePaymentAndRefundOverview",
    "ReportsTransactionsPaymentAndRefundOverview",
    "ReportsAccountsAccountOverviewDetail",
    "ReportsInvoicesInvoiceOverviewDetail",
    "ReportsOrdersOrderOverviewDetail",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetail",
    "ReportsPurchaseOrdersPurchaseOrderOverviewDetail",
    "ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetail",
    "ReportsTransactionsPaymentAndRefundOverviewDetail",
    "ReportsAccountsAccountOverviewDetailAccountOverview",
    "ReportsInvoicesInvoiceOverviewDetailInvoiceOverview",
    "ReportsOrdersOrderOverviewDetailOrderOverview",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview",
    "ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview",
    "ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePayment",
    "ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefund",
    "ReportsTransactionsPaymentAndRefundOverviewDetailPayment",
    "ReportsTransactionsPaymentAndRefundOverviewDetailRefund",
    "ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewNew",
    "ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewCancelled",
    "ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewReactivated",
    "ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewVoided",
    "ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewAmended",
    "ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewNetGain",
    "ReportsOrdersOrderOverviewDetailOrderOverviewNew",
    "ReportsOrdersOrderOverviewDetailOrderOverviewCancelled",
    "ReportsOrdersOrderOverviewDetailOrderOverviewReactivated",
    "ReportsOrdersOrderOverviewDetailOrderOverviewChanged",
    "ReportsOrdersOrderOverviewDetailOrderOverviewDeleted",
    "ReportsOrdersOrderOverviewDetailOrderOverviewNetGain",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewNew",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewCancelled",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewReactivated",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewVoided",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewAmended",
    "ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewNetGain",
    "ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewNew",
    "ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewCancelled",
    "ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewReactivated",
    "ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewChanged",
    "ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewDeleted",
    "ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewNetPurchases",
    "ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePaymentNew",
    "ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePaymentDeleted",
    "ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefundNew",
    "ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefundDeleted",
    "ReportsTransactionsPaymentAndRefundOverviewDetailPaymentNew",
    "ReportsTransactionsPaymentAndRefundOverviewDetailPaymentDeleted",
    "ReportsTransactionsPaymentAndRefundOverviewDetailRefundNew",
    "ReportsTransactionsPaymentAndRefundOverviewDetailRefundDeleted",
]


class ReportsAccountsAccountOverview(Dto):
    """The reports accounts account overview body, under ``report``."""

    MEASURED_FROM = ("GET /api/{api_version}/reports/accounts/account_overview",)

    ENVELOPE_KEY = "report"

    accounts: ReportsAccountsAccountOverviewDetail | None = None


class ReportsInvoicesInvoiceOverview(Dto):
    """What ``get_reports_invoices_invoice_overview`` answers, under ``report``."""

    MEASURED_FROM = ("GET /api/{api_version}/reports/invoices/invoice_overview",)

    ENVELOPE_KEY = "report"

    invoices: ReportsInvoicesInvoiceOverviewDetail | None = None


class ReportsOrdersOrderOverview(Dto):
    """What ``get_reports_orders_order_overview`` answers, under ``report``."""

    MEASURED_FROM = ("GET /api/{api_version}/reports/orders/order_overview",)

    ENVELOPE_KEY = "report"

    orders: ReportsOrdersOrderOverviewDetail | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverview(Dto):
    """What ``get_reports_purchase_invoices_purchase_invoice_overview`` answers, under
    ``report``."""

    MEASURED_FROM = ("GET /api/{api_version}/reports/purchase_invoices/purchase_invoice_overview",)

    ENVELOPE_KEY = "report"

    purchase_invoices: ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetail | None = None


class ReportsPurchaseOrdersPurchaseOrderOverview(Dto):
    """What ``get_reports_purchase_orders_purchase_order_overview`` answers, under ``report``."""

    MEASURED_FROM = ("GET /api/{api_version}/reports/purchase_orders/purchase_order_overview",)

    ENVELOPE_KEY = "report"

    purchase_orders: ReportsPurchaseOrdersPurchaseOrderOverviewDetail | None = None


class ReportsPurchaseTransactionsPurchasePaymentAndRefundOverview(Dto):
    """What ``get_reports_purchase_transactions_purchase_payment_and_refund_overview`` answers,
    under ``report``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/reports/purchase_transactions/purchase_payment_and_refund_overview",
    )

    ENVELOPE_KEY = "report"

    purchase_payment_and_refund_overview: (
        ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetail | None
    ) = None


class ReportsTransactionsPaymentAndRefundOverview(Dto):
    """What ``get_reports_transactions_payment_and_refund_overview`` answers, under ``report``."""

    MEASURED_FROM = ("GET /api/{api_version}/reports/transactions/payment_and_refund_overview",)

    ENVELOPE_KEY = "report"

    payment_and_refund_overview: ReportsTransactionsPaymentAndRefundOverviewDetail | None = None


class ReportsAccountsAccountOverviewDetail(Dto):
    """A :class:`ReportsAccountsAccountOverview`'s ``accounts``."""

    account_overview: list[ReportsAccountsAccountOverviewDetailAccountOverview] | None = None


class ReportsInvoicesInvoiceOverviewDetail(Dto):
    """A :class:`ReportsInvoicesInvoiceOverview`'s ``invoices``."""

    invoice_overview: list[ReportsInvoicesInvoiceOverviewDetailInvoiceOverview] | None = None


class ReportsOrdersOrderOverviewDetail(Dto):
    """A :class:`ReportsOrdersOrderOverview`'s ``orders``."""

    order_overview: list[ReportsOrdersOrderOverviewDetailOrderOverview] | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetail(Dto):
    """A :class:`ReportsPurchaseInvoicesPurchaseInvoiceOverview`'s ``purchase_invoices``."""

    purchase_invoice_overview: (
        list[ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview] | None
    ) = None


class ReportsPurchaseOrdersPurchaseOrderOverviewDetail(Dto):
    """A :class:`ReportsPurchaseOrdersPurchaseOrderOverview`'s ``purchase_orders``."""

    purchase_order_overview: (
        list[ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview] | None
    ) = None


class ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetail(Dto):
    """A :class:`ReportsPurchaseTransactionsPurchasePaymentAndRefundOverview`'s
    ``purchase_payment_and_refund_overview``."""

    purchase_payments: (
        list[ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePayment]
        | None
    ) = None
    purchase_refunds: (
        list[ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefund] | None
    ) = None


class ReportsTransactionsPaymentAndRefundOverviewDetail(Dto):
    """A :class:`ReportsTransactionsPaymentAndRefundOverview`'s ``payment_and_refund_overview``."""

    payments: list[ReportsTransactionsPaymentAndRefundOverviewDetailPayment] | None = None
    refunds: list[ReportsTransactionsPaymentAndRefundOverviewDetailRefund] | None = None


class ReportsAccountsAccountOverviewDetailAccountOverview(Dto):
    """One entry of a :class:`ReportsAccountsAccountOverviewDetail`'s ``account_overview``."""

    cancelled: str | None = None
    date: str | None = None
    deleted: str | None = None
    net_gain: str | None = None
    new: str | None = None
    reactivated: str | None = None


class ReportsInvoicesInvoiceOverviewDetailInvoiceOverview(Dto):
    """One entry of a :class:`ReportsInvoicesInvoiceOverviewDetail`'s ``invoice_overview``."""

    amended: ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewAmended | None = None
    cancelled: ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewCancelled | None = None
    date: str | None = None
    invoice_total: str | None = None
    net_gain: ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewNetGain | None = None
    new: ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewNew | None = None
    reactivated: ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewReactivated | None = None
    voided: ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewVoided | None = None


class ReportsOrdersOrderOverviewDetailOrderOverview(Dto):
    """One entry of a :class:`ReportsOrdersOrderOverviewDetail`'s ``order_overview``."""

    cancelled: ReportsOrdersOrderOverviewDetailOrderOverviewCancelled | None = None
    changed: ReportsOrdersOrderOverviewDetailOrderOverviewChanged | None = None
    date: str | None = None
    deleted: ReportsOrdersOrderOverviewDetailOrderOverviewDeleted | None = None
    net_gain: ReportsOrdersOrderOverviewDetailOrderOverviewNetGain | None = None
    new: ReportsOrdersOrderOverviewDetailOrderOverviewNew | None = None
    order_total: str | None = None
    reactivated: ReportsOrdersOrderOverviewDetailOrderOverviewReactivated | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview(Dto):
    """One entry of a :class:`ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetail`'s
    ``purchase_invoice_overview``."""

    amended: (
        ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewAmended | None
    ) = None
    cancelled: (
        ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewCancelled | None
    ) = None
    date: str | None = None
    net_gain: (
        ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewNetGain | None
    ) = None
    new: ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewNew | None = (
        None
    )
    purchase_invoice_total: str | None = None
    reactivated: (
        ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewReactivated
        | None
    ) = None
    voided: (
        ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewVoided | None
    ) = None


class ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview(Dto):
    """One entry of a :class:`ReportsPurchaseOrdersPurchaseOrderOverviewDetail`'s
    ``purchase_order_overview``."""

    cancelled: (
        ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewCancelled | None
    ) = None
    changed: ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewChanged | None = (
        None
    )
    date: str | None = None
    deleted: ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewDeleted | None = (
        None
    )
    net_purchases: (
        ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewNetPurchases | None
    ) = None
    new: ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewNew | None = None
    purchase_order_total: str | None = None
    reactivated: (
        ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewReactivated | None
    ) = None


class ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePayment(Dto):
    """One entry of a
    :class:`ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetail`'s
    ``purchase_payments``."""

    date: str | None = None
    deleted: (
        ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePaymentDeleted
        | None
    ) = None
    new: (
        ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePaymentNew | None
    ) = None
    purchase_payment_applied: str | None = None


class ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefund(Dto):
    """One entry of a
    :class:`ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetail`'s
    ``purchase_refunds``."""

    date: str | None = None
    deleted: (
        ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefundDeleted
        | None
    ) = None
    new: (
        ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefundNew | None
    ) = None


class ReportsTransactionsPaymentAndRefundOverviewDetailPayment(Dto):
    """One entry of a :class:`ReportsTransactionsPaymentAndRefundOverviewDetail`'s ``payments``."""

    date: str | None = None
    deleted: ReportsTransactionsPaymentAndRefundOverviewDetailPaymentDeleted | None = None
    new: ReportsTransactionsPaymentAndRefundOverviewDetailPaymentNew | None = None
    payment_applied: str | None = None


class ReportsTransactionsPaymentAndRefundOverviewDetailRefund(Dto):
    """One entry of a :class:`ReportsTransactionsPaymentAndRefundOverviewDetail`'s ``refunds``."""

    date: str | None = None
    deleted: ReportsTransactionsPaymentAndRefundOverviewDetailRefundDeleted | None = None
    new: ReportsTransactionsPaymentAndRefundOverviewDetailRefundNew | None = None


class ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewNew(Dto):
    """A :class:`ReportsInvoicesInvoiceOverviewDetailInvoiceOverview`'s ``new``."""

    amount: str | None = None
    count: str | None = None


class ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewCancelled(Dto):
    """A :class:`ReportsInvoicesInvoiceOverviewDetailInvoiceOverview`'s ``cancelled``."""

    amount: str | None = None
    count: str | None = None


class ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewReactivated(Dto):
    """A :class:`ReportsInvoicesInvoiceOverviewDetailInvoiceOverview`'s ``reactivated``."""

    amount: str | None = None
    count: str | None = None


class ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewVoided(Dto):
    """A :class:`ReportsInvoicesInvoiceOverviewDetailInvoiceOverview`'s ``voided``."""

    amount: str | None = None
    count: str | None = None


class ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewAmended(Dto):
    """A :class:`ReportsInvoicesInvoiceOverviewDetailInvoiceOverview`'s ``amended``."""

    amount: str | None = None
    count: str | None = None


class ReportsInvoicesInvoiceOverviewDetailInvoiceOverviewNetGain(Dto):
    """A :class:`ReportsInvoicesInvoiceOverviewDetailInvoiceOverview`'s ``net_gain``."""

    amount: str | None = None
    count: str | None = None


class ReportsOrdersOrderOverviewDetailOrderOverviewNew(Dto):
    """A :class:`ReportsOrdersOrderOverviewDetailOrderOverview`'s ``new``."""

    amount: str | None = None
    count: str | None = None


class ReportsOrdersOrderOverviewDetailOrderOverviewCancelled(Dto):
    """A :class:`ReportsOrdersOrderOverviewDetailOrderOverview`'s ``cancelled``."""

    amount: str | None = None
    count: str | None = None


class ReportsOrdersOrderOverviewDetailOrderOverviewReactivated(Dto):
    """A :class:`ReportsOrdersOrderOverviewDetailOrderOverview`'s ``reactivated``."""

    amount: str | None = None
    count: str | None = None


class ReportsOrdersOrderOverviewDetailOrderOverviewChanged(Dto):
    """A :class:`ReportsOrdersOrderOverviewDetailOrderOverview`'s ``changed``."""

    amount: str | None = None
    count: str | None = None


class ReportsOrdersOrderOverviewDetailOrderOverviewDeleted(Dto):
    """A :class:`ReportsOrdersOrderOverviewDetailOrderOverview`'s ``deleted``."""

    amount: str | None = None
    count: str | None = None


class ReportsOrdersOrderOverviewDetailOrderOverviewNetGain(Dto):
    """A :class:`ReportsOrdersOrderOverviewDetailOrderOverview`'s ``net_gain``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewNew(Dto):
    """A :class:`ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview`'s
    ``new``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewCancelled(Dto):
    """A :class:`ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview`'s
    ``cancelled``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewReactivated(Dto):
    """A :class:`ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview`'s
    ``reactivated``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewVoided(Dto):
    """A :class:`ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview`'s
    ``voided``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewAmended(Dto):
    """A :class:`ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview`'s
    ``amended``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverviewNetGain(Dto):
    """A :class:`ReportsPurchaseInvoicesPurchaseInvoiceOverviewDetailPurchaseInvoiceOverview`'s
    ``net_gain``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewNew(Dto):
    """A :class:`ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview`'s
    ``new``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewCancelled(Dto):
    """A :class:`ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview`'s
    ``cancelled``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewReactivated(Dto):
    """A :class:`ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview`'s
    ``reactivated``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewChanged(Dto):
    """A :class:`ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview`'s
    ``changed``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewDeleted(Dto):
    """A :class:`ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview`'s
    ``deleted``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverviewNetPurchases(Dto):
    """A :class:`ReportsPurchaseOrdersPurchaseOrderOverviewDetailPurchaseOrderOverview`'s
    ``net_purchases``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePaymentNew(Dto):
    """A
    :class:`ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePayment`'s
    ``new``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePaymentDeleted(Dto):
    """A
    :class:`ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchasePayment`'s
    ``deleted``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefundNew(Dto):
    """A
    :class:`ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefund`'s
    ``new``."""

    amount: str | None = None
    count: str | None = None


class ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefundDeleted(Dto):
    """A
    :class:`ReportsPurchaseTransactionsPurchasePaymentAndRefundOverviewDetailPurchaseRefund`'s
    ``deleted``."""

    amount: str | None = None
    count: str | None = None


class ReportsTransactionsPaymentAndRefundOverviewDetailPaymentNew(Dto):
    """A :class:`ReportsTransactionsPaymentAndRefundOverviewDetailPayment`'s ``new``."""

    amount: str | None = None
    count: str | None = None


class ReportsTransactionsPaymentAndRefundOverviewDetailPaymentDeleted(Dto):
    """A :class:`ReportsTransactionsPaymentAndRefundOverviewDetailPayment`'s ``deleted``."""

    amount: str | None = None
    count: str | None = None


class ReportsTransactionsPaymentAndRefundOverviewDetailRefundNew(Dto):
    """A :class:`ReportsTransactionsPaymentAndRefundOverviewDetailRefund`'s ``new``."""

    amount: str | None = None
    count: str | None = None


class ReportsTransactionsPaymentAndRefundOverviewDetailRefundDeleted(Dto):
    """A :class:`ReportsTransactionsPaymentAndRefundOverviewDetailRefund`'s ``deleted``."""

    amount: str | None = None
    count: str | None = None
