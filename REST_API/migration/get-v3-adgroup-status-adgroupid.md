# GET /v3/adgroup/status/{adGroupId} → AdGroup.status

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-adgroup-status-adgroupid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/adgroup/status/{adGroupId} → AdGroup.status

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/adgroup/status/{adGroupId}` |
| GraphQL query | `AdGroup.status` |
| Return type | `AdGroupStatus` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Not nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/adgroup/status/{adGroupId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetAdGroupStatus($id: ID!) {
  adGroup(id: $id) {
    id
    isEnabled
    status
  }
}
```
