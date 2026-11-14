# GET /v3/study/{studyId} → Query.conversionLiftStudy

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-study-studyid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/study/{studyId} → Query.conversionLiftStudy

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/study/{studyId}` |
| GraphQL query | `Query.conversionLiftStudy(providerId:, studyId:)` |
| Return type | `ConversionLiftStudy` |

GraphQL requires an explicit `providerId` argument (numeric lift provider ID, e.g. Circana = `3`). Obtain provider IDs from `conversionLiftProviders` or `conversionLiftProvider(conversionLiftProviderId: ...)`. REST infers the lift provider from the caller's token/context.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| studyId (path) | `studyId` | ID! | Required | Path `{studyId}` → `studyId` argument (numeric literals coerce to `ID!`). |
| N/A | `providerId` | ID! | Required | No REST equivalent; provider is inferred from caller context on REST. Numeric provider ID (e.g. `3`) coerces to `ID!`. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `StudyId` | `studyId` | Long! | Not nullable | Path `{studyId}` → `studyId` argument. |
| `StudyName` | `name` | String! | Not nullable | N/A |
| `AdvertiserId` | `advertiser { id }` | ID! | Not nullable | Nested relationship replaces flat ID. |
| `StartDate` | `startDate` | DateTime! | Not nullable | UTC inclusive start. |
| `EndDate` | `endDate` | DateTime! | Not nullable | UTC inclusive end. |
| `Status` | `status` | ConversionLiftStudyStatus! | Not nullable | Enum mapped (`PENDING`/`APPROVED`/`REJECTED`). |
| `RejectedReason` | `rejectionReason` | String | Nullable | N/A |
| `EmailAddress` | `emailAddresses` | [String!]! | Not nullable | REST single string → GraphQL string array (one or more notification addresses). |
| `Campaigns` | `providerAttributes` → `campaigns { id }` | [Campaign!]! | Not nullable | Third-party studies: traverse `providerAttributes { ... on ConversionLiftStudyCircanaAttributes { campaigns { id } } }` (provider-specific union). |
| `ConversionIds` | `providerAttributes` → `itemsets` | Connection<Itemset> | Nullable | GraphQL models conversions as itemsets under provider attributes; not a flat string list. |
| `LookbackWindow` | `providerAttributes.attributionWindowInDays` (Circana) | Byte! | Not nullable | Provider-specific naming; Circana maps `LagPeriod` → `attributionWindowInDays`. |
| `TotalEstimatedImpressions` | `providerAttributes.estimatedMinimumImpressions` (Circana) | Int! | Not nullable | Provider-specific; Circana maps `EstimatedMinimumImpressions`. |
| `ReportingSlices` | `providerAttributes.reportingSlices { id }` | [ConversionLiftReportingSlice!]! | Not nullable | REST int IDs → GraphQL slice objects. |

## Endpoint-specific nested types and enums

### ConversionLiftStudyStatus

| REST value | GraphQL value |
| --- | --- |
| `Pending` | `PENDING` |
| `Approved` | `APPROVED` |
| `Rejected` | `REJECTED` |

## Code examples

### REST example

```
GET /v3/study/12345 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ConversionLiftStudyById {
  conversionLiftStudy(providerId: 3, studyId: 12345) {
    studyId
    name
    startDate
    endDate
    status
    emailAddresses
    advertiser {
      id
    }
    providerAttributes {
      ... on ConversionLiftStudyCircanaAttributes {
        estimatedMinimumImpressions
        attributionWindowInDays
        campaigns {
          id
        }
        reportingSlices {
          id
        }
      }
    }
  }
}
```
