# GET /v3/frequency/counter/{counterId} → FrequencyCounter

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-frequency-counter-counterid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/frequency/counter/{counterId} → FrequencyCounter

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/frequency/counter/{counterId}` |
| GraphQL query | `FrequencyCounter` (entity resolution by ID) |
| Return type | `FrequencyCounter` |

## Multi-step operations

Use GraphQL `Query.frequencyCounter(id:)` to load a frequency counter by ID.

| REST endpoint | GraphQL equivalent | Notes |
| --- | --- | --- |
| `GET /v3/frequency/counter/{counterId}` | Resolve `FrequencyCounter` by ID | GraphQL read; counter fields (name, `resetIntervalInMinutes`, owner, etc.) are available on the entity. |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| counterId (path) | `FrequencyCounter.id` | ID! | Required | Path parameter maps to the entity ID. |

## Response field mapping

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

For the full frequency configuration payload (increments, bid lists, etc.), use `FrequencyCounter.frequencyConfig` (see GET /v3/frequency/config/{counterId}).

## Code examples

### REST example

```
GET /v3/frequency/counter/{counterId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query FrequencyCounterByOwner {
  advertiser(id: "<advertiser-id>") {
    frequencyCounters(first: 10) {
      nodes {
        id
        name
        resetIntervalInMinutes
        isCustomName
        counterAttribute
        owner {
          __typename
          ... on Advertiser { id }
          ... on Partner { id }
        }
      }
    }
  }
}
```
