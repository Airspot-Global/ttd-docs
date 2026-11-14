# POST /v3/creative/query/advertiser → Advertiser.creatives

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-creative-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/creative/query/advertiser → Advertiser.creatives

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/creative/query/advertiser` |
| GraphQL query | `Advertiser.creatives` |
| Return type | `AdvertiserCreativesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent key—attaches as `Advertiser.creatives` | ID! | Required | Resolve `Advertiser` by ID, then query `creatives`. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerms` | `where.search.like` | String | Optional | REST requires all terms to match across ID, name, and description. `where.search` uses `CreativeSearchFilterInput` and matches ID, ad server creative ID, name, and description. |
| `SearchTerms` | `where.searchText.like` | String | Optional | Alternative filter on name and description only via `StringSearchFilterInput`; different semantics from `where.search`. |
| `SortFields` | `creatives(order:)` | [AdvertiserCreativeSortInput!] | Optional | REST multi-field sort maps to `order` array. Default REST sort is `Name` ascending → `order: [{ name: ASC }]`. |
| `SortFields[].FieldId` | `order[].name`, `order[].description` | SortEnumType | Optional | REST `Name` → `name`; REST `Description` → `description`. |
| `SortFields[].Ascending` | `order[].*` value | SortEnumType | Optional | `true` → `ASC`; `false` → `DESC`. |
| `CreativeTypes` | `where.type.in` | CreativeTypeOperationFilterInput | Optional | REST creative-type enum values map to GraphQL `CreativeType` enum members (e.g. `Image` → `HOSTED_DISPLAY`). |
| `CreativeAuditStatusFilter` | `where.supplyVendorAudits` | ListSupplyVendorCreativeAuditFilterInput | Optional | See nested `CreativeAuditStatusFilter` table. |
| `Availabilities` | `where.isArchived` | CreativeArchivedOperationFilterInput | Optional | REST defaults to `Available` only. `Available` → `isArchived: { eq: false }`; `Archived` → `isArchived: { eq: true }`. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [Creative!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| Result[].* (Creative fields) | `nodes[].*` | N/A | N/A | Each `Result[]` item is a full REST `Creative` model. Field mapping is identical to `GET /v3/creative/{creativeId}`—prefix GraphQL paths with `nodes[].`. See that endpoint doc for the complete field table. |

## Endpoint-specific nested types and enums

### CreativeAuditStatusFilter

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CreativeAuditor` | `where.supplyVendorAudits.some.supplyVendorId` | IdOperationFilterInput | Nullable | REST auditor name (e.g. `Google`, `AppNexus`) maps to the corresponding supply-vendor ID filter. |
| `AuditStatuses` | `where.supplyVendorAudits.some.auditStatus.in` | CreativeAuditStatusOperationFilterInput | Nullable | REST lowercase strings map to `CreativeAuditStatusInput` enum (e.g. `approved` → `APPROVED`, `pending` → `PENDING`, `not audited` → `NOT_AUDITED`, `rejected` → `REJECTED`, `unauditable` → `UNAUDITABLE`). |

### CreativeSortingField (enum)

REST values: `Name`, `Description`. GraphQL sort members on `AdvertiserCreativeSortInput`: `name`, `description` (plus additional sort keys not exposed in REST).

### CreativeType (enum)

REST `CreativeType` values map to GraphQL `CreativeType` members—for example `Image` → `HOSTED_DISPLAY`, `HostedVideo` → `HOSTED_VIDEO`, `ThirdPartyTag` → `THIRD_PARTY_DISPLAY`, `Html5` → `HOSTED_HTML5`, `HostedNative` → `HOSTED_NATIVE`, `HostedAudio` → `HOSTED_AUDIO`, `ThirdPartyVideo` → `THIRD_PARTY_VIDEO`, `ThirdPartyAudio` → `THIRD_PARTY_AUDIO`.

## Code examples

### REST example

```
POST /v3/creative/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<advertiser-id>",
  "Availabilities": ["Available"],
  "PageStartIndex": 0,
  "PageSize": 25
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCreativesByAdvertiser($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    id
    creatives(
      first: 25
      where: { isArchived: { eq: false } }
      order: [{ name: ASC }]
    ) {
      totalCount
      nodes {
        id
        name
        description
        flightStart
        flightEnd
        type
        isArchived
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
