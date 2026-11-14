# GET /v3/campaign/name/{campaignId} → Campaign

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-campaign-name-campaignid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/campaign/name/{campaignId} → Campaign

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/campaign/name/{campaignId}` |
| GraphQL query | `Campaign` (via entity lookup by `id`) |
| Return type | `Campaign` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | REST `IdName.Id`—query `Campaign` by ID. |
| `Name` | `name` | String! | Not nullable | REST `IdName.Name`. |

## Code examples

### REST example

```
GET /v3/campaign/name/{campaignId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCampaignName($id: ID!) {
  campaign(id: $id) {
    id
    name
  }
}
```
