# POST /v3/advertiser/query/partner → Partner.advertisers

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-advertiser-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/advertiser/query/partner → Partner.advertisers

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/advertiser/query/partner` |
| GraphQL query | `Partner.advertisers` |
| Return type | `AdvertisersConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerms` | `where.name` | StringOperationFilterInput | Optional | No `searchTerms` filter; use `name: { contains: "..." }` for substring match (or `id: { contains: "..." }`). |
| `SortFields` | `order` | [AdvertiserForPartnerSortInput!] | Optional | Sort input (e.g. `order: [{ name: ASC }]`). |
| `Availabilities` | `where.isArchived` | IsArchivedFilterInput | Optional | REST Availability Archived/Available maps to `isArchived` filter. |
| `PartnerId` | Parent: `partner(id:)` | ID! | Required | Parent entity key; not a public query argument. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [Advertiser!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[]` | `nodes` | Advertiser | Nullable | Each page item is a full Advertiser entity; field-level mapping same as GET /v3/advertiser/{`advertiserId`}. |

## Code examples

### REST example

```
POST /v3/advertiser/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "partner123",
  "PageStartIndex": 0,
  "PageSize": 50,
  "SearchTerms": ["Acme"],
  "Availabilities": ["Available"]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query PartnerAdvertisers {
  partner(id: "partner123") {
    advertisers(
      first: 50
      where: { name: { contains: "Acme" }, isArchived: { eq: false } }
      order: [{ name: ASC }]
    ) {
      nodes {
        id
        name
        description
      }
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
