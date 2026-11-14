# POST /v3/thirdpartydata/query → ThirdPartyDataProvider.thirdPartyDataTaxonomies

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-thirdpartydata-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/thirdpartydata/query → ThirdPartyDataProvider.thirdPartyDataTaxonomies

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/thirdpartydata/query` |
| GraphQL query | `ThirdPartyDataProvider.thirdPartyDataTaxonomies` |
| Return type | `ThirdPartyDataTaxonomiesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageSize` | `first` | Int | Optional | N/A |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `IncludeActiveIDsCountExpandedFlag` | `filter.includeActiveIdsCountExpanded` | Boolean | Optional | N/A |
| `IncludeAudienceExpansionFlag` | `filter.includeAudienceExpansion` | Boolean | Optional | N/A |
| `ProviderElementId` | `filter.providerElementId` | String | Optional | N/A |
| `ProviderId` | `ThirdPartyDataProvider(id:)` | N/A | Required | Parent lookup—not a connection argument |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[ThirdPartyData!]` | Nullable | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].ThirdPartyDataId` | `id` | ID! | Not nullable | N/A |
| `Result[].ProviderId` | `thirdPartyDataProvider.id` | ID! | Not nullable | Provider ID is the parent entity key |
| `Result[].ProviderElementId` | `providerElementId` | ID! | Not nullable | N/A |
| `Result[].DisplayName` | `name` | String! | Not nullable | REST `DisplayName` → GraphQL `name` |
| `Result[].ParentElementId` | `parentElementId` | String | Nullable | N/A |
| `Result[].ActiveIDsCount` | `activeIdsCount` | Long | Nullable | N/A |
| `Result[].Buyable` | `buyable` | Boolean! | Not nullable | N/A |
| `Result[].Description` | `description` | String | Nullable | N/A |
| `Result[].AudienceSize` | N/A | N/A | N/A | Deprecated on REST |
| `Result[].AudienceExpansion` | `audienceExpansion` | SegmentAudienceExpansion | Nullable | See domain guide—SegmentAudienceExpansion |
| `Result[].ReceivedIDsCount` | `receivedIdsCount` | Long | Nullable | N/A |
| `Result[].LastUpdatedAtUTC` | `lastUpdatedAtUtc` | DateTime | Nullable | N/A |
| `Result[].ActiveIDsCountExpanded` | `activeIdsCountExpanded` | Boolean | Nullable | N/A |
| `Result[].TaxonomyComplianceStatus` | `thirdPartyDataTaxonomyApprovalStatus` | ThirdPartyDataTaxonomyApprovalStatus | Nullable | REST taxonomy compliance status → GraphQL taxonomy approval status enum |
| `Result[].IsDirectIPTargeting` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].SubProviderId` | `thirdPartyDataSubProvider.id` | ID! | Not nullable | Parent `thirdPartyDataSubProvider` nullable; absent when the segment has no sub-provider. When present, `id` is not nullable. |

## Endpoint-specific nested types and enums

### ThirdPartyData

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ThirdPartyDataId` | `id` | ID! | Not nullable | N/A |
| `ProviderId` | `thirdPartyDataProvider.id` | ID! | Not nullable | Provider ID is the parent entity key |
| `ProviderElementId` | `providerElementId` | ID! | Not nullable | N/A |
| `DisplayName` | `name` | String! | Not nullable | REST `DisplayName` → GraphQL `name` |
| `ParentElementId` | `parentElementId` | String | Nullable | N/A |
| `ActiveIDsCount` | `activeIdsCount` | Long | Nullable | N/A |
| `Buyable` | `buyable` | Boolean! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `AudienceSize` | N/A | N/A | N/A | Deprecated on REST |
| `AudienceExpansion` | `audienceExpansion` | SegmentAudienceExpansion | Nullable | See domain guide—SegmentAudienceExpansion |
| `ReceivedIDsCount` | `receivedIdsCount` | Long | Nullable | N/A |
| `LastUpdatedAtUTC` | `lastUpdatedAtUtc` | DateTime | Nullable | N/A |
| `ActiveIDsCountExpanded` | `activeIdsCountExpanded` | Boolean | Nullable | N/A |
| `TaxonomyComplianceStatus` | `thirdPartyDataTaxonomyApprovalStatus` | ThirdPartyDataTaxonomyApprovalStatus | Nullable | REST taxonomy compliance status → GraphQL taxonomy approval status enum |
| `IsDirectIPTargeting` | N/A | N/A | N/A | Not currently available in GraphQL |
| `SubProviderId` | `thirdPartyDataSubProvider.id` | ID! | Not nullable | Parent `thirdPartyDataSubProvider` nullable; absent when the segment has no sub-provider. When present, `id` is not nullable. |

### SegmentDataLabels

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `audienceExpansion` | Boolean | Nullable | N/A |
| `audiencePrecisionLevel` | AudiencePrecisionLevel | Nullable | N/A |
| `audienceRefreshCadence` | DataLabelTimeFrequency | Nullable | N/A |
| `categoryId` | Int | Nullable | N/A |
| `crossDeviceExpansion` | Boolean | Nullable | N/A |
| `dataInclusionMethodology` | DataInclusionMethodology | Nullable | N/A |
| `dataSources` | `[DataLabelDataSource!]` | Nullable | N/A |
| `geo` | String | Nullable | N/A |
| `inputIdMatchKeys` | `[DataLabelInputIdMatchKey!]` | Nullable | N/A |
| `providerUniqueIdCount` | Int | Nullable | N/A |
| `providerUniqueIdType` | ProviderUniqueIdType | Nullable | N/A |
| `sourceLookbackWindow` | DataLabelTimeFrequency | Nullable | N/A |

### ThirdPartyDataTaxonomyApprovalStatus

| GraphQL value | Notes |
| --- | --- |
| `APPROVED` | N/A |
| `DENIED` | N/A |
| `NOT_IN_QUEUE` | N/A |
| `PENDING` | N/A |

## Code examples

### REST example

```
POST /v3/thirdpartydata/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "ProviderId": "prov123",
  "PageStartIndex": 0,
  "PageSize": 100,
  "ProviderElementId": "elem456"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ProviderTaxonomies {
  thirdPartyDataProvider(id: "prov123") {
    thirdPartyDataTaxonomies(
      first: 100
      filter: { providerElementId: "elem456" }
    ) {
      nodes {
        id
        providerElementId
        name
        buyable
        thirdPartyDataTaxonomyApprovalStatus
      }
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
