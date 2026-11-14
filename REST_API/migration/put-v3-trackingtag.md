# PUT /v3/trackingtag → trackingTagUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-trackingtag
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/trackingtag → trackingTagUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/trackingtag` |
| GraphQL operation | `trackingTagUpdate` |
| Input type | `TrackingTagUpdateInput` |
| Output type | `TrackingTagUpdatePayload` (`data: TrackingTagREST`, `errors: [TrackingTagUpdateMutationError!]` / `RestProxyMutationError`) |

## Input field mapping

Input type: `TrackingTagUpdateInput`

Same fields as create (`TrackingTagCreateInput`), plus `TrackingTagId` (required). All fields other than `TrackingTagId` are optional on update.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `TrackingTagId` | `trackingTagId` | ID! | Required | Required on update |
| `AdvertiserId` | `advertiserId` | ID | Optional | Optional on update |
| `TrackingTagName` | `trackingTagName` | String | Optional | Max 256 chars; optional on update |
| `TrackingTagType` | `trackingTagType` | TrackingTagTypeRESTInput | Optional | Impression, Retargeting, or Conversion; optional on update |
| `TrackingTagLocation` | `trackingTagLocation` | String | Optional | N/A |
| `Revenue` | `revenue` | String | Optional | String for macro support |
| `Currency` | `currency` | String | Optional | Max 3 chars |
| `ContainerTagBody` | `containerTagBody` | String | Optional | N/A |
| `TagRedirectUri` | `tagRedirectUri` | String | Optional | N/A |
| `HouseholdEnabled` | `householdEnabled` | Boolean | Optional | N/A |
| `DataEventTypeId` | `dataEventTypeId` | TrackingDataEventTypeIdRESTInput | Optional | 15 event types; see domain page |

## Output field mapping

Output type: `TrackingTagREST` (returned as `data` on `TrackingTagUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID | Nullable | N/A |
| `TrackingTagId` | `trackingTagId` | ID | Nullable | N/A |
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

## Code examples

### REST example

```
PUT /v3/trackingtag HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "TrackingTagId": "tag-456",
  "TrackingTagName": "Updated Conversion Tag",
  "Revenue": "30.00",
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
  trackingTagUpdate(input: {
    trackingTagId: "tag-456"
    trackingTagName: "Updated Conversion Tag"
    revenue: "30.00"
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
