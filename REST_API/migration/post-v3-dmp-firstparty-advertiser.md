# POST /v3/dmp/firstparty/advertiser → Advertiser.firstPartyData

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-dmp-firstparty-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/dmp/firstparty/advertiser → Advertiser.firstPartyData

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/dmp/firstparty/advertiser` |
| GraphQL query | `Advertiser.firstPartyData` |
| Return type | `FirstPartyDataConnection` |

> **IMPORTANT:** This REST endpoint is deprecated. Use `Advertiser(id).firstPartyData` with filtering instead.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `Advertiser(id:)` | N/A | Required | Parent lookup—not a connection argument |
| `PageSize` | `first` | Int | Optional | N/A |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `DataTypes` | N/A | N/A | Optional | Not currently available in GraphQL |
| `IncludeActiveIDsCountExpandedFlag` | N/A | N/A | Optional | REST transport only |
| `LookAlikeModelBuildStatuses` | N/A | N/A | Optional | Not currently available in GraphQL |
| `LookAlikeModelEligibilities` | N/A | N/A | Optional | Not currently available in GraphQL |
| `LookAlikeModelResultStatuses` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SearchTerms` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields` | `order` | `[AdvertiserTargetingDataDisplayNoCacheSortInput!]` | Optional | N/A |
| `UniqueCountMaximum` | `where.idsCount` | LongOperationFilterInput | Optional | REST maximum unique count → `idsCount` filter (for example `{ lte: ... }`) |
| `UniqueCountMinimum` | `where.idsCount` | LongOperationFilterInput | Optional | REST minimum unique count → `idsCount` filter (for example `{ gte: ... }`) |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[FirstPartyData!]` | Nullable | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].FirstPartyDataId` | `id` | Long! | Not nullable | N/A |
| `Result[].Name` | `name` | String! | Not nullable | N/A |
| `Result[].DataType` | `targetingData.dataType` | TargetingDataType! | Not nullable | REST `FirstPartyDataType` enum → `targetingData.dataType`. See domain guide—TargetingDataType |
| `Result[].UniqueUserCount` | `activeUniques.idsCount` | Long | Nullable | Deprecated REST `UniqueUserCount` → `activeUniques.idsCount` |
| `Result[].LookAlikeModelEligibility` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].LookAlikeModelDetails` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].PersonsCount` | `activeUniques.personsCount` | Long | Nullable | Deprecated REST `PersonsCount` → `activeUniques.personsCount` |
| `Result[].HouseholdCount` | `activeUniques.householdCount` | Long | Nullable | Deprecated REST `HouseholdCount` → `activeUniques.householdCount` |
| `Result[].ImportedAudienceCount` | N/A | N/A | N/A | Deprecated on REST |
| `Result[].ReceivedIDsCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].ActiveIDsCount` | `activeUniques.idsCount` | Long | Nullable | N/A |
| `Result[].ActiveIDsInAppCount` | `activeUniques.idsInAppCount` | Long | Nullable | N/A |
| `Result[].ActiveIDsWebCount` | `activeUniques.idsWebCount` | Long | Nullable | N/A |
| `Result[].ActiveIDsConnectedTvCount` | `activeUniques.idsConnectedTvCount` | Long | Nullable | N/A |
| `Result[].ActivePersonsCount` | `activeUniques.personsCount` | Long | Nullable | N/A |
| `Result[].ActiveHouseholdCount` | `activeUniques.householdCount` | Long | Nullable | N/A |
| `Result[].ActiveIDsCountExpanded` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

### FirstPartyData

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `FirstPartyDataId` | `id` | Long! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |
| `DataType` | `targetingData.dataType` | TargetingDataType! | Not nullable | Only `dataType` is selected from `TargetingData`. See domain guide—TargetingDataType |
| `UniqueUserCount` | `activeUniques.idsCount` | Long | Nullable | Deprecated REST `UniqueUserCount` → `activeUniques.idsCount` |
| `LookAlikeModelEligibility` | N/A | N/A | N/A | Not currently available in GraphQL |
| `LookAlikeModelDetails` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PersonsCount` | `activeUniques.personsCount` | Long | Nullable | Deprecated REST `PersonsCount` → `activeUniques.personsCount` |
| `HouseholdCount` | `activeUniques.householdCount` | Long | Nullable | Deprecated REST `HouseholdCount` → `activeUniques.householdCount` |
| `ImportedAudienceCount` | N/A | N/A | N/A | Deprecated on REST |
| `ReceivedIDsCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ActiveIDsCount` | `activeUniques.idsCount` | Long | Nullable | N/A |
| `ActiveIDsInAppCount` | `activeUniques.idsInAppCount` | Long | Nullable | N/A |
| `ActiveIDsWebCount` | `activeUniques.idsWebCount` | Long | Nullable | N/A |
| `ActiveIDsConnectedTvCount` | `activeUniques.idsConnectedTvCount` | Long | Nullable | N/A |
| `ActivePersonsCount` | `activeUniques.personsCount` | Long | Nullable | N/A |
| `ActiveHouseholdCount` | `activeUniques.householdCount` | Long | Nullable | N/A |
| `ActiveIDsCountExpanded` | N/A | N/A | N/A | Not currently available in GraphQL |

## Code examples

### REST example

```
POST /v3/dmp/firstparty/advertiser HTTP/1.1
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
query AdvertiserFirstPartyData {
  advertiser(id: "adv123") {
    firstPartyData(
      first: 50
      where: { idsCount: { gte: 1000 } }
      order: [{ idsCount: DESC }]
    ) {
      nodes {
        id
        name
        targetingData {
          dataType
        }
        activeUniques {
          idsCount
        }
      }
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
