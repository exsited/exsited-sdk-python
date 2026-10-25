"""Typed views over the custom feature bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "CustomFeatureList",
    "CustomFeature",
    "CustomFeatureDetail",
    "CustomFeatureDetailCustomForm",
    "CustomFeatureDetailCustomFormConfiguration",
    "CustomFeatureDetailCustomFormConfigurationColumn1",
    "CustomFeatureDetailCustomFormConfigurationColumn2",
    "CustomFeatureDetailCustomFormConfigurationSettings",
    "CustomFeatureDetailCustomFormConfigurationColumn1Attribute",
    "CustomFeatureDetailCustomFormConfigurationColumn2Attribute",
]


class CustomFeatureList(Dto):
    """One page of what ``get_custom_features`` lists, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/custom_feature",)

    data: list[CustomFeatureDetail] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class CustomFeature(Dto):
    """The custom feature body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/custom_feature/{custom_feature_id}",
        "POST /api/{api_version}/custom_feature",
        "PATCH /api/{api_version}/custom_feature/{custom_feature_id}",
        "POST /api/{api_version}/custom_feature/{custom_feature_id}",
    )

    custom_feature: CustomFeatureDetail | None = None
    message: str | None = None


class CustomFeatureDetail(Dto):
    """A :class:`CustomFeature`'s ``custom_feature``."""

    activity_logs: list[Any] | None = None
    child_custom_components: list[Any] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    custom_component: Any = None
    custom_forms: list[CustomFeatureDetailCustomForm] | None = None
    custom_objects: list[Any] | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    relation: str | None = None
    status: str | None = None
    use_in: str | None = None
    version: int | None = None


class CustomFeatureDetailCustomForm(Dto):
    """One entry of a :class:`CustomFeatureDetail`'s ``custom_forms``."""

    configuration: CustomFeatureDetailCustomFormConfiguration | None = None


class CustomFeatureDetailCustomFormConfiguration(Dto):
    """A :class:`CustomFeatureDetailCustomForm`'s ``configuration``."""

    column_1: CustomFeatureDetailCustomFormConfigurationColumn1 | None = None
    column_2: CustomFeatureDetailCustomFormConfigurationColumn2 | None = None
    settings: CustomFeatureDetailCustomFormConfigurationSettings | None = None


class CustomFeatureDetailCustomFormConfigurationColumn1(Dto):
    """A :class:`CustomFeatureDetailCustomFormConfiguration`'s ``column_1``."""

    attributes: list[CustomFeatureDetailCustomFormConfigurationColumn1Attribute] | None = None


class CustomFeatureDetailCustomFormConfigurationColumn2(Dto):
    """A :class:`CustomFeatureDetailCustomFormConfiguration`'s ``column_2``."""

    attributes: list[CustomFeatureDetailCustomFormConfigurationColumn2Attribute] | None = None


class CustomFeatureDetailCustomFormConfigurationSettings(Dto):
    """A :class:`CustomFeatureDetailCustomFormConfiguration`'s ``settings``."""

    custom_form: str | None = None
    form_layout: str | None = None


class CustomFeatureDetailCustomFormConfigurationColumn1Attribute(Dto):
    """One entry of a :class:`CustomFeatureDetailCustomFormConfigurationColumn1`'s
    ``attributes``."""

    data_type: str | None = None
    display_name: str | None = None
    name: str | None = None
    show_in_list_view: bool | None = None
    type: str | None = None


class CustomFeatureDetailCustomFormConfigurationColumn2Attribute(Dto):
    """One entry of a :class:`CustomFeatureDetailCustomFormConfigurationColumn2`'s
    ``attributes``."""

    name: str | None = None
    type: str | None = None
