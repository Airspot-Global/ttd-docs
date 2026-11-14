# POST /v3/advertiser → advertiserCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/advertiser → advertiserCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/advertiser` |
| GraphQL operation | `advertiserCreate` |
| Input type | `AdvertiserCreateInput` |
| Output type | `AdvertiserCreatePayload` (`data: Advertiser`, `errors: [AdvertiserCreateMutationError!]`) |

## Multi-step operations

`POST /v3/advertiser` accepts a wide REST body with inline bid lists, frequency configs, political profiles, and brands. `advertiserCreate` covers core advertiser provisioning only—not a 1:1 mirror of the REST body.

| REST-only or non-inline behavior | GraphQL target |
| --- | --- |
| `associatedBidLists` / `defaultBidLists` | Create-only |
| `increments` | Writable on `AdvertiserCreateInput.increments` (`[String!]`) |
| `newFrequencyConfigs` | Create-only |
| `useLegacyAdditionalFees` | Create-only |
| `candidateProfiles`, `isBallotMeasure`, `isCandidateElection`, `isIndependentExpenditure` | Create-only |
| `brands` | Create-only |
| `customLabels[].customLabelId` | `customLabels: [String!]`—GraphQL accepts label **names**, not IDs |
| `advertiserCategory` / `industryCategoryId` | `advertiserCategoryInput.categoryId` (required on GraphQL create) |
| `currencyCode` | Not currently available in GraphQL |
| `keywords`, `logoUrl`, DSA fields, `advertiserAudienceSettings` | Create-only |
| `partnerId` | Create-only |

Inside REST `associatedBidLists` input, do not send read-only response fields: `bidListSource`, `bidListAdjustmentType`, `bidListDimensions`.

## Input field mapping

Input type: `AdvertiserCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `partnerId` | ID! | Required | Required on create |
| `AdvertiserId` | N/A | N/A | Optional | Read-only |
| `AdvertiserName` | `name` | String! | Required | REST `AdvertiserName` → GraphQL `name` |
| `Description` | `description` | String | Optional | N/A |
| `CurrencyCode` | N/A | N/A | Optional | Create-only; inherits partner currency |
| `AttributionClickLookbackWindowInSeconds` | `attributionClickLookbackWindowInSeconds` | Int! | Required | Required on GraphQL create |
| `AttributionImpressionLookbackWindowInSeconds` | `attributionImpressionLookbackWindowInSeconds` | Int! | Required | Required on GraphQL create |
| `ClickDedupWindowInSeconds` | `clickDedupeWindowInSeconds` | Int! | Required | REST `ClickDedup` → GraphQL `clickDedupe` |
| `ConversionDedupWindowInSeconds` | `conversionDedupeWindowInSeconds` | Int! | Required | REST `ConversionDedup` → GraphQL `conversionDedupe` |
| `DefaultRightMediaOfferTypeId` | `defaultRightMediaOfferTypeId` | Long! | Required | Required on GraphQL create |
| `IndustryCategoryId` | N/A | N/A | Optional | Deprecated on REST; use `advertiserCategoryInput` |
| `AdvertiserCategory` | `advertiserCategoryInput` | AdvertiserCategoryInput! | Required | Required on GraphQL create; see nested table |
| `AdvertiserCategory.CategoryId` | `advertiserCategoryInput.categoryId` | Long! | Required | Only writable category field |
| `Keywords` | N/A | N/A | Optional | Create-only |
| `LogoURL` | N/A | N/A | Optional | Create-only |
| `DomainAddress` | `domainAddress` | String! | Required | Required on GraphQL create |
| `CustomLabels` | `customLabels` | [String!] | Optional | GraphQL accepts label names, not nested ID objects |
| `CustomLabels[].CustomLabelId` | N/A | N/A | Optional | REST label IDs do not map 1:1; supply names in `customLabels` |
| `AssociatedBidLists` | N/A | N/A | Optional | Use `advertiserAssociateBidList` after create |
| `DefaultBidLists` | N/A | N/A | Optional | Use `advertiserAssociateBidList` after create |
| `IgnoreReferralUrlInConversion` | N/A | N/A | Optional | Create-only |
| `IsBallotMeasure` | N/A | N/A | Optional | Create-only |
| `IsCandidateElection` | N/A | N/A | Optional | Create-only |
| `IsIndependentExpenditure` | N/A | N/A | Optional | Create-only |
| `CandidateProfiles` | N/A | N/A | Optional | Not inline on create; see nested table |
| `Increments` | `increments` | [String!] | Optional | Frequency counter IDs this advertiser increments |
| `NewFrequencyConfigs` | N/A | N/A | Optional | Configure frequency configs separately |
| `IndustryCategoryTaxonomyId` | N/A | N/A | Optional | Read-only |
| `IndustryCategoryMapping` | N/A | N/A | Optional | Read-only |
| `AdvertiserNameDsa` | N/A | N/A | Optional | Create-only |
| `PayerNameDsa` | N/A | N/A | Optional | Create-only |
| `AdvertiserAudienceSettings` | N/A | N/A | Optional | Create-only |
| `Country` | `country` | String! | Required | ISO 3166-1 alpha-2; required on GraphQL create |
| `IsHecAutoExempt` | `isHecAutoExempt` | Boolean | Optional | N/A |
| `Availability` | N/A | N/A | Optional | Read-only |
| `IsDimensionalBiddingModeSupported` | N/A | N/A | Optional | Read-only; not in input types |
| `VettingStatus` | N/A | N/A | Optional | Read-only |

## Output field mapping

Output type: `Advertiser` (returned as `data` on `AdvertiserCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `partner.id` | String! | Not nullable | N/A |
| `AdvertiserId` | `id` | ID! | Not nullable | REST `AdvertiserId` → GraphQL `id` |
| `AdvertiserName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `CurrencyCode` | `currency.id` | ID! | Not nullable | Nested `Currency`; `id` is ISO 4217 code |
| `AttributionClickLookbackWindowInSeconds` | `attributionClickLookbackWindowInSeconds` | Int | Nullable | Also available under `attribution.clickLookbackWindow` |
| `AttributionImpressionLookbackWindowInSeconds` | `attributionImpressionLookbackWindowInSeconds` | Int | Nullable | Also available under `attribution.impressionLookbackWindow` |
| `ClickDedupWindowInSeconds` | `clickDedupeWindowInSeconds` | Int! | Not nullable | N/A |
| `ConversionDedupWindowInSeconds` | `conversionDeDupeWindowInSeconds` | Int! | Not nullable | GraphQL spelling `DeDupe` |
| `DefaultRightMediaOfferTypeId` | `defaultRightMediaOfferTypeId` | Long | Nullable | N/A |
| `IndustryCategoryId` | `industryCategory.id` | ID | Nullable | Deprecated on REST |
| `AdvertiserCategory` | `industryCategory` | IndustryCategory! | Not nullable | Industry category object |
| `Keywords` | `keywords` | [String!]! | Not nullable | N/A |
| `Availability` | N/A | N/A | N/A | Not currently available in GraphQL |
| `LogoURL` | `logo` | String! | Not nullable | REST `LogoURL` → GraphQL `logo` |
| `DomainAddress` | `domainAddress` | String | Nullable | N/A |
| `CustomLabels` | `customLabels` | CustomLabelsConnection | Nullable | Paginated connection, not flat ID list |
| `IsDimensionalBiddingModeSupported` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | Paginated; not returned inline from create payload unless selected |
| `DefaultBidLists` | `defaultBidLists` | DefaultBidListsConnection | Nullable | Paginated |
| `IgnoreReferralUrlInConversion` | `ignoreReferralUrlInConversion` | Boolean! | Not nullable | N/A |
| `IsBallotMeasure` | `political.isBallotMeasure` | Boolean! | Not nullable | Nested under `political` |
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

Required on `advertiserCreate`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserCategory.CategoryId` | `categoryId` | Long! | Required | Only writable field on category input |

### CandidateProfile—REST input (no GraphQL inline equivalent)

REST `CandidateProfiles[]` is writable on `POST /v3/advertiser` but is **not** accepted on `AdvertiserCreateInput`. Configure political candidate data outside this mutation.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PoliticalDataId` | N/A | N/A | Optional | Server-assigned; maps to `political.candidateProfiles[].id` on read |
| `CandidateName` | N/A | N/A | N/A | Create-only |
| `ElectionState` | N/A | N/A | Optional | Create-only |
| `PayingEntityName` | N/A | N/A | N/A | Create-only |
| `PayingEntityAddress` | N/A | N/A | N/A | Create-only |
| `PayingEntityEmailAddress` | N/A | N/A | Optional | Create-only |
| `PayingEntityExecutiveName` | N/A | N/A | N/A | Create-only |
| `PayingEntityExecutiveTitle` | N/A | N/A | N/A | Create-only |
| `GeoDescription` | N/A | N/A | Optional | Maryland state/local only on REST |
| `AudienceDescription` | N/A | N/A | Optional | Maryland state/local only on REST |
| `DisclaimerNotice` | N/A | N/A | Optional | Create-only |
| `IsAdvertiserIEC` | N/A | N/A | Optional | New York political only on REST |
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

REST `Brands[]` is writable on `POST /v3/advertiser` but is **not** accepted on `AdvertiserCreateInput`.

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
POST /v3/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "prt-123",
  "AdvertiserName": "Manual Test Advertiser",
  "DomainAddress": "https://example.com",
  "Country": "US",
  "AttributionClickLookbackWindowInSeconds": 864000,
  "AttributionImpressionLookbackWindowInSeconds": 86400,
  "ClickDedupWindowInSeconds": 0,
  "ConversionDedupWindowInSeconds": 0,
  "DefaultRightMediaOfferTypeId": 3,
  "AdvertiserCategory": { "CategoryId": 123 }
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation CreateAdvertiser($input: AdvertiserCreateInput!) {
  advertiserCreate(input: $input) {
    data {
      id
      name
      domainAddress
      partner { id }
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
    "partnerId": "prt-123",
    "name": "Manual Test Advertiser",
    "domainAddress": "https://example.com",
    "country": "US",
    "attributionClickLookbackWindowInSeconds": 864000,
    "attributionImpressionLookbackWindowInSeconds": 86400,
    "clickDedupeWindowInSeconds": 0,
    "conversionDedupeWindowInSeconds": 0,
    "defaultRightMediaOfferTypeId": 3,
    "advertiserCategoryInput": {
      "categoryId": 123
    }
  }
}
```

REST-inline fields such as `associatedBidLists`, `candidateProfiles`, and `brands` are not inputs on `AdvertiserCreateInput`. Use `advertiserAssociateBidList` and other dedicated mutations after create when REST parity is required.
