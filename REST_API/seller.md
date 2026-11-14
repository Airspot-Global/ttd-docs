# Seller

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Seller
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Seller (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/seller/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-seller-query

Retrieve a paged, filterable list of sellers, seller domains, and whether they can be targeted as a `SellerDomain` in a [bid list](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlist).  
This will only return sellers that have spent through our platform.

### GET /v3/seller/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-seller-query-facets

Retrieve the properties that can be used for sorting and filtering seller results in [POST /seller/query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-seller-query).

### GET /v3/seller/{sellerDomain}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-seller-sellerdomain

Retrieve seller details for a specific seller domain. `SellerDomains` can be targeted in [bid lists](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-bidlist).  
This will return all sellers regardless of whether they have spent through our platform.
