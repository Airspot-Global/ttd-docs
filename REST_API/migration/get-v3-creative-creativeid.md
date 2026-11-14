# GET /v3/creative/{creativeId} → Creative

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-creative-creativeid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/creative/{creativeId} → Creative

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/creative/{creativeId}` |
| GraphQL query | `Creative` (via entity lookup by `id`) |
| Return type | `Creative` |

Returns the full creative entity by ID. Readable scalars resolve on the `Creative` interface; format-specific attribute leaves and some nested collections resolve on concrete implementors via inline fragments.

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CreativeId` | `id` | ID! | Not nullable | Entity key. |
| `CreativeName` | `name` | String | Nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `FlightStartDateUTC` | `flightStart` | DateTime | Nullable | N/A |
| `FlightEndDateUTC` | `flightEnd` | DateTime | Nullable | N/A |
| `CreatedAtUTC` | `createdAt` | DateTime! | Not nullable | N/A |
| `LastUpdatedAtUTC` | `lastUpdatedAt` | DateTime! | Not nullable | N/A |
| `AdvertiserId` | `advertiser.id` | ID! | Not nullable | Nested on `advertiser`. |
| `CreativeType` | `type` | CreativeType! | Not nullable | N/A |
| `Availability` | `isArchived` | Boolean! | Not nullable | REST availability maps to archive state (`Available` → `false`, `Archived` → `true`). |
| `ShareLink` | `shareLink` | String! | Not nullable | N/A |
| `CreativeAuditStatuses` | `auditStatuses` | AuditStatuses | Nullable | Object—select `supplyVendorAuditStatuses` and/or `supplyVendorPublisherAuditStatuses`. |
| `PoliticalDataId` | `politicalAdIcon.politicalDataId` | ID! | Not nullable | Nested on `politicalAdIcon` when present. |
| `DynamicCreativeRuleId` | `dynamicCreativeOptimizationRule.id` | ID! | Not nullable | On the `Creative` interface. Some concrete types also expose `dynamicCreativeRules[].id`. |
| `MiaozhenMonitoringProduct` | `enabledMiaozhenProduct` | Byte! | Not nullable | On `HostedAudioCreative`, `HostedDisplayCreative`, and `HostedVideoCreative` concrete types. |
| `UcfunnelReviewRequired` | N/A | N/A | N/A | Not currently available in GraphQL |
| `VioohReviewRequired` | N/A | N/A | N/A | Not currently available in GraphQL |
| `VioohSelectedPublisher` | N/A | N/A | N/A | Not currently available in GraphQL |
| `WillThisBeServedInChina` | N/A | N/A | N/A | Create-only |

### Format-specific REST *attributes wrappers

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

### REST example

```
GET /v3/creative/{creativeId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCreativeById($id: ID!) {
  creative(id: $id) {
    id
    name
    description
    flightStart
    flightEnd
    createdAt
    lastUpdatedAt
    type
    isArchived
    shareLink
    advertiser {
      id
    }
    politicalAdIcon {
      politicalDataId
    }
    dynamicCreativeOptimizationRule {
      id
    }
    auditStatuses {
      supplyVendorAuditStatuses {
        auditStatusEnum
        supplyVendor {
          id
        }
      }
    }
    ... on HostedDisplayCreative {
      imageUrl
      deepLinks {
        link
        linkType
      }
      enabledMiaozhenProduct
    }
  }
}
```
