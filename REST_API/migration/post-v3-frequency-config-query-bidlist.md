# POST /v3/frequency/config/query/bidlist → BidList.frequencyConfigs

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-frequency-config-query-bidlist
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/frequency/config/query/bidlist → BidList.frequencyConfigs

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/frequency/config/query/bidlist` |
| GraphQL query | `BidList.frequencyConfigs` |
| Return type | `FrequencyConfigsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `BidListIds` | Parent `BidList.id` on the relationship field | N/A | Required | Parent entity ID is sent as the sole BidListIds entry per request key. |

## Response field mapping

 | REST response field | GraphQL field | GraphQL type | Nullable | Notes | |---------------------|---------------|--------------|----------|-------| | `Result` | `nodes` | `[FrequencyConfig!]` | Nullable | N/A | | `ResultCount` | N/A | N/A | N/A | N/A | | `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A | | `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

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

### REST example

```
POST /v3/frequency/config/query/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 10,
  "BidListIds": ["<bid-list-id>"]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query BidListFrequencyConfigs {
  bidList(id: "<bid-list-id>") {
    id
    ... on BidList {
      frequencyConfigs(first: 10) {
        nodes {
          counter {
            id
          }
        }
        totalCount
      }
    }
  }
}
```
