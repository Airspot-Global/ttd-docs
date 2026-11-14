# Frequency goals

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/FrequencyConfigurationBasicGoals
- Retrieved: 2026-11-14
- Category: Guides

---

# Frequency goals

A frequency goal specifies the preferred number of impressions to be targeted for a user. The platform optimizes toward the number of impressions set as the frequency goal. For example, users who have already seen an ad are favored to see another impression over unknown users until the specified frequency goal is reached.

A frequency goal uses a counter, increments (entities like campaigns or ad groups that increment the counter), and an `Optimized` bid list with the `VolumeControlPriority` property set to `FrequencyGoal`. For details on the frequency framework elements, see Frequency.

> **IMPORTANT**: Frequency goals must have the minimum range of 1 per 24 hours.

## Create ad group frequency goals

There are two ways of creating ad group frequency goals:

- When creating or updating an ad group
- By creating a frequency configuration

The following sections explain each process and provide examples for creating a 1/24 (hr) frequency goal. See also Understanding fraction notation and pacing.

> **TIP**: If you want your ad group frequency goal configuration to appear editable in the platform UI, see FAQs.

### Create frequency goals when creating or updating ad groups

To create a frequency goal when creating or updating an ad group, you need to set a minimum of the following values in the ad group's `NewFrequencyConfigs`object of the respective POST /v3/adgroup or PUT /v3/adgroup request.

Here's what you need to know:

- The `NewFrequencyConfigs` object is returned in the response only if you include it in the request.
- If at least one frequency configuration in the request includes invalid values, the whole request will fail.

The following is a snippet of a POST /v3/adgroup request with the `NewFrequencyConfigs` object for creating a 1/24 frequency goal.

```
{
    "AdGroupId": "adgr1234",
    "NewFrequencyConfigs": [
        {
            "CounterName": "adgr1234 24 Hours",
            "ResetIntervalInMinutes": 1440,
            "FrequencyGoal": 2
        }
    ]
}
```

### Frequency configuration properties

The following table explains the `NewFrequencyConfigs` object properties.

| Property | Value Example | Description |
| --- | --- | --- |
| `CounterName` | `adgr1234 24 Hours` | An optional alphanumeric string with whitespace to identify the counter. |
| `ResetIntervalInMinutes` | `1440` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency goal fraction in minutes, for example, 24 hr x 60 min = 1440 min. |
| `FrequencyGoal` | `2` | A positive integer that specifies the minimum number of ads to be shown to a user during the time interval specified in `ResetIntervalInMinutes`. For example, the value of `2` targets users who have been exposed to an ad once, while the value of `1` targets only new users, which may have a dramatic impact on bidding. **NOTE**: The system will try to reach each user the designated number of times. It is not guaranteed that every user will reach this target, as user behavior cannot be controlled. |

This request creates a counter, sets the ad group to increment the counter, and creates a bid list that will appear in all bid list endpoints, for example, as shown in the following example.

#### Frequency goal bid list response example

The following is an example of a bid list created from the `NewFrequencyConfigs` settings in the request above.

```
{
    "IsGlobal": true,
    "BidListDImensions": [
        "HasFrequencyV2AdjustmentId"
    ],
    "BidListType": ,
    "BidListId": "1234567",
    "Name": "Auto-Generated",
    "BidListSource": "User",
    "BidListAdjustmentType": "Optimized",
    "ResolutionType": "ApplyMinimumAdjustment",
    "BidLines": [
        {
            "BidLineId": "2345678",
            "BidAdjustment": 1,
            "FrequencyRange":{
                "CounterId": "count123",
                "TimesShown": {
                    "Min": 0,
                    "Max": 1
                },
            "VolumeControlPriority": "FrequencyGoal"
            }
        }
    ],
    "BidListOwner": "AdGroup",
    "BidListOwnerId": "adgr1234",
    "IsAvailableForLibraryUse": false
}
```

### Create ad group frequency goals using frequency configuration

To create an ad group frequency goal by configuring frequency, use the POST /v3/frequency/config endpoint and do the following:

1. Create a counter in the frequency configuration with at least the `AdvertiserId` of the advertiser who owns the counter and the `ResetIntervalInMinutes` to specify the frequency cycle.
2. Create a frequency goal bid list with the bid list adjustment of type `Optimized`, bid line max and min ranges, the bid line `VolumeControlPriority` property set to `FrequencyGoal`, `AdGroup` as the `BidListOwner`, and other properties as shown in the following example.
3. To add the ad group in `AssociatedAdGroups` as an increment for this counter, set `IncrementByAllEntitiesAssociatedWithBidLists` to `true`.

The following is a snippet of a POST /v3/frequency/config request for creating a 1/24 frequency goal for an ad group.

```
{
   "Counter":{
      "AdvertiserId":"advt1234",
      "ResetIntervalInMinutes":1440,
      "CounterName":"advt1234 24 Hours"
   },
   "BidLists":[
      {
         "Name":"adgr1234 1/24 Frequency Goal",
         "BidListOwner":"AdGroup",
         "BidListOwnerId":"adgr1234",
         "BidListAdjustmentType":"Optimized",
         "ResolutionType":"ApplyMultiplyAdjustment",
         "AssociatedAdGroups":[
            "adgr1234"
         ],
         "BidLines":[
            {
               "Range":{
                  "Min":0,
                  "Max":2
               },
               "BidAdjustment":1,
               "VolumeControlPriority":"FrequencyGoal"
            }
         ]
      }
   ],
   "IncrementByAllEntitiesAssociatedWithBidLists":true
}
```

The following tables explain the property values in the above request.

### Counter properties

| Property | Value Example | Description |
| --- | --- | --- |
| `AdvertiserId` | `advt1234` | The platform ID of the advertiser that owns this counter. This value cannot be updated after creation. |
| `ResetIntervalInMinutes` | `1440` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency goal fraction in minutes, for example, 24 hr x 60 min = 1440 min. |
| `CounterName` | `advt1234 24 Hours` | An optional alphanumeric string with whitespace to identify the counter. |

### Bid list properties

| Property | Value Example | Description |
| --- | --- | --- |
| `Name` | `adgr1234 1/24 Frequency Goal` | An alphanumeric string with whitespace to identify the bid list. |
| `BidListOwner` | `AdGroup` | The type of the owner of this bid list. |
| `BidListOwnerId` | `adgr1234` | The ID of the ad group that owns the bid list. |
| `BidListAdjustmentType` | `Optimized` | Setting the `BidListAdjustmentType` to `Optimized` allows the bid list to set the bid line `VolumeControlPriority` to `FrequencyGoal`. |
| `BidLines.Range.Min` | `0` | The minimum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes`. To include users who have not yet seen the ad, set this value to `0`. |
| `BidLines.Range.Max` | `2` | The maximum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes`. This is the numerator in the frequency goal fraction. |
| `BidLines.BidAdjustment` | `1` | Bid lines in a bid list using `VolumeControlPriority` must always have their bid adjustment set to `1`. |
| `BidLines.VolumeControlPriority` | `FrequencyGoal` | The volume control priority to apply to this adjustment. |

## Create campaign frequency goals

There are two ways of creating campaign frequency goals:

- When creating or updating an campaign
- By creating a frequency configuration

The following sections explain each process and provide examples for creating a 1/24 (hr) frequency goal. See also Understanding fraction notation and pacing.

### Create frequency goals when creating or updating campaigns

To create a frequency goal when creating or updating a campaign, you need to set a minimum of the following values in the campaign's `NewFrequencyConfigs`object of the respective POST /v3/campaign or PUT /v3/campaign request.

Here's what you need to know:

- The `NewFrequencyConfigs` object is returned in the response only if you include it in the request.
- If at least one frequency configuration in the request includes an invalid value, the whole request will fail.

The following is a snippet of a POST /v3/campaign request with the `NewFrequencyConfigs` object for creating a 1/24 frequency goal.

```
{
    "CampaignId": "camp1234",
    "NewFrequencyConfigs": [
        {
            "CounterName": "camp1234 24 Hours",
            "ResetIntervalInMinutes": 1440,
            "FrequencyGoal": 2
        }
    ]
}
```

### Frequency configuration properties

The following table explains the `NewFrequencyConfigs` object properties.

| Property | Value Example | Description |
| --- | --- | --- |
| `CounterName` | `adgr1234 24 Hours` | An optional alphanumeric string with whitespace to identify the counter. |
| `ResetIntervalInMinutes` | `1440` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency goal fraction in minutes, for example, 24 hr x 60 min = 1440 min. |
| `FrequencyGoal` | `2` | A positive integer that specifies the minimum number of ads to be shown to a user during the time interval specified in `ResetIntervalInMinutes`. For example, the value of `2` targets users who have been exposed to an ad once, while the value of `1` targets only new users, which may have a dramatic impact on bidding. **NOTE**: The system will try to reach each user the designated number of times. It is not guaranteed that every user will reach this target, as user behavior cannot be controlled. |

### Create campaign frequency goals using frequency configuration

To create a campaign frequency goal by configuring frequency, use the POST /v3/frequency/config endpoint and do the following:

1. Create a counter in the frequency configuration with at least the `AdvertiserId` of the advertiser who owns the counter and the `ResetIntervalInMinutes` to specify the frequency cycle.
2. Create a frequency goal bid list with the bid list adjustment of type `Optimized`, bid line max and min ranges, the bid line `VolumeControlPriority` property set to `FrequencyGoal`, `Campaign` as the `BidListOwner`, and other properties as shown in the following example.
3. To add the campaign in `AssociatedCampaigns` as an increment for this counter, set `IncrementByAllEntitiesAssociatedWithBidLists` to `true`.

The following is a snippet of a POST /v3/frequency/config request for creating a 1/24 frequency goal for a campaign.

```
{
   "Counter":{
      "AdvertiserId":"advt1234",
      "ResetIntervalInMinutes":1440,
      "CounterName":"advt1234 24 Hours"
   },
   "BidLists":[
      {
         "Name":"camp1234 1/24 Frequency Goal",
         "BidListOwner":"Campaign",
         "BidListOwnerId":"camp1234",
         "BidListAdjustmentType":"Optimized",
         "ResolutionType":"ApplyMultiplyAdjustment",
         "AssociatedCampaigns":[
            "camp1234"
         ],
         "BidLines":[
            {
               "Range":{
                  "Min":0,
                  "Max":2
               },
               "BidAdjustment":1,
               "VolumeControlPriority":"FrequencyGoal"
            }
         ]
      }
   ],
   "IncrementByAllEntitiesAssociatedWithBidLists":true
}
```

The following tables explain the property values in the above request.

### Counter properties

| Property | Value Example | Description |
| --- | --- | --- |
| `AdvertiserId` | `advt1234` | The platform ID of the advertiser that owns this counter. This value cannot be updated after creation. |
| `ResetIntervalInMinutes` | `1440` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency goal fraction in minutes, for example, 24 hr x 60 min = 1440 min. |
| `CounterName` | `advt1234 24 Hours` | An optional alphanumeric string with whitespace to identify the counter. |

### Bid list properties

| Property | Value Example | Description |
| --- | --- | --- |
| `Name` | `camp1234 1/24 Frequency Goal` | An alphanumeric string with whitespace to identify the bid list. |
| `BidListOwner` | `Campaign` | The type of the owner of this bid list. |
| `BidListOwnerId` | `camp1234` | The ID of the campaign that owns the bid list. |
| `BidListAdjustmentType` | `Optimized` | Setting the `BidListAdjustmentType` to `Optimized` allows the bid list to set the bid line `VolumeControlPriority` to `FrequencyGoal`. |
| `BidLines.Range.Min` | `0` | The minimum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes`. To include users who have not yet seen the ad, set this value to `0`. |
| `BidLines.Range.Max` | `2` | The maximum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes`. This is the numerator in the frequency goal fraction. |
| `BidLines.BidAdjustment` | `1` | Bid lines in a bid list using `VolumeControlPriority` must always have their bid adjustment set to `1`. |
| `BidLines.VolumeControlPriority` | `FrequencyGoal` | The volume control priority to apply to this adjustment. |

## FAQs

The following is a list of commonly asked questions about frequency caps.

### How do I make sure that users can edit my ad group frequency goal configuration in the platform UI?

To make your frequency goal configuration editable in the platform UI, be sure to follow these requirements when creating it:

 Create only one counter per ad group. If you reuse counters on multiple ad groups, you will not be able to edit values in the UI without using the **Override Values** button.

 Associate and enable only one frequency cap bid list for the ad group. The bid list must be owned by the same ad group.

 Make sure that the ad group’s `Increments` list includes the same counter ID as the bid list associated with the ad group.

 If you are defining both a frequency cap and a frequency goal for an ad group, use separate counters, even if the cap and goal have the same reset interval.
