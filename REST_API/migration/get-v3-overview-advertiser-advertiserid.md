# GET /v3/overview/advertiser/{advertiserId} → Query.advertiser(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-overview-advertiser-advertiserid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/overview/advertiser/{advertiserId} → Query.advertiser(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/overview/advertiser/{advertiserId}` |
| GraphQL query | `Query.advertiser(id:)` |
| Return type | `Advertiser` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `advertiserId` | `advertiser(id: $advertiserId)` | ID! | Required | Root query argument. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `id` | ID! | Not nullable | N/A |
| `AdvertiserName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `Campaigns` | `campaigns` | CampaignsWithAggregatesConnection | Nullable | Paginate; nested fields under `campaigns { nodes { … } }`; see CampaignOverview on the Overview domain page. |
| `Creatives` | `creatives` | AdvertiserCreativesConnection | Nullable | Advertiser-level creative list; paginate. |

## Code examples

### REST example

```
GET /v3/overview/advertiser/{advertiserId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserOverview($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    id
    name
    description
    campaigns(first: 100, where: { isArchived: { eq: false } }) {
      nodes {
        id
        name
        description
        startDate
        endDate
        isArchived
        adGroups(first: 100, where: { isArchived: { eq: false } }) {
          nodes {
            id
            name
            description
            isEnabled
            isArchived
            creatives(first: 100) {
              nodes { id name description }
            }
          }
        }
      }
    }
    creatives(first: 100) {
      nodes { id name description }
    }
  }
}
```
