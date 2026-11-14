# POST /v3/myreports/reporttemplateheader/query → Query.reportingTemplates

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-myreports-reporttemplateheader-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/myreports/reporttemplateheader/query → Query.reportingTemplates

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/myreports/reporttemplateheader/query` |
| GraphQL query | `Query.reportingTemplates` |
| Return type | `ReportingTemplatesConnection` (`MyReportsTemplate` nodes) |

**Deprecated on REST**—use `reportingTemplates` instead.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SortFields` | `order` | [ReportTemplatesSortInput!] | Optional | REST sort fields Name/CreatedBy map to `ReportTemplatesSortInput.name` / `createdByName` (not 1:1 field IDs). |
| `SortFields[].FieldId` | `order[].name` (per field) | SortEnumType | Required | Enum → SortEnumType per sort field. |
| `SortFields[].Ascending` | `order[].*` | SortEnumType | Optional | GraphQL uses ASC/DESC enum per sort field, not boolean ascending flag. |
| `CreatedByContains` | `where.createdByName.contains` | String | Optional | N/A |
| `NameContains` | `where.name.contains` | String | Optional | N/A |
| `Format` | `where.format.eq` | ReportFormatType | Optional | `ReportTemplateFormat` → `ReportFormatType`. |
| `ReportTemplateIds` | `where.id.in` | [Long] | Optional | string → Long ID filter. |
| `ShowOnlyCreatedByMe` | N/A | N/A | Optional | No direct filter on `reportingTemplates`. Default behavior may scope to current user for some queries; verify—not exposed as explicit filter arg. |
| `Type` | `where.userGenerated` | Boolean | Optional | REST Standard ≈ `userGenerated:false`; Custom ≈ `userGenerated:true`. |
| `Type` | `where.recommendedTemplateType` | ReportTemplateType | Optional | Covers suggested/recommended template filtering. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [MyReportsTemplate!] | Nullable | N/A |
| `ResultCount` | (derived from `nodes`) | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].ReportTemplateId` | `id` | ID! | Not nullable | long → ID. |
| `Result[].Name` | `name` | String! | Not nullable | N/A |
| `Result[].Type` | `userGenerated` | Boolean! | Not nullable | REST Standard ≈ `userGenerated:false`; Custom ≈ `userGenerated:true`. |
| `Result[].Type` | `recommendedTemplateDetails` | SuggestedReportTemplate | Nullable | Suggested/recommended templates; null when not a recommended template. |
| `Result[].Format` | `format` | ReportFormatType! | Not nullable | N/A |
| `Result[].CreatedByUserName` | `createdByName` | String | Nullable | N/A |

## Endpoint-specific nested types and enums

### ReportTemplateHeader

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ReportTemplateId` | `id` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |
| `Type` | `userGenerated` | Boolean! | Not nullable | REST Standard ≈ `userGenerated:false`; Custom ≈ `userGenerated:true`. |
| `Type` | `recommendedTemplateDetails` | SuggestedReportTemplate | Nullable | Suggested/recommended templates; null when not a recommended template. |
| `Format` | `format` | ReportFormatType! | Not nullable | N/A |
| `CreatedByUserName` | `createdByName` | String | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/myreports/reporttemplateheader/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 25,
  "NameContains": "Weekly",
  "Format": "Excel"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ReportingTemplates {
  reportingTemplates(
    first: 25
    where: { name: { contains: "Weekly" }, format: { eq: EXCEL } }
    order: [{ name: ASC }]
  ) {
    nodes {
      id
      name
      format
      createdByName
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
