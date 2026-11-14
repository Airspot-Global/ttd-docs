# GET /v3/crmdata/segment/{advertiserId} → Advertiser.crmDataSegments

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-crmdata-segment-advertiserid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/crmdata/segment/{advertiserId} → Advertiser.crmDataSegments

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/crmdata/segment/{advertiserId}` |
| GraphQL query | `Advertiser.crmDataSegments` |
| Return type | `CrmDataSegmentsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `advertiserId` | (parent—Advertiser.id) | ID! | Required | Path parameter; resolved via parent Advertiser. |
| `pagingToken` | `after` | String | Optional | REST uses query-string `pagingToken`; GraphQL connection uses first/after pagination—cursor semantics differ from REST token. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Segments` | `nodes` | [CrmDataSegment!] | Nullable | Segment list on `Advertiser.crmDataSegments`. |
| `PagingToken` | `pageInfo.endCursor` | String | Nullable | REST returns opaque token for next page; GraphQL connection uses cursors. |
| `Segments[].CrmDataId` | `CrmDataSegment.id` | ID! | Not nullable | N/A |
| `Segments[].SegmentName` | `CrmDataSegment.name` | String! | Not nullable | N/A |
| `Segments[].Region` | `CrmDataSegment.region` | CrmDataRegion! | Not nullable | N/A |
| `Segments[].FirstPartyDataId` | `CrmDataSegment.targetingData.id` | ID! | Not nullable | Via CrmDataSegment.`targetingData`.id for retargeting ID. |

## Code examples

### REST example

```
GET /v3/crmdata/segment/{advertiserId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CrmDataSegments {
  advertiser(id: "adv123") {
    crmDataSegments(first: 50) {
      nodes {
        id
        name
        region
        targetingData {
          id
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
