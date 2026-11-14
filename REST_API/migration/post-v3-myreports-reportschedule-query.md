# POST /v3/myreports/reportschedule/query → Query.myReportsReportSchedules

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-myreports-reportschedule-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/myreports/reportschedule/query → Query.myReportsReportSchedules

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/myreports/reportschedule/query` |
| GraphQL query | `Query.myReportsReportSchedules` |
| Return type | `MyReportsReportSchedulesConnection` (`MyReportsReportSchedule` nodes) |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SortFields` | `order` | [MyReportsReportScheduleSortInput!] | Optional | REST Name/CreationDate → `order.name` / `order.createdDate`. |
| `ReportScheduleIds` | `where.searchText.like` | String | Optional | GraphQL supports exact schedule ID match, not a list filter. |
| `NameContains` | `where.name.contains` | String | Optional | N/A |
| `RequestedByUserNameContains` | N/A | N/A | Optional | **Remodelled in GraphQL** |
| `ShowOnlyRequestedByMe` | `where.createdByCurrentUser.eq` | Boolean | Optional | Approximate mapping; REST defaults to current user when no filters applied. |
| `ReportScheduleStatus` | `where.status.eq` | ReportScheduleStatus | Optional | Enum name parity Active/Disabled. |
| `ReportTemplateIds` | N/A | N/A | Optional | **Remodelled in GraphQL** |
| `IsCompleted` | N/A | N/A | Optional | **Remodelled in GraphQL** |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [MyReportsReportSchedule!] | Nullable | N/A |
| `ResultCount` | (derived from `nodes`) | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].ReportScheduleId` | `id` | ID! | Not nullable | long → ID. |
| `Result[].ReportScheduleName` | `name` | String! | Not nullable | N/A |
| `Result[].RequestedByUserName` | `createdByUser` | UserBasicInfo | Nullable | string → UserBasicInfo object. |
| `Result[].CreationDateUtc` | `createdDate` | DateTime! | Not nullable | N/A |
| `Result[].ReportTemplateId` | `templateId` | Long | Nullable | N/A |
| `Result[].IsCompleted` | N/A | N/A | N/A | No `isCompleted` on `MyReportsReportSchedule`; infer from `activeExecution.state` if needed. |
| `Result[].ReportScheduleStatus` | `status` | ReportScheduleStatus! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/myreports/reportschedule/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 25,
  "NameContains": "Weekly",
  "ReportScheduleStatus": "Active",
  "ShowOnlyRequestedByMe": true
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query MyReportsReportSchedules {
  myReportsReportSchedules(
    first: 25
    where: {
      name: { contains: "Weekly" }
      status: { eq: ACTIVE }
      createdByCurrentUser: { eq: true }
    }
    order: [{ createdDate: DESC }]
  ) {
    nodes {
      id
      name
      status
      templateId
      createdDate
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
