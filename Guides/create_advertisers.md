# Create Advertisers

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/AdvertiserCreate
- Category: Guides

---

# Create Advertisers

To set up campaigns in the API platform, you must first create an advertiser account. This provides you with an advertiser ID, which is required for many tasks, including creating campaigns, tracking tags, seeds, and data elements, as well as uploading creatives. Some settings you define when creating the advertiser, like currency code, default frequency, and bid lists, are [propagated](/v3/portal/api/doc/EntityRelationships) to associated campaigns and ad groups.

Configuring the advertiser is a "set and forget" experience, meaning it's a one-time setup. You only need to modify it to make rare global changes, like [preferences](#preferences) for attribution and deduplication windows.

## 

What You Need to Know[](#wyntk)

Here's what you need to know about creating an advertiser account:

*   To create an advertiser, you must have a partner ID, which was provided to you as part of your API credentials during your [onboarding](/v3/portal/api/doc/ApiPlatformGetStarted).
*   To find the industry categories that applies to your advertiser account, use the IAB Tech Lab Content Taxonomy [version 2.2](https://iabtechlab.com/wp-content/uploads/2020/12/Implementation_Guide_for_Brand_Suitability_with_IABTechLab_Content_Taxonomy_2-2.pdf). If you want to see how version 1.0 maps to version 2.2, see [IAB Content Taxonomy Mapping: Version 1.0 to 2.2](/v3/portal/openpath/doc/TaxonomyMapping).
*   Some advertiser tasks, such as [uploading data](/v3/portal/data/doc/DataAuthentication), require additional credentials beyond the advertiser ID, like a secret key (also known as an advertiser key).
*   By default, your advertiser's currency code is set to the United States Dollar (USD) for budgeting and reporting purposes. If you select a different currency when creating an advertiser, you will not be able to change it and will have to create a new advertiser.
*   You can specify default frequency, bid lists, [Prism](/v3/portal/api/doc/Prism) settings, and other settings that will be automatically propagated to all campaigns and their ad groups created for the advertiser. You can change these settings for all individual instances as needed when creating or updating them. For details, see the Ownership Relationships diagram in [Entity Relationships](/v3/portal/api/doc/EntityRelationships).

See also [FAQs](#faqs).

### 

Additional Requirements[](#additional-requirements)

If you are running political campaigns or operating in specific regions of Europe, or use certain industry categories, additional requirements apply:

*   To improve transparency around which categories require additional attention, advertisers must include a valid subcategory when using categories that might have subcategories classified as sensitive. For example, an advertiser in the **Shopping** category must specify a valid subcategory because it includes the sensitive **Lotteries and Scratch Cards** subcategory.
*   If you are interested in running advertising campaigns for candidates or ballot measures for federal, state or local elections, there are additional requirements. For details, see [Political Advertising](/v3/portal/api/doc/PoliticalAdvertising).
*   If you are targeting anyone the European Economic Area, the United Kingdom (under the UK GDPR), or Switzerland, collectively General Data Protection Regulation (GDPR) regions, you must include the DSA properties and check policy restrictions. See also [Digital Services Act Properties](#dsa) and [EU Health Policy](#eu-health).

### 

Recommended Options[](#recommendations)

We recommend the following options to enhance your campaigns:

*   For optimized audience-based buying, The Trade Desk has curated a pool of thousands of vetted, trusted sellers and publishers at no cost to you. Explore the [Sellers and Publishers 500+ Marketplace](/v3/portal/api/doc/SP500) to take advantage of this opportunity.
*   To help retailers understand how much of your spend is tied to impressions that use their audience data, you can [share](#share-costs) monthly reports of the partner cost.

## 

Create Request Examples[](#create)

To submit a successful create request, use either [GraphQL](#gql-example) or [REST](#rest-example) API and specify all required properties for the advertiser, such as attribution and deduplication windows. Each API call can create only one advertiser.

### 

GraphQL API[](#gql-example)

To create an advertiser, use the `advertiserCreate` mutation. Here's an example that specifies the required properties and attribution and deduplication windows.

mutation {

    advertiserCreate(

        input: {

            partnerId: "PARTNER\_ID\_PLACEHOLDER"

            name: "ADVERTISER\_NAME\_PLACEHOLDER"

            description: "ADVERTISER\_DESCRIPTION\_PLACEHOLDER"

            attributionClickLookbackWindowInSeconds: 5184000

            attributionImpressionLookbackWindowInSeconds:5184000 

            clickDedupeWindowInSeconds: 7

            conversionDedupeWindowInSeconds: 60

            advertiserCategoryInput: {

                categoryId: 8311

            }

            defaultRightMediaOfferTypeId: 1

            domainAddress: "https://www.domain.com"

            country: "US"

        }

    ) {

        data {

            clickDedupeWindowInSeconds

            conversionDeDupeWindowInSeconds

            name

            description

            domainAddress

            country{

                id

            }

        }

        errors{

            ... on MutationError{

                message

                field

            }

        }

    }

    }

A successful response returns the assigned advertiser ID and other information. To look up details, you can use [GraphQL queries](/v3/portal/api/doc/AdvertiserGQLQueryExamples).

### 

REST API[](#rest-example)

To create an advertiser, specify all the required properties and applicable preferences in a [POST /v3/advertiser](/v3/portal/api/ref/post-advertiser) call.

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

   "DomainAddress":"https://www.domain.com"

}

A successful response returns the assigned advertiser ID and other information. To look up details, you can use [GraphQL queries](/v3/portal/api/doc/AdvertiserGQLQueryExamples).

## 

Configure Advertiser Preferences[](#preferences)

For the new advertiser being set up, you can configure preferences for attribution and deduplication windows, and consent to sharing monthly reports of the partner costs with retailers.

### 

Attribution Windows[](#attribution)

An attribution window is the period of time after a click or impression occurs that a conversion is tracked for credit to the click or impression. The following table lists attribution examples.

| Type | Property | Example |
| Click Lookback Window | `AttributionClickLookbackWindowInSeconds` | If the lookback window is set to 30 days, conversions or actions that take place 31 days after that impression is served do not count toward attribution credit and are not included in any reports. |
| Impression | `AttributionImpressionLookbackWindowInSeconds` | A 30-day impression attribution window credits any conversion made within 30 days after an impression is served. |

### 

Deduplication Windows[](#deduplication)

A deduplication window is the period during which duplicate clicks or conversions is disregarded for attribution. The following table lists deduplication examples.

| Type | Property | Example |
| Click | `ClickDedupWindowInSeconds` | A window of seven seconds ensures that if a user clicks an ad more than once during those seven seconds, it is counted as one click. |
| Conversion | `ConversionDedupWindowInSeconds` | A window of 500 seconds ensures that if a user performs a desired conversion action (for example, a sale, newsletter sign-ups, or any other measurable result) more than once during those 500 seconds, it will be counted as one conversion. |

During the deduplication process for conversions, the decision of whether a conversion event should be recorded or deduplicated depends on the referrer URL in the tracking tag. By default, if conversion events occur on different pages (but with the same [TDID](/v3/portal/resources/doc/Glossary#tdid) and tracking tag ID) within the deduplication window, they are still counted as separate conversions.

> **TIP**: To count duplicate conversions only once within the deduplication window, choose to ignore the referrer URL for deduplication when defining the attribution windows for the advertiser.

### 

Advertiser Consent for Sharing Partner Costs with Retailers[](#share-costs)

Partner cost is the total cost advertisers incur for impressions, calculated as the sum of media cost, data cost, fee features cost, and tech fees when a retailer's data is applied. [Additional fees](https://desk.thetradedesk.com/knowledge-portal/en/fees-additional-types.html), such as margin fee, CPM fee, and flat CPM rate, are not included in the cost.

Sharing monthly reports of the partner cost with retailers helps them understand how much of your spend is tied to impressions that use their audience data. This visibility allows retailers to better assess your progress toward meeting commitments and confirm when those commitments have been fulfilled. You, as the advertiser, must give consent before the partner cost can be shared.

#### Cost Data Shared with Retailers

Retailers receive a monthly report with aggregated partner cost data for impressions targeting their audience segments. It can be delivered in Excel or CSV format.

> **NOTE**: Partner cost is reported as a lump sum. Retailers do not see a breakdown of media costs, data costs, or fees.

The following table is an example of a report generated in April, including three advertisers who consented to share partner cost in March.

**Example Report: Generated April**

| Month | Advertiser Name | Partner Cost |
| March | Advertiser A | $10,000 |
| March | Advertiser B | $5,000 |
| March | Advertiser C | $3,000 |

#### Consent to Share Partner Cost

To provide consent to share your partner cost data with retailers, use the following `advertisers` mutation with your advertiser ID and the merchant ID of the retailer in the `retailCommitmentTrackerSettings` object. You can use it for multiple advertisers and retailers.

mutation {

  advertisers {

    retailCommitmentTrackerSettings {

      create(input: {advertiserId: "ADVERTISER\_ID\_PLACEHOLDER", 

      merchantId: "MERCHANT\_ID\_PLACEHOLDER"})

    }

  }

}

## 

Digital Services Act Properties[](#dsa)

The Digital Services Act (DSA) is a set of regulations for the EU ([Release Notes](/v3/portal/api/doc/ReleaseNotes2023#december-1-2023) for December 1, 2023). Per DSA, online platforms—which will include certain publishers such as online marketplaces, social networks, travel and accommodation platforms, app stores, as well content-sharing platforms—must ensure that users in the EU have real-time access to certain information about any ad shown to them, including (amongst other things) the name of the advertiser and the name of the natural or legal person (individual or organization) who paid for the ad, if it is different from the advertiser.

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
| [Bid Lists](/v3/portal/api/doc/BidList) | Bid list contains atmospheric conditions. | [Pollen risk targeting](/v3/portal/api/doc/Pollen) is disabled in GDPR regions. |
| [Ad Groups](/v3/portal/api/doc/AdGroup) | Ad group optimization uses Audience Booster, Prism, and Audience Predictor. | Certain ad group performance enhancements are not supported in GDPR regions. For details, see [Performance-Enhancing Features](/v3/portal/api/doc/AdGroup#ad-group-koa-features).  
In GraphQL API, the Prism is controlled at the advertiser level by the new `prism` property.  
**NOTE**: Prism is disabled for advertisers whose partners have opted out of fee-based features. |
| [CRM Data](/v3/portal/api/area/Crm%20Data) | Upload contains health data that originates within GDPR regions | Advertisers cannot upload health data that violates policy. |

> **NOTE**: Health advertisers are identified through self-categorization and review by The Trade Desk, of the advertised product.

## 

Next Steps[](#next-steps)

Now that you have your advertiser ID, you can [onboard](/v3/portal/data/doc/DataGetStartedAdvertiser) your data. If you've already done that, then you can create your [seeds](/v3/portal/api/doc/Seed) and [campaigns](/v3/portal/api/doc/Campaigns).

For the full workflow, see [Get Started for Advertisers](/v3/portal/api/doc/Advertisers).

## 

FAQs[](#faqs)

The following is a list of frequently asked questions about creating advertiser accounts.

### 

How do I find my industry category?

To retrieve categories in a taxonomy, make a [GET categorytaxonomy/13/category/industrycategories](/v3/portal/api/ref/get-categorytaxonomy-categoryTaxonomyId-category-industrycategories) call where `13` in the path is the (2.2) taxonomy ID.

Look through the list of the available categories and choose the one that applies to your industry. Here's a response snippet with two sample categories in IAB 2.2 taxonomy.

> **NOTE**: The Trade Desk uses the IAB Tech Lab Content Taxonomy [version 2.2](https://iabtechlab.com/wp-content/uploads/2020/12/Implementation_Guide_for_Brand_Suitability_with_IABTechLab_Content_Taxonomy_2-2.pdf) for assigning industry categories to advertisers. If you want to see how version 1.0 maps to version 2.2, see [IAB Content Taxonomy Mapping: Version 1.0 to 2.2](/v3/portal/openpath/doc/TaxonomyMapping).

\[

  {

    "CategoryId": 8311,

    "externalId": "568",

    "parentCategoryId": "1234",

    "name": "Women's Fashion",

    "path": "Style & Fashion\\\\Fashion",

    "children": \[\],

    "mappingInformation": \[

      {

         "CategoryTaxonomyId":2,

         "CategoryId":292,

         "ExternalId":"IAB18-5"

      }

    \]

  },

  {

    "categoryId": 7168,

    "externalId": "432",

    "parentCategoryId": "1234",

    "name": "Celebrity Fan/Gossip",

    "path": "Arts & Entertainment\\\\Celebrity Fan/Gossip",

    "children": \[\],

    "mappingInformation": \[

      {

        "CategoryTaxonomyId": 13,

        "categoryId": 3,

        "externalId": "IAB1-2"

      }

    \]

  }

\]

### 

Are there limitations to using industry categories?

Special considerations apply to some features based on the advertiser industry category. Ad groups associated with advertisers assigned to some industry categories and subcategories cannot use Koa Audience Predictor or Prism. Some of these industries include Careers, Health and Fitness, Personal Finance, and Real Estate.

### 

How do I attach a seed to an advertiser? And can I change the default seed for the advertiser?

The very first seed you create is automatically attached to the advertiser as the default seed. If you have more than one seed, you can replace the default seed with a different one. For details, see [Change Default Seed for an Advertiser](/v3/portal/api/doc/Seed#change-default).

### 

How do I disable deduplication?

To disable deduplication, do the following:

*   For clicks, set the `ClickDedupWindowInSeconds` property to `0`.
*   For conversions, set the `ConversionDedupWindowInSeconds` property to `0`.

### 

Do I have to link to an advertiser logo or brand image?

No. It is not required, but it is recommended that this value be set because a logo URL is necessary to bid on certain types of inventory from select supply vendors.

### 

How do I enable Prism for an advertiser?

You can enable Prism using GraphQL or REST. For details, see [Prism](/v3/portal/api/doc/Prism).

### 

Does changing Prism settings affect live ad groups?

No. Changing Prism settings does not affect any live ad groups.

### 

Why does the partner cost in retailer spend reports differ from the reports I generate?

Partner cost is calculated differently in retailer spend reports and the reports you generate in the platform, which may cause discrepancies. Here's the difference:

*   Retailer spend reports aim to provide retailers with a simplified spend view by attributing the full partner cost to them.
*   Your generated reports may duplicate or split partner cost depending on the report type and settings.

If you’re unsure how to compare the numbers, contact your Account Manager.

### 

Can I give consent to multiple retailers using bulk edits?

No. There are no bulk operations available. You must make multiple API calls.

### 

How do I stop sharing partner costs?

If you need to stop sharing your partner cost data with retailers, contact the Client Services team.