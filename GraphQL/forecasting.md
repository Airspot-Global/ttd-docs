# Forecasting

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/Forecasting
- Retrieved: 2026-11-14
- Category: GraphQL

---

# Forecasting

During pre-flight or when you are planning your campaign strategy, you can use forecasting to plan scalable campaigns that align with your business objectives. Forecasts help you understand how much you can expect to spend with different strategies, and they also provide useful metrics like Decision Power, which summarizes your flexibility for decisioned buying and pacing capability, and Relevance, which tells you how likely you are to reach people who match your seed.

Here's what you need to know about forecasting:

- You can use forecasting to predict estimated spend and delivery under different configurations such as budget, inventory, reach, and so on. This enables you to make more informed decisions when setting up your campaigns and ad groups.
- Forecasting uses seven days of historical data to estimate potential spend.
- Market conditions, supply, demand, and seasonal shifts can cause differences between forecasted and actual spend.

## Forecasting key metrics

The output of a forecast includes multiple metrics that describe expected scale, efficiency, and quality for an ad group. After you create a forecast, these metrics return in the `data.adGroupLevelForecastResults` object of the response.

While the forecast response contains many values, the following table focuses on three key metrics used to evaluate targeting quality and spend potential.

| Metric | What it measures |
| --- | --- |
| `decisionPower` | A forward-looking score from 0–100 that estimates how much flexibility the platform has to find relevant impressions and pace delivery. For details, see Decision Power. |
| `relevance` | This metric scores how well available impressions match your ideal customer profile across multiple dimensions. Relevance is calculated based on your seed. |
| `maxPotentialSpend` | The estimated maximum amount the campaign could spend under the forecasted configuration. **NOTE**: This metric is calculated based on whether you provide a budget. If you provide a budget, projected spend equals the provided budget. If no budget is provided, the `valuesAtInputBudget` object returns forecast metrics calculated at the spend level where `decisionPower` equals 80. |

## Creating and managing forecasts

Here's what you need to know about creating and managing forecasts:

- After you generate a forecast, you can update its settings and include more dimensions and targeting criteria without having to create a new one.
- If needed, you can add more dimensions to a forecast by assigning more bid lists to it. This also enables you to test and see how well the bid list will perform under your configurations before assigning it to an ad group.

The following table lists the tasks for creating and managing forecasts.

| Task | Operation | Notes |
| --- | --- | --- |
| Create a forecast. | `forecastCreate` mutation | To retrieve the results of the forecast right away, include the `adGroupLevelForecastResults` field. |
| Retrieve the details or status of a forecast. | `forecast` query | To check the status of a forecast being generated, include its ID and the `status` field. |
| Retrieve a list of forecasts associated with an advertiser. | `forecastsForAdvertiser` query | You can use this query to view and compare the results of multiple forecasts at once. |
| Update a forecast. | `forecastSettingsUpdate` mutation | - Be sure to include all of the required fields such as `forecastId`, `roiGoal`, `marketType`, and so on. - To add more dimensions or bid lists to a forecast, use the `forecastAssociateBidList` mutation. |
| Clone a forecast. | `forecastClone` mutation | None. |
| Update and clone a forecast at the same time. | `forecastCreateFrom` mutation | Use this mutation when you want to update the existing forecast while also cloning and creating a copy of it at the same time. |
| Associate or remove a bid list from an existing forecast. | `forecastAssociateBidList` mutation | This is how you add or remove dimensions from a forecast. |
| Archive a forecast. | `forecastArchive` mutation | You cannot restore an archived forecast, however, you can retrieve a list of archived forecasts. |

### Create a forecast

To create a forecast, use the `forecastCreate` mutation and include the required fields such as your advertiser ID, the forecast duration, and, in the `data` field, the metrics you want to use to predict your potential outcomes.

To create the most accurate and actionable results for a forecast, consider also providing the following:

- To improve forecast precision, use shorter timeframes. For example, specify one week instead of three months to reduce variability.
- To accurately model bidding behavior, include the IDs of all Bid lists that contain dimensions relevant to your targeting strategy.
- To reflect the correct audience scale and quality, provide the ID of the audience you intend to target.
- To receive forecast results immediately, include the `adGroupLevelForecastResults` field in your request.

Here’s an example `forecastCreate` mutation that creates a forecast of a video ad group. It estimates potential spend, reach, and impressions over a nine-day period based on the specified audience, budget, and targeting configurations. The forecasting results are returned in the `adGroupLevelForecastResults` field.

```
mutation {
  forecastCreate(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      name: "FORECAST_NAME_PLACEHOLDER"
      adGroupForecastSettings: {
        audienceId: "AUDIENCE_ID_EXAMPLE"
        channel: VIDEO
        cpm: { amount: 15, currencyCode: USD }
        forecastDurationInDays: 9
        isPolitical: false
        marketType: OPEN_MARKET
        qualityAllianceViewabilityProfile: 0
        reachType: HOUSEHOLD
        roiGoal: REACH
        seed: { id: "SEED_ID_PLACEHOLDER" }
        targetAllKnowUsers: true
        adFormatDurationIds: [{ id: 1 }]
        adFormatFileTypeIds: [{ id: 1 }]
        adGroupFunnelLocationType: CONSIDERATION
        budgetInAdvertiserCurrency: 5000
        bidLists: [
          {
            bidListId: "BID_LIST_ID_PLACEHOLDER"
            isDefault: true
            isEnabled: true
          }
        ]
      }
    }
  ) {
    data {
      id
      isArchived
      isAsync
      lastUpdatedByUser
      name
      status
      adGroupLevelForecastResults {
        availsNumber
        durationInDays
        lastCalculatedAt
        maxPotentialSpend
        spend
        curves {
          averageCpm
          averageFrequency
          budget
          decisionPower
          householdReach
          impressions
          personsReach
          relevance
        }
        valuesAtInputBudget {
          householdReach
          impressions
          personsReach
          decisionPower
          averageFrequency
          relevance
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

After you create the forecast, its ID is returned as an integer and the forecast results appear in the `data.adGroupLevelForecastResults` object.

### Retrieve a forecast

To retrieve a forecast and check its status or view its results, use the `forecast` query and include the ID of the forecast you want to retrieve. Here's an example query that retrieves the name, status, and results of a single forecast by its ID.

```
query GetForecastExample {
  forecast(id: FORECAST_ID_PLACEHOLDER) {
    id
    name
    status
    adGroupLevelForecastResults {
      durationInDays
      lastCalculatedAt
      maxPotentialSpend
    }
  }
}
```

### Retrieve a list of forecasts

To retrieve a list of forecasts including their IDs, statuses, and results, use the `forecastsForAdvertiser` query and include your advertiser ID. You can use this operation when you want to view the statuses and results of multiple forecasts at once for comparison.

> **TIP**: To retrieve a list of archived forecasts, set the `filter.isArchived` value to `true`.

Here’s an example `forecastsForAdvertiser` query that retrieves the name, status, and results of multiple forecasts owned by an advertiser.

```
query GetForecastListExample {
  forecastsForAdvertiser(
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    paging: { first: 20 }
  ) {
    nodes {
      id
      name
      status
      adGroupLevelForecastResults {
        curves {
          averageCpm
          averageFrequency
          budget
          decisionPower
          householdReach
          impressions
          personsReach
          relevance
        }
      }
    }
  }
}
```

### Update a forecast

To update a forecast with different configurations to evaluate, use the `forecastSettingsUpdate` mutation and include the ID of the forecast, each required field and each setting you want to update.

> **NOTE**: You cannot use this mutation to add more bid lists or dimensions to the forecast. For details on how to add more bid lists to a forecast, see Associate a bid list to a forecast.

Here's an example that updates the channel of an existing forecast to `DISPLAY`. It contains all required fields including the setting to update.

```
mutation {
  forecastSettingsUpdate(
    input: {
      forecastId: FORECAST_ID_PLACEHOLDER
      updatedForecastSettings: {
        roiGoal: REACH
        marketType: OPEN_MARKET
        channel: DISPLAY
        adGroupFunnelLocationType: AWARENESS
        reachType: PERSON
        cpm: { amount: 19, currencyCode: USD }
      }
    }
  ) {
    data {
      forecastId
      forecast {
        adGroupForecastSettings {
          roiGoal
          marketType
          channel
          adGroupFunnelLocationType
          reachType
          cpm {
            amount
            currency {
              id
              isVisible
            }
          }
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Clone a forecast

If you want to create different variations of a forecast with minimal updates, you can clone an existing forecast. To clone a forecast, use the `forecastClone` mutation and include the ID of the forecast you want to clone. Here's an example that clones a forecast and returns the ID, name, and information of the new forecast copy.

```
mutation {
  forecastClone(input: { advertiserId: "ADVERTISER_ID_PLACEHOLDER", forecastId: FORECAST_ID_PLACEHOLDER }) {
    data {
      id
      name
      isArchived
      adGroupLevelForecastResults {
        maxPotentialSpend
        spend
      }
    }
  }
}
```

### Update and clone a forecast

To update the details of a forecast while cloning and creating a copy of it, use the `forecastCreateFrom` mutation and include the ID of the forecast you want to update and clone. Here's an example that updates the channel of an existing forecast and creates a copy of it.

```
mutation {
  forecastCreateFrom(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      forecastId: FORECAST_ID_PLACEHOLDER
      updatedForecastSettings: { channel: DISPLAY }
    }
  ) {
    data {
      id
      name
      status
      adGroupLevelForecastResults {
        maxPotentialSpend
        spend
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Associate a bid list to a forecast

To add more bid lists and dimensions to a forecast, use the `forecastAssociateBidList` mutation and include the IDs of the bid lists you want to add to or remove from a forecast. Here's what you need to know:

- To add bid lists, include the `bidListsToAddOrUpdate` input field.
- To remove bid lists, include the `bidListIdsToRemove` input field.

Here’s a `forecastAssociateBidList` mutation example that adds and enables one bid list, sets it as the default, and removes two others.

```
mutation {
  forecastAssociateBidList(
    input: {
      forecastId: FORECAST_ID_PLACEHOLDER
      bidListsToAddOrUpdate: [
        {
            bidListId: 530618873,
            isEnabled: true,
            isDefault: true
        }
      ]
      bidListIdsToRemove: [530618874, 530618875]
    }
  ) {
    data {
      id
      name
      adGroupLevelForecastResults {
        availsNumber
        durationInDays
        lastCalculatedAt
        maxPotentialSpend
        spend
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Archive a forecast

If you no longer need a forecast, you can archive it. Here's what you need to know about archiving a forecast:

- After you archive a forecast, you cannot restore it.
- You can view an archived forecast by using the `forecastsForAdvertiser` query to retrieve it.
- Archiving a forecast sets its `IsArchived` value to `true`. See also Retrieve a list of forecasts.

To archive a forecast, use the `forecastArchive` mutation and include your advertiser ID and the ID of the forecast you want to archive. Here's a `forecastArchive` mutation example to archive a forecast.

```
mutation {
  forecastArchive(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      forecastId: FORECAST_ID_PLACEHOLDER
    }
  ) {
    userErrors {
      field
      message
    }
  }
}
```

## FAQs

The following are frequently asked questions about forecasts.

### Why didn’t my ad group spend as forecasted?

Forecasts are only estimates based on seven days of historical data. Market conditions, supply, demand, and seasonal shifts can cause differences between forecasted and actual spend.

### Why are person reach counts greater than my country’s population?

Person reach counts are based on person IDs, which may group device IDs differently for work and home environments, causing counts to exceed real-world populations, especially when forecasting against broad targeting.

### Are household numbers unique or accumulated?

Household and person reach estimates are unique counts based on your forecast inputs.

### Can I add a marketplace blue list to a forecast?

Yes. To include a marketplace blue list when you create or update a forecast, set the `marketType` value to `MARKETPLACE`. This automatically applies the advertiser’s or partner’s blue list marketplace configuration to the forecast.
