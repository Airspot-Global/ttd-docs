# Geo-Interest Expansion for CTV

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/GeoInterestExpansion
- Category: Guides

---

# Geo-Interest Expansion for CTV

Geo-interest segments provide an ID-less audience targeting solution for CTV, where you target co-located people with potentially similar interests. For example, if you want to advertise to fast food lovers, you can build an audience in the platform to target those areas where there's interest in fast food.

## 

Benefits[](#benefits)

Here are some of the benefits of using geo-interest targeting:

*   To increase scale, use geo-interest targeting as a complement to the Identity Alliance household graph.
*   If you do not want to use hyper-personalized household targeting where you are targeting the individual household, use geo-interest segments to target multiple areas based on interest. This helps reduce customer frustration that may arise from 1:1 targeting.
*   Use geo-interest targeting as an additional targeting method for your existing campaigns.

## 

How Geo-Interest Segments Are Created[](#created)

To create geo-interest segments, The Trade Desk collects IP addresses from received bid requests, removes the last octet so they no longer correspond to a single household, and hashes the result into a geographical area code known as MCID, as shown in the following example.

| Original IP Address | IP Address Without Last Octet | Area Code After Hashing (MCID) |
| `102.89.159.92` | `102.89.159` | `18c74e02-a796-47ff-86ff-24b95bb7a25f"` |

  
Here's what The Trade Desk takes into consideration when creating geo-interest segments:

*   To determine the set of interests in each area, we look at the categories of sites visited by users in that area who have consented to our cookies. For example, Jessica is looking for a late-night bite and browses the website of her favorite fast-food restaurant. The Trade Desk classifies this website as fast food by using the standard TTD contextual taxonomy.
*   We also look at what other people in the area are interested in, and over time, we have a list of the top interests in the area.
*   We create a geo-interest segment for each interest category, and each segment maps to all the areas where users have those interests.

  
Here's what you need to know about geo-interest segments:

*   A single geo-interest segment can have multiple MCID area codes.
*   A single geographical MCID area code can be used in multiple interest segments.
*   The number of individuals in a geographical area varies depending on the population density of the area.
*   Geo-interest segments in the platform are refreshed daily.
*   Every geographical area has an MCID area code, and every MCID area code has a minimum threshold of people.
*   The platform has a geo-interest segment for each interest category and, behind the scenes, each segment maps to all the areas where users have those interests.

The following example illustrates a geo-interest segment that has multiple MCID area codes where fast food is a top interest category. On the left, the image shows a list of hashed MCIDs within the segment, while on the right, it shows a map of a geographical location with each point representing the area in which the MCIDs originated.

![Geo-interest Segment example](/v3/content/docs/Images/geo-interest-segment-example.png)

The following image provides a closeup of one of the MCIDs from the preceding image by illustrating how many people in this area are interested in fast food, which is the top interest in this location.

![MCID Example](/v3/content/docs/Images/geo-interest-MCID-example.png)  

## 

Set Up Geo-Interest Targeting[](#setup)

To target geo-interest segments, complete the following tasks.

| Task | Endpoint or Further Reference | Notes |
| (Recommended) [Set](#set) geo-interest targeting as your primary audience targeting strategy. | [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) or  
[PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) | When you create or update an [ad group](/v3/portal/api/doc/AdGroup), set the `UseMcIdAsPrimary` value to `true`. |
| [Look up](#look-up) geo-interest data segments. | [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) | Retrieve the third-party data ID of each geo-interest segment you want to use. |
| Include geo-interest segments in your audience. | [Audiences](/v3/portal/api/doc/Audience) | During audience creation, include the third-party data ID of the geo-interest segments you want to use in the `ThirdPartyDataIds` array of your audience [data groups](/v3/portal/api/doc/Audience#createdatagroups). |

### 

Set Geo-Interest Targeting as Your Primary Targeting Strategy[](#set)

By default, ad groups that use geo-interest targeting can bid only on avails that other forms of audience targeting cannot reach. To enable an ad group with geo-interest targeting to bid on all avails, you need to set geo-interest as your primary audience targeting strategy.

For the best results, use geo-interest as the primary strategy in the following cases:

*   You're not using another form of audience targeting.
*   You're using a geo-based interest audience for the first time. (After you establish the maximum scale, you can always revert to the default behavior of geo-interest targeting. For details, see [FAQs](#faqs).)

To set geo-interest as your primary audience targeting strategy, in a [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) or [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) call, set the `RTBAttributes.AudienceTargeting.UseMcIdAsPrimary` value to `true` as shown in the following code snippet.

{

   "CampaignId":"t0ncimu",

   "AdGroupName":"Strategy 1",

   "AdGroupCategory":{

      "CategoryId": 8311

   },

   "RTBAttributes":{

      "AudienceTargeting":{

         "UseMcIdAsPrimary": true

      }

   }

}

After you set geo-interest targeting as your primary strategy, [look up](#look-up) the geo-interest segments that you want to include in your audience.

### 

Look Up Geo-Interest Segments[](#look-up)

To look up and retrieve a list of all geo-interest segments, in a [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) call, include the following values:

*   In the `BrandIds` list, include `ttdgeointerest` as a value.
*   In the `SearchTerms` list, include `Geo Interest Segments` as a value.

> **TIP**: To narrow your search, include additional search terms such as `Beauty & Fashion`.

{

  "AdvertiserId": "lofgv9s",

    "BrandIds": \["ttdgeointerest"\],

  "SearchTerms": \["Geo Interest Segments"\],

  "PageStartIndex": 0,

  "PageSize": 10

}

A successful response returns a list of geo-interest segments with information such as the third-party data ID. The following code snippet is an example of a single geo-interest data segment returned in the response.

{

    "ThirdPartyDataId": "10645207|ttdgeointerest",

    "BrandId": "ttdgeointerest",

    "BrandName": "Data Alliance",

    "Name": "Accessories",

    "FullPath": "Geo Interest Segments (beta) > Beauty & Fashion > 

    Fashion > Accessories",

    "Description": "Geo Interest Segments with eligible sites/apps 

    classified in this category.",

    "DevicesBrowsers30DayCount": 905000,

    "UniqueUserCount": 665978000

}

When you are ready to create your audience, include the third-party data ID of each geo-segment you want to use in the [data groups](/v3/portal/api/doc/Audience#createdatagroups) of your audience.

## 

FAQs[](#faqs)

The following is a list of commonly asked questions about geo-interest segments and targeting.

### 

Are geo-interest segments different from geo segments?

Yes. Geo segments are used to target geographic areas, while geo-interest segments target co-located people with potentially similar interests, but not a specific area.

### 

How is geo-interest targeting different from household targeting?

Household targeting works by targeting individuals in specific households based on IP addresses, whereas geo-interest segments target an entire area based on top interests in the area.

### 

How do I revert to the default behavior of geo-interest targeting?

In a [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) call, set the `UseMcIdAsPrimary` value to `false`.