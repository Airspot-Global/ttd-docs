# GET /v3/iptargetinglist/{ipTargetingListId} → Query.ipTargetingList

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-iptargetinglist-iptargetinglistid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/iptargetinglist/{ipTargetingListId} → Query.ipTargetingList

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/iptargetinglist/{ipTargetingListId}` |
| GraphQL query | `Query.ipTargetingList(id: ID!)` |
| Return type | `IPTargetingList` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser { id }` | ID! | Not nullable | Owner advertiser; use `advertiser { id }`. |
| `IPTargetingListId` | `id` | ID! | Not nullable | N/A |
| `IPTargetingDataName` | `name` | String! | Not nullable | N/A |
| `IPTargetingRanges` | `ipTargetingRanges` | [IPTargetingRange!]! | Not nullable | Nested—see IPTargetingRange type. |
| `IPTargetingRanges.MinIP` | `ipTargetingRanges { minIP }` | String! | Not nullable | N/A |
| `IPTargetingRanges.MaxIP` | `ipTargetingRanges { maxIP }` | String! | Not nullable | N/A |
| `IPTargetingRanges.TargetingDataMetadataId` | `ipTargetingRanges { targetingDataMetadataId }` | Long | Nullable | N/A |

## Endpoint-specific nested types and enums

### IPTargetingRange

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `MinIP` | `minIP` | String! | Not nullable | N/A |
| `MaxIP` | `maxIP` | String! | Not nullable | N/A |
| `TargetingDataMetadataId` | `targetingDataMetadataId` | Long | Nullable | N/A |

## Code examples

### REST example

```
GET /v3/iptargetinglist/{ipTargetingListId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query IPTargetingListById($id: ID!) {
  ipTargetingList(id: $id) {
    id
    name
    ipTargetingRanges {
      minIP
      maxIP
      targetingDataMetadataId
    }
    advertiser {
      id
    }
  }
}
```
