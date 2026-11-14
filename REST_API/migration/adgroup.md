# Ad group: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/adgroup-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Ad group: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/adgroup/{adGroupId}` | `Query.adGroup` | N/A |
| `POST /v3/adgroup/query/campaign` | `Campaign.adGroups` | N/A |
| `POST /v3/adgroup/query/advertiser` | `Advertiser.adGroups` | N/A |
| `GET /v3/adgroup/status/{adGroupId}` | `AdGroup.status` | Enabled status—also available via `AdGroup.isEnabled` |
| `GET /v3/adgroup/name/{adGroupId}` | `AdGroup.id`, `AdGroup.name` | Lightweight ID/name—no new fields |
| `POST /v3/adgroup/query/campaign/template` | `Campaign.adGroups` | Template ad groups—`where: { isTemplate: { eq: true } }` on `AdGroupForCampaignFilterInput` |
| `GET /v3/adgroup/analyticsreport/{adGroupId}` | `AdGroup.analyticsReport` | N/A |
| `GET /v3/adgroup/koarecommendations/{adGroupId}` | N/A | Not currently available in GraphQL |
| `GET /v3/adgroup/koaapplieditems/{adGroupId}` | N/A | Not currently available in GraphQL |
| `POST /v3/adgroup/query/bidderservice` | N/A | Not currently available in GraphQL |
| `GET /v3/adgroup/doubleverifysettings/{adGroupId}` | N/A | Not currently available in GraphQL |
| `GET /v3/adgroup/bidlist/{adGroupId}` | `AdGroup.associatedBidLists` | Associated bid lists—same fields as main ad group read |
| `POST /v3/adgroup` | `adGroupCreate` | Bid lists and campaign defaults still need extra mutations |
| `PUT /v3/adgroup` | `adGroupUpdate` | Bid lists use `PUT /v3/adgroup/bidlist`; `NewFrequencyConfigs` is create-only |
| `PUT /v3/adgroup/status` | `adGroupUpdate` | Maps to `id` + `isEnabled` |
| `PUT /v3/adgroup/doubleverifysettings` | N/A | Deprecated on REST |
| `PUT /v3/adgroup/acceptrecommendation/{adGroupId}` | N/A | Not currently available in GraphQL |
| `POST /v3/adgroup/bidlist` | `bidListCreate` + `adGroupAssociateBidList` | Two-step GraphQL flow |
| `DELETE /v3/adgroup/bidlist/{adGroupId}/{bidListId}` | `adGroupAssociateBidList` | Disassociate via detach |
| `PUT /v3/adgroup/bidlist` | `adGroupAssociateBidListBatch` | Full-replace associated bid lists |
| `POST /v3/adgroup/buildcomplete` | N/A | Not currently available in GraphQL |
| `POST /v3/adgroup/buildcomplete/batch` | N/A | Not currently available in GraphQL |

## Shared nested types and enums

### AssociatedBidList (bid list association)

Used on `AdGroup.associatedBidLists` from both the main ad group read and the dedicated bid-list endpoint. Each connection node is `AdGroupAssociatedBidList` with association flags plus a nested `bidList: IBidList!`.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `bidList.id` | ID! | Not nullable | On nested `IBidList` |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | On `AdGroupAssociatedBidList` |
| `IsDefaultForDimension` | `isDefaultForUI` | Boolean! | Not nullable | REST name; GraphQL field is `isDefaultForUI` |
| `BidListSource` | `bidList.source` | BidListSource! | Not nullable | On nested `IBidList` |
| `BidListAdjustmentType` | `bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | On nested `IBidList` |
| `BidListDimensions` | `bidList.dimensions` | [BidListDimension!]! | Not nullable | On nested `IBidList` |
