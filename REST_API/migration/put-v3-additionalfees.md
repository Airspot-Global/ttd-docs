# PUT /v3/additionalfees → additionalFeeCardUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-additionalfees
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/additionalfees → additionalFeeCardUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/additionalfees` |
| GraphQL operation | `additionalFeeCardUpdate` |
| Input type | `AdditionalFeeCardUpdateInput` |
| Output type | `AdditionalFeeCardUpdatePayload` (`data: AdditionalFeeCardUpdateResult`, `errors: [AdditionalFeeCardUpdateMutationError!]`) |

## Input field mapping

Input type: `AdditionalFeeCardUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `Fees` | `fees` | `[AdditionalFeeInput!]` | Required | N/A |
| `Fees[].Amount` | `amount` | `Decimal!` | Required | N/A |
| `Fees[].Description` | `description` | `String` | Optional | N/A |
| `Fees[].FeeType` | `feeType` | `AdditionalFeeTypeInput!` | Required | Input enum type is `AdditionalFeeTypeInput` (see nested enum table). |
| `OwnerId` | `ownerId` | `ID!` | Required | N/A |
| `OwnerType` | `ownerType` | `String!` | Required | REST serializes lowercase (`campaign`, `adgroup`, `advertiser`); GraphQL accepts the same string values. |
| `StartDateUtc` | `startDateUtc` | `DateTime!` | Required | N/A |

## Output field mapping

Output type: `AdditionalFeeCardUpdateResult` (returned as `data` on `AdditionalFeeCardUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Fees` | `fees` | `[AdditionalFeeUpdateResult!]!` | Not nullable | N/A |
| `Fees[].Amount` | `amount` | `Decimal!` | Not nullable | N/A |
| `Fees[].Description` | `description` | `String!` | Not nullable | REST allows a null description; the GraphQL response coerces null to an empty string, so callers cannot distinguish "no description" from "empty description". |
| `Fees[].FeeType` | `feeType` | `AdditionalFeeType!` | Not nullable | Output enum type is `AdditionalFeeType` (distinct from input `AdditionalFeeTypeInput`; see nested enum table). |
| `OwnerId` | `ownerId` | `ID` | Nullable | N/A |
| `OwnerType` | `ownerType` | `String` | Nullable | N/A |
| `StartDateUtc` | `startDate` | `DateTime!` | Not nullable | REST uses `StartDateUtc` on both request and response; the GraphQL **response** field is `startDate` (not `startDateUtc`). Use `startDateUtc` on input and read `startDate` on output. |

## Endpoint-specific nested types and enums

### AdditionalFeeTypeInput and AdditionalFeeType

REST serializes fee types as PascalCase strings in JSON. GraphQL uses separate enum types on input and output with SCREAMING_SNAKE_CASE members. All ten values exist on both sides.

| REST value (`FeeType`) | GraphQL input (`AdditionalFeeTypeInput`) | GraphQL output (`AdditionalFeeType`) |
| --- | --- | --- |
| `None` | `NONE` | `NONE` |
| `MediaCostPercentage` | `MEDIA_COST_PERCENTAGE` | `MEDIA_COST_PERCENTAGE` |
| `DataCostPercentage` | `DATA_COST_PERCENTAGE` | `DATA_COST_PERCENTAGE` |
| `MediaPlusDataCostPercentage` | `MEDIA_PLUS_DATA_COST_PERCENTAGE` | `MEDIA_PLUS_DATA_COST_PERCENTAGE` |
| `PartnerCostPercentage` | `PARTNER_COST_PERCENTAGE` | `PARTNER_COST_PERCENTAGE` |
| `PartnerDataCostPercentage` | `PARTNER_DATA_COST_PERCENTAGE` | `PARTNER_DATA_COST_PERCENTAGE` |
| `FeeCPM` | `FEE_CPM` | `FEE_CPM` |
| `RateCPM` | `RATE_CPM` | `RATE_CPM` |
| `RateCPC` | `RATE_CPC` | `RATE_CPC` |
| `CustomPMP_PartnerCostPercentage` | `CUSTOM_PMP_PARTNER_COST_PERCENTAGE` | `CUSTOM_PMP_PARTNER_COST_PERCENTAGE` |

## Code examples

### REST example

```
PUT /v3/additionalfees HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "OwnerId": "abc123",
  "OwnerType": "campaign",
  "StartDateUtc": "2026-07-29T12:00:00Z",
  "Fees": [
    {
      "Amount": 5.0,
      "Description": "Partner fee",
      "FeeType": "MediaCostPercentage"
    }
  ]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  additionalFeeCardUpdate(input: {
    ownerId: "abc123"
    ownerType: "campaign"
    startDateUtc: "2026-07-29T12:00:00Z"
    fees: [
      {
        amount: 5.0
        description: "Partner fee"
        feeType: MEDIA_COST_PERCENTAGE
      }
    ]
  }) {
    data {
      ownerId
      ownerType
      startDate
      fees {
        amount
        description
        feeType
      }
    }
    errors {
      ... on RestProxyMutationError {
        message
        field
      }
    }
  }
}
```
