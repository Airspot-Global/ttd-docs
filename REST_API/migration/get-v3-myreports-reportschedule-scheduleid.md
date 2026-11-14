# GET /v3/myreports/reportschedule/{scheduleId} → Query.myReportsReportSchedule

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-myreports-reportschedule-scheduleid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/myreports/reportschedule/{scheduleId} → Query.myReportsReportSchedule

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/myreports/reportschedule/{scheduleId}` |
| GraphQL query | `Query.myReportsReportSchedule(id:)` |
| Return type | `MyReportsReportSchedule!` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `scheduleId` | `myReportsReportSchedule(id:)` | ID! | Required | long → ID. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ReportScheduleId` | `id` | ID! | Not nullable | N/A |
| `ReportScheduleName` | `name` | String! | Not nullable | N/A |
| `RequestedByUserName` | `createdByUser` | UserBasicInfo | Nullable | string → UserBasicInfo object. |
| `CreationDateUtc` | `createdDate` | DateTime! | Not nullable | N/A |
| `ReportTemplateId` | `templateId` | Long | Nullable | N/A |
| `IsCompleted` | N/A | N/A | N/A | No `isCompleted` on `MyReportsReportSchedule`; infer from `activeExecution.state` if needed. |
| `ReportScheduleStatus` | `status` | ReportScheduleStatus! | Not nullable | N/A |
| `ReportFileFormat` | `reportDefinition` | MyReportsReportDefinition! | Not nullable | GraphQL stores format on schedule settings; not a top-level scalar on `MyReportsReportSchedule`. |
| `PartnerFilters` | `filters.partnerFilters` | [Partner!]! | Not nullable | string IDs → Partner objects. |
| `AdvertiserFilters` | `filters.advertiserFilters` | [Advertiser!]! | Not nullable | N/A |
| `CampaignFilters` | `filters.campaignFilters` | [Campaign!]! | Not nullable | N/A |
| `AdGroupFilters` | `filters.adGroupFilters` | [AdGroup!]! | Not nullable | N/A |
| `ContractFilters` | `filters.privateContractFilters` | [String!]! | Not nullable | N/A |
| `DealFilters` | `filters.supplyVendorDealFilters` | [SupplyVendorDeal!]! | Not nullable | See the MyReports domain page for `SupplyVendorDeal` field details. |
| `DealFilters[].SupplyVendorId` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `DealFilters[].SupplyVendorDealId` | `supplyVendorDealCode` | String! | Not nullable | REST deal code maps to `SupplyVendorDeal.supplyVendorDealCode`. |
| `DealFilters[].FloorPriceCPM.Amount` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `DealFilters[].FloorPriceCPM.CurrencyCode` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `TrackingTagFilters` | `filters.trackingTagFilters` | [TrackingTag!]! | Not nullable | N/A |
| `AdGroupCustomLabelFilters` | `filters.adGroupCustomLabelFilters` | [CustomLabel!]! | Not nullable | N/A |
| `CampaignCustomLabelFilters` | `filters.campaignCustomLabelFilters` | [CustomLabel!]! | Not nullable | N/A |
| `FilterOnAllAuthorizedAdvertisers` | N/A | N/A | N/A | Feature-gated REST filter; no direct field on filters—may require `filtersByReportTypeId`. |
| `ApplyDeltaFiltering` | N/A | N/A | N/A | **Read-only** |
| `ReportDateRange` | `lookbackWindowType` | MyReportsLookbackWindowType! | Not nullable | `ReportDateRange` → `MyReportsLookbackWindowType`. |
| `TimeZone` | `timezone` | String! | Not nullable | N/A |
| `ReportDateFormat` | `reportDateFormat` | ReportDateFormatType | Nullable | Enum rename. |
| `ReportNumericFormat` | `reportNumericFormat` | ReportNumberSeparatorType | Nullable | Enum rename. |
| `IncludeHeaders` | `includeHeaders` | Boolean | Nullable | N/A |
| `LookbackDays` | `lookbackWindowInDays` | Int | Nullable | N/A |
| `ReportFrequency` | `frequencyType` | ReportFrequencyType! | Not nullable | `ReportFrequency` → `ReportFrequencyType`. |
| `ScheduleStartDate` | `startDate` | DateTime! | Not nullable | N/A |
| `ReportStartDateInclusive` | `activeExecution.reportStartDateInclusive` | DateTime | Nullable | On schedule read, date range may be on `activeExecution` rather than schedule root. |
| `ReportEndDateExclusive` | `activeExecution.reportEndDateExclusive` | DateTime | Nullable | N/A |
| `AssociatedTailAggregationProfiles` | `tailAggregations` | [MyReportsTailAggregation!] | Nullable | See the MyReports domain page for tail aggregation field details. |
| `AssociatedTailAggregationProfiles[].ColumnId` | `columnId` | Int! | Not nullable | N/A |
| `AssociatedTailAggregationProfiles[].TailAggregationProfileId` | `tailAggregationProfile` | TailAggregationProfileType! | Not nullable | long → enum. |
| `ConversionPixelNames` | `conversionPixelMappings` | [ConversionPixelMapping!]! | Not nullable | See the MyReports domain page for `ConversionPixel` field details. |
| `ConversionPixelNames[].AdvertiserId` | `advertiser.id` | ID! | Not nullable | N/A |
| `ConversionPixelNames[].ConversionPixelName` | `trackingTag.name` | String! | Not nullable | N/A |
| `ConversionPixelNames[].ConversionType` | `trackingTag.id` | String! | Not nullable | Tracking tag ID. |
| `ConversionPixelNames[].CrossDeviceAttributionModelId` | `crossDeviceAttributionModelId` | CrossDeviceAttributionModelId! | Not nullable | N/A |
| `ConversionPixelMessage` | N/A | N/A | N/A | **REST transport only** |
| `EmailAddresses` | `emails` | [String!]! | Not nullable | N/A |
| `AcrBrandFilters` | `filters.acrBrandFilters` | [String!]! | Not nullable | int → String. |
| `IsOfflineConversionFilter` | `filters.isOfflineConversionFilters` | [Boolean!]! | Not nullable | N/A |
| `GracenoteAcrBrandFilters` | `filters.gracenoteAcrBrandFilters` | [String!]! | Not nullable | N/A |
| `GracenoteGenderFilters` | `filters.gracenoteGenderFilters` | [String!]! | Not nullable | N/A |
| `GracenoteAgeBracketFilters` | `filters.gracenoteAgeBracketFilters` | [String!]! | Not nullable | short → String. |
| `MerchantFilters` | `filters.merchantFilters` | [MerchantBasicInfo!]! | Not nullable | string IDs → MerchantBasicInfo objects. |
| `CrossDeviceAttributionModelFilters` | `filters.crossDeviceAttributionModelFilters` | [CrossDeviceAttributionModelId!]! | Not nullable | N/A |
| `SearchTrackingTagFilters` | `filters.searchTrackingTagFilters` | [SearchTrackingTag!]! | Not nullable | N/A |
| `ISpotNetworkFilters` | `filters.iSpotNetworkFilters` | [ISpotNetwork!]! | Not nullable | int → ISpotNetwork objects. |

## Code examples

### REST example

```
GET /v3/myreports/reportschedule/{scheduleId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query MyReportsReportSchedule {
  myReportsReportSchedule(id: "12345") {
    id
    name
    status
    templateId
    timezone
    frequencyType
    lookbackWindowType
    filters {
      advertiserFilters {
        id
      }
    }
    conversionPixelMappings {
      trackingTag {
        id
        name
      }
    }
  }
}
```
