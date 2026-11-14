# POST /v3/label → customLabelCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-label
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/label → customLabelCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/label` |
| GraphQL operation | `customLabelCreate` |
| Input type | `CustomLabelCreateInput` |
| Output type | `CustomLabelCreatePayload` (`data: CustomLabelREST`, `errors: [CustomLabelCreateMutationError!]`) |

## Input field mapping

Input type: `CustomLabelCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CustomLabelId` | `customLabelId` | ID | Optional | Optional; auto-generated if omitted |
| `PartnerId` | `partnerId` | ID | Optional | Defaults to user's primary partner |
| `LabelName` | `labelName` | String! | Required | Max 40 chars |

## Output field mapping

Output type: `CustomLabelREST` (returned as `data` on `CustomLabelCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CustomLabelId` | `customLabelId` | ID! | Not nullable | The created label's ID |
| `PartnerId` | `partnerId` | ID | Nullable | May be null if not specified |
| `LabelName` | `labelName` | String! | Not nullable | The label name |

## Code examples

### REST example

```
POST /v3/label HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "LabelName": "Holiday 2026",
  "PartnerId": "partner123"
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
  customLabelCreate(input: {
    labelName: "Holiday 2026"
    partnerId: "partner123"
  }) {
    data {
      customLabelId
      partnerId
      labelName
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
