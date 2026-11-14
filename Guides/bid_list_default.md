# Default bid lists

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/BidListDefault
- Retrieved: 2026-11-14
- Category: Guides

---

# Default bid lists

Default bid lists are intended for grouping bid lists that are common across most campaigns for a specific advertiser and/or across most ad groups under a campaign. Thus, instead of setting up bid lists for individual campaigns and ad groups, you can save time and effort by creating default bid lists that are housed at the advertiser or campaign level. The advertiser default lists can be propagated to any new campaigns created for the advertiser as needed and subsequently applied to any ad groups within those campaigns. The campaign default bid lists, which allow a wider variety of dimensions, can be applied to new ad groups under each campaign as needed. Once an advertiser or campaign default bid list is applied to an ad group, it is automatically enabled for bidding.

## Standard vs. default bid lists

Default bid lists are a subset of standard bid lists, which allows more user control, efficiency, and granularity in bid list management as well as complete parity and visibility in the UI. The following table provides a high-level comparison. For details on standard bid lists, see Bid lists.

| Comparison Aspect | Standard Bid Lists | Default Bid Lists |
| --- | --- | --- |
| Ownership | Can be owned by: - Partner - Advertiser - Campaign - Ad group | Can be owned by: - Partner - Advertiser - Campaign |
| Level Applied | N/A | Can be applied only to these levels: - Advertiser - Campaign |
| Association levels | Can be associated with the bid list owner and all respective descendants under it. For details, see the _Bid List Relationships_ section in Bid lists. | Can be associated only with ad groups under a campaign that has applied advertiser- or campaign-level default bid lists. |
| Inheritance | All associated and enabled bid lists are automatically inherited by all respective descendants. | Advertiser- and campaign-owned default bid lists are not inherited automatically by their descendants. You, as the API user, determine if and when a bid list will be inherited by a lower entity. |
| Allowed bid adjustment types | - Target - Block - Optimized | - Target - Block |
| Allowed dimensions | All | - All available at the campaign level - Limited at the advertiser level For details, see Allowed dimensions. |
| Single- or multi-dimensional bid lists | Both | Only single-dimensional lists |
| Checking for inherited higher-level bid lists | For a given entity level, you can only see bid lists that are associated directly with that entity. You must query higher entity bid list associations to see all bid lists that are inherited and active for a lower entity level. | Since advertiser- or campaign-owned default bid lists are always associated only at the ad group level, you will always be able to query for all associated default bid lists at the ad group level. |
| Bid line limits and counts | No difference. For details, see the _Bid Line Limits_ section in Bid lists. | No difference. For details, see the _Bid Line Limits_ section in Bid lists. |

## Allowed dimensions in default bid lists

- Default bid lists can be only single-dimensional. Multi-dimensional bid lists are currently not allowed.
- Some dimensions may require permissions. If needed, please contact your Account Manager for help.
- At the campaign level, default bid lists can include any dimensions, except `HasVideoPlayerSizeId`.
- At the advertiser level, default bid lists can include only the following dimensions.

| Category | Dimension Values |
| --- | --- |
| Brand Safety | `HasGrapeshotBrandSafetyCategoryId` `HasIntegralBrandSafetyCategoryId` `HasDoubleVerifyBrandSafetyCategoryId` `HasIntegralVideoBrandSafetyCategoryId` `HasPeer39BrandSafetyCategoryId` |
| Page Quality | `HasIntegralPageQualityCategoryId` `HasGrapeshotDisplayPageQualityCategoryId` `HasGrapeshotVideoPageQualityCategoryId` `HasPeer39PageQualityCategoryId` `HasIntegralVideoPageQualityCategoryId` `HasTencentPageQualityCategoryId` `HasAdBugPageQualityCategoryId` `HasAdBugVideoPageQualityCategoryId` `HasRTBAsiaPageQualityCategoryId` `HasRTBAsiaVideoPageQualityCategoryId` |
| Viewability | `HasDisplayViewabilityScoreRange` `HasIntegralViewabilityCategoryId` `HasVideoViewabilityScoreRange` `HasDoubleVerifyViewabilityCategoryId` `HasIntegralVideoViewabilityCategoryId` `HasDoubleVerifyVideoViewabilityCategoryId` `HasPeer39ViewabilityCategoryId` `HasGrapeshotViewabilityCategoryId` `HasGrapeshotVideoViewabilityCategoryIds` |
| Language | `HasLanguageId` `HasGrapeshotLanguageId` `HasPeer39LanguageId` |
| Other Dimensions | `HasAdsTxtSellerTypeId` `HasGeoSegmentId` `HasDomainFragmentId` `HasPrivateContractId` `HasSupplyVendorId` |

## What you need to know

Here’s what you need to keep in mind when working with default bid lists. They:

- Are optional and single-dimensional. You can associate bid lists with campaigns and ad groups on an individual basis as explained in Bid lists.
- Can be only of type `TargetList` or `BlockList` (specified in `BidAdjustmentType`). You cannot add Optimized bid lists, such as Volume Control bid lists, as default ones.
- Can be defined only at the advertiser or campaign level. Advertiser default bid lists have a limited number of dimensions that can be used.
- If included, get propagated sequentially to the descendants by following the bid list inheritance rules. For details, see Bid lists.
For example, the advertiser’s default bid lists cannot be applied directly to ad groups without first including them in the advertiser’s campaigns.
- Will not be automatically applied to the advertiser’s _existing_ campaigns or their _existing_ ad groups.
- May be included only in the advertiser’s _new_ campaigns, by setting the `IncludeDefaultsFromAdvertiser` parameter to `true` in the POST/campaign request. The applied default bid lists are automatically added to the `DefaultBidLists` array.
- May be included only in _new_ ad groups, using the `IncludeDefaultsFromCampaign` parameter to `true` in the POST/adgroup request. The applied default bid lists are automatically added to the `AssociatedBidLists` array with the following settings, which you can update as needed:

  - The `IsEnabled` parameter set to `true`.
  - The `IsDefaultForDimension` parameter set to `false`.

- If the same bid list is already applied to the campaign or ad group, it will be included only once.
- When included, the applied default bid lists in the `DefaultBidLists` array for campaigns and the `AssociatedBidLists` array for ad groups can be subsequently retrieved using the respective GET requests and updated using the respective PUT requests and as needed, but no new default bid lists can be included from the parent advertiser or campaign.

## FAQs

The following table provides a matrix of answers to some default bid list FAQs about each entity involved.

| Question | Advertiser | Campaign | Ad Group |
| --- | --- | --- | --- |
| Where can default bid lists be defined? | In `DefaultBidLists` array | In `DefaultBidLists` array | N/A |
| Can default bid list be multi-dimensional? | No | No | N/A |
| How can default bid lists be inherited from the parent? | N/A | Using `IncludeDefaultsFromAdvertiser` property, but only at creation | Using `IncludeDefaultsFromCampaign` property, but only at creation |
| Can other bid lists be included as default bid lists in addition to those from the parent at creation? | N/A | Yes, by setting `IncludeDefaultsFromAdvertiser` to `true` and adding bid list IDs to `DefaultBidLists` array | N/A |
| Can the items in the `DefaultBidLists` array be modified? | Yes, but changes will apply only to new campaigns | Yes, but changes will apply only to new ad groups | N/A |
| Can default bid lists be automatically added to `AssociatedBidLists` and enabled for bidding? | No | No | Yes, but only at creation Any subsequent enabling or disabling of bid lists will affect only the current ad group. |
| If the contents of a default bid list are updated, are the changes automatically applied to all campaigns and ad groups that use it? | N/A | Yes | Yes |

## Endpoints

The following table lists the endpoints for creating, updating, applying, and retrieving default bid lists.

> **IMPORTANT**: Since arrays in PUT requests _replace_ the current ones instead of _adding_ to them, if you want to add bid lists to any current arrays, make sure to retrieve them with the respective GET requests first and then include the current and new values in respective PUT requests with any other appropriate changes.

| Endpoints | Advertiser | Campaign | Ad Group |
| --- | --- | --- | --- |
| For defining/adding default bid lists | POST/advertiser PUT/advertiser | POST/campaign PUT/campaign | N/A |
| For including default bid lists in descendants | N/A | POST/campaign | POST/adgroup |
| For updating default bid lists | PUT/advertiser | PUT/campaign | N/A |
| For retrieving default bid lists | GET/advertiser/{advertiserId} | GET/campaign/{campaignId} | N/A, the applied default bid lists will be returned in the `AssociatedBidLists` array |

See also Request examples.

## Apply advertiser's default bid lists

The following table outlines the process of creating a set of default bid lists for an existing advertiser and including them as default bid lists in a new campaign and a new ad group for that campaign.

| Step # | Description | Endpoints and Further Reference | Notes |
| --- | --- | --- | --- |
| 1 | (Optional, if you already have the necessary bid lists) Create bid lists with the allowed dimensions common to most campaigns for the advertiser and make sure that the `BidAdjustmentType` is set to either `TargetList` or `BlockList` and the advertiser or partner is set as the bid list owner. | POST/bidlist For details, see Create bid lists. | Request example snippet |
| 2 | Update the advertiser by adding the bid list IDs to the `DefaultBidLists` array. **IMPORTANT**: If the advertiser already has an array of default bid lists to which you want to add the new ones, make sure to retrieve the current list using a GET request. | PUT/advertiser | Request example snippet For an example with all required fields, see Create advertiser. |
| 3 | Create a new campaign for the advertiser and set the `IncludeDefaultsFromAdvertiser` parameter to `true`. If you want to include: - Only advertiser’s default bid lists, do not include the `DefaultBidLists` array in the request. - Other bid lists _in addition_ to the advertiser’s default bid lists, include the IDs of the additional bid lists in the `DefaultBidLists` array in the request. | POST/campaign For details on creating campaigns, see Campaigns. | Request example snippet The response will include the `DefaultBidLists` array automatically populated with the advertiser’s default bid lists and any other bid lists that were specified in the request. |
| 4 | Create a new ad group for the campaign and set the `IncludeDefaultsFromCampaign` parameter to `true`. If you want to include other bid lists in addition to the campaign default bid lists, include the IDs of the additional bid lists in the `AssociatedBidLists` array in the request and set the lists as enabled. | POST/adgroup For details on creating ad groups, see Ad groups. | Request example snippet The response will include the `AssociatedBidLists` array automatically populated with the default bid lists from the specified campaign, already enabled for bidding, and any additional bid lists you may have included in the request. |

## Update campaign default bid lists

The following table outlines the process of creating a set of default bid lists for an existing campaign and including them as associated bid lists in a new ad group for that campaign. The sections that follow provide code examples for each request.

| Step # | Description | Endpoints and Further Reference | Notes |
| --- | --- | --- | --- |
| 1 | (Optional, if you already have the necessary bid lists) Create bid lists with dimensions common to all campaign’s ad groups and make sure that the `BidAdjustmentType` is set to either `TargetList` or `BlockList` and the campaign is set as the bid list owner. | POST/bidlist For details, see Bid list. | Request example snippet |
| 2 | Retrieve the existing default bid lists for the campaign. | GET/campaign/{campaignId} | Request example snippet |
| 3 | Update the campaign by adding the new bid list IDs to the retrieved `DefaultBidLists` array. | PUT/campaign | Request example snippet For an example with all required fields, see Campaigns. |
| 4 | Create a new ad group for the campaign and set the `IncludeDefaultsFromCampaign` parameter to `true`. If you want to include other bid lists in addition to the campaign default bid lists, include the IDs of the additional bid lists in the `AssociatedBidLists` array in the request and set the lists as enabled. | POST/adgroup For details on creating ad groups, see Ad groups. | Request example snippet The response will include the `AssociatedBidLists` array automatically populated with the default bid lists from the specified campaign, already enabled for bidding. |

## Request examples

The following are code snippets of request examples illustrating the steps in the Applying advertiser's default bid lists and Updating campaign default bid lists procedures.

- Create bid lists
- Add bid lists as defaults
- Include advertiser's default bid lists in a new campaign
- Retrieve campaign information
- Add default bid lists to an existing campaign
- Include campaign default bid lists in a new ad group

### Create default bid lists

To create default bid lists, set the `BidListAdjustmentType` property to `TargetList` or `BlockList`. The following is a POST /v3/bidlist request body example with that property set to `TargetList`.

```
{
    "Name": "DEFAULT_BID_LIST_NAME_PLACEHOLDER",
    "BidListAdjustmentType": "TargetList",
    "BidLines": [
        // Include the dimensions that you want applied to all campaigns.
    ],
    "BidListOwner": "Advertiser",
    "BidListOwnerId": "abcd1234"
    // Include other required fields.
}
```

### Add bid lists as defaults

The following code snippet can be included in the respective POST and PUT advertiser or campaign requests.

> **IMPORTANT**: Since arrays in PUT requests _replace_ the current ones instead of _adding_ to them, if you want to add bid lists to any current arrays, make sure to retrieve them with the respective GET requests first and then include the current and new values in respective PUT requests with any other appropriate changes.

```
{
    "DefaultBidLists": [
        {
          "BidListId": "efgh5678"
        },
        {
          "BidListId": "ijkl9012"
        }
    ]
    // Include other required fields.
}
```

### Include advertiser's default bid lists in a new campaign

To include an advertiser's default bid lists in a new campaign, set the `IncludeDefaultsFromAdvertiser` property to `true`. The applied default bid lists are automatically added to the `DefaultBidLists` array. The following is a POST /v3/campaign request body example with that property set to `true`.

> **TIP**: If you want to include other bid lists to the campaign _in addition_ to the advertiser’s default bid lists, include the `DefaultBidLists` array with the IDs of the additional bid lists in the request.

```
{
    "AdvertiserId": "abcd1234",
    "CampaignName": "CAMPAIGN_NAME_PLACEHOLDER",
    "CampaignConversionReportingColumns":[
        {
            "TrackingTagId": "12345678ab",
            "ReportingColumnId": 1
        }
    ],
    "IncludeDefaultsFromAdvertiser": true
    // Include other required fields.
}
```

### Retrieve campaign information

To retrieve campaign information such as associated default bid lists, use the GET /v3/campaign/{campaignId} endpoint. The following request example uses an authorization token, which is required by The Trade Desk API to authorize the request.

```
curl --location --request GET 'https://api.thetradedesk.com/v3/campaign/t0ncimu' \
--header 'Content-Type: application/json' \
--header 'TTD-Auth: yourauthtoken'
```

### Add default bid lists to an existing campaign

To add default bid lists to an existing campaign, use the PUT /v3/campaign endpoint. The following is an example of a request to update a campaign by adding two default bid lists.

> **IMPORTANT**: Since arrays in PUT requests _replace_ the current ones instead of _adding_ to them, if you want to add bid lists to any current arrays, make sure to retrieve them with the respective GET requests first and then include the current and new values in respective PUT requests with any other appropriate changes.

```
{
    "AdvertiserId": "abcd1234",
    "CampaignName": "CAMPAIGN_NAME_PLACEHOLDER",
    "CampaignConversionReportingColumns":[
        {
            "TrackingTagId": "12345678ab",
            "ReportingColumnId": 1
        }
    ],
       "DefaultBidLists": [
        {
          "BidListId": "efgh5678"
        },
        {
          "BidListId": "ijkl9012"
        }
    ]
    // Include other required fields.
}
```

### Include campaign default bid lists in a new ad group

To include campaign default bid lists in a new ad group, use the POST /v3/adgroup endpoint. All default bid lists associated with the campaign are automatically applied this ad group upon its creation. If the same bid list is already applied to the ad group, it will be included only once. The applied lists can be removed, as needed.

> **TIP**: If you want to include other bid lists to the ad group _in addition_ to the campaign default bid lists, include the `AssociatedBidLists` array with the IDs of the additional bid lists in the request and set them as enabled.

```
{
   "CampaignId":"mnop3456",
   "AdGroupName":"AD_GROUP_NAME_PLACEHOLDER",
   "IncludeDefaultsFromCampaign": true
   // Include other required fields.
}
```
