"""Typed views over the employee bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Employee",
    "EmployeeList",
    "EmployeeCustomForm",
    "EmployeeContact",
    "EmployeeCreatedBy",
    "EmployeeLastUpdatedBy",
    "EmployeeContactName",
    "EmployeeContactEmail",
    "EmployeeContactCreatedBy",
]


class Employee(Dto):
    """The employee body, under ``employee``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/employees",
        "GET /api/{api_version}/employees/{employee_id}",
        "POST /api/{api_version}/employees",
        "PATCH /api/{api_version}/employees/{employee_id}",
    )

    ENVELOPE_KEY = "employee"

    activity_logs: list[Any] | None = None
    code: str | None = None
    contacts: list[EmployeeContact] | None = None
    created_by: EmployeeCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: list[Any] | None = None
    custom_form: EmployeeCustomForm | None = None
    description: str | None = None
    display_name: str | None = None
    email_address: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    image_uuid: Any = None
    last_updated_by: EmployeeLastUpdatedBy | None = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class EmployeeList(Dto):
    """One page of ``Employee`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/employees",)

    data: list[Employee] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class EmployeeCustomForm(Dto):
    """A :class:`Employee`'s ``custom_form``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class EmployeeContact(Dto):
    """One entry of a :class:`Employee`'s ``contacts``."""

    # Null in every record measured, so untyped.
    address: Any = None
    created_by: EmployeeContactCreatedBy | None = None
    created_on: str | None = None
    email: EmployeeContactEmail | None = None
    # Null in every record measured, so untyped.
    fax: Any = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    # Null in every record measured, so untyped.
    mobile: Any = None
    name: EmployeeContactName | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    phone: Any = None
    status: str | None = None
    type: str | None = None
    version: int | None = None


class EmployeeCreatedBy(Dto):
    """A :class:`Employee`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class EmployeeLastUpdatedBy(Dto):
    """A :class:`Employee`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class EmployeeContactName(Dto):
    """A :class:`EmployeeContact`'s ``name``."""

    # Null in every record measured, so untyped.
    designation: Any = None
    first: str | None = None
    last: str | None = None
    # Null in every record measured, so untyped.
    middle: Any = None
    # Null in every record measured, so untyped.
    salutation: Any = None


class EmployeeContactEmail(Dto):
    """A :class:`EmployeeContact`'s ``email``."""

    address: str | None = None
    email_opted_out: bool | None = None


class EmployeeContactCreatedBy(Dto):
    """A :class:`EmployeeContact`'s ``created_by``."""

    name: str | None = None
    object: str | None = None
