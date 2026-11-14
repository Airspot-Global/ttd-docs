# DELETE /v3/campaignflight/{campaignFlightId} → campaignFlightDelete

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/delete-v3-campaignflight-campaignflightid
- Retrieved: 2026-11-14
- Category: REST_API

---

# DELETE /v3/campaignflight/{campaignFlightId} → campaignFlightDelete

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `DELETE /v3/campaignflight/{campaignFlightId}` |
| GraphQL operation | `campaignFlightDelete` |
| Input type | `CampaignFlightDeleteInput` |
| Output type | `PayloadWithErrorsOfCampaignFlightDeleteReturn` (`data: CampaignFlightDeleteReturn`, `userErrors: [UserError!]`) |

## Input field mapping

Input type: `CampaignFlightDeleteInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `campaignFlightId` | `campaignFlightId` | Long! | Required | Path parameter |

## Output field mapping

Output type: `CampaignFlightDeleteReturn` (returned as `data` on `CampaignFlightDeletePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| N/A | `wasSuccessfullyDeleted` | Boolean! | Not nullable | REST returns empty body on success |

## Code examples

### REST example

```
DELETE /v3/campaignflight/12345 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  campaignFlightDelete(
    input: {
      campaignFlightId: 12345
    }
  ) {
    data {
      wasSuccessfullyDeleted
    }
    userErrors {
      message
      field
    }
  }
}
```
