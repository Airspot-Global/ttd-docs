# GraphQL API errors and complexity limits

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/GqlApiErrors
- Retrieved: 2026-11-14
- Category: GraphQL

---

# GraphQL API errors and complexity limits

To optimize performance and prevent overload, The Trade Desk has GraphQL query complexity limits and other rate-limiting rules. Query complexity refers to the amount of work needed to process your request. It increases with the depth of search and breadth of fields to return.

Here's what you need to know about the error types and responses that you might receive when making calls with the GraphQL API:

- All errors are returned with an HTTP 200 status code.
- An error can contain an error code, message, or more fields in the response.
- There are two types of errors as shown in the following table.

| Type of Error | Description | Example |
| --- | --- | --- |
| Unexpected | Top-level errors that occur outside of the expected query or mutation workflow. These errors might include internal server errors, syntax errors, and more | An internal server error where your request contains too many tokens. |
| Expected | Field-specific errors that are defined in the GraphQL schema as possible outcomes for certain queries or mutations | A validation error where your mutation input doesn't meet the schema requirements. |

> **TIP**: To receive detailed messages about potential errors, always include appropriate error fields in your requests.

## Unexpected errors

When using GraphQL, certain limits can cause two types of unexpected errors. These errors appear inside the `errors` object outside of your data object, as a list of error objects. This is different from the expected errors, which are returned inside the body of the response, as an object.

| Error | Description | Example |
| --- | --- | --- |
| System errors | Errors due to the system configuration limits of the GraphQL software. | Complexity limit reached. |
| API gateway errors | Errors due to GraphQL API usage but excludes REST API usage. | Account request limit exceeded. |

### System errors

System errors occur due to queries or mutations that violate rules set up by the GraphQL software. Most commonly, this happens when you have a query that's too complex to run. The GraphQL API calculates the complexity of each query and mutation, then determines if a call will cause overload. When you encounter a system error, the GraphQL API returns an `errors` object nested under the `data` object in your response.

To reduce complexity, see the following tips:

- Limit query scope to optimize results and return less items. For example, narrow the focus of your query by specifying identifiers (like `BrandIds` or `ThirdPartyDataIds`) whenever possible.
- Limit data requests in GraphQL to query for only the values you need.
- Limit optional data processing in GraphQL unless required. For example, when querying for data, avoid requesting the `totalCount` field unless you need it.
- Limit page size to around 1000 in your paginated requests.

#### Complexity limit error example

Here's an example JSON response for a GraphQL API call that failed due to high complexity.

```
{
  "errors": [
    {
      "message": "Complexity limit of {COMPLEXITY_LIMIT_PLACEHOLDER} hit. Request complexity: {YOUR_COMPLEXITY_PLACEHOLDER}.",
    }
  ]
}
```

> **NOTE**: Complexity limits are put in place to reduce heavy workloads, but if your query is slow or unresponsive, you can still have a complexity issue. For examples of complex queries, see GraphQL queries.

### API gateway errors

API Gateway errors occur when you have too much workload in your queries or mutations for our servers to handle. You may be causing an infinite loop, or your query may require too many resources to run. In an API Gateway error, you receive a 429 status code with a message describing the cause. For details, see Rate limits.

## Error codes

When you surpass the limits of GraphQL, you will receive an error message and code that describes that went wrong. Depending on the type of error, GraphQL may hide the message unless explicitly asked for in your request.

The following table lists the possible GraphQL errors that appear in the `code` field of the response.

| Error Response Code | Description | Type of Error |
| --- | --- | --- |
| `AUTHENTICATION_FAILURE` | The user doesn't have valid authentication credentials to access the requested resource. | Expected Error |
| `INTERNAL_SERVER_ERROR` | The server encountered an unexpected condition, which prevented it from fulfilling the request or serving the response. | Unexpected Error |
| `RESOURCE_LIMIT_EXCEEDED` | The request exceeded the threshold on the rate limit or complexity limit. | Unexpected Error |
| `SERVICE_UNAVAILABLE` | The service is temporarily unavailable. | Unexpected Error |
| `NOT_FOUND` | The requested resource isn't found, or the authenticated user isn't authorized to perform the requested action. | Expected Error |
| `VALIDATION_FAILURE` | The request didn't have all required input values, had malformed syntax, or the included input that failed validation. | Expected Error |

### Error code examples

Here's an example of an unexpected execution error for `AUTHENTICATION_FAILURE` with a detailed message.

```
{
  "errors": [
    {
      "message": "IDX10223: Lifetime validation failed. The token is expired. ValidTo (UTC): '04/26/2024 04:26:36', Current time (UTC): '05/23/2024 00:57:50'.",
      "extensions": {
        "code": "AUTHENTICATION_FAILURE"
      }
    }
  ]
}
```

Here's an example of an unexpected execution error for `INTERNAL_SERVER_ERROR`.

```
{
  "data": {
    "campaigns": null
  },
  "errors": [
    {
      "message": "Unexpected Execution Error",
      "locations": [
        {
          "line": 1,
          "column": 2
        }
      ],
      "path": [
        "campaigns"
      ],
      "extensions": {
        "code": "INTERNAL_SERVER_ERROR"
      }
    }
  ]
}
```

Here's an example of an expected error for `NOT_FOUND` that doesn't use the system error object. For details, see GraphQL mutations.

```
{
  "data": {
    "userSaveSettings": {
      "userErrors": [
        {
          "message": "Please choose a setting to save.",
          "field": [
            "setting"
          ]
        }]
    }
  }
}
```
