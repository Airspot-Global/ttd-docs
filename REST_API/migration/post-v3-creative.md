# POST /v3/creative → creativeCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-creative
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/creative → creativeCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/creative` |
| GraphQL operation | `creativeCreate` |
| Input type | `CreativeCreateInput` |
| Output type | `CreativeCreatePayload` (`creativeCreateResult: CreativeCreateResult`, `errors: [CreativeCreateError!]`) |

`creativeCreate` uses format-specific `*Options` inputs and a required `creativeType` enum—not a 1:1 mirror of REST's single `*Attributes` wrapper. Set exactly one `*Options` field matching `creativeType`.

## Multi-step operations

For hosted **video** or **audio** creatives, upload the media file before calling create:

1. Call `creativeCreatePresignedUrlGenerate` (REST: `POST /v3/creative/generateuploadurlforvideocreative` or `.../generateuploadurlforaudiocreative`) to obtain a presigned upload URL.
2. Upload the media file to that URL.
3. Call `creativeCreate` with the public asset URL in the matching `*Options.assetUrl` (or `hostedNativeVideoOptions.videoAssetUrl`).

## Input field mapping

Input type: `CreativeCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID! | Required | N/A |
| `CreativeId` | N/A | N/A | Optional | Read-only |
| `CreativeName` | `name` | String! | Required | Max 256 characters. |
| `Description` | `description` | String | Optional | Max 512 characters. |
| `CreativeType` | `creativeType` | CreativeTypeInput! | Required | Required on GraphQL create; set to match the chosen `*Options` input. |
| `ImageAttributes` | `hostedDisplayOptions` | HostedDisplayOptionsInput | Optional | Set `creativeType: HOSTED_DISPLAY`. Exactly one `*Options` input required. |
| `FacebookAttributes` | N/A | N/A | Optional | Deprecated on REST |
| `FacebookPagePostAttributes` | N/A | N/A | Optional | Deprecated on REST |
| `FlashAttributes` | N/A | N/A | Optional | Deprecated on REST |
| `ThirdPartyTagAttributes` | `thirdPartyDisplayOptions` | ThirdPartyDisplayOptionsInput | Optional | Set `creativeType: THIRD_PARTY_DISPLAY`. |
| `TradeDeskHostedAudioAttributes` | `hostedAudioOptions` | HostedAudioOptionsInput | Optional | Set `creativeType: HOSTED_AUDIO`. |
| `TradeDeskHostedVideoAttributes` | `hostedVideoOptions` | HostedVideoOptionsInput | Optional | Set `creativeType: HOSTED_VIDEO`. |
| `ThirdPartyHostedVideoAttributes` | `thirdPartyVideoOptions` | ThirdPartyVideoOptionsInput | Optional | Set `creativeType: THIRD_PARTY_VIDEO`. |
| `ThirdPartyHostedAudioAttributes` | `thirdPartyAudioOptions` | ThirdPartyAudioOptionsInput | Optional | Set `creativeType: THIRD_PARTY_AUDIO`. |
| `Html5Attributes` | `hostedHtml5Options` | HostedHtml5OptionsInput | Optional | Set `creativeType: HOSTED_HTML5`. |
| `HostedNativeAttributes` | `hostedNativeOptions` | HostedNativeOptionsInput | Optional | Set `creativeType: HOSTED_NATIVE`. |
| `ThirdPartyNativeAttributes` | N/A | N/A | Optional | Not currently available in GraphQL |
| `HostedNativeWithThirdPartyVideoAttributes` | `hostedNativeVideoOptions` | HostedNativeVideoOptionsInput | Optional | Set `creativeType: HOSTED_NATIVE_VIDEO`. |
| `BroadcasterHostedVideo` (read-only REST `CreativeType`) | `broadcasterHostedVideoOptions` | BroadcasterHostedVideoOptionsInput | Optional | GraphQL-only create path; set `creativeType: BROADCASTER_HOSTED_VIDEO`. REST POST has no dedicated attributes wrapper—broadcasters are created via GraphQL or platform workflows. |
| `CreativeAuditStatuses` | N/A | N/A | Optional | Read-only |
| `FlightStartDateUTC` | `flightStartDate` | DateTime | Optional | Also accepts `flightStart`. |
| `FlightEndDateUTC` | `flightEndDate` | DateTime | Optional | Also accepts `flightEnd`. |
| `Availability` | N/A | N/A | Optional | Cannot set `Archived` on create. |
| `CreatedAtUTC` | N/A | N/A | Optional | Read-only |
| `LastUpdatedAtUTC` | N/A | N/A | Optional | Read-only |
| `ShareLink` | N/A | N/A | Optional | Read-only |
| `WillThisBeServedInChina` | `willThisBeServedInChina` | Boolean | Optional | Once set to `true`, cannot revert to `false`. |
| `VioohReviewRequired` | N/A | N/A | Optional | No `CreativeCreateInput` field; use `submitCreativeForApproval` with `submitToVioohForReview` after create. |
| `VioohSelectedPublisher` | `hostedDisplayOptions.vioohPublisherToSubmitTo` / `hostedVideoOptions.vioohPublisherToSubmitTo` | String | Optional | VIOOH seller ID on hosted display or video format options. |
| `UcfunnelReviewRequired` | N/A | N/A | Optional | Not currently available in GraphQL |
| `PoliticalDataId` | `politicalDataId` | ID | Optional | Required for political advertising creatives. |
| `DynamicCreativeRuleId` | `thirdParty*Options.dynamicCreativeRuleId` | String | Optional | On third-party format options. |
| `MiaozhenMonitoringProduct` | `enabledMiaozhenProduct` | Byte | Optional | China OTP monitoring product on `CreativeCreateInput`. |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `autoApprove` | Boolean! |  |
| `isDryRun` | Boolean! | When `true`, validates without creating. |
| `creativeLabels` | [String!] |  |
| `flightTimeZoneIANA` | String |  |
| `adServerCreativeId` | String |  |

### Migration notes

- Exactly one `*Options` property must be provided and must match `creativeType`. The creative type cannot be changed after creation.
- `FacebookAttributes`, `FacebookPagePostAttributes`, and `FlashAttributes` are deprecated and rejected on create.
- Once `willThisBeServedInChina` is set to `true`, it cannot be reverted to `false`.
- REST `ImageContent` (base64) has no GraphQL equivalent—use `creativeCreatePresignedUrlGenerate` + `assetUrl` for hosted assets.

## Output field mapping

Output type: `Creative` (returned as `creativeCreateResult.creative` on `CreativeCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CreativeId` | `creative.id` | ID! | Not nullable | Also on `creative.id`. |
| `AdvertiserId` | `creative.advertiser.id` | ID! | Not nullable | Nested on `advertiser`. |
| `CreativeName` | `creative.name` | String | Nullable | N/A |
| `Description` | `creative.description` | String | Nullable | N/A |
| `CreativeType` | `creative.type` | CreativeType! | Not nullable | N/A |
| `ImageAttributes` | `HostedDisplayCreative` fragment | N/A | N/A | Query with inline fragment; see GET doc. |
| `ThirdPartyTagAttributes` | `ThirdPartyDisplayCreative` fragment | N/A | N/A | N/A |
| `TradeDeskHostedVideoAttributes` | `HostedVideoCreative` fragment | N/A | N/A | N/A |
| `TradeDeskHostedAudioAttributes` | `HostedAudioCreative` fragment | N/A | N/A | N/A |
| `ThirdPartyHostedVideoAttributes` | `ThirdPartyVideoCreative` fragment | N/A | N/A | N/A |
| `ThirdPartyHostedAudioAttributes` | `ThirdPartyAudioCreative` fragment | N/A | N/A | N/A |
| `Html5Attributes` | `HostedHtml5Creative` fragment | N/A | N/A | N/A |
| `HostedNativeAttributes` | `HostedNativeCreative` fragment | N/A | N/A | N/A |
| `ThirdPartyNativeAttributes` | `ThirdPartyDisplayCreative` fragment | N/A | N/A | Not currently available in GraphQL |
| `HostedNativeWithThirdPartyVideoAttributes` | `HostedNativeVideoCreative` fragment | N/A | N/A | N/A |
| `BroadcasterHostedVideo` (REST `CreativeType`) | `BroadcasterHostedVideoCreative` fragment | N/A | N/A | Query with inline fragment. |
| `FacebookAttributes` | N/A | N/A | N/A | Deprecated on REST |
| `FacebookPagePostAttributes` | N/A | N/A | N/A | Deprecated on REST |
| `FlashAttributes` | N/A | N/A | N/A | Deprecated on REST |
| `CreativeAuditStatuses` | `creative.auditStatuses` | AuditStatuses | Nullable | N/A |
| `FlightStartDateUTC` | `creative.flightStart` | DateTime | Nullable | N/A |
| `FlightEndDateUTC` | `creative.flightEnd` | DateTime | Nullable | N/A |
| `Availability` | `creative.isArchived` | Boolean! | Not nullable | `Available` → `false`, `Archived` → `true`. |
| `CreatedAtUTC` | `creative.createdAt` | DateTime! | Not nullable | N/A |
| `LastUpdatedAtUTC` | `creative.lastUpdatedAt` | DateTime! | Not nullable | N/A |
| `ShareLink` | `creative.shareLink` | String! | Not nullable | N/A |
| `WillThisBeServedInChina` | N/A | N/A | N/A | Create-only |
| `VioohReviewRequired` | N/A | N/A | N/A | Not currently available in GraphQL |
| `VioohSelectedPublisher` | N/A | N/A | N/A | Not currently available in GraphQL |
| `UcfunnelReviewRequired` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PoliticalDataId` | `creative.politicalAdIcon.politicalDataId` | ID | Nullable | N/A |
| `DynamicCreativeRuleId` | `creative.dynamicCreativeOptimizationRule.id` | ID | Nullable | N/A |
| `MiaozhenMonitoringProduct` | `enabledMiaozhenProduct` on concrete types | Byte! | Not nullable | On hosted audio/display/video types. |

## Endpoint-specific nested types and enums

### HostedDisplayOptionsInput (REST: ImageAttributes)

Set with `creativeType: HOSTED_DISPLAY`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `ImageContent` | N/A | N/A | Required | REST base64 upload; GraphQL uses `assetUrl` from presigned upload. |
| `ClickthroughUrl` | `clickthroughUrl` | String! | Required | N/A |
| `LandingPageUrl` | `landingPageUrl` | String! | Required | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| Width / Height / ImageUrl | N/A | N/A | Optional | Read-only |
| `AdTechnologyIds` | N/A | N/A | Optional | Read-only |

### ThirdPartyDisplayOptionsInput (REST: ThirdPartyTagAttributes)

Set with `creativeType: THIRD_PARTY_DISPLAY`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdTag` | `adTag` | String! | Required | N/A |
| `Width` | `width` | Int! | Required | N/A |
| `Height` | `height` | Int! | Required | N/A |
| `LandingPageUrls` | `landingPageUrls` | [String!]! | Required | N/A |
| `AdServerName` | `adServerName` | String | Optional | N/A |
| `AdServerCreativeId` | `adServerCreativeId` | String | Optional | N/A |
| `MraidVersion` | `mraidVersionId` | Int | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| `DynamicCreativeRuleId` | `dynamicCreativeRuleId` | String | Optional | On third-party options. |

### HostedVideoOptionsInput (REST: TradeDeskHostedVideoAttributes)

Set with `creativeType: HOSTED_VIDEO`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| VideoUploadAttributes (from presigned URL) | `assetUrl` | String! | Required | Public URL after presigned upload. |
| `ClickthroughUrl` | `clickthroughUrl` | String! | Required | N/A |
| `LandingPageUrl` | `landingPageUrl` | String! | Required | N/A |
| `Skippable` | `isSkippable` | Boolean | Optional | N/A |
| `SkipOffsetInSeconds` | `skipOffsetInSeconds` | Int | Optional | N/A |
| `CompanionCreativeIds` | `companionCreativeIds` | [ID!] | Optional | N/A |
| `TrackingEvents` | `playerTrackingEvents` | [TrackingEventInput!] | Optional | N/A |
| `IsVideoRetargetingEnabled` | `isRetargetingEnabled` | Boolean | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| UniversalAdId / UniversalAdIdRegistry | `universalAdId` | UniversalAdIdInput | Optional | N/A |

### HostedAudioOptionsInput (REST: TradeDeskHostedAudioAttributes)

Set with `creativeType: HOSTED_AUDIO`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| AudioUploadAttributes (from presigned URL) | `assetUrl` | String! | Required | Public URL after presigned upload. |
| `ClickthroughUrl` | `clickthroughUrl` | String! | Required | N/A |
| `LandingPageUrl` | `landingPageUrl` | String! | Required | N/A |
| `CompanionCreativeIds` | `companionCreativeIds` | [ID!] | Optional | N/A |
| `TrackingEvents` | `trackingEvents` | [TrackingEventInput!] | Optional | N/A |
| `IsAudioRetargetingEnabled` | `isRetargetingEnabled` | Boolean | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |

### ThirdPartyVideoOptionsInput (REST: ThirdPartyHostedVideoAttributes)

Set with `creativeType: THIRD_PARTY_VIDEO`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `VastTagUrl` | `vastXmlUrl` | String! | Required | N/A |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `DynamicCreativeRuleId` | `dynamicCreativeRuleId` | String | Optional | N/A |
| `IsVideoRetargetingEnabled` | `isRetargetingEnabled` | Boolean | Optional | N/A |
| `TrackingEvents` | `playerTrackingEvents` | [TrackingEventInput!] | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |

### ThirdPartyAudioOptionsInput (REST: ThirdPartyHostedAudioAttributes)

Set with `creativeType: THIRD_PARTY_AUDIO`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `VastOrDaastTagUrl` | `vastOrDaastUrl` | String! | Required | N/A |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `DynamicCreativeRuleId` | `dynamicCreativeRuleId` | String | Optional | N/A |
| `TrackingEvents` | `playerTrackingEvents` | [TrackingEventInput!] | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |

### HostedHtml5OptionsInput (REST: html5Attributes)

Set with `creativeType: HOSTED_HTML5`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| ZipFileContent / asset upload | `assetUrl` | String! | Required | Public URL after presigned upload. |
| `BackupImageContent` | `backupImageAssetUrl` | String | Optional | N/A |
| `ClickthroughUrl` | `clickthroughUrl` | String | Optional | N/A |
| `ClickTrackingParamName` | `clickTrackingParamName` | String! | Required | N/A |
| `WidthInPixels` | `widthInPixels` | Int! | Required | N/A |
| `HeightInPixels` | `heightInPixels` | Int! | Required | N/A |
| `LandingPageUrls` | `landingPageUrls` | [String!]! | Required | N/A |
| `UseClickthroughAsDefault` | `useClickthroughAsDefault` | Boolean! | Required | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |

### HostedNativeOptionsInput (REST: HostedNativeAttributes)

Set with `creativeType: HOSTED_NATIVE`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdServerName` | N/A | N/A | Optional | No field on `HostedNativeOptionsInput`. |
| `AdServerCreativeId` | N/A | N/A | Optional | N/A |
| `LandingPageUrl` | `landingPageUrl` | String! | Required | N/A |
| `ClickThroughUrl` | `clickthroughUrl` | String! | Required | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl4` | `pixelImpressionTrackingUrl4` | String | Optional | N/A |
| `TrackingEvents` | N/A | N/A | Optional | Not currently available in GraphQL |
| `TextAssets` | shortTitle / longTitle / sponsor / callToAction / price / shortDescription / longDescription | String | Optional | GraphQL flattens `TextAssets[]` by `TextAssetType`; see NativeTextAsset table. |
| `ImageAssets` (main) | `mainAssetUrls` | [String!]! | Required | GraphQL flattens `ImageAssets[]` with `ImageAssetType: ImageMain`; see NativeImageAsset table. |
| `ImageAssets` (icon) | `iconAssetUrl` | String | Optional | `ImageAssetType: ImageIcon`. |
| `ImageAssets` (logo) | `logoAssetUrl` | String | Optional | `ImageAssetType: ImageLogo`. |
| `DecimalAssets` | `rating` | Decimal | Optional | See NativeDecimalAsset table. |
| `VideoAsset` | N/A | N/A | Optional | Use `creativeType: HOSTED_NATIVE_VIDEO` and `hostedNativeVideoOptions`. |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| `IsPlayerRetargetingEnabled` | N/A | N/A | Optional | Use `hostedNativeVideoOptions.isRetargetingEnabled` for hosted native video. |

### ThirdPartyNativeAttributes (REST only)

REST `ThirdPartyNativeAttributes` has no GraphQL create input (`CreativeCreateInput` has no `thirdPartyNativeOptions` and `CreativeTypeInput` has no `THIRD_PARTY_NATIVE` member).

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdServerName` | N/A | N/A | Optional | Not currently available in GraphQL |
| `AdServerCreativeId` | N/A | N/A | Optional | N/A |
| `LandingPageUrl` | N/A | N/A | Required | N/A |
| `ClickThroughUrl` | N/A | N/A | Required | N/A |
| `AssetsUrl` | N/A | N/A | Required | N/A |
| `ThirdPartyImpressionTrackingUrl` | N/A | N/A | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | N/A | N/A | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | N/A | N/A | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl4` | N/A | N/A | Optional | N/A |
| `ThirdPartyTrackingTags` | N/A | N/A | Optional | N/A |

### HostedNativeVideoOptionsInput (REST: HostedNativeWithThirdPartyVideoAttributes)

Set with `creativeType: HOSTED_NATIVE_VIDEO`. REST `HostedNativeWithThirdPartyVideoAttributes` extends `HostedNativeAttributes` with a third-party `VideoVastUrl`; hosted native video uses the same GraphQL asset structure plus `videoAssetUrl`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `VideoVastUrl` (HostedNativeWithThirdPartyVideo only) | N/A | N/A | Optional | Not currently available in GraphQL |
| `VideoAsset` / video upload | `videoAssetUrl` | String! | Required | From presigned video upload. |
| `ImageAssets` (main) | `mainAssetUrls` | [String!]! | Required | Thumbnail assets from presigned upload. |
| `ImageAssets` (icon) | `iconAssetUrl` | String | Optional | N/A |
| `ImageAssets` (logo) | `logoAssetUrl` | String | Optional | N/A |
| `TextAssets` | shortTitle / longTitle / sponsor / callToAction / price / shortDescription / longDescription | String | Optional | See NativeTextAsset table. |
| `DecimalAssets` | `rating` | Decimal | Optional | See NativeDecimalAsset table. |
| `LandingPageUrl` | `landingPageUrl` | String! | Required | N/A |
| `ClickThroughUrl` | `clickthroughUrl` | String! | Required | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl4` | `pixelImpressionTrackingUrl4` | String | Optional | N/A |
| `TrackingEvents` | `playerTrackingEvents` | [TrackingEventInput!] | Optional | See TrackingEventInput table. |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| `IsPlayerRetargetingEnabled` | `isRetargetingEnabled` | Boolean | Optional | N/A |

### BroadcasterHostedVideoOptionsInput (GraphQL-only create)

Set with `creativeType: BROADCASTER_HOSTED_VIDEO`. REST exposes `BroadcasterHostedVideo` as a read-only `CreativeType` on `TradeDeskHostedVideoAttributes`; create via GraphQL.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| Video asset URLs | `assetUrls` | [String!]! | Required | Public CDN URLs for broadcaster-hosted video files. |
| `ClickthroughUrl` | `clickthroughUrl` | String! | Required | N/A |
| `LandingPageUrl` | `landingPageUrl` | String! | Required | N/A |
| `Skippable` | `isSkippable` | Boolean | Optional | N/A |
| `SkipOffsetInSeconds` | `skipOffsetInSeconds` | Int | Optional | N/A |
| `CompanionCreativeIds` | `companionCreativeIds` | [ID!] | Optional | N/A |
| `TrackingEvents` | `trackingEvents` | [TrackingEventInput!] | Optional | See TrackingEventInput table. |
| `IsVideoRetargetingEnabled` | `isPlayerRetargetingEnabled` | Boolean | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| `UniversalAdId` / `UniversalAdIdRegistry` | `universalAdId` | UniversalAdIdInput | Optional | See UniversalAdIdInput table. |

### TrackingEventInput (REST: VideoTrackingEvent)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `EventType` | `type` | TrackingEventType! | Required | REST `VideoTrackingEventType` maps to `TrackingEventType` enum (e.g. `Start` → `START`, `Complete` → `COMPLETE`). |
| `EventUrl` | `url` | String! | Required | N/A |

### UniversalAdIdInput

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `UniversalAdId` | `id` | String! | Required | N/A |
| `UniversalAdIdRegistry` | `registry` | String! | Required | N/A |

### NativeTextAsset (REST: NativeTextAsset)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `Text` + `TextAssetType: ShortTitle` | `shortTitle` | String | Optional | N/A |
| `Text` + `TextAssetType: LongTitle` | `longTitle` | String | Optional | N/A |
| `Text` + `TextAssetType: Sponsor` | `sponsor` | String! | Required | Required on GraphQL create. |
| `Text` + `TextAssetType: CallToAction` | `callToAction` | String | Optional | N/A |
| `Text` + `TextAssetType: Price` | `price` | String | Optional | N/A |
| `Text` + `TextAssetType: ShortDescription` | `shortDescription` | String | Optional | N/A |
| `Text` + `TextAssetType: LongDescription` | `longDescription` | String | Optional | N/A |

### NativeImageAsset (REST: NativeImageAsset)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `ImageContent` + `ImageAssetType: ImageMain` | `mainAssetUrls` | [String!]! | Required | REST base64 upload; GraphQL uses presigned-upload URLs. |
| `ImageContent` + `ImageAssetType: ImageIcon` | `iconAssetUrl` | String | Optional | N/A |
| `ImageContent` + `ImageAssetType: ImageLogo` | `logoAssetUrl` | String | Optional | N/A |
| `ImageFileName` | N/A | N/A | Required | Create-only |
| `WidthInPixel` / `HeightInPixel` | N/A | N/A | Optional | Read-only |
| `ImageUrl` | N/A | N/A | Optional | Read-only |

### NativeDecimalAsset (REST: NativeDecimalAsset)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `Value` + `DecimalAssetType: Rating` | `rating` | Decimal | Optional | Rating between 0.0 and 5.0. |

### NativeVideoAsset (REST: NativeVideoAsset)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `VideoUploadAttributes` | `videoAssetUrl` | String! | Required | Public URL after presigned upload on `hostedNativeVideoOptions`. |
| `Duration` | N/A | N/A | Optional | Read-only |
| `VideoUrl` | N/A | N/A | Optional | Read-only |

### ChinaCreativeInfoInput (REST: DeepLinkAttributes)

Nested under format `*Options.chinaCreativeInfo` when `willThisBeServedInChina: true`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `UriScheme.Link` | `uriSchemeDeepLink` | String | Optional | N/A |
| `UniversalLink.Link` | `universalLinkDeepLink` | String | Optional | N/A |

## Code examples

### REST example

```
POST /v3/creative HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv-abc123",
  "CreativeName": "My Banner Ad",
  "ImageAttributes": {
    "ImageContent": "<base64>",
    "ClickthroughUrl": "https://example.com/click",
    "LandingPageUrl": "https://example.com/landing"
  },
  "Availability": "Available"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation CreateHostedDisplayCreative($input: CreativeCreateInput!) {
  creativeCreate(input: $input) {
    creativeCreateResult {
      creative { id }
      creative {
        id
        name
        type
        ... on HostedDisplayCreative {
          imageUrl
        }
      }
    }
    errors {
      ... on CreativeCreateFieldValidationError {
        message
        field
      }
    }
  }
}
```

Variables:

```
{
  "input": {
    "advertiserId": "adv-abc123",
    "name": "My Banner Ad",
    "creativeType": "HOSTED_DISPLAY",
    "hostedDisplayOptions": {
      "assetUrl": "https://cdn.example.com/uploaded-banner.png",
      "clickthroughUrl": "https://example.com/click",
      "landingPageUrl": "https://example.com/landing"
    }
  }
}
```

Use `creativeCreatePresignedUrlGenerate` + upload when migrating from REST `ImageContent` base64 or hosted video/audio upload flows.
