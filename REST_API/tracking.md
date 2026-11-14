# Tracking

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Tracking
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Tracking (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/tracking/appeventtracker

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-tracking-appeventtracker

Create a new AppEventTracker for an advertiser.

### PUT /v3/tracking/appeventtracker

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-tracking-appeventtracker

Update an existing AppEventTracker.

### GET /v3/tracking/appeventtracker/{appEventTrackerId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-tracking-appeventtracker-appeventtrackerid

Get details of a particular AppEventTracker.

### POST /v3/tracking/appeventtrackerwithactivity/advertiser/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-tracking-appeventtrackerwithactivity-advertiser-query

Retrieve a list of AppEventTrackers set up for a particular advertiser, along with some basic activity statistics .

### POST /v3/tracking/trackedappvendor/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-tracking-trackedappvendor-query

Retrieve a list of supported AppEventTracker vendors.

### POST /v3/tracking/universalpixel

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-tracking-universalpixel

Create a new UniversalPixel.

### PUT /v3/tracking/universalpixel

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-tracking-universalpixel

Update an existing UniversalPixel.

### POST /v3/tracking/universalpixelmappingwithactivity/universalpixel/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-tracking-universalpixelmappingwithactivity-universalpixel-query

Return a list of UniversalPixelMappings set up for a UniversalPixel along with some basic activity statistics.  
Note that this query will always return a paged result. You may set the PageSize using the query parameters to a maximum of 100.  
This maximum may change at any point in time based on performance considerations, so please design accordingly.

### GET /v3/tracking/universalpixel/pixelcode/china/{universalPixelId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-tracking-universalpixel-pixelcode-china-universalpixelid

Get the JavaScript Pixel code for the UniversalPixel for China.

### GET /v3/tracking/universalpixel/pixelcode/{universalPixelId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-tracking-universalpixel-pixelcode-universalpixelid

Get the JavaScript Pixel code for the UniversalPixel.

### GET /v3/tracking/universalpixel/{universalPixelId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-tracking-universalpixel-universalpixelid

Get the details of a particular UniversalPixel.

### POST /v3/tracking/universalpixelwithactivity/advertiser/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-tracking-universalpixelwithactivity-advertiser-query

Return a list of UniversalPixels set up for the Advertiser along with some basic activity statistics.  
**TIP**: Using the equivalent advertiser GraphQL query, you can enhance performance, customize criteria, and, if needed, expand your search across multiple advertisers.  
For details, see [Look Up Tracking Tags](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AdvertiserGQLQueryExamples#tracking-tags).  
**NOTE**: This query always returns a paged result. You may set the `PageSize` property in the query parameters to a maximum of 100.  
This maximum may change at any point in time based on performance considerations, so please design accordingly.
