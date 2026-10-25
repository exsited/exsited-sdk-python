"""Path templates and body keys for the alert responsibility endpoints."""

from __future__ import annotations

#: Singular on the wire, and served by the workflow services over the same records as
#: ``/settings/alert_responsibilities``; the answers' own ``href`` values say
#: ``/alert_responsibilities``, which v4 does not serve at the top level.
ALERT_RESPONSIBILITIES = "/api/{api_version}/alert_responsibility"
ALERT_RESPONSIBILITY = "/api/{api_version}/alert_responsibility/{alert_responsibility_id}"

#: The key a listing's records sit under.
ALERT_RESPONSIBILITIES_KEY = "data"

#: The envelope one record arrives under.
ALERT_RESPONSIBILITY_KEY = "alert_responsibility"
