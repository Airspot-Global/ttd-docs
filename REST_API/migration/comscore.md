# Comscore: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/comscore-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Comscore: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/comscore/populationdemographicmembers` | `Query.comscorePopulations` | Unpaged full list with nested demographic members |
