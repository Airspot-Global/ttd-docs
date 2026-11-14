# Factual proximity design: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/factualproximitydesign-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Factual proximity design: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/factualproximitydesign/query/partner` | `Partner.factualProximityDesigns` | Paged connection on `Partner` with optional name filter. No GET-by-ID endpoint. |
