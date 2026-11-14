# REST API return codes

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/ReturnCodes
- Retrieved: 2026-11-14
- Category: Guides

---

# REST API return codes

The REST API supports the following HTTP response codes to indicate the request status.

| Numeric Code | Message | Description |
| --- | --- | --- |
| 200 | OK | The request was successful. |
| 240 | No Content | The request was successful, but there is no content to return. |
| 400 | Bad Request | The request did not contain all required input, had malformed syntax, or the included input failed validation. |
| 401 | Unauthorized | The user does not have valid authentication credentials to access the requested resource. |
| 403 | Forbidden | The user does not have access to this endpoint or the entity for which they made the call; or the endpoint or entity does not exist. |
| 404 | Not Found | The requested resource has not been found. |
| 409 | Conflict | The request conflicts with the current state of the server. |
| 410 | Gone | The request uses a deprecated endpoint or property. |
| 429 | Too Many Requests | The number of sent requests to the endpoint has exceeded the rate limit. |
| 500 | Internal Server Error | The server encountered an unexpected condition, which prevented it from fulfilling the request or serving the response. |
| 503 | Service Unavailable | The server was unable to handle the request due to a temporary overload. Use the `'Retry-After'` header as guidance on when to retry your request. |

See also the HTTP status codes RFC.
