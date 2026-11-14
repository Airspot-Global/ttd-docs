# POST /v3/factualproximitydesign/query/partner → Partner.factualProximityDesigns

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-factualproximitydesign-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/factualproximitydesign/query/partner → Partner.factualProximityDesigns

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/factualproximitydesign/query/partner` |
| GraphQL query | `Partner.factualProximityDesigns` |
| Return type | `FactualProximityDesignsConnection` |

Paged factual proximity designs for a partner. Exposed as the `factualProximityDesigns` relationship field on `Partner`.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | Parent: `Partner.factualProximityDesigns` (relationship field) | N/A | Required | Required parent identifier; supplied by `Partner.id`, not a filter arg. |
| `FactualDesignFilter` | `filter.factualDesignFilter` (`FactualProximityDesignByPartnerInput`) | String | Optional | Optional name-equality filter. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | FactualProximityDesign | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].DesignId` | `FactualProximityDesign.designId` | ID! | Not nullable | N/A |
| `Result[].TargetingCodeId` | `FactualProximityDesign.targetingCodeId` | ID! | Not nullable | N/A |
| `Result[].DesignGuid` | `FactualProximityDesign.designGuid` | String! | Not nullable | `Guid` serialized as string. |
| `Result[].DesignName` | `FactualProximityDesign.designName` | String! | Not nullable | N/A |
| `Result[].TargetingCodeName` | `FactualProximityDesign.targetingCodeName` | String! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### FactualProximityDesign

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DesignId` | `designId` | ID! | Not nullable | N/A |
| `TargetingCodeId` | `targetingCodeId` | ID! | Not nullable | N/A |
| `DesignGuid` | `designGuid` | String! | Not nullable | `Guid` serialized as string. |
| `DesignName` | `designName` | String! | Not nullable | N/A |
| `TargetingCodeName` | `targetingCodeName` | String! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/factualproximitydesign/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "<partner-id>",
  "FactualDesignFilter": "My Design",
  "PageStartIndex": 0,
  "PageSize": 20
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetFactualProximityDesigns($partnerId: ID!) {
  partner(id: $partnerId) {
    factualProximityDesigns(
      first: 20
      filter: { factualDesignFilter: "My Design" }
    ) {
      edges {
        node {
          designId
          designGuid
          designName
          targetingCodeId
          targetingCodeName
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
