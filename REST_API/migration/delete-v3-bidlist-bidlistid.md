# DELETE /v3/bidlist/{bidListId} → bidListDelete

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/delete-v3-bidlist-bidlistid
- Retrieved: 2026-11-14
- Category: REST_API

---

# DELETE /v3/bidlist/{bidListId} → bidListDelete

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `DELETE /v3/bidlist/{bidListId}` |
| GraphQL operation | `bidListDelete` |
| Input type | `BidListDeleteInput` |
| Output type | `BidListDeletePayload` (`data: BidListDeleteReturn`, `errors: [BidListDeleteMutationError!]`) |

## Input field mapping

Input type: `BidListDeleteInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| bidListId (path) | `id` | ID! | Required | Path parameter becomes `input.id` |

## Output field mapping

Output type: `BidListDeleteReturn` (returned as `data` on `BidListDeletePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| bidListId (long) | `data.wasDeleted` | Boolean! | Not nullable | REST returns the deleted ID; GraphQL returns a success indicator on `data` |
| N/A | `errors` | [BidListDeleteMutationError!] | Nullable | Union of delete-specific errors (for example `BidListNotFoundError`) when deletion fails |

## Code examples

### REST example

```
DELETE /v3/bidlist/bl_abc123 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation DeleteBidList {
  bidListDelete(input: { id: "bl_abc123" }) {
    data {
      wasDeleted
    }
    errors {
      ... on BidListNotFoundError {
        message
        field
      }
    }
  }
}
```
