# POST /v3/delta/creative/query/advertiser → Query.creativeDelta

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-delta-creative-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/delta/creative/query/advertiser → Query.creativeDelta

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/delta/creative/query/advertiser` |
| GraphQL query | `Query.creativeDelta` |
| Return type | `CreativeDelta` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `input.advertiser.changeTrackingVersion` | Long! | Optional | REST optional long? defaults when omitted; GraphQL requires non-null Long |
| `AdvertiserId` | `input.advertiser.ids` | [ID!] | Optional | REST single optional/required ID → GraphQL IDs list (wrap single value in array) REST AdvertiserId maps to one element in AdvertiserDeltaInput.ids. |
| `ReturnEntireCreative` | N/A | N/A | Optional | GraphQL delta always returns full entity objects; no IDs-only mode. |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `pageSize` | Int | Placement: `input.advertiser.pageSize`. GraphQL-only pagination control; REST delta has implicit paging via More*Available without explicit page size on most endpoints. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `currentMinimumTrackingVersion` | Long! | Not nullable | REST single version → GraphQL splits into `currentMinimumTrackingVersion` and `nextChangeTrackingVersion`. |
| `LastChangeTrackingVersion` | `nextChangeTrackingVersion` | Long! | Not nullable | GraphQL-only companion cursor for subsequent delta calls. |
| `ElementIds` | N/A | N/A | N/A | GraphQL always returns full entity objects; derive IDs from `creatives[].id`. |
| `Creatives` | `creatives` | [Creative!]! | Not nullable | REST `Creatives` → `Creative` entities in `creatives`. |
| `MoreCreativesAvailable` | `moreAvailable` | Boolean! | Not nullable | N/A |
| `Creatives[].CreativeId` | `id` | ID! | Not nullable | Entity key. |
| `Creatives[].CreativeName` | `name` | String | Nullable | N/A |
| `Creatives[].Description` | `description` | String | Nullable | N/A |
| `Creatives[].FlightStartDateUTC` | `flightStart` | DateTime | Nullable | N/A |
| `Creatives[].FlightEndDateUTC` | `flightEnd` | DateTime | Nullable | N/A |
| `Creatives[].CreatedAtUTC` | `createdAt` | DateTime! | Not nullable | N/A |
| `Creatives[].LastUpdatedAtUTC` | `lastUpdatedAt` | DateTime! | Not nullable | N/A |
| `Creatives[].AdvertiserId` | `advertiser.id` | ID! | Not nullable | Nested on `advertiser`. |
| `Creatives[].CreativeType` | `type` | CreativeType! | Not nullable | N/A |
| `Creatives[].Availability` | `isArchived` | Boolean! | Not nullable | REST availability maps to archive state (`Available` → `false`, `Archived` → `true`). |
| `Creatives[].ShareLink` | `shareLink` | String! | Not nullable | N/A |
| `Creatives[].CreativeAuditStatuses` | `auditStatuses` | AuditStatuses | Nullable | See AuditStatuses nested table. |
| `Creatives[].PoliticalDataId` | `politicalAdIcon.politicalDataId` | ID! | Not nullable | Nested on `politicalAdIcon` when present. |
| `Creatives[].DynamicCreativeRuleId` | `dynamicCreativeOptimizationRule.id` | ID | Nullable | On the `Creative` interface. |
| `Creatives[].MiaozhenMonitoringProduct` | `enabledMiaozhenProduct` | Byte! | Not nullable | On `HostedAudioCreative`, `HostedDisplayCreative`, and `HostedVideoCreative` concrete types. |
| `Creatives[].WillThisBeServedInChina` | N/A | N/A | N/A | Create-only |
| `Creatives[].VioohReviewRequired` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Creatives[].VioohSelectedPublisher` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Creatives[].UcfunnelReviewRequired` | N/A | N/A | N/A | Not currently available in GraphQL |

### Format-specific REST *attributes wrappers (creatives[])

REST returns exactly one `*Attributes` wrapper per creative. GraphQL flattens those leaves onto concrete `Creative` implementors—query the matching type with an inline fragment.

| REST attributes wrapper | GraphQL concrete type | Notes |
| --- | --- | --- |
| ImageAttributes | `HostedDisplayCreative` | Image URL, dimensions, clickthrough, landing page, and related leaves. |
| ThirdPartyTagAttributes | `ThirdPartyDisplayCreative` | Ad tag, dimensions, landing pages, MRAID version, and related leaves. |
| TradeDeskHostedVideoAttributes | `HostedVideoCreative` | VAST tag, duration, companions, encoding status, and related leaves. |
| TradeDeskHostedAudioAttributes | `HostedAudioCreative` | Audio VAST/DAAST tag, duration, and related leaves. |
| ThirdPartyHostedVideoAttributes | `ThirdPartyVideoCreative` | Third-party VAST tag and related leaves. |
| ThirdPartyHostedAudioAttributes | `ThirdPartyAudioCreative` | Third-party audio tag and related leaves. |
| Html5Attributes | `HostedHtml5Creative` | HTML5 asset URL, dimensions, and related leaves. |
| HostedNativeAttributes | `HostedNativeCreative` | Hosted native asset fields and related leaves. |
| HostedNativeWithThirdPartyVideoAttributes | `HostedNativeVideoCreative` | Hosted native assets with hosted or third-party video leaves. |
| ThirdPartyNativeAttributes | `ThirdPartyDisplayCreative` | Third-party native asset URL and related leaves (when applicable). |
| FacebookAttributes | N/A | Deprecated on REST |
| FacebookPagePostAttributes | N/A | Deprecated on REST |
| FlashAttributes | N/A | Deprecated on REST |

## Endpoint-specific nested types and enums

### ImageAttributes → HostedDisplayCreative

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ImageUrl` | `imageUrl` | String | Nullable | Query via `... on HostedDisplayCreative`. Dimensions live on `adFormat`, not flat width/height scalars. |
| `ClickthroughUrl` | `clickthroughUrl` | String | Nullable | N/A |
| `LandingPageUrl` | `landingPageUrl` | String! | Not nullable | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Nullable | REST impression URLs map to `pixelImpressionTrackingUrl1` / `2` / `3`. |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Nullable | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Nullable | N/A |
| `ThirdPartyClickTrackingUrl` | `thirdPartyClickTrackingUrl` | String | Nullable | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!]! | Not nullable | N/A |
| `IsSecurable` | `isSecurable` | Boolean | Nullable | N/A |
| `AdServerName` | `adServerName` | String | Nullable | N/A |
| `AdServerCreativeId` | `adServerCreativeId` | ID | Nullable | N/A |

### CreativeDeepLink (REST: CreativeDeepLinkAttributes)

REST nests links under `UriScheme` and `UniversalLink`. GraphQL exposes a flat `deepLinks` array on supported concrete types; each entry has `link` and `linkType`.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `UriScheme.Link` | `link` | String! | Not nullable | Where `linkType` is `URI_SCHEME`. |
| `UniversalLink.Link` | `link` | String! | Not nullable | Where `linkType` is `UNIVERSAL_LINK`. |
| N/A | `linkType` | DeepLinkType! | Not nullable | `URI_SCHEME` or `UNIVERSAL_LINK`. |

### AuditStatuses (REST: CreativeAuditStatuses list)

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| (list items) | `supplyVendorAuditStatuses` | [SupplyVendorAuditStatus!]! | Not nullable | Per-supply-vendor audit rows. |
| (list items) | `supplyVendorPublisherAuditStatuses` | [SupplyVendorPublisherAuditStatus!]! | Not nullable | Per-publisher audit rows. |

## Code examples

The following are examples of querying creative deltas for an advertiser with REST and GraphQL.

Basic delta query:

### REST example

```
POST /v3/delta/creative/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "LastChangeTrackingVersion": null,
  "AdvertiserId": "example-id",
  "ReturnEntireCreative": false
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CreativeDelta {
  creativeDelta(input: {
    advertiser: {
      changeTrackingVersion: 0
      ids: ["adv123"]
      pageSize: 100
    }
  }) {
    currentMinimumTrackingVersion
    nextChangeTrackingVersion
    moreAvailable
    creatives {
      id
      name
      type
      isArchived
      advertiser { id }
    }
  }
}
```

Format-specific creative fields (ImageAttributes equivalent):

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CreativeDeltaFormatFields {
  creativeDelta(input: {
    advertiser: {
      changeTrackingVersion: 0
      ids: ["adv123"]
      pageSize: 10
    }
  }) {
    creatives {
      id
      name
      type
      shareLink
      auditStatuses {
        supplyVendorAuditStatuses {
          auditStatusEnum
          supplyVendor { id }
        }
      }
      ... on HostedDisplayCreative {
        imageUrl
        clickthroughUrl
        landingPageUrl
        pixelImpressionTrackingUrl1
        thirdPartyClickTrackingUrl
        deepLinks {
          link
          linkType
        }
        enabledMiaozhenProduct
      }
      ... on HostedVideoCreative {
        durationInSeconds
        vastPreviewUrl
        enabledMiaozhenProduct
      }
    }
  }
}
```
