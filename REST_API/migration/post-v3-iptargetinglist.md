# POST /v3/iptargetinglist → ipTargetingListCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-iptargetinglist
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/iptargetinglist → ipTargetingListCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/iptargetinglist` |
| GraphQL operation | `ipTargetingListCreate` |
| Input type | `IpTargetingListCreateInput` |
| Output type | `IpTargetingListCreatePayload` (`data: IPTargetingListREST`, `errors: [IpTargetingListCreateMutationError!]` / `RestProxyMutationError`) |

## Input field mapping

Input type: `IpTargetingListCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID! | Required | N/A |
| `IPTargetingDataName` | `ipTargetingDataName` | String! | Required | Cannot be changed after creation. |
| `IPTargetingRanges` | `ipTargetingRanges` | [IPTargetingRangeRESTInput!]! | Required | N/A |
| `IPTargetingRanges[].MinIP` | `minIP` | String! | Required | Required in each range object. |
| `IPTargetingRanges[].MaxIP` | `maxIP` | String! | Required | Required in each range object. |
| `IPTargetingRanges[].TargetingDataMetadataId` | `targetingDataMetadataId` | ID | Optional | N/A |

## Output field mapping

Output type: `IPTargetingListREST` (returned as `data` on `IpTargetingListCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID | Nullable | N/A |
| `IPTargetingListId` | `ipTargetingListId` | ID | Nullable | Server-generated on create. |
| `IPTargetingDataName` | `ipTargetingDataName` | String | Nullable | N/A |
| `IPTargetingRangesCount` | `ipTargetingRangesCount` | Long! | Not nullable | Count of ranges after create. |

## Endpoint-specific nested types and enums

### IPTargetingRangeRESTInput

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `MinIP` | `minIP` | String! | Required | N/A |
| `MaxIP` | `maxIP` | String! | Required | N/A |
| `TargetingDataMetadataId` | `targetingDataMetadataId` | ID | Optional | N/A |

## Code examples

### REST example

```
POST /v3/iptargetinglist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "abc123",
  "IPTargetingDataName": "My IP List",
  "IPTargetingRanges": [
    { "MinIP": "10.0.0.1", "MaxIP": "10.0.0.255" }
  ]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation IPTargetingListCreate($input: IpTargetingListCreateInput!) {
  ipTargetingListCreate(input: $input) {
    data {
      advertiserId
      ipTargetingListId
      ipTargetingDataName
      ipTargetingRangesCount
    }
    errors { ... on RestProxyMutationError { message field } }
  }
}
```

Variables:

```
{
  "input": {
    "advertiserId": "abc123",
    "ipTargetingDataName": "My IP List",
    "ipTargetingRanges": [
      { "minIP": "10.0.0.1", "maxIP": "10.0.0.255" }
    ]
  }
}
```
