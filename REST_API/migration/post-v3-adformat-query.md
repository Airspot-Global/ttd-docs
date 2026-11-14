# POST /v3/adformat/query → Query.adFormats

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-adformat-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/adformat/query → Query.adFormats

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/adformat/query` |
| GraphQL query | `Query.adFormats` |
| Return type | `AdFormatsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `SearchTerms` | `where.name` | StringOperationFilterInput | Optional | No `searchTerms` argument. REST requires every term to match across ID, label, IAB name, or display name; approximate with `where.name: { contains: "..." }` (semantics differ). |
| `SearchTerms` | `where.id` | StringIdOperationFilterInput | Optional | No `searchTerms` argument. REST requires every term to match across ID, label, IAB name, or display name; approximate with `where.id: { contains: "..." }` (semantics differ). |
| `SortFields` | `order` | [AdFormatSortInput!] | Optional | Sort input (e.g. `order: [{ name: ASC }]`). Defaults to name ascending when omitted in REST. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[AdFormat!]` | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | `Int!` | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `AdFormatId` | `AdFormat.id` | `ID!` | Not nullable | Already available on `AdFormat`. |
| `AdFormatName` | `AdFormat.iabName` | `String!` | Not nullable | Renamed: REST `AdFormatName` maps to `iabName`. |
| `Width` | `DisplayAdFormat.widthInPixels` | `Int!` | Not nullable | Already available on concrete ad-format subtypes (e.g. `DisplayAdFormat`), not on the `AdFormat` interface. |
| `Height` | `DisplayAdFormat.heightInPixels` | `Int!` | Not nullable | Already available on concrete ad-format subtypes (e.g. `DisplayAdFormat`), not on the `AdFormat` interface. |
| `IsDisplayRTBEligible` | `isDisplayRTBEligible` | Boolean! | Not nullable | New field on all five concrete ad-format subtypes (`DisplayAdFormat`, `VideoAdFormat`, `NativeAdFormat`, `AudioAdFormat`, `NativeVideoAdFormat`). |
| `InventoryType` | `AdFormat.mediaType` | MediaType! | Not nullable | Renamed: REST `InventoryType` maps to `mediaType`. |
| `IsFacebookRightHandSideEligible` | N/A | N/A | N/A | Deprecated in REST—not exposed in GraphQL. |
| `IsFacebookPagePostEligible` | N/A | N/A | N/A | Deprecated in REST—not exposed in GraphQL. |

## Endpoint-specific nested types and enums

### AdFormat

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdFormatId` | `id` | `ID!` | Not nullable | On `AdFormat`. |
| `AdFormatName` | `iabName` | `String!` | Not nullable | Renamed from REST `AdFormatName`. |
| `Width` | `widthInPixels` | `Int!` | Not nullable | On concrete subtypes such as `DisplayAdFormat`. |
| `Height` | `heightInPixels` | `Int!` | Not nullable | On concrete subtypes such as `DisplayAdFormat`. |
| `IsDisplayRTBEligible` | `isDisplayRTBEligible` | Boolean! | Not nullable | New field on all five concrete subtypes. |
| `InventoryType` | `mediaType` | MediaType! | Not nullable | Renamed from REST `InventoryType`. |

### AdFormatSortingField (enum)

| REST value | GraphQL mapping | Notes |
| --- | --- | --- |
| `Name` | `order: [{ name: ASC }]` or `order: [{ name: DESC }]` | REST `SortFields[].Ascending` controls `ASC` vs `DESC`. Only sort field supported by REST. |

### MediaType (enum)

| REST value | GraphQL value | Notes |
| --- | --- | --- |
| `Unknown` | `UNKNOWN` | N/A |
| `Display` | `DISPLAY` | N/A |
| `Video` | `VIDEO` | N/A |
| `Native` | `NATIVE` | N/A |
| `Audio` | `AUDIO` | N/A |
| `NativeVideo` | `NATIVE_VIDEO` | N/A |

## Code examples

The following are examples of querying ad formats with REST and GraphQL.

List ad formats with eligibility fields:

### REST example

```
POST /v3/adformat/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetAdFormatFlags {
  adFormats {
    nodes {
      id
      iabName
      mediaType
      ... on DisplayAdFormat {
        widthInPixels
        heightInPixels
        isDisplayRTBEligible
        isOpenPathEnabled
      }
      ... on VideoAdFormat {
        isDisplayRTBEligible
        isOpenPathEnabled
      }
    }
  }
}
```

### REST example (by ID)

```
POST /v3/adformat/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "SearchTerms": ["<adFormatId>"],
  "PageStartIndex": 0,
  "PageSize": 1
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query LookupAdFormat {
  adFormats(where: { id: { eq: "<adFormatId>" } }, first: 1) {
    nodes {
      id
      ... on DisplayAdFormat {
        isDisplayRTBEligible
        isOpenPathEnabled
      }
    }
  }
}
```
