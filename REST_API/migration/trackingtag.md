# Tracking tag: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/trackingtag-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Tracking tag: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/trackingtag/{trackingTagId}` | `Query.trackingTag(id:)` | N/A |
| `POST /v3/trackingtag/query/advertiser` | `Advertiser.availableTrackingTags`, `Advertiser.ownedTrackingTags`, or `Query.trackingTags` | N/A |
| `GET /v3/offlinetrackingtag/{trackingTagId}` | `Query.trackingTag(id:)` | Offline category / `OfflineTrackingTag` |
| `POST /v3/offlinetrackingtag/query/advertiser` | `Query.trackingTags` or `Advertiser.availableTrackingTags` | Requires advertiser and offline data provider filters |
| `POST /v3/trackingtag` | `trackingTagCreate` | N/A |
| `PUT /v3/trackingtag` | `trackingTagUpdate` | N/A |

## Shared nested types and enums

### TrackingTagCategory

| REST value | GraphQL value |
| --- | --- |
| `StaticTag` | `STATIC_TAG` |
| `AppEventTrackerTag` | `APP_EVENT_TRACKER_TAG` |
| `UniversalPixelTag` | `UNIVERSAL_PIXEL_TAG` |
| `OfflineTag` | `OFFLINE_TAG` |

### TrackingTagType

| REST value | GraphQL value |
| --- | --- |
| `Impression` | `IMPRESSION` |
| `Retargeting` | `RETARGETING` |
| `Conversion` | `CONVERSION` |

### TrackingTagTypeREST

| REST value | GraphQL value |
| --- | --- |
| `Impression` | `IMPRESSION` |
| `Retargeting` | `RETARGETING` |
| `Conversion` | `CONVERSION` |

### TrackingDataEventTypeIdREST

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

### AvailabilityREST

| REST value | GraphQL value |
| --- | --- |
| `Available` | `AVAILABLE` |
| `Archived` | `ARCHIVED` |
