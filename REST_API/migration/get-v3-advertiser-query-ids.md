# GET /v3/advertiser/query/ids → Query.advertisers

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-advertiser-query-ids
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/advertiser/query/ids → Query.advertisers

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/advertiser/query/ids` |
| GraphQL query | `Query.advertisers` |
| Return type | `[ID!]!` |

## Multi-step operations

REST returns all accessible advertiser IDs in a single response. GraphQL has no bulk-ID shortcut; paginate `Query.advertisers` (or `Partner.advertisers`) and collect `nodes { id }` across pages until `pageInfo.hasNextPage` is false.

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| (root) | `advertisers { nodes { id } }` | [ID!]! | Not nullable | Paginate and collect node IDs; no bulk-ID shortcut endpoint in GraphQL. |

## Code examples

### REST example

```
GET /v3/advertiser/query/ids HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AllAdvertiserIds {
  advertisers(first: 100) {
    nodes {
      id
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
