"""Typed views over the custom attribute bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "CustomAttribute",
    "CustomAttributeList",
    "CustomAttributes",
    "CustomAttributeOption",
    "CustomAttributeUseIn",
    "CustomAttributesOption",
    "CustomAttributesUseIn",
    "CustomAttributesActivityLog",
]


class CustomAttribute(Dto):
    """The custom attribute body, under ``custom_attribute``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/custom_attributes",
        "GET /api/{api_version}/custom_attributes/{custom_attribute_id}",
        "PATCH /api/{api_version}/custom_attributes/{custom_attribute_id}",
    )

    ENVELOPE_KEY = "custom_attribute"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    encrypt_data: bool | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    include_seconds: Any = None
    is_mandatory: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    max_length: int | None = None
    # Null in every record measured, so untyped.
    max_size: Any = None
    # Null in every record measured, so untyped.
    max_value: Any = None
    # Null in every record measured, so untyped.
    meta_data: Any = None
    # Null in every record measured, so untyped.
    min_value: Any = None
    name: str | None = None
    object: str | None = None
    options: list[CustomAttributeOption] | None = None
    status: str | None = None
    # Null in every record measured, so untyped.
    time_format: Any = None
    type: str | None = None
    # Null in every record measured, so untyped.
    unit: Any = None
    # Null in every record measured, so untyped.
    uom: Any = None
    use_in: list[CustomAttributeUseIn] | None = None
    version: int | None = None


class CustomAttributeList(Dto):
    """One page of ``CustomAttribute`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/custom_attributes",)

    data: list[CustomAttribute] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class CustomAttributes(Dto):
    """The custom attributes body, under ``custom_attribute``."""

    MEASURED_FROM = ("POST /api/{api_version}/custom_attributes",)

    ENVELOPE_KEY = "custom_attribute"

    activity_logs: list[CustomAttributesActivityLog] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    encrypt_data: bool | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    include_seconds: Any = None
    is_mandatory: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    max_length: int | None = None
    # Null in every record measured, so untyped.
    max_size: Any = None
    # Null in every record measured, so untyped.
    max_value: Any = None
    meta_data: str | None = None
    # Null in every record measured, so untyped.
    min_value: Any = None
    name: str | None = None
    object: str | None = None
    options: list[CustomAttributesOption] | None = None
    status: str | None = None
    # Null in every record measured, so untyped.
    time_format: Any = None
    type: str | None = None
    # Null in every record measured, so untyped.
    unit: Any = None
    # Null in every record measured, so untyped.
    uom: Any = None
    use_in: list[CustomAttributesUseIn] | None = None
    uuid: str | None = None
    version: int | None = None


class CustomAttributeOption(Dto):
    """One entry of a :class:`CustomAttribute`'s ``options``."""

    display_order: int | None = None
    name: str | None = None


class CustomAttributeUseIn(Dto):
    """One entry of a :class:`CustomAttribute`'s ``use_in``."""

    associated_account_groups: list[Any] | None = None
    associated_item_groups: list[Any] | None = None
    associated_user_groups: list[Any] | None = None
    enabled: bool | None = None
    required: bool | None = None
    resource: str | None = None
    unique: bool | None = None


class CustomAttributesOption(Dto):
    """One entry of a :class:`CustomAttributes`'s ``options``."""

    display_order: int | None = None
    name: str | None = None


class CustomAttributesUseIn(Dto):
    """One entry of a :class:`CustomAttributes`'s ``use_in``."""

    associated_account_groups: list[Any] | None = None
    associated_item_groups: list[Any] | None = None
    associated_user_groups: list[Any] | None = None
    enabled: bool | None = None
    required: bool | None = None
    resource: str | None = None
    unique: bool | None = None


class CustomAttributesActivityLog(Dto):
    """One entry of a :class:`CustomAttributes`'s ``activity_logs``."""

    activity: str | None = None
