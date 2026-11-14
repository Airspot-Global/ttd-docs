# PUT /v3/frequency/counter → frequencyCounterUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-frequency-counter
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/frequency/counter → frequencyCounterUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/frequency/counter` |
| GraphQL operation | `frequencyCounterUpdate` |
| Input type | `FrequencyCounterUpdateInput` |
| Output type | `FrequencyCounterUpdatePayload` (`data: FrequencyCounter`, `errors: [FrequencyCounterUpdateMutationError!]`) |

## Input field mapping

Input type: `FrequencyCounterUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CounterId` | `id` | ID! | Required | N/A |
| `AdvertiserId` | N/A | N/A | Optional | **Read-only** |
| `PartnerId` | N/A | N/A | Optional | **Read-only** |
| `FCapCrossDspGroupId` | N/A | N/A | Optional | **Not currently available in GraphQL** |
| `ResetIntervalInMinutes` | `resetIntervalInMinutes` | Int | Optional | Must be greater than 0 when provided |
| `CounterName` | `name` | String | Optional | N/A |
| `IsCustomName` | N/A | N/A | Optional | **Read-only** |
| `CounterAttribute` | `counterAttributeInput` | FrequencyCounterSpecialTypeInput | Optional | See domain page for enum mapping |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `incrementorsToAdd` | FrequencyCounterIncrementorsInput | Adds incrementors to the counter |
| `incrementorsToRemove` | FrequencyCounterIncrementorsInput | Removes incrementors from the counter |

## Output field mapping

Output type: `FrequencyCounter` (returned as `data` on `FrequencyCounterUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CounterId` | `id` | ID! | Not nullable | N/A |
| `AdvertiserId` | owner … on Advertiser { id } | ID | Nullable | Present when `owner` resolves to `Advertiser` |
| `PartnerId` | owner … on Partner { id } | ID | Nullable | Present when `owner` resolves to `Partner` |
| `FCapCrossDspGroupId` | N/A | N/A | N/A | Not returned on `FrequencyCounter` |
| `ResetIntervalInMinutes` | `resetIntervalInMinutes` | Int! | Not nullable | N/A |
| `CounterName` | `name` | String! | Not nullable | N/A |
| `IsCustomName` | `isCustomName` | Boolean! | Not nullable | N/A |
| `CounterAttribute` | `counterAttribute` | FrequencyCounterSpecialType! | Not nullable | N/A |

## Code examples

### REST example

```
PUT /v3/frequency/counter HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CounterId": "fc456",
  "ResetIntervalInMinutes": 720
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation UpdateFrequencyCounter {
  frequencyCounterUpdate(input: {
    id: "fc456"
    resetIntervalInMinutes: 720
  }) {
    data {
      id
      resetIntervalInMinutes
      name
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
