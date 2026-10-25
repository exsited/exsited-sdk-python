"""Typed views over the organisation bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto

__all__ = [
    "SettingsOrganisation",
    "SettingsOrganisationParentOrganization",
]


class SettingsOrganisation(Dto):
    """The root organisation body, under ``organization``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/organisation",)

    ENVELOPE_KEY = "organization"

    # Null in every record measured, so untyped.
    address_line1: Any = None
    # Null in every record measured, so untyped.
    address_line2: Any = None
    # Null in every record measured, so untyped.
    address_line3: Any = None
    # Null in every record measured, so untyped.
    address_line4: Any = None
    # Null in every record measured, so untyped.
    address_line5: Any = None
    # Null in every record measured, so untyped.
    city: Any = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    # Null in every record measured, so untyped.
    details: Any = None
    display_name: str | None = None
    # Null in every record measured, so untyped.
    email: Any = None
    # Null in every record measured, so untyped.
    fax: Any = None
    # Null in every record measured, so untyped.
    fax_area_code: Any = None
    # Null in every record measured, so untyped.
    fax_country_code: Any = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    mobile: Any = None
    # Null in every record measured, so untyped.
    mobile_area_code: Any = None
    # Null in every record measured, so untyped.
    mobile_country_code: Any = None
    name: str | None = None
    # Empty in every record measured, so untyped.
    nodes: list[Any] | None = None
    object: str | None = None
    parent_organization: SettingsOrganisationParentOrganization | None = None
    # Null in every record measured, so untyped.
    phone: Any = None
    # Null in every record measured, so untyped.
    phone_area_code: Any = None
    # Null in every record measured, so untyped.
    phone_country_code: Any = None
    # Null in every record measured, so untyped.
    post_code: Any = None
    # Null in every record measured, so untyped.
    state: Any = None
    status: str | None = None
    type: str | None = None
    # Null in every record measured, so untyped.
    website: Any = None


class SettingsOrganisationParentOrganization(Dto):
    """A :class:`SettingsOrganisation`'s ``parent_organization``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
