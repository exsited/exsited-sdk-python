"""Path templates, body keys and query names for the account endpoints. ``{account_id}`` is the
record's ``id`` (``"W13ZGY"``), never its ``uuid``; ``set-password`` is the one hyphenated path."""

from __future__ import annotations

ACCOUNTS = "/api/{api_version}/accounts"
ACCOUNT = "/api/{api_version}/accounts/{account_id}"
ACCOUNT_INFORMATION = "/api/{api_version}/accounts/{account_id}/information"
ACCOUNT_CANCEL = "/api/{api_version}/accounts/{account_id}/cancel"
ACCOUNT_REACTIVATE = "/api/{api_version}/accounts/{account_id}/reactivate"
ACCOUNT_PURGE = "/api/{api_version}/accounts/{account_id}/purge"
ACCOUNT_SET_PASSWORD = "/api/{api_version}/accounts/{account_id}/set-password"

ACCOUNT_CONTACTS = "/api/{api_version}/accounts/{account_id}/contacts"
# A read names the contact by its slot, ``CONTACT_1`` to ``CONTACT_5``; a write names it by its
# ``con_`` id, and the server answers a slot there with a 404.
ACCOUNT_CONTACT_BY_TYPE = "/api/{api_version}/accounts/{account_id}/contacts/{contact_type}"
ACCOUNT_CONTACT = "/api/{api_version}/accounts/{account_id}/contacts/{contact_id}"

ACCOUNT_ADDRESSES = "/api/{api_version}/accounts/{account_id}/addresses"
ACCOUNT_ADDRESS = "/api/{api_version}/accounts/{account_id}/addresses/{address_id}"

ACCOUNT_BILLING_PREFERENCES = "/api/{api_version}/accounts/{account_id}/billing_preferences"

ACCOUNT_PAYMENT_METHODS = "/api/{api_version}/accounts/{account_id}/payment_methods"
ACCOUNT_PAYMENT_METHOD = (
    "/api/{api_version}/accounts/{account_id}/payment_methods/{payment_method_id}"
)

ACCOUNT_NOTES = "/api/{api_version}/accounts/{account_id}/notes"
ACCOUNT_NOTE = "/api/{api_version}/accounts/{account_id}/notes/{note_id}"
ACCOUNT_NOTE_FILES = "/api/{api_version}/accounts/{account_id}/notes/{note_id}/files"
ACCOUNT_NOTE_FILE = "/api/{api_version}/accounts/{account_id}/notes/{note_id}/files/{file_id}"

ACCOUNT_IMAGE = "/api/{api_version}/accounts/{account_id}/image"

ACCOUNT_EMAILS = "/api/{api_version}/accounts/{account_id}/communications/emails"
ACCOUNT_EMAIL = "/api/{api_version}/accounts/{account_id}/communications/emails/{email_id}"

# A create names the custom object the instance belongs to, a "co_" id; an update names the
# instance, a "coi_" id. The server also serves the create under custom_objects_instances.
ACCOUNT_CUSTOM_OBJECT = "/api/{api_version}/accounts/{account_id}/custom_objects/{custom_object_id}"
ACCOUNT_CUSTOM_OBJECT_INSTANCE = (
    "/api/{api_version}/accounts/{account_id}/custom_objects_instances/{custom_object_instance_id}"
)
# A read names both, the schema's "co_" id and then the instance's "coi_" id. The server also
# serves the reads under custom_objects_instances, the same handler.
ACCOUNT_CUSTOM_OBJECT_INSTANCE_OF = (
    "/api/{api_version}/accounts/{account_id}/custom_objects/{custom_object_id}/instances/"
    "{custom_object_instance_id}"
)

# A component's objects under the account and its child accounts: the "cmp_" id, then the
# object's "cco_" id. The path segment is the singular "component".
ACCOUNT_COMPONENT_OBJECTS = "/api/{api_version}/accounts/{account_id}/component/{component_id}"
ACCOUNT_COMPONENT_OBJECT = (
    "/api/{api_version}/accounts/{account_id}/component/{component_id}/{component_object_id}"
)

ACCOUNT_KPIS = "/api/{api_version}/accounts/{account_id}/kpis"
ACCOUNT_FINANCIAL_SUMMARY = "/api/{api_version}/accounts/{account_id}/financial_summary"

# Related listings. Each is the same records the resource's own top-level listing
# holds, narrowed to one account, and each answers the standard list envelope.
ACCOUNT_ORDERS = "/api/{api_version}/accounts/{account_id}/orders"
ACCOUNT_INVOICES = "/api/{api_version}/accounts/{account_id}/invoices"
ACCOUNT_PAYMENTS = "/api/{api_version}/accounts/{account_id}/payments"
ACCOUNT_REFUNDS = "/api/{api_version}/accounts/{account_id}/refunds"
ACCOUNT_CREDIT_NOTES = "/api/{api_version}/accounts/{account_id}/credit_notes"
ACCOUNT_PURCHASE_ORDERS = "/api/{api_version}/accounts/{account_id}/purchase_orders"
ACCOUNT_PURCHASE_INVOICES = "/api/{api_version}/accounts/{account_id}/purchase_invoices"
ACCOUNT_PURCHASE_PAYMENTS = "/api/{api_version}/accounts/{account_id}/purchase_payments"
ACCOUNT_PURCHASE_REFUNDS = "/api/{api_version}/accounts/{account_id}/purchase_refunds"
ACCOUNT_CUSTOM_OBJECTS = "/api/{api_version}/accounts/{account_id}/custom_objects"
ACCOUNT_INVENTORIES = "/api/{api_version}/accounts/{account_id}/inventories"
ACCOUNT_QUOTE_PARTIAL_INVOICES = "/api/{api_version}/accounts/{account_id}/quote_partial_invoices"

#: The key a listing's records sit under.
ACCOUNTS_KEY = "data"
ACCOUNT_EMAILS_KEY = "data"
ACCOUNT_NOTES_KEY = "data"
ACCOUNT_NOTE_FILES_KEY = "data"
ACCOUNT_ORDERS_KEY = "data"
ACCOUNT_COMPONENT_OBJECTS_KEY = "data"
ACCOUNT_PAYMENTS_KEY = "data"
ACCOUNT_PURCHASE_INVOICES_KEY = "data"
ACCOUNT_PURCHASE_ORDERS_KEY = "data"
ACCOUNT_PURCHASE_PAYMENTS_KEY = "data"
ACCOUNT_PURCHASE_REFUNDS_KEY = "data"
ACCOUNT_REFUNDS_KEY = "data"

#: The envelope one record arrives under.
ACCOUNT_KEY = "account"
NOTE_KEY = "note"
ACCOUNT_KPIS_KEY = "account_kpis"
CUSTOM_OBJECT_KEY = "custom_object"
CUSTOM_OBJECT_INSTANCE_KEY = "custom_object_instance"
CUSTOM_COMPONENT_OBJECT_KEY = "custom_component_object"

#: The names that shape the listing; every other name is a ``filter_<field>`` or
#: ``filter_<field>_<operator>``, and an unknown one is ``400`` naming the field.
ACCOUNTS_QUERY_PARAMS = ("limit", "cursor", "sort")

#: The fields ``filter_<field>`` accepts, each with ``_neq`` too.
FILTERABLE_FIELDS: frozenset[str] = frozenset(
    {
        "id",
        "name",
        "display_name",
        "email_address",
        "description",
        "origin",
        "website",
        "linkedin",
        "facebook",
        "twitter",
        "created_by",
        "last_updated_by",
        "status",
        "group",
        "manager",
        "currency",
        "time_zone",
        "tax",
        "uuid",
        "communication_preference",
        "accounting_code",
        "created_on",
        "last_updated_on",
    }
)

#: The subset that also takes ``_contains`` and ``_not_contains``.
TEXT_FILTER_FIELDS: frozenset[str] = frozenset(
    {
        "id",
        "name",
        "display_name",
        "email_address",
        "description",
        "origin",
        "website",
        "linkedin",
        "facebook",
        "twitter",
        "created_by",
        "last_updated_by",
    }
)

#: The subset that also takes ``_gt``, ``_gte``, ``_lt`` and ``_lte``, as ``YYYY-MM-DD``.
DATE_FILTER_FIELDS: frozenset[str] = frozenset({"created_on", "last_updated_on"})

#: The primary contact's fields, filtered as ``filter_contact1_<field>``; a custom attribute
#: is ``filter_attribute_<name>``, and the string, number, boolean and text kinds are not
#: implemented by the API.
CONTACT_FILTER_FIELDS: frozenset[str] = frozenset(
    {
        "contact_salutation",
        "first_name",
        "last_name",
        "middle_name",
        "designation",
        "email_address",
        "address_line1",
        "country",
    }
)
