# Supply vendor: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/supplyvendor-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Supply vendor: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/supplyvendor/query/advertiser` | `Advertiser.supplyVendors` | N/A |
| `POST /v3/supplyvendor/query/partner` | `Partner.supplyVendors` | N/A |
| `GET /v3/supplyvendorpublisher/{supplyVendorId}/{supplyVendorPublisherId}` | `SupplyVendor.publisher(supplyVendorPublisherId:)` | N/A |
| `GET /v3/supplyvendorbidding/query/{supplyVendorId}` | `SupplyVendor.bidding` | N/A |
