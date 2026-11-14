# GET /v3/campaignflight/{campaignFlightId} → CampaignFlight

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-campaignflight-campaignflightid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/campaignflight/{campaignFlightId} → CampaignFlight

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/campaignflight/{campaignFlightId}` |
| GraphQL query | `Query.campaign` |
| Return type | `CampaignFlight` |

There is no public top-level `Query.campaignFlight` by ID. Reach a flight by querying the parent campaign and filtering its `flights` connection.

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CampaignFlightId` | `flights.nodes.id` | ID! | Not nullable | Absent when `flights` is null. Filter `flights(where: { id: { eq: $flightId } })`. |
| `CampaignId` | `campaign.id` | String | Nullable | Parent campaign reference. |
| `StartDateInclusiveUTC` | `flights.nodes.startDateInclusiveUTC` | DateTime! | Not nullable | N/A |
| `EndDateExclusiveUTC` | `flights.nodes.endDateExclusiveUTC` | DateTime | Nullable | N/A |
| `BudgetInAdvertiserCurrency` | `flights.nodes.budgetInAdvertiserCurrency` | Decimal! | Not nullable | N/A |
| `BudgetInImpressions` | `flights.nodes.budgetInImpressions` | Long | Nullable | N/A |
| `DailyTargetInAdvertiserCurrency` | `flights.nodes.dailyTargetInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `DailyTargetInImpressions` | `flights.nodes.dailyTargetInImpressions` | Long | Nullable | N/A |

## Code examples

### REST example

```
GET /v3/campaignflight/{campaignFlightId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCampaignFlight($campaignId: ID!, $flightId: Long!) {
  campaign(id: $campaignId) {
    id
    flights(where: { id: { eq: $flightId } }, first: 1) {
      nodes {
        id
        campaign { id }
        startDateInclusiveUTC
        endDateExclusiveUTC
        budgetInAdvertiserCurrency
        budgetInImpressions
        dailyTargetInAdvertiserCurrency
        dailyTargetInImpressions
      }
    }
  }
}
```
