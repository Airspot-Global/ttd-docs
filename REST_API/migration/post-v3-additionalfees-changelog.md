# POST /v3/additionalfees/changelog → Campaign.passThroughFeeCards

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-additionalfees-changelog
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/additionalfees/changelog → Campaign.passThroughFeeCards

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/additionalfees/changelog` |
| GraphQL query | `Campaign.passThroughFeeCards(where:)` |
| Return type | `PassThroughFeeCard` connection |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `OwnerType` | `passThroughFeeCards(where.targetType)` | PassThroughFeeTargetType! | Required | `campaign` → `CAMPAIGN`, `adgroup` → `AD_GROUP`, `advertiser` → `ADVERTISER`. |
| `OwnerId` | `passThroughFeeCards(where.ownerId)` | String | Required | Same owner filter as the current-card GET. |
| `StartDateUtc` | `passThroughFeeCards(where.startDateUtc.gte)` | DateTime | Optional | Lower bound on card effective date. |
| `EndDateUtc` | `passThroughFeeCards(where.startDateUtc.lte)` | DateTime | Optional | Upper bound; REST filters cards in range. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| _(list of cards)_ | `passThroughFeeCards.nodes[]` | [PassThroughFeeCard!] | Nullable | Each node uses the same per-card mapping as GET current card. |
| _(no REST ID)_ | `passThroughFeeCards.nodes[].id` | Long! | Not nullable | GraphQL exposes the primary key; REST omits it. |
| `OwnerId` | `passThroughFeeCards.nodes[].target` (union member `id`) | ID! | Not nullable | Owner ID is on the `target` union member (`Campaign`, `AdGroup`, `Advertiser`, or `Partner`). Select with inline fragments matching `targetType`. |
| `OwnerType` | `passThroughFeeCards.nodes[].targetType` | PassThroughFeeTargetType! | Not nullable | REST `campaign` → `CAMPAIGN`, `adgroup` → `AD_GROUP`, `advertiser` → `ADVERTISER`. |
| `StartDateUtc` | `startDateUtc` | DateTime! | Not nullable | N/A |
| `Fees` | `passThroughFees` (connection) | PassThroughFeesConnection | Nullable | N/A |
| `Fees[].Description` | `passThroughFees.nodes.description` | String! | Not nullable | N/A |
| `Fees[].Amount` | `passThroughFees.nodes.amount` | Decimal | Nullable | N/A |
| `Fees[].FeeType` | `passThroughFees.nodes.type` | PassThroughFeeType! | Not nullable | See the AdditionalFees domain page for enum mapping. |

## Code examples

### REST example

```
POST /v3/additionalfees/changelog HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "OwnerType": "campaign",
  "OwnerId": "<campaignId>",
  "StartDateUtc": "2025-01-01T00:00:00Z",
  "EndDateUtc": "2026-12-31T23:59:59Z"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CampaignFeeCardChangelog {
  campaign(id: "<campaignId>") {
    id
    passThroughFeeCards(
      first: 50
      where: {
        ownerId: { eq: "<campaignId>" }
        targetType: { eq: CAMPAIGN }
        startDateUtc: {
          gte: "2025-01-01T00:00:00Z"
          lte: "2026-12-31T23:59:59Z"
        }
      }
      order: [{ startDateUtc: ASC }]
    ) {
      nodes {
        id
        targetType
        target {
          ... on Campaign {
            id
          }
        }
        startDateUtc
        passThroughFees(first: 20) {
          nodes {
            description
            amount
            type
          }
        }
      }
    }
  }
}
```
