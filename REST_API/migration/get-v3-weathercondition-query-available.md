# GET /v3/weathercondition/query/available → enum WeatherCondition

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-weathercondition-query-available
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/weathercondition/query/available → enum WeatherCondition

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/weathercondition/query/available` |
| GraphQL query | `enum WeatherCondition` (schema introspection) |
| Return type | `enum WeatherCondition` |

No dedicated list query is required. GraphQL exposes every supported condition as members of `enum WeatherCondition`—discover them via schema introspection (the GraphQL convention for catalogue and facet metadata endpoints). REST returns integer ID and display-name pairs; GraphQL weather targeting uses enum members directly.

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| _(catalogue list)_ | `enum WeatherCondition` (introspection) | `WeatherCondition` | Not nullable | Full catalogue—introspect `WeatherCondition` instead of calling a list query. |
| `WeatherConditionId` | N/A | N/A | N/A | **Remodelled in GraphQL**—GraphQL targeting uses enum members, not numeric IDs. |
| `ConditionName` | enum member `name` | `WeatherCondition` | Not nullable | Each catalogue entry maps to a `WeatherCondition` enum member (for example `RAIN`, `CLEAR`, `SNOW`). Member descriptions carry human-readable labels. |

## Endpoint-specific nested types and enums

### WeatherCondition (enum)

| GraphQL value | Notes |
| --- | --- |
| `ASH` | Ash conditions. |
| `CLEAR` | Clear skies. |
| `CLOUDS` | Cloudy skies. |
| `DRIZZLE` | Drizzle conditions. |
| `DUST` | Dust conditions. |
| `FOG` | Fog conditions. |
| `HAZE` | Haze conditions. |
| `MIST` | Mist conditions. |
| `RAIN` | Rainy conditions. |
| `SAND` | Sand conditions. |
| `SMOKE` | Smoke conditions. |
| `SNOW` | Snowy conditions. |
| `SQUALL` | Squall conditions. |
| `THUNDERSTORM` | Thunderstorm conditions. |
| `TORNADO` | Tornado conditions. |
| `WIND` | Windy conditions. |

Use this enum on bid-list and dimensional-bidding fields (for example `weatherCondition` on bid lines). It replaces REST `{ WeatherConditionId, ConditionName }` objects—clients enumerate allowed values from the enum definition.

## Code examples

### REST example

```
GET /v3/weathercondition/query/available HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query WeatherConditionCatalogue {
  __type(name: "WeatherCondition") {
    name
    enumValues {
      name
      description
    }
  }
}
```

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query BidListWeatherTargeting {
  bidList(id: "<bid-list-id>") {
    bidLines {
      weatherCondition
    }
  }
}
```
