# POST /v3/campaign/query/advertiser → Advertiser.campaigns

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-campaign-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/campaign/query/advertiser → Advertiser.campaigns

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/campaign/query/advertiser` |
| GraphQL query | `Advertiser.campaigns` |
| Return type | `CampaignsWithAggregatesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent key—attaches as `Advertiser.campaigns` | ID! | Required | Resolve `Advertiser` by ID, then query `campaigns`. |
| `SearchTerms` | `where.name` | StringOperationFilterInput | Optional | No direct `searchTerms` arg—filter by name via `where`. |
| `SortFields` | `order` | [CampaignForAdvertiserSortInput!] | Optional | REST sort fields map to `CampaignForAdvertiserSortInput` members (e.g. `name`, `startDate`). |
| `Availabilities` | `where.isArchived` | IsArchivedFilterInput | Optional | REST `Available`/`Archived` → `isArchived` (e.g. `Available` → `{ eq: false }`). |
| `Availabilities` | `where.status` | CampaignStatusOperationFilterInput | Optional | REST `Available`/`Archived` may also map to `status` filters. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

Row-level field mapping for each `Campaign` in `Result[]` is identical to `GET /v3/campaign/{campaignId}`—prefix GraphQL paths with `nodes[].` (e.g. `nodes[].status`, `nodes[].budget.total`). See that endpoint doc for the complete field table.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [Campaign!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].CampaignId` | `nodes[].id` | ID! | Not nullable | N/A |
| `Result[].CampaignName` | `nodes[].name` | String! | Not nullable | N/A |
| `Result[].StartDate` | `nodes[].startDate` | DateTime! | Not nullable | N/A |
| `Result[].EndDate` | `nodes[].endDate` | DateTime | Nullable | N/A |
| Result[].* (remaining `Campaign` fields) | `nodes[].*` | N/A | N/A | Each `Result[]` item is a full REST `Campaign` model. Field mapping is identical to `GET /v3/campaign/{campaignId}`—prefix GraphQL paths with `nodes[].` (e.g. `nodes[].status`, `nodes[].budget.total`). See that endpoint doc for the complete field table. |

## Code examples

### REST example

```
POST /v3/campaign/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv456",
  "Availabilities": ["Available"],
  "PageStartIndex": 0,
  "PageSize": 25
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCampaignsByAdvertiser($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    id
    campaigns(
      first: 25
      where: { isArchived: { eq: false } }
    ) {
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        id
        name
        startDate
        endDate
      }
    }
  }
}
```
