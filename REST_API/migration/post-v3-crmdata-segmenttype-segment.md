# POST /v3/crmdata/{segmentType}/segment → crmDataSegmentCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-crmdata-segmenttype-segment
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/crmdata/{segmentType}/segment → crmDataSegmentCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/crmdata/{segmentType}/segment` |
| GraphQL operation | `crmDataSegmentCreate` |
| Input type | `CrmDataSegmentCreateInput` |
| Output type | `CrmDataSegmentCreatePayload` (`data: CrmDataSegment`, `errors: [CrmDataSegmentCreateMutationError!]`) |

## Input field mapping

Input type: `CrmDataSegmentCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `segmentType` | `segmentType` | SegmentType! | Required | Path parameter; see CrmDataDropInfo domain page `SegmentType` table for REST path → GraphQL enum mappings |
| `AdvertiserId` | `ownerId.advertiserId` | ID | Optional | REST body requires `AdvertiserId`; `ownerId` input object is required |
| `SegmentName` | `name` | String! | Required | N/A |
| `Region` | `region` | CrmDataRegion! | Required | REST `Optional<CrmDataRegion>` string → `CrmDataRegion` enum |
| `DataProviderId` | `dataProviderId` | String | Optional | 3rd-party integrations only |

## Output field mapping

Output type: `CrmDataSegment` (returned as `data` on `CrmDataSegmentCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CrmDataId` | `id` | ID! | Not nullable | Returned on `payload.data` |
| `FirstPartyDataId` | `targetingData.id` | ID! | Not nullable | Not applicable for conversions; `long` → `ID` |

## Code examples

### REST example

```
POST /v3/crmdata/targeting/segment HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "abc123",
  "SegmentName": "My Targeting Segment",
  "Region": "US"
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
  crmDataSegmentCreate(
    input: {
      segmentType: TARGETING
      ownerId: { advertiserId: "abc123" }
      name: "My Targeting Segment"
      region: US
    }
  ) {
    data {
      id
      targetingData {
        id
      }
    }
    errors {
      ... on UserError {
        message
        field
      }
    }
  }
}
```
