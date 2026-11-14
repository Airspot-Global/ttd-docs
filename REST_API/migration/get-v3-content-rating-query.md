# GET /v3/content/rating/query → Query.contentRatings

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-content-rating-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/content/rating/query → Query.contentRatings

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/content/rating/query` |
| GraphQL query | `Query.contentRatings` |
| Return type | `ContentRatingsConnection` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `RatingId` | `id` | ID! | Not nullable | Maps from REST `RatingId`. |
| `RatingName` | `name` | String | Nullable | Not populated from this REST response; available when selected on the GraphQL query. REST returns taxonomy-qualified names (`TaxonomyName > RatingName` when `TaxonomyId` is set); GraphQL `name` uses raw `RatingName` only. |

## Endpoint-specific nested types and enums

### ContentRating

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `RatingId` | `id` | ID! | Not nullable | Maps from REST `RatingId`. |
| `RatingName` | `name` | String | Nullable | Nullable in GraphQL schema. REST returns taxonomy-qualified names when `TaxonomyId` is set; GraphQL `name` uses raw `RatingName` only. |

## Code examples

### REST example

```
GET /v3/content/rating/query HTTP/1.1
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
query ContentRatings {
  contentRatings(first: 100) {
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
