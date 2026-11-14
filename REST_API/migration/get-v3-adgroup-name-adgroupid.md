# GET /v3/adgroup/name/{adGroupId} → AdGroup.id

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-adgroup-name-adgroupid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/adgroup/name/{adGroupId} → AdGroup.id

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/adgroup/name/{adGroupId}` |
| GraphQL query | `AdGroup.id` |
| Return type | `AdGroup` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/adgroup/name/{adGroupId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetAdGroupName($id: ID!) {
  adGroup(id: $id) {
    id
    name
  }
}
```
