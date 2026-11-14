# Weather condition: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/weathercondition-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Weather condition: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/weathercondition/query/available` | `enum WeatherCondition` | Discover allowed values via schema introspection; use enum members for weather targeting instead of REST integer IDs. |
