# GET /v3/myreports/view/{scheduleExecutionId}/{scheduleDeliveryId}/{exp} → Query.myReportsReportSchedule (partial)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-myreports-view-scheduleexecutionid-scheduledeliveryid-exp
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/myreports/view/{scheduleExecutionId}/{scheduleDeliveryId}/{exp} → Query.myReportsReportSchedule (partial)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/myreports/view/{scheduleExecutionId}/{scheduleDeliveryId}/{exp}` |
| GraphQL query | `Query.myReportsReportSchedule(id:)` |

**GraphQL Field:** `activeExecution.delivery.downloadLink`**Return Type:** `String`

> **Advisory:** REST returns **HTTP 302** with a `Location` header pointing at the signed report download URL. There is **no JSON response body**. The closest GraphQL field is `activeExecution.delivery.downloadLink`, which exposes a download link string rather than following the signed redirect URL flow—auth and signature models differ; verify before migrating clients.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| (report schedule ID) | `myReportsReportSchedule(id:)` | ID! | Required | GraphQL entry point: pass the report **schedule** ID (same identifier as `scheduleId` on `GET /v3/myreports/reportschedule/{scheduleId}`), **not** `scheduleExecutionId` from this REST path. |
| `scheduleExecutionId` | N/A | N/A | Required | **REST transport only** |
| `scheduleDeliveryId` | N/A | N/A | Required | REST path parameter; no GraphQL argument—`delivery` is a singular object that may not correspond to this REST delivery ID. |
| `exp` | N/A | N/A | Required | **REST transport only** |
| `sig` | N/A | N/A | Required | **REST transport only** |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| (response body) | N/A | N/A | N/A | REST returns HTTP 302 redirect to report download; no JSON response body. |
| (redirect target) | `activeExecution.delivery.downloadLink` | String | Nullable | GraphQL exposes a download link string on the schedule's most recent execution delivery rather than following the signed redirect URL flow. `activeExecution` resolves the **most recent** execution for the schedule (may differ from the REST URL's `scheduleExecutionId`), and `delivery` is a single object (may differ from the REST URL's `scheduleDeliveryId`). Different auth/signature model—verify before migrating clients. |

## Code examples

### REST example

```
GET /v3/myreports/view/{scheduleExecutionId}/{scheduleDeliveryId}/{exp}?sig={signature} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ReportDownloadLink {
  myReportsReportSchedule(id: "12345") {
    activeExecution {
      delivery {
        downloadLink
      }
    }
  }
}
```
