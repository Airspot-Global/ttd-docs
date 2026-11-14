# Interest targeting: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/interesttargeting-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Interest targeting: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/interesttargeting/query` | `Query.interestTargetingCategories` | Plain list; full dataset returned (no server-side pagination) |
