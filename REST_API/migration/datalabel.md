# Data label: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/datalabel-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Data label: REST → GraphQL migration guide

Data labels describe metadata attached to third-party data providers and segments, such as contact information, privacy policies, audience precision, and data sourcing details. There is no standalone DataLabel entity; included GET endpoints expose labels as relationship fields on `ThirdPartyDataProvider` and `ThirdPartyData`.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/datalabels/provider/{providerId}` | `ThirdPartyDataProvider.providerDataLabels` | Nullable when labels are not defined |
| `GET /v3/datalabels/segment/{providerId}/{segmentId}` | `ThirdPartyData.segmentDataLabels` | Nullable when parent lacks `providerElementId` |
