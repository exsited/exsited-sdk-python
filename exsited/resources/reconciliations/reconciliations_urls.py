"""Path templates and body keys for the reconciliation endpoints."""

from __future__ import annotations

#: v4 serves no reconciliation itself, only the two lists hung off one.
RECONCILIATION_SALE_PAYMENTS = (
    "/api/{api_version}/reconciliations/{reconciliation_id}/sale_payments"
)
RECONCILIATION_SALE_REFUNDS = "/api/{api_version}/reconciliations/{reconciliation_id}/sale_refunds"

#: The key a listing's records sit under.
RECONCILIATION_SALE_PAYMENTS_KEY = "data"
RECONCILIATION_SALE_REFUNDS_KEY = "data"
