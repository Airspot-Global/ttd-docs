# POST /v3/delta/study → Query.liftStudyDelta(input: LiftStudyDeltaInput)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-delta-study
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/delta/study → Query.liftStudyDelta(input: LiftStudyDeltaInput)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/delta/study` |
| GraphQL query | `Query.liftStudyDelta(input: LiftStudyDeltaInput)` |
| Return type | `LiftStudyDelta` |

> **Note:** This is the legacy lift study delta (`liftStudyDelta`). It is distinct from `conversionLiftStudyDelta`, which covers conversion lift studies for a conversion lift provider.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `input.lastChangeId` | ID | Optional | String form of the REST tracking version. Pass null or omit for the latest change ID. |
| `ReturnEntireLiftStudy` | `input.returnEntireLiftStudy` | Boolean | Optional | If true, returns `liftStudies` objects instead of `elementIds`. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `nextChangeTrackingVersion` | Long! | Not nullable | Use the string form as `input.lastChangeId` on the next delta call. |
| `ElementIds` | `elementIds` | [ID!] | Nullable | Lift study IDs (integer values serialized as ID strings) when `returnEntireLiftStudy` is false. |
| `LiftStudies` | `liftStudies` | [LiftStudy!] | Nullable | Full lift study objects when `returnEntireLiftStudy` is true. |
| `MoreLiftStudiesAvailable` | `moreLiftStudiesAvailable` | Boolean | Nullable | True when additional lift studies exist beyond this page (only when `returnEntireLiftStudy` is true). |

## Endpoint-specific nested types and enums

### LiftStudy

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `StudyId` | `studyId` | ID! | Not nullable | Lift study identifier. |
| `StudyName` | `studyName` | String! | Not nullable | N/A |
| `AdvertiserId` | `advertiser.id` | ID! | Not nullable | REST flat ID → `advertiser` entity reference. |
| `StartDate` | `startDate` | DateTime! | Not nullable | UTC start date (read-only). |
| `EndDate` | `endDate` | DateTime! | Not nullable | UTC end date (read-only). |
| `Status` | `status` | LiftStatus! | Not nullable | Enum values: `PENDING`, `APPROVED`, `REJECTED`. |
| `RejectedReason` | `rejectedReason` | String | Nullable | N/A |
| `EmailAddress` | `emailAddress` | String! | Not nullable | N/A |
| `Campaigns` | `campaigns` | [ID!]! | Not nullable | Campaign IDs attached to the study. |
| `ConversionIds` | `conversionIds` | [ID!]! | Not nullable | Conversion tracker IDs. |
| `LookbackWindow` | `lookbackWindow` | Int | Nullable | Attribution lookback window in days. |
| `TotalEstimatedImpressions` | `totalEstimatedImpressions` | Int | Nullable | Combined estimated impressions across campaigns. |
| `ReportingSlices` | `reportingSlices` | [Int!] | Nullable | Reporting slice configuration. |

## Code examples

The following are examples of querying lift study deltas with REST and GraphQL.

Basic delta query (IDs only):

### REST example

```
POST /v3/delta/study HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "LastChangeTrackingVersion": null,
  "ReturnEntireLiftStudy": false
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query LiftStudyDelta {
  liftStudyDelta(input: {
    returnEntireLiftStudy: false
  }) {
    nextChangeTrackingVersion
    elementIds
    moreLiftStudiesAvailable
  }
}
```

Full lift study objects:

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query LiftStudyDeltaWithStudies {
  liftStudyDelta(input: {
    lastChangeId: "100"
    returnEntireLiftStudy: true
  }) {
    nextChangeTrackingVersion
    moreLiftStudiesAvailable
    liftStudies {
      studyId
      studyName
      status
      startDate
      endDate
      emailAddress
      campaigns
      conversionIds
      lookbackWindow
      totalEstimatedImpressions
      reportingSlices
      advertiser {
        id
      }
    }
  }
}
```
