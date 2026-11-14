# GET /v3/additionalfees/{ownerType}/{ownerId} → Campaign.passThroughFeeCards

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-additionalfees-ownertype-ownerid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/additionalfees/{ownerType}/{ownerId} → Campaign.passThroughFeeCards

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/additionalfees/{ownerType}/{ownerId}` |
| GraphQL query | `Campaign.passThroughFeeCards(where:)` |
| Return type | `PassThroughFeeCard` connection |

## Multi-step operations

| ownerType (path) | GraphQL entry point | Notes |
| --- | --- | --- |
| `campaign` | `campaign(id: ownerId) { passThroughFeeCards(...) }` | Query from the Campaign entity. |
| `adgroup` | `adGroup(id: ownerId) { campaign { passThroughFeeCards(...) } }` | Fee cards are exposed on `Campaign`; filter with `targetType: AD_GROUP` and `ownerId` matching the ad group. |
| `advertiser` | N/A | No direct `Advertiser.passThroughFeeCards` field; use `POST /v3/additionalfees/changelog` (`Campaign.passThroughFeeCards` with date filters) or target-specific campaign/ad group cards. |

**Current-card selection:** REST returns a single nullable card. GraphQL returns a connection—select the node whose `startDateUtc` is active at the query time per applicable product rules.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| ownerType (path) | `passThroughFeeCards(where.targetType)` | PassThroughFeeTargetType! | Required | `campaign` → `CAMPAIGN`, `adgroup` → `AD_GROUP`. |
| ownerId (path) | `passThroughFeeCards(where.ownerId)` | String | Required | Maps to the fee card owner identifier. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| _(no REST ID)_ | `id` | Long! | Not nullable | GraphQL exposes the primary key; REST omits it. |
| `OwnerId` | `target` (union member `id`) | ID! | Not nullable | Owner ID is on the `target` union member (`Campaign`, `AdGroup`, `Advertiser`, or `Partner`). Select with inline fragments matching `targetType`. |
| `OwnerType` | `targetType` | PassThroughFeeTargetType! | Not nullable | REST `campaign`/`adgroup` → `CAMPAIGN`/`AD_GROUP`. |
| `StartDateUtc` | `startDateUtc` | DateTime! | Not nullable | N/A |
| `Fees` | `passThroughFees` (connection) | PassThroughFeesConnection | Nullable | Nested fees on the card. |
| `Fees[].Description` | `passThroughFees.nodes.description` | String! | Not nullable | N/A |
| `Fees[].Amount` | `passThroughFees.nodes.amount` | Decimal | Nullable | GraphQL amount (not ×100). |
| `Fees[].FeeType` | `passThroughFees.nodes.type` | PassThroughFeeType! | Not nullable | See the AdditionalFees domain page for enum mapping. |

## Code examples

The following are examples of reading the current fee card for a campaign and for an ad group.

Current campaign fee card (`ownerType` = `campaign` → `Campaign.passThroughFeeCards(where:)`):

### REST example

```
GET /v3/additionalfees/campaign/{campaignId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CampaignCurrentFeeCard {
  campaign(id: "<campaignId>") {
    id
    passThroughFeeCards(
      first: 5
      where: {
        ownerId: { eq: "<campaignId>" }
        targetType: { eq: CAMPAIGN }
      }
      order: [{ startDateUtc: DESC }]
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

Current ad group fee card (`ownerType` = `adgroup` → `Campaign.passThroughFeeCards(where:)` via parent campaign):

### REST example

```
GET /v3/additionalfees/adgroup/{adGroupId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdGroupCurrentFeeCard {
  adGroup(id: "<adGroupId>") {
    id
    campaign {
      passThroughFeeCards(
        first: 5
        where: {
          ownerId: { eq: "<adGroupId>" }
          targetType: { eq: AD_GROUP }
        }
        order: [{ startDateUtc: DESC }]
      ) {
        nodes {
          id
          targetType
          target {
            ... on AdGroup {
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
}
```
