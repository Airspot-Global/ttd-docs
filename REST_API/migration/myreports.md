# My reports: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/myreports-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# My reports: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/myreports/reportexecution/query/advertisers` | `Advertiser.reportExecutions` | N/A |
| `POST /v3/myreports/reportexecution/query/partners` | `Partner.reportExecutions` | N/A |
| `GET /v3/myreports/view/{scheduleExecutionId}/{scheduleDeliveryId}/{exp}` | `ScheduleExecution.delivery.downloadLink` | Partial—REST returns an HTTP 302 redirect; GraphQL field exposes the download link string (different auth/signature model, verify before migrating) |
| `POST /v3/myreports/reporttemplateheader/query` | `Query.reportingTemplates` | N/A |
| `POST /v3/myreports/supportedtailaggregationprofiles/query` | `Query.derivedReportTemplate` | Flat REST page → nested template columns |
| `POST /v3/myreports/reportschedule/query` | `Query.myReportsReportSchedules` | **Not currently available in GraphQL** |
| `GET /v3/myreports/reportschedule/{scheduleId}` | `Query.myReportsReportSchedule(id:)` | N/A |
| `POST /v3/myreports/conversionpixelnames` | `Query.historicalConversionPixels` | **Not currently available in GraphQL** |

## Shared nested types and enums

### ReportDelivery

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ReportDestination` | `reportDestination` | ReportDestination! | Not nullable | N/A |
| `DeliveredPath` | `deliveredPath` | String | Nullable | N/A |
| `DeliveredUTC` | `deliveredUtc` | DateTime | Nullable | N/A |
| `DownloadURL` | `downloadUrl` | String | Nullable | N/A |
| `DownloadURLExpirationUTC` | `downloadUrlExpirationUtc` | DateTime | Nullable | N/A |

### ReportExecutionStateInput (filter) vs ScheduleExecutionStateDisplayType (output)

The filter arg enum and the output `state` enum share the same backing data but differ in granularity:

- **Filter**—`reportExecutions(filter: { reportExecutionStates: [...] })` uses `ReportExecutionStateInput` (5 values), matching REST `ReportExecutionState` display names.
- **Output**—connection nodes expose `ScheduleExecution.state: ScheduleExecutionStateDisplayType` (8 values), which surfaces the raw platform states 1:1.

| Platform state | Output `ScheduleExecutionStateDisplayType` | Filter `ReportExecutionStateInput` | REST `ReportExecutionState` |
| --- | --- | --- | --- |
| WaitingForDependencies | `WAITING_FOR_DEPENDENCIES` | `PENDING` | `Pending` |
| InProgress | `IN_PROGRESS` | `IN_PROGRESS` | `In Progress` |
| Completed | `COMPLETED` | `COMPLETE` | `Complete` |
| Failed | `FAILED` | `FAILED` | `Failed` |
| Canceled | `CANCELED` | `CANCELED` | `Canceled` |
| WaitingForRetryAfterFailure | `WAITING_FOR_RETRY_AFTER_FAILURE` | `PENDING` | `Pending` |
| WaitingForExecution | `WAITING_FOR_EXECUTION` | `PENDING` | `Pending` |
| WaitingForFailureHandling | `WAITING_FOR_FAILURE_HANDLING` | `PENDING` | `Pending` |

**Consequence (by design, mirrors REST):** the filter↔output relationship is many-to-one. Filtering by `PENDING` returns nodes whose `state` reads back as one of `WAITING_FOR_DEPENDENCIES` / `WAITING_FOR_EXECUTION` / `WAITING_FOR_RETRY_AFTER_FAILURE` / `WAITING_FOR_FAILURE_HANDLING`—there is no `PENDING` value in the output enum. Likewise filter `COMPLETE` ↔ output `COMPLETED`.

### ConversionPixel

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser.id` | ID! | Not nullable | N/A |
| `ConversionPixelName` | `trackingTag.name` | String! | Not nullable | N/A |
| `ConversionType` | `trackingTag.id` | String! | Not nullable | Tracking tag ID. |
| `CrossDeviceAttributionModelId` | `crossDeviceAttribution.model` / `crossDeviceAttributionModelId` | CrossDeviceAttributionModelId | Nullable | On schedule read, field is `crossDeviceAttributionModelId`. |

### SupplyVendorDeal

GraphQL exposes only entity identifiers—REST floor price and supply-vendor ID are not on this type.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `SupplyVendorId` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `SupplyVendorDealId` | `supplyVendorDealCode` | String! | Not nullable | REST deal code. |
| `FloorPriceCPM.Amount` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `FloorPriceCPM.CurrencyCode` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| (composite key) | `id` | ID! | Not nullable | Entity identifier for the deal. |

### MyReportsTailAggregation

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ColumnId` | `columnId` | Int! | Not nullable | On schedule read: `columnId`. |
| `ColumnId` | `id` | ID! | Not nullable | On derived template: `id`. |
| `ColumnName` | `name` | String! | Not nullable | On derived template columns only. |
| `TailAggregationProfileId` | `tailAggregationProfile` / `tailAggregations` | TailAggregationProfileType! | Not nullable | long profile ID → enum. |
| `TailAggregationProfileDescription` | N/A | N/A | N/A | No separate description field in GraphQL. |
