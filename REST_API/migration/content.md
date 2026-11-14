# Content: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/content-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Content: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/content/genre/query` | `Query.contentGenres` | Paginated connection |
| `GET /v3/content/rating/query` | `Query.contentRatings` | Paginated connection |
