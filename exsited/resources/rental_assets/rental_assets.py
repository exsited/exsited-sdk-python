"""Rental asset endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.rental_assets import rental_assets_urls
from exsited.resources.rental_assets.rental_assets_dto import (
    RentalAsset,
    RentalAssetAvailabilityList,
    RentalAssetList,
    RentalAssetProfileList,
    RentalAssetProfileView,
)

__all__ = [
    "get_rental_asset_availability",
    "update_rental_asset_availability",
    "get_rental_asset_profiles",
    "create_rental_asset_profile",
    "get_rental_assets",
    "create_rental_asset",
    "get_rental_asset_profile",
    "update_rental_asset_profile",
    "delete_rental_asset_profile",
    "update_rental_asset",
    "delete_rental_asset",
    "get_rental_asset",
    "cancel_rental_asset",
    "reactivate_rental_asset",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

RentalAssetPayload = Mapping[str, Any] | str | Dto


def get_rental_asset_availability(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAssetAvailabilityList]:
    """Rental asset availability - ``GET /rental_asset_availability``."""
    return client.send_get_request(
        rental_assets_urls.RENTAL_ASSET_AVAILABILITY,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAssetAvailabilityList,
    )


def update_rental_asset_availability(
    client: Any,
    payload: RentalAssetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update rental asset availability - ``PATCH /rental_asset_availability``."""
    _require_payload(payload)
    return client.send_patch_request(
        rental_assets_urls.RENTAL_ASSET_AVAILABILITY,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_rental_asset_profiles(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAssetProfileList]:
    """List rental asset profiles - ``GET /rental_asset_profiles``."""
    return client.send_get_request(
        rental_assets_urls.RENTAL_ASSET_PROFILES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAssetProfileList,
    )


def create_rental_asset_profile(
    client: Any,
    payload: RentalAssetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAssetProfileView]:
    """Create rental asset profile - ``POST /rental_asset_profiles``."""
    _require_payload(payload)
    return client.send_post_request(
        rental_assets_urls.RENTAL_ASSET_PROFILES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAssetProfileView,
    )


def get_rental_assets(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAssetList]:
    """List rental assets - ``GET /rental_assets``."""
    return client.send_get_request(
        rental_assets_urls.RENTAL_ASSETS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAssetList,
    )


def create_rental_asset(
    client: Any,
    payload: RentalAssetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAsset]:
    """Create rental asset - ``POST /rental_assets``."""
    _require_payload(payload)
    return client.send_post_request(
        rental_assets_urls.RENTAL_ASSETS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAsset,
    )


def get_rental_asset_profile(
    client: Any,
    rental_asset_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAssetProfileView]:
    """Get rental asset profile - ``GET /rental_asset_profiles/{rental_asset_profile_id}``."""
    return client.send_get_request(
        rental_assets_urls.RENTAL_ASSET_PROFILE,
        path_params={"rental_asset_profile_id": rental_asset_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAssetProfileView,
    )


def update_rental_asset_profile(
    client: Any,
    rental_asset_profile_id: str,
    payload: RentalAssetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update rental asset profile - ``PATCH /rental_asset_profiles/{rental_asset_profile_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        rental_assets_urls.RENTAL_ASSET_PROFILE,
        path_params={"rental_asset_profile_id": rental_asset_profile_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_rental_asset_profile(
    client: Any,
    rental_asset_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete rental asset profile - ``DELETE /rental_asset_profiles/{rental_asset_profile_id}``."""
    return client.send_delete_request(
        rental_assets_urls.RENTAL_ASSET_PROFILE,
        path_params={"rental_asset_profile_id": rental_asset_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_rental_asset(
    client: Any,
    rental_asset_uuid: str,
    payload: RentalAssetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAsset]:
    """Update rental asset - ``PATCH /rental_assets/{rental_asset_uuid}``."""
    _require_payload(payload)
    return client.send_patch_request(
        rental_assets_urls.RENTAL_ASSET,
        path_params={"rental_asset_uuid": rental_asset_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAsset,
    )


def delete_rental_asset(
    client: Any,
    rental_asset_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete rental asset - ``DELETE /rental_assets/{rental_asset_uuid}``."""
    return client.send_delete_request(
        rental_assets_urls.RENTAL_ASSET,
        path_params={"rental_asset_uuid": rental_asset_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_rental_asset(
    client: Any,
    rental_asset_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAsset]:
    """Get rental asset - ``GET /rental_assets/{rental_asset_uuid}``."""
    return client.send_get_request(
        rental_assets_urls.RENTAL_ASSET,
        path_params={"rental_asset_uuid": rental_asset_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAsset,
    )


def cancel_rental_asset(
    client: Any,
    rental_asset_id: str,
    payload: RentalAssetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAsset]:
    """Cancel rental asset - ``POST /rental_assets/{rental_asset_id}/cancel``."""
    _require_payload(payload)
    return client.send_post_request(
        rental_assets_urls.RENTAL_ASSET_CANCEL,
        path_params={"rental_asset_id": rental_asset_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAsset,
    )


def reactivate_rental_asset(
    client: Any,
    rental_asset_id: str,
    payload: RentalAssetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[RentalAsset]:
    """Reactivate rental asset - ``POST /rental_assets/{rental_asset_id}/reactivate``."""
    _require_payload(payload)
    return client.send_post_request(
        rental_assets_urls.RENTAL_ASSET_REACTIVATE,
        path_params={"rental_asset_id": rental_asset_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=RentalAsset,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
