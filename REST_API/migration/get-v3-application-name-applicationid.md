# GET /v3/application/name/{applicationId} → Query.mobileApplications

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-application-name-applicationid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/application/name/{applicationId} → Query.mobileApplications

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/application/name/{applicationId}` |
| GraphQL query | `Query.mobileApplications` |
| Return type | `MobileApplicationsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `{applicationId}` (path) | `where.id.eq` | `String` | Required | REST path parameter becomes an equality filter on `Query.mobileApplications`. Pair with `first: 1` on the query (see overview). |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `nodes[].id` | `ID!` | Not nullable | Nullability inversion: REST contract marks `Id` Optional; GraphQL `id: ID!`. |
| `Name` | `nodes[].name` | `String!` | Not nullable | Nullability inversion: REST contract marks `Name` Optional; GraphQL `name: String!`. |
| `MobilePlatform` | `nodes[].mobilePlatform` | `MobilePlatform` | Nullable | Remodelled in GraphQL: REST bare enum scalar → nested object. See nested tables. |
| N/A | `nodes[].categories` | `[String!]!` | Not nullable | GraphQL-only gain: application category tags. Not returned by this REST endpoint. |

## Endpoint-specific nested types and enums

### MobilePlatform

REST returns `MobilePlatform` as a **bare string enum** (13 member names). GraphQL exposes a nullable **`MobilePlatform` object** on each node:

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `mobilePlatformType` | `MobilePlatformType!` | Not nullable | Authoritative enum—maps 1:1 from the REST `MobilePlatform` member. Branch on this field, not on `operatingSystem`. |
| `operatingSystem` | `String` | Nullable | Derived human-readable companion label from the same underlying platform. **Not part of the schema contract**—values are not enumerated in GraphQL. Null when `mobilePlatformType` is `NONE`. Do **not** string-match this field in production logic; use `mobilePlatformType` instead. |

### REST `MobilePlatform` → `mobilePlatformType`

All 13 REST enum members have a matching GraphQL `MobilePlatformType` member:

| REST `MobilePlatform` | GraphQL `mobilePlatformType` |
| --- | --- |
| `None` | `NONE` |
| `Apple` | `APPLE` |
| `Google` | `GOOGLE` |
| `Tencent` | `TENCENT` |
| `Roku` | `ROKU` |
| `Amazon` | `AMAZON` |
| `Firetv` | `FIRETV` |
| `tvOS` | `TV_OS` |
| `Samsung` | `SAMSUNG` |
| `LGTV` | `LGTV` |
| `Vizio` | `VIZIO` |
| `GoogleTV` | `GOOGLE_TV` |
| `SamsungGalaxy` | `SAMSUNG_GALAXY` |

Common mis-guesses: `tvOS` → `TV_OS` (not `TVOS`), `GoogleTV` → `GOOGLE_TV`, `SamsungGalaxy` → `SAMSUNG_GALAXY`, `LGTV` → `LGTV` (unchanged), `None` → `NONE`.

### `operatingSystem` (illustrative only—not contractual)

The server derives `operatingSystem` from the same platform backing store. Because the schema types it as plain `String`, exact values are **not** part of the API contract. Illustrative examples only:

- REST `Apple` → `mobilePlatformType: APPLE`, `operatingSystem` may be `"iOS"` _(illustrative)_
- REST `Google` → `mobilePlatformType: GOOGLE`, `operatingSystem` may be `"Android"` _(illustrative)_

For most other platforms the string often echoes the platform name; for `NONE`, `operatingSystem` is `null`.

## Code examples

The following are examples of looking up a mobile application by ID with REST and GraphQL.

### REST example

```
GET /v3/application/name/com.example.myapp HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

REST returns HTTP 200 with a single object, or HTTP 404 when the ID is unknown:

```
{
  "Id": "com.example.myapp",
  "Name": "My Example App",
  "MobilePlatform": "Apple"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query MobileApplicationById {
  mobileApplications(
    where: { id: { eq: "com.example.myapp" } }
    first: 1
  ) {
    totalCount
    nodes {
      id
      name
      mobilePlatform {
        mobilePlatformType
        operatingSystem
      }
      categories
    }
  }
}
```

When the ID is unknown, GraphQL still returns HTTP 200 with `{ "data": { "mobileApplications": { "totalCount": 0, "nodes": [] } } }`—no error. Replace REST 404 handling with a `totalCount === 0` or `nodes.length === 0` check.
