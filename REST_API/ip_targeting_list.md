# IP Targeting List

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/IP%20Targeting%20List
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/IP%20Targeting%20List (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/iptargetinglist

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-iptargetinglist

Create a new IP Targeting List. For efficiency, this method returns an IP Targeting List Summary on success instead of echoing the full list.  
Each Advertiser has a quota for the number of IP targeting ranges they may include across all of their IP Targeting Lists. If creating a given list would exceed the overall quota for an Advertiser, the list will not be created and an error will be returned. In this case, you must submit a smaller list or remove IP ranges from an existing list to make room for the new list.

### PUT /v3/iptargetinglist

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-iptargetinglist

Update an existing IP Targeting List. For efficiency, this method returns an IP Targeting List Summary on success instead of echoing the full list.  
Each Advertiser has a quota for the number of IP targeting ranges they may include across all of their IP Targeting Lists. If updating a given list would exceed the overall quota for an Advertiser, the list will not be updated and an error will be returned. In this case, you must submit a smaller list or remove IP ranges from an existing list to make room for the updates.

### GET /v3/iptargetinglist/{ipTargetingListId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-iptargetinglist-iptargetinglistid

Get an existing IP Targeting List.

### POST /v3/iptargetinglist/query/advertiser

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-iptargetinglist-query-advertiser

Get a page of summaries of IP Targeting List that belong to the specified Advertiser.

### GET /v3/iptargetinglist/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-iptargetinglist-query-facets

Get the facets of IP Targeting List that can be queried.

### GET /v3/iptargetinglist/usage/{advertiserId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-iptargetinglist-usage-advertiserid

Get the cumulative IP Targeting Lists usage for an Advertiser.
