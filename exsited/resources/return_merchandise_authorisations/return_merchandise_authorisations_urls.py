"""Path templates and body keys for the return merchandise authorisation endpoints."""

from __future__ import annotations

RETURN_MERCHANDISE_AUTHORISATIONS = "/api/{api_version}/return_merchandise_authorisations"
RETURN_MERCHANDISE_AUTHORISATION = "/api/{api_version}/return_merchandise_authorisations/{rma_id}"
INVOICE_RETURN_MERCHANDISE_AUTHORISATION_RECEIVE = (
    "/api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations/{rma_code}/receive"
)
INVOICE_RETURN_MERCHANDISE_AUTHORISATION_RECEIVE_BY_UUID = "/api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations/{rma_code}/receive/{receive_uuid}"

#: The writes under one RMA take its ``rma_`` id and refuse a code; the reads under it take
#: its code and answer ``404`` for an ``rma_`` id. So one path can need two identifiers, and
#: the ``_BY_CODE`` templates are the read side of it.
RETURN_MERCHANDISE_AUTHORISATION_APPROVE = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_id}/approve"
)
RETURN_MERCHANDISE_AUTHORISATION_REJECT = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_id}/reject"
)
RETURN_MERCHANDISE_AUTHORISATION_RECEIVE = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_id}/receive"
)
RETURN_MERCHANDISE_AUTHORISATION_NOTES = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_id}/notes"
)
RETURN_MERCHANDISE_AUTHORISATION_NOTE = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_id}/notes/{note_id}"
)
RETURN_MERCHANDISE_AUTHORISATION_NOTE_FILE = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_id}/notes/{note_id}/files/{file_id}"
)
RETURN_MERCHANDISE_AUTHORISATION_RECEIVE_BY_CODE = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_code}/receive"
)
RETURN_MERCHANDISE_AUTHORISATION_RECEIVE_BY_UUID = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_code}/receive/{receive_uuid}"
)
RETURN_MERCHANDISE_AUTHORISATION_NOTES_BY_CODE = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_code}/notes"
)
RETURN_MERCHANDISE_AUTHORISATION_NOTE_BY_CODE = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_code}/notes/{note_id}"
)
RETURN_MERCHANDISE_AUTHORISATION_NOTE_FILES_BY_CODE = (
    "/api/{api_version}/return_merchandise_authorisations/{rma_code}/notes/{note_id}/files"
)
RETURN_MERCHANDISE_AUTHORISATION_NOTE_FILE_BY_CODE = "/api/{api_version}/return_merchandise_authorisations/{rma_code}/notes/{note_id}/files/{file_id}"

#: The key a listing's records sit under.
INVOICE_RETURN_MERCHANDISE_AUTHORISATION_RECEIVE_KEY = "receive_return_merchandise_authorisations"
RETURN_MERCHANDISE_AUTHORISATIONS_KEY = "data"
RETURN_MERCHANDISE_AUTHORISATION_RECEIVE_BY_CODE_KEY = "data"
RETURN_MERCHANDISE_AUTHORISATION_NOTES_BY_CODE_KEY = "data"
RETURN_MERCHANDISE_AUTHORISATION_NOTE_FILES_BY_CODE_KEY = "data"

#: The envelope one record arrives under.
INVOICE_KEY = "invoice"
RECEIVE_RETURN_MERCHANDISE_AUTHORISATION_KEY = "receive_return_merchandise_authorisation"
RETURN_MERCHANDISE_AUTHORISATION_KEY = "return_merchandise_authorisation"
RECEIVE_RMA_KEY = "receive_rma"
NOTE_KEY = "note"
FILE_KEY = "file"
