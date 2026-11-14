# PUT /v3/campaignflight → campaignFlightUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-campaignflight
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/campaignflight → campaignFlightUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/campaignflight` |
| GraphQL operation | `campaignFlightUpdate` |
| Input type | `CampaignFlightInput` |
| Output type | `PayloadWithErrorsOfCampaignFlight` (`data: CampaignFlight`, `userErrors: [UserError!]`) |

## Input field mapping

Input type: `CampaignFlightInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CampaignFlightId` | `campaignFlightId` | Long! | Required | N/A |
| `CampaignId` | `campaignId` | String | Optional | N/A |
| `StartDateInclusiveUTC` | `startDateInclusiveUTC` | DateTime | Optional | N/A |
| `EndDateExclusiveUTC` | `endDateExclusiveUTC` | DateTime | Optional | N/A |
| `BudgetInAdvertiserCurrency` | `budgetInAdvertiserCurrency` | Decimal | Optional | N/A |
| `BudgetInImpressions` | `budgetInImpressions` | Long | Optional | N/A |
| `DailyTargetInAdvertiserCurrency` | `dailyTargetInAdvertiserCurrency` | Decimal | Optional | N/A |
| `DailyTargetInImpressions` | `dailyTargetInImpressions` | Long | Optional | N/A |

## Output field mapping

Output type: `CampaignFlight` (returned as `data` on `CampaignFlightUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CampaignFlightId` | `id` | ID! | Not nullable | N/A |
| `CampaignId` | `campaign.id` | ID! | Not nullable | N/A |
| `StartDateInclusiveUTC` | `startDateInclusiveUTC` | DateTime! | Not nullable | N/A |
| `EndDateExclusiveUTC` | `endDateExclusiveUTC` | DateTime | Nullable | N/A |
| `BudgetInAdvertiserCurrency` | `budgetInAdvertiserCurrency` | Decimal! | Not nullable | N/A |
| `BudgetInImpressions` | `budgetInImpressions` | Long | Nullable | N/A |
| `DailyTargetInAdvertiserCurrency` | `dailyTargetInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `DailyTargetInImpressions` | `dailyTargetInImpressions` | Long | Nullable | N/A |

## Code examples

### REST example

```
PUT /v3/campaignflight HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignFlightId": 12345,
  "CampaignId": "camp123",
  "StartDateInclusiveUTC": "2026-06-15T00:00:00Z",
  "BudgetInAdvertiserCurrency": 15000.00
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
  campaignFlightUpdate(
    input: {
      campaignFlightId: 12345
      campaignId: "camp123"
      startDateInclusiveUTC: "2026-06-15T00:00:00Z"
      budgetInAdvertiserCurrency: 15000.00
    }
  ) {
    data {
      id
      campaign { id }
      startDateInclusiveUTC
      budgetInAdvertiserCurrency
    }
    userErrors {
      message
      field
    }
  }
}
```
