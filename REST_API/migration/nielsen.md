# Nielsen: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/nielsen-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Nielsen: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/nielsen/reportingcountries` | `Query.nielsenReportingCountries` | Full country list; GraphQL exposes a filterable connection |
| `POST /v3/nielsen/brand/query` | `Query.nielsenBrands` | Paged connection with optional `searchTerm` |
