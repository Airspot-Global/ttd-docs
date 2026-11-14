# Bid List

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Bid%20List
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Bid%20List (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL bidList Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list

Get a bid list by ID.

### GraphQL bidListCreate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-create

Create a bid list.

### GraphQL bidListUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-update

Updates a bid list. This is a different approach - it lets you set lines to add and lines to remove and does not require one to specify all of the bid lines.

### GraphQL bidListSet Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-set

Updates a bid list. Sets all the lines in the bid list to what is in the input.

### GraphQL bidListDelete Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-delete

Deletes a bid list.

### GraphQL adGroupAssociateBidList Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-associate-bid-list

Associate or remove bid lists from an ad group and enable or disable them for bidding.

### GraphQL advertiserAssociateBidList Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser-associate-bid-list

Associate or remove bid lists from an advertiser and enable or disable them for bidding.

### POST /v3/bidlist (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlist

We recommend using the [`bidListCreate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-create) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Create a bid list, returning the created bid list.  
**TIP**: Using the equivalent bid list GraphQL query, you can enhance performance, customize criteria, and, if needed, clone bid lists.  
For details, see [Create Bid Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/BidListsCreateManageGQL#createbidlist).

### PUT /v3/bidlist (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-bidlist

This endpoint is no longer being actively developed and may have suboptimal performance. Use the [`bidListUpdate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-update) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Update a bid list, returning the updated bid list.  
**TIP**: Using the equivalent bid list GraphQL query, you can enhance performance, customize criteria, and, if needed, update multiple bid lines.  
For details, see [Update Bid Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/BidListsCreateManageGQL#updatebidlists).

### POST /v3/bidlist/batch (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlist-batch

We recommend using the [`bidListCreate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-create) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Create multiple bid lists at once.  
Returns a list of the created bid lists.  
If one of the bid lists is not valid the full request fails and the reason for the failure is returned.

### PUT /v3/bidlist/batch (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-bidlist-batch

We recommend using the [`bidListUpdate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-update) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Update multiple bid lists at once, returning the bid lists.  
If one of the bid lists is not valid the query fails and returns the reason for the failure.  
In this case, some of the bid lists might have been updated, but as the query is idempotent the full batch can be retried without any issues.

### POST /v3/bidlist/batch/get (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlist-batch-get

We recommend using the [`bidList` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Retrieve the contents of an array of bid lists.  
**IMPORTANT**: In the request, be sure to pass a list of bid list IDs as a string array, not an object array. For details and examples, see [Bid List](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/BidList#batch-bid-lists).  
Returns a list of bid list contents, including all bid dimension line items.

### GET /v3/bidlist/{bidListId} (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-bidlist-bidlistid

We recommend using the [`bidList` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Retrieve the content of a bid list.  
Returns a bid list including all the bid dimension line items.  
**TIP**: Using the equivalent bid list GraphQL query, you can enhance performance, customize criteria, and, if needed, expand your search for multiple bid lines or owners.  
For details, see [Bid List Queries](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/BidListsCreateManageGQL#getbidlists).

### DELETE /v3/bidlist/{bidListId} (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/delete-bidlist-bidlistid

We recommend using the [`bidListDelete` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/bid-list-delete) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Delete a user bid list and its associations.

### POST /v3/bidlist/query/associated (deprecated)

Reference: not in TTD's live reference (old link `/v3/portal/api/ref/post-bidlist-query-associated`).

This endpoint is unstable.

Retrieve a paged and filterable list of ad groups, campaigns, advertisers, and partners associated with a specific bid list.  
This endpoint's maximum `PageSize` is 10,000 and the `PageSize` may not be set to `null`.

### POST /v3/bidlist/query/unassociated

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlist-query-unassociated

Retrieve a paged list of unassociated bid lists at a given level of ownership.

### POST /v3/bidlistsummary/query/adgroup/available (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlistsummary-query-adgroup-available

We recommend using the [`adGroup` → `availableBidLists` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Retrieve a paged list of bid lists that are available to associate with the ad group provided.

### POST /v3/bidlistsummary/query/advertiser/available (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlistsummary-query-advertiser-available

We recommend using the [`advertiser` → `associatedBidLists`](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser) query for associated bid lists, and the [`advertiser` → `ownedBidLists` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser) for owned bid lists, in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Retrieve a paged list of bid lists that are available to associate with the provided advertiser.

### POST /v3/bidlistsummary/query/campaign/available (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlistsummary-query-campaign-available

We recommend using the [`campaign` → `associatedBidLists`](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign) query for associated bid lists, and the [`campaign` → `ownedBidLists` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign) for owned bid lists, in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Retrieve a paged list of bid lists that are available to associate with the provided campaign.

### POST /v3/bidlistsummary/query/global

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlistsummary-query-global

Retrieve a paged list of global bid lists.  
By default, global bid lists that include a private contract ID are excluded from the results. If you don't see the results you expect, you could use the optional `ReturnBidListsUnavailableForLibraryUse` parameter with a value of `true` to include additional bid lists in the results.

### POST /v3/bidlistsummary/query/partner/available (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlistsummary-query-partner-available

We recommend using the [`partner` → `associatedBidLists` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner) for associated bid lists, and the [`partner` → `ownedBidLists` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner) for owned bid lists, in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Retrieve a paged list of bid lists that are available to associate with the provided partner.
