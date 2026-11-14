# Koa Optimizations

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/KoaOptimizations
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/KoaOptimizations (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Koa Optimizations

> **IMPORTANT**: This page provides guidance on using the latest version of Koa Optimizations. If you're using the previous version, see Koa Optimizations (legacy).

Koa is the artificial intelligence that powers The Trade Desk platform. It automatically generates optimizations, sets of bid dimensions and adjustments applied to ad groups to enhance the performance of your advertising campaigns. Applied optimizations are collected in bid lists.

Koa Optimizations, a machine-learning algorithm, works to achieve your goals by prioritizing spend on better-performing inventory and de-prioritizing spend on worse-performing inventory, using bid adjustments. The latest version of Koa Optimizations offers dimension-level granularity, providing greater confidence, control, and flexibility.

Koa evaluates each targeting dimension and expresses its findings as bid factors—a transparent view of how the AI values each dimension on average. Any inputs you add take precedence over Koa's evaluation. Koa treats them as fixed and will never override them, so you stay in control of the decisions that are yours to make.

## What you need to know

There are some key differences between the latest version of Koa Optimizations and the legacy version, shown in the following table.

| Comparison Aspect | Latest Version | Legacy Version |
| --- | --- | --- |
| Behavior and configuration | Always on, read-only. | Manually configured as needed. |
| Default state | On | Off |
| Supported dimensions | - Existing: `AdEnvironment`, `AdFormat`, `Browser`, `DeviceType`, `Geography`, `OS` - New: `DeviceMakeAndModel`, `InternetConnectionType`, `Publisher` - Deprecated: `FoldPlacement`, `Site` (both always return `false`) | `AdEnvironment`, `AdFormat`, `Browser`, `DeviceType`, `FoldPlacement`, `Geography`, `OS`, `Site` |
| Ability to turn off dimensions | Dimensions are always on and are read-only. | Any dimension can be disabled manually. |

> **IMPORTANT**: You can manually set bid adjustments on your bid lists using the bidding API; however, Koa is turned off for all grains that have manual bid adjustments. For example, in `Geography`, if you override NY, Koa is turned off for NY but not for other regions.

## The KoaDimensions object

You can view a read-only representation of the bid dimensions in the `AdGroup.RTBAttributes.KoaOptimizationSettings.KoaDimensions` object returned by any of the ad group endpoints. However, the set of values in this object represents the legacy values. The `KoaDimensions` object includes the deprecated dimensions `FoldPlacement` and `Site`, both set to `false`, and does not include the new `DeviceMakeAndModel`, `InternetConnectionType`, and `Publisher` values.

## Retrieve optimizations applied by Koa

To get the list of optimizations that Koa has currently applied to an ad group, in a GET /v3/adgroup/koaapplieditems/{adGroupId} call, specify the ad group ID as the path parameter.

Here's an example of a GET /v3/adgroup/koaapplieditems/{adGroupId} response, which includes a list of applied optimizations with the applied `BidAdjustment` values. Note that the rest of the properties, such as `PotentialImpact`, `VolumeControlPriority`, and `KoaOptimizationId`, are included only for backward compatibility.

```
{
    "PotentialImpact": {
        "GoalPerformancePercent": 23.0,
        "IsGoalImprovement": true,
        "SpendPercent": 0.0,
        "GeneratedOn": "2025-11-26T04:40:44.127"
    },
    "Optimizations": [
        {
            "DimensionValues": {
                "HasDomainFragmentId": "nbc.com"
            },
            "VolumeControlPriority": "Neutral",
            "BidAdjustment": 2.0000,
            "KoaOptimizationId": 25
        },
        {
            "DimensionValues": {
                "HasDomainFragmentId": "abc.com"
            },
            "VolumeControlPriority": "Neutral",
            "BidAdjustment": 1.5000,
            "KoaOptimizationId": 26
        },
        {
            "DimensionValues": {
                "HasAdFormatId": "Micro Bar (88x31)"
            },
            "VolumeControlPriority": "One",
            "BidAdjustment": 2.0000,
            "KoaOptimizationId": 16
        },
        {
            "DimensionValues": {
                "HasDeviceTypeId": "Digital Out Of Home"
            },
            "VolumeControlPriority": "Neutral",
            "BidAdjustment": 1.2500,
            "KoaOptimizationId": 27
        },
        {
            "DimensionValues": {
                "HasGeoSegmentId": "USA"
            },
            "VolumeControlPriority": "Neutral",
            "BidAdjustment": 1.7500,
            "KoaOptimizationId": 28
        },
        {
            "DimensionValues": {
                "HasDeviceTypeId": "Roku"
            },
            "VolumeControlPriority": "Neutral",
            "BidAdjustment": 1.7500,
            "KoaOptimizationId": 29
        }
    ],
    "UpdateAttemptDetails": {
        "NoOptimizationsReasonId": "NotEnoughKpiEvents",
    },
    "OptimizationMode": "None",
    "IncompatibleFeatures": [
        "PacingASAP"
    ]
}
```

## FAQs

The following is a list of commonly asked questions about Koa Optimizations.

### What's the difference between Koa bidding strategy and Koa Optimizations?

Koa bidding strategy operates at the campaign level while Koa Optimizations works at the ad group level. Koa bidding strategy specifies how Koa balances performance, delivery, and CPM efficiency across your campaign. Koa Optimizations is the bid factors that Koa automatically generates based on the bidding strategy you set, the decision power score, the inventory you're targeting, and other campaign signals.

### Why is Koa now always on instead of opt-in?

The latest version of Koa represents the whole bidding system, which offers more transparency in terms of what the system is doing, and if needed you can adjust bidding. Always-on Koa drives consistent improvement toward campaign goals, helping you benefit from the advanced Koa algorithms.

### How often does Koa generate and apply optimizations?

Approximately every two days.

### Do I have to do anything to migrate to the latest version of Koa Optimizations?

No, you don't have to do anything. The latest version will be used for new campaigns.

### Do I need to update my API calls when migrating from the legacy version?

No, you don't have to do anything. The new version is implemented automatically, and you don't have to make any adjustments to your Koa integrations because this is a read-only.

### What happens to my existing bid adjustments when I migrate?

Existing bid adjustments are treated as manual overrides.

### Can I go back to the legacy version?

No. The version in use is always the latest version.

### What new dimensions were added in the latest version?

The new dimensions are `InternetConnectionType`, `DeviceMakeAndModel`, and `Publisher` (which has replaced `Site`).

### Can I disable individual dimensions?

Dimensions are read-only. You cannot disable them.

### If Koa is always on, how do I prevent it from adjusting a dimension I want to control manually?

If needed, you can manually set bid adjustments on your bid lists using the bidding API; however, if you do that, anything you set manually is no longer tracked by Koa.

Only specify bid adjustments manually for dimensions where you're 100% sure of exactly what you want. We recommend you leave the rest to Koa.

### Why do deprecated dimensions return false instead of being removed entirely?

Deprecated dimensions are still included for backward compatibility. In the longer term they will be removed entirely.

### Why are PotentialImpact, VolumeControlPriority, and KoaOptimizationId still in the response if they're only for backward compatibility? Will they be removed?

These values are included to support instances where an earlier version of Koa Optimizations is still in use. At some point in the future they will be removed.
