# Custom Label

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Custom%20Label
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Custom%20Label (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/label

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-label

Creates a new Custom Label.  
Once added, these labels can be applied to Advertisers, Campaigns, and Ad Groups via their respective POST/PUT endpoints.

### GET /v3/label/{customLabelId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-label-customlabelid

Gets a Custom Label.

### POST /v3/label/query/partner

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-label-query-partner

Gets all Custom Labels for a Partner.
