"""Account endpoints, under ``/api/{api_version}/accounts``."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.account_emails.account_emails_dto import (
    AccountCommunicationsEmail,
    AccountCommunicationsEmailList,
)
from exsited.resources.accounts import accounts_urls
from exsited.resources.accounts.accounts_dto import (
    Account,
    AccountAddress,
    AccountComponentObject,
    AccountContact,
    AccountCustomObject,
    AccountFinancialSummary,
    AccountImage,
    AccountKpis,
    AccountList,
    AccountNoteFile,
    NoteFileList,
    NoteList,
    NoteView,
)
from exsited.resources.credit_notes.credit_notes_dto import CreditNoteList
from exsited.resources.custom_components.custom_components_dto import ComponentObjects
from exsited.resources.invoices.invoices_dto import InvoiceList
from exsited.resources.orders.orders_dto import AccountOrders
from exsited.resources.payments.payments_dto import AccountPayments
from exsited.resources.purchase_invoices.purchase_invoices_dto import AccountPurchaseInvoices
from exsited.resources.purchase_orders.purchase_orders_dto import AccountPurchaseOrders
from exsited.resources.purchase_payments.purchase_payments_dto import AccountPurchasePayments
from exsited.resources.purchase_refunds.purchase_refunds_dto import AccountPurchaseRefunds
from exsited.resources.refunds.refunds_dto import AccountRefunds
from exsited.resources.settings.settings_dto import CustomObjectList

__all__ = [
    "get_accounts",
    "get_account",
    "get_account_information",
    "get_account_image",
    "get_account_contacts",
    "get_account_contact",
    "get_account_addresses",
    "get_account_address",
    "get_account_billing_preferences",
    "get_account_payment_methods",
    "get_account_payment_method",
    "get_account_notes",
    "get_account_note",
    "get_account_note_files",
    "get_account_note_file",
    "get_account_emails",
    "get_account_email",
    "get_account_orders",
    "get_account_invoices",
    "get_account_payments",
    "get_account_refunds",
    "get_account_credit_notes",
    "get_account_purchase_orders",
    "get_account_purchase_invoices",
    "get_account_purchase_payments",
    "get_account_purchase_refunds",
    "get_account_custom_objects",
    "get_account_inventories",
    "get_account_quote_partial_invoices",
    "get_account_kpis",
    "get_account_financial_summary",
    "get_account_custom_object",
    "get_account_custom_object_instance",
    "get_account_component_objects",
    "get_account_component_object",
    "create_account",
    "replace_account",
    "cancel_account",
    "reactivate_account",
    "set_account_password",
    "update_account_information",
    "create_account_contacts",
    "create_account_addresses",
    "update_account_address",
    "replace_account_address",
    "update_account_contact",
    "replace_account_contact",
    "replace_account_billing_preferences",
    "create_account_payment_method",
    "update_account_payment_method",
    "replace_account_payment_method",
    "create_account_note",
    "update_account_note",
    "upload_account_image",
    "create_account_custom_object_instance",
    "update_account_custom_object_instance",
    "send_account_email",
    "purge_account",
    "delete_account",
    "delete_account_contact",
    "delete_account_address",
    "delete_account_payment_method",
    "delete_account_note",
    "delete_account_note_file",
    "delete_account_image",
]

#: A body as the API's own mapping, as JSON text, or as an ``accounts_dto`` type.
AccountPayload = Mapping[str, Any] | str | Dto


def get_accounts(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountList]:
    """List accounts - ``GET /accounts``. ``ACCOUNTS_QUERY_PARAMS`` shape the listing; every other
    name is ``filter_<field>`` or ``filter_<field>_<operator>`` over the ``accounts_urls`` filter
    sets, and an unknown one is ``400``."""
    return client.send_get_request(
        accounts_urls.ACCOUNTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountList,
    )


def get_account(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Retrieve one account - ``GET /accounts/{account_id}``. Pass the ``id`` (``"W13ZGY"``), not
    the ``uuid``, which answers ``404``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_information(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Retrieve an account's core information - ``GET /accounts/{account_id}/information``; the same
    ``account`` body as ``get_account``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_INFORMATION,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_image(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountImage]:
    """Retrieve the account's image reference - ``GET /accounts/{account_id}/image``; an
    ``image_uri``, not image bytes, and null when unset."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_IMAGE,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountImage,
    )


def get_account_contacts(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """List an account's contacts - ``GET /accounts/{account_id}/contacts``; the account envelope
    carrying ``contacts``, not a listing."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_CONTACTS,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_contact(
    client: Any,
    account_id: str,
    contact_type: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountContact]:
    """Retrieve one contact - ``GET /accounts/{account_id}/contacts/{contact_type}``, by its slot,
    ``CONTACT_1`` to ``CONTACT_5``; ``billing``, the type it reads back as, and its ``id`` are 404."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_CONTACT_BY_TYPE,
        path_params={"account_id": account_id, "contact_type": contact_type},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountContact,
    )


def get_account_addresses(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """List an account's addresses - ``GET /accounts/{account_id}/addresses``; the account envelope
    carrying ``addresses``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_ADDRESSES,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_address(
    client: Any,
    account_id: str,
    address_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountAddress]:
    """Retrieve one address - ``GET /accounts/{account_id}/addresses/{address_id}``, by its
    ``addr_`` id."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_ADDRESS,
        path_params={"account_id": account_id, "address_id": address_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountAddress,
    )


def get_account_billing_preferences(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Retrieve an account's billing preferences -
    ``GET /accounts/{account_id}/billing_preferences``. The alignment setting reads back as
    ``charges_aligned_to_billing``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_BILLING_PREFERENCES,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_payment_methods(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """List an account's payment methods - ``GET /accounts/{account_id}/payment_methods``; the
    account envelope carrying them."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_PAYMENT_METHODS,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_payment_method(
    client: Any,
    account_id: str,
    payment_method_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Retrieve one payment method -
    ``GET /accounts/{account_id}/payment_methods/{payment_method_id}``. A method the account does
    not hold answers ``200`` with no ``payment_methods`` key, not ``404``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_PAYMENT_METHOD,
        path_params={
            "account_id": account_id,
            "payment_method_id": payment_method_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_notes(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteList]:
    """List an account's notes - ``GET /accounts/{account_id}/notes``; a paged listing, under
    ``data``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_NOTES,
        path_params={"account_id": account_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteList,
    )


def get_account_note(
    client: Any,
    account_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteView]:
    """Retrieve one note - ``GET /accounts/{account_id}/notes/{note_id}``, under ``note``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_NOTE,
        path_params={"account_id": account_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteView,
    )


def get_account_note_files(
    client: Any,
    account_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteFileList]:
    """List a note's attachments - ``GET /accounts/{account_id}/notes/{note_id}/files``; each is
    addressed by its ``uuid``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_NOTE_FILES,
        path_params={"account_id": account_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteFileList,
    )


def get_account_note_file(
    client: Any,
    account_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountNoteFile]:
    """Retrieve one attachment - ``GET /accounts/{account_id}/notes/{note_id}/files/{file_id}``;
    it answers a JSON descriptor of the
    file under ``file``, not the file's bytes."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_NOTE_FILE,
        path_params={
            "account_id": account_id,
            "note_id": note_id,
            "file_id": file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountNoteFile,
    )


def get_account_emails(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountCommunicationsEmailList]:
    """List the emails sent to or from an account -
    ``GET /accounts/{account_id}/communications/emails``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_EMAILS,
        path_params={"account_id": account_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountCommunicationsEmailList,
    )


def get_account_email(
    client: Any,
    account_id: str,
    email_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountCommunicationsEmail]:
    """Retrieve one email - ``GET /accounts/{account_id}/communications/emails/{email_id}``, by the
    ``uuid`` the listing hands out."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_EMAIL,
        path_params={"account_id": account_id, "email_id": email_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountCommunicationsEmail,
    )


def get_account_orders(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountOrders]:
    """List an account's orders - ``GET /accounts/{account_id}/orders``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_ORDERS,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=AccountOrders,
    )


def get_account_invoices(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InvoiceList]:
    """List an account's invoices - ``GET /accounts/{account_id}/invoices``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_INVOICES,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=InvoiceList,
    )


def get_account_payments(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountPayments]:
    """List an account's payments - ``GET /accounts/{account_id}/payments``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_PAYMENTS,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=AccountPayments,
    )


def get_account_refunds(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountRefunds]:
    """List an account's refunds - ``GET /accounts/{account_id}/refunds``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_REFUNDS,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=AccountRefunds,
    )


def get_account_credit_notes(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CreditNoteList]:
    """List an account's credit notes - ``GET /accounts/{account_id}/credit_notes``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_CREDIT_NOTES,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=CreditNoteList,
    )


def get_account_purchase_orders(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountPurchaseOrders]:
    """List an account's purchase orders - ``GET /accounts/{account_id}/purchase_orders``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_PURCHASE_ORDERS,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=AccountPurchaseOrders,
    )


def get_account_purchase_invoices(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountPurchaseInvoices]:
    """List an account's purchase invoices - ``GET /accounts/{account_id}/purchase_invoices``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_PURCHASE_INVOICES,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=AccountPurchaseInvoices,
    )


def get_account_purchase_payments(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountPurchasePayments]:
    """List an account's purchase payments - ``GET /accounts/{account_id}/purchase_payments``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_PURCHASE_PAYMENTS,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=AccountPurchasePayments,
    )


def get_account_purchase_refunds(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountPurchaseRefunds]:
    """List an account's purchase refunds - ``GET /accounts/{account_id}/purchase_refunds``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_PURCHASE_REFUNDS,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=AccountPurchaseRefunds,
    )


def get_account_custom_objects(
    client: Any,
    account_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomObjectList]:
    """List the custom objects on an account - ``GET /accounts/{account_id}/custom_objects``."""
    return _account_listing(
        client,
        accounts_urls.ACCOUNT_CUSTOM_OBJECTS,
        account_id,
        query_params,
        raise_on_error,
        response_format,
        dto_type=CustomObjectList,
    )


def get_account_inventories(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """List an account's inventories - ``GET /accounts/{account_id}/inventories``; unpaged, under
    ``account.inventories``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_INVENTORIES,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_quote_partial_invoices(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """List an account's partial invoices from quotes -
    ``GET /accounts/{account_id}/quote_partial_invoices``; unpaged, under
    ``account.partial_invoices``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_QUOTE_PARTIAL_INVOICES,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def get_account_kpis(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountKpis]:
    """The account's revenue and order counters - ``GET /accounts/{account_id}/kpis``, under
    ``account_kpis``; the money fields are strings, ``"0.00"``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_KPIS,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountKpis,
    )


def get_account_financial_summary(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountFinancialSummary]:
    """The account's invoice totals - ``GET /accounts/{account_id}/financial_summary``, under
    ``account``, beside its ``name``; the money fields are strings."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_FINANCIAL_SUMMARY,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountFinancialSummary,
    )


def get_account_custom_object(
    client: Any,
    account_id: str,
    custom_object_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountCustomObject]:
    """One custom object with this account's instances of it -
    ``GET /accounts/{account_id}/custom_objects/{custom_object_id}``, the ``co_`` id, under
    ``custom_object``; the instances are paged inside it."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_CUSTOM_OBJECT,
        path_params={"account_id": account_id, "custom_object_id": custom_object_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountCustomObject,
    )


def get_account_custom_object_instance(
    client: Any,
    account_id: str,
    custom_object_id: str,
    custom_object_instance_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One custom object instance -
    ``GET /accounts/{account_id}/custom_objects/{custom_object_id}/instances/{custom_object_instance_id}``,
    the ``coi_`` id, under ``custom_object_instance``. Never measured, so no typed view."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_CUSTOM_OBJECT_INSTANCE_OF,
        path_params={
            "account_id": account_id,
            "custom_object_id": custom_object_id,
            "custom_object_instance_id": custom_object_instance_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_account_component_objects(
    client: Any,
    account_id: str,
    component_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjects]:
    """List a component's objects under an account and its child accounts -
    ``GET /accounts/{account_id}/component/{component_id}``, the ``cmp_`` id; cursor paged."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_COMPONENT_OBJECTS,
        path_params={"account_id": account_id, "component_id": component_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjects,
    )


def get_account_component_object(
    client: Any,
    account_id: str,
    component_id: str,
    component_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[AccountComponentObject]:
    """One component object under an account -
    ``GET /accounts/{account_id}/component/{component_id}/{component_object_id}``, the ``cco_``
    id, under ``custom_component_object``."""
    return client.send_get_request(
        accounts_urls.ACCOUNT_COMPONENT_OBJECT,
        path_params={
            "account_id": account_id,
            "component_id": component_id,
            "component_object_id": component_object_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=AccountComponentObject,
    )


def create_account(
    client: Any,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Create an account - ``POST /accounts``; answered ``201``, under ``account``. ``name`` and
    ``type`` are required, and ``POST /accounts/{account_id}`` is a ``400``."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def replace_account(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Replace an account - ``PUT /accounts/{account_id}``, wrapped in ``account``. ``name`` and
    ``type`` are required on every call, and a field the body omits is kept, not cleared."""
    _require_payload(payload)
    return client.send_put_request(
        accounts_urls.ACCOUNT,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def cancel_account(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Cancel an account - ``POST /accounts/{account_id}/cancel``, wrapped in ``account``;
    ``effective_date`` is required, as ``YYYY-MM-DD``."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_CANCEL,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def reactivate_account(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Reactivate a cancelled account - ``POST /accounts/{account_id}/reactivate``, the body
    ``cancel_account`` takes; a null ``effective_date`` means now."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_REACTIVATE,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def set_account_password(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Set the account's portal password - ``POST /accounts/{account_id}/set-password``;
    ``password`` and ``confirm_password`` sit at the top level, with no ``account`` wrapper."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_SET_PASSWORD,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def update_account_information(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Update an account's core information - ``PATCH /accounts/{account_id}/information``, wrapped
    in ``account``. Writes are flatter than reads: ``currency`` and ``time_zone`` go in as codes."""
    _require_payload(payload)
    return client.send_patch_request(
        accounts_urls.ACCOUNT_INFORMATION,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def create_account_contacts(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Add contacts to an account - ``POST /accounts/{account_id}/contacts``; answered ``201``. A
    list under ``contacts``, each with its slot as ``type`` (``CONTACT_1``) in the body."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_CONTACTS,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def create_account_addresses(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Add addresses to an account - ``POST /accounts/{account_id}/addresses``; a list under a
    top-level ``addresses``, answered with the whole account."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_ADDRESSES,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def update_account_address(
    client: Any,
    account_id: str,
    address_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Update one address - ``PATCH /accounts/{account_id}/addresses/{address_id}``, under a
    singular ``address``."""
    _require_payload(payload)
    return client.send_patch_request(
        accounts_urls.ACCOUNT_ADDRESS,
        path_params={"account_id": account_id, "address_id": address_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def replace_account_address(
    client: Any,
    account_id: str,
    address_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Replace one address - ``PUT /accounts/{account_id}/addresses/{address_id}``, under a
    singular ``address``; ``address_line_1`` and ``country`` are required."""
    _require_payload(payload)
    return client.send_put_request(
        accounts_urls.ACCOUNT_ADDRESS,
        path_params={"account_id": account_id, "address_id": address_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def update_account_contact(
    client: Any,
    account_id: str,
    contact_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Update one contact - ``PATCH /accounts/{account_id}/contacts/{contact_id}``, the ``con_`` id,
    wrapped in ``contact``; the name goes in flat as ``first_name``, and reads back nested."""
    _require_payload(payload)
    return client.send_patch_request(
        accounts_urls.ACCOUNT_CONTACT,
        path_params={"account_id": account_id, "contact_id": contact_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def replace_account_contact(
    client: Any,
    account_id: str,
    contact_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Replace one contact - ``PUT /accounts/{account_id}/contacts/{contact_id}``, the ``con_`` id;
    a field the body omits is cleared."""
    _require_payload(payload)
    return client.send_put_request(
        accounts_urls.ACCOUNT_CONTACT,
        path_params={"account_id": account_id, "contact_id": contact_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def replace_account_billing_preferences(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Replace an account's billing preferences -
    ``PUT /accounts/{account_id}/billing_preferences``. ``billing_start_date`` is an enum, and the
    alignment setting is written ``charging_and_billing_alignment``."""
    _require_payload(payload)
    return client.send_put_request(
        accounts_urls.ACCOUNT_BILLING_PREFERENCES,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def create_account_payment_method(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Add one payment method - ``POST /accounts/{account_id}/payment_methods``; answered ``201``.
    One object under ``payment_method``, not a list; the first method becomes the default."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_PAYMENT_METHODS,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def update_account_payment_method(
    client: Any,
    account_id: str,
    payment_method_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Update one payment method -
    ``PATCH /accounts/{account_id}/payment_methods/{payment_method_id}``, wrapped in
    ``payment_method``."""
    _require_payload(payload)
    return client.send_patch_request(
        accounts_urls.ACCOUNT_PAYMENT_METHOD,
        path_params={
            "account_id": account_id,
            "payment_method_id": payment_method_id,
        },
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def replace_account_payment_method(
    client: Any,
    account_id: str,
    payment_method_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Replace one payment method -
    ``PUT /accounts/{account_id}/payment_methods/{payment_method_id}``; ``name`` is required, and
    ``processor_type`` and ``payment_processor`` are refused."""
    _require_payload(payload)
    return client.send_put_request(
        accounts_urls.ACCOUNT_PAYMENT_METHOD,
        path_params={
            "account_id": account_id,
            "payment_method_id": payment_method_id,
        },
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def create_account_note(
    client: Any,
    account_id: str,
    note: str,
    *,
    files: Mapping[str, Any] | Sequence[tuple[str, Any]] | None = None,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteView]:
    """Attach a note to an account - ``POST /accounts/{account_id}/notes``; a form, the text as the
    ``note`` field with any ``files`` beside it."""
    _require_note(note)
    return client.send_post_request(
        accounts_urls.ACCOUNT_NOTES,
        path_params={"account_id": account_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteView,
    )


def update_account_note(
    client: Any,
    account_id: str,
    note_id: str,
    note: str,
    *,
    files: Mapping[str, Any] | Sequence[tuple[str, Any]] | None = None,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteView]:
    """Update a note - ``PATCH /accounts/{account_id}/notes/{note_id}``; a form, as the create
    is."""
    _require_note(note)
    return client.send_patch_request(
        accounts_urls.ACCOUNT_NOTE,
        path_params={"account_id": account_id, "note_id": note_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteView,
    )


def upload_account_image(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Set the account's image - ``POST /accounts/{account_id}/image``; ``image_base64`` in a JSON
    body, not a multipart upload."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_IMAGE,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def create_account_custom_object_instance(
    client: Any,
    account_id: str,
    custom_object_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a custom object instance on an account -
    ``POST /accounts/{account_id}/custom_objects/{custom_object_id}``, the schema's ``co_`` id.
    Answers ``custom_object_instance``, unmeasured, so no typed view."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_CUSTOM_OBJECT,
        path_params={"account_id": account_id, "custom_object_id": custom_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_account_custom_object_instance(
    client: Any,
    account_id: str,
    custom_object_instance_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Account]:
    """Update a custom object instance -
    ``PATCH /accounts/{account_id}/custom_objects_instances/{custom_object_instance_id}``, the
    instance's ``coi_`` id; answered with the account."""
    _require_payload(payload)
    return client.send_patch_request(
        accounts_urls.ACCOUNT_CUSTOM_OBJECT_INSTANCE,
        path_params={
            "account_id": account_id,
            "custom_object_instance_id": custom_object_instance_id,
        },
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Account,
    )


def send_account_email(
    client: Any,
    account_id: str,
    payload: AccountPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Send an email and log it on the account -
    ``POST /accounts/{account_id}/communications/emails``; ``to``, ``subject``, ``body``, ``cc`` and
    ``bcc`` with no envelope. It sends real mail, and names no view."""
    _require_payload(payload)
    return client.send_post_request(
        accounts_urls.ACCOUNT_EMAILS,
        path_params={"account_id": account_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def purge_account(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Purge an account and its records permanently - ``POST /accounts/{account_id}/purge``;
    ``204``, no body sent. There is no undo."""
    return client.send_post_request(
        accounts_urls.ACCOUNT_PURGE,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_account(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an account - ``DELETE /accounts/{account_id}``. One with orders, invoices or payments
    against it is locked and answers ``409``, which is not retryable."""
    return client.send_delete_request(
        accounts_urls.ACCOUNT,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_account_contact(
    client: Any,
    account_id: str,
    contact_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one contact - ``DELETE /accounts/{account_id}/contacts/{contact_id}``, the ``con_``
    id."""
    return client.send_delete_request(
        accounts_urls.ACCOUNT_CONTACT,
        path_params={"account_id": account_id, "contact_id": contact_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_account_address(
    client: Any,
    account_id: str,
    address_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one address - ``DELETE /accounts/{account_id}/addresses/{address_id}``."""
    return client.send_delete_request(
        accounts_urls.ACCOUNT_ADDRESS,
        path_params={"account_id": account_id, "address_id": address_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_account_payment_method(
    client: Any,
    account_id: str,
    payment_method_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one payment method -
    ``DELETE /accounts/{account_id}/payment_methods/{payment_method_id}``."""
    return client.send_delete_request(
        accounts_urls.ACCOUNT_PAYMENT_METHOD,
        path_params={
            "account_id": account_id,
            "payment_method_id": payment_method_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_account_note(
    client: Any,
    account_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one note - ``DELETE /accounts/{account_id}/notes/{note_id}``."""
    return client.send_delete_request(
        accounts_urls.ACCOUNT_NOTE,
        path_params={"account_id": account_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_account_note_file(
    client: Any,
    account_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one note attachment -
    ``DELETE /accounts/{account_id}/notes/{note_id}/files/{file_id}``, the attachment's ``uuid``."""
    return client.send_delete_request(
        accounts_urls.ACCOUNT_NOTE_FILE,
        path_params={"account_id": account_id, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_account_image(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Remove the account's image - ``DELETE /accounts/{account_id}/image``; ``204``."""
    return client.send_delete_request(
        accounts_urls.ACCOUNT_IMAGE,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _account_listing(
    client: Any,
    path: str,
    account_id: str,
    query_params: Mapping[str, Any] | None,
    raise_on_error: bool | None,
    response_format: str | None = None,
    dto_type: type[Dto] | None = None,
) -> ApiResponse:
    return client.send_get_request(
        path,
        path_params={"account_id": account_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=dto_type,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )


def _require_note(note: Any) -> None:
    # A None note would go out as the text "None" and be stored as the note.
    if note is None:
        raise SdkUsageError(
            "note is required: the note text is the body of this request, and "
            "None would be encoded as the string 'None' and stored as the note"
        )
