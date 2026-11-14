# Frequency bid adjustments

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/FrequencyConfigurationBasicBidAdjustments
- Retrieved: 2026-11-14
- Category: Guides

---

# Frequency bid adjustments

Frequency bid adjustments update bid amounts for a user based on the number of impressions seen within the frequency cycle. A frequency range in a bid line specifies the minimum and maximum number of impressions to be shown to a user. Multiple bid adjustments for individual frequency ranges may be grouped to increase or decrease bidding for users who have seen an ad a certain number of times over a specified time period.

Here's what you need to know about frequency bid adjustments:

- Frequency bid adjustments can be used in conjunction with frequency caps to fine tune the ad group strategy.
- The bid list adjustment should be of type `Optimized`.
- Bid lists with multiple bid adjustments may have gaps between ranges.
- Any impressions that do not match the specified frequency ranges are treated as though their `BidAdjustment` is set to `1`.
- To create a frequency range that extends to the lifetime maximum for a user, set the `TimesShown.Max` value to `2147483647`.

> **IMPORTANT**: To avoid unintentionally inflating bid prices, use frequency ranges that are sequential and do not overlap.

For example, if a bid list includes the following two overlapping frequency ranges within the same bid list, the final bid adjustment will be calculated as 3.5 for an impression that matches both ranges.

- 0-3 times per 1 week with a bid adjustment of 2
- 2-4 times per 1 month with a bid adjustment of 1.5

## Creating bid lists with multiple frequency bid adjustments

To create a bid list with multiple frequency bid adjustments, use the POST /v3/frequency/config endpoint and do the following:

1. Create a counter in the frequency configuration with at least the `AdvertiserId` of the advertiser who owns the counter and the `ResetIntervalInMinutes` to specify the frequency cycle.
2. Create a bid list with the bid list adjustment of type `Optimized`, bid lines with the sequential max and min ranges, `AdGroup` as the `BidListOwner`, and other properties as shown in the following example.
3. To add the ad group in `AssociatedAdGroups` as an increment for this counter, set `IncrementByAllEntitiesAssociatedWithBidLists` to `true`.

For example, the following POST /v3/frequency/config request sample illustrates how to create a bid list with the following three frequency ranges and bid adjustments for a 4-week interval:

| Range Description | Min | Max | Bid Adjustment |
| --- | --- | --- | --- |
| No ads seen yet / first ad to be shown | `0` | `1` | `1.75` |
| Ad seen 1-4 times / to show ad 2-5 times | `1` | `5` | `1.5` |
| Ad seen 5-9 times / to show ad 6-10 times | `5` | `10` | `1.25` |

Here's a request example:

```
{
   "Counter":{
      "AdvertiserId":"advt1234",
      "ResetIntervalInMinutes":40320,
      "CounterName":"advt1234 Four Weeks"
   },
   "BidLists":[
      {
         "Name":"adgr1234 Four Week Frequency",
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
                  "Max":1
               },
               "BidAdjustment":1.75
            },
            {
               "Range":{
                  "Min":1,
                  "Max":5
               },
               "BidAdjustment":1.5
            },
            {
               "Range":{
                  "Min":5,
                  "Max":10
               },
               "BidAdjustment":1.25
            }
         ]
      }
   ],
   "IncrementByAllEntitiesAssociatedWithBidLists":true
}
```

The following tables explain the property values in the above request.

#### Counter properties

| Property | Value Example | Description |
| --- | --- | --- |
| `AdvertiserId` | `advt1234` | The platform ID of the advertiser that owns this counter. This value cannot be updated after creation. |
| `ResetIntervalInMinutes` | `40320` | A positive integer that defines the time interval (in minutes) after which the frequency counter is reset to `0`. This is the denominator in the frequency cap fraction in minutes, for example, 4 weeks x 60 min = 40320 min. |
| `CounterName` | `advt1234 Four Weeks` | An optional alphanumeric string with whitespace to identify the counter. |

#### Bid list properties

| Property | Value Example | Description |
| --- | --- | --- |
| `Name` | `adgr1234 Four Week Frequency` | An alphanumeric string with whitespace to identify the bid list. |
| `BidListOwner` | `AdGroup` | The type of the owner of this bid list. |
| `BidListOwnerId` | `adgr1234` | The ID of the owning ad group. |
| `BidListAdjustmentType` | `Optimized` | The bid list adjustment type. |
| `BidLines.Range.Min` | N/A | The respective minimum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes` for each frequency range in the bid list. |
| `BidLines.Range.Max` | N/A | The respective maximum number of times to show an ad to a user within the counter's `ResetIntervalInMinutes` for each frequency range in the bid list. |
| `BidLines.BidAdjustment` | N/A | The respective bid list adjustment amount for each frequency range in the bid list. |
