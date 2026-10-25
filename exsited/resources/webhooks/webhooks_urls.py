"""Path templates and body keys for the webhook endpoints."""

from __future__ import annotations

#: v4 serves no webhook listing: ``GET /webhooks`` without an id is refused.
WEBHOOK = "/api/{api_version}/webhooks/{webhook_id}"

#: The envelope one record arrives under.
WEBHOOK_KEY = "webhook"
