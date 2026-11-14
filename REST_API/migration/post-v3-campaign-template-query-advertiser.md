# POST /v3/campaign/template/query/advertiser → Advertiser.campaignTemplates

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-campaign-template-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/campaign/template/query/advertiser → Advertiser.campaignTemplates

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/campaign/template/query/advertiser` |
| GraphQL query | `Advertiser.campaignTemplates` |
| Return type | `CampaignTemplatesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent key—attaches as `Advertiser.campaignTemplates` | ID! | Required | Resolve `Advertiser` by ID, then query `campaignTemplates`. |
| `SearchTerms` | N/A | N/A | Optional | No filter args on `campaignTemplates`—only `after` and `first`. |
| `SortFields` | N/A | N/A | Optional | No sort args on `campaignTemplates`. |
| `Availabilities` | N/A | N/A | Optional | No availability filter on `campaignTemplates`. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

Each `Result[]` item is a full REST `Campaign` (not `CampaignTemplate`). Row-level field mapping for campaign body fields is identical to `GET /v3/campaign/{campaignId}`—prefix GraphQL paths with `edges.node.` See that endpoint doc for the complete field table. Template publish/share fields are GraphQL-only on this connection (see rows below).

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `edges.node` | Campaign | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].CampaignId` | `edges.node.id` | ID! | Not nullable | N/A |
| Result[].* (remaining `Campaign` fields) | `edges.node.*` | N/A | N/A | Each `Result[]` item is a full REST `Campaign` model (via `CampaignAdapter.GetAPIModel`), not `CampaignTemplate`. Field mapping is identical to `GET /v3/campaign/{campaignId}`—prefix GraphQL paths with `edges.node.` See that endpoint doc for the complete field table. |
| N/A | `edges.node.isTemplatePublished` | Boolean | Nullable | GraphQL-only on this connection—not a property on REST `Campaign` items in `Page<Campaign>.Result[]`. Available on REST via `GET /v3/campaign/template/{campaignId}`. |
| N/A | `edges.node.templateShareType` | ShareType | Nullable | GraphQL-only on this connection—REST page items have no `ShareType`. Available on REST via `GET /v3/campaign/template/{campaignId}`. Enum values: `ADVERTISER`, `PARTNER`, `GLOBAL`, `NONE`. |

## Code examples

### REST example

```
POST /v3/campaign/template/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv456",
  "PageStartIndex": 0,
  "PageSize": 5
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCampaignTemplatesByAdvertiser($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    id
    campaignTemplates(first: 5) {
      edges {
        node {
          id
          isTemplatePublished
          templateShareType
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
      totalCount
    }
  }
}
```
