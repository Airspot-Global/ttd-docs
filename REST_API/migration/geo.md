# Geo: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/geo-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Geo: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/geosegment/query/advertiser` | `Advertiser.geoSegments` | N/A |
| `POST /v3/geosegment/query/partner` | `Partner.geoSegments` | N/A |
| `GET /v3/geosegment/{geoSegmentId}` | `Query.geoSegmentsSearch` | Filter by `where.id` |
| `GET /v3/geosegment/name/{geoSegmentId}` | `Query.geoSegmentsSearch` | Filter by `where.id`; select `id` and `name` |
| `POST /v3/geosegment/query/supplyvendor` | `Query.geoSegmentsBySupplyVendor` | N/A |
| `GET /v3/geosegment/openpath` | `Query.openPathGeoSegments` | N/A |
| `GET /v3/geosegment/googlecriteria/{googleGeoCriteriaId}` | `Query.geoSegmentByGoogleCriteria` | N/A |
| `POST /v3/geoelement/country/query` | `Query.countries` | **Remodelled in GraphQL**—`Country` shape differs from geo-element rows. |
| `POST /v3/geoelement/metro/query` | N/A | **Deprecated on REST**—use `Query.nielsenDmaGeoElements`. |
| `POST /v3/geoelement/nielsendma/query` | `Query.nielsenDmaGeoElements` | No required filter |
| `POST /v3/geoelement/region/query/country` | `Query.regions` | **Remodelled in GraphQL**—`Region` shape differs; no country-code filter. |
| `POST /v3/geoelement/city/query/region` | `Query.cityGeoElements` | Requires `regionCode` filter |
| `POST /v3/geoelement/zip/query/country` | `Query.zipGeoElements` | Requires `countryCode` filter |
| `GET /v3/geoevent/{providerId}/{geoEventId}` | `Query.geoEvent` | N/A |
| `GET /v3/geotargetsegment/{providerId}/{providerElementId}` | `Query.geoTargetSegment` | N/A |
| `POST /v3/selfservegeofence` | N/A | Not currently available in GraphQL |

## Shared nested types and enums

### GeoSegment (summary)

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoSegmentId` | `id` | ID! | Not nullable | GeoSegmentId → `id` |
| `GeoSegmentName` | `name` | String! | Not nullable | GeoSegmentName → name |
| `Description` | `description` | String | Nullable | N/A |
| `IsStandard` | `isStandard` | Boolean! | Not nullable | N/A |
| `GeoLocationType` | `type` | GeoSegmentType! | Not nullable | Enum rename GeoLocationType → GeoSegmentType |

### GeoTargetPoint

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `LngDeg` | `lngDeg` | Float! | Not nullable | N/A |
| `LatDeg` | `latDeg` | Float! | Not nullable | N/A |
| `RadMet` | `radMet` | Int! | Not nullable | N/A |

### GeoTargetPolygon

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PolygonFileNamePrefix` | `polygonFileNamePrefix` | String! | Not nullable | N/A |
| `Polygons` | `polygons` | [Polygon!]! | Not nullable | N/A |

### Polygon

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PolygonId` | `polygonId` | ID! | Not nullable | N/A |
| `Status` | `status` | String | Nullable | N/A |
| `TimeSlots` | `timeSlots` | [TimeSlot!] | Nullable | N/A |
