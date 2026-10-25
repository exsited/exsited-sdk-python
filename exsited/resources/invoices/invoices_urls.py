"""Path templates, body keys and query names for the invoice endpoints. ``{invoice_id}`` is the
record's ``id``, never its ``uuid``; the RMA path is spelled ``authorisations``."""

from __future__ import annotations

INVOICES = "/api/{api_version}/invoices"
INVOICE = "/api/{api_version}/invoices/{invoice_id}"
INVOICE_INFORMATION = "/api/{api_version}/invoices/{invoice_id}/information"
INVOICE_KPIS = "/api/{api_version}/invoices/{invoice_id}/kpis"

#: The lines, and one line. The server ignores ``{line_id}``: it answers the first line
#: whatever the id says.
INVOICE_LINES = "/api/{api_version}/invoices/{invoice_id}/lines"
INVOICE_LINE = "/api/{api_version}/invoices/{invoice_id}/lines/{line_id}"

#: One credit note application through an invoice. The server does not scope it: any
#: application id answers under any invoice that exists.
INVOICE_CREDIT_NOTE_APPLICATION = (
    "/api/{api_version}/invoices/{invoice_id}/credit_note_applications/{credit_note_application_id}"
)

INVOICE_CUSTOM_OBJECTS = "/api/{api_version}/invoices/{invoice_id}/custom_objects"
INVOICE_CUSTOM_OBJECT = "/api/{api_version}/invoices/{invoice_id}/custom_objects/{custom_object_id}"
INVOICE_CUSTOM_OBJECT_INSTANCE = (
    "/api/{api_version}/invoices/{invoice_id}/custom_objects/{custom_object_id}"
    "/instances/{instance_id}"
)

#: The three lifecycle transitions. Each answers ``202``, not ``200``.
INVOICE_AMEND = "/api/{api_version}/invoices/{invoice_id}/amend"
INVOICE_CANCEL = "/api/{api_version}/invoices/{invoice_id}/cancel"
INVOICE_REACTIVATE = "/api/{api_version}/invoices/{invoice_id}/reactivate"

#: Answers bytes, not JSON - see
#: :func:`~exsited.resources.invoices.invoices.get_invoice_pdf`.
INVOICE_PDF = "/api/{api_version}/invoices/{invoice_id}/pdf"

INVOICE_ITEM_FULFILLMENTS = "/api/{api_version}/invoices/{invoice_id}/item_fulfillments"
INVOICE_ITEM_FULFILLMENT = (
    "/api/{api_version}/invoices/{invoice_id}/item_fulfillments/{fulfillment_id}"
)

#: British spelling, with an ``s``.
INVOICE_RMAS = "/api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations"
INVOICE_RMA = "/api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations/{rma_id}"

INVOICE_NOTES = "/api/{api_version}/invoices/{invoice_id}/notes"
INVOICE_NOTE = "/api/{api_version}/invoices/{invoice_id}/notes/{note_id}"
INVOICE_NOTE_FILES = "/api/{api_version}/invoices/{invoice_id}/notes/{note_id}/files"
INVOICE_NOTE_FILE = "/api/{api_version}/invoices/{invoice_id}/notes/{note_id}/files/{file_id}"

#: An order's invoices - and the endpoint that raises one against an order.
ORDER_INVOICES = "/api/{api_version}/orders/{order_id}/invoices"

#: The key a listing's records sit under.
INVOICES_KEY = "data"
INVOICE_ITEM_FULFILLMENTS_KEY = "data"
INVOICE_NOTES_KEY = "data"
INVOICE_RMAS_KEY = "data"
INVOICE_CUSTOM_OBJECTS_KEY = "data"

#: The envelope one record arrives under.
INVOICE_KEY = "invoice"
INVOICE_KPIS_KEY = "invoice_kpis"
CREDIT_NOTE_APPLICATION_KEY = "credit_note_application"
ITEM_FULFILLMENT_KEY = "item_fulfillment"
NOTE_KEY = "note"
RETURN_MERCHANDISE_AUTHORISATION_KEY = "return_merchandise_authorisation"

#: The names that shape the listing, which pages by cursor; every other name is a
#: ``filter_<field>`` or ``filter_<field>_<operator>``, the money and date fields taking the
#: range operators too. A bare ``filter`` expression is ``400``.
INVOICES_QUERY_PARAMS = ("limit", "cursor")
