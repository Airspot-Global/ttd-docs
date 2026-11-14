# DMP

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/DMP
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/DMP (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL firstPartyDataDelta Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/first-party-data-delta

Get all changed first-party data for an advertiser since the last change-tracking version.

### GraphQL thirdPartyData Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/third-party-data

Get a third-party data segment by ID.

### GraphQL thirdPartyDatas Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/third-party-datas

Get third-party data segments.

### GraphQL thirdPartyDataProvider Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/third-party-data-provider

Gets a third-party data provider by provider ID.

### GraphQL thirdPartyDataProviders Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/third-party-data-providers

Get third-party data providers.

### POST /v3/dmp/firstparty/advertiser (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-dmp-firstparty-advertiser

We recommend using the [`advertiser` → `firstPartyData` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser) with filtering in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Retrieve first-party data for a given advertiser ID based on specified search parameters.  
**TIP**: You can use the equivalent advertiser GraphQL query to enhance performance, customize criteria, and, if needed, expand your search across multiple advertisers. For details, see [Look Up Advertiser Data Segments](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AdvertiserGQLQueryExamples#advertiser-data-segment-query).

### GET /v3/dmp/firstparty/facets (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-dmp-firstparty-facets

We recommend using the [`advertiser` → `firstPartyData` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser) with filtering in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Get the facets of First Party Data that can be retrieved and/or queried.

### GET /v3/dmp/lookalikemodel/build/{firstPartyDataId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-dmp-lookalikemodel-build-firstpartydataid

Build a Look-Alike Model for a First Party Data Id that does not have a Look-Alike Model (OR) rebuild the Look-Alike Model for a First Party Data Id.  
Look-Alike Models may be built for First Party Datas that have their LookAlikeEligibility status set to 'Eligible'.  
Use POST dmp/firstparty/advertiser to query whether a First Party Data is eligible for Look-Alike Modeling.  
When a Look-Alike Model is requested for the first time, it gets built within 5-10 minutes of when it was requested. This sets the generation date on the model, and once it has been built, every subsequent build gets queued with a 24 hour time lag.  
Please note that all time lags are subject to change, and design accordingly.  
It is recommended that you examine the status of the Look-Alike Model before attempting to retrieve the Third Party Data associated with the Model.

### GET /v3/dmp/lookalikemodel/{firstPartyDataId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-dmp-lookalikemodel-firstpartydataid

Get the Look-Alike Model that exists for a First Party Data Id.  
If the First Party data is not accessible or if a Look-Alike Model does not exist for the First Party Data Id, this will throw an error.  
It is recommended that you examine the status of the model returned in this call, before attempting to retrieve the Look-Alike Third Party Data.

### GET /v3/dmp/lookalikethirdpartydata/facets/{advertiserId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-dmp-lookalikethirdpartydata-facets-advertiserid

Get the Facets by which the Look-Alike Third Party data may be retrieved/queried.

### POST /v3/dmp/lookalikethirdpartydata/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-dmp-lookalikethirdpartydata-query

Retrieve the Third Party Data that are statistically similar to the First Party Data Id.  
To use this call, you must first build a Look-Alike model for the First Party Data using the GET dmp/lookalikemodel/build call.  
Once the Look-Alike Model Build Status is 'Ready', you may use this query to retrive the resulting Look-Alike Third Party Data.  
It is recommended that Third Party Data Look-Alikes be requested only for models that are 'Ready', and do not have a 'Queued' status.  
If the Look-Alike Model has a Queued status, it is likely that you might receive outdated data.  
Look-Alike Models once generated, are re-generated periodically, if a build has been requested on them by calling dmp/lookalikemodel/build/{firstpartydataid}.  
This re-generation lag is 24 hours currently(after Last Generation Date), but might change in the future, so please design accordingly.

### POST /v3/dmp/thirdparty/advertiser (legacy)

<!-- airspot:begin anchor="POST /v3/dmp/thirdparty/advertiser (legacy)" -->
> **Airspot note (observed 2026-11-09, sandbox + production; not in TTD's official docs):** This endpoint returned HTTP 500 in the sandbox. Its GraphQL replacement was not usable for us either: the root `thirdPartyDatas` query gave `INTERNAL_SERVER_ERROR` in the sandbox, and `partner { thirdPartyData }` timed out after 60 seconds in both sandbox and production.
<!-- airspot:end -->

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-dmp-thirdparty-advertiser

This is a legacy endpoint. Use the [`thirdPartyDatas` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/third-party-datas) in GraphQL for improved performance and expanded functionality.

Retrieve third-party data that matches the request. For details about how to maximize performance and reduce likelihood of timeouts, see [Rate Limits](https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/RateLimits).  
**IMPORTANT**: Segments are returned only if either active ID or received ID count is not `null` and is greater than zero. For details on active and received IDs, see [Unique ID Counting Methodologies](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/IdCountingMethodologies).

### GET /v3/dmp/thirdparty/facets/{advertiserId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-dmp-thirdparty-facets-advertiserid

This is a legacy endpoint. Use the [`thirdPartyDatas` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/third-party-datas) with filtering in GraphQL for improved performance and expanded functionality.

Get the facets of Third Party Data that can be retrieved and/or queried by the Advertiser.
