# POST /v3/seller/query → Query.publishers

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-seller-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/seller/query → Query.publishers

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/seller/query` |
| GraphQL query | `Query.publishers(where: PublisherFilterInput, order: [PublisherSortInput!])` |
| Return type | `PublishersConnection` |

## Multi-step operations

| Concern | GraphQL approach | Notes |
| --- | --- | --- |
| Paged seller list | `Query.publishers` | Reuses the existing publishers connection instead of a dedicated sellers query. |
| Seller metadata on list nodes | `Publisher.isTargetable`, `Publisher.sellerStatus`, `Publisher.aliasToSellerDomain`, `Publisher.sellerDomainAliases` | Select on each node in `publishers.nodes`; backed per-domain by `GET /v3/seller/{sellerDomain}`. |

**Behavioral differences from REST:**

- REST applies `showOnlySellersWithSignificantSpend: true` on this POST query (only sellers with platform spend). `Query.publishers` may not apply the same spend scoping.
- REST `SellerStatusFilter` (Allowed/Disallowed) is **Not currently available in GraphQL** on `PublisherFilterInput` (`publisherMarketplaceState` is a different concept).

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `IncludedSellerDomains` | `PublisherFilterInput.publisherDomain` | String filter | Optional | Filter to specific seller domains. |
| `SellerNameFilters` | `PublisherFilterInput.publisherName` | String filter | Optional | Name contains filters. |
| `SellerStatusFilter` | N/A | N/A | Optional | **Not currently available in GraphQL** |
| `SortFields` | `order: [PublisherSortInput!]` | PublisherSortInput | Optional | `SellerName` → `publisherName`; `SellerDomain` → `publisherDomain`. Default REST sort is `SellerName ASC`. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| Result (page elements) | `publishers.nodes` | [Publisher!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `publishers.totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].SellerDomain` | `nodes.domain` | String! | Not nullable | N/A |
| `Result[].SellerName` | `nodes.name` | String! | Not nullable | N/A |
| `Result[].AliasToSellerDomain` | `nodes.aliasToSellerDomain` | String | Nullable | N/A |
| `Result[].SellerDomainAliases` | `nodes.sellerDomainAliases` | [String!]! | Not nullable | May be empty. |
| `Result[].SellerStatus` | `nodes.sellerStatus` | SellerStatus | Nullable | See the Seller domain page for enum mapping. |
| `Result[].IsTargetable` | `nodes.isTargetable` | Boolean | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/seller/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 25,
  "SellerNameFilters": ["news"],
  "SortFields": [{ "Field": "SellerName", "Direction": "Ascending" }]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query SellerListParity {
  publishers(
    first: 25
    where: { publisherName: { contains: "news" } }
    order: [{ publisherName: ASC }]
  ) {
    nodes {
      id
      domain
      name
      isTargetable
      sellerStatus
      sellerDomainAliases
    }
    pageInfo {
      hasNextPage
      endCursor
    }
    totalCount
  }
}
```
