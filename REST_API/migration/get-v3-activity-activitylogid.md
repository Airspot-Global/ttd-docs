# GET /v3/activity/{activityLogId} → Query.activityLog

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-activity-activitylogid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/activity/{activityLogId} → Query.activityLog

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/activity/{activityLogId}` |
| GraphQL query | `Query.activityLog` |
| Return type | `ActivityLog` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `activityLogId` | `id` | `ID!` | Required | REST numeric path ID → opaque GraphQL ID; do not cast or derive IDs across APIs |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ActivityRollupTimeUtc` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ActivityTimeUtc` | `occurredAt` | `DateTime!` | Not nullable | N/A |
| `BidLineChanges` | `details` | `ActivityDetails` | Nullable | Remodelled in GraphQL |
| `Entity` | `category` | `ActivityCategory!` | Not nullable | Remodelled in GraphQL |
| `HasBidListChanges` | N/A | N/A | N/A | Derive client-side: `true` when `category == BID_LIST` and `details { ... on BidListChangeDetails { changeCount } }` returns `changeCount > 0`; no boolean field exists |
| `Id` | `id` | `ID!` | Not nullable | Opaque GraphQL ID—not the REST numeric `long` |
| `Message` | `message` | `String` | Nullable | N/A |
| `ModifiedByUser` | `actor` | `String` | Nullable | N/A |
| `Note` | N/A | N/A | N/A | Not currently available in GraphQL |
| `OwnerAdGroupId` | `affectedEntities` | `[ActivityLogAffectedEntity!]!` | Not nullable | Read `affectedEntities { type entityId }` where `type == AD_GROUP` and use `entityId` |
| `OwnerCampaignId` | `affectedEntities` | `[ActivityLogAffectedEntity!]!` | Not nullable | Read `affectedEntities { type entityId }` where `type == CAMPAIGN` and use `entityId` |
| `Source` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

### ActivityLogAffectedEntity

Select `affectedEntities { type entityId node { ... } }` on each `ActivityLog` entry.

| REST field / concept | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `OwnerAdGroupId` / `OwnerCampaignId` (see main table) | `entityId` | `ID!` | Not nullable | Platform ID of the affected entity; filter by `type` to pick the required owner |
| N/A | `node` | `AffectedEntityNode` | Nullable | Reference for resolving the affected entity's name and other fields from its owning type |
| N/A | `type` | `ActivityLogEntity!` | Not nullable | Entity kind discriminator (`AD_GROUP`, `CAMPAIGN`, and others) |

### BidLineActivity → BidListChangeDetails

When `category` is `BID_LIST`, select `details { ... on BidListChangeDetails { bidList changeCount dimensionName } }`.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidDimensionId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BidDimensionType` | `dimensionName` | `String` | Nullable | Remodelled in GraphQL |
| `ChangeTimeUtc` | `ActivityLog.occurredAt` | `DateTime!` | Not nullable | Remodelled in GraphQL |
| `Id` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Name` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Op` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ValueFrom` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ValueTo` | N/A | N/A | N/A | Not currently available in GraphQL |
| `VolumeControlValueFrom` | N/A | N/A | N/A | Not currently available in GraphQL |
| `VolumeControlValueTo` | N/A | N/A | N/A | Not currently available in GraphQL |

## Code examples

### REST example

```
GET /v3/activity/{activityLogId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ActivityLogById {
  activityLog(id: "opaque-activity-log-id-from-graphql") {
    id
    occurredAt
    actor
    message
    category
    affectedEntities {
      type
      entityId
    }
    details {
      ... on BidListChangeDetails {
        bidList {
          id
        }
        changeCount
        dimensionName
      }
    }
  }
}
```
