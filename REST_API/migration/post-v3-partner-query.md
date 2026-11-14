# POST /v3/partner/query → Query.partners

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-partner-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/partner/query → Query.partners

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/partner/query` |
| GraphQL query | `Query.partners` |
| Return type | `PartnersConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `SearchTerms` | `where.name` | StringOperationFilterInput | Optional | No `searchTerms` argument; use `name: { contains: "..." }` for substring match (or `id: { contains: "..." }`). |
| `SortFields` | `order` | [PartnerSortInput!] | Optional | Sort input (e.g. `order: [{ name: ASC }]`). |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [Partner!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].PartnerId` | `nodes[].id` | ID! | Not nullable | N/A |
| `Result[].PartnerIdInteger` | `nodes[].idInteger` | Int! | Not nullable | N/A |
| `Result[].PartnerName` | `nodes[].name` | String! | Not nullable | N/A |
| `Result[].AssociatedBidLists` | `nodes[].associatedBidLists` | AssociatedBidListsConnection | Nullable | See the Partner domain page for nested fields; select via `nodes`. |
| `Result[].AssociatedBidLists.BidListId` | `nodes[].associatedBidLists { nodes { bidList { id } } }` | ID! | Not nullable | Nested—see AssociatedBidList on the Partner domain page. |
| `Result[].AssociatedBidLists.IsEnabled` | `nodes[].associatedBidLists { nodes { isEnabled } }` | Boolean! | Not nullable | N/A |
| `Result[].AssociatedBidLists.IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].AssociatedBidLists.BidListSource` | `nodes[].associatedBidLists { nodes { bidList { source } } }` | BidListSource! | Not nullable | N/A |
| `Result[].AssociatedBidLists.BidListAdjustmentType` | `nodes[].associatedBidLists { nodes { bidList { adjustmentType } } }` | BidListAdjustmentType! | Not nullable | N/A |
| `Result[].AssociatedBidLists.BidListDimensions` | `nodes[].associatedBidLists { nodes { bidList { dimensions } } }` | [BidListDimension!]! | Not nullable | N/A |
| `Result[].Increments` | `nodes[].increments` | [String!]! | Not nullable | N/A |
| `Result[].NewFrequencyConfigs` | N/A | N/A | N/A | Never returned by this endpoint—omitted from GraphQL output. |

## Code examples

### REST example

```
POST /v3/partner/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "SearchTerms": ["acme"],
  "PageStartIndex": 0,
  "PageSize": 20
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query SearchPartners {
  partners(
    first: 20
    where: { name: { contains: "acme" } }
    order: [{ name: ASC }]
  ) {
    nodes {
      id
      idInteger
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
