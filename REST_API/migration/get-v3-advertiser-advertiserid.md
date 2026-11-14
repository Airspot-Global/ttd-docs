# GET /v3/advertiser/{advertiserId} → Query.advertiser(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-advertiser-advertiserid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/advertiser/{advertiserId} → Query.advertiser(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/advertiser/{advertiserId}` |
| GraphQL query | `Query.advertiser(id:)` |
| Return type | `Advertiser` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `partner.id` | String! | Not nullable | N/A |
| `AdvertiserId` | `id` | ID! | Not nullable | N/A |
| `AdvertiserName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `CurrencyCode` | `currency` | Currency! | Not nullable | External enum maps to Currency object; use `currency.id` for ISO 4217 code. |
| `AttributionClickLookbackWindowInSeconds` | `attributionClickLookbackWindowInSeconds` | Int | Nullable | N/A |
| `AttributionImpressionLookbackWindowInSeconds` | `attributionImpressionLookbackWindowInSeconds` | Int | Nullable | N/A |
| `ClickDedupWindowInSeconds` | `clickDedupeWindowInSeconds` | Int! | Not nullable | N/A |
| `ConversionDedupWindowInSeconds` | `conversionDeDupeWindowInSeconds` | Int! | Not nullable | N/A |
| `DefaultRightMediaOfferTypeId` | `defaultRightMediaOfferTypeId` | Long | Nullable | N/A |
| `IndustryCategoryId` | `industryCategory.id` | ID | Nullable | Scalar ID via nested `industryCategory` object. |
| `AdvertiserCategory` | `industryCategory` | IndustryCategory! | Not nullable | N/A |
| `AdvertiserCategory.CategoryId` | `industryCategory.id` | ID | Nullable | N/A |
| `AdvertiserCategory.CategoryName` | `industryCategory.name` | String! | Not nullable | N/A |
| `AdvertiserCategory.CategoryTaxonomyId` | `industryCategory.taxonomy.id` | ID! | Not nullable | Via nested `taxonomy` on `IndustryCategory`. |
| `AdvertiserCategory.CategoryTaxonomyName` | `industryCategory.taxonomy.name` | String! | Not nullable | N/A |
| `AdvertiserCategory.CategoryTaxonomyVersion` | `industryCategory.taxonomy.version` | String! | Not nullable | N/A |
| `AdvertiserCategory.Mappings` | `industryCategory.mappings` | [CategoryMapping!] | Nullable | N/A |
| `AdvertiserCategory.Mappings.CategoryTaxonomyId` | `industryCategory.mappings.taxonomyId` | Int! | Not nullable | N/A |
| `AdvertiserCategory.Mappings.CategoryId` | `industryCategory.mappings.categoryId` | Int! | Not nullable | N/A |
| `AdvertiserCategory.Mappings.ExternalId` | `industryCategory.mappings.externalId` | String! | Not nullable | N/A |
| `Keywords` | `keywords` | [String!]! | Not nullable | N/A |
| `Availability` | `isArchived` | Boolean! | Not nullable | REST Availability enum maps inversely to `isArchived` (Available=false, Archived=true). |
| `LogoURL` | `logoUrl` | String | Nullable | N/A |
| `DomainAddress` | `domainAddress` | String | Nullable | N/A |
| `CustomLabels` | `customLabels` | CustomLabelsConnection | Nullable | Paginated connection; use `nodes` for a flat list. |
| `CustomLabels[].CustomLabelId` | `customLabels { nodes { id } }` | ID! | Not nullable | N/A |
| `IsDimensionalBiddingModeSupported` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | See AssociatedBidList on the Advertiser domain page. |
| `AssociatedBidLists[].BidListId` | `associatedBidLists { nodes { bidList { id } } }` | ID! | Not nullable | See AssociatedBidList on the Advertiser domain page. |
| `AssociatedBidLists[].IsEnabled` | `associatedBidLists { nodes { isEnabled } }` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists[].BidListSource` | `associatedBidLists { nodes { bidList { source } } }` | BidListSource! | Not nullable | N/A |
| `AssociatedBidLists[].BidListAdjustmentType` | `associatedBidLists { nodes { bidList { adjustmentType } } }` | BidListAdjustmentType! | Not nullable | N/A |
| `AssociatedBidLists[].BidListDimensions` | `associatedBidLists { nodes { bidList { dimensions } } }` | [BidListDimension!]! | Not nullable | N/A |
| `DefaultBidLists` | `defaultBidLists` | DefaultBidListsConnection | Nullable | Paginated connection; nodes are `IBidList`. |
| `DefaultBidLists[].BidListId` | `defaultBidLists { nodes { id } }` | ID! | Not nullable | N/A |
| `IgnoreReferralUrlInConversion` | `ignoreReferralUrlInConversion` | Boolean! | Not nullable | N/A |
| `IsBallotMeasure` | `political.isBallotMeasure` | Boolean! | Not nullable | Political fields live on nested `political` object. |
| `IsCandidateElection` | `political.isCandidateElection` | Boolean! | Not nullable | N/A |
| `IsIndependentExpenditure` | `political.isIndependentExpenditure` | Boolean! | Not nullable | N/A |
| `CandidateProfiles` | `political.candidateProfiles` | [PoliticalData!]! | Not nullable | N/A |
| `CandidateProfiles[].PoliticalDataId` | `political.candidateProfiles { id }` | ID! | Not nullable | N/A |
| `CandidateProfiles[].CandidateName` | `political.candidateProfiles { candidateName }` | String! | Not nullable | N/A |
| `CandidateProfiles[].ElectionState` | `political.candidateProfiles { electionStateName }` | String | Nullable | REST election state maps to `electionStateName`. |
| `CandidateProfiles[].PayingEntityName` | `political.candidateProfiles { payingEntityName }` | String! | Not nullable | N/A |
| `CandidateProfiles[].PayingEntityAddress` | `political.candidateProfiles { payingEntityAddress }` | String! | Not nullable | N/A |
| `CandidateProfiles[].PayingEntityEmailAddress` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CandidateProfiles[].PayingEntityExecutiveName` | `political.candidateProfiles { payingEntityExecutiveName }` | String! | Not nullable | N/A |
| `CandidateProfiles[].PayingEntityExecutiveTitle` | `political.candidateProfiles { payingEntityExecutiveTitle }` | String! | Not nullable | N/A |
| `CandidateProfiles[].GeoDescription` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CandidateProfiles[].AudienceDescription` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CandidateProfiles[].DisclaimerNotice` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CandidateProfiles[].IsAdvertiserIEC` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CandidateProfiles[].FileLocationInS3` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CandidateProfiles[].FederalVerificationId` | `political.candidateProfiles { verificationFormId }` | String | Nullable | Paired with `verificationFormIdType`. |
| `CandidateProfiles[].StateVerificationId` | `political.candidateProfiles { verificationFormId }` | String | Nullable | Paired with `verificationFormIdType`. |
| `CandidateProfiles[].OtherStateElectionId` | `political.candidateProfiles { verificationFormIdType }` | String | Nullable | REST other-state ID maps to verification form metadata. |
| `VettingStatus` | `vettingStatus` | AdvertiserVettingStatus! | Not nullable | N/A |
| `Increments` | `increments` | [String!]! | Not nullable | N/A |
| `NewFrequencyConfigs` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Brands[].BrandOwner` | `assignedBrands { owner }` | String! | Not nullable | N/A |
| `Brands[].BrandName` | `assignedBrands { name }` | String! | Not nullable | N/A |
| (Brand ID) | `assignedBrands { id }` | ID! | Not nullable | GraphQL-only identifier for the brand. |
| `IndustryCategoryTaxonomyId` | `industryCategory` | IndustryCategory | Nullable | Deprecated on REST |
| `IndustryCategoryMapping` | `industryCategory` | IndustryCategory | Nullable | Deprecated on REST |
| `IndustryCategoryMapping.CategoryTaxonomyId` | `industryCategory` | IndustryCategory | Nullable | Deprecated on REST |
| `IndustryCategoryMapping.CategoryId` | `industryCategory` | IndustryCategory | Nullable | Deprecated on REST |
| `IndustryCategoryMapping.ExternalId` | `industryCategory` | IndustryCategory | Nullable | Deprecated on REST |
| `AdvertiserNameDsa` | `nameDsa` | String | Nullable | N/A |
| `PayerNameDsa` | `payerNameDsa` | String | Nullable | N/A |
| `AdvertiserAudienceSettings` | `audienceSettings` | AdvertiserAudienceSettings! | Not nullable | N/A |
| `AdvertiserAudienceSettings.AudienceBoosterEnabled` | `audienceSettings.isAudienceBoosterEnabled` | Boolean! | Not nullable | N/A |
| `AdvertiserAudienceSettings.AudienceExcluderEnabled` | `audienceSettings.isAudienceExcluderEnabled` | Boolean! | Not nullable | N/A |
| `Country` | `country` | Country | Nullable | REST ISO 3166-1 alpha-2 string maps to nested `Country` object. |
| `Country` (ISO 3166-1 alpha-2) | `country.shortName` | String! | Not nullable | Null when `country` is absent. |
| `IsHecAutoExempt` | `isHecAutoExempt` | Boolean | Nullable | N/A |

## Endpoint-specific nested types and enums

### PoliticalData

Candidate profiles are exposed on `Advertiser.political.candidateProfiles` as `PoliticalData` objects.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PoliticalDataId` | `id` | ID! | Not nullable | N/A |
| `CandidateName` | `candidateName` | String! | Not nullable | N/A |
| `ElectionState` | `electionStateName` | String | Nullable | REST election state maps to `electionStateName`. |
| `PayingEntityName` | `payingEntityName` | String! | Not nullable | N/A |
| `PayingEntityAddress` | `payingEntityAddress` | String! | Not nullable | N/A |
| `PayingEntityEmailAddress` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PayingEntityExecutiveName` | `payingEntityExecutiveName` | String! | Not nullable | N/A |
| `PayingEntityExecutiveTitle` | `payingEntityExecutiveTitle` | String! | Not nullable | N/A |
| `GeoDescription` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AudienceDescription` | N/A | N/A | N/A | Not currently available in GraphQL |
| `DisclaimerNotice` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsAdvertiserIEC` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FileLocationInS3` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FederalVerificationId` | `verificationFormId` | String | Nullable | Paired with `verificationFormIdType`. |
| `StateVerificationId` | `verificationFormId` | String | Nullable | Paired with `verificationFormIdType`. |
| `OtherStateElectionId` | `verificationFormIdType` | String | Nullable | Verification form metadata. |

### Brand

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| (Brand ID) | `id` | ID! | Not nullable | GraphQL-only identifier. |
| `BrandOwner` | `owner` | String! | Not nullable | N/A |
| `BrandName` | `name` | String! | Not nullable | N/A |

### Country

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| (ISO 3166-1 alpha-2) | `shortName` | String! | Not nullable | REST `Country` string maps here; also available as `id`. |
| (country name) | `longName` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/advertiser/{advertiserId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetAdvertiser {
  advertiser(id: "abc123") {
    id
    name
    attributionClickLookbackWindowInSeconds
    attributionImpressionLookbackWindowInSeconds
    defaultRightMediaOfferTypeId
    logoUrl
    increments
    nameDsa
    payerNameDsa
  }
}
```
