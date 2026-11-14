# POST /v3/datagroup/query/advertiser → Advertiser.dataGroups

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-datagroup-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/datagroup/query/advertiser → Advertiser.dataGroups

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/datagroup/query/advertiser` |
| GraphQL query | `Advertiser.dataGroups` |
| Return type | Connection of `TargetingDataGroup` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `Advertiser.dataGroups` | N/A | Required | Advertiser ID is implicit from the parent `Advertiser` node; not a public filter arg on the connection. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerms` | `searchTerms` | [String!] | Optional | Direct argument on `Advertiser.dataGroups`. |
| `SortFields` | `sortFields` | [DataGroupSortFieldSortingInput!] | Optional | Maps to `DataGroupSortFieldInput` enum (`NAME`, `DESCRIPTION`) plus optional `ascending`. Defaults to name ascending when omitted. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `Advertiser.dataGroups.nodes` | [TargetingDataGroup!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `Advertiser.dataGroups.totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].DataGroupId` | `id` | ID! | Not nullable | Existing field on connection nodes. |
| `Result[].DataGroupName` | `name` | String! | Not nullable | Existing field on connection nodes. |
| `Result[].Description` | `description` | String | Nullable | Existing field on connection nodes. |
| `Result[].AdvertiserId` | (parent implied) | N/A | N/A | Parent is `Advertiser`; flat `advertiserId` not surfaced on nodes. |
| `Result[].IsSharable` | `isSharable` | Boolean | Nullable | Available on list rows without a separate GET by ID. |
| `Result[].FirstPartyDataIds` | `firstPartyData` | N/A | N/A | Flat ID lists not available on list nodes; use the `firstPartyData` connection. |
| `Result[].ThirdPartyDataIds` | `thirdPartyData` | N/A | N/A | Flat ID lists not available on list nodes; use the `thirdPartyData` connection. |
| `Result[].SkipUnauthorizedThirdPartyData` | N/A | N/A | N/A | Write-only on create/update; not populated on read responses. |
| `Result[].GeoForCounts` | N/A | N/A | N/A | Deprecated on query result rows in REST; not surfaced. Use GET `/v3/datagroup/{id}` count fields on the entity. |
| `Result[].UniqueUserCount` | N/A | N/A | N/A | Deprecated on query result rows in REST; not surfaced. Use GET `/v3/datagroup/{id}` count fields on the entity. |
| `Result[].PersonsCount` | N/A | N/A | N/A | Deprecated on query result rows in REST; not surfaced. Use GET `/v3/datagroup/{id}` count fields on the entity. |
| `Result[].HouseholdCount` | N/A | N/A | N/A | Deprecated on query result rows in REST; not surfaced. Use GET `/v3/datagroup/{id}` count fields on the entity. |
| `Result[].SuccessfullyRetrievedCounts` | N/A | N/A | N/A | Deprecated on query result rows in REST; not surfaced. Use GET `/v3/datagroup/{id}` count fields on the entity. |

## Endpoint-specific nested types and enums

### DataGroupSortFieldInput

| REST value | GraphQL enum value | Notes |
| --- | --- | --- |
| `Name` | `NAME` | Default sort when `sortFields` is omitted. |
| `Description` | `DESCRIPTION` | N/A |

## Code examples

### REST example

```
POST /v3/datagroup/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<advertiser-id>",
  "PageStartIndex": 0,
  "PageSize": 10,
  "SearchTerms": ["audience"],
  "SortFields": [{ "FieldId": "Name", "Ascending": true }]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserDataGroups {
  advertiser(id: "<advertiser-id>") {
    dataGroups(
      first: 10
      searchTerms: ["audience"]
      sortFields: [{ fieldId: NAME, ascending: true }]
    ) {
      totalCount
      nodes {
        id
        name
        isSharable
      }
    }
  }
}
```
