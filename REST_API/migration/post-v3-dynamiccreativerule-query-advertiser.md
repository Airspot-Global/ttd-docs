# POST /v3/dynamiccreativerule/query/advertiser → Advertiser.dynamicCreativeRules

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-dynamiccreativerule-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/dynamiccreativerule/query/advertiser → Advertiser.dynamicCreativeRules

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/dynamiccreativerule/query/advertiser` |
| GraphQL query | `Advertiser.dynamicCreativeRules` |
| Return type | `[DynamicCreativeRule!]!` |

REST `POST /v3/dynamiccreativerule/query/advertiser` is a paginated advertiser-scoped query with search, sort, and page-count fields. GraphQL exposes an advertiser-scoped plain list via `Advertiser.dynamicCreativeRules` with no pagination, search, or sort arguments. Query through a parent `Advertiser` (requires `Advertiser.id`). Request self-extension fields on each `DynamicCreativeRule` (the same fields documented for GET `/v3/dynamiccreativerule/{dynamicCreativeRuleId}`).

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `Advertiser.dynamicCreativeRules` | N/A | Required | Advertiser ID is implicit from the parent `Advertiser` node. |
| `SearchTerms` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields[].FieldId` | N/A | N/A | Required | Not currently available in GraphQL |
| `SortFields[].Ascending` | N/A | N/A | Optional | Not currently available in GraphQL |
| `PageStartIndex` | N/A | N/A | Optional | N/A |
| `PageSize` | N/A | N/A | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `Advertiser.dynamicCreativeRules` | [DynamicCreativeRule!]! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].DynamicCreativeRuleId` | `id` | String! | Not nullable | On list elements. Existing field on `DynamicCreativeRule`. |
| `Result[].Name` | `name` | String! | Not nullable | On list elements. Existing field on `DynamicCreativeRule`. |
| `Result[].AdvertiserId` | `advertiser` | Advertiser | Nullable | On list elements. Entity reference instead of flat `advertiserId`. |
| `Result[].DataElementGroups` | `dataElementGroups` | [DataElementGroup!]! | Not nullable | On list elements. Self-extension field backed by GET-by-ID. |
| `Result[].DataElementGroups.GroupName` | `dataElementGroups { groupName }` | String! | Not nullable | Nested leaf on list elements. |
| `Result[].DataElementGroups.OutputName` | `dataElementGroups { outputName }` | String! | Not nullable | Nested leaf on list elements. |
| `Result[].DataElementGroups.FirstPartyDataIds` | `dataElementGroups { firstPartyDataIds }` | [ID!]! | Not nullable | Nested leaf on list elements. |
| `Result[].DataElementGroups.ThirdPartyDataIds` | `dataElementGroups { thirdPartyDataIds }` | [ID!]! | Not nullable | Nested leaf on list elements. |

## Endpoint-specific nested types and enums

### DynamicCreativeRuleSortingField

REST enum used in `SortFields[].FieldId`. **Not currently available in GraphQL** on `Advertiser.dynamicCreativeRules`.

| Enum value | Notes |
| --- | --- |
| `Name` | Sort by dynamic creative rule name. |

## Code examples

### REST example

```
POST /v3/dynamiccreativerule/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<ADVERTISER_ID>",
  "PageStartIndex": 0,
  "PageSize": 10
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserDynamicCreativeRules {
  advertiser(id: "<ADVERTISER_ID>") {
    id
    dynamicCreativeRules {
      id
      name
      advertiser {
        id
      }
      dataElementGroups {
        groupName
        outputName
        firstPartyDataIds
        thirdPartyDataIds
      }
    }
  }
}
```
