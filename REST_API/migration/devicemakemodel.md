# Device make model: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/devicemakemodel-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Device make model: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/devicemakemodel/query` | `Query.deviceModels` | Paged connection with optional name filter across make, model, and marketing name |
