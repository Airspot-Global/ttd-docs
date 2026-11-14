# POST /v3/dynamicparameterretargeting/query/advertiser → Advertiser.dynamicParameterRetargetingRules

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-dynamicparameterretargeting-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/dynamicparameterretargeting/query/advertiser → Advertiser.dynamicParameterRetargetingRules

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/dynamicparameterretargeting/query/advertiser` |
| GraphQL query | `Advertiser.dynamicParameterRetargetingRules(first: Int, after: String, where: DynamicParameterRetargetingRuleWhereInput, order: [DynamicParameterRetargetingRuleSortFieldInput!])` |
| Return type | `DynamicParameterRetargetingRulesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `Advertiser.dynamicParameterRetargetingRules` | N/A | Required | Resolved from the parent `Advertiser` entity and injected into the REST request. |
| `SearchTerms` | `where.searchTerms` | `[String!]` | Optional | Optional free-text search terms. |
| `SortFields` | `order` | `[DynamicParameterRetargetingRuleSortFieldInput!]` | Optional | Optional sort configuration; each entry has `fieldId` and optional `ascending`. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[DynamicParameterRetargetingRule!]` | Nullable | N/A |
| `Result[].RuleId` | `id` (on `DynamicParameterRetargetingRule`) | ID! | Not nullable | N/A |
| `Result[].TrackingTagId` | `trackingTagId` (on `DynamicParameterRetargetingRule`) | ID! | Not nullable | N/A |
| `Result[].SegmentName` | `segmentName` (on `DynamicParameterRetargetingRule`) | String! | Not nullable | Computed from the associated tracking tag name. |
| `Result[].EvaluatedParameter` | `evaluatedParameter` (on `DynamicParameterRetargetingRule`) | String! | Not nullable | N/A |
| `Result[].FunctionId` | `functionId` (on `DynamicParameterRetargetingRule`) | Int! | Not nullable | Surfaced as an integer scalar (not an enum). |
| `Result[].StringParameter` | `stringParameter` (on `DynamicParameterRetargetingRule`) | String | Nullable | Valid for alphanumeric functions only. |
| `Result[].NumericParameter` | `numericParameter` (on `DynamicParameterRetargetingRule`) | Decimal | Nullable | Valid for numeric functions only. |
| `Result[].SecondaryNumericParameter` | `secondaryNumericParameter` (on `DynamicParameterRetargetingRule`) | Decimal | Nullable | Valid for numeric functions accepting a secondary parameter. |
| `Result[].CreatedAt` | `createdAt` (on `DynamicParameterRetargetingRule`) | DateTime | Nullable | Read-only. |
| `Result[].LastUpdatedAt` | `lastUpdatedAt` (on `DynamicParameterRetargetingRule`) | DateTime | Nullable | Read-only. |
| `Result[].IsArchived` | N/A | N/A | N/A | Remodelled in GraphQL |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Endpoint-specific nested types and enums

### DynamicParameterRetargetingRuleSortFieldInput

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `fieldId` | `DynamicParameterRetargetingRuleSortingFieldInput!` | Sort field identifier. |
| `ascending` | `Boolean` | Sort direction; optional. |

### DynamicParameterRetargetingRuleSortingFieldInput

| Enum value | REST value |
| --- | --- |
| `TRACKING_TAG_ID` | 1 |
| `TRACKING_TAG_NAME` | 2 |
| `NAME` | 3 |
| `SEGMENT_TYPE` | 4 |

## Code examples

### REST example

```
POST /v3/dynamicparameterretargeting/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "{advertiserId}",
  "SearchTerms": ["revenue"],
  "SortFields": [{ "FieldId": "NAME", "Ascending": true }],
  "PageStartIndex": 0,
  "PageSize": 25
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetAdvertiserDynamicParameterRetargetingRules(
  $advertiserId: ID!
  $first: Int
  $after: String
) {
  advertiser(id: $advertiserId) {
    dynamicParameterRetargetingRules(
      first: $first
      after: $after
      where: { searchTerms: ["revenue"] }
      order: [{ fieldId: NAME, ascending: true }]
    ) {
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        id
        trackingTagId
        segmentName
        evaluatedParameter
        functionId
        stringParameter
        numericParameter
        secondaryNumericParameter
        createdAt
        lastUpdatedAt
      }
    }
  }
}
```
