# Category: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/category-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Category: REST → GraphQL migration guide

Distinct from industry category trees in the CategoryTaxonomy domain (`IndustryCategory`).

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/category/query` | `Query.categories` | Paged connection; requires `categorySourceType` and at least one of `partnerId` or `advertiserId`. |
