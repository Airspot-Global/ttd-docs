# Frequency management tasks and endpoints

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/FrequencyTasks
- Retrieved: 2026-11-14
- Category: Guides

---

# Frequency management tasks and endpoints

The following sections list the endpoints for managing the frequency framework elements and provide high-level guidelines for using them:

- Counters
- Increments
- Bid lists

For common use cases and setup instructions, see the guides for Frequency caps, goals, and bid adjustments.

> **TIP**: For basic configurations, it is most efficient to use the frequency configuration endpoints, which allow you to set up counters, increments, and bid lists in one step.

## Counters

A counter is a container that holds the user’s frequency count information (the number of times the user has seen the ad) and defines the time interval (the `ResetIntervalInMinutes` field) after which the counter is reset.

Here's what you need to know about counters:

- Counters are the key frequency setting. Querying frequency configurations requires a valid counter ID.
- Use as few counters as possible to cover unique combinations of `ResetIntervalInMinutes` and `Increments` in your strategy.
- Counters retain user counts for approximately two weeks after a campaign ends. This may affect your data if you decide to reuse counters.
- Delete any counters that are no longer needed. Deleting a counter will also delete any increment links that reference that counter.

### Creating counters

The following table lists the endpoints you can use to create counters.

| Task | Endpoint | Configuration | Notes |
| --- | --- | --- | --- |
| Create a counter, its increments, and bid lists. | POST /v3/frequency/config | Basic | For example, see Frequency caps or Frequency goals. |
| Create an individual counter. | POST /v3/frequency/counter | Advanced | This is one step in a multi-step workflow of manually configuring frequency. **TIP**: For basic configurations, it is most efficient to use the frequency configuration endpoints, which allow you to create and manage counters. |
| Create a counter while creating or updating a campaign. | POST /v3/campaign PUT /v3/campaign | Basic | Specify the counter details in the `NewFrequencyConfigs` object of the request. For example, see Frequency caps or Frequency goals. |
| Create a counter while creating or updating an ad group. | POST /v3/adgroup PUT /v3/adgroup | Basic | Specify the counter details in the `NewFrequencyConfigs` object of the request. For example, see Frequency caps or Frequency goals. |

### Retrieving counters

The following table lists the endpoints you can use to retrieve counter information.

| Task | Endpoint | Configuration | Notes |
| --- | --- | --- | --- |
| Retrieve details for a counter, its increments, and bid lists. | GET /v3/frequency/config/{counterId} | Basic | Use this endpoint to retrieve entire frequency configuration, including counter information and other details at the same time. For details, see Look up frequency configuration for a counter. |
| Retrieve details for an individual counter. | GET /v3/frequency/counter/{counterId} | Advanced | Use this endpoint to look up only counter details with no increment or bid list details. |
| Retrieve a paged and filterable list of frequency counters for a specific advertiser or partner. | POST /v3/frequency/counter/query | Basic | N/A |
| Retrieve a paged and filterable list of frequency configurations, including counters, for a specific entity. | POST /v3/frequency/config/query | Basic | N/A |

### Look up frequency configuration for a counter

To view the frequency information for a specific counter, include its ID as the path parameter in a GET /v3/frequency/config/{counterId} request.

For example, for a counter with the ID of `2gbda7q`, a `GET /v3/frequency/config/2gbda7q` request may return the following configuration details, which include an ad group that increments the counter and a bid list with which the frequency configuration is associated.

```
{
   "Counter":{
      "CounterId":"2gbda7q",
      "AdvertiserId":"7ftzaer",
      "ResetIntervalInMinutes":300,
      "CounterName":"Basic Frequency - AG: 8hbtm7p, Reset: 300",
      "CounterAttribute":"None"
   },
   "Increments":{
      "AdGroups":[
         "qzjt6yn"
      ]
   },
   "BidLists":[
      {
         "BidListId":"62220626",
         "Name":"Default Frequency Cap List",
         "BidListOwner":"AdGroup",
         "BidListOwnerId":"qzjt6yn",
         "NumberOfBidLines":1,
         "BidListAdjustmentType":"TargetList",
         "AssociatedAdGroups":[
            "qzjt6yn"
         ],
         "BidLines":[
            {
               "Range":{
                  "Min":0,
                  "Max":1
               },
               "VolumeControlPriority":"Neutral",
               "BidAdjustment":1.000000
            }
         ]
      }
   ]
}
```

### Updating counters

The following table lists the endpoints you can use to update counters.

| Task | Endpoint | Configuration | Notes |
| --- | --- | --- | --- |
| Update a counter, its increments, and bid lists. | PUT /v3/frequency/config | Basic | N/A |
| Update an individual counter. | PUT /v3/frequency/counter | Advanced | Using this endpoint is more efficient if you want to edit only a counter name or reset interval. |

### Deleting counters

The following table lists the endpoint you can use to delete counters.

| Task | Endpoint | Configuration |
| --- | --- | --- |
| Delete an individual frequency counter and all of its associated increments, and bid lists. | DELETE /v3/frequency/config/{counterId} | Basic |

## Increments

Increments are entities (partners, advertisers, campaigns, and ad groups) that serve impressions to users and increase the user's frequency count for the associated counter.

Descendant entities affect increment the counters of their higher-level entities set as increments. For example, a partner set as an increment would increase the counter any time a user sees an ad for any ad groups for any of its advertisers' campaigns.

> **TIP**: Use the entity-level inheritance to set up frequency increments at the appropriate levels and reduce manual tasks.

For example, to increment frequency counts for every ad group in a campaign, set the campaign to increment the counter rather than individual ad groups. If an ad group is added to the campaign after frequency is set up, the campaign-level increment will apply to the new ad group, whereas if individual ad groups are specified as increments, the new ad group will need to be manually added.

### Creating increments

| Task | Endpoint | Configuration | Notes |
| --- | --- | --- | --- |
| Create a counter, its increments, and bid lists. | POST /v3/frequency/config | Basic | For example, see Frequency caps or Frequency goals. |
| Add an ad group as an increment to a counter. | POST /v3/adgroup PUT /v3/adgroup | Advanced | To increase counts each time a user sees an ad for this ad group, list the frequency `CounterIds` in the `Increments` array. |
| Add a campaign as an increment to a counter. | POST /v3/campaign PUT /v3/campaign | Advanced | To increase counts each time a user sees an ad for this campaign, including any of its ad groups, list the frequency `CounterIds` in the `Increments` array. |
| Add an advertiser as an increment to this counter. | POST /v3/advertiser PUT /v3/advertiser | Advanced | To increase counts each time a user sees an ad for this advertiser, including all of its campaigns and ad groups, list the frequency `CounterIds` in the `Increments` array. |

### Retrieving increments

The endpoints listed below return all increments as a list of `CounterIds` in the `Increments` array. To retrieve individual counter details, use the GET /v3/frequency/counter/{counterId} endpoint.

| Task | Endpoint | Configuration |
| --- | --- | --- |
| Retrieve all increments for a specific counter. | GET /v3/frequency/config/{counterId} | Basic |
| Retrieve all counters incremented by an ad group. | GET /v3/adgroup/{adGroupId} | Basic |
| Retrieve all counters incremented by a campaign. | GET /v3/campaign/{campaignId} | Basic |
| Retrieve all counters incremented by an advertiser. | GET /v3/advertiser/{advertiserId} | Basic |

### Updating increments

| Task | Endpoint | Configuration | Notes |
| --- | --- | --- | --- |
| Update a counter, its increments, and bid lists. | PUT /v3/frequency/config | Basic | N/A |
| Update an ad group as an increment to a counter. | POST /v3/adgroup PUT /v3/adgroup | Advanced | Update `CounterIds` in the `Increments` array as needed. |
| Update a campaign as an increment to a counter. | POST /v3/campaign PUT /v3/campaign | Advanced | Update `CounterIds` in the `Increments` array as needed. |
| Update an advertiser as an increment to a counter. | POST /v3/advertiser PUT /v3/advertiser | Advanced | Update `CounterIds` in the `Increments` array as needed. |

### Removing increments

| Task | Endpoint | Configuration | Notes |
| --- | --- | --- | --- |
| Update a counter, its increments, and bid lists. | PUT /v3/frequency/config | Basic | Remove entities from the `Increments` object. |
| Remove an ad group as an increment to a counter. | POST /v3/adgroup PUT /v3/adgroup | Advanced | Remove `CounterIds` from the `Increments` array. |
| Remove a campaign as an increment to a counter. | POST /v3/campaign PUT /v3/campaign | Advanced | Remove `CounterIds` from the `Increments` array. |
| Remove an advertiser as an increment to a counter. | POST /v3/advertiser PUT /v3/advertiser | Advanced | Remove `CounterIds` from the `Increments` array. |

## Bid lists

Use bid lists to apply frequency caps, frequency goals, and bid adjustments to partners, advertisers, campaigns, and ad groups by specifying the counter to use and configuring the relevant adjustments. For details, see Frequency bid adjustments.
