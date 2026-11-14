# Campaign Flight

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Campaign%20Flight
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Campaign%20Flight (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL campaignFlightCreate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-flight-create

Create a campaign flight using the data specified in the input.

### GraphQL campaignFlightUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-flight-update

Updates a campaign flight using the data specified in the input.

### GraphQL campaignFlightDelete Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-flight-delete

Deletes a campaign flight using the campaign flight ID provided in the input.

### POST /v3/campaignflight (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-campaignflight

This is a legacy endpoint. Use the [`campaignFlightCreate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-flight-create) in GraphQL for improved performance and expanded functionality.

Create a new campaign flight.  
IMPORTANT: You may not use this API to add flights to campaigns that have no flights defined.

### PUT /v3/campaignflight (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-campaignflight

This is a legacy endpoint. Use the \[`campaignFlightUpdate` mutation\]\](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-flight-update) in GraphQL for improved performance and expanded functionality.

Update an existing campaign flight.  
Here's what you need to know about updating campaign flights:

*   You may not modify a past flight (with the end date set to a date in the past).
*   You may not set the flight end date to a date in the past.
*   You may not change the start date of a flight that has started spending.

### GET /v3/campaignflight/{campaignFlightId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaignflight-campaignflightid

This is a legacy endpoint. Use the [`campaign` -> `flights` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign) with filtering in GraphQL for improved performance and expanded functionality.

Get an existing campaign flight for the specified ID.  
**TIP**: Using the equivalent campaign flight GraphQL query, you can enhance performance, customize criteria, and, if needed, expand your search across multiple campaigns.  
For details, see [Campaign Flights](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CampaignQueryExamplesGQL#campaign-flights).

### DELETE /v3/campaignflight/{campaignFlightId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/delete-campaignflight-campaignflightid

This is a legacy endpoint. Use the [`campaignFlightDelete` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-flight-delete) in GraphQL for improved performance and expanded functionality.

Delete an existing campaign flight for the specified ID.  
Here's what you need to know about deleting campaign flights:

*   The API will only permit deleting flights that are in the past if it is also the last flight defined for the campaign.
*   You may not delete the flight if it is the only flight in the campaign.
*   You may not delete a flight if the flight has already started spending.
*   You may not delete a past flight (with the end date set to a date in the past).
