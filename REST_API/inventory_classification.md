# Inventory Classification

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Inventory%20Classification
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Inventory%20Classification (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/inventoryclassification/domainclasses/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-inventoryclassification-domainclasses-query

Retrieve a list of domain classes.  
**IMPORTANT**: Per our Marketplace Quality policies, we do not allow for the enumeration of this data. You can use this endpoint only to check a single entry, not to retrieve the entire list.  
Domain classes allow restricting spend on specific types of inventory unless the buyer explicitly opts in.  
This is a more transparent and flexible option than putting a site on an exclusion list.  
Classes are added to a domain semi-manually and can be set to block spend or to be used only for reporting purposes.  
If an domain has a class that is set to block spend, only ad groups that utilize domain targeting, seller targeting, or use a  
single-publisher private contract can bid on it.

### GET /v3/inventoryclassification/name/{domainClassId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-inventoryclassification-name-domainclassid

Get the identifier and name for a DomainClass based on identifier

### POST /v3/inventoryclassification/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-inventoryclassification-query

Retrieve a list of domains, apps, or app names that match the `SearchTerm`, along with their statuses. The list returns a maximum of 500 results.
