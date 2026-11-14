# POST /v3/frequency/counter → frequencyCounterCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-frequency-counter
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/frequency/counter → frequencyCounterCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/frequency/counter` |
| GraphQL operation | `frequencyCounterCreate` |
| Input type | `FrequencyCounterCreateInput` |
| Output type | `FrequencyCounterCreatePayload` (`data: FrequencyCounter`, `errors: [FrequencyCounterCreateMutationError!]`) |

## Input field mapping

Input type: `FrequencyCounterCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CounterId` | N/A | N/A | Optional | Ignored on create; no GraphQL input |
| `AdvertiserId` | `owner.advertiserId` | ID | Optional | **Read-only** |
| `PartnerId` | `owner.partnerId` | ID | Optional | Required on create when no `advertiserId` |
| `FCapCrossDspGroupId` | `owner.fCapCrossDspGroupId` | ID | Optional | Required on create when neither `advertiserId` nor `partnerId` is set; exactly one of `advertiserId`, `partnerId`, or `fCapCrossDspGroupId` on `FrequencyCounterOwnerInput` |
| `ResetIntervalInMinutes` | `resetIntervalInMinutes` | Int! | Required | Must be greater than 0 |
| `CounterName` | `name` | String! | Required | Required in GraphQL; optional in REST |
| `IsCustomName` | N/A | N/A | Optional | **Read-only** |
| `CounterAttribute` | `counterAttributeInput` | FrequencyCounterSpecialTypeInput | Optional | Prefer over deprecated `counterAttribute`; see domain page for enum mapping |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `incrementors` | FrequencyCounterIncrementorsInput | Optional ad group, campaign, advertiser, or partner IDs to set as incrementors on create |

## Output field mapping

Output type: `FrequencyCounter` (returned as `data` on `FrequencyCounterCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CounterId` | `id` | ID! | Not nullable | N/A |
| `AdvertiserId` | owner … on Advertiser { id } | ID | Nullable | Present when `owner` resolves to `Advertiser` |
| `PartnerId` | owner … on Partner { id } | ID | Nullable | Present when `owner` resolves to `Partner` |
| `FCapCrossDspGroupId` | owner … on FCapCrossDspGroup { id } | ID | Nullable | Present when `owner` resolves to `FCapCrossDspGroup` |
| `ResetIntervalInMinutes` | `resetIntervalInMinutes` | Int! | Not nullable | N/A |
| `CounterName` | `name` | String! | Not nullable | N/A |
| `IsCustomName` | `isCustomName` | Boolean! | Not nullable | N/A |
| `CounterAttribute` | `counterAttribute` | FrequencyCounterSpecialType! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/frequency/counter HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv123",
  "ResetIntervalInMinutes": 1440,
  "CounterName": "DailyCap"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation CreateFrequencyCounter {
  frequencyCounterCreate(input: {
    owner: { advertiserId: "adv123" }
    name: "DailyCap"
    resetIntervalInMinutes: 1440
  }) {
    data {
      id
      name
      resetIntervalInMinutes
      isCustomName
      counterAttribute
    }
    errors {
      ... on FrequencyCounterValidationError {
        message
        field
      }
      ... on FrequencyCounterMutationError {
        message
        field
      }
    }
  }
}
```
