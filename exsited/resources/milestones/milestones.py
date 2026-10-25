"""Milestone endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.milestones import milestones_urls
from exsited.resources.milestones.milestones_dto import Milestones

__all__ = [
    "get_milestones",
    "get_milestones_account_by_id",
    "get_milestones_labour_by_id",
    "get_milestones_employee_by_code",
    "get_milestone",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_milestones(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Milestones]:
    """List all milestones - ``GET /milestones``."""
    return client.send_get_request(
        milestones_urls.MILESTONES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Milestones,
    )


def get_milestones_account_by_id(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Milestones]:
    """Get milestones by account - ``GET /milestones/account/{account_id}``."""
    return client.send_get_request(
        milestones_urls.MILESTONES_ACCOUNT_BY_ID,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Milestones,
    )


def get_milestones_labour_by_id(
    client: Any,
    labour_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Milestones]:
    """Get milestones by labour - ``GET /milestones/labour/{labour_id}``."""
    return client.send_get_request(
        milestones_urls.MILESTONES_LABOUR_BY_ID,
        path_params={"labour_id": labour_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Milestones,
    )


def get_milestones_employee_by_code(
    client: Any,
    employee_code: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Milestones]:
    """Get milestones by employee - ``GET /milestones/employee/{employee_code}``; the employee's
    ``code``, since an ``emp_`` id answers ``404``."""
    return client.send_get_request(
        milestones_urls.MILESTONES_EMPLOYEE_BY_CODE,
        path_params={"employee_code": employee_code},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Milestones,
    )


def get_milestone(
    client: Any,
    milestone_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get one milestone - ``GET /milestones/{milestone_uuid}``, a ``wfm_`` id or its raw uuid; a
    workflow's milestone definition is a different record and answers ``404``."""
    return client.send_get_request(
        milestones_urls.MILESTONE,
        path_params={"milestone_uuid": milestone_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )
