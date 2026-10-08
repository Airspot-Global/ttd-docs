# Forecasting API Guide

- Source: https://partner.thetradedesk.com/v3/portal/api/area/Universal%20Forecasting
- Category: Guides

---

# Forecasting in The Trade Desk

Forecasting allows platform users to predict the performance, spend, and reach of a campaign or ad group before it launches. By analyzing historical inventory data (typically the last 30 days) and current market conditions, the platform provides estimates to help optimize targeting and budget allocation.

The Trade Desk currently provides two primary ways to generate forecasts:
1. **Universal Forecasting (REST)**: The modern REST-based approach.
2. **GraphQL Forecasting (`forecastCreate`)**: The recommended approach for modern, performant integrations.

---

## 1. Universal Forecasting (REST)

The Universal Forecasting API is a standalone service that generates forecasts based on the data available at the time of the request.

### Endpoint
`POST /v3/universalforecasting/generate`

### Key Request Parameters
| Field | Type | Description |
| :--- | :--- | :--- |
| `AdvertiserId` | String | (Required) The ID of the advertiser for whom the forecast is generated. |
| `StartDate` | DateTime | The starting date for the forecast period. |
| `EndDate` | DateTime | The ending date for the forecast period. |
| `Budget` | Double | The total budget to be tested. If omitted, the API returns a baseline "Market Capacity" level. |
| `Targeting` | Object | A set of targeting parameters including Geo, Audience, Inventory, and Bid Lists. |

### Detailed Targeting & Budget Fields
To get an accurate forecast, you should include the following core parameters:

- **Max Bid CPM**: Located under `RTBAttributes.MaxBidCPM`. Defines the maximum price you are willing to pay for impressions.
- **Demographics**: Located under `DemographicTargeting.AgeRangeTargeting.AgeRanges` and `DemographicTargeting.GenderTargeting.Genders`.
- **Geography**: Located under `GeographyTargeting.LocationTargeting.Locations`. Requires `LocationId` values from the TTD Geography taxonomy.
- **Device Type**: Located under `DeviceTargeting.DeviceTypes` (e.g., "PC", "Mobile", "ConnectedTV").

### Request Example
```json
{
  "AdvertiserId": "adv-123",
  "StartDate": "2024-05-01T00:00:00Z",
  "EndDate": "2024-05-07T23:59:59Z",
  "RTBAttributes": {
    "MaxBidCPM": {
      "Amount": 5.0,
      "CurrencyCode": "USD"
    }
  },
  "Targeting": {
    "BidListIds": ["bl-456", "bl-789"],
    "DemographicTargeting": {
      "AgeRangeTargeting": { "AgeRanges": ["18-24", "25-34"] },
      "GenderTargeting": { "Genders": ["Male", "Female"] }
    },
    "GeographyTargeting": {
      "LocationTargeting": {
        "Locations": [ { "LocationId": 12345 }, { "LocationId": 67890 } ]
      }
    }
  }
}
```

---

## 2. GraphQL Forecasting (`forecastCreate`)

The GraphQL API is the recommended way to perform forecasting, as it integrates seamlessly with modern Kokai features and provides more granular control.

### Mutation
`mutation forecastCreate($input: ForecastCreateInput!)`

### Example GraphQL Mutation Variable
```json
{
  "input": {
    "advertiserId": "adv-123",
    "budget": { "amount": 1000, "currencyCode": "USD" },
    "targeting": {
      "demographicTargeting": {
        "ageRangeTargeting": { "ageRanges": ["AGE_25_TO_34", "AGE_35_TO_44"] },
        "genderTargeting": { "genders": ["MALE", "FEMALE"] }
      },
      "geographyTargeting": {
        "locationTargeting": { "locationIds": [123, 456] }
      },
      "rtbAttributes": {
        "maxBidCPM": { "amount": 5.0, "currencyCode": "USD" }
      }
    }
  }
}
```

### Benefits of GraphQL
- **Kokai Compatibility**: Native support for the latest platform features.
- **Selective Data Retrieval**: Fetch only the metrics you need (e.g., only `decisionPower` or `projectedSpend`).
- **Improved Performance**: Reduced payload size and faster response times compared to legacy REST endpoints.

---

## 3. Core Forecasting Metrics

When you receive a forecast response, pay attention to these critical KPIs:

### **Decision Power (0 - 100)**
Estimates the platform's flexibility to find relevant impressions and pace delivery effectively. 
- **High (80-100)**: Excellent delivery prospects.
- **Medium (50-79)**: Stable, but might require optimization if budget is high.
- **Low (0-49)**: High risk of under-delivery; consider widening targeting or increasing bid caps.

### **Relevance**
Indicates how well the available inventory matches your "Ideal Customer Profile" based on your Seed or Audience configuration.

### **Projected Spend and Reach**
- **ProjectedSpend**: Estimated maximum spend for the period.
- **ProjectedTotalImpressions**: Estimated total volume of available impressions.

---

## 4. Best Practices & Rules

> [!TIP]
> **Use Shorter Timeframes**: For maximum accuracy, run forecasts for a 7-day period. This reduces the risk of market volatility affecting the predictions.

> [!IMPORTANT]
> **Include Bid Lists**: Always include your Bid List IDs in the request. Forecasting accuracy depends heavily on the specific bidding logic and dimension adjustments defined in your bid lists.

### Rate Limits
Forecasting is a resource-intensive operation.
- Implement **Client-Side Caching**: Avoid re-requesting the same forecast within 24 hours unless the campaign configuration has changed significantly.
- **Avoid Real-Time Polling**: Do not trigger forecasts automatically on every UI change; use a "Calculate Forecast" button or debounce input changes.

---

## 5. Related Resources
- [REST API: Universal Forecasting (Ref)](../REST_API/universal_forecasting.md)
- [GraphQL: Forecast Creation Example](../GraphQL/forecasting_gql_examples.md)
