# Frequency caps

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/FrequencyConfigurationBasicCaps
- Retrieved: 2026-11-14
- Category: Guides

---

# Frequency caps

A frequency cap, or an f-cap, limits the number of impressions a user can see within a given time period in a frequency cycle.

A frequency cap uses a counter, increments (entities like campaigns or ad groups that increment the counter), and a bid list of type `TargetList`. For details on the frequency framework elements and how pacing is affected by frequency caps, see Frequency.

## Create ad group frequency caps

There are two ways of creating ad group frequency caps:

- When creating or updating an ad group
- By creating a frequency configuration

The following sections explain each process and provide examples for creating a 1/24 (hr) frequency cap.

> **TIP**: If you want your ad group frequency cap configuration to appear editable in the platform UI, see FAQs.

### Create frequency caps when creating or updating ad groups

To create a frequency cap when creating or updating an ad group, you need to set a minimum of the following values in an ad group's `NewFrequencyConfigs`object of the respective POST /v3/adgroup or PUT /v3/adgroup request.

Here's what you need to know:

- The `NewFrequencyConfigs` object is returned in the response only if you include it in the request.
- If at least one frequency configuration in the request includes invalid values, the whole request will fail.

The following is a snippet of a POST /v3/adgroup request with the `NewFrequencyConfigs` object for creating a 1/24 frequency cap.

```
{
    "AdGroupId": "adgr1234",
    "NewFrequencyConfigs": [
        {
            "CounterName": "adgr1234 24 Hours",
            "ResetIntervalInMinutes": 1440,
            "FrequencyCap": 1
        }
    ]
}
```

### Frequency configuration properties

The following table explains the `NewFrequencyConfigs` object properties.

| Property | Value Example | Description |
| --- | --- | --- |
| `CounterName` | `advt1234 24 Hours` | An optional alphanumeric string with whitespace to identify the counter. |
| `ResetIntervalInMinutes` | `1440` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency cap fraction in minutes, for example, 24 hr x 60 min = 1440 min. |
| `FrequencyCap` | `1` | A positive integer that specifies the maximum number of ads to be shown to a user during the time interval specified in `ResetIntervalInMinutes`. This is the numerator in the frequency cap fraction. |

This request creates a counter, sets the ad group to increment the counter, and creates a bid list that will appear in all bid list endpoints, for example, as shown in the following example.

### Frequency cap bid list response example

The following is an example of a bid list created from the `NewFrequencyConfigs` settings in the request above.

> **NOTE**: Setting the `BidListAdjustmentType` to `TargetList` allows ad groups to bid on users who appear within the specified frequency range. Once the user's frequency count is beyond range, the platform no longer bids on ads for that user.

```
{
    "IsGlobal": false,
    "BidListDimensions": [
        "HasFrequencyV2AdjustmentId"
    ],
    "BidListType": ,
    "BidListId": "1234567",
    "Name": "Auto-Generated",
    "BidListSource": "User",
    "BidListAdjustmentType": "TargetList",
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
                }
            }
        }
    ],
    "BidListOwner": "AdGroup",
    "BidListOwnerId": "adgr1234",
    "IsAvailableForLibraryUse": false

}
```

### Create ad group frequency caps using frequency configuration

To create an ad group frequency cap by configuring frequency, use the POST /v3/frequency/config endpoint and do the following:

1. Create a counter in the frequency configuration with at least the `AdvertiserId` of the advertiser who owns the counter and the `ResetIntervalInMinutes` to specify the frequency cycle.
2. Create a frequency cap bid list with the bid list adjustment of type `TargetList`, bid line max and min ranges, `AdGroup` as the `BidListOwner`, and other properties as shown in the following example.
3. To add the ad group in `AssociatedAdGroups` as an increment for this counter, set `IncrementByAllEntitiesAssociatedWithBidLists` to `true`.

The following is a snippet of a POST /v3/frequency/config request for creating a 1/24 frequency cap for an ad group.

```
{
  "Counter": {
    "AdvertiserId": "advt1234",
    "ResetIntervalInMinutes": 1440,
    "CounterName": "advt1234 24 Hours"
  },
  "BidLists": [
    {
      "Name": "adgr1234 1/24 Frequency Cap",
      "BidListOwner": "AdGroup",
      "BidListOwnerId": "adgr1234",
      "BidListAdjustmentType": "TargetList",
      "AssociatedAdGroups": [
        "adgr1234"
      ],
      "BidLines": [
        {
          "Range": {
            "Min": 0,
            "Max": 1
          },
          "BidAdjustment": 1
        }
      ]
    }
  ],
  "IncrementByAllEntitiesAssociatedWithBidLists": true
}
```

The following tables explain the property values in the above request.

### Counter properties

| Property | Value Example | Description |
| --- | --- | --- |
| `AdvertiserId` | `advt1234` | The platform ID of the advertiser that owns this counter. This value cannot be updated after creation. |
| `ResetIntervalInMinutes` | `1440` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency cap fraction in minutes, for example, 24 hr x 60 min = 1440 min. |
| `CounterName` | `advt1234 24 Hours` | An optional alphanumeric string with whitespace to identify the counter. |

### Bid list properties

| Property | Value Example | Description |
| --- | --- | --- |
| `Name` | `adgr1234 1/24 Frequency Cap` | An alphanumeric string with whitespace to identify the bid list. |
| `BidListOwner` | `AdGroup` | The type of the owner of this bid list. |
| `BidListOwnerId` | `adgr1234` | The ID of the ad group that owns the bid lis. |
| `BidListAdjustmentType` | `TargetList` | Setting the `BidListAdjustmentType` to `TargetList` allows the ad group to bid only on users who appear within the specified frequency range. Once the user's frequency count is beyond the range, they are no longer served ads. |
| `BidLines.Range.Min` | `0` | The minimum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes`. To include users who have not yet seen the ad, set this value to `0`. |
| `BidLines.Range.Max` | `1` | The maximum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes`. This is the numerator in the frequency cap fraction. |
| `BidLines.BidAdjustment` | `1` | Bid lines in a `TargetList` must always be set to `1`. |

## Create campaign frequency caps

There are two ways of creating campaign frequency caps:

- When creating or updating a campaign
- By creating a frequency configuration

The following sections explain each process and provide examples for creating a 5/10080 (min) frequency cap.

### Create frequency caps when creating or updating campaigns

To create a frequency cap when creating or updating a campaign, you need to set a minimum of the following values in a campaign's `NewFrequencyConfigs` object of the respective POST /v3/campaign or PUT /v3/campaign request.

Here's what you need to know:

- The `NewFrequencyConfigs` object is returned in the response only if you include it in the request.
- If at least one frequency configuration in the request includes an invalid value, the whole request will fail.

The following is a snippet of a POST /v3/campaign request with the `NewFrequencyConfigs` object for creating a 5/10080 frequency cap.

```
{
    "CampaignId": "camp1234",
    "NewFrequencyConfigs": [
        {
            "CounterName": "camp1234 One Week",
            "ResetIntervalInMinutes": 10080,
            "FrequencyCap": 5
        }
    ]
}
```

### Frequency configuration properties

The following table explains the `NewFrequencyConfigs` object properties.

| Property | Value Example | Description |
| --- | --- | --- |
| `CounterName` | `camp1234 One Week` | An optional alphanumeric string with whitespace to identify the counter. |
| `ResetIntervalInMinutes` | `10080` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency cap fraction in minutes. |
| `FrequencyCap` | `5` | A positive integer that specifies the maximum number of ads to be shown to a user during the time interval specified in `ResetIntervalInMinutes`. This is the numerator in the frequency cap fraction. |

### Create campaign frequency caps using frequency configuration

To create a campaign frequency cap by configuring frequency, use the POST /v3/frequency/config endpoint and do the following:

1. Create a counter in the frequency configuration with at least the `AdvertiserId` of the advertiser who owns the counter and the `ResetIntervalInMinutes` to specify the frequency cycle.
2. Create a frequency cap bid list with the bid list adjustment of type `TargetList`, bid line max and min ranges, `Campaign` as the `BidListOwner`, and other properties as shown in the following example.
3. To add the campaign in `AssociatedCampaigns` as an increment for this counter, set `IncrementByAllEntitiesAssociatedWithBidLists` to `true`.

The following is a snippet of a POST /v3/frequency/config request for creating a 5/10080 frequency cap for a campaign.

```
{
  "Counter": {
    "AdvertiserId": "advt1234",
    "ResetIntervalInMinutes": 10080,
    "CounterName": "advt1234 One Week"
  },
  "BidLists": [
    {
      "Name": "camp1234 5/10080 Frequency Cap",
      "BidListOwner": "Campaign",
      "BidListOwnerId": "camp1234",
      "BidListAdjustmentType": "TargetList",
      "AssociatedCampaigns": [
        "camp1234"
      ],
      "BidLines": [
        {
          "Range": {
            "Min": 0,
            "Max": 5
          },
          "BidAdjustment": 1
        }
      ]
    },
  ],
  "IncrementByAllEntitiesAssociatedWithBidLists": true
}
```

The following tables explain the property values in the above request.

### Counter properties

| Property | Value Example | Description |
| --- | --- | --- |
| `AdvertiserId` | `advt1234` | The platform ID of the advertiser that owns this counter. This value cannot be updated after creation. |
| `ResetIntervalInMinutes` | `10080` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency cap fraction in minutes. |
| `CounterName` | `advt1234 One Week` | An optional alphanumeric string with whitespace to identify the counter. |

### Bid list properties

| Property | Value Example | Description |
| --- | --- | --- |
| `Name` | `camp1234 5/10080 Frequency Cap` | An alphanumeric string with whitespace to identify the bid list. |
| `BidListOwner` | `Campaign` | The type of the owner of this bid list. |
| `BidListOwnerId` | `camp1234` | The ID of the campaign that owns the bid list. |
| `BidListAdjustmentType` | `TargetList` | Setting the `BidListAdjustmentType` to `TargetList` allows the campaign's ad groups to bid only on users who appear within the specified frequency range. Once the user's frequency count is beyond the range, they are no longer served ads. |
| `BidLines.Range.Min` | `0` | The minimum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes`. To include users who have not yet seen the ad, set this value to `0`. |
| `BidLines.Range.Max` | `5` | The maximum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes`. This is the numerator in the frequency cap fraction. |
| `BidLines.BidAdjustment` | `1` | Bid lines in a `TargetList` must always be set to `1`. |

## FAQs

The following is a list of commonly asked questions about frequency caps.

### How do I make sure that users can edit my ad group frequency cap configuration in the platform UI?

To make your frequency cap configuration editable in the platform UI, be sure to follow these requirements when creating it:

 Create only one counter per ad group. If you reuse counters on multiple ad groups, you will not be able to edit values in the UI without using the **Override Values** button.
 Associate and enable only one frequency cap bid list for the ad group. The bid list must be owned by the same ad group.
 Make sure that the ad group’s `Increments` list includes the same counter ID as the bid list associated with the ad group.
 If you are defining both a frequency cap and a frequency goal for an ad group, use separate counters, even if the cap and goal have the same reset interval.
