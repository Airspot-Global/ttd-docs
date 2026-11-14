# PUT /v3/study/status → liftStudyStatusUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-study-status
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/study/status → liftStudyStatusUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/study/status` |
| GraphQL operation | `liftStudyStatusUpdate` |
| Input type | `LiftStudyStatusUpdateInput` |
| Output type | `LiftStudyStatusUpdatePayload` (`data: LiftStudyREST`, `errors: [LiftStudyStatusUpdateMutationError!]`) |

## Input field mapping

Input type: `LiftStudyStatusUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `StudyId` | `studyId` | ID! | Required | N/A |
| `Status` | `status` | LiftStatusRESTInput! | Required | `Pending` / `Approved` / `Rejected` → `PENDING` / `APPROVED` / `REJECTED` |
| `RejectedReason` | `rejectedReason` | String | Optional | N/A |

## Output field mapping

Output type: `LiftStudyREST` (returned as `data` on `LiftStudyStatusUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `StudyId` | `studyId` | ID! | Not nullable | N/A |
| `StudyName` | `studyName` | String! | Not nullable | N/A |
| `AdvertiserId` | `advertiserId` | ID! | Not nullable | N/A |
| `StartDate` | `startDate` | DateTime! | Not nullable | N/A |
| `EndDate` | `endDate` | DateTime! | Not nullable | N/A |
| `Status` | `status` | LiftStatusREST! | Not nullable | N/A |
| `RejectedReason` | `rejectedReason` | String | Nullable | N/A |
| `EmailAddress` | `emailAddress` | String! | Not nullable | N/A |
| `Campaigns` | `campaigns` | [String!]! | Not nullable | N/A |
| `ConversionIds` | `conversionIds` | [ID!]! | Not nullable | N/A |
| `LookbackWindow` | `lookbackWindow` | Int | Nullable | N/A |
| `TotalEstimatedImpressions` | `totalEstimatedImpressions` | Int | Nullable | N/A |
| `ReportingSlices` | `reportingSlices` | [Int!] | Nullable | N/A |

## Endpoint-specific nested types and enums

### LiftStatusRESTInput

| REST value | GraphQL value |
| --- | --- |
| `Pending` | `PENDING` |
| `Approved` | `APPROVED` |
| `Rejected` | `REJECTED` |

### LiftStatusREST

| REST value | GraphQL value |
| --- | --- |
| `Pending` | `PENDING` |
| `Approved` | `APPROVED` |
| `Rejected` | `REJECTED` |

## Code examples

### REST example

```
PUT /v3/study/status HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "StudyId": 12345,
  "Status": "Approved"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  liftStudyStatusUpdate(input: {
    studyId: "12345"
    status: APPROVED
  }) {
    data {
      studyId
      studyName
      status
      rejectedReason
    }
    errors {
      ... on RestProxyMutationError {
        message
        field
      }
    }
  }
}
```
