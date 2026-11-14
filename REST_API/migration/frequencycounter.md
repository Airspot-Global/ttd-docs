# Frequency counter: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/frequencycounter-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Frequency counter: REST → GraphQL migration guide

GraphQL nests owner IDs under `owner`, renames `CounterName` to `name`, uses `id` instead of `counterId`, and does not expose `FCapCrossDspGroupId` on the counter type.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/frequency/counter` | `frequencyCounterCreate` | `owner` required; `name` required in GraphQL |
| `PUT /v3/frequency/counter` | `frequencyCounterUpdate` | `id` required; owner fields are immutable |

## Shared nested types and enums

### FrequencyCounterOwnerInput (create)

REST sends flat `AdvertiserId` and/or `PartnerId`. GraphQL nests them under `owner` on `FrequencyCounterCreateInput`.

| REST field | GraphQL `owner` object |
| --- | --- |
| AdvertiserId: "adv123" | { `advertiserId`: "adv123" } |
| PartnerId: "prt123" | { `partnerId`: "prt123" } |
| Both provided | { `advertiserId`: "adv123", `partnerId`: "prt123" } |

At least one of `advertiserId` or `partnerId` must be set on create.

### FrequencyCounter (mutation response `data`)

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `id` | ID! | Not nullable | Maps from REST `CounterId` |
| `name` | String! | Not nullable | Maps from REST `CounterName` |
| `resetIntervalInMinutes` | Int! | Not nullable | N/A |
| `isCustomName` | Boolean! | Not nullable | Maps from REST `IsCustomName` |
| `counterAttribute` | FrequencyCounterSpecialType! | Not nullable | Maps from REST `CounterAttribute` |
| `owner` | FrequencyCounterOwner | Nullable | Union of `Advertiser`, `Partner` |
| `isDeleted` | Boolean! | Not nullable | N/A |
| `frequencyCounterIncrementors` | [FrequencyCounterIncrementor!]! | Not nullable | N/A |

### FrequencyCounterSpecialTypeInput (create / update input)

Maps REST `CounterAttribute` string enum values to GraphQL enum members on `counterAttributeInput`.

| REST CounterAttribute | GraphQL FrequencyCounterSpecialTypeInput |
| --- | --- |
| None | NONE |
| AllowUIGroupConfiguration | UI_GROUP |
| RestrictedFrequencyGroup | RESTRICTED_FREQUENCY_GROUP |
| RestrictedCampaignInterval | RESTRICTED_CAMPAIGN_INTERVAL |
| RestrictedCampaignLifetime | RESTRICTED_CAMPAIGN_LIFETIME |
| CrossDSP | CROSS_DSP |

### FrequencyCounterCreateMutationError / FrequencyCounterUpdateMutationError

Union members: `FrequencyCounterValidationError`, `FrequencyCounterMutationError`, `FrequencyCounterInternalExceptionError`. Use inline fragments in mutation payloads (for example `... on FrequencyCounterValidationError { message field }`).
