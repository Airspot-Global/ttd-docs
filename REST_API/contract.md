# Contract

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Contract
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Contract (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/contract

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract

Create a new Contract.

### PUT /v3/contract

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-contract

Update an existing Contract.

### POST /v3/contract/buyers/query/advertisers

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract-buyers-query-advertisers

Query for Advertisers that may act as buyers of Contracts offered by the chosen Partner.  
These are the Advertisers that may be specified in ContractPermissions of the Partner's Contracts.

### POST /v3/contract/buyers/query/partners

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract-buyers-query-partners

Query for info about all the Partners that may act as buyers for Contracts offered by the chosen Partner.  
These are the Partners that may be specified in the ContractsPermissions of the Partner's Contracts.

### GET /v3/contract/{contractId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-contract-contractid

Get an existing Contract.

### GET /v3/contract/name/{contractId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-contract-name-contractid

Get the identifier and name for a Contract based on identifier

### POST /v3/contract/query/advertiser/available

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract-query-advertiser-available

Query for a page of Contracts that are available for the chosen Advertiser to buy.

### POST /v3/contract/query/deliveryprofile

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract-query-deliveryprofile

Query for a page of Contracts that are associated with specified DeliveryProfileId

### GET /v3/contract/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-contract-query-facets

Get the facets of Contracts that can be used in queries.

### POST /v3/contract/query/partner

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract-query-partner

Query for a page of Contracts owned by a Partner.

### POST /v3/contract/query/partner/available

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract-query-partner-available

Query for a page of Contracts that are available to the Advertisers under the chosen Partner.

### POST /v3/contract/query/supplyvendordeal

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract-query-supplyvendordeal

Query for a page of Contracts associated with the specific SupplyVendorDealId

### POST /v3/contract/report/impressions/available

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contract-report-impressions-available

Query for a page of an Available Impressions Report for a specific Contract.
