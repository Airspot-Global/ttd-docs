# GET /v3/datagroup/{dataGroupId}/{geoForCounts} → TargetingDataGroup

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-datagroup-datagroupid-geoforcounts
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/datagroup/{dataGroupId}/{geoForCounts} → TargetingDataGroup

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/datagroup/{dataGroupId}/{geoForCounts}` |
| GraphQL query | `Advertiser.dataGroups` |
| Return type | `TargetingDataGroup` |

`geoForCounts` path param → `TargetingDataGroup.counts(geoForCounts:)`. Response body matches GET `/v3/datagroup/{dataGroupId}`.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| geoForCounts (path) | `counts(geoForCounts:)` | String | Required | Filters audience counts to the specified geo (country or continent). |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | Same mapping as GET-by-ID. |
| `DataGroupId` | `id` | ID! | Not nullable | Existing field on `TargetingDataGroup`. |
| `DataGroupName` | `name` | String! | Not nullable | Existing field on `TargetingDataGroup`. |
| `Description` | `description` | String | Nullable | Existing field on `TargetingDataGroup`. |
| `IsSharable` | `isSharable` | Boolean | Nullable | N/A |
| `FirstPartyDataIds` | `firstPartyData` | N/A | N/A | Flat ID list not available; use the `firstPartyData` connection. |
| `ThirdPartyDataIds` | `thirdPartyData` | N/A | N/A | Flat ID list not available; use the `thirdPartyData` connection. |
| `SkipUnauthorizedThirdPartyData` | N/A | N/A | N/A | Write-only on create/update; not populated on read responses. |
| `GeoForCounts` | `counts(geoForCounts: …).geoForCounts` | String | Nullable | Set from path parameter on this endpoint; echoed on the same `DataGroupCounts` object as the counts it describes. |
| `UniqueUserCount` | `counts(geoForCounts: …).uniqueUserCount` | Long | Nullable | `counts(geoForCounts: …)` uses the geo-specific REST path when the geo arg is provided. |
| `PersonsCount` | `counts(geoForCounts: …).personsCount` | Long | Nullable | Same geo-routing as `uniqueUserCount`. |
| `HouseholdCount` | `counts(geoForCounts: …).householdCount` | Long | Nullable | Same geo-routing as `uniqueUserCount`. |
| `ActiveIDsCountExpanded` | `counts(geoForCounts: …).activeIDsCountExpanded` | Boolean | Nullable | Same geo-routing as `uniqueUserCount`. |
| `SuccessfullyRetrievedCounts` | `counts(geoForCounts: …).successfullyRetrievedCounts` | Boolean | Nullable | Same geo-routing as `uniqueUserCount`. |

## Code examples

### REST example

```
GET /v3/datagroup/{dataGroupId}/US HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query DataGroupWithGeoCounts {
  advertiser(id: "<advertiser-id>") {
    dataGroups(first: 1, searchTerms: ["<targeting-data-group-id>"]) {
      nodes {
        id
        name
        isSharable
        counts(geoForCounts: "US") {
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
