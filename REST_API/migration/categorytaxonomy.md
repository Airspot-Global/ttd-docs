# Category taxonomy: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/categorytaxonomy-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Category taxonomy: REST → GraphQL migration guide

In GraphQL, the REST `Category` response shape for taxonomy trees is exposed as `TaxonomyIndustryCategory` on `CategoryTaxonomy.industryCategories`. The separate `IndustryCategory` type (with `mappings`, `isDefault`, and `taxonomy`) is a different GraphQL type used on other paths.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/categorytaxonomy/industrycategorytaxonomies` | `Query.industryCategoryTaxonomies` | Lists all industry category taxonomies. |
| `GET /v3/categorytaxonomy/{categoryTaxonomyId}/category/industrycategories` | `CategoryTaxonomy.industryCategories` | Industry category tree as `[TaxonomyIndustryCategory!]!`; also reachable via `industryCategoryTaxonomies { industryCategories }`. Cross-taxonomy `MappingInformation` from REST is not on `TaxonomyIndustryCategory`—use `IndustryCategory.mappings` where needed. |
