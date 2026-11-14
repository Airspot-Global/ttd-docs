# POST /v3/bidlist/batch/get → Query.bidList(id:) (multiple)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-bidlist-batch-get
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/bidlist/batch/get → Query.bidList(id:) (multiple)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/bidlist/batch/get` |
| GraphQL query | `Query.bidList(id:)` (multiple selections) |
| Return type | `IBidList` (per selection) |

## Multi-step operations

One REST batch request maps to multiple top-level `bidList(id:)` selections. The per-ID error envelope from REST is not preserved in GraphQL.

| REST endpoint | GraphQL equivalent | Notes |
| --- | --- | --- |
| `POST /v3/bidlist/batch/get` | Multiple `bidList(id:)` selections in one query | Each ID is a separate selection; partial failures surface as null or field errors per selection |

## Request and filter field mapping

| REST request field | GraphQL argument / selection | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| (request body—JSON string array of bid list IDs) | Multiple `bidList(id: $id)` selections | ID! | Required | One aliased selection per ID, e.g. `a: bidList(id: $a)`, `b: bidList(id: $b)` |

## Response field mapping

Each successful REST row maps to one aliased `bidList(id:)` selection returning `IBidList`. Use the same body field mapping as `GET /v3/bidlist/{bidListId}`.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| (per-ID `BidListResult` body) | (per alias) | IBidList | Nullable | See `GET /v3/bidlist/{bidListId}` response mapping |
| Errors (per-ID REST error envelope) | N/A | N/A | N/A | Not preserved; failed IDs return `null` or a field error on that alias |

## Code examples

### REST example

```
POST /v3/bidlist/batch/get HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

["123456", "789012"]
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query BatchBidLists($a: ID!, $b: ID!) {
  a: bidList(id: $a) { id name }
  b: bidList(id: $b) { id name }
}
```
