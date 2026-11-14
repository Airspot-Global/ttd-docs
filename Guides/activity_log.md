# Activity logs

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/ActivityLog
- Retrieved: 2026-11-14
- Category: Guides

---

# Activity logs

The activity log captures changes made to an ad group and who made them. These logs assist in evaluating how specific changes affect campaign strategy. Here's what you need to know about activity logs:

- Activity logs are available only in the REST API.
- Activity is logged for ad groups and ad-group owned bid lists.
- The activity log endpoints enable you to retrieve activity logs as well as create and update notes for individual activity logs.
- Activity log information is rolled up every five minutes and is retrievable through the API 10-15 minutes after the change is logged.
- The maximum lookback period for the activity log endpoints counts the previous three months plus the days in the current month leading up to today.

For instance, in a lookback on January 15 of the current year, all of October, November, and December of the previous year and everything up to January 15 of the current year will be included in the Activity Log. The following table shows the spectrum of one of the shortest to one of the longest lookback periods.

| Lookback Date | Date Range | Lookback Duration |
| --- | --- | --- |
| July 1, 2020 | April 1, 2020 - July 1, 2020 | 92 days |
| January 31, 2021 | October 1, 2020 - January 31, 2021 | 123 days |

## Ad group property changes

To learn more about ad groups, review our Ad groups article. To learn more about ad group properties, review the POST /v3/adgroup documentation.

The following property changes are logged when an ad group is updated. They are not logged when an ad group is created.

> **IMPORTANT**: When an ad group is created through the API, initial property values are not logged, except as noted. When a user creates an ad group through the platform user interface, it does log initial values for most properties. Creating a new ad group through the user interface creates an initial ad group and then updates that ad group's settings to add the other properties throughout the workflow.

| Property | Ad Group Create | Ad Group Update |
| --- | --- | --- |
| `IsEnabled` | N/A | Yes |

### Ad group audience

The following properties are logged when updated.

| Property | Ad Group Create | Ad Group Update |
| --- | --- | --- |
| `RTBAttributes.AudienceTargeting.AudienceExcluderEnabled` | N/A | Yes |
| `RTBAttributes.AudienceTargeting.AudienceId` | N/A | Yes |
| `RTBAttributes.AudienceTargeting.AudiencePredictorEnabled` | N/A | Yes |
| `RTBAttributes.AudienceTargeting.CrossDeviceVendorListForAudience.CrossDeviceVendorId` | N/A | Yes |

> **NOTE**: The `RTBAttributes.AudienceTargeting.AudienceExcluderEnabled` property controls the enhanced feature known as Prism.

### Ad group budget and goals

The following properties are logged when updated.

| Property | Ad Group Create | Ad Group Update |
| --- | --- | --- |
| `RTBAttributes.BudgetSettings.BaseBidCPM` | N/A | Yes |
| `RTBAttributes.BudgetSettings.MaxBidCPM` | N/A | Yes |
| `RTBAttributes.BudgetSettings.PacingMode` | N/A | Yes |
| `RTBAttributes.BudgetSettings.ROIGoal` | N/A | Yes |

### Ad group flights

The following properties are logged when updated.

| Property | Ad Group Create | Ad Group Update |
| --- | --- | --- |
| `RTBAttributes.BudgetSettings.AdGroupFlights.Budget.Amount` | N/A | Yes |
| `RTBAttributes.BudgetSettings.AdGroupFlights.Budget.BudgetInImpressions` | N/A | Yes |
| `RTBAttributes.BudgetSettings.AdGroupFlights.Budget.DailyBudget` | N/A | Yes |
| `RTBAttributes.BudgetSettings.AdGroupFlights.Budget.DailyTargetInImpressions` | N/A | Yes |

### Ad group contract targeting

The following properties are logged when updated.

| Property | Ad Group Create | Ad Group Update |
| --- | --- | --- |
| `RTBAttributes.ContractTargeting.AllowOpenMarketBiddingWhenTargetingContracts` | N/A | Yes |

### Ad group associated bid lists

The following properties are logged when a `BidList` is owned by the ad group. Changes are logged when a `BidList` is added or removed from `AssociatedBidLists`, or the bid list is enabled or disabled.

| Property | Insert | Update | Delete |
| --- | --- | --- | --- |
| `AssociatedBidLists.BidList.BidListId` | Yes | Yes | Yes |
| `AssociatedBidLists.BidList.IsDefaultForDimension` | Yes | Yes | Yes |
| `AssociatedBidLists.BidList.IsEnabled` | Yes | Yes | Yes |

### `bid list` logged property changes

To learn more about bid lists, review our Bid lists article. To learn more about bid list properties, review the POST /v3/bidlist documentation.

`BidList` and `BidLines` properties are logged when the `BidListOwner` is `AdGroup`.

These properties are logged when the bid list is deleted.

| Property | Insert | Update | Delete |
| --- | --- | --- | --- |
| `BidListAdjustmentType` | N/A | N/A | Yes |
| `BidListDimensions` | N/A | N/A | Yes |
| `BidListId` | N/A | N/A | Yes |
| `BidListOwnerId` | N/A | N/A | Yes |
| `Name` | N/A | N/A | Yes |
| `SourceType` | N/A | N/A | Yes |

`BidLines` properties are logged when `BidLines` are added or removed or when the `BidAdjustment` for a bid line is updated.

| Property | Insert | Update | Delete |
| --- | --- | --- | --- |
| `BidLines.BidLineId` | Yes | Yes | Yes |
| `BidLines.BidAdjustment` | Yes | Yes | Yes |
| `BidLines.DimensionDescriptor` | Yes | Yes | Yes |

## Activity log endpoint summary

| Task | Endpoint |
| --- | --- |
| Retrieve detail for an activity log entry by `ActivityLogId`. | GET /v3/activity/{activityLogId} |
| Retrieve a summary of changed properties and usernames responsible for the changes within a date range for the specified ad group. These can be used to filter information in the POST /v3/activity/query/adgroup endpoint. | POST /v3/activity/query/facets |
| Retrieve and optionally filter a paged list of activity log entries for the specified ad group. | POST /v3/activity/query/adgroup |
| Create or update the note for an activity log entry. | PUT /v3/activity |
| Retrieve activity log changes since the last change version for the specified ad group. | POST /v3/delta/activity/query/adgroup |

## Filter activity log information

Activity log information is filterable based on what, when, where, and how data was changed. The following sections highlight filtering capabilities and while they are broken out into separate sections, they can all be used together for a comprehensive filtering strategy.

### Filter by what changed

1. Use the POST /v3/activity/query/facets endpoint to generate a summary of all of the grouped `Entities` changed in the activity log for a specific ad group.
2. Use available `Entities` from step 1 to filter on changes using the `UpdatedIn` filter in the POST /v3/activity/query/adgroup call.

The table below details logged activity types, their messaging, and what `Entity` / `UpdatedIn` value they roll up into. The `UpdatedIn` value can be used for filtering.

Here's the HTML table converted to Markdown format:

| Logged Activity | Entity / Updated In | API Property | Message |
| --- | --- | --- | --- |
| The ad group was enabled or disabled. | Ad Group | `AdGroup.IsEnabled` | The ad group was `enabled/disabled`. |
| Remove all audience targeting. | Audience | `RTBAttributes.AudienceTargeting` | Audience type changed from `AudienceTypeFrom` to `Target Everyone`. |
| Prism was enabled or disabled for the ad group. | Audience | `RTBAttributes.AudienceTargeting.AudienceExcluderEnabled` | Prism was `enabled/disabled`. |
| An custom audience ID was assigned to the ad group that is not associated to Koa targeting. | Audience | `RTBAttributes.AudienceTargeting.AudienceId` | Audience type changed to `DataGroup.Name`. |
| The audience type changed to Koa retargeting. | Audience | `RTBAttributes.AudienceTargeting.AudienceRetargetingEnabled` | Audience type changed to `AudienceTypeTo`. |
| The audience type changed to Koa Audience Predictor. | Audience | `RTBAttributes.AudienceTargeting.AudiencePredictorEnabled` | Audience type changed to `AudienceTypeTo`. |
| The audience type changed to use Koa Demographic Targeting. | Audience | `RTBAttributes.AudienceTargeting.DemographicTargeting` | Audience type changed to `Automated Demographic Targeting`. |
| The audience type changed to use Koa Interest Targeting. | Audience | `RTBAttributes.AudienceTargeting.InterestTargeting` | Audience type changed to `Interest Targeting`. |
| Target only trackable users was enabled for audience targeting on the ad group. | Audience | `RTBAttributes.AudienceTargeting.TargetTrackableUsersEnabled` | Audience type changed from `Target Everyone` to `Target Trackable Users`. |
| A cross-device vendor was set for the ad group. | Audience | `RTBAttributes.AudienceTargeting.CrossDeviceVendorListForAudience` | Started using cross device vendor `CrossDeviceVendorTo`. |
| The cross-device vendor changed for the ad group. | Audience | `RTBAttributes.AudienceTargeting.CrossDeviceVendorListForAudience` | Cross device vendor changed from `CrossDeviceVendorFrom` to `CrossDeviceVendorTo`. |
| The cross-device vendor was removed from the ad group. | Audience | `RTBAttributes.AudienceTargeting.CrossDeviceVendorListForAudience` | Cross device vendor was stopped. |
| The ad group's pacing mode was changed. | Budget and Goals | `RTBAttributes.BudgetSettings.PacingMode` | Pacing changed to `PacingNameTo` from `PacingNameFrom`. |
| The ad group's goal was changed and the goal doesn't have a numeric value. (MaximizeReach, MaximizeLtvIncrementalReach) | Budget and Goals | `RTBAttributes.ROIGoal` | Goal type changed from `GoalTypeFrom` to `GoalTypeTo`. |
| The ad group's goal was changed and the goal has a numeric value. | Budget and Goals | `RTBAttributes.ROIGoal` | Goal type changed to `GoalTypeTo` with a goal of `GoalTypeValueTo`. |
| The ad group goal's value was changed. (Does not apply to MaximizeReach or MaximizeLtvIncrementalReach.) | Budget and Goals | `RTBAttributes.ROIGoal` | Goal value changed from `GoalValueFrom` to `GoalValueTo`. |
| The ad group set or changed a base bid CPM. | Base/Max Bid | `RTBAttributes.BudgetSettings.BaseBidCPM` | The base bid changed to `BaseBidValueTo` from `BaseBidValueFrom`. |
| The ad group set or changed a max bid CPM. | Base/Max Bi. | `RTBAttributes.BudgetSettings.MaxBidCPM` | The maximum bid changed to `MaxBidValueTo` from `MaxBidValueFrom`. |
| An ad group flight's budget was set. | Flight Budget | `RTBAttributes.BudgetSettings.AdGroupFlights.BudgetInAdvertiserCurrency` | Flight budget set to `BudgetValueTo`. |
| An ad group flight's budget was changed. | Flight Budget | `RTBAttributes.BudgetSettings.AdGroupFlights.BudgetInAdvertiserCurrency` | Flight budget changed from `BudgetValueFrom` to `BudgetValueTo`. |
| An ad group flight's impression budget was set. | Flight Budget | `RTBAttributes.BudgetSettings.AdGroupFlights.BudgetInImpressions` | Flight impression budget set to `ImpressionBudgetTo`. |
| An ad group's flight impression budget was changed. | Flight Budget | `RTBAttributes.BudgetSettings.AdGroupFlights.BudgetInImpressions` | Flight impression budget changed from `ImpressionBudgetFrom` to `ImpressionBudgetTo`. |
| An ad group flight's daily target was changed. | Flight Budget | `RTBAttributes.BudgetSettings.AdGroupFlights.DailyTargetInAdvertiserCurrency` | Flight daily target changed to `DailyTargetTo` from `DailyTargetFrom`. |
| An ad group flight's daily impression target was changed. | Flight Budget | `RTBAttributes.BudgetSettings.AdGroupFlights.DailyTargetInImpressions` | An ad group flight's daily impression budget changed from `DailyBudgetFrom` to `DailyBudgetTo`. |
| The ad group's contract targeting market type was added. | Private Contract | `RTBAttributes.ContractTargeting.AllowOpenMarketWhenTargetingContracts` | Market type set to `MarketTypeTo`. |
| The ad group's contract targeting market type was changed. | Private Contract | `RTBAttributes.ContractTargeting.AllowOpenMarketWhenTargetingContracts` | Market type changed from `MarketTypeFrom` to `MarketTypeTo`. |
| A Koa optimization was turned on or off for an ad group dimension. | Koa Optimizations | `AssociatedBidLists.BidListId` | `BidLine.DimensionName` Koa optimization was turned `on/off`. |
| A bid list was added to the ad group's associated bid lists. | See dimension enumeration | `AssociatedBidLists.BidListId` | `BidListNameType` was added. |
| A bid list was disassociated from the ad group. | See dimension enumeration | `AssociatedBidLists.BidListId` | `BidListNameType` was disassociated from the ad group. |
| A bid line's bid adjustment was changed. | See dimension enumeration | `AssociatedBidLists.BidListId - BidList.BidLines.BidAdjustment` | `numberOfChangedItem`, `BidListNameType` items had their bid adjusted. |
| A bid line was removed from the bid list. | See dimension enumeration | `AssociatedBidLists.BidListId - BidList.BidLines.BidAdjustment` | `numberOfChangedItem` were removed from `BidListNameType`. |
| The bid list was enabled or disabled in an ad group's associated bid lists. | See dimension enumeration | `AssociatedBidLists.IsEnabled` | `BidListNameType` was `Enabled/Disabled`. |

### Dimension enumeration

You can look up bid list dimensions in the `BidLines` property in POST /v3/bidlist endpoint documentation. All of the properties listed are dimensions, except for `BidAdjustment` and `VolumeControlPriority`.

### Filter by when the change was made

In the POST /v3/activity/query/adgroup call, use `DateTimeStartUtc` and `DateTimeEndUtc` to filter by the timeframe the change was made.

| Property | Required | Default value | Inclusive / Exclusive |
| --- | --- | --- | --- |
| `DateTimeStartUtc` | Yes | - | Inclusive |
| `DateTimeEndUtc` | No | Now | Inclusive |

### Filter by where the change was made

To filter by where a user made a change, use the `Source` filter in the POST /v3/activity/query/adgroup endpoint.

The following is a list of the value enumerations and what they indicate.

| Value | Description |
| --- | --- |
| `Ui` | A user logged into the platform user interface (UI) made the change. `UpdatedBy` will tell you the user who made the change. |
| `Api` | This change was made by a user executing an API call. `UpdatedBy` will tell you the user who made the change. |
| `Other` | This change was made by Koa or our support team. `UpdatedBy` will display `Koa` as the value if Koa made the change, or `TTD Admin` if our system or support team made the change. |
| `Unknown` | The source of this change was unable to be tracked. Rarely occurs. |

### Filter by who made the change

1. Use the POST /v3/activity/query/facets endpoint to generate an `UpdatedBy` list of users who changed information for the specified ad group.
2. Use available `UpdatedBy` from step 1 to filter on changes using the `UpdatedBy` filter in the POST /v3/activity/query/adgroup call.

### Usernames for activity logs with `source` - `other`

| Username | Description |
| --- | --- |
| `Koa` | This username indicates Koa made changes to optimize the ad group. |
| `TTD Admin` | This username indicates our system or support team made a change. |

## Create or update an activity log note

Use the `Note` property to store any additional information you would like to keep with the activity log.

Here's a PUT /v3/activity request example.

```
{
	"Id": 1234567,
	"Note": "This is a system-applied Koa optimization."
}
```

Here's a PUT /v3/activity response example.

```
{
    "Id": 1234567,
    "OwnerAdGroupId": "h3jz8t5",
    "ActivityRollupTimeUtc": "2020-04-15T18:15:00",
    "ActivityTimeUtc": "2020-04-15T18:18:05.473",
    "Message": "Site/App Koa optimization was turned on.",
    "Entity": "Ad Group",
    "Note": "This is a system-applied Koa optimization.",
    "ModifiedByUser": "Koa",
    "HasBidListChanges": false,
    "BidLineChanges": null,
    "Source": "Other"
}
```

## Monitor activity log changes

 Create an efficient integration by using the activity log delta endpoint to only process activity logs for an ad group that were created since the last time the endpoint was called.

The first time you request activity logs from the delta endpoint, the response will return the `LastChangeTrackingVersion`.

Cache this information and on subsequent calls to the endpoint, provide the most recent `LastChangeTrackingVersion`. Including `LastChangeTrackingVersion` with the request will allow the endpoint to retrieve the activity log specified in the `LastChangeTrackingVersion` and all newer activity logs.

### First delta call

Here's a POST /v3/delta/activity/query/adgroup request example.

```
{
	"AdGroupId": "h3jz8t5",
	"ReturnEntireActivity": true,
	"IncludeBidLineDetails": false,
	"LastChangeTrackingVersion": null
}
```

Here's a POST /v3/delta/activity/query/adgroup response example.

Cache the `LastChangeTrackingVersion` to use in the request of the next call. The `LastChangeTrackingVersion` is the same as the most recent activity log `Id` returned.

```
{
    "ActivityLogs": null,
    "MoreActivityLogsAvailable": true,
    "ElementIds": null,
    "LastChangeTrackingVersion": 145070029
}
```

### Subsequent delta call

Here's a POST /v3/delta/activity/query/adgroup request example.

Send the cached `LastChangeTrackingVersion` in the request.

```
{
	"AdGroupId": "h3jz8t5",
	"ReturnEntireActivity": true,
	"IncludeBidLineDetails": false,
	"LastChangeTrackingVersion": 145070029
}
```

Here's a POST /v3/delta/activity/query/adgroup response example.

Cache the requested information and the `LastChangeTrackingVersion` to use in the request of the next call.

```
{
    "ActivityLogs": [
        {
            "Id": 145070029,
            "OwnerAdGroupId": "h3jz8t5",
            "ActivityRollupTimeUtc": "2020-04-15T18:15:00",
            "ActivityTimeUtc": "2020-04-15T18:18:06.55",
            "Message": "1 item was targeted in the Private Contract rail.",
            "Entity": "Private Contract",
            "Note": null,
            "ModifiedByUser": "user@example.com",
            "HasBidListChanges": true,
            "BidLineChanges": null,
            "Source": "Ui"
        },
        {
            "Id": 145070448,
            "OwnerAdGroupId": "h3jz8t5",
            "ActivityRollupTimeUtc": "2020-04-15T18:15:00",
            "ActivityTimeUtc": "2020-04-15T18:18:05.473",
            "Message": "The ad group was enabled.",
            "Entity": "Ad Group",
            "Note": null,
            "ModifiedByUser": "user@example.com",
            "HasBidListChanges": false,
            "BidLineChanges": null,
            "Source": "Ui"
        },
        {
            "Id": 145071661,
            "OwnerAdGroupId": "h3jz8t5",
            "ActivityRollupTimeUtc": "2020-04-15T18:15:00",
            "ActivityTimeUtc": "2020-04-15T18:18:06.647",
            "Message": "Private Contract target rail was added.",
            "Entity": "Private Contract",
            "Note": null,
            "ModifiedByUser": "user@example.com",
            "HasBidListChanges": false,
            "BidLineChanges": null,
            "Source": "Ui"
        }
    ],
    "MoreActivityLogsAvailable": false,
    "ElementIds": null,
    "LastChangeTrackingVersion": 145071661
}
```

## FAQs

The following is a list of commonly asked questions about the activity log.

### What does Stack Ranking Enabled mean?

This is a Solimar feature. In a POST/activity/query/campaign response, the `Stack Ranking Enabled` message means that a campaign has both `AutoAllocatorEnabled` and `AutoPrioritizationEnabled` set to `true`.
