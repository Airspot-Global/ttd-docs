# Data group: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/datagroup-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Data group: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/datagroup/{dataGroupId}` | `Advertiser.dataGroups` | N/A |
| `GET /v3/datagroup/{dataGroupId}/{geoForCounts}` | `Advertiser.dataGroups` | Geo-filtered audience counts via `TargetingDataGroup.counts(geoForCounts:)` |
| `POST /v3/datagroup/query/advertiser` | `Advertiser.dataGroups` | N/A |
| `GET /v3/datagroup/name/{dataGroupId}` | `Advertiser.dataGroups` | N/A |

## Shared nested types and enums

### DataGroupCounts

Audience count fields are grouped under `counts(geoForCounts: String): DataGroupCounts` so the geo filter applies to the whole counts payload and `geoForCounts` always echoes the geo the sibling counts were filtered to.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoForCounts` | `geoForCounts` | String | Nullable | Echoes the geo the counts were filtered to. |
| `UniqueUserCount` | `uniqueUserCount` | Long | Nullable | N/A |
| `PersonsCount` | `personsCount` | Long | Nullable | N/A |
| `HouseholdCount` | `householdCount` | Long | Nullable | N/A |
| `ActiveIDsCountExpanded` | `activeIDsCountExpanded` | Boolean | Nullable | N/A |
| `SuccessfullyRetrievedCounts` | `successfullyRetrievedCounts` | Boolean | Nullable | N/A |
