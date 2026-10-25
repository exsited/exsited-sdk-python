"""Path templates and body keys for the attribute attachment endpoints."""

from __future__ import annotations

#: Singular on the wire; the account views link a file attribute here.
ATTRIBUTE_ATTACHMENT = "/api/{api_version}/attribute_attachment/{file_uuid}"
