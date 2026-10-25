"""Path templates and body keys for the gift certificate endpoints."""

from __future__ import annotations

GIFT_CERTIFICATES = "/api/{api_version}/gift_certificates"
GIFT_CERTIFICATE = "/api/{api_version}/gift_certificates/{gc_id}"
GIFT_CERTIFICATE_ALLOCATIONS = "/api/{api_version}/gift_certificates/{gc_id}/allocations"
GIFT_CERTIFICATE_TRANSACTIONS = "/api/{api_version}/gift_certificates/{gc_id}/transactions"
GIFT_CERTIFICATE_ALLOCATION = (
    "/api/{api_version}/gift_certificates/{gc_id}/allocations/{allocation_id}"
)
GIFT_CERTIFICATE_TRANSACTION = (
    "/api/{api_version}/gift_certificates/{gc_id}/transactions/{transaction_id}"
)

#: The three balance transitions. Each answers ``200`` with the gift certificate as
#: ``get_gift_certificate`` reads it.
GIFT_CERTIFICATE_AMEND = "/api/{api_version}/gift_certificates/{gc_id}/amend"
GIFT_CERTIFICATE_DEALLOCATIONS = "/api/{api_version}/gift_certificates/{gc_id}/deallocations"

#: The key a listing's records sit under.
GIFT_CERTIFICATES_KEY = "data"
GIFT_CERTIFICATE_ALLOCATIONS_KEY = "data"
GIFT_CERTIFICATE_TRANSACTIONS_KEY = "data"

#: The envelope one record arrives under.
GIFT_CERTIFICATE_KEY = "gift_certificate"
GIFT_CERTIFICATE_ALLOCATION_KEY = "gift_certificate_allocation"
GIFT_CERTIFICATE_TRANSACTION_KEY = "gift_certificate_transaction"

#: The one key ``amend_gift_certificate`` takes under ``gift_certificate``.
GIFT_CERTIFICATE_AMEND_KEYS = ("new_balance",)

#: The one key the allocation writes take under ``gift_certificate``: ``account``, as
#: ``{"code": <account id>}`` or ``{"id": "acc_<uuid>"}``.
GIFT_CERTIFICATE_ALLOCATE_KEYS = ("account",)
