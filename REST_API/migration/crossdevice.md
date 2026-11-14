# Cross device: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/crossdevice-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Cross device: REST → GraphQL migration guide

Both REST list endpoints attach as relationship fields on `Advertiser`.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/crossdeviceattributionmodel/query/advertiser` | `Advertiser.crossDeviceAttributionModels` | Paged attribution models for an advertiser |
| `POST /v3/crossdevicevendor/query/advertiser` | `Advertiser.crossDeviceVendors` | Paged vendors for an advertiser; includes optional `fee` on each vendor |
