# GET /v3/adgroup/analyticsreport/{adGroupId} → AdGroup.analyticsReport

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-adgroup-analyticsreport-adgroupid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/adgroup/analyticsreport/{adGroupId} → AdGroup.analyticsReport

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/adgroup/analyticsreport/{adGroupId}` |
| GraphQL query | `AdGroup.analyticsReport` |
| Return type | `AdGroupAnalyticsReport` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Not nullable | Entity key on `AdGroup`; supplied via `Query.adGroup(id:)`. |
| `ComscoreEnabled` | `analyticsReport.comscoreEnabled` | Boolean! | Not nullable | N/A |
| `NielsenEnabled` | `analyticsReport.nielsenEnabled` | Boolean! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.GrossImpressions` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.grossImpressions` | Long! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.PCImpressions` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.pcImpressions` | Long! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.GRP` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.grp` | Decimal! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.TRP` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.trp` | Decimal! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.PercentPopulationReach` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.percentPopulationReach` | Decimal! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.PercentInTargetImpressions` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.percentInTargetImpressions` | Decimal! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.InGeoPCImpressions` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.inGeoPCImpressions` | Long! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.InGeoPCUniqueViewers` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.inGeoPCUniqueViewers` | Long! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.InTargetImpressions` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.inTargetImpressions` | Long! | Not nullable | N/A |
| `ComscoreAnalyticsReport.KeyMetricsMeasurements.InGeoPCAverageFrequency` | `analyticsReport.comscoreAnalyticsReport.keyMetrics.inGeoPCAverageFrequency` | Decimal! | Not nullable | N/A |
| `ComscoreAnalyticsReport.DemographicMemberMeasurements` | `analyticsReport.comscoreAnalyticsReport.demographicMemberMeasurements` | [ComscoreDemographicMemberMeasurement!] | Nullable | See nested table. |
| `ComscoreAnalyticsReport.LocalMarketMeasurements` | `analyticsReport.comscoreAnalyticsReport.localMarketMeasurements` | [ComscoreLocalMarketMeasurement!] | Nullable | See nested table. |
| `ComscoreAnalyticsReport.GeoMarketMeasurements` | `analyticsReport.comscoreAnalyticsReport.geoMarketMeasurements` | [ComscoreGeoMarketMeasurement!] | Nullable | See nested table. |
| `NielsenAnalyticsReport.NetGrpScore` | `analyticsReport.nielsenAnalyticsReport.netGrpScore` | Decimal! | Not nullable | N/A |
| `NielsenAnalyticsReport.NetOnTargetPrecent` | `analyticsReport.nielsenAnalyticsReport.netOnTargetPercent` | Decimal! | Not nullable | REST field name is misspelled `NetOnTargetPrecent`; GraphQL exposes `netOnTargetPercent`. |
| `NielsenAnalyticsReport.GeoMeasurements` | `analyticsReport.nielsenAnalyticsReport.geoMeasurements` | [NielsenGeoMeasurement!] | Nullable | See nested table. |
| `NielsenAnalyticsReport.CountryDemographicMeasurements` | `analyticsReport.nielsenAnalyticsReport.countryDemographicMeasurements` | [NielsenCountryDemographicMeasurement!] | Nullable | See nested table. |
| `MiaozhenAnalyticsReport.NetOnTargetPrecent` | `analyticsReport.miaozhenAnalyticsReport.netOnTargetPercent` | Decimal! | Not nullable | REST field name is misspelled `NetOnTargetPrecent`; GraphQL exposes `netOnTargetPercent`. |
| `MiaozhenAnalyticsReport.DemoReports` | `analyticsReport.miaozhenAnalyticsReport.demoReports` | [MiaozhenDemoReport!] | Nullable | See nested table. |
| `MiaozhenAnalyticsReport.GeoReports` | `analyticsReport.miaozhenAnalyticsReport.geoReports` | [MiaozhenGeoReport!] | Nullable | See nested table. |

## Endpoint-specific nested types and enums

### ComscoreDemographicMemberMeasurement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DemographicMemberId` | `demographicMemberId` | Int | Nullable | N/A |
| `DemographicMemberName` | `demographicMemberName` | String | Nullable | N/A |
| `UniqueViewers` | `uniqueViewers` | Long! | Not nullable | N/A |
| `PercentUniqueViewers` | `percentUniqueViewers` | Decimal! | Not nullable | N/A |
| `CompositionIndexUniqueViewers` | `compositionIndexUniqueViewers` | Decimal! | Not nullable | N/A |
| `PercentPopulationReach` | `percentPopulationReach` | Decimal! | Not nullable | N/A |
| `TotalImpressions` | `totalImpressions` | Decimal! | Not nullable | N/A |
| `PercentImpressions` | `percentImpressions` | Decimal! | Not nullable | N/A |
| `AverageFrequency` | `averageFrequency` | Decimal! | Not nullable | N/A |
| `GRP` | `grp` | Decimal! | Not nullable | N/A |

### ComscoreLocalMarketMeasurement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Name` | `name` | String | Nullable | N/A |
| `PercentImpressions` | `percentImpressions` | Decimal! | Not nullable | N/A |

### ComscoreGeoMarketMeasurement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Name` | `name` | String | Nullable | N/A |
| `TotalImpressions` | `totalImpressions` | Long! | Not nullable | N/A |
| `PercentImpressions` | `percentImpressions` | Decimal! | Not nullable | N/A |

### NielsenGeoMeasurement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Name` | `name` | String | Nullable | N/A |
| `ImpressionCount` | `impressionCount` | Long! | Not nullable | N/A |
| `GrossRatingPoint` | `grossRatingPoint` | Decimal! | Not nullable | N/A |
| `CostPerPoint` | `costPerPoint` | Decimal! | Not nullable | N/A |

### NielsenCountryDemographicMeasurement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CountryName` | `countryName` | String | Nullable | N/A |
| `DemographicMeasurements` | `demographicMeasurements` | [NielsenDemographicMeasurement!] | Nullable | See nested table. |

### NielsenDemographicMeasurement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Name` | `name` | String | Nullable | N/A |
| `GrossRatingPoint` | `grossRatingPoint` | Decimal! | Not nullable | N/A |
| `CostPerPoint` | `costPerPoint` | Decimal! | Not nullable | N/A |
| `OnTargetPercent` | `onTargetPercent` | Decimal! | Not nullable | N/A |

### MiaozhenDemoReport

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DemographicName` | `demographicName` | String | Nullable | N/A |
| `PlatformId` | `platformId` | String | Nullable | N/A |
| `TotalImpressions` | `totalImpressions` | Long! | Not nullable | N/A |
| `UniqueImpressions` | `uniqueImpressions` | Long! | Not nullable | N/A |
| `TotalClicks` | `totalClicks` | Long! | Not nullable | N/A |
| `UniqueClicks` | `uniqueClicks` | Long! | Not nullable | N/A |
| `OnTargetPercent` | `onTargetPercent` | Decimal! | Not nullable | N/A |
| `ReportDate` | `reportDate` | DateTime! | Not nullable | N/A |
| `MiaozhenDemographicTypeId` | `miaozhenDemographicTypeId` | MiaozhenDemographicType! | Not nullable | See enum table. |

### MiaozhenDemographicType (enum)

| REST value | GraphQL value | Notes |
| --- | --- | --- |
| `Gender` | `GENDER` | N/A |
| `Age` | `AGE` | N/A |
| `GenderAndAge` | `GENDER_AND_AGE` | N/A |
| `Education` | `EDUCATION` | N/A |
| `PersonalIncome` | `PERSONAL_INCOME` | N/A |
| `HouseholdIncome` | `HOUSEHOLD_INCOME` | N/A |
| `HouseholdIncomePerPerson` | `HOUSEHOLD_INCOME_PER_PERSON` | N/A |

### MiaozhenGeoReport

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Region` | `region` | String | Nullable | N/A |
| `PlatformId` | `platformId` | String | Nullable | N/A |
| `TotalImpressions` | `totalImpressions` | Long! | Not nullable | N/A |
| `UniqueImpressions` | `uniqueImpressions` | Long! | Not nullable | N/A |
| `TotalClicks` | `totalClicks` | Long! | Not nullable | N/A |
| `UniqueClicks` | `uniqueClicks` | Long! | Not nullable | N/A |
| `ReportDate` | `reportDate` | DateTime! | Not nullable | N/A |
| `ParentRegionId` | `parentRegionId` | String | Nullable | N/A |
| `CityLevelReports` | `cityLevelReports` | [MiaozhenGeoReport!] | Nullable | Self-referential—each element is another `MiaozhenGeoReport`; recurse with the same field set. |

## Code examples

### REST example

```
GET /v3/adgroup/analyticsreport/{adGroupId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdGroupAnalyticsReport($id: ID!) {
  adGroup(id: $id) {
    analyticsReport {
      comscoreEnabled
      nielsenEnabled
      comscoreAnalyticsReport {
        keyMetrics { grossImpressions grp trp }
        demographicMemberMeasurements { demographicMemberName uniqueViewers grp }
      }
      nielsenAnalyticsReport {
        netGrpScore
        netOnTargetPercent
        geoMeasurements { name impressionCount }
      }
      miaozhenAnalyticsReport {
        netOnTargetPercent
        demoReports { demographicName totalImpressions onTargetPercent }
      }
    }
  }
}
```
