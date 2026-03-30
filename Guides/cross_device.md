# Cross-Device Targeting

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/CrossDeviceTargeting
- Category: Guides

---

# Cross-Device Targeting

Cross-device targeting enables you to scale your high-value audiences across devices and environments. It works in tandem with [frequency](/v3/portal/api/doc/Frequency) capping to limit the number of times a user sees an ad across all of their devices, not just the device on which they first saw the ad.

> **TIP**: For cross-device targeting, The Trade Desk recommends using Identity Alliance.

Identity Alliance is a performance-enhancing feature that enables you to make the most of cross-device targeting. Identity Alliance combines all available cross-device vendors into a single graph. With this unified graph, your targeting works from a more complete picture of each user's devices for each impression. Using Identity Alliance as your cross-device solution allows for expanded reach, better frequency management, improved attribution, and more accurate measurement across channels.

### 

Cross-Device Targeting Example[](#example)

Identity Alliance maps connections between users and their devices across the device graphs of industry-leading cross-device vendors. For example, the following image illustrates how three vendors A, B, and C might be linked differently to the devices of users 1, 2, and 3 in the same household.

![Cross-Device Targeting Diagram](/v3/content/docs/Images/identity-alliance.svg)

For a given member of your audience, Vendor A might have the link from their PC to their mobile phone, while Vendor B might have the link from their PC to their tablet. If you target this user with only one vendor, you would lose out on one of these connections—you either wouldn't be able to make the connection between the PC and the mobile phone (if you used Vendor A) or between the PC and the tablet (if you used Vendor B).

You could also spend more than you intend to on User 1, because without the connection between all of User 1's devices, each device is subject to its own frequency cap. With a frequency cap of 3 per day, for example, instead of User 1 seeing three ads per day across all of their devices they may instead see three ads each on their PC, mobile phone, and tablet, leading to six excess impressions.

With the unified graph that Identity Alliance offers, your targeting works from a more complete picture of each user's devices for each impression. An additional household layer connects individuals in a household with the devices that they share, such as a connected television or smart speaker.

## 

Cross-Device Vendors[](#vendor-list)

The following table lists the names and IDs of most commonly used cross-device graph vendors, including Identity Alliance that combines them all. These graphs support a variety of identifiers, including cookies, MAIDs, CTV, UIDs, RampIDs, and more.

| Vendor Name | Vendor ID |
| Identity Alliance | `10` (person)  
`11` (household) |
| Adbrain Device Graph | `1` |
| Tapad Device Graph | `4` |
| LiveRamp IdentityLink | `6` |

For more information about data gathering and matching methodologies, contact individual vendors.

## 

Select a Cross-Device Vendor for an Ad Group[](#set-vendor)

Here's what you need to know about selecting cross-device vendors for your ad groups:

*   You can specify only one cross-device vendor per ad group in the `CrossDeviceVendorListForAudience` object list.
*   To take advantage of the most comprehensive cross-device targeting solution, be sure to select Identity Alliance. In the platform UI, it is selected by default for all new ad groups.
*   You can change the vendor at any time.
*   For CTV campaigns, be sure to select the household graph ID for Identity Alliance (`11`). For all other campaigns, use the person graph.
*   The only required property for selecting a cross-device vendor is `CrossDeviceVendorId`. All other properties are optional.
*   The most commonly used vendors and their IDs are listed in [Cross-Device Vendors](#vendor-list). You can also use the [POST/crossdevicevendor/query/advertiser](/v3/portal/api/ref/post-crossdevicevendor-query-advertiser) endpoint to look up cross-device vendors available for a specific advertiser.

To set a cross-device vendor for an ad group, in a [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) or [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup), in the `RTBAttributes.AudienceTargeting.CrossDeviceVendorListForAudience` list, specify the `CrossDeviceVendorId` value as shown below. For a complete example with all required properties, see [Create an Ad Group](/v3/portal/api/doc/AdGroup#createadgroups).

{

   "RTBAttributes":{

      "AudienceTargeting":{

         "CrossDeviceVendorListForAudience":\[

            {

               "CrossDeviceVendorId":10,

               "CrossDeviceVendorName":"Identity Alliance",

               "CrossDeviceVendorFee":{

                  "PercentOfMediaCostRate":0.17,

                  "PercentOfDataCostRate":null,

                  "CPMRate":{

                     "Amount":0.95,

                     "CurrencyCode":"USD"

                  },

                  "CPMRateInAdvertiserCurrency":{

                     "Amount":0.95,

                     "CurrencyCode":"USD"

                  }

               }

            }

         \]

      }

   }

}

## 

Set Up Cross-Device Attribution for a Conversion Campaign[](#attribution)

You can also specify Identity Alliance as your cross-device vendor for reporting and attribution for all ad groups within a campaign. This allows you to use the combined vendor graph when attributing conversions.

Here's what you need to know about setting up cross-device attribution for your campaigns:

*   Each reporting column must have a unique combination of `CrossDeviceAttributionModelId` and `TrackingTagId` within the campaign.
*   Be sure to specify this property combination for all reporting columns. It is an all-or-none setup for backward compatibility.
*   To take advantage of the most comprehensive cross-device targeting solution, be sure to select Identity Alliance. It is the only vendor available for household cross-device reporting and attribution.
*   For CTV campaigns, be sure to select the household graph ID for Identity Alliance (`11`). For all other campaigns, use the person graph.
*   You can change the person graph vendor at any time.
*   The most commonly used vendors and their IDs are listed in [Cross-Device Vendors](#vendor-list). You can also use the [POST/crossdevicevendor/query/advertiser](/v3/portal/api/ref/post-crossdevicevendor-query-advertiser) endpoint to look up cross-device vendors available for a specific advertiser.

To set a cross-device vendor for an ad group, in a [POST /v3/campaign](/v3/portal/api/ref/post-campaign) or [PUT /v3/campaign](/v3/portal/api/ref/put-campaign), in the `CampaignConversionReportingColumns` list, specify the `CrossDeviceAttributionModelId`, `ReportingColumnId`, and `TrackingTagId` values for all columns as shown in the following campaign code snippet. For examples with all required campaign properties, see [Create Campaigns](/v3/portal/api/doc/CampaignCreate).

{

   "CampaignConversionReportingColumns":\[

        {

            "TrackingTagId":"xyz123",

            "TrackingTagName":"checkout page",

            "ReportingColumnId":2,

            "CrossDeviceAttributionModelId":"11"

        },

        {

            "TrackingTagId":"a1b2c3",

            "ReportingColumnId":3,

            "CrossDeviceAttributionModelId":"11",

        }

    \]

}