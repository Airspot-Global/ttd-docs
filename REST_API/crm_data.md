# Crm Data

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Crm%20Data
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Crm%20Data (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/crmdata/segment

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-crmdata-segment

Create a new CRM data segment. For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### POST /v3/crmdata/{segmentType}/segment

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-crmdata-segmenttype-segment

Create a new CRM data segment. For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### POST /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-crmdata-segmenttype-segment-advertiserid-crmdataid

Create a new drop for a CRM data segment. For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-crmdata-segmenttype-segment-advertiserid-crmdataid

Retrieve the status of a CRM data segment. For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}/{referenceId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-crmdata-segmenttype-segment-advertiserid-crmdataid-referenceid

Check the processing status of a CRM data drop (upload for a segment). For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### GET /v3/crmdata/segment/{advertiserId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-crmdata-segment-advertiserid

Retrieve all CRM data segments for the specified advertiser. For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### POST /v3/crmdata/segment/{advertiserId}/{crmDataId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-crmdata-segment-advertiserid-crmdataid

Create a new drop for a CRM data segment. For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### GET /v3/crmdata/segment/{advertiserId}/{crmDataId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-crmdata-segment-advertiserid-crmdataid

Retrieve the status of a CRM data segment. For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### DELETE /v3/crmdata/segment/{advertiserId}/{crmDataId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/delete-crmdata-segment-advertiserid-crmdataid

Delete a CRM data segment and purge its data. For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).

### GET /v3/crmdata/segment/{advertiserId}/{crmDataId}/{referenceId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-crmdata-segment-advertiserid-crmdataid-referenceid

Check the processing status of a CRM data drop (upload for a segment). For details on using the CRM Data API, see [Integrate CRM Data](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/DataIntegrateCRMData).
