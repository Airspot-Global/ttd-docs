# Ispot

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Ispot
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Ispot (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/ispot/brand/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ispot-brand-query

Get all active iSpot brands.

### PUT /v3/ispot/reportsettings/campaign

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ispot-reportsettings-campaign

Update an iSpot Reporting Model for a given Campaign.  
iSpot Reporting Models only apply to impressions served in the U.S Geography.

### GET /v3/ispot/reportsettings/campaign/{campaignId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-ispot-reportsettings-campaign-campaignid

Get an existing iSpot Reporting Model by Campaign ID.
