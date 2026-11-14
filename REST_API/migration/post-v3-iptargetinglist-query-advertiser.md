# POST /v3/iptargetinglist/query/advertiser → Advertiser.ipTargetingLists

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-iptargetinglist-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/iptargetinglist/query/advertiser → Advertiser.ipTargetingLists

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/iptargetinglist/query/advertiser` |
| GraphQL query | `Advertiser.ipTargetingLists` |
| Return type | `IpTargetingListsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `Advertiser.ipTargetingLists` | N/A | Required | Advertiser ID is implicit from the parent `Advertiser` node. |
| `SearchTerms` | `filter.searchTerms` | [String!] | Optional | Optional search filter. |
| `SortFields` | `filter.sortFields` | [IPTargetingListSortingFieldSortingInput!] | Optional | Optional sort specification; see nested type below. |
| `PageStartIndex` | `filter.pageStartIndex` | Int | Optional | N/A |
| `PageSize` | `filter.pageSize` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `ipTargetingLists.nodes` | [IPTargetingListSummary!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `ipTargetingLists.totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].AdvertiserId` | `nodes { advertiserId }` | ID! | Not nullable | N/A |
| `Result[].IPTargetingListId` | `nodes { ipTargetingListId }` | ID! | Not nullable | N/A |
| `Result[].IPTargetingDataName` | `nodes { ipTargetingDataName }` | String! | Not nullable | N/A |
| `Result[].IPTargetingRangesCount` | `nodes { ipTargetingRangesCount }` | Long! | Not nullable | Count only; full ranges available via GET by ID. |

## Endpoint-specific nested types and enums

### IPTargetingListSortingFieldSortingInput

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `FieldId` | `fieldId` | IPTargetingListSortingFieldInput! | Required | N/A |
| `Ascending` | `ascending` | Boolean | Optional | Defaults to `true` when omitted. |

### IPTargetingListSortingFieldInput

| REST value | GraphQL enum value | Notes |
| --- | --- | --- |
| `DataName` | `DATA_NAME` | Default sort when `sortFields` is omitted. |

## Code examples

### REST example

```
POST /v3/iptargetinglist/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<advertiser-id>",
  "PageStartIndex": 0,
  "PageSize": 100
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserIPTargetingLists($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    id
    ipTargetingLists(
      first: 100
      filter: {
        advertiserId: $advertiserId
        pageStartIndex: 0
        pageSize: 100
      }
    ) {
      nodes {
        advertiserId
        ipTargetingListId
        ipTargetingDataName
        ipTargetingRangesCount
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
