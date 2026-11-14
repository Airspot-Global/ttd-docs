# Overview

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Overview
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Overview (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GET /v3/overview/advertiser/{advertiserId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-overview-advertiser-advertiserid

This is a legacy endpoint. Use the [`advertiser` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser) in GraphQL for improved performance and expanded functionality.

Get an advertiser overview. An advertiser overview returns the hierarchy of descendant relationships and essential properties for those descendants.  
The overview endpoints reduce API payload and simplify the processes of hierarchy traversal and name or identifier retrieval.  
In alignment with lightweight processing, these overviews do not contain the full object detail for each descendant.  
Use the GET endpoints designed for the descendant entities to retrieve full detail.

### GET /v3/overview/partner/{partnerId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-overview-partner-partnerid

This is a legacy endpoint. Use the [`partner` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner) in GraphQL for improved performance and expanded functionality.

Get a partner overview. A partner overview returns the hierarchy of descendant relationships and essential properties for those descendants.  
The overview endpoints reduce API payload and simplify the processes of hierarchy traversal and name or identifier retrieval.  
In alignment with lightweight processing, these overviews do not contain the full object detail for each descendant.  
Use the GET endpoints designed for the descendant entities to retrieve full detail.
