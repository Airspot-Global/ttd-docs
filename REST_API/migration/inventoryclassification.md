# Inventory classification: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/inventoryclassification-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Inventory classification: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/inventoryclassification/query` | `Query.inventoryClassifications` | Paged inventory classification search; requires `input: InventoryClassificationQueryInput!` with `searchTerm` (4–100 chars) |
| `POST /v3/inventoryclassification/domainclasses/query` | `Query.domainClasses` | Paged domain class search; optional name filter (4–256 chars); requires `input: DomainClassQueryInput!` |
| `GET /v3/inventoryclassification/name/{domainClassId}` | `Query.domainClass(id:)` | Get domain class ID and display name by path parameter |
