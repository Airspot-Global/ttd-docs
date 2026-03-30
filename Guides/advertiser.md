# Advertiser (Solimar)

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/SolimarAdvertiser
- Category: Guides

---

# Advertiser (Solimar)

> **IMPORTANT**: This guide is intended for Solimar users. To create or manage advertisers in Kokai, see [Create Advertiser](/v3/portal/api/doc/AdvertiserCreate).

An advertiser is a company, group, or brand that buys ad space online in order to sell products or services to a target audience. You must create advertisers before you can set up campaigns in The Trade Desk platform because campaigns, creatives, tracking tags, and data elements must be all associated with an advertiser and require an advertiser ID to be created.

Here's what you need to know:

*   To create advertisers, you must have a partner ID, which was provided to you as part of your API credentials during your [onboarding](/v3/portal/api/doc/ApiPlatformGetStarted).
*   If you are interested in running advertising campaigns for candidates or ballot measures for federal, state or local elections, there are additional requirements. For details, see [Political Advertising](/v3/portal/api/doc/PoliticalAdvertising).
*   By default, your advertiser's currency code is set to the United States Dollar (USD) for budgeting and reporting purposes. If you select a different currency when creating an advertiser, you will not be able to change it and will have to create a new advertiser.
*   You can specify default frequency, bid lists, and other settings that will be automatically propagated to all campaigns and their ad groups created for the advertiser. You can change these settings for all individual instances as needed when creating or updating them.
*   Certain settings at the advertiser level are enabled and propagated to new ad groups by default, such as [Prism](/v3/portal/api/doc/Prism). For details, see [FAQs](#faqs).

For industry categories, we use the IAB Tech Lab Content Taxonomy [version 2.2](https://iabtechlab.com/wp-content/uploads/2020/12/Implementation_Guide_for_Brand_Suitability_with_IABTechLab_Content_Taxonomy_2-2.pdf). For details on required properties, their correlation to the IAB taxonomy 1.0, and mapping information returned in responses, see [Industry Category Taxonomy Migration](/v3/portal/api/doc/UpgradeSupportCategoryTaxonomy).

## 

Create an Advertiser[](#create)

To create an advertiser, specify all the required properties in a [POST /v3/advertiser](/v3/portal/api/ref/post-advertiser) call.

> **IMPORTANT**: Be sure to update your workflows to use the `AdvertiserCategory` property. For details on required properties and taxonomy mapping information returned in responses, see [Using Legacy and New Category Properties](/v3/portal/api/doc/UpgradeSupportCategoryTaxonomy#use-cases).

For example:

{

   "PartnerId":"{partnerid}",

   "AdvertiserName":"Advertiser ABC",

   "Description":"New advertiser",

   "Country":"US",

   "CurrencyCode":"USD",

   "AttributionClickLookbackWindowInSeconds":5184000,

   "AttributionImpressionLookbackWindowInSeconds":5184000,

   "ClickDedupWindowInSeconds":7,

   "ConversionDedupWindowInSeconds":60,

   "DefaultRightMediaOfferTypeId":1,

   "AdvertiserCategory":{

      "CategoryId":8311

   },

   "DomainAddress":"https://www.domain.com",

}

The following is a sample response with an advertiser ID assigned.

{

   "PartnerId":"{partnerid}",

   "AdvertiserId":"{advertiserid}",

   "AdvertiserName":"Advertiser ABC",

   "Description":"New advertiser",

   "Country":"US",

   "CurrencyCode":"USD",

   "AttributionClickLookbackWindowInSeconds":5184000,

   "AttributionImpressionLookbackWindowInSeconds":5184000,

   "ClickDedupWindowInSeconds":7,

   "ConversionDedupWindowInSeconds":60,

   "DefaultRightMediaOfferTypeId":1,

   "AdvertiserCategory":{

      "CategoryId":8311,

      "CategoryName":"Women's Casual Wear",

      "CategoryTaxonomyId":13,

      "CategoryTaxonomyName":"IAB Content Categories v2.2",

      "CategoryTaxonomyVersion":"2.2",

      "Mappings":\[

         {

            "CategoryTaxonomyId":2,

            "CategoryId":292,

            "ExternalId":"IAB18-5"

         },

         {

            "CategoryTaxonomyId":13,

            "CategoryId":8311,

            "ExternalId":"568"

         }

      \]

   },

   "IndustryCategoryMapping":{

      "CategoryTaxonomyId":2,

      "CategoryId":8311,

      "ExternalId":"568"

   },

   "Keywords":\[

      0

   \],

   "Availability":"Available",

   "LogoURL":null,

   "DomainAddress":"https://www.domain.com",

   "AdvertiserAudienceSettings": {

      "AudienceExcluderEnabled": true

   }

}

## 

Digital Services Act Properties[](#dsa)

The Digital Services Act (DSA) is a set of regulations for the European Union (EU) ([Release Notes](/v3/portal/api/doc/ReleaseNotes2023#december-1-2023) for December 1, 2023). Per DSA, online platforms—which will include certain publishers such as online marketplaces, social networks, travel and accommodation platforms, app stores, as well content-sharing platforms—must ensure that users in the EU have real-time access to certain information about any ad shown to them, including (amongst other things) the name of the advertiser and the name of the natural or legal person (individual or organization) who paid for the ad, if it is different from the advertiser.

If you are targeting anyone in the EU, review your advertiser properties and update your workflows to include the following new DSA properties: `AdvertiserNameDsa` and `PayerNameDsa`. If no DSA transparency information is provided in these properties, The Trade Desk will use default values by pulling them from the `AdvertiserName` API property and the `CustomerName` field from our internal business database.

The following table summarizes the details.

| Required Information | DSA Property | Default Value | Notes |
| Advertiser’s name | `AdvertiserNameDsa` | `AdvertiserName` | The default value is read from the advertiser API. |
| Payer’s name | `PayerNameDsa` | `CustomerName` | The default value is read from our internal business database. |

> **IMPORTANT**: It is your responsibility, as required under our Master Services Agreement, to ensure any information you provide to us is truthful and correct. If you fail to confirm the values, you agree to us using the default values.

If you have questions or require more information, contact your Account Manager or Technical Account Manager.

## 

EU Health Policy[](#eu-health)

> **NOTE**: This section only applies to data coming from the European Economic Area, the United Kingdom (under the UK GDPR), or Switzerland, collectively GDPR regions.

The Trade Desk maintains an EU Health Policy that treats health data as sensitive data, which could impact advertisers that promote health-related products. If you are an advertiser that runs campaigns in the GDPR regions, then it may be subject to these policy restrictions.

The following table summarizes the scope of impact.

| Endpoints | Condition | Notes |
| [Bid Lists](/v3/portal/api/doc/BidList) | Bid list contains atmospheric conditions. | [Pollen risk targeting](/v3/portal/api/doc/ReleaseNotes2023#october-10-2023) is disabled in GDPR regions. |
| [Ad Groups](/v3/portal/api/doc/SolimarAdGroup) | Ad group optimization uses Audience Booster, Prism, Audience Predictor, retargeting, or interest targeting. | Certain ad group performance enhancements are not supported in GDPR regions. See also [Performance-Enhancing Features](/v3/portal/api/doc/SolimarAdGroup#ad-group-koa-features). For details, see [Prism](/v3/portal/api/doc/Prism).  
**NOTE**: Prism is disabled for advertisers whose partners have opted out of fee-based features. |
| [CRM Data](/v3/portal/api/area/Crm%20Data) | Upload contains health data that originates within GDPR regions | Advertisers cannot upload health data that violates policy. |

> **NOTE**: Health advertisers are identified through self-categorization and review by The Trade Desk, of the advertised product.

## 

FAQs[](#faqs)

The following is a list of frequently asked questions about advertisers.

### 

How do I enable Prism for an advertiser?

You can enable Prism using REST and GraphQL. For details, see [Prism](/v3/portal/api/doc/Prism).

### 

Does changing Prism settings affect live ad groups?

No. Changing Prism settings does not affect any live ad groups.