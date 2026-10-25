"""Typed views over the rental asset bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "RentalAsset",
    "RentalAssetList",
    "RentalAssetProfile",
    "RentalAssetProfileList",
    "RentalAssetAvailability",
    "RentalAssetAvailabilityList",
    "RentalAssetProfileView",
    "RentalAssetProfileViewCurrency",
    "RentalAssetProfileViewRow",
    "RentalAssetProfileViewRentalAssetProfileSession",
    "RentalAssetProfileViewCreatedBy",
    "RentalAssetProfileViewLastUpdatedBy",
    "RentalAssetRentalAssetProfile",
    "RentalAssetCustomForm",
    "RentalAssetRentalAssetCustomAvailability",
    "RentalAssetCreatedBy",
    "RentalAssetLastUpdatedBy",
    "RentalAssetAvailabilityRentalAssetProfile",
    "RentalAssetAvailabilitySessionList",
    "RentalAssetAvailabilityScheduleList",
    "RentalAssetProfileCurrency",
    "RentalAssetProfileRow",
    "RentalAssetProfileRentalAssetProfileSession",
    "RentalAssetProfileCreatedBy",
    "RentalAssetProfileLastUpdatedBy",
    "RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionPrice",
    "RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionAvailability",
    "RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionWorkingHour",
    "RentalAssetAvailabilitySessionListScheduleList",
    "RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionPrice",
    "RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionAvailability",
    "RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionWorkingHour",
]


class RentalAsset(Dto):
    """The rental asset body, under ``rental_asset``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/rental_assets",
        "GET /api/{api_version}/rental_assets/{rental_asset_uuid}",
        "POST /api/{api_version}/rental_assets",
        "PATCH /api/{api_version}/rental_assets/{rental_asset_uuid}",
        "POST /api/{api_version}/rental_assets/{rental_asset_id}/cancel",
        "POST /api/{api_version}/rental_assets/{rental_asset_id}/reactivate",
    )

    ENVELOPE_KEY = "rental_asset"

    activity_logs: list[Any] | None = None
    code: str | None = None
    created_by: RentalAssetCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: list[Any] | None = None
    custom_form: RentalAssetCustomForm | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    image_name: Any = None
    # Null in every record measured, so untyped.
    item: Any = None
    last_updated_by: RentalAssetLastUpdatedBy | None = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    rental_asset_availability: list[Any] | None = None
    rental_asset_custom_availability: list[RentalAssetRentalAssetCustomAvailability] | None = None
    rental_asset_profile: RentalAssetRentalAssetProfile | None = None
    status: str | None = None
    use_custom_availability: bool | None = None
    version: int | None = None


class RentalAssetList(Dto):
    """One page of ``RentalAsset`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/rental_assets",)

    data: list[RentalAsset] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class RentalAssetProfile(Dto):
    """The rental asset profile body."""

    MEASURED_FROM = ("GET /api/{api_version}/rental_asset_profiles",)

    created_by: RentalAssetProfileCreatedBy | None = None
    created_on: str | None = None
    currency: RentalAssetProfileCurrency | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    is_tax_inclusive: bool | None = None
    last_updated_by: RentalAssetProfileLastUpdatedBy | None = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    max_booking_limit: Any = None
    name: str | None = None
    object: str | None = None
    rental_asset_profile_sessions: list[RentalAssetProfileRentalAssetProfileSession] | None = None
    rental_assets: list[RentalAssetProfileRow] | None = None
    status: str | None = None
    # Null in every record measured, so untyped.
    tax: Any = None
    version: int | None = None


class RentalAssetProfileList(Dto):
    """One page of ``RentalAssetProfile`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/rental_asset_profiles",)

    data: list[RentalAssetProfile] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class RentalAssetAvailability(Dto):
    """The rental asset availability body."""

    MEASURED_FROM = ("GET /api/{api_version}/rental_asset_availability",)

    available_list: list[Any] | None = None
    code: str | None = None
    display_name: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    processed_schedule_list: dict[str, Any] | None = None
    rental_asset_profile: RentalAssetAvailabilityRentalAssetProfile | None = None
    schedule_list: list[RentalAssetAvailabilityScheduleList] | None = None
    session_list: list[RentalAssetAvailabilitySessionList] | None = None
    status: str | None = None
    unavailable_list: list[Any] | None = None
    use_custom_availability: bool | None = None
    version: int | None = None


class RentalAssetAvailabilityList(Dto):
    """One page of ``RentalAssetAvailability`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/rental_asset_availability",)

    data: list[RentalAssetAvailability] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class RentalAssetProfileView(Dto):
    """What ``get_rental_asset_profile`` answers, under ``rental_asset_profile``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/rental_asset_profiles/{rental_asset_profile_id}",
        "POST /api/{api_version}/rental_asset_profiles",
    )

    ENVELOPE_KEY = "rental_asset_profile"

    activity_logs: list[Any] | None = None
    created_by: RentalAssetProfileViewCreatedBy | None = None
    created_on: str | None = None
    currency: RentalAssetProfileViewCurrency | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    is_tax_inclusive: bool | None = None
    last_updated_by: RentalAssetProfileViewLastUpdatedBy | None = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    max_booking_limit: Any = None
    name: str | None = None
    object: str | None = None
    rental_asset_profile_sessions: list[RentalAssetProfileViewRentalAssetProfileSession] | None = (
        None
    )
    rental_assets: list[RentalAssetProfileViewRow] | None = None
    status: str | None = None
    # Null in every record measured, so untyped.
    tax: Any = None
    version: int | None = None


class RentalAssetProfileViewCurrency(Dto):
    """A :class:`RentalAssetProfileView`'s ``currency``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RentalAssetProfileViewRow(Dto):
    """One entry of a :class:`RentalAssetProfileView`'s ``rental_assets``."""

    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    image_name: Any = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    use_custom_availability: bool | None = None


class RentalAssetProfileViewRentalAssetProfileSession(Dto):
    """One entry of a :class:`RentalAssetProfileView`'s ``rental_asset_profile_sessions``."""

    end_date: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rental_asset_profile_session_availability: (
        list[RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionAvailability]
        | None
    ) = None
    rental_asset_profile_session_prices: (
        list[RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionPrice] | None
    ) = None
    rental_asset_profile_session_working_hours: (
        list[RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionWorkingHour]
        | None
    ) = None
    start_date: str | None = None
    status: str | None = None


class RentalAssetProfileViewCreatedBy(Dto):
    """A :class:`RentalAssetProfileView`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class RentalAssetProfileViewLastUpdatedBy(Dto):
    """A :class:`RentalAssetProfileView`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class RentalAssetRentalAssetProfile(Dto):
    """A :class:`RentalAsset`'s ``rental_asset_profile``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RentalAssetCustomForm(Dto):
    """A :class:`RentalAsset`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RentalAssetRentalAssetCustomAvailability(Dto):
    """One entry of a :class:`RentalAsset`'s ``rental_asset_custom_availability``."""

    available: bool | None = None
    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None
    status: str | None = None


class RentalAssetCreatedBy(Dto):
    """A :class:`RentalAsset`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class RentalAssetLastUpdatedBy(Dto):
    """A :class:`RentalAsset`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class RentalAssetAvailabilityRentalAssetProfile(Dto):
    """A :class:`RentalAssetAvailability`'s ``rental_asset_profile``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RentalAssetAvailabilitySessionList(Dto):
    """One entry of a :class:`RentalAssetAvailability`'s ``session_list``."""

    end_date: str | None = None
    name: str | None = None
    processed_schedule_list: dict[str, Any] | None = None
    schedule_list: list[RentalAssetAvailabilitySessionListScheduleList] | None = None
    start_date: str | None = None
    uuid: str | None = None


class RentalAssetAvailabilityScheduleList(Dto):
    """One entry of a :class:`RentalAssetAvailability`'s ``schedule_list``."""

    available: str | None = None
    end_time: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None
    uuid: str | None = None


class RentalAssetProfileCurrency(Dto):
    """A :class:`RentalAssetProfile`'s ``currency``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RentalAssetProfileRow(Dto):
    """One entry of a :class:`RentalAssetProfile`'s ``rental_assets``."""

    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    image_name: Any = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    use_custom_availability: bool | None = None


class RentalAssetProfileRentalAssetProfileSession(Dto):
    """One entry of a :class:`RentalAssetProfile`'s ``rental_asset_profile_sessions``."""

    end_date: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    rental_asset_profile_session_availability: (
        list[RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionAvailability]
        | None
    ) = None
    rental_asset_profile_session_prices: (
        list[RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionPrice] | None
    ) = None
    rental_asset_profile_session_working_hours: (
        list[RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionWorkingHour] | None
    ) = None
    start_date: str | None = None
    status: str | None = None


class RentalAssetProfileCreatedBy(Dto):
    """A :class:`RentalAssetProfile`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class RentalAssetProfileLastUpdatedBy(Dto):
    """A :class:`RentalAssetProfile`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionPrice(Dto):
    """One entry of a :class:`RentalAssetProfileViewRentalAssetProfileSession`'s
    ``rental_asset_profile_session_prices``."""

    id: str | None = None
    is_enabled_pro_rata: bool | None = None
    object: str | None = None
    price: float | None = None
    price_type: str | None = None
    # Null in every record measured, so untyped.
    pricing_level: Any = None
    rental_asset_profile_session_price_hours: list[Any] | None = None
    rental_asset_profile_session_price_peak_hourly: list[Any] | None = None
    status: str | None = None


class RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionAvailability(Dto):
    """One entry of a :class:`RentalAssetProfileViewRentalAssetProfileSession`'s
    ``rental_asset_profile_session_availability``."""

    available: bool | None = None
    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None
    status: str | None = None


class RentalAssetProfileViewRentalAssetProfileSessionRentalAssetProfileSessionWorkingHour(Dto):
    """One entry of a :class:`RentalAssetProfileViewRentalAssetProfileSession`'s
    ``rental_asset_profile_session_working_hours``."""

    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    start_time: str | None = None
    status: str | None = None


class RentalAssetAvailabilitySessionListScheduleList(Dto):
    """One entry of a :class:`RentalAssetAvailabilitySessionList`'s ``schedule_list``."""

    available: str | None = None
    end_time: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None
    uuid: str | None = None


class RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionPrice(Dto):
    """One entry of a :class:`RentalAssetProfileRentalAssetProfileSession`'s
    ``rental_asset_profile_session_prices``."""

    id: str | None = None
    is_enabled_pro_rata: bool | None = None
    object: str | None = None
    price: float | None = None
    price_type: str | None = None
    # Null in every record measured, so untyped.
    pricing_level: Any = None
    rental_asset_profile_session_price_hours: list[Any] | None = None
    rental_asset_profile_session_price_peak_hourly: list[Any] | None = None
    status: str | None = None


class RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionAvailability(Dto):
    """One entry of a :class:`RentalAssetProfileRentalAssetProfileSession`'s
    ``rental_asset_profile_session_availability``."""

    available: bool | None = None
    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    preferred_day: str | None = None
    start_time: str | None = None
    status: str | None = None


class RentalAssetProfileRentalAssetProfileSessionRentalAssetProfileSessionWorkingHour(Dto):
    """One entry of a :class:`RentalAssetProfileRentalAssetProfileSession`'s
    ``rental_asset_profile_session_working_hours``."""

    end_time: str | None = None
    id: str | None = None
    object: str | None = None
    start_time: str | None = None
    status: str | None = None
