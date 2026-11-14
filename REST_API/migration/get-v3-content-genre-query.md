# GET /v3/content/genre/query → Query.contentGenres

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-content-genre-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/content/genre/query → Query.contentGenres

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/content/genre/query` |
| GraphQL query | `Query.contentGenres` |
| Return type | `ContentGenresConnection` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GenreId` | `id` | ID! | Not nullable | Maps from REST `GenreId`. |
| `GenreName` | `name` | String | Nullable | Maps from REST `GenreName`. |
| N/A | `inventoryTag` | GenreInventoryTag! | Not nullable | **Not currently available in GraphQL** |

## Endpoint-specific nested types and enums

### Genre

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GenreId` | `id` | ID! | Not nullable | Maps from REST `GenreId`. |
| `GenreName` | `name` | String | Nullable | Nullable in GraphQL schema. |

## Code examples

### REST example

```
GET /v3/content/genre/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ContentGenres {
  contentGenres(first: 100) {
    nodes {
      id
      name
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
