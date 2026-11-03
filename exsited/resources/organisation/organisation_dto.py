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


    ENVELOPE_KEY = "organization"

    address_line1: Any = None
    address_line2: Any = None
    address_line3: Any = None
    address_line4: Any = None
    address_line5: Any = None
    city: Any = None
    created_by: Any = None
    created_on: str | None = None
    description: Any = None
    details: Any = None
    display_name: str | None = None
    email: Any = None
    fax: Any = None
    fax_area_code: Any = None
    fax_country_code: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    mobile: Any = None
    mobile_area_code: Any = None
    mobile_country_code: Any = None
    name: str | None = None
    nodes: list[Any] | None = None
    object: str | None = None
    parent_organization: SettingsOrganisationParentOrganization | None = None
    phone: Any = None
    phone_area_code: Any = None
    phone_country_code: Any = None
    post_code: Any = None
    state: Any = None
    status: str | None = None
    type: str | None = None
    website: Any = None


class SettingsOrganisationParentOrganization(Dto):
    """A :class:`SettingsOrganisation`'s ``parent_organization``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
