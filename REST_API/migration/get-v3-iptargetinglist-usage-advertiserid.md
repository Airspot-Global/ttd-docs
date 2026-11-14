# GET /v3/iptargetinglist/usage/{advertiserId} → Advertiser.ipTargetingListUsage

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-iptargetinglist-usage-advertiserid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/iptargetinglist/usage/{advertiserId} → Advertiser.ipTargetingListUsage

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/iptargetinglist/usage/{advertiserId}` |
| GraphQL query | `Advertiser.ipTargetingListUsage` |
| Return type | `IPTargetingListUsageSummary` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `ipTargetingListUsage { advertiserId }` | ID! | Not nullable | Path parameter `advertiserId` selects the parent advertiser. |
| `IPTargetingRangesAllowed` | `ipTargetingListUsage { ipTargetingRangesAllowed }` | Long! | Not nullable | N/A |
| `IPTargetingRangesUsed` | `ipTargetingListUsage { ipTargetingRangesUsed }` | Long! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/iptargetinglist/usage/{advertiserId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query IPTargetingListUsage($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    id
    ipTargetingListUsage {
      advertiserId
      ipTargetingRangesAllowed
      ipTargetingRangesUsed
    }
  }
}
```
