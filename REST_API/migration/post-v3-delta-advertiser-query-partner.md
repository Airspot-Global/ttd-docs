# POST /v3/delta/advertiser/query/partner → Query.advertiserDelta

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-delta-advertiser-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/delta/advertiser/query/partner → Query.advertiserDelta

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/delta/advertiser/query/partner` |
| GraphQL query | `Query.advertiserDelta` |
| Return type | `AdvertiserDelta` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `input.changeTrackingVersion` | Long! | Optional | REST optional long? defaults when omitted; GraphQL requires non-null Long |
| `PartnerId` | `input.ids` | [ID!] | Optional | REST single optional/required ID → GraphQL IDs list (wrap single value in array) REST PartnerId maps to one element in PartnerDeltaInput.ids. |
| `ReturnEntireAdvertiser` | N/A | N/A | Optional | GraphQL delta always returns full entity objects; no IDs-only mode. |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `pageSize` | Int | GraphQL-only pagination control; REST delta has implicit paging via More*Available without explicit page size on most endpoints. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `currentMinimumTrackingVersion` | Long! | Not nullable | REST single version → GraphQL splits into `currentMinimumTrackingVersion` and `nextChangeTrackingVersion` |
| `LastChangeTrackingVersion` | `nextChangeTrackingVersion` | Long! | Not nullable | GraphQL-only companion field for pagination cursor No direct REST counterpart; use for subsequent delta calls (replaces REST LastChangeTrackingVersion on next request). |
| `ElementIds` | N/A | N/A | N/A | GraphQL always returns full entity objects; derive IDs from entity ID fields in the returned list. |
| `Advertisers` | `advertisers` | [Advertiser!]! | Not nullable | REST Advertisers → GraphQL advertisers (`Advertiser` entities) |
| `MoreAdvertisersAvailable` | `moreAvailable` | Boolean! | Not nullable | N/A |
| `Advertisers[].PartnerId` | `partnerId` | String! | Not nullable | N/A |
| `Advertisers[].AdvertiserId` | `id` | ID! | Not nullable | AdvertiserId → `id` |
| `Advertisers[].AdvertiserName` | `name` | String! | Not nullable | AdvertiserName → name |
| `Advertisers[].Description` | `description` | String | Nullable | N/A |
| `Advertisers[].CurrencyCode` | `currency.id` | ID! | Not nullable | N/A |
| `Advertisers[].AttributionClickLookbackWindowInSeconds` | `attributionClickLookbackWindowInSeconds` | Int | Nullable | N/A |
| `Advertisers[].AttributionImpressionLookbackWindowInSeconds` | `attributionImpressionLookbackWindowInSeconds` | Int | Nullable | N/A |
| `Advertisers[].ClickDedupWindowInSeconds` | `clickDedupeWindowInSeconds` | Int! | Not nullable | N/A |
| `Advertisers[].ConversionDedupWindowInSeconds` | `conversionDeDupeWindowInSeconds` | Int! | Not nullable | N/A |
| `Advertisers[].DefaultRightMediaOfferTypeId` | `defaultRightMediaOfferTypeId` | Long | Nullable | N/A |
| `Advertisers[].IndustryCategoryId` | `industryCategory.id` | ID | Nullable | IndustryCategoryId → `industryCategory`.id |
| `Advertisers[].AdvertiserCategory` | `industryCategory` | IndustryCategory! | Not nullable | N/A |
| `Advertisers[].AdvertiserCategory.CategoryId` | `industryCategory.id` | ID | Nullable | N/A |
| `Advertisers[].AdvertiserCategory.CategoryName` | `industryCategory.name` | String! | Not nullable | N/A |
| `Advertisers[].AdvertiserCategory.CategoryTaxonomyId` | `industryCategory.taxonomy.id` | ID! | Not nullable | N/A |
| `Advertisers[].AdvertiserCategory.CategoryTaxonomyName` | `industryCategory.taxonomy.name` | String! | Not nullable | N/A |
| `Advertisers[].AdvertiserCategory.CategoryTaxonomyVersion` | `industryCategory.taxonomy.version` | String! | Not nullable | N/A |
| `Advertisers[].Keywords` | `keywords` | [String!]! | Not nullable | N/A |
| `Advertisers[].Availability` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].LogoURL` | `logo` | String! | Not nullable | N/A |
| `Advertisers[].DomainAddress` | `domainAddress` | String | Nullable | N/A |
| `Advertisers[].CustomLabels` | `customLabels.nodes` | CustomLabelsConnection | Nullable | N/A |
| `Advertisers[].CustomLabels[].CustomLabelId` | `customLabels.nodes.id` | ID! | Not nullable | CustomLabelId → `id` via connection nodes. |
| `Advertisers[].AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | N/A |
| `Advertisers[].AssociatedBidLists[].BidListId` | `bidList.id` | ID! | Not nullable | BidListId → `bidList`.id |
| `Advertisers[].AssociatedBidLists[].IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |
| `Advertisers[].AssociatedBidLists[].IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].AssociatedBidLists[].BidListSource` | `bidList.source` | BidListSource! | Not nullable | N/A |
| `Advertisers[].AssociatedBidLists[].BidListAdjustmentType` | `bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `Advertisers[].AssociatedBidLists[].BidListDimensions` | `bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |
| `Advertisers[].DefaultBidLists` | `defaultBidLists` | DefaultBidListsConnection | Nullable | Connection; nodes are IBidList. |
| `Advertisers[].DefaultBidLists[].BidListId` | `defaultBidLists.nodes.id` | ID! | Not nullable | BidListId → nodes.id |
| `Advertisers[].IgnoreReferralUrlInConversion` | `ignoreReferralUrlInConversion` | Boolean! | Not nullable | N/A |
| `Advertisers[].IsBallotMeasure` | `political.isBallotMeasure` | Boolean! | Not nullable | N/A |
| `Advertisers[].IsCandidateElection` | `political.isCandidateElection` | Boolean! | Not nullable | N/A |
| `Advertisers[].IsIndependentExpenditure` | `political.isIndependentExpenditure` | Boolean! | Not nullable | N/A |
| `Advertisers[].CandidateProfiles` | `political.candidateProfiles` | [PoliticalData!]! | Not nullable | N/A |
| `Advertisers[].CandidateProfiles[].PoliticalDataId` | `political.candidateProfiles.id` | ID! | Not nullable | PoliticalDataId → `id` |
| `Advertisers[].CandidateProfiles[].CandidateName` | `political.candidateProfiles.candidateName` | String! | Not nullable | N/A |
| `Advertisers[].CandidateProfiles[].ElectionState` | `political.candidateProfiles.electionStateName` | String | Nullable | N/A |
| `Advertisers[].CandidateProfiles[].PayingEntityName` | `political.candidateProfiles.payingEntityName` | String! | Not nullable | N/A |
| `Advertisers[].CandidateProfiles[].PayingEntityAddress` | `political.candidateProfiles.payingEntityAddress` | String! | Not nullable | N/A |
| `Advertisers[].CandidateProfiles[].PayingEntityEmailAddress` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].CandidateProfiles[].PayingEntityExecutiveName` | `political.candidateProfiles.payingEntityExecutiveName` | String! | Not nullable | N/A |
| `Advertisers[].CandidateProfiles[].PayingEntityExecutiveTitle` | `political.candidateProfiles.payingEntityExecutiveTitle` | String! | Not nullable | N/A |
| `Advertisers[].CandidateProfiles[].GeoDescription` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].CandidateProfiles[].AudienceDescription` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].CandidateProfiles[].DisclaimerNotice` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].CandidateProfiles[].IsAdvertiserIEC` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].CandidateProfiles[].FileLocationInS3` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].CandidateProfiles[].FederalVerificationId` | `political.candidateProfiles.verificationFormId` | String | Nullable | When `verificationFormIdType` is federal. |
| `Advertisers[].CandidateProfiles[].StateVerificationId` | `political.candidateProfiles.verificationFormId` | String | Nullable | When `verificationFormIdType` is state. |
| `Advertisers[].CandidateProfiles[].OtherStateElectionId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].VettingStatus` | `vettingStatus` | AdvertiserVettingStatus! | Not nullable | N/A |
| `Advertisers[].Increments` | `increments` | [String!]! | Not nullable | N/A |
| `Advertisers[].NewFrequencyConfigs` | `frequencyConfigs` | FrequencyConfigsConnection | Nullable | REST returns configs inline on delta payload; GraphQL exposes as `frequencyConfigs` connection on `Advertiser`. |
| `Advertisers[].NewFrequencyConfigs[].CounterId` | `frequencyConfigs.nodes.counter.id` | ID! | Not nullable | CounterId → `id`. |
| `Advertisers[].NewFrequencyConfigs[].OwnedByPartner` | `frequencyConfigs.nodes.counter.owner` | FrequencyCounterOwner | Nullable | REST `true` when owner resolves to `Partner`; `false` when owner is `Advertiser`. |
| `Advertisers[].NewFrequencyConfigs[].CounterName` | `frequencyConfigs.nodes.counter.name` | String! | Not nullable | CounterName → name. |
| `Advertisers[].NewFrequencyConfigs[].ResetIntervalInMinutes` | `frequencyConfigs.nodes.counter.resetIntervalInMinutes` | Int! | Not nullable | N/A |
| `Advertisers[].NewFrequencyConfigs[].FrequencyCap` | `frequencyConfigs.nodes.bidLists.bidLines.frequencyAdjustment.timesShown.max` | Int | Nullable | Cap bid line: `adjustmentType` is `TargetList` and `volumeControlPriority` is `NEUTRAL`; value is `timesShown.max`. |
| `Advertisers[].NewFrequencyConfigs[].FrequencyGoal` | `frequencyConfigs.nodes.bidLists.bidLines.frequencyAdjustment.timesShown.max` | Int | Nullable | Goal bid line: `volumeControlPriority` is `FREQUENCY_GOAL`; value is `timesShown.max`. |
| `Advertisers[].NewFrequencyConfigs[].CounterAttribute` | `frequencyConfigs.nodes.counter.counterAttribute` | FrequencyCounterSpecialType! | Not nullable | N/A |
| `Advertisers[].Brands[].BrandOwner` | `assignedBrands.owner` | String! | Not nullable | BrandOwner → owner |
| `Advertisers[].Brands[].BrandName` | `assignedBrands.name` | String! | Not nullable | BrandName → name |
| `Advertisers[].IndustryCategoryTaxonomyId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].IndustryCategoryMapping` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].IndustryCategoryMapping.CategoryTaxonomyId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].IndustryCategoryMapping.CategoryId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].IndustryCategoryMapping.ExternalId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Advertisers[].AdvertiserNameDsa` | `nameDsa` | String | Nullable | AdvertiserNameDsa → `nameDsa` |
| `Advertisers[].PayerNameDsa` | `payerNameDsa` | String | Nullable | N/A |
| `Advertisers[].AdvertiserAudienceSettings` | `audienceSettings` | AdvertiserAudienceSettings! | Not nullable | N/A |
| `Advertisers[].AdvertiserAudienceSettings.AudienceBoosterEnabled` | `audienceSettings.isAudienceBoosterEnabled` | Boolean! | Not nullable | N/A |
| `Advertisers[].AdvertiserAudienceSettings.AudienceExcluderEnabled` | `audienceSettings.isAudienceExcluderEnabled` | Boolean! | Not nullable | N/A |
| `Advertisers[].Country` | `country` | Country | Nullable | N/A |
| `Advertisers[].IsHecAutoExempt` | `isHecAutoExempt` | Boolean | Nullable | N/A |
| `Advertisers[].IsDimensionalBiddingModeSupported` | N/A | N/A | N/A | Not currently available in GraphQL |

## Code examples

### REST example

```
POST /v3/delta/advertiser/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "LastChangeTrackingVersion": null,
  "PartnerId": "example-id",
  "ReturnEntireAdvertiser": false
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserDeltaByPartner {
  advertiserDelta(input: {
    changeTrackingVersion: 0
    ids: ["partner789"]
    pageSize: 100
  }) {
    currentMinimumTrackingVersion
    nextChangeTrackingVersion
    moreAvailable
    advertisers {
      id
      name
    }
  }
}
```
