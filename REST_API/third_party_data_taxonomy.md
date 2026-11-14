# Third Party Data Taxonomy

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Third%20Party%20Data%20Taxonomy
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Third%20Party%20Data%20Taxonomy (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/thirdpartydata

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-thirdpartydata

Create a new data element (segment) in your third-party data taxonomy and set whether customers can buy it through the Data Management Platform (DMP). For details and examples, see [Third-Party Data Integration](/v3/portal/data/thirdparty/overview).  
This endpoint is available only to data providers. For more information, contact your Technical Account Manager.

### PUT /v3/thirdpartydata

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-thirdpartydata

Update the name, description, or buyable status for a data element in your third-party data taxonomy in the Data Management Platform (DMP).  
This endpoint is available only to data providers. For more information, contact your Technical Account Manager.

### POST /v3/thirdpartydata/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-thirdpartydata-query

Retrieve a paged, filterable list of data elements for a specific data provider. This endpoint is available only to data providers. For more information, contact your Technical Account Manager.

### GET /v3/thirdpartydata/status/{providerId}/{providerElementId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-thirdpartydata-status-providerid-providerelementid

Retrieve the approval status of third-party taxonomy data changes for the specified element. For a list of possible statuses, see [Check Data Change Status](/v3/portal/data/doc/ThirdPartyDataManagement#check-status).  
**NOTE**: This endpoint is available only to third-party data providers.
