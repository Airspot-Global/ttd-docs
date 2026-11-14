# POST /v3/campaignflight → campaignFlightCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-campaignflight
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/campaignflight → campaignFlightCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/campaignflight` |
| GraphQL operation | `campaignFlightCreate` |
| Input type | `CampaignFlightCreateInput` |
| Output type | `PayloadWithErrorsOfCampaignFlight` (`data: CampaignFlight`, `userErrors: [UserError!]`) |

## Input field mapping

Input type: `CampaignFlightCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `campaignId` | ID! | Required | N/A |
| `StartDateInclusiveUTC` | `startDateInclusiveUTC` | DateTime! | Required | N/A |
| `EndDateExclusiveUTC` | `endDateExclusiveUTC` | DateTime | Optional | N/A |
| `BudgetInAdvertiserCurrency` | `budgetInAdvertiserCurrency` | Decimal! | Required | N/A |
| `BudgetInImpressions` | `budgetInImpressions` | Long | Optional | N/A |
| `DailyTargetInAdvertiserCurrency` | `dailyTargetInAdvertiserCurrency` | Decimal | Optional | N/A |
| `DailyTargetInImpressions` | `dailyTargetInImpressions` | Long | Optional | N/A |

## Output field mapping

Output type: `CampaignFlight` (returned as `data` on `CampaignFlightCreatePayload`)

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
POST /v3/campaignflight HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignId": "camp123",
  "StartDateInclusiveUTC": "2026-06-01T00:00:00Z",
  "EndDateExclusiveUTC": "2026-07-01T00:00:00Z",
  "BudgetInAdvertiserCurrency": 10000.00
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
  campaignFlightCreate(
    input: {
      campaignId: "camp123"
      startDateInclusiveUTC: "2026-06-01T00:00:00Z"
      endDateExclusiveUTC: "2026-07-01T00:00:00Z"
      budgetInAdvertiserCurrency: 10000.00
    }
  ) {
    data {
      id
      campaign { id }
      startDateInclusiveUTC
      endDateExclusiveUTC
      budgetInAdvertiserCurrency
    }
    userErrors {
      message
      field
    }
  }
}
```
