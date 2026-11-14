# POST /v3/crmdata/segment → crmDataSegmentCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-crmdata-segment
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/crmdata/segment → crmDataSegmentCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/crmdata/segment` |
| GraphQL operation | `crmDataSegmentCreate` |
| Input type | `CrmDataSegmentCreateInput` |
| Output type | `CrmDataSegmentCreatePayload` (`data: CrmDataSegment`, `errors: [CrmDataSegmentCreateMutationError!]`) |

## Multi-step operations

This route creates a default **targeting** CRM segment. It is equivalent to `POST /v3/crmdata/targeting/segment`. Use `crmDataSegmentCreate` with `segmentType: TARGETING`.

## Input field mapping

Input type: `CrmDataSegmentCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| N/A | `segmentType` | SegmentType! | Required | Path omits segment type on this route; use `TARGETING` |
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

## Endpoint-specific nested types and enums

### CrmDataRegion

| REST value | GraphQL enum |
| --- | --- |
| `US` | `US` |
| `EU` | `EU` |
| `APAC` | `APAC` |

## Code examples

### REST example

```
POST /v3/crmdata/segment HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv-123",
  "SegmentName": "My CRM Segment",
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
      ownerId: { advertiserId: "adv-123" }
      name: "My CRM Segment"
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
