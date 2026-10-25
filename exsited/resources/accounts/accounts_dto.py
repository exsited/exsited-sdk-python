"""Typed views over the account bodies. Reads and writes differ in three places: an address
reads back ``postal_code`` and is written ``post_code``, a contact's name reads nested and is
written flat, and the billing alignment setting reads back under two names."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination
from exsited.resources.custom_components.custom_components_dto import (
    ComponentObjectsDataCustomForm,
    ComponentObjectsDataDetail,
    ComponentObjectsDataParent,
)
from exsited.resources.settings.settings_dto import CustomObject

__all__ = [
    "Reference",
    "User",
    "Currency",
    "TimeZone",
    "CustomForm",
    "SocialLinks",
    "Address",
    "ContactName",
    "ContactEmail",
    "ContactPhone",
    "Contact",
    "PaymentProcessor",
    "PaymentMethod",
    "BillingPreferences",
    "Note",
    "NoteAttachment",
    "Account",
    "AccountList",
    "AccountImage",
    "NoteList",
    "NoteFileList",
    "NoteView",
    "AccountCancel",
    "AccountInformationUpdate",
    "AccountSetPassword",
    "AccountImageUpload",
    "AddressWrite",
    "AddressesCreate",
    "AddressUpdate",
    "ContactWrite",
    "BillingPreferencesWrite",
    "PaymentMethodUpdate",
    "AccountCreate",
    "AccountReplace",
    "AccountReactivate",
    "ContactCreate",
    "ContactsCreate",
    "PaymentMethodCreate",
    "PaymentMethodReplace",
    "CustomObjectInstanceWrite",
    "AccountEmailSend",
    "AccountContact",
    "AccountAddress",
    "AccountNoteFile",
    "AccountKpis",
    "AccountFinancialSummary",
    "AccountFinancialSummaryDetail",
    "AccountCustomObject",
    "AccountComponentObject",
    "AccountAccountingCode",
    "AccountCommunicationPreference",
    "AccountCustomAttribute",
    "NoteViewWatcher",
    "ContactAddress",
    "ContactCustomAttribute",
    "NoteWatcher",
]


class Reference(Dto):
    """A pointer to another record: ``{object, id, name, href}``."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    code: str | None = None
    href: str | None = None
    rate: float | None = None


class User(Dto):
    """Whoever created or last updated a record."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    email: str | None = None
    href: str | None = None


class SocialLinks(Dto):
    """An account's social links. Present on all 1,683 accounts, never ``null``."""

    website: str | None = None
    linkedin: str | None = None
    twitter: str | None = None
    facebook: str | None = None


class Currency(Dto):
    """An account's currency, as a reference. Seen 1,746 times, never ``null``."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    code: str | None = None
    href: str | None = None


class TimeZone(Dto):
    """An account's time zone, as a reference. Seen 1,698 times, never ``null``."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    href: str | None = None


class CustomForm(Dto):
    """The custom form a record was created under."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    href: str | None = None


class Address(Dto):
    """An address as it reads back."""

    object: str | None = None
    id: str | None = None
    address_line_1: str | None = None
    address_line_2: str | None = None
    address_line_3: str | None = None
    address_line_4: str | None = None
    address_line_5: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    #: The read spelling. Written as ``post_code``. See :class:`AddressWrite`.
    postal_code: str | None = None
    default_billing: bool | None = None
    default_shipping: bool | None = None
    href: str | None = None


class ContactName(Dto):
    """A contact's name as it reads back - nested, and split four ways."""

    salutation: str | None = None
    first: str | None = None
    middle: str | None = None
    last: str | None = None
    designation: str | None = None


class ContactEmail(Dto):
    """A contact's email and whether it may be used."""

    address: str | None = None
    do_not_email: bool | None = None
    email_opted_out: bool | None = None


class ContactPhone(Dto):
    """A contact's phone, mobile or fax. All three share this shape."""

    country_code: str | None = None
    area_code: str | None = None
    number: str | None = None
    do_not_call: bool | None = None
    call_opted_out: bool | None = None
    dialing_code: str | None = None
    formatted: str | None = None


class Contact(Dto):
    """A contact as it reads back."""

    object: str | None = None
    id: str | None = None
    #: ``"billing"``, ``"shipping"`` or ``"primary"``, what the slot reads back as. No path takes
    #: it: a read takes the slot, ``CONTACT_1``, and a write takes the ``id``.
    type: str | None = None
    billing_contact: bool | None = None
    shipping_contact: bool | None = None
    receives_billing_information: bool | None = None
    name: ContactName | None = None
    email: ContactEmail | None = None
    phone: ContactPhone | None = None
    mobile: ContactPhone | None = None
    fax: ContactPhone | None = None
    address: ContactAddress | None = None
    custom_attributes: list[ContactCustomAttribute] | None = None
    created_on: str | None = None
    #: ``null`` in 8 of 10 - set only on a contact that has been edited.
    last_updated_on: str | None = None
    created_by: User | None = None
    last_updated_by: User | None = None
    version: int | None = None


class PaymentProcessor(Dto):
    """The processor behind a payment method."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    href: str | None = None


class PaymentMethod(Dto):
    """A payment method as it reads back."""

    object: str | None = None
    id: str | None = None
    processor_type: str | None = None
    status: str | None = None
    default: bool | None = None
    restricted_to_orders: bool | None = None
    #: Untyped: ``null`` in all 7 records measured. It is named as though it holds a list, but
    #: nothing observed says so.
    specified_order_ids: Any = None
    processor: PaymentProcessor | None = None
    reference: str | None = None
    payment_count: int | None = None
    #: ``null`` in 4 of 7 - a method that has never been charged.
    last_used_at: str | None = None
    created_on: str | None = None
    last_updated_on: str | None = None
    created_by: User | None = None
    last_updated_by: User | None = None
    version: int | None = None


class BillingPreferences(Dto):
    """An account's billing preferences as they read back."""

    communication_profile: str | None = None
    invoice_mode: str | None = None
    invoice_term: str | None = None
    billing_period: str | None = None
    billing_start_date: str | None = None
    billing_start_day_of_month: int | None = None
    #: One of the two names the alignment setting reads back under. ``bool`` on all 5 blocks that
    #: carried it.
    charges_aligned_to_billing: bool | None = None
    payment_processor: str | None = None
    payment_mode: str | None = None
    payment_term: str | None = None
    payment_term_alignment: str | None = None
    consolidate_invoice: bool | None = None
    fulfillment_mode: str | None = None
    fulfillment_term: str | None = None
    #: Untyped: an object, seen on 20 of 49, whose keys were never varied enough to establish a
    #: shape.
    proforma_properties: Any = None
    communication_group: str | None = None
    billing_mode: str | None = None
    charging_period: str | None = None
    #: On the 14 records that carried it this read as a string, not a bool - unlike
    #: :attr:`charges_aligned_to_billing`, which the account body carries.
    charging_and_billing_alignment: str | None = None
    charging_start_date: str | None = None
    event_profile: str | None = None


class NoteAttachment(Dto):
    """A file attached to a note."""

    uuid: str | None = None
    filename: str | None = None
    content_type: str | None = None
    size: int | None = None
    href: str | None = None


class Note(Dto):
    """A note on an account."""

    object: str | None = None
    id: str | None = None
    #: HTML, stored and returned as written.
    content: str | None = None
    account: Reference | None = None
    group: Any = None
    user: Any = None
    attachments: list[NoteAttachment] | None = None
    watchers: list[NoteWatcher] | None = None
    created_on: str | None = None
    last_updated_on: str | None = None
    created_by: User | None = None
    last_updated_by: User | None = None
    version: int | None = None
    href: str | None = None


class Account(Dto):
    """One account."""

    ENVELOPE_KEY = "account"

    object: str | None = None
    #: The short code - ``"W13ZGY"`` - and what every path takes. Never ``null`` in 1,686 records.
    id: str | None = None
    name: str | None = None
    status: str | None = None
    type: str | None = None
    display_name: str | None = None
    email_address: str | None = None
    description: str | None = None
    currency: Currency | None = None
    time_zone: TimeZone | None = None
    #: ``null`` on 1,013 of 1,678 - an account with no tax profile.
    tax: Reference | None = None
    custom_form: CustomForm | None = None
    parent_account_id: str | None = None
    #: Untyped: ``null`` in all 1,683 records measured. Read ``get_account_image`` for an
    #: account's image instead.
    image_url: Any = None
    workflow_status: str | None = None
    social_links: SocialLinks | None = None
    communication_preferences: list[AccountCommunicationPreference] | None = None
    invoice_parent_account: bool | None = None
    portal_access: bool | None = None
    origin: str | None = None
    group: Reference | None = None
    manager: Reference | None = None
    #: ``null`` on 1,663 of 1,678 - rarely set.
    sales_rep: Reference | None = None
    #: ``null`` on 1,673 of 1,678 - rarely set.
    user_team: Reference | None = None
    accounting_code: AccountAccountingCode | None = None
    pricing_level: Reference | None = None
    referral_tracking: str | None = None
    created_on: str | None = None
    #: ``null`` on 1,429 of 1,678 - set only once an account has been edited.
    last_updated_on: str | None = None
    created_by: User | None = None
    last_updated_by: User | None = None
    version: int | None = None
    href: str | None = None

    # A plain get_account sends these inline; inventories, partial_invoices, activity_logs and
    # notes arrive only from their own endpoints.
    addresses: list[Address] | None = None
    contacts: list[Contact] | None = None
    payment_methods: list[PaymentMethod] | None = None
    billing_preferences: BillingPreferences | None = None
    custom_attributes: list[AccountCustomAttribute] | None = None
    custom_objects: list[Reference] | None = None
    inventories: list[Any] | None = None
    #: The key ``get_account_quote_partial_invoices`` answers under - which does not match its
    #: path segment.
    partial_invoices: list[Any] | None = None
    activity_logs: list[Any] | None = None
    payment_method: PaymentMethod | None = None
    # Null in every record measured, so untyped.
    tax_id: Any = None
    # Null in every record measured, so untyped.
    tax_id_number: Any = None


class AccountList(Dto):
    """A listing of accounts - the v4 list envelope."""

    object: str | None = None
    #: The path the listing was served from, e.g. ``"/api/v4/accounts"``.
    url: str | None = None
    data: list[Account] | None = None
    pagination: Pagination | None = None


class AccountImage(Dto):
    """What ``GET /accounts/{account_id}/image`` answers."""

    ENVELOPE_KEY = "account"

    image_uri: str | None = None
    account_id: str | None = None


class NoteView(Dto):
    """One note - ``{"note": {...}}``."""

    ENVELOPE_KEY = "note"

    object: str | None = None
    id: str | None = None
    content: str | None = None
    account: Reference | None = None
    attachments: list[NoteAttachment] | None = None
    watchers: list[NoteViewWatcher] | None = None
    created_on: str | None = None
    last_updated_on: str | None = None
    created_by: User | None = None
    last_updated_by: User | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    # Null in every record measured, so untyped.
    user: Any = None


class NoteList(Dto):
    """A listing of notes - the v4 list envelope."""

    object: str | None = None
    url: str | None = None
    data: list[Note] | None = None
    pagination: Pagination | None = None


class NoteFileList(Dto):
    """A listing of one note's attachments - the same envelope, different records."""

    object: str | None = None
    url: str | None = None
    data: list[NoteAttachment] | None = None
    pagination: Pagination | None = None


class AccountCancel(Dto):
    """Body for ``cancel_account``: ``{"account": {"effective_date": ...}}``."""

    ENVELOPE_KEY = "account"

    #: Required, and ``YYYY-MM-DD``. Any other format is a 400 with code ``invalid`` - the endpoint
    #: does not parse a datetime.
    effective_date: str | None = None


class AccountInformationUpdate(Dto):
    """Body for ``update_account_information``."""

    ENVELOPE_KEY = "account"

    name: str | None = None
    display_name: str | None = None
    description: str | None = None
    email_address: str | None = None
    origin: str | None = None
    user_team: str | None = None
    group: str | None = None
    manager: str | None = None
    referral_tracking: str | None = None
    parent_account: str | None = None
    #: The currency code, not the nested object the read returns.
    currency: str | None = None
    #: The time zone name, not the nested object the read returns.
    time_zone: str | None = None
    grant_portal_access: bool | None = None
    grant_portal_password: str | None = None
    #: ``{"uuid": ..., "code": ...}``.
    tax: Any = None


class AccountSetPassword(Dto):
    """Body for ``set_account_password``."""

    password: str | None = None
    confirm_password: str | None = None


class AccountImageUpload(Dto):
    """Body for ``upload_account_image``: base64 in JSON, not a multipart upload."""

    image_base64: str | None = None


class AddressWrite(Dto):
    """One address as it is written."""

    address_line_1: str | None = None
    address_line_2: str | None = None
    address_line_3: str | None = None
    address_line_4: str | None = None
    address_line_5: str | None = None
    city: str | None = None
    #: The name, not an id.
    state: str | None = None
    #: The name, not an id.
    country: str | None = None
    #: The write spelling. Reads back as ``postal_code``.
    post_code: str | None = None
    default_billing: bool | None = None
    default_shipping: bool | None = None


class AddressesCreate(Dto):
    """Body for ``create_account_addresses``: a list under ``addresses``."""

    addresses: list[AddressWrite] | None = None


class AddressUpdate(Dto):
    """Body for ``update_account_address``: one address under a singular key."""

    ENVELOPE_KEY = "address"

    address_line_1: str | None = None
    address_line_2: str | None = None
    address_line_3: str | None = None
    address_line_4: str | None = None
    address_line_5: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    post_code: str | None = None
    default_billing: bool | None = None
    default_shipping: bool | None = None


class ContactWrite(Dto):
    """Body for ``update_account_contact`` and ``replace_account_contact``."""

    ENVELOPE_KEY = "contact"

    salutation: str | None = None
    designation: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    email: ContactEmail | None = None
    phone: ContactPhone | None = None
    mobile: ContactPhone | None = None
    fax: ContactPhone | None = None
    address_line_1: str | None = None
    address_line_2: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    post_code: str | None = None


class BillingPreferencesWrite(Dto):
    """Body for ``replace_account_billing_preferences``."""

    ENVELOPE_KEY = "billing_preferences"

    invoice_mode: str | None = None
    invoice_term: str | None = None
    billing_period: str | None = None
    #: An enum, not a date - ``"DAY_OF_MONTH"`` and the like. A calendar date is a 400 with code
    #: ``matches_invalid``.
    billing_start_date: str | None = None
    billing_start_day_of_month: str | None = None
    #: Written as a ``bool``. Reads back as a ``str`` under this same name - see
    #: :class:`BillingPreferences`, which declares both read spellings.
    charging_and_billing_alignment: bool | None = None
    payment_processor: str | None = None
    payment_term: str | None = None


class PaymentMethodUpdate(Dto):
    """Body for ``update_account_payment_method``."""

    ENVELOPE_KEY = "payment_method"

    default: bool | None = None
    reference: str | None = None
    status: str | None = None


# The nine bodies below hold the keys the server accepts; it refuses any other key with a 400
# naming it. A field whose shape the server does not check is Any.


class AccountCreate(Dto):
    """Body for ``create_account``. ``name`` and ``type`` (``CUSTOMER``, ``SUPPLIER`` or
    ``CUSTOMER_AND_SUPPLIER``) are required; writes are flat, as in
    :class:`AccountInformationUpdate`."""

    ENVELOPE_KEY = "account"

    name: str | None = None
    type: str | None = None
    display_name: str | None = None
    status: str | None = None
    email_address: str | None = None
    #: The currency code; the instance default when omitted.
    currency: str | None = None
    #: The time zone name.
    time_zone: str | None = None
    description: str | None = None
    origin: str | None = None
    user_team: str | None = None
    website: str | None = None
    linkedin: str | None = None
    twitter: str | None = None
    facebook: str | None = None
    pricing_level: str | None = None
    invoice_term: str | None = None
    payment_term: str | None = None
    communication_profile: str | None = None
    payment_processor: str | None = None
    parent_account: str | None = None
    sales_rep: str | None = None
    referral_tracking: str | None = None
    group: str | None = None
    manager: str | None = None
    portal_password: str | None = None
    portal_access: bool | None = None
    grant_portal_access: bool | None = None
    grant_portal_password: str | None = None
    tax_exempt: bool | None = None
    invoice_parent_account: bool | None = None
    #: A decimal; the binder parses a number or a numeric string.
    credit_limit: Any = None
    custom_form: str | None = None
    communication_preferences: list[Any] | None = None
    #: ``{"account_receivable": "<name>"}``.
    accounting_code: Any = None
    #: ``{"uuid": ..., "code": ...}``.
    tax: Any = None
    billing_preferences: Any = None
    custom_attributes: list[Any] | None = None
    #: Each needs a ``type``, as in :class:`ContactCreate`.
    contacts: list[Any] | None = None
    #: Each as :class:`AddressWrite`.
    addresses: list[Any] | None = None
    #: Each as :class:`PaymentMethodCreate`.
    payment_methods: list[Any] | None = None
    discount_profiles: list[Any] | None = None


class AccountReplace(Dto):
    """Body for ``replace_account``. ``name`` and ``type`` are required on every call; ``status``,
    ``addresses``, ``payment_methods`` and the two ``grant_portal_*`` keys are refused."""

    ENVELOPE_KEY = "account"

    name: str | None = None
    type: str | None = None
    display_name: str | None = None
    email_address: str | None = None
    currency: str | None = None
    time_zone: str | None = None
    description: str | None = None
    origin: str | None = None
    user_team: str | None = None
    website: str | None = None
    linkedin: str | None = None
    twitter: str | None = None
    facebook: str | None = None
    pricing_level: str | None = None
    invoice_term: str | None = None
    payment_term: str | None = None
    communication_profile: str | None = None
    payment_processor: str | None = None
    parent_account: str | None = None
    sales_rep: str | None = None
    referral_tracking: str | None = None
    group: str | None = None
    manager: str | None = None
    portal_password: str | None = None
    portal_access: bool | None = None
    tax_exempt: bool | None = None
    invoice_parent_account: bool | None = None
    credit_limit: Any = None
    custom_form: str | None = None
    communication_preferences: list[Any] | None = None
    accounting_code: Any = None
    tax: Any = None
    billing_preferences: Any = None
    custom_attributes: list[Any] | None = None
    discount_profiles: list[Any] | None = None
    #: An entry with an ``id`` (``"con_..."``) updates that contact; one without is created and
    #: needs a ``type``.
    contacts: list[Any] | None = None


class AccountReactivate(Dto):
    """Body for ``reactivate_account``, the same as :class:`AccountCancel`. To reactivate now send
    the mapping ``{"account": {"effective_date": None}}``: an unset field is left out, and a body
    without the key is a 400."""

    ENVELOPE_KEY = "account"

    effective_date: str | None = None


class ContactCreate(Dto):
    """One contact as it is created. ``type`` is required and is the slot's enum name,
    ``CONTACT_1`` to ``CONTACT_5``; it reads back as something else, ``CONTACT_1`` as
    ``billing``."""

    type: str | None = None
    salutation: str | None = None
    designation: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    email: ContactEmail | None = None
    phone: ContactPhone | None = None
    mobile: ContactPhone | None = None
    fax: ContactPhone | None = None
    address_line_1: str | None = None
    address_line_2: str | None = None
    address_line_3: str | None = None
    address_line_4: str | None = None
    address_line_5: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    post_code: str | None = None
    receive_billing_information: bool | None = None
    custom_attributes: list[Any] | None = None


class ContactsCreate(Dto):
    """Body for ``create_account_contacts``: a list under ``contacts``. The server also takes one
    object under ``contact``."""

    contacts: list[ContactCreate] | None = None


class PaymentMethodCreate(Dto):
    """Body for ``create_account_payment_method``: one method, under a singular key, the
    ``OTHER`` key set. ``processor_type``, ``payment_processor`` (a ``pp_`` id) and ``reference``
    are required; ``name`` is refused."""

    ENVELOPE_KEY = "payment_method"

    #: ``DIRECT_CREDIT``, ``DIRECT_DEBIT`` or ``OTHER``; the card and bank keys the first two
    #: accept are not modelled, so send a mapping for those.
    processor_type: str | None = None
    payment_processor: str | None = None
    #: At most 70 characters.
    reference: str | None = None
    status: str | None = None
    default: bool | None = None
    note: str | None = None
    use_for_specified_orders: bool | None = None
    specified_orders: list[Any] | None = None


class PaymentMethodReplace(Dto):
    """Body for ``replace_account_payment_method``. ``name`` is required;
    ``processor_type`` and ``payment_processor`` cannot be replaced and are refused."""

    ENVELOPE_KEY = "payment_method"

    name: str | None = None
    reference: str | None = None
    default: bool | None = None
    note: str | None = None
    use_for_specified_orders: bool | None = None
    specified_orders: list[Any] | None = None
    custom_attributes: list[Any] | None = None


class CustomObjectInstanceWrite(Dto):
    """Body for both custom object instance writes, under the plural ``custom_object_instances``
    for one instance; ``attributes`` must be a list of ``{name, value}``."""

    ENVELOPE_KEY = "custom_object_instances"

    attributes: list[Any] | None = None


class AccountEmailSend(Dto):
    """Body for ``send_account_email``, with no envelope. ``to`` is required with at least one
    address; ``subject`` is at most 255 characters."""

    to: list[str] | None = None
    subject: str | None = None
    body: str | None = None
    cc: list[str] | None = None
    bcc: list[str] | None = None


class AccountContact(Account):
    """What ``get_account_contact`` answers: a :class:`Account` whose ``contacts`` is one record,
    not a list."""

    contacts: Contact | None = None


class AccountAddress(Account):
    """What ``get_account_address`` answers: a :class:`Account` whose ``addresses`` is one
    record, not a list."""

    addresses: Address | None = None


class AccountNoteFile(Dto):
    """What ``get_account_note_file`` answers, under ``file``."""

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class AccountKpis(Dto):
    """What ``get_account_kpis`` answers, under ``account_kpis``."""

    MEASURED_FROM = ("GET /api/{api_version}/accounts/{account_id}/kpis",)

    ENVELOPE_KEY = "account_kpis"

    object: str | None = None
    total_revenue: str | None = None
    monthly_recurring_revenue: str | None = None
    total_collected: str | None = None
    total_refunded: str | None = None
    total_outstanding: str | None = None
    total_overdue: str | None = None
    total_balance: str | None = None
    total_credit_balance: str | None = None
    total_orders: int | None = None
    active_orders: int | None = None
    # Null in every record measured, so untyped.
    last_reactivated_at: Any = None
    # Null in every record measured, so untyped.
    last_cancelled_at: Any = None
    # Null in every record measured, so untyped.
    deleted_at: Any = None
    computed_at: str | None = None


class AccountFinancialSummary(Dto):
    """What ``get_account_financial_summary`` answers, under ``account``: its ``name`` and the
    ``financial_summary`` itself."""

    MEASURED_FROM = ("GET /api/{api_version}/accounts/{account_id}/financial_summary",)

    ENVELOPE_KEY = "account"

    name: str | None = None
    financial_summary: AccountFinancialSummaryDetail | None = None


class AccountFinancialSummaryDetail(Dto):
    """A :class:`AccountFinancialSummary`'s ``financial_summary``."""

    total_due: str | None = None
    total_grand: str | None = None
    total_paid: str | None = None
    invoice_count: int | None = None
    total_due_invoice_count: int | None = None
    total_overdue_amount: str | None = None
    total_overdue_invoice_count: int | None = None
    collected_this_month: str | None = None


class AccountCustomObject(CustomObject):
    """What ``get_account_custom_object`` answers, under ``custom_object``: the schema, with the
    account's instances of it and their own ``pagination``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/accounts/{account_id}/custom_objects/{custom_object_id}",
    )

    ENVELOPE_KEY = "custom_object"

    #: Empty in every record measured, so its entries are untyped.
    instances: list[Any] | None = None
    pagination: Pagination | None = None


class AccountComponentObject(Dto):
    """What ``get_account_component_object`` answers, under ``custom_component_object``: the
    fields of one entry of the listing ``get_account_component_objects`` answers."""

    MEASURED_FROM = (
        "GET /api/{api_version}/accounts/{account_id}/component/{component_id}/{component_object_id}",
    )

    ENVELOPE_KEY = "custom_component_object"

    # Declared here rather than inherited from ComponentObjectsData: a view resolves its
    # annotations in the module that declares it, where the nested names of another module's
    # base do not exist, so an inherited nested field raises NameError on the first read.
    accounts: list[Any] | None = None
    attribute_groups: list[Any] | None = None
    attributes: list[Any] | None = None
    code: str | None = None
    component: ComponentObjectsDataDetail | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    custom_form: ComponentObjectsDataCustomForm | None = None
    custom_objects: list[Any] | None = None
    href: str | None = None
    id: str | None = None
    items: list[Any] | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    orders: list[Any] | None = None
    parents: list[ComponentObjectsDataParent] | None = None
    quotes: list[Any] | None = None
    restrictions: list[Any] | None = None
    status: str | None = None
    version: int | None = None
    workflow_data: list[Any] | None = None
    # Null in every record measured, so untyped.
    workflow_stage: Any = None
    # Null in every record measured, so untyped.
    workflow_status: Any = None
    # Null in every record measured, so untyped.
    workflow_status_uuid: Any = None


class AccountAccountingCode(Dto):
    """A :class:`Account`'s ``accounting_code``."""

    account_receivable: str | None = None


class AccountCommunicationPreference(Dto):
    """One entry of a :class:`Account`'s ``communication_preferences``."""

    channel: str | None = None
    enabled: bool | None = None


class AccountCustomAttribute(Dto):
    """One entry of a :class:`Account`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: Any = None


class NoteViewWatcher(Dto):
    """One entry of a :class:`NoteView`'s ``watchers``."""

    # Null in every record measured, so untyped.
    email: Any = None
    name: str | None = None
    type: str | None = None


class ContactAddress(Dto):
    """A :class:`Contact`'s ``address``."""

    city: str | None = None
    country: str | None = None
    # Null in every record measured, so untyped.
    country_code: Any = None
    line_1: str | None = None
    line_2: str | None = None
    postal_code: str | None = None
    state: str | None = None


class ContactCustomAttribute(Dto):
    """One entry of a :class:`Contact`'s ``custom_attributes``."""

    name: str | None = None
    value: Any = None


class NoteWatcher(Dto):
    """One entry of a :class:`Note`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None
