# REST API rate limits

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/RateLimits
- Retrieved: 2026-11-14
- Category: Guides

---

# REST API rate limits

The API enforces resource governance to ensure all clients can use The Trade Desk services effectively. API endpoint rate limits are an essential part of resource governance and are defined to both protect the platform and inform callers of excessive use. API endpoint limits are defined as a maximum number of calls a client can make to each platform endpoint within a time period, usually a minute. System level usage is also monitored and can result in further dynamic reductions to the rate limits to protect the overall platform.

In some cases, our clients might find it useful to divide their API traffic among several API user accounts. To help safeguard application reliability, especially in cases where the users have similar patterns of API utilization, these users might be throttled as a group. For more information about group throttling, contact your Technical Account Manager.

## FAQs

The following sections provide answers to the most commonly asked questions about rate limits.

### How are rate limits are enforced?

When the rate limit for an API endpoint is exceeded, the endpoint returns an HTTP `429` status code and prevents execution. After a period of time of reduced number of calls, the call rate will drop to a level allowing successful execution.

### How can I avoid exceeding rate limits?

Your code should be able to handle 429 errors and retry after waiting a reasonable amount of time. If you receive the `429` status code too often, consider doing the following:

- Limit concurrency to four callers per endpoint.
- Cache data that does not change frequently. Some examples of calls where data can be cached weekly or monthly are:

  - GET category/industrycategories
  - POST dmp/firstparty/advertiser
  - POST dmp/thirdparty/advertiser (See also Query performance guidance for retrieving third-party data.)
  - POST geosegment/query/partner

- Utilize delta endpoints that reduce execution times and call frequency. For details, see Platform synchronization.

### How should I handle 429 responses?

Requests from the client are throttled until the overall request volume from the client is reduced to the appropriate rate, adhering to the `retry-after` or applying an exponential backoff policy helps to avoid unnecessary calls that result in throttles.

Properly handling 429 errors when they occur should be a part of your base implementation. Implement one of the following solutions depending on the needs of your integration.

- A fixed delay between calls or wait 1 minute after a failed call before retry.
- An exponential backoff policy that waits for progressively longer periods between each failed call.
`Delay = Min (max_delay, base_delay * 2 ^ retrycount)`
- Inspect the `'retry-after'` heading in the HTTP response and extract the value (in seconds)
`'retry-after': '#'`

## Query performance guidance for retrieving third-party data

The following table explains how to maximize performance and reduce likelihood of timeouts when using the POST /v3/dmp/thirdparty/advertiser.

| Scenario | Guidance | Impact |
| --- | --- | --- |
| You don't utilize `TotalFilteredCount` or `TotalUnfilteredCount` from the response. | Set `ExcludeTotalCounts` to `true` in your request. | Excluding counts from the response improves performance and reduces the likelihood of a timeout. |
| You perform searches with wide-open filters when you're looking for specific brands. | Reduce the scope of the query by utilizing `BrandIds` in your request. | Reducing the scope of the query improves performance. |
| You refresh third-party data information by querying all records. | Reduce the scope of the query by utilizing `ThirdPartyDataIds` in your request to refresh information for specific IDs. | Reducing the scope of a query improves performance. |
| You use a `PageSize` of greater than `1000`. | Consider using a `PageSize` of around `1000` in your request. | Using `PageSizes` of `1000` and smaller improves performance and reduces the likelihood of a timeout. |

### Additional resources

> **TIP**: To use GraphQL, see the GraphQL Resource Hub.

You may find the following external resources useful to manage rate limits:

- HTTP status codes RFC
- Exponential Backoff and Jitter
- Implementing HTTP Call Retries with Exponential Backoff with Polly
