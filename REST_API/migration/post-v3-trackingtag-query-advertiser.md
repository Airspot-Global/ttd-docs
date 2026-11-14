# POST /v3/trackingtag/query/advertiser → Advertiser tracking tag connections

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-trackingtag-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/trackingtag/query/advertiser → Advertiser tracking tag connections

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/trackingtag/query/advertiser` |
| GraphQL query | `Advertiser.availableTrackingTags`, `Advertiser.ownedTrackingTags`, or `Query.trackingTags` |
| Return type | `AdvertiserAvailableTrackingTagsConnection`, `OwnedTrackingTagsConnection`, or `TrackingTagsConnection` |

## Multi-step operations

This REST list endpoint maps to one of several GraphQL entry points:

| REST concern | GraphQL entry point | Notes |
| --- | --- | --- |
| Advertiser-scoped list (owned + shared) | `Advertiser.availableTrackingTags` | Includes owned and shared tags. |
| Advertiser-scoped list (owned only) | `Advertiser.ownedTrackingTags` | Owned tags only. |
| Top-level filtered list | `Query.trackingTags(where: { advertiserId: { eq: "..." } })` | Uses `TrackingTagsFilterInput`. |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `Advertiser.availableTrackingTags` or `Advertiser.ownedTrackingTags` | `ID!` | Required | `availableTrackingTags` includes owned + shared tags; `ownedTrackingTags` is owned only. |
| `AdvertiserId` | Alternative: `Query.trackingTags(where: { advertiserId: { eq: "..." } })` | `ID!` | Required | Top-level; uses `TrackingTagsFilterInput`. |
| `PageStartIndex` | `after` | `String` | Optional | N/A |
| `PageSize` | `first` | `Int` | Optional | N/A |
| `SearchTerms` | `where: { and: [{ name: { contains: "..." } }, { id: { contains: "..." } }] }` | Filter input | Optional | REST matches ID **or** name **or** location with AND across terms; compose with `or`/`and` on `name` and `id` in GraphQL. No `location` filter field exists on `TrackingTagsFilterInput` or `TrackingTagFilterInput`. No single combined `searchTerms` arg. |
| `SortFields` | `order: [{ name: ASC }]` | `[TrackingTagSortInput!]` | Optional | Use `TrackingTagSortInput`; sort enums from schema introspection. |
| `TrackingTagTypes` | `where: { trackingTagTypeId: { in: [...] } }` | Filter input | Optional | Map enum to underlying type ID strings. |
| `TrackingTagAvailabilities` | `where: { isArchived: { eq: false } }` | Filter input | Optional | REST defaults to Available only; mirror with `isArchived`. |
| `IncludeOfflineTrackingTags` | Filter via `offlineDataProviderId` / `category` | Filter input | Optional | REST excludes offline tags when `false` (default). GraphQL returns offline rows in the same connections; filter with category traversal or `offlineDataProviderId: { eq: null }` if supported. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[TrackingTag!]` | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | `Int!` | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].TrackingTagId` | `id` | `String!` | Not nullable | N/A |
| `Result[].TrackingTagName` | `name` | `String!` | Not nullable | N/A |
| `Result[].TrackingTagType` | `type` | `TrackingTagType!` | Not nullable | See domain `TrackingTagType` enum mapping. |
| `Result[].TrackingTagCategory` | `category` | `TrackingTagCategory!` | Not nullable | See domain `TrackingTagCategory` enum mapping. |
| `Result[].AdvertiserId` | `advertiser { id }` | `Advertiser!` | Not nullable | **Remodelled in GraphQL** |
| `Result[].TrackingTagLocation` | `location` | `String` | Nullable | N/A |
| `Result[].Revenue` | `revenue` | `String` | Nullable | N/A |
| `Result[].Currency` | `currency` | `String` | Nullable | N/A |
| `Result[].ContainerTagBody` | `containerTagBody` | `String` | Nullable | N/A |
| `Result[].FirstPartyDataId` | `firstPartyData { id }` | `FirstPartyData!` | Not nullable | Read-only in REST. |
| `Result[].TrackingTagAvailability` | `isArchived` | `Boolean!` | Not nullable | `Available` → `false`; `Archived` → `true`. |
| `Result[].OfflineDataProviderId` | `offlineDataProvider { id }` | `OfflineDataProvider` | Nullable | Read-only; populated when category is offline. |
| `Result[].UniversalPixelName` | `universalPixel { name }` | `UniversalPixel` | Nullable | Read-only. |
| `Result[].HitCount7Day` | `hitCount7Day` | `Long` | Nullable | GraphQL also exposes `hitCount1Day`, `hitCount30Day`. |
| `Result[].TagRedirectUri` | `redirectUri` | `String` | Nullable | N/A |
| `Result[].HouseholdEnabled` | `householdEnabled` | `Boolean!` | Not nullable | REST `Optional<bool>`; GraphQL field is non-null. |
| `Result[].ImageTag` | `imageTag` | `String` | Nullable | Read-only. |
| `Result[].IFrameTag` | `iFrameTag` | `String` | Nullable | Read-only. |
| `Result[].DataEventTypeId` | `dataEventType` | `DataEventType` | Nullable | Enum scalar; see `GET /v3/trackingtag/{trackingTagId}` `DataEventType` mapping. |

## Code examples

### REST example

```
POST /v3/trackingtag/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "abc123",
  "PageStartIndex": 0,
  "PageSize": 25,
  "TrackingTagAvailabilities": ["Available"]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserTrackingTags($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    availableTrackingTags(first: 25, where: { isArchived: { eq: false } }) {
      totalCount
      nodes {
        id
        name
        type
        category
      }
    }
  }
}
```
