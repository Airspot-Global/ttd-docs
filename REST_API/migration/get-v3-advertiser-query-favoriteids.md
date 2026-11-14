# GET /v3/advertiser/query/favoriteids → Me.favoritedAdvertisers

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-advertiser-query-favoriteids
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/advertiser/query/favoriteids → Me.favoritedAdvertisers

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/advertiser/query/favoriteids` |
| GraphQL query | `Me.favoritedAdvertisers` |
| Return type | `[ID!]!` |

## Multi-step operations

REST returns favorite advertiser IDs for the current user in one call. GraphQL exposes favorites via `Me.favoritedAdvertisers` (paginated connection) or by filtering `Query.advertisers` / `Partner.advertisers` with `where.isFavoriteForUser eq true`.

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| (root) | `me { favoritedAdvertisers { nodes { id } } }` | [ID!]! | Not nullable | Alternatively filter advertiser queries with `where.isFavoriteForUser eq true`. |

## Code examples

### REST example

```
GET /v3/advertiser/query/favoriteids HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query FavoriteAdvertiserIds {
  me {
    favoritedAdvertisers(first: 100) {
      nodes {
        id
      }
    }
  }
}
```
