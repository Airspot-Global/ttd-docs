# Geo Target Segment

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Geo%20Target%20Segment
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Geo%20Target%20Segment (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/geotargetsegment/addgeotargets/{providerId}/{providerElementId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-geotargetsegment-addgeotargets-providerid-providerelementid

Add specified points or polygons to a geo target segment. Limits to 10k points or polygons per request.  
Have multiple requests to this endpoint to add more than 10k to a geo target segment.

### POST /v3/geotargetsegment/cleargeotargets/{providerId}/{providerElementId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-geotargetsegment-cleargeotargets-providerid-providerelementid

Clear all points or polygons from a geo target segment.

### POST /v3/geotargetsegment/deletegeotargets/{providerId}/{providerElementId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-geotargetsegment-deletegeotargets-providerid-providerelementid

Delete specified points or polygons from a geo target segment. Limits to 10k points or polygons per request.  
Have multiple requests to this endpoint to delete more than 10k to a geo target segment.

### POST /v3/geotargetsegment/generatepolygonfileuploadurl/{providerId}/{fileName}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-geotargetsegment-generatepolygonfileuploadurl-providerid-filename

Get an AWS S3 upload URL for adding the polygon file. For polygon file requirements, rate limits, and other details, see [Geotargeting Data Integration](/v3/portal/data/doc/GeoStore).

### GET /v3/geotargetsegment/{providerId}/{providerElementId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-geotargetsegment-providerid-providerelementid

Get an existing geo target segment
