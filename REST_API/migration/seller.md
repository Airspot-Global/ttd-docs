# Seller: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/seller-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Seller: REST → GraphQL migration guide

REST sellers map to the GraphQL `Publisher` entity: list and filter via `Query.publishers`, and select seller-specific fields on each `Publisher` node.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/seller/query` | `Query.publishers` | N/A |
| `GET /v3/seller/{sellerDomain}` | `Query.publishers(where:)` | Filter `where.publisherDomain` to match the REST path parameter |

## Shared nested types and enums

### SellerStatus

| REST value | GraphQL value | Notes |
| --- | --- | --- |
| `Allowed` | `ALLOWED` | N/A |
| `Disallowed` | `DISALLOWED` | N/A |

Distinct from `Publisher.marketplaceState` (marketplace participation state).
