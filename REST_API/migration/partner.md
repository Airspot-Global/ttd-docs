# Partner: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/partner-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Partner: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/partner/query` | `Query.partners` | N/A |
| `GET /v3/partner/{partnerId}` | `Query.partner(id:)` | N/A |
| `GET /v3/partner/name/{partnerId}` | `Query.partnerBasicInfo(ids:)` | N/A |
| `POST /v3/partner/advertiser/bidlinecounts` | N/A | Not currently available in GraphQL |
| `GET /v3/partner/bidlist/{partnerId}` | `Partner.associatedBidLists` | Associated bid lists—same field as main partner read |
| `GET /v3/partner/brand/{partnerId}` | `Partner.brands` | N/A |
| `PUT /v3/partner` | `partnerUpdate` | Rename via `name`; bid-list associations via `partnerAssociateBidList`; `Increments` and `NewFrequencyConfigs` are not currently available in GraphQL |
| `POST /v3/partner/bidlist` | `partnerAssociateBidList` | **Not currently available in GraphQL** |
| `DELETE /v3/partner/bidlist` | `partnerAssociateBidList` | Remove via `bidListIdsToRemove` |
| `PUT /v3/partner/bidlist` | `partnerAssociateBidList` | **Not currently available in GraphQL** |
| `PUT /v3/partner/brand` | N/A | Not currently available in GraphQL |

## Shared nested types and enums

### AssociatedBidList

Used on `Partner.associatedBidLists` from both the main partner read and the dedicated bid-list endpoint. `AssociatedBidList` exposes `isEnabled` and a nested `bidList: IBidList!`; bid-list attributes are selected through `bidList { ... }`.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `bidList.id` | ID! | Not nullable | Via nested `bidList` on `AssociatedBidList`. |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |
| `IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BidListSource` | `bidList.source` | BidListSource! | Not nullable | N/A |
| `BidListAdjustmentType` | `bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `BidListDimensions` | `bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |
