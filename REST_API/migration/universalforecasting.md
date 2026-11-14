# Universal forecasting: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/universalforecasting-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Universal forecasting: REST → GraphQL migration guide

`forecastCreate` creates a persisted forecast entity—not REST parity for `POST /v3/universalforecasting/generate`.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| POST `/v3/universalforecasting/generate` | `forecastCreate` | Non-1:1 parity—creates a persisted forecast (`ForecastCreateInput`); REST `generate` returns ephemeral universal forecast metrics in one call. |
