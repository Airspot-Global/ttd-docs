# POST /v3/myreports/supportedtailaggregationprofiles/query → Query.derivedReportTemplate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-myreports-supportedtailaggregationprofiles-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/myreports/supportedtailaggregationprofiles/query → Query.derivedReportTemplate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/myreports/supportedtailaggregationprofiles/query` |
| GraphQL query | `Query.derivedReportTemplate` |
| Return type | `DerivedReportTemplateResult` |

> **Note:** `DerivedReportTemplateResult` is a union; the success payload is `MyReportsGetDerivedTemplateResponse`. Expand tail-aggregation columns from `resultSets[].fields`, `resultSets[].metrics`, and `resultSets[].conversionMetrics[].columnType` where `columnType.tailAggregations` is non-null.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `ReportTemplateId` | `derivedReportTemplate(id:)` | ID! | Required | long → ID. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `resultSets[].fields\\| metrics\\| conversionMetrics[].columnType` | ReportingColumn | Nullable | N/A |
| `ResultCount` | (derived) | N/A | N/A | N/A |
| `TotalFilteredCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].ColumnId` | `columnType.id` | ID! | Not nullable | int → ID on `ReportingColumn`. |
| `Result[].ColumnName` | `columnType.name` | String! | Not nullable | N/A |
| `Result[].TailAggregationProfileId` | `columnType.tailAggregations` | [TailAggregationProfileType!] | Nullable | GraphQL exposes enum values, not numeric profile IDs. Also available via `reportTypes.reportingColumns.tailAggregations`. |
| `Result[].TailAggregationProfileDescription` | N/A | N/A | N/A | GraphQL `TailAggregationProfileType` enum has descriptions in schema but no separate description string field per profile row. |

## Endpoint-specific nested types and enums

### SupportedTailAggregationProfile

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ColumnId` | `columnType.id` | ID! | Not nullable | Reporting column ID on `ReportingColumn`. |
| `ColumnName` | `columnType.name` | String! | Not nullable | N/A |
| `TailAggregationProfileId` | `columnType.tailAggregations` | [TailAggregationProfileType!] | Nullable | long profile ID → enum list on `ReportingColumn`. |
| `TailAggregationProfileDescription` | N/A | N/A | N/A | No separate description field in GraphQL. |

## Code examples

### REST example

```
POST /v3/myreports/supportedtailaggregationprofiles/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "ReportTemplateId": 98765
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query SupportedTailAggregations {
  derivedReportTemplate(id: "98765") {
    ... on MyReportsGetDerivedTemplateResponse {
      resultSets {
        fields {
          columnType {
            id
            name
            tailAggregations
          }
        }
        metrics {
          columnType {
            id
            name
            tailAggregations
          }
        }
        conversionMetrics {
          columnType {
            id
            name
            tailAggregations
          }
        }
      }
    }
  }
}
```
