# GET /v3/datagroup/{dataGroupId} → TargetingDataGroup

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-datagroup-datagroupid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/datagroup/{dataGroupId} → TargetingDataGroup

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/datagroup/{dataGroupId}` |
| GraphQL query | `Advertiser.dataGroups` |
| Return type | `TargetingDataGroup` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | Nested object reference instead of flat `advertiserId`. |
| `DataGroupId` | `id` | ID! | Not nullable | Existing field on `TargetingDataGroup`. |
| `DataGroupName` | `name` | String! | Not nullable | Existing field on `TargetingDataGroup`. |
| `Description` | `description` | String | Nullable | Existing field on `TargetingDataGroup`. |
| `IsSharable` | `isSharable` | Boolean | Nullable | N/A |
| `FirstPartyDataIds` | `firstPartyData` | N/A | N/A | Flat ID list not available; use the `firstPartyData` connection. |
| `ThirdPartyDataIds` | `thirdPartyData` | N/A | N/A | Flat ID list not available; use the `thirdPartyData` connection. |
| `SkipUnauthorizedThirdPartyData` | N/A | N/A | N/A | Write-only on create/update; not populated on read responses. |
| `GeoForCounts` | `counts.geoForCounts` | String | Nullable | On `DataGroupCounts`; echoes the geo the counts were filtered to (default `"All Countries"` when unfiltered). |
| `UniqueUserCount` | `counts.uniqueUserCount` | Long | Nullable | On `DataGroupCounts`. The `counts(geoForCounts: …)` arg routes to the geo-specific REST path when set. |
| `PersonsCount` | `counts.personsCount` | Long | Nullable | On `DataGroupCounts` (same payload/geo as sibling count fields). |
| `HouseholdCount` | `counts.householdCount` | Long | Nullable | On `DataGroupCounts` (same payload/geo as sibling count fields). |
| `ActiveIDsCountExpanded` | `counts.activeIDsCountExpanded` | Boolean | Nullable | On `DataGroupCounts` (same payload/geo as sibling count fields). |
| `SuccessfullyRetrievedCounts` | `counts.successfullyRetrievedCounts` | Boolean | Nullable | On `DataGroupCounts` (same payload/geo as sibling count fields). |

## Endpoint-specific nested types and enums

### DataGroupCounts

The five Active IDs counts and the `geoForCounts` echo are exposed under a single field, `counts(geoForCounts: String): DataGroupCounts`, rather than as flat fields each taking their own `geoForCounts` argument. The geo applies to the whole `DataGroupCounts` object, and `geoForCounts` always echoes the geo the sibling counts were filtered to.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoForCounts` | `geoForCounts` | String | Nullable | Echoes the geo the counts were filtered to. |
| `UniqueUserCount` | `uniqueUserCount` | Long | Nullable | N/A |
| `PersonsCount` | `personsCount` | Long | Nullable | N/A |
| `HouseholdCount` | `householdCount` | Long | Nullable | N/A |
| `ActiveIDsCountExpanded` | `activeIDsCountExpanded` | Boolean | Nullable | N/A |
| `SuccessfullyRetrievedCounts` | `successfullyRetrievedCounts` | Boolean | Nullable | N/A |

## Code examples

### REST example

```
GET /v3/datagroup/{dataGroupId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query DataGroupById {
  advertiser(id: "<advertiser-id>") {
    dataGroups(first: 1, searchTerms: ["<targeting-data-group-id>"]) {
      nodes {
        id
        name
        description
        isSharable
        counts {
          geoForCounts
          uniqueUserCount
          successfullyRetrievedCounts
        }
        advertiser {
          id
        }
      }
    }
  }
}
```
