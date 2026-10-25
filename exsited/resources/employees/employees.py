"""Employee endpoints, under ``/api/{api_version}/employees``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.employees import employees_urls
from exsited.resources.employees.employees_dto import Employee, EmployeeList

__all__ = [
    "get_employees",
    "create_employee",
    "delete_employee",
    "get_employee",
    "update_employee",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

EmployeePayload = Mapping[str, Any] | str | Dto


def get_employees(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[EmployeeList]:
    """List employees - ``GET /employees``."""
    return client.send_get_request(
        employees_urls.EMPLOYEES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=EmployeeList,
    )


def create_employee(
    client: Any,
    payload: EmployeePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Employee]:
    """Create employee - ``POST /employees``."""
    _require_payload(payload)
    return client.send_post_request(
        employees_urls.EMPLOYEES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Employee,
    )


def delete_employee(
    client: Any,
    employee_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete employee - ``DELETE /employees/{employee_id}``."""
    return client.send_delete_request(
        employees_urls.EMPLOYEE,
        path_params={"employee_id": employee_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_employee(
    client: Any,
    employee_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Employee]:
    """Get employee - ``GET /employees/{employee_id}``."""
    return client.send_get_request(
        employees_urls.EMPLOYEE,
        path_params={"employee_id": employee_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Employee,
    )


def update_employee(
    client: Any,
    employee_id: str,
    payload: EmployeePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Employee]:
    """Update employee - ``PATCH /employees/{employee_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        employees_urls.EMPLOYEE,
        path_params={"employee_id": employee_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Employee,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
