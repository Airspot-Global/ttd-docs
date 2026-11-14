# POST /v3/activity/query/campaign → Campaign.activityLogs

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-activity-query-campaign
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/activity/query/campaign → Campaign.activityLogs

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/activity/query/campaign` |
| GraphQL query | `Campaign.activityLogs` |
| Return type | `ActivityLogsConnection` |

Here's what you need to know:

-

Primary GraphQL entry point is the parent relationship field `Campaign.activityLogs`

  - REST `POST /v3/activity/query/campaign` is scoped by `CampaignId`—the caller already holds the campaign ID.
  - Reach activity logs through `campaign(id: ...) { activityLogs { ... } }`.
  - When the client has only an entity ID string and no `Campaign` node in context, use the alternate root field `Query.activityLogs(entityType: CAMPAIGN, entityId:)` with the same `where`, `first`, and `after` arguments.

-

The `mode` argument on GraphQL `activityLogs` (`ActivityLogScopeModeInput`, optional)

  - Defaults to `INCLUDE_RELATED`: results include activity logs for the queried campaign and for related entities (for example, changes on its ad groups).
  - REST scopes results to the single campaign only.
  - To match REST's entity-only scope, pass `mode: SELECTED_ENTITY_ONLY`.
  - The other enum member is `INCLUDE_RELATED` (the default).

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageSize` | `first` | `Int` | Optional | N/A |
| `PageStartIndex` | `after` | `String` | Optional | N/A |
| `CampaignId` | N/A | N/A | Required | Not currently available in GraphQL |
| `DateTimeEndUtc` | `where.occurredAt.lte` | `DateTime` | Optional | N/A |
| `DateTimeStartUtc` | `where.occurredAt.gte` | `DateTime` | Required | N/A |
| `IncludeBidLineDetails` | N/A | N/A | Optional | Not currently available in GraphQL |
| `Source` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UpdatedBy` | `where.actor.in` | `[String]` | Optional | Single username maps to a one-element `actor.in` list |
| `UpdatedIn` | `where.categoryAndDetail.in[].category` | `ActivityCategoryInput!` | Optional | Remodelled in GraphQL |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[ActivityLog!]` | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | `Int!` | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].ActivityRollupTimeUtc` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].ActivityTimeUtc` | `occurredAt` | `DateTime!` | Not nullable | N/A |
| `Result[].BidLineChanges` | `details` | `ActivityDetails` | Nullable | Remodelled in GraphQL |
| `Result[].Entity` | `category` | `ActivityCategory!` | Not nullable | Remodelled in GraphQL |
| `Result[].HasBidListChanges` | N/A | N/A | N/A | Derive client-side: `true` when `category == BID_LIST` and `details { ... on BidListChangeDetails { changeCount } }` returns `changeCount > 0`; no boolean field exists |
| `Result[].Id` | `id` | `ID!` | Not nullable | Opaque GraphQL ID—not the REST numeric `long` |
| `Result[].Message` | `message` | `String` | Nullable | N/A |
| `Result[].ModifiedByUser` | `actor` | `String` | Nullable | N/A |
| `Result[].Note` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].OwnerAdGroupId` | `affectedEntities` | `[ActivityLogAffectedEntity!]!` | Not nullable | Read `affectedEntities { type entityId }` where `type == AD_GROUP` and use `entityId` |
| `Result[].OwnerCampaignId` | `affectedEntities` | `[ActivityLogAffectedEntity!]!` | Not nullable | Read `affectedEntities { type entityId }` where `type == CAMPAIGN` and use `entityId` |
| `Result[].Source` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

### ActivityLogAffectedEntity

Select `affectedEntities { type entityId node { ... } }` on each `ActivityLog` node.

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
POST /v3/activity/query/campaign HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignId": "cmp123",
  "DateTimeStartUtc": "2026-01-01T00:00:00Z",
  "DateTimeEndUtc": "2026-07-28T23:59:59Z",
  "PageSize": 100,
  "PageStartIndex": 0,
  "UpdatedBy": "jane.doe@example.com"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CampaignActivityLogs {
  campaign(id: "cmp123") {
    activityLogs(
      first: 100
      where: {
        occurredAt: {
          gte: "2026-01-01T00:00:00Z"
          lte: "2026-07-28T23:59:59Z"
        }
        actor: { in: ["jane.doe@example.com"] }
        categoryAndDetail: {
          in: [{ category: BID_LIST }]
        }
      }
    ) {
      nodes {
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
            changeCount
            dimensionName
            bidList {
              id
            }
          }
        }
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

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ActivityLogsByCampaignId {
  activityLogs(
    entityType: CAMPAIGN
    entityId: "cmp123"
    first: 100
    where: {
      occurredAt: { gte: "2026-01-01T00:00:00Z" }
    }
  ) {
    nodes {
      id
      occurredAt
      actor
      category
      message
    }
    totalCount
  }
}
```
