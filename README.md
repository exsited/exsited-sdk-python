# Exsited Python SDK

The Python SDK for the Exsited v4 REST API. Every endpoint is a function,
`client.<family>.<function>(...)`: you send a JSON request body and get the JSON
response body back. Authentication, token refresh, pagination, retries and error
handling are done for you.

- **Request body:** a dict or a JSON string, sent as JSON. A typed DTO is
  optional and sends the same JSON.
- **Response body:** JSON by default. `response.data` and `response.map` are the
  decoded JSON (a dict or a list), and `response.json` is the JSON text exactly as
  it arrived. A typed view, `response.dto`, is there if you want it; set
  `response_format="json"` or `"dto"` only to change what `.data` holds.
- **Field names are the API's own.** Nothing is renamed, case-converted or
  reshaped in either direction.

```python
from exsited import ExsitedClient, SdkConfig

with ExsitedClient(SdkConfig(auth)) as client:  # auth: see Credentials
    response = client.accounts.cancel_account(
        "W13ZGY", {"account": {"effective_date": "2026-08-31"}}
    )
    print(response.data)  # the decoded JSON body
```

## Contents

- [Install](#install)
- [Credentials](#credentials)
- [Configuration](#configuration)
- [Multiple instances](#multiple-instances)
- [First call](#first-call)
- [Requests](#requests)
  - [Request headers](#request-headers)
- [Filtering and sorting](#filtering-and-sorting)
- [Pagination](#pagination)
- [Payload forms](#payload-forms)
- [Responses](#responses)
  - [Choosing the form](#choosing-the-form)
  - [Typed views](#typed-views)
- [Errors](#errors)
- [Idempotency](#idempotency)
- [Authentication and the token cache](#authentication-and-the-token-cache)
  - [The token cache file](#the-token-cache-file)
- [Diagnostics](#diagnostics)
  - [Secrets and personal data](#secrets-and-personal-data)
- [Retries](#retries)
- [Transport](#transport)
- [Endpoints](#endpoints)
- [Troubleshooting](#troubleshooting)
- [Public API](#public-api)

## Install

The distribution and the import are both `exsited`. Pin the major version:

```bash
pip install "exsited>=4,<5"
python -c "import exsited"
```

Requires Python 3.10 or later.

## Credentials

Pass the credentials in yourself. The SDK does not read them from the
environment.

```python
from exsited import AuthConfig

auth = AuthConfig(
    client_name="default",
    base_url="https://dev-api.exsited.com",
    client_id="...",
    client_secret="...",
    redirect_uri="https://dev.exsited.com/",
)
```

`client_name` is required and names the instance in logs and printed output.
`base_url`, `client_id`, `client_secret` and `redirect_uri` are the four values the
token endpoint takes.

`AuthConfig` is frozen and validated at construction. `repr` and `str` redact
`client_secret`, so an instance is safe to log. Every problem is reported in one
error:

```
SdkConfigError: instance default: missing required values: client_secret, redirect_uri
```

## Configuration

`AuthConfig` holds credentials. `SdkConfig` holds behaviour, passed as keywords.
Every setting has a default:

```python
from exsited import SdkConfig

config = SdkConfig(auth, print_api_info=True, max_retries=3, log_level="DEBUG")
```

| Setting | Default | Notes |
|---|---|---|
| `api_version` | `"v4"` | Fills `{api_version}` in every data path. Accepts `4` or `"v4"` |
| `timeout_seconds` | `30.0` | Read timeout, and the limit on receiving the whole response body. Each retry gets a fresh limit |
| `connect_timeout_seconds` | `10.0` | Time allowed to establish the connection |
| `max_retries` | `1` | Total attempts, including the first. `1` disables retry |
| `retryable_http_codes` | `(429, 500, 502, 503, 504)` | Statuses that are retried. Has no effect while `max_retries` is `1` |
| `unsafe_retryable_http_codes` | `()` | Statuses that may also retry a method other than `GET`, `HEAD`, `OPTIONS` or `TRACE`. Empty, so no write is retried on a status |
| `retry_backoff_seconds` | `0.5` | Base for exponential backoff with full jitter |
| `retry_backoff_max_seconds` | `20.0` | Longest single wait, including a server's `Retry-After` |
| `verify_ssl` | `True` | `False` logs a `WARNING` and issues an `InsecureTransportWarning` |
| `ca_bundle` | `None` | Path to a PEM bundle. Cannot be combined with `verify_ssl=False`. A missing file, or one over 8 MiB, fails at construction |
| `proxy_url` | `None` | Used for `http` and `https` |
| `pool_maxsize` | `10` | Connections kept for reuse. Not a concurrency limit |
| `max_response_bytes` | `67108864` (64 MiB) | Largest response body the SDK reads. A larger body raises |
| `max_upload_bytes` | `67108864` (64 MiB) | Largest request body: JSON, form, upload or multipart, framing included |
| `default_headers` | `()` | A dict, a JSON object string, or `(name, value)` pairs, sent on every request. Checked at construction. A `Content-Type` must be a media type |
| `raise_on_error` | `False` | `False` returns a failure as a response. `True` raises `SdkError` |
| `response_format` | `"map"` | What `.data` holds: `"map"`, `"json"` or `"dto"`. See [Choosing the form](#choosing-the-form) |
| `user_agent` | `exsited-python-sdk/<version>` | |
| `log_level` | `"WARNING"` | `DEBUG`, `INFO`, `WARNING`, `ERROR` or `CRITICAL`, applied to the logger `exsited.<client_name>` |
| `log_bodies` | `False` | Adds the payload and response, redacted, to `DEBUG` records |
| `log_file` | `None` | File that log records are written to |
| `print_api_info` | `False` | Prints client, method, endpoint, params, status, attempt and elapsed time |
| `print_request_payload` | `False` | Prints the payload, redacted |
| `print_response_body` | `False` | Prints the response body. A binary body is summarised |
| `print_headers` | `False` | Prints the headers, redacted |
| `print_curl` | `False` | Prints a `curl` command with the token redacted |
| `print_only_on_error` | `False` | Prints only for failed calls |
| `print_format` | `"pretty"` | Or `"compact"`, one line per call |
| `print_color` | `False` | Ignored when stdout is not a TTY |
| `print_max_chars` | `0` | Truncates printed output. `0` means unlimited |

Configs are frozen. `config.with_overrides(...)` returns a new config and leaves
the original unchanged. A path given as an `os.PathLike` (`ca_bundle`, `log_file`,
`token_cache_path`) is converted to text at construction. As with `AuthConfig`,
every problem is reported in one error. A value that names something, such as a
missing `ca_bundle` path, is on the error's `.detail` rather than in its message.

## Multiple instances

Register every instance once. The first one is the default.

```python
from exsited import build_client, register_instances

register_instances([production_auth, staging_auth])   # AuthConfig objects

build_client()                                        # production
build_client(instance=1)                              # by position
build_client(instance="staging")                      # by client_name
build_client(instance="staging", print_api_info=True) # with SdkConfig overrides
```

Each client has its own config, session, token provider and token store, so two
instances never share a token. An instance is only authenticated when a client for
it makes a call. Duplicate `client_name`s are rejected at registration.

To keep several clients open and reuse them, use a `ClientRegistry`:

```python
from exsited import ClientRegistry

with ClientRegistry([production_auth, staging_auth]) as registry:
    registry.get_client("production").accounts.get_accounts()
    registry.get_client("staging").accounts.get_accounts()
```

`get_client` builds a client on first use and returns the same one afterwards,
whether you select it by name or by position. Leaving the `with` block calls
`close_all_clients()`.

A closed client stays closed. After `close_client()`, the end of a `with` block, or
`close_all_clients()`, its next call raises `SdkUsageError`. Closing twice does
nothing.

## First call

```python
from exsited import ExsitedClient, SdkConfig

with ExsitedClient(SdkConfig(auth)) as client:
    response = client.accounts.get_accounts({"limit": 50})
    for account in response.data["data"]:
        print(account["id"], account["name"])
```

Use `with`, or call `client.close_client()` yourself. A client that is never closed
releases its connections only when it is garbage collected.

## Requests

Every endpoint function takes the client first, so you can call it either way:

```python
from exsited.resources.accounts.accounts import get_account

get_account(client, "W13ZGY")             # explicit
client.accounts.get_account("W13ZGY")     # bound
client.items.get_item("ITEM-0001")
client.invoices.get_invoice("INV-0001")
```

For a path with no endpoint function, use the general methods:
`send_get_request`, `send_post_request`, `send_put_request`, `send_patch_request`,
`send_delete_request`, and `send_api_request(http_method, path, ...)`. They take
`path_params`, `query_params`, `json_body`, `form_data`, `files`, `headers`,
`raise_on_error` and `response_format` as keywords.

```python
from exsited.resources.accounts import accounts_urls

client.send_get_request(accounts_urls.ACCOUNT, path_params={"account_id": "W13ZGY"})
client.send_api_request("GET", "/api/{api_version}/accounts", query_params={"limit": 5})
```

Paths are templates such as `"/api/{api_version}/accounts/{account_id}"`.
`{api_version}` is filled from `config.api_version`. The other placeholders come
from `path_params` and are percent-encoded. A missing or unknown path parameter
fails before any request is sent:

```
SdkUsageError: /api/{api_version}/accounts/{account_id} -> missing path params: account_id; unknown path params: id
```

The SDK checks the method, path, headers, payload shape and query values before
any network I/O, so a mistake is reported at the line that made it.

### Request headers

Header names and values are checked against RFC 9110, in `default_headers`, in the
per-call `headers` argument, and in multipart part headers. The check runs before
the token request, so a header that cannot be sent costs no authentication.

- A **name** may contain letters, digits and `` !#$%&'*+-.^_`|~ ``. A space, a
  colon, a control character or a non-ASCII character is refused.
- A **value** may be empty. Otherwise it may contain visible ASCII characters,
  spaces and tabs, and must not start or end with a space or a tab. NUL, DEL, other
  control characters, newlines and any character at or above `0x80` are refused.

A refused header raises `SdkUsageError`. The error names the header and the
character position, never the value, which may be a credential.

```python
path = accounts_urls.ACCOUNTS

client.send_get_request(path, headers={"X-Note": "a\tb"})     # sent
client.send_get_request(path, headers={"X-Note": "café"})     # SdkUsageError
client.send_get_request(path, headers={"X-Note": "a\x00b"})   # SdkUsageError
```

A header value has no charset on the wire, so encode a non-ASCII value yourself.
A trailing newline is also refused, which catches a key read from a file without
stripping it. The SDK adds one header of its own to a `POST`; see
[Idempotency](#idempotency).

## Filtering and sorting

Names are snake_case in query parameters and bodies alike. `limit`, `cursor` and
`sort` control a listing. Every other parameter is a filter, named
`filter_<field>` for equality and `filter_<field>_<operator>` otherwise. Build the
names with the helpers:

```python
from exsited import SortDirection, filter_param, filter_values, sort_param

client.accounts.get_accounts({
    "limit": 50,
    "sort": sort_param("created_on", SortDirection.DESC),        # "-created_on"
    filter_param("status"): "ACTIVE",                            # filter_status
    filter_param("created_on", "gte"): "2026-04-01",             # filter_created_on_gte
    filter_param("email_address", "contains"): "@acme.com",
})
```

Operators: `eq` (the default), `neq`, `in`, `nin`, `contains`, `not_contains`,
`starts_with`, `gt`, `gte`, `lt`, `lte`, `has_value` and `does_not_have_value`. An
unknown operator raises `SdkUsageError`. An unknown field is a `400` from the API.

- `in` and `nin` take one comma-separated value. Build it with `filter_values`,
  as in `filter_values(["ACTIVE", "INACTIVE"])`. It refuses a member that contains
  a comma, a `None` member, a set and an empty list.
- `has_value` and `does_not_have_value` take no value. Pair them with `True`.

Query values are converted for the wire; names are sent as written. `True` becomes
`"true"`, `None` is dropped so an unset filter is not sent, a `date` or `datetime`
becomes ISO 8601, and a list repeats the key. A nested mapping, a list inside a
list and a set are refused.

## Pagination

v4 listings page in one of two shapes. The records are under `data` in both.

Cursor:

```json
{"object": "list", "data": [...],
 "pagination": {"limit": 5, "has_more": true, "next_cursor": "XCY2e7Cn..."}}
```

Offset:

```json
{"object": "list", "data": [...],
 "pagination": {"records": 296, "limit": 20, "offset": 0,
                "previous_page": "NULL", "next_page": "..."}}
```

`iter_records` and `iter_pages` read the shape from each page, so the same call
walks either kind:

```python
from exsited import iter_pages, iter_records
from exsited.resources.accounts import accounts_urls
from exsited.resources.invoices import invoices_urls

for account in iter_records(client, accounts_urls.ACCOUNTS,
                            query_params={"limit": 100, "filter_status": "ACTIVE"}):
    print(account["id"])

for invoice in iter_records(client, invoices_urls.INVOICES, query_params={"limit": 100}):
    print(invoice["id"])

for page in iter_pages(client, accounts_urls.ACCOUNTS, max_pages=5):
    print(page.status_code, len(page.map["data"]))
```

- Both are generators. Nothing is fetched until you iterate, and stopping early
  fetches no more pages.
- `query_params` is sent again with every page. Do not include `cursor` or
  `offset`: the walk sets them, and passing one raises `SdkUsageError`. To resume
  from a saved cursor, call `send_get_request` with it.
- `record_key` defaults to `"data"`. If the first page has no list under that
  key, `iter_records` raises `SdkUsageError` naming the keys the page does have.
- `has_more: false` ends a cursor walk even if a `next_cursor` is present. An
  offset walk ends when `next_page` is the string `"NULL"` (not JSON `null`), and
  the next offset is computed from `offset` and `limit` rather than taken from the
  `next_page` link.
- A repeated cursor or offset raises `SdkError` instead of looping.
- `iter_records` raises on a failed page. `iter_pages` does too by default; with
  `raise_on_error=False` it yields the failed page and stops.

## Payload forms

A write function takes a payload in any of three forms, and all three send the
same bytes:

```python
from exsited.resources.accounts.accounts_dto import AccountCancel

client.accounts.cancel_account("W13ZGY", {"account": {"effective_date": "2026-08-31"}})
client.accounts.cancel_account("W13ZGY", '{"account": {"effective_date": "2026-08-31"}}')
client.accounts.cancel_account("W13ZGY", AccountCancel(effective_date="2026-08-31"))
```

- A **mapping** is encoded as JSON by the SDK.
- A **JSON string** is sent byte for byte. It is parsed only to check it, so a
  body copied from Postman keeps its spacing, key order and escaping. Invalid JSON,
  or JSON that is a bare scalar, is refused before the request is sent.
- A **DTO** is turned into its mapping and sent the same way. A field left as
  `None` is omitted, not sent as `null`. To send a field the DTO does not declare,
  use a mapping.

## Responses

Every call returns an `ApiResponse`. Three members always read the body the same
way, whatever the configuration says:

```python
response.map      # the decoded body
response.json     # the body text as the API sent it
response.dto      # the typed view
response.data     # follows response_format; .map by default
```

So one codebase can mix the forms:

```python
response.map["data"][0]["email_address"]
response.json                              # '{\n  "object": "list",\n  "data": [...'
response.dto.data[0].currency.code
```

`.json` is the text that arrived, not a re-serialisation, so you can compare it
with a body seen in Postman. For a binary body, such as a note attachment, `.json`
is `None` and `.map` holds the bytes. `.dto` has the type the endpoint declares:
`get_accounts` gives an `AccountList`, `get_account` an `Account`,
`get_account_note` a `NoteView`. A delete, and a call through a general `send_*`
method, declare no type, so `.dto` is `None`. `.json` and `.dto` are built on
first access.

| Member | Meaning |
|---|---|
| `.data` | The form chosen by `response_format`; the decoded body by default |
| `.map`, `.json`, `.dto` | Always available, whatever the configuration says |
| `.status_code` | The HTTP status |
| `.succeeded` | A 2xx status and a body that is not an error envelope |
| `.content_type` | The `Content-Type` header |
| `.headers` | The response headers |
| `.error_type` | An `ErrorType` derived from the status |
| `.error_code`, `.request_id`, `.doc_url` | From the v4 error envelope |
| `.get_error_messages()` | The reported problems as text |
| `.get_field_errors()` | The same problems, structured |
| `.raise_for_status()` | Raises if the call failed, otherwise returns the response |
| `.request_info` | A redacted record of the request |

Every v4 body names itself with an `object` key, such as `"account"`, `"list"` or
`"note"`, and an error body is `"error"`. A 2xx response whose body is
`{"object": "error", ...}` is therefore not `.succeeded`.

### Choosing the form

`response_format` is resolved in this order, highest first:

```python
client.accounts.get_accounts(response_format="dto")     # 1. the call
SdkConfig(auth, response_format="json")                 # 2. the config
# 3. the environment variable EXSITED_RESPONSE_FORMAT=dto
# 4. the default, "map"
```

The environment variable is read once, when the config is built, and the result is
on `client.config.response_format`. An unknown value is refused: from the
environment or the config it raises `SdkConfigError` at construction, and at a
call site it raises `SdkUsageError` before the request is sent.

### Typed views

Each family's views live in `exsited.resources.<family>.<family>_dto`, for example
`exsited.resources.accounts.accounts_dto`. All of them subclass `Dto`.

- A view's fields are its annotations. The field name is the wire name.
- A view converts nothing. A value that does not match the declared type reads as
  `None`: a `version` sent as `"3"` does not become `3`. The only widening is a
  JSON integer read into a `float` field.

When a typed field reads `None` and you expected a value, check `.map`. It holds
the value as it arrived and is the only way to tell a missing key from one sent as
`null`.

Some listing views declare their records as `list[Any]`. For those,
`response.dto.data` holds plain dicts, the same as `.map["data"]`. Check with
`type(response.dto.data[0])`.

## Errors

By default a failed call returns a response instead of raising, so you can read
the error body. Change this per call or in the config:

```python
response = client.accounts.get_account("NOPE")                        # returns
response = client.accounts.get_account("NOPE", raise_on_error=True)   # raises
```

The v4 error envelope is kept whole:

```json
{"object": "error",
 "request_id": "req_23019cc8-cdce-42db-ae8f-b3fdb1e15493",
 "status": 400, "code": "validation_error",
 "message": "One or more fields failed validation",
 "doc_url": "https://developer.exsited.com/...",
 "errors": [{"field": "effective_date", "code": "invalid",
             "message": "Invalid format for effective_date",
             "doc_url": "..."}]}
```

```python
response.error_code          # 'validation_error', the value to branch on
response.request_id          # 'req_23019cc8-...', the value to quote to support
response.get_error_messages()
# ['effective_date: Invalid format for effective_date']
response.get_field_errors()
# [{'field': 'effective_date', 'code': 'invalid', 'message': '...', 'doc_url': '...'}]
```

`error_type` comes from the HTTP status. `error_code` is the API's own
classification. They can differ: a `DELETE` on a locked account answers `409`
(`ErrorType.CONFLICT`) with the code `internal_error`.

Exceptions:

| Exception | Raised for |
|---|---|
| `SdkError` | The base class. A failed call, or a 2xx whose body is an error envelope |
| `SdkAuthError` | A `401` or `403`, or a failed token request |
| `SdkUsageError` | A caller mistake, caught before any network I/O |
| `SdkConfigError` | Invalid configuration, at construction |
| `SdkAttributeError` | An unknown resource name. Also an `AttributeError`, so `hasattr` returns `False` |
| `SdkTokenCacheError`, `SdkTokenLockError` | The token cache file or its lock |

Every raised error carries `status_code`, `error_type`, `error_code`,
`request_id`, `doc_url`, `field_errors`, `raw_response`, `response_headers`,
`request_info`, `detail` and `cause`.

An exception's `.message` is the SDK's own summary, such as
`the API answered 404, 1 problem(s) reported`, or for a 2xx error envelope
`the API answered 200 but its body is an error envelope (object: error)`. The
API's own text is on `.get_error_messages()`. `.raw_response` is a redacted copy
of the body. On a failed call `response.dto` is `None`, because the body is the
error envelope and not the declared record.

A failure that produces no response, such as a connection failure, a timeout or
rejected credentials, always raises, whatever `raise_on_error` says.

## Idempotency

Every `POST` carries an `X-Idempotency-Key` header, so a repeated request does not
create a second record. The key is generated once per call, so a retry and the
replay after a `401` send the same key. `PUT`, `PATCH` and `DELETE` get no key.

To resume a create whose response never arrived, pass your own key. A key you set,
in any capitalisation, is left as it is:

```python
from exsited.resources.accounts import accounts_urls

saved_key = "..."   # the key sent with the first attempt

client.send_post_request(accounts_urls.ACCOUNT_CANCEL,
                         path_params={"account_id": "W13ZGY"},
                         json_body={"account": {"effective_date": "2026-08-31"}},
                         headers={"X-Idempotency-Key": saved_key})
```

## Authentication and the token cache

The SDK authenticates with OAuth2 `client_credentials` against
`/api/v4/oauth2/token`. It fetches a token on first use and refreshes it shortly
before it expires, using the `refresh_token` grant and falling back to a full
`client_credentials` request.

If a call gets a `401` because the token is stale, the SDK refreshes the token
once and replays the call. A `401` that rejects the request itself, rather than
the token, is not replayed.

### The token cache file

By default the SDK writes the access token and the refresh token to a file on
first use.

| | |
|---|---|
| What is written | The access token, the refresh token, an expiry time and a skew |
| Where | `%LOCALAPPDATA%\exsited\exsited_python_token.json` on Windows, `~/Library/Caches/exsited/exsited_python_token.json` on macOS, `$XDG_CACHE_HOME/exsited/exsited_python_token.json` or `~/.cache/exsited/exsited_python_token.json` elsewhere |
| When | On the first call that needs a token, and on every refresh |
| Keyed by | A SHA-256 fingerprint of `base_url`, `client_id`, `client_secret` and `grant_type`, never the values themselves |
| Turn it off | `AuthConfig(..., token_cache_path=None)` |
| Move it | `AuthConfig(..., token_cache_path="/run/secrets/exsited-token.json")` |

**Security note:** the refresh token outlives the access token, so treat the file
as a long-lived credential. On POSIX the file is created with mode `0600` and its
directory with `0700`. On Windows the SDK does not set or check permissions: the
file inherits the NTFS ACLs of `%LOCALAPPDATA%`. On a shared or roaming profile,
use `token_cache_path=None` or a path only you can read.

With `token_cache_path=None` the token is kept in memory for the life of the
process. The cost is one extra authentication per process.

The file is locked across processes, so concurrent workers share one token.
Entries are keyed by the credential fingerprint, so several instances can share
one file without receiving each other's tokens.

## Diagnostics

```python
config = SdkConfig(auth, print_api_info=True, log_level="DEBUG")
```

Each printed block has its own flag: `print_api_info`, `print_request_payload`,
`print_response_body`, `print_headers` and `print_curl`. `print_only_on_error`,
`print_format`, `print_color` and `print_max_chars` control how they are shown. A
misspelt flag raises `TypeError` in `SdkConfig(...)` and `SdkConfigError` in
`with_overrides(...)`.

All flags are off by default and `log_level` is `WARNING`, so a client with no
diagnostics configured prints nothing. The per-call log record is written at
`INFO`. A send that got no response logs at `ERROR`, and a `401` about to be
replayed logs at `WARNING`. Log lines name the endpoint template, not the record
id.

Printing and logging use the same redactor. `render_exchange` renders a call, and
`build_curl_command` builds a `curl` command with the token masked. For a
multipart upload, the `curl` command carries one `-F` per file and one `--form-string`
per form field.

### Secrets and personal data

The redactor finds a secret by its key name, such as `client_secret`,
`access_token`, `Authorization`, `cardNumber` or `cvv`, and masks the value in
bodies, headers, query strings, `curl` commands and exceptions.

It does not redact personal data. Names, email and postal addresses, phone numbers
and amounts stay as they arrived on `.map`, `.json` and `.dto`. Control where they
appear by choosing what you render:

```python
import logging

from exsited import SdkError, set_error_diagnostics

logger = logging.getLogger(__name__)

try:
    client.accounts.get_account("W13ZGY", raise_on_error=True)
except SdkError as error:
    logger.warning(error.explain())          # structural fields only
    print(error.explain(diagnostics=True))   # adds the data, for your terminal

set_error_diagnostics(True)                  # the same, for the whole process
```

By default `explain()` shows only structural fields: the status, the error
category, the method, the endpoint template, the attempt count, the elapsed time,
the type of any underlying exception, the envelope's `code` and `request_id`, and
a hint. It leaves out the resolved URL, the query values, the API's messages, the
response body, a redirect's `Location`, file paths and the underlying exception's
text, and says how to show them:

```
404 [not_found] GET /api/{api_version}/accounts/{account_id} - the API answered 404, 1 problem(s) reported
  attempt : 1/1
  elapsed : 0.31s
  code    : resource_not_found
  request : req_23019cc8
  hint    : no such record - check the id you passed actually exists
  detail  : withheld - call explain(diagnostics=True), or set EXSITED_ERROR_DIAGNOSTICS=1, for the API's message, the response body, the query values, the resolved URL, the path or origin this failure names and the native cause's own wording
```

Set `EXSITED_ERROR_DIAGNOSTICS=1` to show the full detail for a whole run without
changing code. `set_error_diagnostics(True)` does the same from code and returns
the previous setting.

The SDK's exceptions are not chained to the underlying exception. The original is
on `.cause`, and a value that names something, such as a path or an origin, is on
`.detail`. `str(error)` names the status, the category and the endpoint template,
never the record id. The resolved URL and the full body are on
`error.request_info.url` and `error.raw_response`.

## Retries

Retry is off by default, because `max_retries` counts the first attempt:

```python
SdkConfig(auth, max_retries=3)
```

Waits use exponential backoff with full jitter, capped by
`retry_backoff_max_seconds`. A `Retry-After` header, in seconds or as an HTTP date,
replaces the computed wait but is capped by the same limit: with the default of 20
seconds, a request to wait 120 seconds waits 20. Raise `retry_backoff_max_seconds`
to honour longer waits.

`400` and `401` are not retried. A `401` is handled by the token refresh and
replay described in
[Authentication and the token cache](#authentication-and-the-token-cache).

A status from the API is retried if it is in `retryable_http_codes` and the method
allows it. `GET`, `HEAD`, `OPTIONS` and `TRACE` retry on any code in that list.
Every other method retries only on codes that are also in
`unsafe_retryable_http_codes`, which is empty by default.

A transport failure is retried according to whether the request may have reached
the server:

| Failure | Reached the server? | Retried for |
|---|---|---|
| DNS failure, connect timeout, connection refused, proxy or TLS handshake failure | No | Any method |
| Read timeout, connection reset while waiting for or reading the reply, truncated body | Maybe | `GET`, `HEAD`, `OPTIONS`, `TRACE`, `PUT`, `DELETE` |
| Anything else, such as a malformed URL | Not a delivery failure | Nothing |

So a `POST` that timed out waiting for its reply is not retried, because the
record may have been created. A `POST` that never reached the server is retried
under the same `X-Idempotency-Key`.

The SDK copies the request body before the first attempt, so every attempt sends
the same bytes. A body given as an iterable of chunks cannot be copied, so a
request with one is neither retried nor replayed.

## Transport

Each client has its own `requests.Session`.

- **Response size.** A body larger than `max_response_bytes` is refused. A
  declared `Content-Length` over the limit is refused without reading the body,
  and a chunked body is refused as soon as it passes the limit.
  `timeout_seconds` also limits the time to receive the whole body.
- **Request size.** The whole request body is built in memory before the token
  request, and nothing is streamed. `max_upload_bytes` limits its size, multipart
  framing included. Building the body is limited to `timeout_seconds`.
- **Content-Type.** A `Content-Type` header must be a media type and must match
  the body. With `files`, do not set one: the SDK sets it with the multipart
  boundary.
- **Redirects** are not followed. A `3xx` is returned like any other non-2xx, with
  its `Location` header. A path given as an absolute URL must be on the configured
  origin. A URL with a fragment or user information is refused.
- **TLS.** Use `ca_bundle` rather than `verify_ssl=False`; setting both is an
  error. `verify_ssl=False`, or an `http://` `base_url` that is not on this
  machine, logs a `WARNING` and issues an `InsecureTransportWarning`.
- **Repeated 400.** After a `400`, the server can return the same error to the next
  request on that connection. When a `400` names only parameters the request did
  not send, the SDK drops the pooled connections and sends a `GET`, `HEAD` or
  `OPTIONS` request once more.

## Endpoints

Every endpoint is a function on its family, called as
`client.<family>.<function>(...)`. Each function's docstring names its HTTP
method, path and parameters. `client.list_resource_names()` lists the families.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'exsited'` | Run `pip install "exsited>=4,<5"` in the environment that runs your code |
| `SdkUsageError: no instances registered` | Call `register_instances([...])` first, or pass `credentials=` to `build_client()` |
| `SdkConfigError: ... missing required values: ...` | The values arrived as `None` or blank. Check that your environment or `.env` file is loaded and the names match |
| `SdkConfigError: ... base_url: must start with http:// or https://` | Add the scheme to `base_url` |
| `SdkAuthError` on the first call | The token request to `POST /api/v4/oauth2/token` failed. Check the four credentials, the base URL and TLS |
| The token endpoint answers `404` | The token path is `/api/v4/oauth2/token`. For a deployment that mounts it elsewhere, pass `token_path` to `TokenProvider` |
| `CERTIFICATE_VERIFY_FAILED` | Set `ca_bundle="/path/to/ca.pem"` rather than `verify_ssl=False` |
| `400` naming a parameter you never sent | The server repeated an earlier error on a reused connection. For `GET`, `HEAD` and `OPTIONS` the SDK resends once on a fresh connection |
| `iter_records` raises `SdkUsageError` about `record_key` | The listing keeps its records under another key. Pass one of the keys the error lists as `record_key` |
| `log_level` or `log_file` seems to have no effect | Clients with the same `client_name` share the logger `exsited.<client_name>`. Give each client its own name |
| You need a fresh token | Delete the token file, or set `token_cache_path=None` |

## Public API

Everything below can be imported from `exsited` directly.

| Group | Names |
|---|---|
| Entry points | `build_client` `ExsitedClient` `ClientRegistry` |
| Registration | `register_instances` `list_instance_names` `get_registered_instances` |
| Configuration | `AuthConfig` `SdkConfig` `select_credentials` `read_client_name` `USE_DEFAULT_TOKEN_CACHE` `DEFAULT_RESPONSE_FORMAT` `VALID_RESPONSE_FORMATS` `RESPONSE_FORMAT_ENV_VAR` |
| Responses | `ApiResponse` `RequestInfo` `ErrorType` |
| Typed views | `Dto`; each family's views are in its own `<family>_dto` module |
| Errors | `SdkError` `SdkConfigError` `SdkUsageError` `SdkAttributeError` `SdkAuthError` `SdkTokenCacheError` `SdkTokenLockError` |
| Warnings | `InsecureTransportWarning` `DegradedTokenLockWarning` `DegradedTokenCacheWarning` |
| Diagnostics | `error_diagnostics_enabled` `set_error_diagnostics` `DIAGNOSTICS_ENVIRONMENT_VARIABLE` `render_exchange` `build_curl_command` |
| Resources | `register_resource_module` `registered_resource_names` `BoundResource` |
| Pagination | `iter_pages` `iter_records` |
| Tokens | `TokenProvider` `TokenRecord` `TokenStore` `MemoryTokenStore` `FileTokenStore` `build_token_path` `build_credentials_namespace` `build_default_token_cache_path` |
| HTTP | `Transport` `RetryPolicy` `build_url` `substitute_path_params` `build_query_params` `SortDirection` `DEFAULT_RETRYABLE_HTTP_CODES` `DEFAULT_UNSAFE_RETRYABLE_HTTP_CODES` |
| Filtering and sorting | `filter_param` `filter_values` `sort_param` `FILTER_OPERATORS` `PRESENCE_OPERATORS` `LIST_OPERATORS` |
| Redaction | `REDACTED` `SENSITIVE_KEY_MARKERS` `should_redact` `redact_value` `redact_mapping` `redact_text` `MAX_REDACTION_DEPTH` `CIRCULAR` `TOO_DEEP` |
| Version | `__version__` `SDK_VERSION` |
