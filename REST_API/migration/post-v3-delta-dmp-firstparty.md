# POST /v3/delta/dmp/firstparty → Query.firstPartyDataDelta

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-delta-dmp-firstparty
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/delta/dmp/firstparty → Query.firstPartyDataDelta

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/delta/dmp/firstparty` |
| GraphQL query | `Query.firstPartyDataDelta` |
| Return type | `FirstPartyDataDelta` |

> **Note:** This endpoint will be deprecated in the near future. Use 'delta/dmp/query/advertiser/firstparty' instead. Prefer the canonical GraphQL field `Query.firstPartyDataDelta` via `POST /v3/delta/dmp/query/advertiser/firstparty`.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `input.advertiser.changeTrackingVersion` | Long! | Optional | REST optional long? defaults when omitted; GraphQL requires non-null Long |
| `AdvertiserId` | `input.advertiser.ids` | [ID!] | Required | REST single optional/required ID → GraphQL IDs list (wrap single value in array) REST AdvertiserId maps to one element in AdvertiserDeltaInput.ids. |
| `IncludeActiveIDsCountExpandedFlag` | N/A | N/A | Optional | REST transport only |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `pageSize` | Int | Placement: `input.advertiser.pageSize`. GraphQL-only pagination control; REST delta has implicit paging via More*Available without explicit page size on most endpoints. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `currentMinimumTrackingVersion` | Long! | Not nullable | REST single version → GraphQL splits into `currentMinimumTrackingVersion` and `nextChangeTrackingVersion` |
| `LastChangeTrackingVersion` | `nextChangeTrackingVersion` | Long! | Not nullable | GraphQL-only companion field for pagination cursor No direct REST counterpart; use for subsequent delta calls (replaces REST LastChangeTrackingVersion on next request). |
| `Data` | `firstPartyData` | [FirstPartyData!]! | Not nullable | REST Data → GraphQL `firstPartyData` (`FirstPartyData` entities) |
| N/A | `moreAvailable` | Boolean! | Not nullable | GraphQL-only pagination flag; REST FirstPartyDataDelta response has no MoreDataAvailable field. |
| `Data[].FirstPartyDataId` | `id` | Long! | Not nullable | FirstPartyDataId → `id` |
| `Data[].Name` | `name` | String! | Not nullable | N/A |
| `Data[].DataType` | `targetingData.dataType` | TargetingDataType! | Not nullable | N/A |
| `Data[].UniqueUserCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].LookAlikeModelEligibility` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].LookAlikeModelDetails` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].LookAlikeModelDetails.FirstPartyDataId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].LookAlikeModelDetails.LastRequestDateUTC` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].LookAlikeModelDetails.LastGenerationDateUTC` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].LookAlikeModelDetails.LookAlikeModelBuildStatus` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].LookAlikeModelDetails.LookAlikeModelResultStatus` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].DevicesBrowsers30DayCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].UniqueUserInAppCount` | `activeUniques.idsInAppCount` | Long | Nullable | N/A |
| `Data[].UniqueUserWebCount` | `activeUniques.idsWebCount` | Long | Nullable | N/A |
| `Data[].UniqueConnectedTvCount` | `activeUniques.idsConnectedTvCount` | Long | Nullable | N/A |
| `Data[].PersonsCount` | `activeUniques.personsCount` | Long | Nullable | N/A |
| `Data[].HouseholdCount` | `activeUniques.householdCount` | Long | Nullable | N/A |
| `Data[].ImportedAudienceCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].ReceivedIDsCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Data[].ActiveIDsCount` | `activeUniques.idsCount` | Long | Nullable | N/A |
| `Data[].ActiveIDsInAppCount` | `activeUniques.idsInAppCount` | Long | Nullable | N/A |
| `Data[].ActiveIDsWebCount` | `activeUniques.idsWebCount` | Long | Nullable | N/A |
| `Data[].ActiveIDsConnectedTvCount` | `activeUniques.idsConnectedTvCount` | Long | Nullable | N/A |
| `Data[].ActivePersonsCount` | `activeUniques.personsCount` | Long | Nullable | N/A |
| `Data[].ActiveHouseholdCount` | `activeUniques.householdCount` | Long | Nullable | N/A |
| `Data[].ActiveIDsCountExpanded` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

### TargetingData

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DataType` | `dataType` | TargetingDataType! | Not nullable | On `FirstPartyData.targetingData`. |

### ActiveUniques

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| UniqueUserCount / ActiveIDsCount | `idsCount` | Long | Nullable | On `FirstPartyData.activeUniques`. |
| UniqueUserInAppCount / ActiveIDsInAppCount | `idsInAppCount` | Long | Nullable | N/A |
| UniqueUserWebCount / ActiveIDsWebCount | `idsWebCount` | Long | Nullable | N/A |
| UniqueConnectedTvCount / ActiveIDsConnectedTvCount | `idsConnectedTvCount` | Long | Nullable | N/A |
| PersonsCount / ActivePersonsCount | `personsCount` | Long | Nullable | N/A |
| HouseholdCount / ActiveHouseholdCount | `householdCount` | Long | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/delta/dmp/firstparty HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "LastChangeTrackingVersion": null,
  "AdvertiserId": "example-id"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query FirstPartyDataDeltaByAdvertiser {
  firstPartyDataDelta(input: {
    advertiser: {
      changeTrackingVersion: 0
      ids: ["adv123"]
      pageSize: 100
    }
  }) {
    currentMinimumTrackingVersion
    nextChangeTrackingVersion
    moreAvailable
    firstPartyData {
      id
    }
  }
}
```
