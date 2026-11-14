# GET /v3/datagroup/name/{dataGroupId} → TargetingDataGroup

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-datagroup-name-datagroupid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/datagroup/name/{dataGroupId} → TargetingDataGroup

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/datagroup/name/{dataGroupId}` |
| GraphQL query | `Advertiser.dataGroups` |
| Return type | `TargetingDataGroup` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | On `TargetingDataGroup`. |
| `Name` | `name` | String! | Not nullable | On `TargetingDataGroup`. |

## Code examples

### REST example

```
GET /v3/datagroup/name/{dataGroupId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query DataGroupName {
  advertiser(id: "<advertiser-id>") {
    dataGroups(first: 1, searchTerms: ["<targeting-data-group-id>"]) {
      nodes {
        id
        name
      }
    }
  }
}
```
