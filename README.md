# Exsited Python SDK

The Python SDK for the Exsited v4 REST API. Every endpoint is a function,
`client.<family>.<function>(...)`: you send a JSON request body (a dict or a JSON
string) and get the JSON response body back. Authentication, token refresh,
pagination helpers, retries and error handling are done for you.

Field names are the API's own. Nothing is renamed, case-converted or reshaped in
either direction.

## Requirements

- Python 3.10 or later
- An Exsited instance and an OAuth2 client (client id, client secret and redirect URI)

## Install

The distribution and the import are both `exsited`:

```bash
pip install "exsited>=4,<5"
```

## Configure credentials

Pass the credentials in yourself. The SDK does not read them from the environment,
so load them from environment variables, a secret manager or a config file of your
own and hand them to `AuthConfig`:

```python
import os

from exsited import AuthConfig

auth = AuthConfig(
    client_name="default",
    base_url=os.environ.get("EXSITED_BASE_URL", "https://your-instance.example.com"),
    client_id=os.environ.get("EXSITED_CLIENT_ID", "your-client-id"),
    client_secret=os.environ.get("EXSITED_CLIENT_SECRET", "your-client-secret"),
    redirect_uri=os.environ.get("EXSITED_REDIRECT_URI", "https://your-redirect-uri"),
)
```

`client_name` is required and names the instance in logs and printed output.
`AuthConfig` is validated at construction, and `repr` and `str` redact
`client_secret`, so an instance is safe to log.

Behaviour such as timeouts, retries and logging is set on `SdkConfig`, passed as
keywords. Every setting has a default:

```python
from exsited import SdkConfig

config = SdkConfig(auth, max_retries=3, log_level="DEBUG")
```

## First call

```python
from exsited import ExsitedClient, SdkConfig

with ExsitedClient(SdkConfig(auth)) as client:
    response = client.accounts.get_accounts({"limit": 50})
    for account in response.data["data"]:
        print(account["id"], account["name"])
```

Use `with`, or call `client.close_client()` yourself. `response.data` and
`response.map` are the decoded JSON, and `response.json` is the JSON text exactly as
it arrived.

## Errors

By default a failed call returns a response instead of raising, so you can read the
error body. Pass `raise_on_error=True` to a call, or set it in `SdkConfig`, to raise
`SdkError` instead:

```python
response = client.accounts.get_account("NOPE")
print(response.error_code, response.request_id, response.get_error_messages())

client.accounts.get_account("NOPE", raise_on_error=True)  # raises SdkError
```

## Pagination

Listings page by cursor or by offset. `iter_records` reads the shape from each page,
so one call walks either kind:

```python
from exsited import iter_records
from exsited.resources.accounts import accounts_urls

for account in iter_records(client, accounts_urls.ACCOUNTS, query_params={"limit": 100}):
    print(account["id"])
```

## Documentation

Full documentation, with an example for every endpoint, is at
https://exsited.mintlify.app

## License

MIT. See [LICENSE](LICENSE).
