# POST /v3/devicemakemodel/query → Query.deviceModels

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-devicemakemodel-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/devicemakemodel/query → Query.deviceModels

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/devicemakemodel/query` |
| GraphQL query | `Query.deviceModels` |
| Return type | `DeviceModelsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `DeviceModelNameFilter` | `Query.deviceModels(where:)` | DeviceModelFilterInput | Optional | REST matches any device whose make, model, or marketing name contains the value. GraphQL requires composing `where.or` with `name.contains`, `marketingName.contains`, and `make.name.contains`—no single arg equivalent. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [DeviceModel!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].DeviceMakeId` | `DeviceModel.make.id` | ID! | Not nullable | `int` → `ID` (string). REST flattens onto `DeviceMakeModel`; GraphQL nests under `make`. |
| `Result[].DeviceModelId` | `DeviceModel.id` | ID! | Not nullable | `int` → `ID` (string). |
| `Result[].DeviceModelName` | `DeviceModel.name` | String! | Not nullable | Model name. |
| `Result[].DeviceMakeName` | `DeviceModel.make.name` | String! | Not nullable | Make name; also available as `DeviceModel.makeName` (identical to `make { name }`). |
| `Result[].DeviceModelMarketingName` | `DeviceModel.marketingName` | String | Nullable | Marketing-friendly name; nullable in GraphQL. REST model marks it required but value may be empty string. |

## Endpoint-specific nested types and enums

### DeviceMakeModel

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DeviceMakeId` | `make.id` | ID! | Not nullable | `int` → `ID` (string). Nested under `make` in GraphQL. |
| `DeviceModelId` | `id` | ID! | Not nullable | `int` → `ID` (string). |
| `DeviceModelName` | `name` | String! | Not nullable | Model name. |
| `DeviceMakeName` | `make.name` | String! | Not nullable | Make name; also available as `makeName`. |
| `DeviceModelMarketingName` | `marketingName` | String | Nullable | Marketing-friendly name; nullable in GraphQL. |

## Code examples

### REST example

```
POST /v3/devicemakemodel/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 100,
  "DeviceModelNameFilter": "iPhone"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query DeviceModels {
  deviceModels(
    first: 100
    where: {
      or: [
        { name: { contains: "iPhone" } }
        { marketingName: { contains: "iPhone" } }
        { make: { name: { contains: "iPhone" } } }
      ]
    }
  ) {
    nodes {
      id
      name
      marketingName
      make {
        id
        name
      }
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
