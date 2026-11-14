# GET /v3/frequency/config/{counterId} → FrequencyCounter.frequencyConfig

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-frequency-config-counterid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/frequency/config/{counterId} → FrequencyCounter.frequencyConfig

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/frequency/config/{counterId}` |
| GraphQL query | `FrequencyCounter.frequencyConfig` |
| Return type | `FrequencyConfig` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| counterId (path) | Parent `FrequencyCounter.id` | ID! | Required | REST path parameter identifies the counter whose config is loaded. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Counter` | `frequencyConfig.counter` | FrequencyCounter! | Not nullable | Nested counter on the config payload. |
| `Counter.CounterId` | `frequencyConfig.counter.id` | ID! | Not nullable | CounterId → `id`. |
| `Counter.AdvertiserId` | `frequencyConfig.counter.owner` | FrequencyCounterOwner | Nullable | REST advertiser ID maps to the counter owner union. |
| `Counter.PartnerId` | `frequencyConfig.counter.owner` | FrequencyCounterOwner | Nullable | REST partner ID maps to the counter owner union. |
| `Counter.FCapCrossDspGroupId` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `Counter.ResetIntervalInMinutes` | `frequencyConfig.counter.resetIntervalInMinutes` | Int! | Not nullable | N/A |
| `Counter.CounterName` | `frequencyConfig.counter.name` | String! | Not nullable | CounterName → name. |
| `Counter.IsCustomName` | `frequencyConfig.counter.isCustomName` | Boolean! | Not nullable | N/A |
| `Counter.CounterAttribute` | `frequencyConfig.counter.counterAttribute` | FrequencyCounterSpecialType! | Not nullable | N/A |
| `Increments` | `frequencyConfig.increments` | FrequencyConfigIncrements! | Not nullable | N/A |
| `Increments.AdGroups` | `frequencyConfig.increments.adGroups` | [AdGroup!]! | Not nullable | REST ID list → entity references with ID. |
| `Increments.Campaigns` | `frequencyConfig.increments.campaigns` | [Campaign!]! | Not nullable | REST ID list → entity references with ID. |
| `Increments.Advertisers` | `frequencyConfig.increments.advertisers` | [Advertiser!]! | Not nullable | REST ID list → entity references with ID. |
| `Increments.Partners` | N/A | N/A | N/A | `FrequencyConfigIncrements` has no `partners` field in GraphQL. |
| `BidLists` | `frequencyConfig.bidLists` | [IBidList!]! | Not nullable | N/A |
| `BidLists.BidListId` | `frequencyConfig.bidLists.id` | ID! | Not nullable | BidListId → `id`. |
| `BidLists.Name` | `frequencyConfig.bidLists.name` | String! | Not nullable | N/A |
| `BidLists.BidListOwner` | `frequencyConfig.bidLists.ownerType` | BidListOwnerType! | Not nullable | REST owner enum → `ownerType`. |
| `BidLists.BidListOwnerId` | `frequencyConfig.bidLists.owner` | BidListOwner | Nullable | REST flat owner ID → nested `BidListOwner` union. |
| `BidLists.NumberOfBidLines` | `frequencyConfig.bidLists.bidLinesCount` | Int! | Not nullable | NumberOfBidLines → `bidLinesCount`. |
| `BidLists.BidListAdjustmentType` | `frequencyConfig.bidLists.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `BidLists.AssociatedAdGroups` | `frequencyConfig.bidLists.appliedAdGroups` | BidListAppliedAdGroupsConnection | Nullable | AssociatedAdGroups → `appliedAdGroups` connection (`nodes` hold ad group refs). |
| `BidLists.AssociatedCampaigns` | N/A | N/A | N/A | `IBidList` exposes `appliedAdGroups` only; no campaign association field. |
| `BidLists.AssociatedAdvertisers` | N/A | N/A | N/A | `IBidList` exposes `appliedAdGroups` only; no advertiser association field. |
| `BidLists.AssociatedPartners` | N/A | N/A | N/A | `IBidList` exposes `appliedAdGroups` only; no partner association field. |
| `BidLists.BidLines` | `frequencyConfig.bidLists.bidLines` | [BidLine!]! | Not nullable | N/A |
| `BidLists.BidLines.Range` | `frequencyConfig.bidLists.bidLines.frequencyAdjustment.timesShown` | RangeOfInt32 | Nullable | REST range min/max → `frequencyAdjustment.timesShown` on `BidLine`. |
| `BidLists.BidLines.Range.Min` | `frequencyConfig.bidLists.bidLines.frequencyAdjustment.timesShown.min` | Int | Nullable | N/A |
| `BidLists.BidLines.Range.Max` | `frequencyConfig.bidLists.bidLines.frequencyAdjustment.timesShown.max` | Int | Nullable | N/A |
| `BidLists.BidLines.VolumeControlPriority` | `frequencyConfig.bidLists.bidLines.volumeControlPriority` | VolumeControlPriority! | Not nullable | N/A |
| `BidLists.BidLines.BidAdjustment` | `frequencyConfig.bidLists.bidLines.bidAdjustment` | Decimal! | Not nullable | N/A |
| `BidLists.BidListSource` | `frequencyConfig.bidLists.source` | BidListSource! | Not nullable | N/A |
| `IncrementByAllEntitiesAssociatedWithBidLists` | `frequencyConfig.incrementByAllEntitiesAssociatedWithBidLists` | Boolean | Nullable | Type extension on FrequencyConfig. |

## Code examples

### REST example

```
GET /v3/frequency/config/{counterId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query FrequencyConfigByCounter {
  advertiser(id: "<advertiser-id>") {
    frequencyCounters(first: 10) {
      nodes {
        id
        frequencyConfig {
          incrementByAllEntitiesAssociatedWithBidLists
          increments {
            advertisers {
              id
            }
          }
          counter {
            id
            resetIntervalInMinutes
          }
        }
      }
    }
  }
}
```
