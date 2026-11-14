# Ad technology: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/adtechnology-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Ad technology: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/adtechnology/query` | `Query.adTechnologies` | Paged connection with search terms and sort; forward-only pagination. For vendors on a specific creative, use `creative(id:).googleVendors` instead. |
