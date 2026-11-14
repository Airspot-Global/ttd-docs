# Dynamic parameter retargeting: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/dynamicparameterretargeting-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Dynamic parameter retargeting: REST → GraphQL migration guide

Single-rule reads use `Query.dynamicParameterRetargeting(id:)`; advertiser lists use `Advertiser.dynamicParameterRetargetingRules`.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/dynamicparameterretargeting/{ruleId}` | `Query.dynamicParameterRetargeting(id:)` | Get a single rule by ID |
| `POST /v3/dynamicparameterretargeting/query/advertiser` | `Advertiser.dynamicParameterRetargetingRules(first:, after:)` | Paged connection with optional search and sort filters |

## Shared nested types and enums

### DynamicParameterRetargetingRule

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
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
