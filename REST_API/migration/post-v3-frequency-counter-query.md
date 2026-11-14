# POST /v3/frequency/counter/query → Advertiser.frequencyCounters / Partner.frequencyCounters

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-frequency-counter-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/frequency/counter/query → Advertiser.frequencyCounters / Partner.frequencyCounters

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/frequency/counter/query` |
| GraphQL query | `Advertiser.frequencyCounters`, `Partner.frequencyCounters` |
| Return type | `FrequencyCountersConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `EntityType` | Drives parent (`Advertiser` default \| `Partner`) | N/A | Optional | Selects `Advertiser.frequencyCounters` or `Partner.frequencyCounters`. Default REST Advertiser when omitted. |
| `EntityId` | Parent: `Advertiser.frequencyCounters` \| `Partner.frequencyCounters` | N/A | Required | Lists FrequencyCounter stubs for the owning entity. |

## Response field mapping

 | REST response field | GraphQL field | GraphQL type | Nullable | Notes | |---------------------|---------------|--------------|----------|-------| | `Result` | `nodes` | `[FrequencyCounter!]` | Nullable | N/A | | `ResultCount` | N/A | N/A | N/A | N/A | | `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A | | `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

### FrequencyCounter node (each `nodes` element)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CounterId` | `id` | ID! | Not nullable | CounterId → `id`. |
| `AdvertiserId` | `owner` | FrequencyCounterOwner | Nullable | REST advertiser ID maps to the counter owner union (`... on Advertiser { id }`). |
| `PartnerId` | `owner` | FrequencyCounterOwner | Nullable | REST partner ID maps to the counter owner union (`... on Partner { id }`). |
| `FCapCrossDspGroupId` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `ResetIntervalInMinutes` | `resetIntervalInMinutes` | Int! | Not nullable | N/A |
| `CounterName` | `name` | String! | Not nullable | CounterName → name. |
| `IsCustomName` | `isCustomName` | Boolean! | Not nullable | N/A |
| `CounterAttribute` | `counterAttribute` | FrequencyCounterSpecialType! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/frequency/counter/query HTTP/1.1
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
query AdvertiserFrequencyCounters {
  advertiser(id: "<advertiser-id>") {
    id
    frequencyCounters(first: 10) {
      nodes {
        id
        name
        resetIntervalInMinutes
      }
      totalCount
    }
  }
}
```
