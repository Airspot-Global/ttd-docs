# GET /v3/trackingtag/{trackingTagId} → Query.trackingTag

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-trackingtag-trackingtagid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/trackingtag/{trackingTagId} → Query.trackingTag

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/trackingtag/{trackingTagId}` |
| GraphQL query | `Query.trackingTag(id:)` |
| Return type | `TrackingTag` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser { id }` | `Advertiser!` | Not nullable | **Remodelled in GraphQL**—use `advertiser { id }`. |
| `TrackingTagId` | `id` | `String!` | Not nullable | N/A |
| `TrackingTagName` | `name` | `String!` | Not nullable | N/A |
| `TrackingTagType` | `type` | `TrackingTagType!` | Not nullable | N/A |
| `TrackingTagLocation` | `location` | `String` | Nullable | N/A |
| `Revenue` | `revenue` | `String` | Nullable | N/A |
| `Currency` | `currency` | `String` | Nullable | N/A |
| `ContainerTagBody` | `containerTagBody` | `String` | Nullable | N/A |
| `FirstPartyDataId` | `firstPartyData { id }` | `FirstPartyData!` | Not nullable | Read-only in REST. |
| `TrackingTagCategory` | `category` | `TrackingTagCategory!` | Not nullable | e.g. `STATIC_TAG`, `OFFLINE_TAG`, `UNIVERSAL_PIXEL_TAG`, `APP_EVENT_TRACKER_TAG`. |
| `TrackingTagAvailability` | `isArchived` | `Boolean!` | Not nullable | `Available` → `false`; `Archived` → `true`. |
| `OfflineDataProviderId` | `offlineDataProvider { id }` | `OfflineDataProvider` | Nullable | Read-only; populated when category is offline. |
| `UniversalPixelName` | `universalPixel { name }` | `UniversalPixel` | Nullable | Read-only. |
| `HitCount7Day` | `hitCount7Day` | `Long` | Nullable | GraphQL also exposes `hitCount1Day`, `hitCount30Day`. |
| `TagRedirectUri` | `redirectUri` | `String` | Nullable | N/A |
| `HouseholdEnabled` | `householdEnabled` | `Boolean!` | Not nullable | REST `Optional<bool>`; GraphQL field is non-null. |
| `ImageTag` | `imageTag` | `String` | Nullable | Read-only. |
| `IFrameTag` | `iFrameTag` | `String` | Nullable | Read-only. |
| `DataEventTypeId` | `dataEventType` | `DataEventType` | Nullable | Enum scalar; see mapping table below. |

## Endpoint-specific nested types and enums

### DataEventType

REST `TrackingDataEventTypeId` serializes as PascalCase; GraphQL `DataEventType` uses `SCREAMING_SNAKE_CASE`.

| REST value | GraphQL value |
| --- | --- |
| `AddToCart` | `ADD_TO_CART` |
| `Purchase` | `PURCHASE` |
| `ViewItem` | `VIEW_ITEM` |
| `SearchItem` | `SEARCH_ITEM` |
| `SearchCategory` | `SEARCH_CATEGORY` |
| `Login` | `LOGIN` |
| `MessageBusiness` | `MESSAGE_BUSINESS` |
| `Direction` | `DIRECTION` |
| `StartCheckout` | `START_CHECKOUT` |
| `ViewCart` | `VIEW_CART` |
| `SiteVisit` | `SITE_VISIT` |
| `WishListItem` | `WISH_LIST_ITEM` |
| `SubscribeToNewsletter` | `SUBSCRIBE_TO_NEWSLETTER` |
| `LoyaltyMembers` | `LOYALTY_MEMBERS` |
| `Other` | `OTHER` |

## Code examples

### REST example

```
GET /v3/trackingtag/{trackingTagId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetTrackingTag($id: String!) {
  trackingTag(id: $id) {
    id
    name
    type
    category
    location
    revenue
    currency
    containerTagBody
    redirectUri
    householdEnabled
    isArchived
    hitCount7Day
    imageTag
    iFrameTag
    advertiser { id }
    firstPartyData { id }
    offlineDataProvider { id }
    universalPixel { name }
    dataEventType
  }
}
```
