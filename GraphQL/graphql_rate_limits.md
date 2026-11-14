# GraphQL API rate limits

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/GqlApiRateLimits
- Retrieved: 2026-11-14
- Category: GraphQL

---

# GraphQL API rate limits

Our GraphQL API enforces rate limits to ensure fair and effective access for all clients. Rate limits are designed to safeguard the stability of our products and provide clear guidance for managing usage. When you receive a rate limit, you will get the `429` request error code and should handle them gracefully.

## Rate calculations

Rate limits are set as the maximum number of requests an user account can make within a timeframe. In addition, your system usage is continuously monitored, and dynamic adjustments may be applied to high-cost requests to protect API uptime during periods of high demand.

In certain scenarios where clients distribute their API traffic across multiple user accounts, you might be subject to group throttling in addition to user account throttling. This mechanism ensures fair usage and protects platform stability. For details on group throttling and its implications, contact your Technical Account Manager.

## 429 error code

When your API usage rate limit is exceeded, the response returns an HTTP `429` error code and the API blocks further execution of the request. After a period of reduced call activity, you are permitted to send successful requests again.

> **TIP**: To avoid repeated throttles, follow the `retry-after` header or implement an exponential backoff strategy. For details, see mitigation.

## Rate limit management

To create workflows that do not break when rate limited, your code should be able to handle the `429` error code. Follow these sections for best practices to perform rate limit prevention and mitigation.

### Prevention

To prevent multiple instances of rate limits, build your integrations with logic to wait between subsequent calls and reduce the number of calls sent to the API.

Here are some considerations for developing your integration using GraphQL:

- Limit concurrency to four callers per operation.
- When using GraphQL mutations, use batch requests to reduce the number of requests made to the API.
- Cache data that does not change frequently and use it instead of calling the API.
- If applicable, utilize delta mutations that reduce execution times and call frequency. For examples, see our Delta Python Scripts on Github.

### Mitigation

You should ensure your implementation can properly handle repeated `429` errors after your callers have been rate limited. There are several approaches that you can implement depending on the needs of your integration and other factors such as response size, performance, and difficulty.

To reduce timeout risks, consider doing either of the following:

- A fixed delay between calls or wait 1 minute after a failed call before retry.
- Inspect the `'retry-after'` heading in the HTTP response and extract the value (in seconds)
`'retry-after': '#'`
- Implement a backoff policy that waits for progressively longer periods between each failed call. The following example uses exponential growth for delay time.
`Delay = Min (max_delay, base_delay * 2 ^ retrycount)`

## Additional resources

You may find the following external resources useful to manage rate limits:

- HTTP status codes RFC
- Exponential Backoff and Jitter
- Implementing HTTP Call Retries with Exponential Backoff with Polly

## FAQs

The following sections provide answers to the most commonly asked questions about rate limits.

### Are GraphQL API rate limits different from those for the REST API?

No. API rate limits are enforced in the same manner for GraphQL and REST, but your REST API call count is independent of your GraphQL API call count.

### Does my UI usage count toward my API rate limits?

Yes. The UI product page calls the corresponding API with your account credentials, so the usage counts.

### How do I increase my rate limit?

If you have a special case that requires increased volume or traffic, contact your Technical Account Manager.
