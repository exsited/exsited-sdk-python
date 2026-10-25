"""Timesheet endpoints, under ``/api/{api_version}/timesheets``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.timesheets import timesheets_urls
from exsited.resources.timesheets.timesheets_dto import TimesheetList, Timesheets, TimesheetUpdated

__all__ = [
    "get_timesheets",
    "create_timesheet",
    "delete_timesheet",
    "update_timesheet",
    "get_timesheet",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

TimesheetPayload = Mapping[str, Any] | str | Dto


def get_timesheets(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TimesheetList]:
    """List all timesheets - ``GET /timesheets``."""
    return client.send_get_request(
        timesheets_urls.TIMESHEETS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TimesheetList,
    )


def create_timesheet(
    client: Any,
    payload: TimesheetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Timesheets]:
    """Create timesheet - ``POST /timesheets``."""
    _require_payload(payload)
    return client.send_post_request(
        timesheets_urls.TIMESHEETS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Timesheets,
    )


def delete_timesheet(
    client: Any,
    created_timesheet_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete timesheet - ``DELETE /timesheets/{timesheet_id}``."""
    return client.send_delete_request(
        timesheets_urls.TIMESHEET,
        path_params={"timesheet_id": created_timesheet_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_timesheet(
    client: Any,
    created_timesheet_id: str,
    payload: TimesheetPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[TimesheetUpdated]:
    """Update timesheet - ``PATCH /timesheets/{timesheet_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        timesheets_urls.TIMESHEET,
        path_params={"timesheet_id": created_timesheet_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=TimesheetUpdated,
    )


def get_timesheet(
    client: Any,
    timesheet_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Timesheets]:
    """Get one timesheet - ``GET /timesheets/{timesheet_id}``, by the ``ts_`` id the listing and
    the create answer."""
    return client.send_get_request(
        timesheets_urls.TIMESHEET,
        path_params={"timesheet_id": timesheet_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Timesheets,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
