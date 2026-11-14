# GET /v3/categorytaxonomy/{categoryTaxonomyId}/category/industrycategories → CategoryTaxonomy.industryCategories

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-categorytaxonomy-categorytaxonomyid-category-industrycategories
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/categorytaxonomy/{categoryTaxonomyId}/category/industrycategories → CategoryTaxonomy.industryCategories

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/categorytaxonomy/{categoryTaxonomyId}/category/industrycategories` |
| GraphQL query | `CategoryTaxonomy.industryCategories` |
| Return type | `[TaxonomyIndustryCategory!]!` |

The REST response uses the `Category` type; GraphQL exposes the same tree shape as `TaxonomyIndustryCategory` on `CategoryTaxonomy.industryCategories`. This is distinct from the separate `IndustryCategory` type (which includes `mappings`, `isDefault`, and `taxonomy`).

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `CategoryTaxonomy.industryCategories` | [TaxonomyIndustryCategory!]! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].CategoryId` | `id` | ID | Nullable | `long` → `ID`. |
| `Result[].Name` | `name` | String! | Not nullable | N/A |
| `Result[].ParentCategoryId` | `parentCategoryId` | ID | Nullable | `long` → `ID`; null at root. |
| `Result[].IsSensitive` | `isSensitive` | Boolean! | Not nullable | N/A |
| `Result[].MappingInformation` | N/A | N/A | N/A | REST nested list per category. Not on `TaxonomyIndustryCategory`; see `CategoryMapping` leaves and `IndustryCategory.mappings` below. |
| `Result[].MappingInformation[].CategoryTaxonomyId` | `IndustryCategory.mappings[].taxonomyId` | Int! | Not nullable | **Not currently available in GraphQL** |
| `Result[].MappingInformation[].CategoryId` | `IndustryCategory.mappings[].categoryId` | Int! | Not nullable | Same remodelled path as `CategoryTaxonomyId`. |
| `Result[].MappingInformation[].ExternalId` | `IndustryCategory.mappings[].externalId` | String! | Not nullable | Same remodelled path as `CategoryTaxonomyId`. |
| `Result[].ExternalId` | `externalId` | String | Nullable | N/A |
| `Result[].Path` | `path` | String! | Not nullable | Computed hierarchy path. |
| `Result[].Children` | `children` | [TaxonomyIndustryCategory!]! | Not nullable | Recursive self-reference for the category tree. |

## Endpoint-specific nested types and enums

### TaxonomyIndustryCategory

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CategoryId` | `id` | ID | Nullable | `long` → `ID`. |
| `Name` | `name` | String! | Not nullable | N/A |
| `ParentCategoryId` | `parentCategoryId` | ID | Nullable | Null at root. |
| `IsSensitive` | `isSensitive` | Boolean! | Not nullable | N/A |
| `MappingInformation` | N/A | N/A | N/A | Not on `TaxonomyIndustryCategory`; see `CategoryMapping` below and `IndustryCategory.mappings`. |
| `ExternalId` | `externalId` | String | Nullable | N/A |
| `Path` | `path` | String! | Not nullable | Computed hierarchy path. |
| `Children` | `children` | [TaxonomyIndustryCategory!]! | Not nullable | Recursive tree. |

### CategoryMapping

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CategoryTaxonomyId` | `IndustryCategory.mappings[].taxonomyId` | Int! | Not nullable | Remodelled path—query `IndustryCategory` (not `TaxonomyIndustryCategory`) for cross-taxonomy mappings. |
| `CategoryId` | `IndustryCategory.mappings[].categoryId` | Int! | Not nullable | N/A |
| `ExternalId` | `IndustryCategory.mappings[].externalId` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/categorytaxonomy/1/category/industrycategories HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query IndustryCategoriesByTaxonomy {
  industryCategoryTaxonomies {
    id
    industryCategories {
      id
      name
      parentCategoryId
      isSensitive
      externalId
      path
      children {
        id
        name
        path
      }
    }
  }
}
```
