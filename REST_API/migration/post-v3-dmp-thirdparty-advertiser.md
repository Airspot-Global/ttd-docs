# POST /v3/dmp/thirdparty/advertiser → Query.thirdPartyDatas

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-dmp-thirdparty-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/dmp/thirdparty/advertiser → Query.thirdPartyDatas

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/dmp/thirdparty/advertiser` |
| GraphQL query | `Query.thirdPartyDatas` |
| Return type | `ThirdPartyDatasConnection` |

> **IMPORTANT:** `Query.thirdPartyDatas` is deprecated—use `partner(id).thirdPartyDataExpanded` for segment discovery.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageSize` | `first` | Int | Optional | N/A |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `AdvertiserId` | N/A | N/A | Optional | Not currently available in GraphQL |
| `AdEnvironment` | N/A | N/A | Optional | Not currently available in GraphQL |
| `BrandIds` | N/A | N/A | Optional | Not currently available in GraphQL |
| `CategoryIds` | N/A | N/A | Optional | Not currently available in GraphQL |
| `CountryName` | `where.country.name` | EqOnlyStringOperationFilterInput | Optional | REST country name → `TargetingDataCountryV2FilterInput.name` |
| `DataRateFilters` | `where.dataRates` | ListDataRate2FilterFilterInput | Optional | REST data-rate filters → `dataRates` filter list |
| `ExcludeTotalCounts` | N/A | N/A | Optional | REST transport only |
| `IncludeActiveIDsCountExpandedFlag` | N/A | N/A | Optional | REST transport only |
| `OnlyUsableForPlanningTool` | `where.isPlannerOnly` | BooleanOperationFilterInput | Optional | REST planning-tool flag → `isPlannerOnly` |
| `SearchTerms` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields` | `order` | `[ThirdPartyDataSortInput!]` | Optional | See domain guide—ThirdPartyDataSortInput |
| `SupportsDynamicCreativeRules` | N/A | N/A | Optional | Not currently available in GraphQL |
| `ThirdPartyDataIds` | `where.id` | LongOperationFilterInput | Optional | REST segment ID list → `id` filter (for example `{ in: [...] }`) |
| `UniqueCountMaximum` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UniqueCountMinimum` | N/A | N/A | Optional | Not currently available in GraphQL |
| `AudienceUnlimitedOnly` | N/A | N/A | Optional | Not currently available in GraphQL |
| `OnlyEligibleForSeeds` | N/A | N/A | Optional | Not currently available in GraphQL |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[ThirdPartyData!]` | Nullable | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].ThirdPartyDataId` | `id` | ID! | Not nullable | N/A |
| `Result[].BrandId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].BrandName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].Name` | `name` | String! | Not nullable | N/A |
| `Result[].FullPath` | `fullPath` | String! | Not nullable | N/A |
| `Result[].Description` | `description` | String | Nullable | N/A |
| `Result[].UniqueUserCount` | `activeUniques.idsCount` | Long | Nullable | Deprecated REST `UniqueUserCount`; use `activeUniques.idsCount` |
| `Result[].UniqueUserWebCount` | `activeUniques.idsWebCount` | Long | Nullable | Deprecated REST field; maps to `activeUniques.idsWebCount` |
| `Result[].CPMRate` | `dataRates.nodes[].rateAmount` | Decimal! | Not nullable | REST inline CPM → `dataRates` on `DataRate`. Read `dataRateType.name` (a free-text `String!`, not an enum): when `CPM`, amount is `rateAmount`; when `Hybrid`, CPM cap is `secondaryRateAmount`. Currency is `currencyCodeId`. |
| `Result[].CPMRateInAdvertiserCurrency` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].PercentOfMediaCostRate` | `dataRates.nodes[].rateAmount` | Decimal! | Not nullable | REST inline percentage → `dataRates` connection on `DataRate`. Read `dataRateType.name` (a free-text `String!`, not an enum): when `RevShare` or `Hybrid`, percentage is `rateAmount`. |
| `Result[].IsPartnerDirect` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].PersonsCount` | `activeUniques.personsCount` | Long | Nullable | Deprecated REST `PersonsCount` → `activeUniques.personsCount` |
| `Result[].HouseholdCount` | `activeUniques.householdCount` | Long | Nullable | Deprecated REST `HouseholdCount` → `activeUniques.householdCount` |
| `Result[].ReceivedIDsCount` | `receivedIdsCount` | Long | Nullable | N/A |
| `Result[].ActiveIDsCountExpanded` | `activeIdsCountExpanded` | Boolean | Nullable | N/A |
| `Result[].IsEligibleForSeeds` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].DataEventTypeId` | `targetingData.dataEventType` | DataEventType | Nullable | REST long ID → `targetingData.dataEventType` enum. See domain guide—DataEventType |
| `Result[].IsAudienceUnlimited` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

### ThirdPartyData

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ThirdPartyDataId` | `id` | ID! | Not nullable | N/A |
| `BrandId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BrandName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Name` | `name` | String! | Not nullable | N/A |
| `FullPath` | `fullPath` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `UniqueUserCount` | `activeUniques.idsCount` | Long | Nullable | Deprecated REST `UniqueUserCount`; use `activeUniques.idsCount` |
| `UniqueUserWebCount` | `activeUniques.idsWebCount` | Long | Nullable | Deprecated REST field; maps to `activeUniques.idsWebCount` |
| `CPMRate` | `dataRates.nodes[].rateAmount` | Decimal! | Not nullable | When `dataRateType.name` (a free-text `String!`) is `CPM`, amount is `rateAmount`; when `Hybrid`, CPM cap is `secondaryRateAmount`. Currency is `currencyCodeId`. |
| `CPMRateInAdvertiserCurrency` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PercentOfMediaCostRate` | `dataRates.nodes[].rateAmount` | Decimal! | Not nullable | When `dataRateType.name` (a free-text `String!`) is `RevShare` or `Hybrid`, percentage is `rateAmount`. |
| `IsPartnerDirect` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PersonsCount` | `activeUniques.personsCount` | Long | Nullable | Deprecated REST `PersonsCount` → `activeUniques.personsCount` |
| `HouseholdCount` | `activeUniques.householdCount` | Long | Nullable | Deprecated REST `HouseholdCount` → `activeUniques.householdCount` |
| `ReceivedIDsCount` | `receivedIdsCount` | Long | Nullable | N/A |
| `ActiveIDsCountExpanded` | `activeIdsCountExpanded` | Boolean | Nullable | N/A |
| `IsEligibleForSeeds` | N/A | N/A | N/A | Not currently available in GraphQL |
| `DataEventTypeId` | `targetingData.dataEventType` | DataEventType | Nullable | REST long ID → `targetingData.dataEventType` enum. See domain guide—DataEventType |
| `IsAudienceUnlimited` | N/A | N/A | N/A | Not currently available in GraphQL |

## Code examples

### REST example

```
POST /v3/dmp/thirdparty/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv123",
  "PageStartIndex": 0,
  "PageSize": 50
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ThirdPartyDatas {
  thirdPartyDatas(first: 50) {
    nodes {
      id
      name
      fullPath
      description
      receivedIdsCount
      activeUniques {
        idsCount
        idsWebCount
      }
      thirdPartyDataProvider {
        id
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
