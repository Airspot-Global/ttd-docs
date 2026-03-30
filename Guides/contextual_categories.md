# Contextual Categories

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/ContextualCategories
- Category: Guides

---

# Contextual Categories

Contextual targeting is an alternative to ID-based advertising: it analyzes the content being consumed instead of the person consuming it. This strategy enables you (advertiser) to target or block websites and apps based on the "context" of their content, and deliver relevant ads by matching identified keywords with the content of a website or an app, where an ad can potentially be placed. Alternatively, you can prevent your ads from being placed on pages and apps that have offensive content you do not want to be associated with your product. By using contextual targeting, you can reach customers at the right moment by matching your advertising with the content that the customers are consuming.

## 

Your Contextual Targeting Options[](#options)

As an advertiser, you can take advantage of contextual targeting by doing any of the following:

*   Using The Trade Desk standard contextual categories that are automatically available to all advertisers. No action needed.
*   Leveraging the third-party data provider categories available to you in the platform.
*   Declaring your own keywords and phrases and creating your own custom categories (known as TTD contextual custom categories) in the platform.

## 

Contextual Category Types[](#types)

Contextual data is categorized into sub-products that determine how contextual categories are displayed and priced. Based on the way keywords are defined and data ownership, contextual categories can be identified as standard or custom, originating from a third-party or The Trade Desk (also known as "TTD contextual").

### 

Third-Party vs. The Trade Desk Categories[](#types-ownership)

Third-party standard or custom contextual categories are owned by third-party data providers that define them in their own platforms and then upload them to The Trade Desk platform and make them available for partners and advertisers.

The Trade Desk standard or custom categories are built in The Trade Desk platform and are often referred to as "TTD contextual categories." The Trade Desk offers approximately 650 standard categories, which are automatically available in the platform and are not exposed through the API. For details, see [The Trade Desk's contextual targeting solution](https://desk.thetradedesk.com/knowledge-portal/en/faq-ttd-contextual-what.html) in the Knowledge Portal. For details on how to create and manage the TTD contextual custom categories, see [The Trade Desk Contextual Custom Categories](/v3/portal/api/doc/ContextualCategoriesTTD).

### 

Standard vs. Custom Categories[](#types-data)

Standard categories are predefined, curated categories that are tested for scale. These categories are created in accordance with IAB guidelines and include arts and entertainment, sports, finance, and so on. Standard categories are organized hierarchically.

Custom categories, as the name suggests, are lists of keywords and phrases that you or a data provider can build with customizations based on specific requirements.

## 

FAQs[](#faqs)

The following is a list of commonly asked questions about custom categories.

### 

What endpoints do I use to create different types of contextual categories?

The following table lists the sets of endpoints intended for each type of contextual category.

> **IMPORTANT**: The `contextualdata` endpoints are for only third-party data providers.

| Contextual Category Type | Standard | Custom | Notes |
| The Trade Desk  
(TTD contextual) | N/A, these are automatically available in the platform. | [Custom Category](/v3/portal/api/area/Custom%20Category)  
(`/customcategory` endpoints) | For usage, see [The Trade Desk Contextual Custom Categories](/v3/portal/api/doc/ContextualCategoriesTTD). |

### 

I see the CustomCategorySourceType property in the custom category endpoints. Can I use them to create third-party contextual custom categories?

No. Only third-party data providers can create third-party contextual custom categories.

### 

Can I look up other custom categories for a specific advertiser or partner, not just TTD contextual ones?

Yes. Use the [POST /v3/customcategory/query](/v3/portal/api/ref/post-customcategory-query) and select the source type you are interested in.

### 

Is direct URL targeting a type of contextual targeting?

No. As the name suggests, this type of targeting matches the specified URLs directly, not text context on a page.

### 

How often does The Trade Desk crawl websites and apps?

Daily. The crawler estimates how frequently a webpage changes. If the page has not changed since it was last time scraped, the interval is doubled up to a maximum of eight days. If the page has changed, the interval is halved to a minimum of one day. Therefore, the most frequently changing webpages are scraped daily.