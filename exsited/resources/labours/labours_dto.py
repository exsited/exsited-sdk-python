"""Typed views over the labour bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Labour",
    "LabourList",
    "LabourProfile",
    "LabourProfileList",
    "LabourAvailability",
    "LabourAvailabilityList",
    "LabourProfileView",
    "LabourCalendar",
    "LabourProfileSessionList",
    "LabourProfileSessionView",
    "LabourOrderList",
    "LabourProfileViewCurrency",
    "LabourProfileViewTax",
    "LabourProfileViewRow",
    "LabourProfileViewSession",
    "LabourProfileViewCreatedBy",
    "LabourProfileViewLastUpdatedBy",
    "LabourLabourProfile",
    "LabourCustomForm",
    "LabourLabourContact",
    "LabourLabourCustomAvailability",
    "LabourCreatedBy",
    "LabourLastUpdatedBy",
    "LabourOrder",
    "LabourAvailabilityLabourProfile",
    "LabourAvailabilityScheduleList",
    "LabourAvailabilitySessionList",
    "LabourProfileCurrency",
    "LabourProfileTax",
    "LabourProfileRow",
    "LabourProfileSession",
    "LabourProfileCreatedBy",
    "LabourProfileLastUpdatedBy",
    "LabourProfileViewSessionPrice",
    "LabourProfileViewSessionAvailability",
    "LabourProfileViewSessionWorkingHour",
    "LabourLabourContactPhone",
    "LabourLabourContactFax",
    "LabourLabourContactMobile",
    "LabourOrderCurrency",
    "LabourOrderTimeZone",
    "LabourOrderCustomForm",
    "LabourOrderAccount",
    "LabourOrderCommunicationPreference",
    "LabourOrderBillingPreferences",
    "LabourAvailabilitySessionListScheduleList",
    "LabourProfileSessionPrice",
    "LabourProfileSessionAvailability",
    "LabourProfileSessionWorkingHour",
    "LabourProfileViewSessionPricePricingLevel",
    "LabourProfileViewSessionPriceHour",
    "LabourOrderBillingPreferencesProformaProperties",
    "LabourProfileSessionPricePricingLevel",
    "LabourProfileSessionPriceHour",
]


class Labour(Dto):
    """The labour body, under ``labour``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/labours",
        "GET /api/{api_version}/labours/available_for_booking",
        "GET /api/{api_version}/labours/{labour_uuid}",
        "POST /api/{api_version}/labours",
        "PATCH /api/{api_version}/labours/{labour_uuid}",
        "POST /api/{api_version}/labours/{labour_id}/cancel",
        "POST /api/{api_version}/labours/{labour_id}/reactivate",
    )

    ENVELOPE_KEY = "labour"

    activity_logs: list[Any] | None = None
    code: str | None = None
    created_by: LabourCreatedBy | None = None
    created_on: str | None = None
    custom_form: LabourCustomForm | None = None
    description: str | None = None
    display_name: str | None = None
    email_address: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    image_name: Any = None
    labour_availability: list[Any] | None = None
    labour_contacts: list[LabourLabourContact] | None = None
    labour_custom_availability: list[LabourLabourCustomAvailability] | None = None
    labour_profile: LabourLabourProfile | None = None
    last_updated_by: LabourLastUpdatedBy | None = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    use_custom_availability: bool | None = None
    version: int | None = None


class LabourList(Dto):
    """One page of ``Labour`` records, under ``data``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/labours",
        "GET /api/{api_version}/labours/available_for_booking",
    )

    data: list[Labour] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class LabourProfile(Dto):
    """The labour profile body."""

    MEASURED_FROM = ("GET /api/{api_version}/labour_profiles",)

    created_by: LabourProfileCreatedBy | None = None
    created_on: str | None = None
    currency: LabourProfileCurrency | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    labours: list[LabourProfileRow] | None = None
    last_updated_by: LabourProfileLastUpdatedBy | None = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    max_booking_limit: Any = None
    name: str | None = None
    object: str | None = None
    sessions: list[LabourProfileSession] | None = None
    status: str | None = None
    tax: LabourProfileTax | None = None
    tax_inclusive: bool | None = None
    version: int | None = None


class LabourProfileList(Dto):
    """One page of ``LabourProfile`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/labour_profiles",)

    data: list[LabourProfile] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class LabourAvailability(Dto):
    """The labour availability body."""

    MEASURED_FROM = ("GET /api/{api_version}/labour_availability",)

    available_list: list[Any] | None = None
    code: str | None = None
    display_name: str | None = None
    email_address: str | None = None
    id: str | None = None
    labour_profile: LabourAvailabilityLabourProfile | None = None
    name: str | None = None
    object: str | None = None
    processed_schedule_list: dict[str, Any] | None = None
    schedule_list: list[LabourAvailabilityScheduleList] | None = None
    session_list: list[LabourAvailabilitySessionList] | None = None
    status: str | None = None
    unavailable_list: list[Any] | None = None
    use_custom_availability: bool | None = None
    version: int | None = None


class LabourAvailabilityList(Dto):
    """One page of ``LabourAvailability`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/labour_availability",)

    data: list[LabourAvailability] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class LabourCalendar(LabourAvailability):
    """What ``get_labour_calendar`` answers, under ``labour_calendar``: a
    :class:`LabourAvailability` record for one labour."""

    MEASURED_FROM = ("GET /api/{api_version}/labours/{labour_id}/availability",)

    ENVELOPE_KEY = "labour_calendar"


class LabourProfileView(Dto):
    """What ``get_labour_profile`` answers, under ``labour_profile``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/labour_profiles/{labour_profile_id}",
        "POST /api/{api_version}/labour_profiles",
    )

    ENVELOPE_KEY = "labour_profile"

    activity_logs: list[Any] | None = None
    created_by: LabourProfileViewCreatedBy | None = None
    created_on: str | None = None
    currency: LabourProfileViewCurrency | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    labours: list[LabourProfileViewRow] | None = None
    last_updated_by: LabourProfileViewLastUpdatedBy | None = None
    last_updated_on: str | None = None
    max_booking_limit: int | None = None
    name: str | None = None
    object: str | None = None
    sessions: list[LabourProfileViewSession] | None = None
    status: str | None = None
    tax: LabourProfileViewTax | None = None
    tax_inclusive: bool | None = None
    version: int | None = None


class LabourOrderList(Dto):
    """One page of what ``get_labour_orders`` lists, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/labours/{labour_uuid}/orders",)

    data: list[LabourOrder] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class LabourProfileViewCurrency(Dto):
    """A :class:`LabourProfileView`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileViewTax(Dto):
    """A :class:`LabourProfileView`'s ``tax``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class LabourProfileViewRow(Dto):
    """One entry of a :class:`LabourProfileView`'s ``labours``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileViewSession(Dto):
    """One entry of a :class:`LabourProfileView`'s ``sessions``."""

    allow_overtime: bool | None = None
    availability: list[LabourProfileViewSessionAvailability] | None = None
    end_date: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    prices: list[LabourProfileViewSessionPrice] | None = None
    start_date: str | None = None
    status: str | None = None
    working_hours: list[LabourProfileViewSessionWorkingHour] | None = None


class LabourProfileSessionList(Dto):
    """One page of a labour profile's sessions, under ``data``, each a
    :class:`LabourProfileViewSession`."""

    MEASURED_FROM = ("GET /api/{api_version}/labour_profiles/{labour_profile_id}/sessions",)

    data: list[LabourProfileViewSession] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class LabourProfileSessionView(LabourProfileViewSession):
    """What ``get_labour_profile_session`` answers, under ``labour_profile_session``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/labour_profiles/{labour_profile_id}/sessions/{session_id}",
    )

    ENVELOPE_KEY = "labour_profile_session"


class LabourProfileViewCreatedBy(Dto):
    """A :class:`LabourProfileView`'s ``created_by``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileViewLastUpdatedBy(Dto):
    """A :class:`LabourProfileView`'s ``last_updated_by``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourLabourProfile(Dto):
    """A :class:`Labour`'s ``labour_profile``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourCustomForm(Dto):
    """A :class:`Labour`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourLabourContact(Dto):
    """One entry of a :class:`Labour`'s ``labour_contacts``."""

    address_line_1: str | None = None
    address_line_2: str | None = None
    address_line_3: str | None = None
    address_line_4: str | None = None
    address_line_5: str | None = None
    city: str | None = None
    contact_type: str | None = None
    country: str | None = None
    designation: str | None = None
    email_address: str | None = None
    fax: LabourLabourContactFax | None = None
    first_name: str | None = None
    id: str | None = None
    last_name: str | None = None
    # Null in every record measured, so untyped.
    middle_name: Any = None
    mobile: LabourLabourContactMobile | None = None
    object: str | None = None
    phone: LabourLabourContactPhone | None = None
    post_code: str | None = None
    receive_email: bool | None = None
    salutation: str | None = None
    state: str | None = None
    status: str | None = None


class LabourLabourCustomAvailability(Dto):
    """One entry of a :class:`Labour`'s ``labour_custom_availability``."""

    available: bool | None = None
    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None


class LabourCreatedBy(Dto):
    """A :class:`Labour`'s ``created_by``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourLastUpdatedBy(Dto):
    """A :class:`Labour`'s ``last_updated_by``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourOrder(Dto):
    """One entry of a :class:`LabourOrderList`'s ``data``."""

    account: LabourOrderAccount | None = None
    allow_contract: bool | None = None
    # Null in every record measured, so untyped.
    billing_address: Any = None
    billing_preferences: LabourOrderBillingPreferences | None = None
    billing_start_date: str | None = None
    communication_preferences: list[LabourOrderCommunicationPreference] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: LabourOrderCurrency | None = None
    custom_form: LabourOrderCustomForm | None = None
    # Null in every record measured, so untyped.
    customer_purchase_order_id: Any = None
    # Null in every record measured, so untyped.
    description: Any = None
    # Null in every record measured, so untyped.
    discount_profile: Any = None
    display_name: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    invoice_note: Any = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    manager: Any = None
    name: str | None = None
    next_billing_from_date: str | None = None
    object: str | None = None
    order_start_date: str | None = None
    order_type: str | None = None
    # Null in every record measured, so untyped.
    origin: Any = None
    # Null in every record measured, so untyped.
    original_total: Any = None
    pre_order: bool | None = None
    price_tax_inclusive: bool | None = None
    quote_converted: bool | None = None
    quote_order: bool | None = None
    # Null in every record measured, so untyped.
    referral_account: Any = None
    # Null in every record measured, so untyped.
    sales_rep: Any = None
    # Null in every record measured, so untyped.
    shipping_address: Any = None
    shipping_cost: float | None = None
    # Null in every record measured, so untyped.
    shipping_profile: Any = None
    status: str | None = None
    time_zone: LabourOrderTimeZone | None = None
    version: int | None = None


class LabourAvailabilityLabourProfile(Dto):
    """A :class:`LabourAvailability`'s ``labour_profile``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourAvailabilityScheduleList(Dto):
    """One entry of a :class:`LabourAvailability`'s ``schedule_list``."""

    available: bool | None = None
    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None


class LabourAvailabilitySessionList(Dto):
    """One entry of a :class:`LabourAvailability`'s ``session_list``."""

    end_date: str | None = None
    name: str | None = None
    processed_schedule_list: dict[str, Any] | None = None
    schedule_list: list[LabourAvailabilitySessionListScheduleList] | None = None
    start_date: str | None = None
    uuid: str | None = None


class LabourProfileCurrency(Dto):
    """A :class:`LabourProfile`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileTax(Dto):
    """A :class:`LabourProfile`'s ``tax``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class LabourProfileRow(Dto):
    """One entry of a :class:`LabourProfile`'s ``labours``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileSession(Dto):
    """One entry of a :class:`LabourProfile`'s ``sessions``."""

    allow_overtime: bool | None = None
    availability: list[LabourProfileSessionAvailability] | None = None
    end_date: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    prices: list[LabourProfileSessionPrice] | None = None
    start_date: str | None = None
    status: str | None = None
    working_hours: list[LabourProfileSessionWorkingHour] | None = None


class LabourProfileCreatedBy(Dto):
    """A :class:`LabourProfile`'s ``created_by``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileLastUpdatedBy(Dto):
    """A :class:`LabourProfile`'s ``last_updated_by``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileViewSessionPrice(Dto):
    """One entry of a :class:`LabourProfileViewSession`'s ``prices``."""

    enabled_pro_rata: bool | None = None
    hours: list[LabourProfileViewSessionPriceHour] | None = None
    id: str | None = None
    object: str | None = None
    peak_hourly: list[Any] | None = None
    price: float | None = None
    price_type: str | None = None
    pricing_level: LabourProfileViewSessionPricePricingLevel | None = None
    status: str | None = None


class LabourProfileViewSessionAvailability(Dto):
    """One entry of a :class:`LabourProfileViewSession`'s ``availability``."""

    available: bool | None = None
    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None
    status: str | None = None


class LabourProfileViewSessionWorkingHour(Dto):
    """One entry of a :class:`LabourProfileViewSession`'s ``working_hours``."""

    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    start_time: str | None = None
    status: str | None = None


class LabourLabourContactPhone(Dto):
    """A :class:`LabourLabourContact`'s ``phone``."""

    area_code: str | None = None
    country_code: str | None = None
    do_not_call: bool | None = None
    full: str | None = None
    number: str | None = None


class LabourLabourContactFax(Dto):
    """A :class:`LabourLabourContact`'s ``fax``."""

    area_code: str | None = None
    country_code: str | None = None
    do_not_call: bool | None = None
    full: str | None = None
    number: str | None = None


class LabourLabourContactMobile(Dto):
    """A :class:`LabourLabourContact`'s ``mobile``."""

    area_code: str | None = None
    country_code: str | None = None
    do_not_call: bool | None = None
    full: str | None = None
    number: str | None = None


class LabourOrderCurrency(Dto):
    """A :class:`LabourOrder`'s ``currency``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourOrderTimeZone(Dto):
    """A :class:`LabourOrder`'s ``time_zone``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourOrderCustomForm(Dto):
    """A :class:`LabourOrder`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourOrderAccount(Dto):
    """A :class:`LabourOrder`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourOrderCommunicationPreference(Dto):
    """One entry of a :class:`LabourOrder`'s ``communication_preferences``."""

    channel: str | None = None
    enabled: bool | None = None


class LabourOrderBillingPreferences(Dto):
    """A :class:`LabourOrder`'s ``billing_preferences``."""

    billing_period: str | None = None
    communication_profile: str | None = None
    consolidate_invoice: bool | None = None
    fulfillment_mode: str | None = None
    fulfillment_term: str | None = None
    invoice_mode: str | None = None
    invoice_term: str | None = None
    payment_mode: str | None = None
    payment_processor: str | None = None
    payment_term: str | None = None
    payment_term_alignment: str | None = None
    proforma_properties: LabourOrderBillingPreferencesProformaProperties | None = None


class LabourAvailabilitySessionListScheduleList(Dto):
    """One entry of a :class:`LabourAvailabilitySessionList`'s ``schedule_list``."""

    available: str | None = None
    end_time: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None
    uuid: str | None = None


class LabourProfileSessionPrice(Dto):
    """One entry of a :class:`LabourProfileSession`'s ``prices``."""

    enabled_pro_rata: bool | None = None
    hours: list[LabourProfileSessionPriceHour] | None = None
    id: str | None = None
    object: str | None = None
    peak_hourly: list[Any] | None = None
    price: float | None = None
    price_type: str | None = None
    pricing_level: LabourProfileSessionPricePricingLevel | None = None
    status: str | None = None


class LabourProfileSessionAvailability(Dto):
    """One entry of a :class:`LabourProfileSession`'s ``availability``."""

    available: bool | None = None
    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None
    status: str | None = None


class LabourProfileSessionWorkingHour(Dto):
    """One entry of a :class:`LabourProfileSession`'s ``working_hours``."""

    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    start_time: str | None = None
    status: str | None = None


class LabourProfileViewSessionPricePricingLevel(Dto):
    """A :class:`LabourProfileViewSessionPrice`'s ``pricing_level``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileViewSessionPriceHour(Dto):
    """One entry of a :class:`LabourProfileViewSessionPrice`'s ``hours``."""

    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    price: float | None = None
    start_time: str | None = None
    status: str | None = None


class LabourOrderBillingPreferencesProformaProperties(Dto):
    """A :class:`LabourOrderBillingPreferences`'s ``proforma_properties``."""

    # Null in every record measured, so untyped.
    acceptance_date: Any = None
    acceptance_required: bool | None = None
    # Null in every record measured, so untyped.
    acceptance_term: Any = None
    payment_required: bool | None = None
    # Null in every record measured, so untyped.
    terms_and_conditions: Any = None


class LabourProfileSessionPricePricingLevel(Dto):
    """A :class:`LabourProfileSessionPrice`'s ``pricing_level``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class LabourProfileSessionPriceHour(Dto):
    """One entry of a :class:`LabourProfileSessionPrice`'s ``hours``."""

    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    price: float | None = None
    start_time: str | None = None
    status: str | None = None
