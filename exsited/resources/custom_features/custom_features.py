"""Custom feature endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.custom_features import custom_features_urls
from exsited.resources.custom_features.custom_features_dto import (
    CustomFeature,
    CustomFeatureList,
)

__all__ = [
    "get_custom_features",
    "get_custom_feature_by_id",
    "create_custom_feature",
    "delete_custom_feature_by_id",
    "update_custom_feature_by_id",
    "create_custom_feature_by_id",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

CustomFeaturePayload = Mapping[str, Any] | str | Dto


def get_custom_features(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomFeatureList]:
    """List custom features - ``GET /custom_feature``, cursor paged, the active ones only."""
    return client.send_get_request(
        custom_features_urls.CUSTOM_FEATURE,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomFeatureList,
    )


def get_custom_feature_by_id(
    client: Any,
    custom_feature_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomFeature]:
    """Retrieve custom feature - ``GET /custom_feature/{custom_feature_id}``, the ``cmp_`` id,
    under ``custom_feature``; a deleted one is ``404``."""
    return client.send_get_request(
        custom_features_urls.CUSTOM_FEATURE_BY_ID,
        path_params={"custom_feature_id": custom_feature_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomFeature,
    )


def create_custom_feature(
    client: Any,
    payload: CustomFeaturePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomFeature]:
    """Create custom feature - ``POST /custom_feature``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        custom_features_urls.CUSTOM_FEATURE,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomFeature,
    )


def delete_custom_feature_by_id(
    client: Any,
    custom_feature_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete custom feature - ``DELETE /custom_feature/{custom_feature_id}``, the ``cmp_`` id;
    answered ``204``."""
    return client.send_delete_request(
        custom_features_urls.CUSTOM_FEATURE_BY_ID,
        path_params={"custom_feature_id": custom_feature_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_custom_feature_by_id(
    client: Any,
    custom_feature_id: str,
    payload: CustomFeaturePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomFeature]:
    """Update custom feature - ``PATCH /custom_feature/{custom_feature_id}``; answered ``202``."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_features_urls.CUSTOM_FEATURE_BY_ID,
        path_params={"custom_feature_id": custom_feature_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomFeature,
    )


def create_custom_feature_by_id(
    client: Any,
    custom_feature_id: str,
    payload: CustomFeaturePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[CustomFeature]:
    """Customize form layout and attributes - ``POST /custom_feature/{custom_feature_id}``; answered
    ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        custom_features_urls.CUSTOM_FEATURE_BY_ID,
        path_params={"custom_feature_id": custom_feature_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=CustomFeature,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
