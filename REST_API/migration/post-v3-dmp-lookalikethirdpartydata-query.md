# POST /v3/dmp/lookalikethirdpartydata/query → Advertiser.targetingDataSegments.edges[].lookAlikeThirdPartyData

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-dmp-lookalikethirdpartydata-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/dmp/lookalikethirdpartydata/query → Advertiser.targetingDataSegments.edges[].lookAlikeThirdPartyData

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/dmp/lookalikethirdpartydata/query` |
| GraphQL query | `TargetingDataSegmentsEdge.lookAlikeThirdPartyData` |
| Return type | `LookAlikeThirdPartyDataConnection` |

> **IMPORTANT:** The connection hangs off `targetingDataSegments` **edges**, not `nodes`: `advertiser(id:).targetingDataSegments.edges[].lookAlikeThirdPartyData`. The field is on the edge type, not on `TargetingDataSegment`.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageSize` | `first` | Int | Optional | N/A |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `FirstPartyDataId` | N/A | N/A | Optional | Remodelled in GraphQL |
| `BrandIds` | N/A | N/A | Optional | Not currently available in GraphQL |
| `CategoryIds` | N/A | N/A | Optional | Not currently available in GraphQL |
| `DataRateFilters` | N/A | N/A | Optional | Not currently available in GraphQL |
| `IncludeActiveIDsCountExpandedFlag` | N/A | N/A | Optional | REST transport only |
| `RelevanceRatioMaximum` | N/A | N/A | Optional | Not currently available in GraphQL |
| `RelevanceRatioMinimum` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SearchTerms` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UniqueCountMaximum` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UniqueCountMinimum` | N/A | N/A | Optional | Not currently available in GraphQL |
| `ValueRatioMaximum` | N/A | N/A | Optional | Not currently available in GraphQL |
| `ValueRatioMinimum` | N/A | N/A | Optional | Not currently available in GraphQL |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[LookAlikeThirdPartyData!]` | Nullable | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].FirstPartyDataId` | N/A | N/A | N/A | Remodelled in GraphQL |
| `Result[].RelevanceRatio` | `relevanceRatio` | Float! | Not nullable | N/A |
| `Result[].ValueRatio` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].ThirdPartyData` | `targetingDataSegment` | TargetingDataSegment | Nullable | REST nested object → `targetingDataSegment` on the lookalike node |
| `Result[].ThirdPartyData.ThirdPartyDataId` | `targetingDataSegment.thirdPartyDataId` | ID! | Not nullable | On `ThirdPartyTargetingDataSegment` |
| `Result[].ThirdPartyData.BrandId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].ThirdPartyData.BrandName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].ThirdPartyData.Name` | `targetingDataSegment.name` | String! | Not nullable | On `ThirdPartyTargetingDataSegment` |
| `Result[].ThirdPartyData.FullPath` | `targetingDataSegment.fullPath` | String! | Not nullable | On `ThirdPartyTargetingDataSegment` |
| `Result[].ThirdPartyData.Description` | `targetingDataSegment.description` | String | Nullable | On `ThirdPartyTargetingDataSegment` |
| `Result[].ThirdPartyData.UniqueUserCount` | `targetingDataSegment.targetingDataInsights.activeCounts.devices` | Long! | Not nullable | Deprecated REST `UniqueUserCount`; `ThirdPartyTargetingDataSegment` has no `activeUniques` |
| `Result[].ThirdPartyData.UniqueUserWebCount` | N/A | N/A | N/A | No web-specific active count on `ThirdPartyTargetingDataSegment` |
| `Result[].ThirdPartyData.CPMRate` | `dataRates.nodes[].cost.cpmCost` | MoneyModel | Nullable | REST inline rate → lookalike node `dataRates` connection. See domain guide—MoneyModel |
| `Result[].ThirdPartyData.CPMRateInAdvertiserCurrency` | `dataRates.nodes[].cost.cpmCostInAdvertiserCurrency` | MoneyModel | Nullable | REST inline advertiser-currency rate → lookalike node `dataRates` connection |
| `Result[].ThirdPartyData.PercentOfMediaCostRate` | `dataRates.nodes[].cost.percentOfMediaCost` | Decimal | Nullable | REST inline rate → lookalike node `dataRates` connection |
| `Result[].ThirdPartyData.IsPartnerDirect` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].ThirdPartyData.PersonsCount` | `targetingDataSegment.targetingDataInsights.activeCounts.persons` | Long! | Not nullable | Deprecated REST `PersonsCount` |
| `Result[].ThirdPartyData.HouseholdCount` | `targetingDataSegment.targetingDataInsights.activeCounts.households` | Long! | Not nullable | Deprecated REST `HouseholdCount` |
| `Result[].ThirdPartyData.ActiveIDsCountExpanded` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `Result[].ThirdPartyData.IsEligibleForSeeds` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].ThirdPartyData.DataEventTypeId` | `targetingDataSegment.dataEventType` | DataEventType | Nullable | REST long ID → `dataEventType` on `ThirdPartyTargetingDataSegment`. See domain guide—DataEventType |
| `Result[].ThirdPartyData.IsAudienceUnlimited` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

### LookAlikeThirdPartyData

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `FirstPartyDataId` | N/A | N/A | N/A | Remodelled in GraphQL |
| `RelevanceRatio` | `relevanceRatio` | Float! | Not nullable | N/A |
| `ValueRatio` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ThirdPartyData` | `targetingDataSegment` | TargetingDataSegment | Nullable | REST nested object → `targetingDataSegment` on the lookalike node |
| `CPMRate` | `dataRates.nodes[].cost.cpmCost` | MoneyModel | Nullable | See domain guide—MoneyModel |
| `PercentOfMediaCostRate` | `dataRates.nodes[].cost.percentOfMediaCost` | Decimal | Nullable | N/A |

### ThirdPartyTargetingDataSegment

Concrete type behind `targetingDataSegment` for lookalike results. Fields below are on `ThirdPartyTargetingDataSegment`, not the `TargetingDataSegment` interface alone.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ThirdPartyDataId` | `thirdPartyDataId` | ID! | Not nullable | N/A |
| `BrandId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BrandName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Name` | `name` | String! | Not nullable | N/A |
| `FullPath` | `fullPath` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `UniqueUserCount` | `targetingDataInsights.activeCounts.devices` | Long! | Not nullable | Deprecated REST `UniqueUserCount`; no `activeUniques` on this type |
| `UniqueUserWebCount` | N/A | N/A | N/A | No web-specific active count on this type |
| `PersonsCount` | `targetingDataInsights.activeCounts.persons` | Long! | Not nullable | Deprecated REST `PersonsCount` |
| `HouseholdCount` | `targetingDataInsights.activeCounts.households` | Long! | Not nullable | Deprecated REST `HouseholdCount` |
| `ActiveIDsCountExpanded` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `DataEventTypeId` | `dataEventType` | DataEventType | Nullable | REST long ID → `dataEventType`. See domain guide—DataEventType |
| `IsPartnerDirect` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsEligibleForSeeds` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsAudienceUnlimited` | N/A | N/A | N/A | Not currently available in GraphQL |

## Code examples

### REST example

```
POST /v3/dmp/lookalikethirdpartydata/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "FirstPartyDataId": "fpd456",
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
query LookAlikeThirdPartyData {
  advertiser(id: "adv123") {
    targetingDataSegments(
      first: 1
      where: { targetingDataId: { eq: "fpd456" } }
    ) {
      edges {
        lookAlikeThirdPartyData(first: 25) {
          nodes {
            relevanceRatio
            dataRates(first: 1) {
              nodes {
                cost {
                  cpmCost {
                    amount
                    currencyCode
                  }
                }
              }
            }
            targetingDataSegment {
              ... on ThirdPartyTargetingDataSegment {
                id
                thirdPartyDataId
                name
                fullPath
                description
                dataEventType
                targetingDataInsights {
                  activeCounts {
                    devices
                    persons
                    households
                  }
                }
              }
            }
          }
          totalCount
          pageInfo {
            hasNextPage
            endCursor
          }
        }
      }
    }
  }
}
```
