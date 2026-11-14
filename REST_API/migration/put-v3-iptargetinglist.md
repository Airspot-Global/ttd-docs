# PUT /v3/iptargetinglist → ipTargetingListUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-iptargetinglist
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/iptargetinglist → ipTargetingListUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/iptargetinglist` |
| GraphQL operation | `ipTargetingListUpdate` |
| Input type | `IpTargetingListUpdateInput` |
| Output type | `IpTargetingListUpdatePayload` (`data: IPTargetingListREST`, `errors: [IpTargetingListUpdateMutationError!]` / `RestProxyMutationError`) |

## Input field mapping

Input type: `IpTargetingListUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `IPTargetingListId` | `ipTargetingListId` | ID! | Required | N/A |
| `AdvertiserId` | `advertiserId` | ID | Optional | Optional on update input. |
| `IPTargetingRanges` | `ipTargetingRanges` | [IPTargetingRangeRESTInput!] | Optional | Replaces all existing ranges; pass empty array to clear. `ipTargetingDataName` is not in the update input. |

## Output field mapping

Output type: `IPTargetingListREST` (returned as `data` on `IpTargetingListUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID | Nullable | N/A |
| `IPTargetingListId` | `ipTargetingListId` | ID | Nullable | N/A |
| `IPTargetingDataName` | `ipTargetingDataName` | String | Nullable | Read-only after creation. |
| `IPTargetingRangesCount` | `ipTargetingRangesCount` | Long! | Not nullable | Count of ranges after update. |

## Code examples

### REST example

```
PUT /v3/iptargetinglist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "IPTargetingListId": "list-xyz-789",
  "AdvertiserId": "abc123",
  "IPTargetingRanges": [
    { "MinIP": "172.16.0.1", "MaxIP": "172.16.0.255" }
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
mutation IPTargetingListUpdate($input: IpTargetingListUpdateInput!) {
  ipTargetingListUpdate(input: $input) {
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
    "ipTargetingListId": "list-xyz-789",
    "advertiserId": "abc123",
    "ipTargetingRanges": [
      { "minIP": "172.16.0.1", "maxIP": "172.16.0.255" }
    ]
  }
}
```
