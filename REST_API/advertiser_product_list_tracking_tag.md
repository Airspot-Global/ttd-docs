# Advertiser Product List Tracking Tag

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Advertiser%20Product%20List%20Tracking%20Tag
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Advertiser%20Product%20List%20Tracking%20Tag (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/ecommerce/campaigns/trackingtag/lists/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-campaigns-trackingtag-lists-query

Get campaign IDs, tracking tags, product lists and their associated advertisers for a given merchant ID. For details, see [Product List Tracking Tags](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceTrackingTag).

### POST /v3/ecommerce/trackingtag/lists/batch/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-trackingtag-lists-batch-query

Get the names and IDs of product lists for multiple tracking tag IDs. For details, see [Product List Tracking Tags](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceTrackingTag).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### POST /v3/ecommerce/trackingtag/lists/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-trackingtag-lists-query

Get all tracking tags and their associated product lists for a given advertiser ID. For details, see [Product List Tracking Tags](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceTrackingTag).
