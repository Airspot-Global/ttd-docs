# IP targeting list: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/iptargetinglist-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# IP targeting list: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/iptargetinglist/{ipTargetingListId}` | `Query.ipTargetingList(id:)` | Full list including IP ranges |
| `GET /v3/iptargetinglist/usage/{advertiserId}` | `Advertiser.ipTargetingListUsage` | Per-advertiser range allowance and usage |
| `POST /v3/iptargetinglist/query/advertiser` | `Advertiser.ipTargetingLists` | Paged summary list; optional search and sort |
| `POST /v3/iptargetinglist` | `ipTargetingListCreate` | Create list with name and IP ranges |
| `PUT /v3/iptargetinglist` | `ipTargetingListUpdate` | Replace ranges; name cannot be changed |

## Shared nested types and enums

### IPTargetingRangeRESTInput

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `MinIP` | `minIP` | String! | Required | N/A |
| `MaxIP` | `maxIP` | String! | Required | N/A |
| `TargetingDataMetadataId` | `targetingDataMetadataId` | ID | Optional | N/A |
