# Ad format: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/adformat-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Ad format: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/adformat/query` | `Query.adFormats` | Paged collection; two new fields (`isDisplayRTBEligible`, `isOpenPathEnabled`) on concrete subtypes |
