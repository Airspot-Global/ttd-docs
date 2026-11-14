# POST /v3/myreports/reportexecution/query/advertisers → Advertiser.reportExecutions

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-myreports-reportexecution-query-advertisers
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/myreports/reportexecution/query/advertisers → Advertiser.reportExecutions

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/myreports/reportexecution/query/advertisers` |
| GraphQL query | `Advertiser.reportExecutions` |
| Return type | `ReportExecutionsConnection` |

## Multi-step operations

This REST POST-as-query maps to the `reportExecutions` relationship field on a parent `Advertiser`. The advertiser context comes from the parent entity (`Advertiser.id`); filter body fields attach to the relationship field's filter input.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserIds` | Parent: `Advertiser.reportExecutions`; parent ID from `Advertiser.id` | N/A | Required | Cross-domain relationship on `Advertiser`. Filter body `AdvertiserIds` aligns with the parent advertiser context. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SortFields` | `filter.sortFields` | [ReportExecutionSortingFieldSortingInput!] | Optional | Optional sort on the relationship field filter input. |
| `ExecutionStates` | N/A | N/A | Optional | **Deprecated on REST**—use `ReportExecutionStates`. |
| `ReportExecutionStates` | `filter.reportExecutionStates` | [ReportExecutionStateInput!] | Optional | When specified, only executions in these states are returned. REST display names (e.g. `Complete`) map to `ReportExecutionStateInput` values (e.g. `COMPLETE`). |
| `ExecutionSpansStartDate` | `filter.executionSpansStartDate` | DateTime | Optional | Filter where `reportEndDateExclusive` is after this value. |
| `ExecutionSpansEndDate` | `filter.executionSpansEndDate` | DateTime | Optional | Filter where `reportStartDateInclusive` is on or before this value. |
| `ReportScheduleIds` | `filter.reportScheduleIds` | [ID!] | Optional | Schedule IDs of executions to retrieve. Exposed as `ID`; parsed back to the REST `long` body. |
| `ReportScheduleNameContains` | `filter.reportScheduleNameContains` | String | Optional | Case-insensitive substring match on schedule name. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[ScheduleExecution!]` | Nullable | N/A |
| `ResultCount` | (derived from `nodes`) | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].ReportExecutionId` | `id` | ID! | Not nullable | Already available as `ScheduleExecution.id`. |
| `Result[].ReportExecutionState` | `state` | ScheduleExecutionStateDisplayType | Nullable | REST enum is a subset of `ScheduleExecutionStateDisplayType`. See the MyReports domain page for filter vs output enum mapping. |
| `Result[].LastStateChangeUTC` | `lastStatusChangeDate` | DateTime | Nullable | Already available as `ScheduleExecution.lastStatusChangeDate`. |
| `Result[].DisabledReason` | `disabledReason` | String | Nullable | REST merges schedule + template disable reasons. |
| `Result[].Timezone` | `timezone` | String | Nullable | REST embeds schedule timezone on each execution row. |
| `Result[].ReportStartDateInclusive` | `reportStartDateInclusive` | DateTime | Nullable | Already available on `ScheduleExecution`. |
| `Result[].ReportEndDateExclusive` | `reportEndDateExclusive` | DateTime | Nullable | Already available on `ScheduleExecution`. |
| `Result[].ReportScheduleId` | `reportScheduleId` | ID | Nullable | Exposed as `ID`—REST `long` rendered as a string ID. |
| `Result[].ReportScheduleName` | `reportScheduleName` | String | Nullable | Flattened schedule name on the execution node for REST parity. |
| `Result[].ReportDeliveries` | `reportDeliveries` | [ReportDelivery!] | Nullable | REST returns a filtered list. See the MyReports domain page for `ReportDelivery` field details. |

## Code examples

### REST example

```
POST /v3/myreports/reportexecution/query/advertisers HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserIds": ["<advertiser-id>"],
  "PageStartIndex": 0,
  "PageSize": 10,
  "ReportExecutionStates": ["Complete"]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserReportExecutions {
  advertiser(id: "<advertiser-id>") {
    id
    reportExecutions(
      filter: { reportExecutionStates: [COMPLETE] }
      first: 10
    ) {
      totalCount
      nodes {
        id
        disabledReason
        timezone
        reportScheduleName
        reportDeliveries {
          reportDestination
          deliveredPath
          downloadUrl
        }
      }
    }
  }
}
```
