# REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/RestToGqlMigrationGuide
- Retrieved: 2026-11-14
- Category: REST_API

---

# REST → GraphQL migration guide

This guide provides a complete, field-level mapping between every REST endpoint in the Platform API and its GraphQL equivalent. Whether migrating an existing REST integration or building new functionality, this guide documents exactly how each REST operation, field, and pattern translates to GraphQL.

For general guidelines, see also GraphQL API Resource Hub.

## Who this guide is for

| Audience | What this guide covers |
| --- | --- |
| Partner engineers | Migrate existing REST integrations to GraphQL. |
| New integrators | Choose between REST and GraphQL for a given operation. |
| AI agents and code-generation tools | Get structured mappings to translate REST code to GraphQL automatically. |

## How to use this guide

Each domain has a domain page (a summary of all endpoints and shared types) and an endpoint detail page per REST endpoint (the full field mapping and code examples).

The following table provides a list of example tasks you might have to perform.

| Task | Step |
| --- | --- |
| Understand the systematic differences | To see the patterns that apply across all endpoints (field naming, pagination, error handling, and so on), read Systematic differences between REST and GraphQL. |
| Find the relevant domain | To find the REST endpoints in use, navigate to the corresponding domain page (for example, Advertiser, Ad Group, or Campaign). |
| Get the field-level mapping | To get field-by-field input/output mappings, multi-step operation notes, and before/after code examples, follow the endpoint detail links from each domain page. |

## Systematic differences between REST and GraphQL

The following patterns apply uniformly across the entire API surface. Understanding them enables applying mechanical transformations to any endpoint without consulting the per-field mapping tables.

### Field name cases

REST uses PascalCase. GraphQL uses camelCase.

| REST | GraphQL |
| --- | --- |
| `AdvertiserName` | `advertiserName` |
| `IsEnabled` | `isEnabled` |
| `AttributionClickLookbackWindowInSeconds` | `attributionClickLookbackWindowInSeconds` |

Most fields follow this rule exactly. Exceptions (where the GraphQL field was renamed, not just re-cased, or where a REST `*Id` becomes a nested object such as REST `CampaignId` → `campaign.id`) are documented in each endpoint's field mapping table.

### Identifiers

REST endpoints use `int`, `long`, or `string` identifiers depending on the domain (for example, `AdvertiserId` is a string, `CategoryId` is a long). GraphQL uses the `ID` scalar for all entity identifiers—always transmitted as a string in JSON, regardless of the underlying storage type.

| REST | GraphQL |
| --- | --- |
| `"AdvertiserId": "abc123"` | `id: "abc123"` (type `ID!`) |
| `"CategoryId": 45` | `categoryId: 45` (type `Long!`) |

Note that the GraphQL `ID` scalar is a string in transport. Numeric IDs that are typed as `Long` or `Int` in GraphQL remain numeric.

### Single GraphQL endpoint

All GraphQL operations are sent to a single endpoint (`POST https://GRAPHQL_ENDPOINT_URL_PLACEHOLDER/graphql`). Include the same auth header used for REST:

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

Unlike REST, where each operation has its own URL path (`/v3/advertiser`, `/v3/campaign`, and so on), every GraphQL mutation and query is sent to the same URL. The operation is specified in the request body.

### Pagination

See also GraphQL API response pagination in our GraphQL Hub.

REST uses offset-based pagination with `PageStartIndex` and `PageSize`. GraphQL uses cursor-based pagination.

Here's an example REST request:

```
{
  "PartnerId": "abc123",
  "PageStartIndex": 0,
  "PageSize": 25
}
```

Here's the equivalent GraphQL query:

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query {
  advertisers(first: 25, after: null) {
    nodes {
      id
      name
    }
    pageInfo {
      hasNextPage
      endCursor
    }
    totalCount
  }
}
```

To fetch the next page, pass the `endCursor` value from the previous response as the `after` argument:

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query {
  advertisers(first: 25, after: "eyJpZCI6Mn0=") {
    nodes {
      id
      name
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Key differences:

| Concept | REST | GraphQL |
| --- | --- | --- |
| Page size | `PageSize` | `first` (forward) or `last` (backward) |
| Page position | `PageStartIndex` (zero-based offset) | `after` / `before` (opaque cursor) |
| Result count | `TotalFilteredCount` in response | `totalCount` on the connection |
| Items | `Result` array | `nodes` array (or `edges` with `node` and `cursor`) |
| Next page check | Compare `PageStartIndex + PageSize < TotalFilteredCount` | `pageInfo.hasNextPage` |

### Error handling

See also GraphQL API errors and complexity limits in our GraphQL Hub.

REST returns HTTP status codes (400, 401, 403, 404, 500) with a JSON error body. GraphQL always returns HTTP 200—errors are reported in the response payload.

Here's an example REST error response:

```
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "Message": "Validation failed.",
  "ErrorDetails": [
    {
      "Property": "$.AdvertiserName",
      "Reasons": ["Advertiser name must not be empty."]
    }
  ]
}
```

In GraphQL, every mutation returns a payload with a `data` field and an `errors` field. When the mutation succeeds, `data` is populated and `errors` is empty. When it fails, `data` is `null` and `errors` contains one or more error objects with `message` and `code`:

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  advertiserCreate(input: { ... }) {
    data {
      id
      name
    }
    errors {
      message
      code
    }
  }
}
```

Here's an example success response:

```
{
  "data": {
    "advertiserCreate": {
      "data": { "id": "adv-123", "name": "Acme Corp" },
      "errors": []
    }
  }
}
```

Here's an example error response:

```
{
  "data": {
    "advertiserCreate": {
      "data": null,
      "errors": [
        {
          "message": "Advertiser name must not be empty.",
          "code": "VALIDATION_ERROR"
        }
      ]
    }
  }
}
```

Consult the GraphQL schema for the specific error types available on each mutation's `errors` field.

### Timestamps

REST uses various DateTime string formats depending on the endpoint. GraphQL uses the `DateTime` scalar, which is always ISO 8601 format:

| REST | GraphQL |
| --- | --- |
| `"2026-01-15T00:00:00"` (varies) | `"2026-01-15T00:00:00Z"` (ISO 8601, UTC) |

### Structural differences in response types

Some REST fields that are flat scalars or simple objects are represented differently in GraphQL responses. Here are the common patterns:

| Pattern | REST | GraphQL |
| --- | --- | --- |
| Country | `"Country": "US"` (string) | `country { id shortName longName }` (object) |
| Currency | `"CurrencyCode": "USD"` (string) | `currency { id longName }` (object) |
| Attribution windows | `"AttributionClickLookbackWindowInSeconds": 604800` (flat field) | `attribution { clickLookbackWindow clickInterval ... }` (nested object) |
| Custom labels | `[{ "CustomLabelId": "lbl-1" }]` (objects with IDs) | `customLabels: ["label-name"]` (string names) on input; `customLabels(first:) { nodes { ... } }` (connection) on response |

These per-field structural differences are documented in each endpoint's field mapping table. The patterns in this table are the most common ones encountered during migration.
