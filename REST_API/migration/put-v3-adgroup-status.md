# PUT /v3/adgroup/status → adGroupUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-adgroup-status
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/adgroup/status → adGroupUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/adgroup/status` |
| GraphQL operation | `adGroupUpdate` |
| Input type | `AdGroupUpdateInput` |
| Output type | `PayloadWithErrorsOfAdGroup` (`data: AdGroup`, `userErrors: [UserError!]!`) |

## Input field mapping

Input type: `AdGroupUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Required | N/A |
| `IsEnabled` | `isEnabled` | Boolean | Optional | N/A |

## Output field mapping

Output type: `AdGroup` (returned as `data` on `PayloadWithErrorsOfAdGroup`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Not nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |

## Code examples

### Example—PUT status

### REST example

```
PUT /v3/adgroup/status HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdGroupId": "ag_xyz789",
  "IsEnabled": true
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation EnableAdGroup {
  adGroupUpdate(input: {
    id: "ag_xyz789"
    isEnabled: true
  }) {
    data {
      id
      isEnabled
    }
    userErrors {
      message
      field
    }
  }
}
```
