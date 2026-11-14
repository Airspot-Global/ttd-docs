# DELETE /v3/crmdata/segment/{advertiserId}/{crmDataId} → crmDataSegmentArchive

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/delete-v3-crmdata-segment-advertiserid-crmdataid
- Retrieved: 2026-11-14
- Category: REST_API

---

# DELETE /v3/crmdata/segment/{advertiserId}/{crmDataId} → crmDataSegmentArchive

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `DELETE /v3/crmdata/segment/{advertiserId}/{crmDataId}` |
| GraphQL operation | `crmDataSegmentArchive` |
| Input type | `CrmDataSegmentArchiveInput` |
| Output type | `CrmDataSegmentArchivePayload` (`data: Boolean`, `errors: [CrmDataSegmentArchiveMutationError!]`) |

## Input field mapping

Input type: `CrmDataSegmentArchiveInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `advertiserId` | N/A | N/A | Required | Path parameter; GraphQL archive input uses segment ID only. Advertiser context enforced via auth. |
| `crmDataId` | `id` | String! | Required | Path parameter mapped to archive input `id` (CRM segment metadata ID) |

## Output field mapping

REST returns an empty response body on success. `CrmDataSegmentArchivePayload` returns `data: Boolean` on success and `errors` on failure. The mutation archives the segment (sets an archived flag) rather than performing a hard delete.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| N/A | `data` | Boolean | Nullable | GraphQL-only success indicator; REST success body is empty |

## Code examples

### REST example

```
DELETE /v3/crmdata/segment/abc123/crm-segment-id-456 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  crmDataSegmentArchive(input: { id: "crm-segment-id-456" }) {
    data
    errors {
      ... on UserError {
        message
        field
      }
    }
  }
}
```
