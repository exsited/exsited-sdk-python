"""Reaching an endpoint module as ``client.<resource>``: an explicit registry of name to module
path, so a typo raises, and :class:`BoundResource`, which applies the client to each function."""

from __future__ import annotations

import difflib
import functools
import importlib.util
import keyword
from importlib import import_module
from typing import Any

from exsited.errors import SdkAttributeError, SdkUsageError

__all__ = [
    "BoundResource",
    "register_resource_module",
    "resolve_resource_module",
    "registered_resource_names",
]

#: Named after the SDK family, not the path: several v4 families share a path segment.
_RESOURCE_MODULES: dict[str, str] = {
    "aba_files": "exsited.resources.aba_files.aba_files",
    "account_emails": "exsited.resources.account_emails.account_emails",
    "account_groups": "exsited.resources.account_groups.account_groups",
    "accounting_codes": "exsited.resources.accounting_codes.accounting_codes",
    "accounts": "exsited.resources.accounts.accounts",
    "action_scripts": "exsited.resources.action_scripts.action_scripts",
    "additional_codes": "exsited.resources.additional_codes.additional_codes",
    "alert_responsibilities": "exsited.resources.alert_responsibilities.alert_responsibilities",
    "alert_responsibility": "exsited.resources.alert_responsibility.alert_responsibility",
    "alerts": "exsited.resources.alerts.alerts",
    "applications": "exsited.resources.applications.applications",
    "approval_profiles": "exsited.resources.approval_profiles.approval_profiles",
    "approval_user_groups": "exsited.resources.approval_user_groups.approval_user_groups",
    "approvals": "exsited.resources.approvals.approvals",
    "attribute_attachments": "exsited.resources.attribute_attachments.attribute_attachments",
    "billing_periods": "exsited.resources.billing_periods.billing_periods",
    "bookings": "exsited.resources.bookings.bookings",
    "charging_periods": "exsited.resources.charging_periods.charging_periods",
    "communication_profiles": "exsited.resources.communication_profiles.communication_profiles",
    "communications": "exsited.resources.communications.communications",
    "countries": "exsited.resources.countries.countries",
    "credit_note_applications": "exsited.resources.credit_note_applications.credit_note_applications",
    "credit_notes": "exsited.resources.credit_notes.credit_notes",
    "custom_attributes": "exsited.resources.custom_attributes.custom_attributes",
    "custom_components": "exsited.resources.custom_components.custom_components",
    "custom_events": "exsited.resources.custom_events.custom_events",
    "custom_features": "exsited.resources.custom_features.custom_features",
    "custom_fields": "exsited.resources.custom_fields.custom_fields",
    "custom_forms": "exsited.resources.custom_forms.custom_forms",
    "day_of_month": "exsited.resources.day_of_month.day_of_month",
    "departments": "exsited.resources.departments.departments",
    "designations": "exsited.resources.designations.designations",
    "document_templates": "exsited.resources.document_templates.document_templates",
    "email_templates": "exsited.resources.email_templates.email_templates",
    "employees": "exsited.resources.employees.employees",
    "events": "exsited.resources.events.events",
    "express": "exsited.resources.express.express",
    "external_databases": "exsited.resources.external_databases.external_databases",
    "fulfillment_profiles": "exsited.resources.fulfillment_profiles.fulfillment_profiles",
    "fulfillment_terms": "exsited.resources.fulfillment_terms.fulfillment_terms",
    "gift_certificates": "exsited.resources.gift_certificates.gift_certificates",
    "integration_connections": "exsited.resources.integration_connections.integration_connections",
    "inventory_adjustments": "exsited.resources.inventory_adjustments.inventory_adjustments",
    "invoice_terms": "exsited.resources.invoice_terms.invoice_terms",
    "invoices": "exsited.resources.invoices.invoices",
    "item_fulfillments": "exsited.resources.item_fulfillments.item_fulfillments",
    "item_receipts": "exsited.resources.item_receipts.item_receipts",
    "items": "exsited.resources.items.items",
    "labours": "exsited.resources.labours.labours",
    "milestones": "exsited.resources.milestones.milestones",
    "note_attachments": "exsited.resources.note_attachments.note_attachments",
    "note_groups": "exsited.resources.note_groups.note_groups",
    "orders": "exsited.resources.orders.orders",
    "organisation": "exsited.resources.organisation.organisation",
    "organisations": "exsited.resources.organisations.organisations",
    "payments": "exsited.resources.payments.payments",
    "portals": "exsited.resources.portals.portals",
    "pricing_periods": "exsited.resources.pricing_periods.pricing_periods",
    "proforma_invoices": "exsited.resources.proforma_invoices.proforma_invoices",
    "purchase_credit_note_applications": "exsited.resources.purchase_credit_note_applications"
    ".purchase_credit_note_applications",
    "purchase_credit_notes": "exsited.resources.purchase_credit_notes.purchase_credit_notes",
    "purchase_express": "exsited.resources.purchase_express.purchase_express",
    "purchase_invoices": "exsited.resources.purchase_invoices.purchase_invoices",
    "purchase_orders": "exsited.resources.purchase_orders.purchase_orders",
    "purchase_payments": "exsited.resources.purchase_payments.purchase_payments",
    "purchase_refunds": "exsited.resources.purchase_refunds.purchase_refunds",
    "quote_orders": "exsited.resources.quote_orders.quote_orders",
    "receive_terms": "exsited.resources.receive_terms.receive_terms",
    "reconciliations": "exsited.resources.reconciliations.reconciliations",
    "refunds": "exsited.resources.refunds.refunds",
    "rental_assets": "exsited.resources.rental_assets.rental_assets",
    "reports": "exsited.resources.reports.reports",
    "return_merchandise_authorisations": "exsited.resources.return_merchandise_authorisations"
    ".return_merchandise_authorisations",
    "return_vendor_authorizations": "exsited.resources.return_vendor_authorizations"
    ".return_vendor_authorizations",
    "roles": "exsited.resources.roles.roles",
    "sales_reps": "exsited.resources.sales_reps.sales_reps",
    "salutations": "exsited.resources.salutations.salutations",
    "settings": "exsited.resources.settings.settings",
    "settings_workflows": "exsited.resources.settings_workflows.settings_workflows",
    "shipping_packages": "exsited.resources.shipping_packages.shipping_packages",
    "shipping_rules": "exsited.resources.shipping_rules.shipping_rules",
    "system_events": "exsited.resources.system_events.system_events",
    "tasks": "exsited.resources.tasks.tasks",
    "teams": "exsited.resources.teams.teams",
    "time_periods": "exsited.resources.time_periods.time_periods",
    "timesheets": "exsited.resources.timesheets.timesheets",
    "uom": "exsited.resources.uom.uom",
    "usages": "exsited.resources.usages.usages",
    "webhooks": "exsited.resources.webhooks.webhooks",
    "workflows": "exsited.resources.workflows.workflows",
    "zones": "exsited.resources.zones.zones",
}


def register_resource_module(resource_name: str, module_path: str) -> None:
    """Make a resource module reachable as ``client.<resource_name>``, from its importable path
    as a string; an unreachable name or a clashing re-registration raises ``SdkUsageError``."""
    if (
        not isinstance(resource_name, str)
        or resource_name.startswith("_")
        or not resource_name.isidentifier()
        or keyword.iskeyword(resource_name)
    ):
        # An underscore or non-identifier name could never be reached as an attribute.
        raise SdkUsageError(
            f"cannot register resource {resource_name!r}: a resource name must be "
            "a Python identifier that is not a keyword and does not start with an "
            "underscore, or no lookup could ever reach it - pick another name"
        )
    if resource_name in _client_attribute_names():
        # ``__getattr__`` runs only when lookup fails, so a real attribute would always win.
        raise SdkUsageError(
            f"cannot register resource {resource_name!r}: ExsitedClient "
            "already has an attribute of that name, and it would win every "
            "lookup - pick another name"
        )
    registered = _RESOURCE_MODULES.get(resource_name)
    if registered is not None and registered != module_path:
        # A client built before a rebind keeps its namespace: one name, two modules.
        raise SdkUsageError(
            f"cannot register resource {resource_name!r} against {module_path!r}: "
            f"it is already registered against {registered!r}, and clients built "
            f"before the change would keep the old one - pick another name"
        )
    if not _module_exists(module_path):
        # Refused now: ``ModuleNotFoundError`` escapes both ``except SdkError`` and ``hasattr``.
        raise SdkUsageError(
            f"cannot register resource {resource_name!r}: nothing importable at "
            f"{module_path!r} - check the module path"
        )
    _RESOURCE_MODULES[resource_name] = module_path


def _module_exists(module_path: str) -> bool:
    """Whether ``module_path`` names something importable; ``find_spec`` needs the guard
    because it *raises* when a parent package is missing."""
    try:
        return importlib.util.find_spec(module_path) is not None
    except (ImportError, AttributeError, ValueError, TypeError):
        return False


def _client_attribute_names() -> frozenset[str]:
    """Every attribute name :class:`ExsitedClient` already answers by itself; the
    import is deferred, since at module scope it would cycle."""
    from exsited.client.exsited_client import ExsitedClient

    return frozenset(dir(ExsitedClient))


def registered_resource_names() -> tuple[str, ...]:
    """Every registered resource name, sorted - those reachable on a client."""
    return tuple(sorted(_RESOURCE_MODULES))


def resolve_resource_module(resource_name: str) -> Any:
    """Import the module registered under a resource name; an unknown one raises
    :class:`~exsited.errors.SdkAttributeError`, an ``AttributeError``, so ``hasattr`` works."""
    module_path = _RESOURCE_MODULES.get(resource_name)
    if module_path is None:
        available = ", ".join(registered_resource_names()) or "none registered yet"
        raise SdkAttributeError(f"no resource {resource_name!r}; available: {available}")
    try:
        return import_module(module_path)
    except ImportError as error:
        # ``ImportError`` only: a ``SyntaxError`` is a real bug, not a missing name.
        raise SdkAttributeError(
            f"resource {resource_name!r} could not be imported from {module_path!r}",
            detail=str(error),
            cause=error,
        ) from None


class BoundResource:
    """A resource module with the client pre-applied as each function's first argument."""

    def __init__(self, client: Any, module: Any) -> None:
        self._client = client
        self._module = module

    def __getattr__(self, name: str) -> Any:
        """Bind one endpoint function with the client already applied, or say what this
        module offers, with a ``difflib`` suggestion when the name is close."""
        if name.startswith("_"):
            # Before the resolver: ``copy`` asks a half-built instance for ``__setstate__``.
            raise AttributeError(name)
        available = self._public_function_names()
        if name not in available:
            suggestion = difflib.get_close_matches(name, available, n=1)
            hint = f"; did you mean {suggestion[0]}?" if suggestion else ""
            raise SdkAttributeError(
                f"{self._module.__name__.rsplit('.', 1)[-1]} has no {name!r}{hint}"
            )
        target = getattr(self._module, name, None)
        if not callable(target):
            # ``partial`` on a non-callable raises ``TypeError``, which ``hasattr`` does not catch.
            raise SdkAttributeError(
                f"{self._module.__name__.rsplit('.', 1)[-1]} lists {name!r} in "
                f"__all__ but it is "
                f"{'not defined' if target is None else 'not callable'}, so it is "
                f"not an endpoint"
            )
        return functools.partial(target, self._client)

    def __deepcopy__(self, memo: dict[int, Any]) -> "BoundResource":
        """Copy the façade, sharing the client and the module - without this
        ``copy.deepcopy`` dies on the ``RLock`` inside the client's logger."""
        clone = BoundResource(self._client, self._module)
        memo[id(self)] = clone
        return clone

    def _public_function_names(self) -> list[str]:
        """The endpoint names, read from ``__all__`` so imported names are not offered."""
        declared = getattr(self._module, "__all__", None)
        if isinstance(declared, (list, tuple, set, frozenset)):
            return sorted(str(entry) for entry in declared)
        # A bare string is a forgotten list, read as no declaration rather than as characters.
        return sorted(
            attribute
            for attribute in dir(self._module)
            if not attribute.startswith("_") and callable(getattr(self._module, attribute))
        )

    def __dir__(self) -> list[str]:
        return self._public_function_names()
