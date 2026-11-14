# Third Party Data Rate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Third%20Party%20Data%20Rate
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Third%20Party%20Data%20Rate (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/datarate/batch

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-datarate-batch

Stage a batch of third-party taxonomy data rates for processing and approval. A batch can include a maximum of 5000 rates. For details and examples, see the Assign Rates to Data Elements section in [Third-Party Data Integration](/v3/portal/data/thirdparty/overview).  
This endpoint is available only to data providers. For details, contact your Technical Account Manager.

### GET /v3/datarate/batch/{batchId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-datarate-batch-batchid

Get the processing and approval status for a batch of submitted data rates. This endpoint is available only to data providers. For more information, contact your Technical Account Manager.

### GET /v3/datarate/brands/{providerId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-datarate-brands-providerid

Retrieve a list of brands for a specific data provider ID. For details and examples, see [Third-Party Data Management](/v3/portal/data/doc/ThirdPartyDataManagement).  
This endpoint is available only to data providers. For more information, contact your Technical Account Manager.

### POST /v3/datarate/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-datarate-query

Retrieve a filterable, paged list of data rates. For details and examples, see [Third-Party Data Management](/v3/portal/data/doc/ThirdPartyDataManagement).  
This endpoint is available only to data providers. For more information, contact your Technical Account Manager.
