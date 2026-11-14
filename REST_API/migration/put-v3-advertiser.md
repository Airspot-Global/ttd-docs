# PUT /v3/advertiser → advertiserUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/advertiser → advertiserUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/advertiser` |
| GraphQL operation | `advertiserUpdate` |
| Input type | `AdvertiserUpdateInput` |
| Output type | `AdvertiserUpdatePayload` (`data: Advertiser`, `errors: [AdvertiserUpdateMutationError!]`) |

## Multi-step operations

`PUT /v3/advertiser` accepts inline bid lists, frequency configs, political profiles, and brands on a single REST body. `advertiserUpdate` covers core advertiser fields only—not a 1:1 mirror of the REST body.

| REST-only or non-inline behavior | GraphQL target |
| --- | --- |
| `advertiserId` | `id` (`ID!`) on `AdvertiserUpdateInput` |
| `partnerId` | Not on update input; read via `Advertiser.partnerId` |
| `currencyCode` | Create-only |
| `associatedBidLists` / `defaultBidLists` | Create-only |
| `increments` | Writable on `AdvertiserUpdateInput.increments` (`[String!]`) |
| `newFrequencyConfigs` | Create-only |
| `useLegacyAdditionalFees` | Create-only |
| `candidateProfiles`, `isBallotMeasure`, `isCandidateElection`, `isIndependentExpenditure` | Create-only |
| `brands` | Create-only |
| `customLabels[].customLabelId` | `customLabels: [String!]`—replaces the full label list by **name** |
| `advertiserCategory` / `industryCategoryId` | `advertiserCategoryInput.categoryId` when updating category |
| `advertiserAudienceSettings` | Partially covered by `dataSettings` on update input (different shape) |
| `keywords`, `logoUrl`, DSA fields | Create-only |

Inside REST `associatedBidLists` input, do not send read-only response fields: `bidListSource`, `bidListAdjustmentType`, `bidListDimensions`.

## Input field mapping

Input type: `AdvertiserUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `id` | ID! | Required | REST `AdvertiserId` → GraphQL `id` |
| `PartnerId` | N/A | N/A | Optional | Create-only |
| `AdvertiserName` | `name` | String | Optional | REST `AdvertiserName` → GraphQL `name` |
| `Description` | `description` | String | Optional | N/A |
| `CurrencyCode` | N/A | N/A | Optional | Create-only |
| `AttributionClickLookbackWindowInSeconds` | `attributionClickLookbackWindowInSeconds` | Int | Optional | N/A |
| `AttributionImpressionLookbackWindowInSeconds` | `attributionImpressionLookbackWindowInSeconds` | Int | Optional | N/A |
| `ClickDedupWindowInSeconds` | `clickDedupeWindowInSeconds` | Int | Optional | REST `ClickDedup` → GraphQL `clickDedupe` |
| `ConversionDedupWindowInSeconds` | `conversionDedupeWindowInSeconds` | Int | Optional | REST `ConversionDedup` → GraphQL `conversionDedupe` |
| `DefaultRightMediaOfferTypeId` | `defaultRightMediaOfferTypeId` | Long | Optional | N/A |
| `IndustryCategoryId` | N/A | N/A | Optional | Deprecated on REST—use `advertiserCategoryInput` |
| `AdvertiserCategory` | `advertiserCategoryInput` | AdvertiserCategoryInput | Optional | See nested table |
| `AdvertiserCategory.CategoryId` | `advertiserCategoryInput.categoryId` | Long! | Required | Required when `advertiserCategoryInput` is provided |
| `Keywords` | N/A | N/A | Optional | Create-only |
| `LogoURL` | N/A | N/A | Optional | Create-only |
| `DomainAddress` | `domainAddress` | String | Optional | N/A |
| `CustomLabels` | `customLabels` | [String!] | Optional | Replaces entire label list by name |
| `CustomLabels[].CustomLabelId` | N/A | N/A | Optional | REST label IDs do not map 1:1; supply names in `customLabels` |
| `AssociatedBidLists` | N/A | N/A | Optional | Use `advertiserAssociateBidList` |
| `DefaultBidLists` | N/A | N/A | Optional | Use `advertiserAssociateBidList` |
| `IgnoreReferralUrlInConversion` | N/A | N/A | Optional | Create-only |
| `IsBallotMeasure` | N/A | N/A | Optional | Create-only |
| `IsCandidateElection` | N/A | N/A | Optional | Create-only |
| `IsIndependentExpenditure` | N/A | N/A | Optional | Create-only |
| `CandidateProfiles` | N/A | N/A | Optional | Not inline on update; see nested table |
| `Increments` | `increments` | [String!] | Optional | Replaces complete list; pass empty array or null to remove all incrementors |
| `NewFrequencyConfigs` | N/A | N/A | Optional | Configure frequency configs separately |
| `IndustryCategoryTaxonomyId` | N/A | N/A | Optional | Read-only |
| `IndustryCategoryMapping` | N/A | N/A | Optional | Read-only |
| `AdvertiserNameDsa` | N/A | N/A | Optional | Create-only |
| `PayerNameDsa` | N/A | N/A | Optional | Create-only |
| `AdvertiserAudienceSettings` | `dataSettings` | AdvertiserDataSettingsUpdateInput | Optional | Different GraphQL shape; partial overlap only |
| `Country` | `country` | String | Optional | ISO 3166-1 alpha-2 |
| `IsHecAutoExempt` | `isHecAutoExempt` | Boolean | Optional | N/A |
| `Availability` | N/A | N/A | Optional | Create-only |
| `IsDimensionalBiddingModeSupported` | N/A | N/A | Optional | Read-only; not in input types |
| `VettingStatus` | N/A | N/A | Optional | Create-only |

### GraphQL-only input fields (no REST equivalent on `PUT /v3/advertiser`)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `audienceUnlimitedSubscription` | AdvertiserAudienceUnlimitedSubscriptionInput |  |
| `defaultAttributionSetting` | AdvertiserAttributionDefaultSettingUpdateInput |  |
| `defaultOptimizationSettings` | AdvertiserAttributionDefaultOptimizationUpdateInput |  |
| `defaultTrackingTags` | AdvertiserAttributionDefaultTrackingTagUpdateInput |  |

## Output field mapping

Output type: `Advertiser` (returned as `data` on `AdvertiserUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `partner.id` | String! | Not nullable | N/A |
| `AdvertiserId` | `id` | ID! | Not nullable | N/A |
| `AdvertiserName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `CurrencyCode` | `currency.id` | ID! | Not nullable | Nested `Currency`; `id` is ISO 4217 code |
| `AttributionClickLookbackWindowInSeconds` | `attributionClickLookbackWindowInSeconds` | Int | Nullable | Also under `attribution.clickLookbackWindow` |
| `AttributionImpressionLookbackWindowInSeconds` | `attributionImpressionLookbackWindowInSeconds` | Int | Nullable | Also under `attribution.impressionLookbackWindow` |
| `ClickDedupWindowInSeconds` | `clickDedupeWindowInSeconds` | Int! | Not nullable | N/A |
| `ConversionDedupWindowInSeconds` | `conversionDeDupeWindowInSeconds` | Int! | Not nullable | GraphQL spelling `DeDupe` |
| `DefaultRightMediaOfferTypeId` | `defaultRightMediaOfferTypeId` | Long | Nullable | N/A |
| `IndustryCategoryId` | `industryCategory.id` | ID | Nullable | Deprecated on REST |
| `AdvertiserCategory` | `industryCategory` | IndustryCategory! | Not nullable | N/A |
| `Keywords` | `keywords` | [String!]! | Not nullable | N/A |
| `Availability` | N/A | N/A | N/A | Not currently available in GraphQL |
| `LogoURL` | `logo` | String! | Not nullable | N/A |
| `DomainAddress` | `domainAddress` | String | Nullable | N/A |
| `CustomLabels` | `customLabels` | CustomLabelsConnection | Nullable | Paginated connection |
| `IsDimensionalBiddingModeSupported` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | Paginated |
| `DefaultBidLists` | `defaultBidLists` | DefaultBidListsConnection | Nullable | Paginated |
| `IgnoreReferralUrlInConversion` | `ignoreReferralUrlInConversion` | Boolean! | Not nullable | N/A |
| `IsBallotMeasure` | `political.isBallotMeasure` | Boolean! | Not nullable | N/A |
| `IsCandidateElection` | `political.isCandidateElection` | Boolean! | Not nullable | N/A |
| `IsIndependentExpenditure` | `political.isIndependentExpenditure` | Boolean! | Not nullable | N/A |
| `CandidateProfiles` | `political.candidateProfiles` | [PoliticalData!]! | Not nullable | See nested table |
| `VettingStatus` | `vettingStatus` | AdvertiserVettingStatus! | Not nullable | Read-only |
| `Increments` | `increments` | [String!]! | Not nullable | N/A |
| `NewFrequencyConfigs` | `frequencyConfigs` | FrequencyConfigsConnection | Nullable | Connection, not inline list |
| `IndustryCategoryTaxonomyId` | `industryCategory.taxonomy.id` | ID! | Not nullable | Read-only |
| `IndustryCategoryMapping` | `industryCategory.mappings` | [CategoryMapping!] | Nullable | Read-only |
| `AdvertiserNameDsa` | `nameDSA` | String | Nullable | N/A |
| `PayerNameDsa` | `payerNameDSA` | String | Nullable | N/A |
| `AdvertiserAudienceSettings` | `audienceSettings` | AdvertiserAudienceSettings! | Not nullable | N/A |
| `Country` | `country` | Country | Nullable | Object, not ISO string |
| `IsHecAutoExempt` | `isHecAutoExempt` | Boolean | Nullable | N/A |

## Endpoint-specific nested types and enums

### AdvertiserCategoryInput

Optional on `advertiserUpdate` (required `categoryId` when provided).

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserCategory.CategoryId` | `categoryId` | Long! | Required | Only writable field |

### CandidateProfile—REST input (no GraphQL inline equivalent)

REST `CandidateProfiles[]` is writable on `PUT /v3/advertiser` but is **not** accepted on `AdvertiserUpdateInput`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PoliticalDataId` | N/A | N/A | Optional | Maps to `political.candidateProfiles[].id` on read |
| `CandidateName` | N/A | N/A | N/A | Create-only |
| `ElectionState` | N/A | N/A | Optional | Create-only |
| `PayingEntityName` | N/A | N/A | N/A | Create-only |
| `PayingEntityAddress` | N/A | N/A | N/A | Create-only |
| `PayingEntityEmailAddress` | N/A | N/A | Optional | Create-only |
| `PayingEntityExecutiveName` | N/A | N/A | N/A | Create-only |
| `PayingEntityExecutiveTitle` | N/A | N/A | N/A | Create-only |
| `GeoDescription` | N/A | N/A | Optional | Create-only |
| `AudienceDescription` | N/A | N/A | Optional | Create-only |
| `DisclaimerNotice` | N/A | N/A | Optional | Create-only |
| `IsAdvertiserIEC` | N/A | N/A | Optional | Create-only |
| `FileLocationInS3` | N/A | N/A | Optional | Create-only |
| `FederalVerificationId` | N/A | N/A | Optional | Create-only |
| `StateVerificationId` | N/A | N/A | Optional | Create-only |
| `OtherStateElectionId` | N/A | N/A | Optional | Create-only |

### CandidateProfile—REST response on `Advertiser`

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PoliticalDataId` | `political.candidateProfiles[].id` | ID! | Not nullable | N/A |
| `CandidateName` | `political.candidateProfiles[].candidateName` | String! | Not nullable | N/A |
| `ElectionState` | `political.candidateProfiles[].electionStateName` | String | Nullable | REST enum → GraphQL state name |
| `PayingEntityName` | `political.candidateProfiles[].payingEntityName` | String! | Not nullable | N/A |
| `PayingEntityAddress` | `political.candidateProfiles[].payingEntityAddress` | String! | Not nullable | N/A |
| `PayingEntityExecutiveName` | `political.candidateProfiles[].payingEntityExecutiveName` | String! | Not nullable | N/A |
| `PayingEntityExecutiveTitle` | `political.candidateProfiles[].payingEntityExecutiveTitle` | String! | Not nullable | N/A |
| `FederalVerificationId` | `political.candidateProfiles[].verificationFormId` | String | Nullable | When `verificationFormIdType` is federal |
| `StateVerificationId` | `political.candidateProfiles[].verificationFormId` | String | Nullable | When `verificationFormIdType` is state/EIN |
| `PayingEntityEmailAddress` | N/A | N/A | N/A | Not exposed on `PoliticalData` |
| `GeoDescription` | N/A | N/A | N/A | Not exposed on `PoliticalData` |
| `AudienceDescription` | N/A | N/A | N/A | Not exposed on `PoliticalData` |
| `DisclaimerNotice` | N/A | N/A | N/A | Not exposed on `PoliticalData` |
| `IsAdvertiserIEC` | N/A | N/A | N/A | Use `political.isIndependentExpenditure` at advertiser level |
| `FileLocationInS3` | N/A | N/A | N/A | Not exposed on `PoliticalData` |
| `OtherStateElectionId` | N/A | N/A | N/A | Not exposed on `PoliticalData` |

### Brand—REST input (no GraphQL inline equivalent)

REST `Brands[]` is writable on `PUT /v3/advertiser` but is **not** accepted on `AdvertiserUpdateInput`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BrandOwner` | N/A | N/A | N/A | Create-only |
| `BrandName` | N/A | N/A | N/A | Create-only |

### Brand—REST response on `Advertiser`

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BrandOwner` | `assignedBrands[].owner` | String! | Not nullable | Also surfaced as `brandOwner` on advertiser |
| `BrandName` | `assignedBrands[].name` | String! | Not nullable | N/A |
| N/A | `assignedBrands[].id` | ID! | Not nullable | GraphQL-only brand identifier |

## Code examples

### REST example

```
PUT /v3/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv-999",
  "AdvertiserName": "Updated Advertiser",
  "DomainAddress": "https://updated-example.com"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation UpdateAdvertiser($input: AdvertiserUpdateInput!) {
  advertiserUpdate(input: $input) {
    data {
      id
      name
      domainAddress
    }
    errors {
      ... on AdvertiserValidationError {
        message
        field
      }
    }
  }
}
```

Variables:

```
{
  "input": {
    "id": "adv-999",
    "name": "Updated Advertiser",
    "domainAddress": "https://updated-example.com"
  }
}
```

REST-inline fields such as `associatedBidLists`, `candidateProfiles`, and `brands` are not inputs on `AdvertiserUpdateInput`. Use `advertiserAssociateBidList` and other dedicated mutations when REST parity is required.
