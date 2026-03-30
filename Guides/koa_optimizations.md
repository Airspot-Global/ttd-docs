# Koa Optimizations

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/KoaOptimizations
- Category: Guides

---

# Koa Optimizations

> **IMPORTANT**: This documentation explains how to use the Koa v3.5 API in Kokai. For details on using the Koa v3 API in Solimar, see [Koa Optimizations (Solimar)](/v3/portal/api/doc/SolimarKoaOptimizations).

Optimizations are sets of bid dimensions and adjustments applied to ad groups to enhance the performance of your advertising campaigns. You can apply these optimizations manually or use Koa, the artificial intelligence that powers The Trade Desk platform, to generate them automatically. Applied optimizations are collected in bid lists.

Koa Optimizations is a machine-learning algorithm that works to achieve your goals by prioritizing spend on better-performing inventory and de-prioritizing spend on worse-performing inventory, using bid adjustments. In Kokai, the new Koa Optimizations feature offers dimension-level granularity, providing greater confidence, control, and flexibility.

Here's what you need to know about Koa Optimizations:

*   Koa Optimizations is off by default.
*   You can turn on Koa Optimizations for any combination of bid dimensions in ad groups while managing the remaining dimensions manually as needed.
*   When Koa Optimizations is on, Koa reviews ad group performance and automatically applies optimizations to the specified dimensions, approximately every two days.
*   If you manually apply bid adjustments to dimensions with Koa Optimizations enabled, both Koa-generated and user-created bid lists will be respected in the API. This is different from the UI where users must disable Koa Optimizations before manually applying bid adjustments to those dimensions.
*   For backward compatibility, the Koa v3 (Solimar) properties are returned in responses for Kokai ad groups. See also [FAQs](#faqs).

> **IMPORTANT**: You must use only the new Koa v3.5 properties (`KoaDimensions`) to manage Koa Optimizations in Kokai. Using the Koa v3 properties can lead to a more complex integration and a degraded user experience.

## 

Supported Bid Dimensions[](#supported-dimensions)

The latest version of Koa Optimizations gives you singular control over the following eight bid dimensions: Ad Format, Geography, Site, Ad Environment, Device Type, Browser, OS, Fold Placement. Each dimension is represented by a Boolean value in the `RTBAttributes.KoaOptimizationSettings.KoaDimensions` object, which you can use to turn on or off the respective dimension when creating or updating ad groups. For example:

{

   "KoaDimensions": {

      "AdFormat": true,

      "Geography": true,

      "Site": true,

      "AdEnvironment": false,

      "DeviceType": true,

      "Browser": false,

      "OS": true,

      "FoldPlacement": true

   }

}

For details, see [Managing Koa Optimizations](#manage).

## 

Checking Potential Impact of Koa Optimizations[](#potential-impact)

To help you stay informed and adapt to changes that Koa applies, the [GET /v3/adgroup/koaapplieditems/{adGroupId}](/v3/portal/api/ref/get-adgroup-koaapplieditems-adgroupid) endpoint returns a `PotentialImpact` object, which includes the information on how optimizations recommended by Koa benefit the specified ad group and affect its goal performance and potential spend.

The following table explains the potential impact data.

| Parameter | Description |
| `GoalPerformancePercent` | The expected percentage change in goal performance. |
| `IsGoalImprovement` | Indicates whether the `GoalPerformancePercent` value is a goal improvement. |
| `SpendPercent` | The percentage change impact that Koa expects the recommended optimizations to have on potential spend. When using Koa v3.5 this value will always be zero. |
| `GeneratedOn` | The date when the `PotentialImpact` data was generated. |

Any features, user settings, or ad group performance data that may be negatively affecting Koa's ability to generate optimal strategies are indicated in the `UpdateAttemptDetails` and `IncompatibleFeatures` properties of the [GET /v3/adgroup/koaapplieditems/{adGroupId}](/v3/portal/api/ref/get-adgroup-koaapplieditems-adgroupid). For an example, see [Retrieve Applied Koa Optimizations](#get-applied-optimizations).

## 

Managing Koa Optimizations[](#manage)

The following table lists all tasks that you might need to perform when managing optimizations applied or recommended by Koa.

| Task | Endpoint | Notes |
| [Verify](#Koa-version-verify) the Koa Optimizations API version. | [GET/adgroup/{adGroupId}](/v3/portal/api/ref/get-adgroup-adgroupid) | Check the value of `KoaOptimizationsVersion` property value. |
| [Turn on](#turn-on) Koa Optimizations for specified bid dimensions. | [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup)  
[PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) | **IMPORTANT**: To avoid unintended complex integrations and degraded experience, do not use the Koa v3 properties such as `IsEnabled` and `OptionalDimensions` to manage the Koa Optimizations settings, even if they are returned in responses for backward compatibility. Instead, use only the `KoaDimensions` object. |
| [Retrieve applied optimizations](#get-applied-optimizations) for an ad group. | [GET /v3/adgroup/koaapplieditems/{adGroupId}](/v3/portal/api/ref/get-adgroup-koaapplieditems-adgroupid) | Use the returned `PotentialImpact` object to [interpret the benefits](#potential-impact) of the applied optimizations. |
| [Turn off](#turn-off) Koa Optimizations for an entire ad group or specified bid dimensions. | [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup)  
[PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) | **IMPORTANT**: To avoid unintended complex integrations and degraded experience, do not use the Koa v3 properties such as `IsEnabled` and `OptionalDimensions` to manage the Koa Optimizations settings, even if they are returned in responses for backward compatibility. Instead, use only the `KoaDimensions` object. |

### 

Verify the Koa Optimizations Version[](#Koa-version-verify)

You may not apply different Koa Optimizations version settings, such as v3 and v3.5 settings. Koa endpoints return an error when there is a version mismatch. To confirm the Koa version and to use the correct APIs, check the value of the `KoaOptimizationsVersion` and `KoaOptimizationsMinorVersion` properties in your ad groups. For example, a [GET/adgroup/{adGroupId}](/v3/portal/api/ref/get-adgroup-adgroupid) call might return the following response.

{

   "AdGroupId":"cbgb9681",

   "RTBAttributes":{

      "KoaOptimizationSettings":{

         "KoaDimensions":{

            "AdFormat": true,

            "Geography": true,

            "Site": true,

            "AdEnvironment": false,

            "DeviceType": true,

            "Browser": false,

            "OS": true,

            "FoldPlacement": true

         },

         "IsEnabled":true,

         "OptionalDimensions":\[

            "HasAdFormatId",

            "HasGeoSegmentId"

         \],

         "IsBiddingUpEnabled":true

      },

      "KoaOptimizationsVersion":"V3",

      "KoaOptimizationsMinorVersion": "5"

   }

}

Note that the sample response also includes the Koa v3 properties, such as `IsEnabled`, `OptionalDimensions`, and `IsBiddingUpEnabled`, for backward compatibility.

`KoaOptimizationsVersion` and `KoaOptimizationsMinorVersion` are read-only properties that in conjunction indicate the version of Koa used to apply optimizations, if there are any, to the ad group. The following table explains their values.

| Koa Optimizations Version Value | Koa Optimizations Minor Version Value | Description |
| None | None | The ad group is not using Koa for optimizations. |
| `V3` | `0` | The ad group is using Koa version 3 for optimizations. See [Koa Optimizations (Solimar)](/v3/portal/api/doc/KoaOptimizations) for the Solimar experience. |
| `V3` | `5` | The ad group is using Koa version 3.5 for optimizations. Continue using this documentation. |

### 

Turn On Koa Optimizations[](#turn-on)

> **IMPORTANT**: You must use only the new Koa v3.5 properties (`KoaDimensions`) to manage Koa Optimizations in Kokai. Using the Koa v3 properties can lead to a more complex integration and a degraded user experience.

Here's what you need to know about the `KoaDimensions` property when creating or updating an ad group in Kokai:

*   Each dimension is represented by a Boolean value. To turn on Koa Optimizations for a dimension, set its value to `true`.
*   To turn off Koa Optimizations for a dimension, set its to `false` or omit it from the list. See also [Turn Off Koa Optimizations](#turn-off).
*   If you omit the entire object in your request, all optional dimensions will be disabled.

To apply Koa Optimizations to an ad group, in a [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) or [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) request, in `KoaOptimizationSettings`object, include the `KoaDimensions` with the properties of bid dimensions that you want optimized set to `true`.

{

   "AdGroupId":"cbgb9681",

   "RTBAttributes":{

      "KoaOptimizationSettings":{

         "KoaDimensions":{

            "AdFormat": true,

            "Geography": true,

            "AdEnvironment": false,

            "DeviceType": true,

            "Browser": false,

            "OS": true,

            "FoldPlacement": true

         }

      }

   }

}

### 

Retrieve Applied Koa Optimizations[](#get-applied-optimizations)

To get the list of Koa optimizations currently applied to an ad group, in a [GET /v3/adgroup/koaapplieditems/{adGroupId}](/v3/portal/api/ref/get-adgroup-koaapplieditems-adgroupid) call, specify the ad group ID as the path parameter.

Here's an example of a [GET /v3/adgroup/koaapplieditems/{adGroupId}](/v3/portal/api/ref/get-adgroup-koaapplieditems-adgroupid) response, which includes a list of applied optimizations as well as the details about the latest update attempt and any features or user settings (`IncompatibleFeatures`) that may have affected the generation of optimal strategies.

{

    "PotentialImpact": {

        "GoalPerformancePercent": 23.0,

        "IsGoalImprovement": true,

        "SpendPercent": 0.0,

        "GeneratedOn": "2024-04-26T04:40:44.127"

    },

    "Optimizations": \[

        {

            "DimensionValues": {

                "HasDomainFragmentId": "nbc.com"

            },

            "VolumeControlPriority": "Neutral",

            "BidAdjustment": 2.0000,

            "KoaOptimizationId": 25

        },

        {

            "DimensionValues": {

                "HasDomainFragmentId": "abc.com"

            },

            "VolumeControlPriority": "Neutral",

            "BidAdjustment": 1.5000,

            "KoaOptimizationId": 26

        },

        {

            "DimensionValues": {

                "HasAdFormatId": "Micro Bar (88x31)"

            },

            "VolumeControlPriority": "One",

            "BidAdjustment": 2.0000,

            "KoaOptimizationId": 16

        },

        {

            "DimensionValues": {

                "HasDeviceTypeId": "Digital Out Of Home"

            },

            "VolumeControlPriority": "Neutral",

            "BidAdjustment": 1.2500,

            "KoaOptimizationId": 27

        },

        {

            "DimensionValues": {

                "HasGeoSegmentId": "USA"

            },

            "VolumeControlPriority": "Neutral",

            "BidAdjustment": 1.7500,

            "KoaOptimizationId": 28

        },

        {

            "DimensionValues": {

                "HasDeviceTypeId": "Roku"

            },

            "VolumeControlPriority": "Neutral",

            "BidAdjustment": 1.7500,

            "KoaOptimizationId": 29

        }

    \],

    "UpdateAttemptDetails": {

        "NoOptimizationsReasonId": "NotEnoughKpiEvents", 

    },   

    "OptimizationMode": "None",

    "IncompatibleFeatures": \[

        "PacingASAP"

    \]

}

### 

Turn Off Koa Optimizations[](#turn-off)

To turn off Koa Optimizations for all dimensions in an ad group, in a [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) or [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) request, include an empty `KoaOptimizationSettings` object, as shown in the following example.

{

   "AdGroupId":"cbgb9681",

   "RTBAttributes":{

      "KoaOptimizationSettings":{

      }

   }

}

> **TIP**: To turn off Koa Optimizations for specific dimensions in an ad group, in the `KoaDimensions` object, set dimensions for which you want to turn off Koa Optimizations to `false` or omit them from the list.

The following examples show an ad group in which Koa Optimizations is turned off for all dimensions, except Geography.

{

   "AdGroupId":"cbgb9681",

   "RTBAttributes":{

      "KoaOptimizationSettings":{

         "KoaDimensions":{

            "AdFormat": false,

            "Geography": true,

            "Site": false,

            "AdEnvironment": false,

            "DeviceType": false,

            "Browser": false,

            "OS": false,

            "FoldPlacement": false

         }

      }

   }

}

{

   "AdGroupId":"cbgb9681",

   "RTBAttributes":{

      "KoaOptimizationSettings":{

         "KoaDimensions":{

            "Geography":true

         }

      }

   }

}

## 

FAQs[](#faqs)

The following is a list of commonly asked questions about Koa Optimizations.

### 

How can I tell if Koa Optimizations is on for an ad group?

In Kokai, Koa Optimizations settings are configured at the dimension level rather than the ad group level. To check if the Koa Optimizations is enabled for any dimensions, query the ad group and check if the `RTBAttributes.KoaOptimizationSettings.KoaDimensions` object is present. For details, see [Turn On Koa Optimizations](#turn-on).

### 

If Koa is off by default, does that mean that my campaigns are not being optimized?

In Kokai, Koa functions as an augmentative, optional feature. To direct volume and bids toward inventory most likely to drive your ad group KPIs, you can apply optimizations manually or use Koa to generate them automatically. This is in addition to the platform's algorithms that automatically optimize your campaigns.

### 

What happens if I omit a dimension from the KoaDimensions object in my request?

Whichever dimensions you exclude from the `KoaDimensions` object, Koa Optimizations will be turned off for those dimensions. If you pass an empty `KoaDimensions` object, Koa Optimizations will be turned off for all dimensions in the ad group. For more details and examples, see [Turn Off Koa Optimizations](#turn-off).

### 

What happens if I omit the KoaDimensions or KoaOptimizationSettings objects from my request?

For most advertisers, if you exclude the `KoaDimensions` or `KoaOptimizationSettings` objects from your request, Koa Optimizations will automatically be disabled for all ad group dimensions. However, for advertisers in certain industries—such as Careers, Medical Health, Personal Finance, and Real Estate—Koa Optimizations will be enabled by default for all dimensions except `Site`.

### 

I thought Koa Optimizations was off by default for newly created ad groups. Why do I see it enabled?

While Koa Optimizations is off by default for new ad groups, there is an exception for certain industries. If a new ad group belongs to certain categories like Careers, Medical Health, Personal Finance, or Real Estate, Koa Optimizations is automatically enabled for all dimensions except `Site`. This is part of the platform's default behavior to optimize for specific advertiser categories in different geographies.

### 

Can I check how effective optimizations are?

You can check the expected, not actual, impact of Koa Optimizations on ad group goal performance and potential spend at any time. For details, see [Checking Potential Impact of Koa Optimizations](#potential-impact).

### 

How often does Koa generate and apply optimizations?

Approximately every two days.

### 

Which Koa properties are intended to be used only in Solimar?

The Koa v3 properties intended to be used to manage [Koa Optimizations only in Solimar](/v3/portal/api/doc/SolimarKoaOptimizations) include the following:

*   `IsEnabled`
*   `OptionalDimensions`
*   `IsBiddingUpEnabled`

> **IMPORTANT**: To manage Koa Optimizations in Kokai, you must use only the new Koa v3.5 properties (`KoaDimensions`). Using the Koa v3 properties can lead to a more complex integration and a degraded user experience.

### 

Can I use the IsEnabled property to turn Koa Optimizations on and off in Kokai?

No. The `IsEnabled` is a Koa v3 property not intended to be used in Kokai. To turn on and off Koa Optimizations in Kokai and to avoid confusion, be sure to use only the `KoaDimensions` object. For details, see [Managing Koa Optimizations](#manage).

### 

What's the difference between the OptionalDimensions and KoaDimensions objects?

The following table summarizes the differences between the two objects.

| Property | Experience | Koa Version | Notes |
| `KoaDimensions` | Kokai | v3.5 | This property enables you to turn on and off Koa Optimizations for all supported bid dimensions in Kokai. |
| `OptionalDimensions` | Solimar | v3 | This property enables you to turn on Koa Optimizations only for the Ad Format and Geography bid dimensions that are optional in Solimar. |

> **IMPORTANT**: To avoid confusion and unintended optimizations, use only the `KoaDimensions` object in Kokai.

### 

What happens to the Koa Optimizations settings after Solimar campaigns are upgraded to Kokai?

By default, during the upgrade, all campaigns are upgraded to Koa v3.5 and Koa Optimizations is turned off. For details, see [Upgrade Solimar Campaigns to Kokai](/v3/portal/api/doc/KokaiCampaignUpgrade). The only exception is the campaigns with sensitive categories. For those campaigns, the following changes apply:

*   If _all_ dimensions were off in Solimar, we turn on all dimensions except for the Site dimension.
*   If only _some_ dimensions were on in Solimar, we keep these settings on and turn off only the Site dimension if it was on.

### 

Can I use GraphQL to turn on Koa Optimizations?

Not yet. We're actively expanding GraphQL API capabilities by delivering new features incrementally. We encourage you to check for [updates](/v3/portal/api/doc/ReleaseNotes) as we roll out new functionality and enhancements. We greatly appreciate your patience and feedback as we continue to improve your experience.