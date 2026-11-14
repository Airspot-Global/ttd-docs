# Lift study: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/liftstudy-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Lift study: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/study/{studyId}` | `Query.conversionLiftStudy(providerId:, studyId:)` | Requires explicit `providerId`; REST infers provider from caller context |
| `POST /v3/study/query` | `Query.conversionLiftProvider(conversionLiftProviderId:).conversionLiftStudies(first:, after:)` | Paged connection; also available on `Advertiser.conversionLiftStudies` |
| `PUT /v3/study/status` | `liftStudyStatusUpdate` | Update lift study status and rejected reason |

## Shared nested types and enums

### ConversionLiftStudyStatus

| REST value | GraphQL value |
| --- | --- |
| `Pending` | `PENDING` |
| `Approved` | `APPROVED` |
| `Rejected` | `REJECTED` |
