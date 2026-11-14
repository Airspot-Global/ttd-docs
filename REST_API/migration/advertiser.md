# Advertiser: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/advertiser-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Advertiser: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/advertiser/{advertiserId}` | `Query.advertiser(id:)` | Full advertiser detail including REST-backed gap fields |
| `POST /v3/advertiser/query/partner` | `Partner.advertisers` | N/A |
| `GET /v3/advertiser/name/{advertiserId}` | `Advertiser.id` / `Advertiser.name` | N/A |
| `POST /v3/advertiser/adgroup/bidlinecounts` | `Advertiser.bidLineLimit` | Advertiser-level bid line limit only |
| `GET /v3/advertiser/query/ids` | `Query.advertisers` | Paginate and collect IDs; no bulk-ID shortcut |
| `GET /v3/advertiser/query/favoriteids` | `Me.favoritedAdvertisers` | N/A |
| `GET /v3/advertiser/bidlist/{advertiserId}` | `Advertiser.associatedBidLists` | N/A |
| `POST /v3/advertiser` | `advertiserCreate` | GraphQL create; REST-inline bid lists / frequency / political data require separate steps |
| `PUT /v3/advertiser` | `advertiserUpdate` | GraphQL update; REST-inline bid lists / frequency / political data require separate steps |
| `POST /v3/advertiser/bidlist` | `advertiserAssociateBidList` | Associate one bid list via `bidListsToAddOrUpdate` |
| `DELETE /v3/advertiser/bidlist` | `advertiserAssociateBidList` | Remove association via `bidListIdsToRemove` |
| `PUT /v3/advertiser/bidlist` | `advertiserAssociateBidList` | Replace associations via `bidListsToAddOrUpdate` (and `bidListIdsToRemove` as needed) |

## Shared nested types and enums

### AssociatedBidList

Used on `Advertiser.associatedBidLists` (GET-by-ID and dedicated bid-list lookup). `AssociatedBidList` exposes `isEnabled` and a nested `bidList: IBidList!`; bid-list attributes are selected through `bidList { ... }`.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `bidList.id` | ID! | Not nullable | Via nested `bidList` on `AssociatedBidList`. |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |
| `IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BidListSource` | `bidList.source` | BidListSource! | Not nullable | N/A |
| `BidListAdjustmentType` | `bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `BidListDimensions` | `bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |
