# POST /v3/frequency/config/query → Partner.frequencyConfigs / Advertiser.frequencyConfigs / AdGroup.frequencyConfigs

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-frequency-config-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/frequency/config/query → Partner.frequencyConfigs / Advertiser.frequencyConfigs / AdGroup.frequencyConfigs

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/frequency/config/query` |
| GraphQL query | `Partner.frequencyConfigs`, `Advertiser.frequencyConfigs`, `AdGroup.frequencyConfigs` |
| Return type | `FrequencyConfigsConnection` |

Campaign not supported (`Campaign.frequencyConfigs` name collision—use Advertiser, Partner, or AdGroup instead).

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `EntityType` | Drives parent type (`Partner` \| `Advertiser` \| `AdGroup`) | N/A | Required | Selects which relationship field hosts the connection (`Partner.frequencyConfigs`, `Advertiser.frequencyConfigs`, or `AdGroup.frequencyConfigs`). Not implemented on Campaign. |
| `EntityId` | Parent entity `id` on the chosen relationship field | N/A | Required | REST body EntityId equals the parent entity ID. |
| `OutputDetailLevel` | Input `FrequencyConfigByEntityInput.includeAncestors`, `includeDescendants` | Boolean | Optional | REST flags enum split into two optional booleans. Omit both (or false) = entity-only (REST default). Set one or both true to match IncludeAncestors, IncludeDescendants, or their combination. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[FrequencyConfig!]` | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

### FrequencyConfig node (each `nodes` element)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Counter` | `counter` | FrequencyCounter! | Not nullable | Nested counter on the config payload. |
| `Counter.CounterId` | `counter.id` | ID! | Not nullable | CounterId → `id`. |
| `Counter.AdvertiserId` | `counter.owner` | FrequencyCounterOwner | Nullable | REST advertiser ID maps to the counter owner union. |
| `Counter.PartnerId` | `counter.owner` | FrequencyCounterOwner | Nullable | REST partner ID maps to the counter owner union. |
| `Counter.FCapCrossDspGroupId` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `Counter.ResetIntervalInMinutes` | `counter.resetIntervalInMinutes` | Int! | Not nullable | N/A |
| `Counter.CounterName` | `counter.name` | String! | Not nullable | CounterName → name. |
| `Counter.IsCustomName` | `counter.isCustomName` | Boolean! | Not nullable | N/A |
| `Counter.CounterAttribute` | `counter.counterAttribute` | FrequencyCounterSpecialType! | Not nullable | N/A |
| `Increments` | `increments` | FrequencyConfigIncrements! | Not nullable | N/A |
| `Increments.AdGroups` | `increments.adGroups` | [AdGroup!]! | Not nullable | REST ID list → entity references with ID. |
| `Increments.Campaigns` | `increments.campaigns` | [Campaign!]! | Not nullable | REST ID list → entity references with ID. |
| `Increments.Advertisers` | `increments.advertisers` | [Advertiser!]! | Not nullable | REST ID list → entity references with ID. |
| `Increments.Partners` | N/A | N/A | N/A | `FrequencyConfigIncrements` has no `partners` field in GraphQL. |
| `BidLists` | `bidLists` | [IBidList!]! | Not nullable | N/A |
| `BidLists.BidListId` | `bidLists.id` | ID! | Not nullable | BidListId → `id`. |
| `BidLists.Name` | `bidLists.name` | String! | Not nullable | N/A |
| `BidLists.BidListOwner` | `bidLists.ownerType` | BidListOwnerType! | Not nullable | REST owner enum → `ownerType`. |
| `BidLists.BidListOwnerId` | `bidLists.owner` | BidListOwner | Nullable | REST flat owner ID → nested `BidListOwner` union. |
| `BidLists.NumberOfBidLines` | `bidLists.bidLinesCount` | Int! | Not nullable | NumberOfBidLines → `bidLinesCount`. |
| `BidLists.BidListAdjustmentType` | `bidLists.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `BidLists.AssociatedAdGroups` | `bidLists.appliedAdGroups` | BidListAppliedAdGroupsConnection | Nullable | AssociatedAdGroups → `appliedAdGroups` connection (`nodes` hold ad group refs). |
| `BidLists.AssociatedCampaigns` | N/A | N/A | N/A | `IBidList` exposes `appliedAdGroups` only; no campaign association field. |
| `BidLists.AssociatedAdvertisers` | N/A | N/A | N/A | `IBidList` exposes `appliedAdGroups` only; no advertiser association field. |
| `BidLists.AssociatedPartners` | N/A | N/A | N/A | `IBidList` exposes `appliedAdGroups` only; no partner association field. |
| `BidLists.BidLines` | `bidLists.bidLines` | [BidLine!]! | Not nullable | N/A |
| `BidLists.BidLines.Range` | `bidLists.bidLines.frequencyAdjustment.timesShown` | RangeOfInt32 | Nullable | REST range min/max → `frequencyAdjustment.timesShown` on `BidLine`. |
| `BidLists.BidLines.Range.Min` | `bidLists.bidLines.frequencyAdjustment.timesShown.min` | Int | Nullable | N/A |
| `BidLists.BidLines.Range.Max` | `bidLists.bidLines.frequencyAdjustment.timesShown.max` | Int | Nullable | N/A |
| `BidLists.BidLines.VolumeControlPriority` | `bidLists.bidLines.volumeControlPriority` | VolumeControlPriority! | Not nullable | N/A |
| `BidLists.BidLines.BidAdjustment` | `bidLists.bidLines.bidAdjustment` | Decimal! | Not nullable | N/A |
| `BidLists.BidListSource` | `bidLists.source` | BidListSource! | Not nullable | N/A |
| `IncrementByAllEntitiesAssociatedWithBidLists` | `incrementByAllEntitiesAssociatedWithBidLists` | Boolean | Nullable | N/A |

## Code examples

The following are examples of querying frequency configs on an advertiser—a paged list and a detail-level filter with ancestors and descendants.

### REST example

```
POST /v3/frequency/config/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 10,
  "EntityType": "Advertiser",
  "EntityId": "<advertiser-id>"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserFrequencyConfigs {
  advertiser(id: "<advertiser-id>") {
    id
    frequencyConfigs(first: 10) {
      nodes {
        incrementByAllEntitiesAssociatedWithBidLists
        counter {
          id
          resetIntervalInMinutes
        }
      }
      totalCount
    }
  }
}
```

To include ancestor and descendant configs, set `OutputDetailLevel` on the REST request (or use `includeAncestors` and `includeDescendants` in the GraphQL filter).

### REST example

```
POST /v3/frequency/config/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 10,
  "EntityType": "Advertiser",
  "EntityId": "<advertiser-id>",
  "OutputDetailLevel": "IncludeAncestors | IncludeDescendants"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserFrequencyConfigsWithDetailLevel {
  advertiser(id: "<advertiser-id>") {
    id
    frequencyConfigs(
      first: 10
      filter: { includeAncestors: true, includeDescendants: true }
    ) {
      nodes {
        counter {
          id
        }
      }
      totalCount
    }
  }
}
```
