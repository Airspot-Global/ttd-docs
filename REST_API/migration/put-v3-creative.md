# PUT /v3/creative → creativeUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-creative
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/creative → creativeUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/creative` |
| GraphQL operation | `creativeUpdate` |
| Input type | `CreativeUpdateInput` |
| Output type | `PayloadWithErrorsOfCreative` (`data: Creative`, `userErrors: [UserError!]!`) |

`creativeUpdate` uses format-specific `*CreativeOptions` inputs keyed by `creativeId` and `advertiserId`. The creative type cannot be changed after creation—update the matching `*CreativeOptions` for the existing type.

## Input field mapping

Input type: `CreativeUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | String! | Required | N/A |
| `CreativeId` | `creativeId` | String! | Required | Required on update. |
| `CreativeName` | `name` | String | Optional | Max 256 characters. |
| `Description` | `description` | String | Optional | Max 512 characters. |
| `CreativeType` | N/A | N/A | Optional | Create-only |
| `ImageAttributes` | `hostedDisplayCreativeOptions` | HostedDisplayICreativeOptionsInput | Optional | Exactly one `*CreativeOptions` for the existing type. |
| `FacebookAttributes` | N/A | N/A | Optional | Deprecated on REST |
| `FacebookPagePostAttributes` | N/A | N/A | Optional | Deprecated on REST |
| `FlashAttributes` | N/A | N/A | Optional | Deprecated on REST |
| `ThirdPartyTagAttributes` | `thirdPartyDisplayCreativeOptions` | ThirdPartyDisplayICreativeOptionsInput | Optional | N/A |
| `TradeDeskHostedAudioAttributes` | `hostedAudioCreativeOptions` | HostedAudioICreativeOptionsInput | Optional | N/A |
| `TradeDeskHostedVideoAttributes` | `hostedVideoCreativeOptions` | HostedVideoICreativeOptionsInput | Optional | N/A |
| `ThirdPartyHostedVideoAttributes` | `thirdPartyVideoCreativeOptions` | ThirdPartyVideoICreativeOptionsInput | Optional | N/A |
| `ThirdPartyHostedAudioAttributes` | `thirdPartyAudioCreativeOptions` | ThirdPartyAudioICreativeOptionsInput | Optional | N/A |
| `Html5Attributes` | `hostedHtml5CreativeOptions` | HostedHtml5ICreativeOptionsInput | Optional | N/A |
| `HostedNativeAttributes` | `hostedNativeCreativeOptions` | HostedNativeICreativeOptionsInput | Optional | N/A |
| `ThirdPartyNativeAttributes` | N/A | N/A | Optional | Not currently available in GraphQL |
| `HostedNativeWithThirdPartyVideoAttributes` | `hostedNativeVideoCreativeOptions` | HostedNativeVideoICreativeOptionsInput | Optional | N/A |
| `BroadcasterHostedVideo` (read-only REST `CreativeType`) | `broadcasterHostedVideoCreativeOptions` | BroadcasterHostedVideoICreativeOptionsInput | Optional | GraphQL update path for broadcaster-hosted video creatives. |
| `CreativeAuditStatuses` | N/A | N/A | Optional | Create-only |
| `FlightStartDateUTC` | `flightStart` | DateTime | Optional | N/A |
| `FlightEndDateUTC` | `flightEnd` | DateTime | Optional | N/A |
| `Availability` | N/A | N/A | Optional | REST `Archived` maps to archive workflow; no direct field on `CreativeUpdateInput`. |
| `CreatedAtUTC` | N/A | N/A | Optional | Create-only |
| `LastUpdatedAtUTC` | N/A | N/A | Optional | Create-only |
| `ShareLink` | N/A | N/A | Optional | Create-only |
| `WillThisBeServedInChina` | N/A | N/A | Optional | No direct update field; set at create. |
| `VioohReviewRequired` | N/A | N/A | Optional | Format-specific update options. |
| `VioohSelectedPublisher` | N/A | N/A | Optional | N/A |
| `UcfunnelReviewRequired` | N/A | N/A | Optional | Not currently available in GraphQL |
| `PoliticalDataId` | `politicalDataId` | ID | Optional | N/A |
| `DynamicCreativeRuleId` | `thirdParty*CreativeOptions.dynamicCreativeRuleId` | String | Optional | On third-party format options. |
| `MiaozhenMonitoringProduct` | N/A | N/A | Optional | No direct update input; read on concrete types. |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `adServerCreativeId` | String |  |
| `flightTimeZoneIANA` | String |  |
| `labels` | [String!] |  |

### Migration notes

- Exactly one `*CreativeOptions` property must match the existing creative type; the type cannot be changed.
- `FacebookAttributes`, `FacebookPagePostAttributes`, and `FlashAttributes` are deprecated and rejected on update.
- REST `ImageContent` on update is rejected—use asset URL workflows for hosted asset changes.

## Output field mapping

Output type: `Creative` (returned as `data` on `PayloadWithErrorsOfCreative`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CreativeId` | `data.id` | ID! | Not nullable | N/A |
| `AdvertiserId` | `data.advertiser.id` | ID! | Not nullable | N/A |
| `CreativeName` | `data.name` | String | Nullable | N/A |
| `Description` | `data.description` | String | Nullable | N/A |
| `CreativeType` | `data.type` | CreativeType! | Not nullable | N/A |
| `ImageAttributes` | `HostedDisplayCreative` fragment | N/A | N/A | Inline fragment on `data`. |
| `ThirdPartyTagAttributes` | `ThirdPartyDisplayCreative` fragment | N/A | N/A | N/A |
| `TradeDeskHostedVideoAttributes` | `HostedVideoCreative` fragment | N/A | N/A | N/A |
| `TradeDeskHostedAudioAttributes` | `HostedAudioCreative` fragment | N/A | N/A | N/A |
| `ThirdPartyHostedVideoAttributes` | `ThirdPartyVideoCreative` fragment | N/A | N/A | N/A |
| `ThirdPartyHostedAudioAttributes` | `ThirdPartyAudioCreative` fragment | N/A | N/A | N/A |
| `Html5Attributes` | `HostedHtml5Creative` fragment | N/A | N/A | N/A |
| `HostedNativeAttributes` | `HostedNativeCreative` fragment | N/A | N/A | N/A |
| `ThirdPartyNativeAttributes` | `ThirdPartyDisplayCreative` fragment | N/A | N/A | Not currently available in GraphQL |
| `HostedNativeWithThirdPartyVideoAttributes` | `HostedNativeVideoCreative` fragment | N/A | N/A | N/A |
| `BroadcasterHostedVideo` (REST `CreativeType`) | `BroadcasterHostedVideoCreative` fragment | N/A | N/A | Inline fragment on `data`. |
| `FacebookAttributes` | N/A | N/A | N/A | Deprecated on REST |
| `FacebookPagePostAttributes` | N/A | N/A | N/A | Deprecated on REST |
| `FlashAttributes` | N/A | N/A | N/A | Deprecated on REST |
| `CreativeAuditStatuses` | `data.auditStatuses` | AuditStatuses | Nullable | N/A |
| `FlightStartDateUTC` | `data.flightStart` | DateTime | Nullable | N/A |
| `FlightEndDateUTC` | `data.flightEnd` | DateTime | Nullable | N/A |
| `Availability` | `data.isArchived` | Boolean! | Not nullable | N/A |
| `CreatedAtUTC` | `data.createdAt` | DateTime! | Not nullable | N/A |
| `LastUpdatedAtUTC` | `data.lastUpdatedAt` | DateTime! | Not nullable | N/A |
| `ShareLink` | `data.shareLink` | String! | Not nullable | Read-only |
| `WillThisBeServedInChina` | N/A | N/A | N/A | Create-only |
| `VioohReviewRequired` | N/A | N/A | N/A | Not currently available in GraphQL |
| `VioohSelectedPublisher` | N/A | N/A | N/A | Not currently available in GraphQL |
| `UcfunnelReviewRequired` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PoliticalDataId` | `data.politicalAdIcon.politicalDataId` | ID | Nullable | N/A |
| `DynamicCreativeRuleId` | `data.dynamicCreativeOptimizationRule.id` | ID | Nullable | N/A |
| `MiaozhenMonitoringProduct` | `enabledMiaozhenProduct` on concrete types | Byte! | Not nullable | On `HostedAudioCreative`, `HostedDisplayCreative`, and `HostedVideoCreative`. |

## Endpoint-specific nested types and enums

### HostedDisplayICreativeOptionsInput (REST: ImageAttributes)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `ImageContent` | N/A | N/A | Optional | Not currently available in GraphQL |
| `ClickthroughUrl` | `clickthroughUrl` | String | Optional | N/A |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `ThirdPartyClickTrackingUrl` | `thirdPartyClickTrackingUrl` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| `IsPauseAd` | `isPauseAd` | Boolean | Optional | N/A |

### ThirdPartyDisplayICreativeOptionsInput (REST: ThirdPartyTagAttributes)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdTag` | `adTag` | String | Optional | N/A |
| `LandingPageUrls` | `landingPageUrls` | [String!] | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |

### HostedVideoICreativeOptionsInput (REST: TradeDeskHostedVideoAttributes)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `ClickthroughUrl` | `clickthroughUrl` | String | Optional | N/A |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `Skippable` | `isSkippable` | Boolean | Optional | N/A |
| `SkipOffsetInSeconds` | `skipOffsetInSeconds` | Int | Optional | N/A |
| `CompanionCreativeIds` | `companionCreativeIds` | [String!] | Optional | N/A |
| `TrackingEvents` | `playerTrackingEvents` | [TrackingEventInput!] | Optional | N/A |
| `IsVideoRetargetingEnabled` | `isRetargetingEnabled` | Boolean | Optional | N/A |
| `ThirdPartyClickTrackingUrl` | `thirdPartyClickTrackingUrl` | String | Optional | N/A |
| `UniversalAdId` | `universalAdId` | UniversalAdIdInput | Optional | N/A |

### HostedAudioICreativeOptionsInput (REST: TradeDeskHostedAudioAttributes)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `ClickthroughUrl` | `clickthroughUrl` | String | Optional | N/A |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `CompanionCreativeIds` | `companionCreativeIds` | [String!] | Optional | N/A |
| `TrackingEvents` | `trackingEvents` | [TrackingEventInput!] | Optional | N/A |
| `IsAudioRetargetingEnabled` | `isRetargetingEnabled` | Boolean | Optional | N/A |

### ThirdPartyVideoICreativeOptionsInput / ThirdPartyAudioICreativeOptionsInput

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| VastTagUrl / VastOrDaastTagUrl | vastXmlUrl / vastOrDaastUrl | String | Optional | Video vs audio option type. |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `DynamicCreativeRuleId` | `dynamicCreativeRuleId` | String | Optional | N/A |
| `TrackingEvents` | `playerTrackingEvents` | [TrackingEventInput!] | Optional | N/A |

### HostedHtml5ICreativeOptionsInput (REST: html5Attributes)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| ZipFileContent / asset upload | N/A | N/A | Optional | Rejected on REST update; asset URL changes use platform workflows. |
| `BackupImageContent` | N/A | N/A | Optional | Rejected on REST update. |
| `ClickthroughUrl` | `clickthroughUrl` | String | Optional | N/A |
| `ClickTrackingParamName` | `clickTrackingParameterName` | String | Optional | N/A |
| `WidthInPixels` | N/A | N/A | Optional | Read-only |
| `HeightInPixels` | N/A | N/A | Optional | Read-only |
| `LandingPageUrls` | `landingPageUrls` | [String!] | Optional | N/A |
| `UseClickthroughAsDefault` | `useClickthroughAsDefault` | Boolean | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Optional | N/A |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| `IsSecurable` | `isSecurable` | Boolean | Optional | N/A |

### HostedNativeICreativeOptionsInput (REST: HostedNativeAttributes)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdServerName` | N/A | N/A | Optional | No field on update input. |
| `AdServerCreativeId` | N/A | N/A | Optional | N/A |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `ClickThroughUrl` | `clickthroughUrl` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl4` | `pixelImpressionTrackingUrl4` | String | Optional | N/A |
| `TextAssets` | shortTitle / longTitle / sponsor / callToAction / price / shortDescription / longDescription | String | Optional | GraphQL flattens `TextAssets[]` by `TextAssetType`. |
| `ImageAssets` | N/A | N/A | Optional | Image asset changes rejected on REST update. |
| `DecimalAssets` | `rating` | Decimal | Optional | N/A |
| `VideoAsset` | N/A | N/A | Optional | Use `hostedNativeVideoCreativeOptions` for hosted native video creatives. |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| `IsPlayerRetargetingEnabled` | N/A | N/A | Optional | Use `hostedNativeVideoCreativeOptions.isRetargetingEnabled` for hosted native video. |

### HostedNativeVideoICreativeOptionsInput (REST: HostedNativeWithThirdPartyVideoAttributes)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `ClickThroughUrl` | `clickthroughUrl` | String | Optional | N/A |
| `TextAssets` | shortTitle / longTitle / sponsor / callToAction / price / shortDescription / longDescription | String | Optional | N/A |
| `DecimalAssets` | `rating` | Decimal | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl` | `pixelImpressionTrackingUrl1` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl2` | `pixelImpressionTrackingUrl2` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl3` | `pixelImpressionTrackingUrl3` | String | Optional | N/A |
| `ThirdPartyImpressionTrackingUrl4` | `pixelImpressionTrackingUrl4` | String | Optional | N/A |
| `TrackingEvents` | `playerTrackingEvents` | [TrackingEventInput!] | Optional | See TrackingEventInput table below. |
| `ThirdPartyTrackingTags` | `thirdPartyTrackingTags` | [String!] | Optional | N/A |
| `IsPlayerRetargetingEnabled` | `isRetargetingEnabled` | Boolean | Optional | N/A |
| `VideoVastUrl` | N/A | N/A | Optional | REST-only for hosted native with third-party video. |

### BroadcasterHostedVideoICreativeOptionsInput (REST: BroadcasterHostedVideo)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `ClickthroughUrl` | `clickthroughUrl` | String | Optional | N/A |
| `LandingPageUrl` | `landingPageUrl` | String | Optional | N/A |
| `Skippable` | `isSkippable` | Boolean | Optional | N/A |
| `SkipOffsetInSeconds` | `skipOffsetInSeconds` | Int | Optional | N/A |
| `TrackingEvents` | `playerTrackingEvents` | [TrackingEventInput!] | Optional | N/A |
| `IsVideoRetargetingEnabled` | `isRetargetingEnabled` | Boolean | Optional | N/A |
| `UniversalAdId` / `UniversalAdIdRegistry` | `universalAdId` | UniversalAdIdInput | Optional | N/A |

### TrackingEventInput (REST: VideoTrackingEvent)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `EventType` | `type` | TrackingEventType! | Required | REST `VideoTrackingEventType` maps to `TrackingEventType` enum. |
| `EventUrl` | `url` | String! | Required | N/A |

## Code examples

### REST example

```
PUT /v3/creative HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CreativeId": "cr-abc123",
  "AdvertiserId": "adv-abc123",
  "CreativeName": "My Banner Ad",
  "ImageAttributes": {
    "ClickthroughUrl": "https://example.com/click-updated"
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
mutation UpdateCreative($input: CreativeUpdateInput!) {
  creativeUpdate(input: $input) {
    data {
      id
      name
      lastUpdatedAt
      ... on HostedDisplayCreative {
        clickthroughUrl
      }
    }
    userErrors {
      message
      field
    }
  }
}
```

Variables:

```
{
  "input": {
    "creativeId": "cr-abc123",
    "advertiserId": "adv-abc123",
    "name": "My Banner Ad",
    "hostedDisplayCreativeOptions": {
      "clickthroughUrl": "https://example.com/click-updated"
    }
  }
}
```
