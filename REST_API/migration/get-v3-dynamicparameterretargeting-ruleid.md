# GET /v3/dynamicparameterretargeting/{ruleId} → Query.dynamicParameterRetargeting

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-dynamicparameterretargeting-ruleid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/dynamicparameterretargeting/{ruleId} → Query.dynamicParameterRetargeting

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/dynamicparameterretargeting/{ruleId}` |
| GraphQL query | `Query.dynamicParameterRetargeting(id: ID!)` |
| Return type | `DynamicParameterRetargetingRule` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `RuleId` | `id` | ID! | Not nullable | Already available on `TrackingTag.dynamicTrackingRule.id` Available on `TrackingTag.dynamicTrackingRule`. |
| `TrackingTagId` | `trackingTagId` | ID! | Not nullable | N/A |
| `SegmentName` | `segmentName` | String! | Not nullable | Computed from the associated tracking tag name. |
| `EvaluatedParameter` | `evaluatedParameter` | String! | Not nullable | N/A |
| `FunctionId` | `functionId` | Int! | Not nullable | Surfaced as an integer scalar (not an enum). |
| `StringParameter` | `stringParameter` | String | Nullable | Valid for alphanumeric functions only. |
| `NumericParameter` | `numericParameter` | Decimal | Nullable | Valid for numeric functions only. |
| `SecondaryNumericParameter` | `secondaryNumericParameter` | Decimal | Nullable | Valid for numeric functions accepting a secondary parameter. |
| `CreatedAt` | `createdAt` | DateTime | Nullable | Read-only. |
| `LastUpdatedAt` | `lastUpdatedAt` | DateTime | Nullable | Read-only. |
| `IsArchived` | N/A | N/A | N/A | Remodelled in GraphQL |

## Code examples

### REST example

```
GET /v3/dynamicparameterretargeting/{ruleId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetDynamicParameterRetargetingRule($id: ID!) {
  dynamicParameterRetargeting(id: $id) {
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
```
