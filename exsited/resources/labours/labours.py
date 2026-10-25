"""Labour endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.labours import labours_urls
from exsited.resources.labours.labours_dto import (
    Labour,
    LabourAvailabilityList,
    LabourCalendar,
    LabourList,
    LabourOrderList,
    LabourProfileList,
    LabourProfileSessionList,
    LabourProfileSessionView,
    LabourProfileView,
)

__all__ = [
    "get_labour_availability",
    "get_labour_profiles",
    "create_labour_profile",
    "get_labours",
    "create_labour",
    "get_labour_profile",
    "update_labour_profile",
    "delete_labour_profile",
    "get_labours_available_for_booking",
    "update_labour",
    "delete_labour",
    "get_labour",
    "cancel_labour",
    "reactivate_labour",
    "get_labour_orders",
    "update_labour_availability",
    "get_labour_profile_sessions",
    "get_labour_profile_session",
    "get_labour_calendar",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

LabourPayload = Mapping[str, Any] | str | Dto


def get_labour_availability(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourAvailabilityList]:
    """Labour availability - ``GET /labour_availability``."""
    return client.send_get_request(
        labours_urls.LABOUR_AVAILABILITY,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourAvailabilityList,
    )


def get_labour_profiles(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourProfileList]:
    """List labour profiles - ``GET /labour_profiles``."""
    return client.send_get_request(
        labours_urls.LABOUR_PROFILES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourProfileList,
    )


def create_labour_profile(
    client: Any,
    payload: LabourPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourProfileView]:
    """Create labour profile - ``POST /labour_profiles``."""
    _require_payload(payload)
    return client.send_post_request(
        labours_urls.LABOUR_PROFILES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourProfileView,
    )


def get_labours(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourList]:
    """List labours - ``GET /labours``."""
    return client.send_get_request(
        labours_urls.LABOURS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourList,
    )


def create_labour(
    client: Any,
    payload: LabourPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Labour]:
    """Create labour - ``POST /labours``."""
    _require_payload(payload)
    return client.send_post_request(
        labours_urls.LABOURS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Labour,
    )


def get_labour_profile(
    client: Any,
    labour_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourProfileView]:
    """Get labour profile - ``GET /labour_profiles/{labour_profile_id}``."""
    return client.send_get_request(
        labours_urls.LABOUR_PROFILE,
        path_params={"labour_profile_id": labour_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourProfileView,
    )


def update_labour_profile(
    client: Any,
    labour_profile_id: str,
    payload: LabourPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update labour profile - ``PATCH /labour_profiles/{labour_profile_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        labours_urls.LABOUR_PROFILE,
        path_params={"labour_profile_id": labour_profile_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_labour_profile(
    client: Any,
    labour_profile_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete labour profile - ``DELETE /labour_profiles/{labour_profile_id}``."""
    return client.send_delete_request(
        labours_urls.LABOUR_PROFILE,
        path_params={"labour_profile_id": labour_profile_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_labours_available_for_booking(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourList]:
    """Available labours - ``GET /labours/available_for_booking``."""
    return client.send_get_request(
        labours_urls.LABOURS_AVAILABLE_FOR_BOOKING,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourList,
    )


def update_labour(
    client: Any,
    labour_uuid: str,
    payload: LabourPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Labour]:
    """Update labour - ``PATCH /labours/{labour_uuid}``."""
    _require_payload(payload)
    return client.send_patch_request(
        labours_urls.LABOUR,
        path_params={"labour_uuid": labour_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Labour,
    )


def delete_labour(
    client: Any,
    labour_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete labour - ``DELETE /labours/{labour_uuid}``."""
    return client.send_delete_request(
        labours_urls.LABOUR,
        path_params={"labour_uuid": labour_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_labour(
    client: Any,
    labour_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Labour]:
    """Get labour - ``GET /labours/{labour_uuid}``."""
    return client.send_get_request(
        labours_urls.LABOUR,
        path_params={"labour_uuid": labour_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Labour,
    )


def cancel_labour(
    client: Any,
    labour_id: str,
    payload: LabourPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Labour]:
    """Cancel labour - ``POST /labours/{labour_id}/cancel``."""
    _require_payload(payload)
    return client.send_post_request(
        labours_urls.LABOUR_CANCEL,
        path_params={"labour_id": labour_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Labour,
    )


def reactivate_labour(
    client: Any,
    labour_id: str,
    payload: LabourPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Labour]:
    """Reactivate labour - ``POST /labours/{labour_id}/reactivate``."""
    _require_payload(payload)
    return client.send_post_request(
        labours_urls.LABOUR_REACTIVATE,
        path_params={"labour_id": labour_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Labour,
    )


def get_labour_orders(
    client: Any,
    labour_uuid: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourOrderList]:
    """Get labour orders - ``GET /labours/{labour_uuid}/orders``."""
    return client.send_get_request(
        labours_urls.LABOUR_ORDERS,
        path_params={"labour_uuid": labour_uuid},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourOrderList,
    )


def update_labour_availability(
    client: Any,
    payload: LabourPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Edit availability slots in bulk - ``PATCH /labour_availability``; the body is
    ``{"labours": [{"id", "labour_availability", "labour_custom_availability"}]}``, ``204``."""
    _require_payload(payload)
    return client.send_patch_request(
        labours_urls.LABOUR_AVAILABILITY,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_labour_profile_sessions(
    client: Any,
    labour_profile_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourProfileSessionList]:
    """List a labour profile's sessions - ``GET /labour_profiles/{labour_profile_id}/sessions``."""
    return client.send_get_request(
        labours_urls.LABOUR_PROFILE_SESSIONS,
        path_params={"labour_profile_id": labour_profile_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourProfileSessionList,
    )


def get_labour_profile_session(
    client: Any,
    labour_profile_id: str,
    session_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourProfileSessionView]:
    """Get one labour profile session -
    ``GET /labour_profiles/{labour_profile_id}/sessions/{session_id}``."""
    return client.send_get_request(
        labours_urls.LABOUR_PROFILE_SESSION,
        path_params={"labour_profile_id": labour_profile_id, "session_id": session_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourProfileSessionView,
    )


def get_labour_calendar(
    client: Any,
    labour_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[LabourCalendar]:
    """One labour's availability calendar - ``GET /labours/{labour_id}/availability``, under
    ``labour_calendar``; the id or the code."""
    return client.send_get_request(
        labours_urls.LABOUR_CALENDAR,
        path_params={"labour_id": labour_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=LabourCalendar,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
