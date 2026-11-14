# POST /v3/trackingtag → trackingTagCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-trackingtag
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/trackingtag → trackingTagCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/trackingtag` |
| GraphQL operation | `trackingTagCreate` |
| Input type | `TrackingTagCreateInput` |
| Output type | `TrackingTagCreatePayload` (`data: TrackingTagREST`, `errors: [TrackingTagCreateMutationError!]` / `RestProxyMutationError`) |

## Input field mapping

Input type: `TrackingTagCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID! | Required | N/A |
| `TrackingTagId` | N/A | N/A | Optional | InvalidOnCreate; ignored if supplied—server assigns ID in response |
| `TrackingTagName` | `trackingTagName` | String! | Required | Max 256 chars |
| `TrackingTagType` | `trackingTagType` | TrackingTagTypeRESTInput! | Required | Impression, Retargeting, or Conversion |
| `TrackingTagLocation` | `trackingTagLocation` | String | Optional | N/A |
| `Revenue` | `revenue` | String | Optional | String for macro support |
| `Currency` | `currency` | String | Optional | Max 3 chars |
| `ContainerTagBody` | `containerTagBody` | String | Optional | N/A |
| `TagRedirectUri` | `tagRedirectUri` | String | Optional | N/A |
| `HouseholdEnabled` | `householdEnabled` | Boolean | Optional | N/A |
| `DataEventTypeId` | `dataEventTypeId` | TrackingDataEventTypeIdRESTInput | Optional | 15 event types |

## Output field mapping

Output type: `TrackingTagREST` (returned as `data` on `TrackingTagCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID | Nullable | N/A |
| `TrackingTagId` | `trackingTagId` | ID | Nullable | Assigned by server on create |
| `TrackingTagName` | `trackingTagName` | String | Nullable | N/A |
| `TrackingTagType` | `trackingTagType` | TrackingTagTypeREST | Nullable | N/A |
| `TrackingTagLocation` | `trackingTagLocation` | String | Nullable | N/A |
| `Revenue` | `revenue` | String | Nullable | N/A |
| `Currency` | `currency` | String | Nullable | N/A |
| `ContainerTagBody` | `containerTagBody` | String | Nullable | N/A |
| `FirstPartyDataId` | `firstPartyDataId` | ID | Nullable | Read-only |
| `TrackingTagCategory` | `trackingTagCategory` | TrackingTagCategoryREST | Nullable | Read-only |
| `TrackingTagAvailability` | `trackingTagAvailability` | AvailabilityREST | Nullable | Read-only |
| `OfflineDataProviderId` | `offlineDataProviderId` | ID | Nullable | Read-only |
| `UniversalPixelName` | `universalPixelName` | String | Nullable | Read-only |
| `HitCount7Day` | `hitCount7Day` | Long | Nullable | Read-only |
| `TagRedirectUri` | `tagRedirectUri` | String | Nullable | N/A |
| `HouseholdEnabled` | `householdEnabled` | Boolean | Nullable | N/A |
| `ImageTag` | `imageTag` | String | Nullable | Read-only |
| `IFrameTag` | `iFrameTag` | String | Nullable | Read-only |
| `DataEventTypeId` | `dataEventTypeId` | TrackingDataEventTypeIdREST | Nullable | N/A |

## Endpoint-specific nested types and enums

### TrackingTagTypeREST

| REST value | GraphQL value |
| --- | --- |
| `Impression` | `IMPRESSION` |
| `Retargeting` | `RETARGETING` |
| `Conversion` | `CONVERSION` |

## Code examples

### REST example

```
POST /v3/trackingtag HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv-123",
  "TrackingTagName": "Conversion Tag",
  "TrackingTagType": "Conversion",
  "Revenue": "25.00",
  "Currency": "USD"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  trackingTagCreate(input: {
    advertiserId: "adv-123"
    trackingTagName: "Conversion Tag"
    trackingTagType: CONVERSION
    revenue: "25.00"
    currency: "USD"
  }) {
    data {
      trackingTagId
      trackingTagName
      imageTag
      iFrameTag
    }
    errors {
      ... on RestProxyMutationError {
        message
        field
      }
    }
  }
}
```
