# Contextual Categories

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/ContextualCategories
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/ContextualCategories (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Contextual targeting

Contextual targeting is an alternative to ID-based advertising: it analyzes the content being consumed instead of the person consuming it. This strategy enables you (advertiser) to target or block websites and apps based on the "context" of their content, and deliver relevant ads by matching identified keywords with the content of a website or an app, where an ad can potentially be placed. Alternatively, you can prevent your ads from being placed on pages and apps that have offensive content you do not want to be associated with your product. By using contextual targeting, you can reach customers at the right moment by matching your advertising with the content that the customers are consuming.

## Your contextual targeting options

As an advertiser, you can take advantage of contextual targeting by doing any of the following:

- Using The Trade Desk standard contextual categories that are automatically available to all advertisers.
- Leveraging the third-party data provider categories available to you in the platform.
- Declaring your own keywords and phrases and creating your own custom categories (known as TTD contextual custom categories) in the platform.

## Contextual category types

Contextual data is categorized into sub-products that determine how contextual categories are displayed and priced. Based on the way keywords are defined and data ownership, contextual categories can be identified as standard or custom, originating from a third-party provider or The Trade Desk (also known as "TTD contextual").

### Third-party vs. The Trade Desk categories

Third-party standard or custom contextual categories are owned by third-party data providers that define them in their own platforms and then upload them to The Trade Desk platform and make them available for partners and advertisers. Each third-party category has a tactic pre-assigned by its provider. The tactic determines how the platform evaluates impressions against the category before bidding and controls which categories you can group together in your targeting configuration. For details, see Tactics.

The Trade Desk standard or custom categories are built in The Trade Desk platform and are often referred to as "TTD contextual categories." The Trade Desk offers approximately 650 standard categories, which are automatically available in the platform and are not exposed through the API. For details, see The Trade Desk's contextual targeting solution in the Knowledge Portal. For details on how to create and manage the TTD contextual custom categories, see The Trade Desk contextual custom categories.

### Standard vs. custom categories

Standard categories are predefined, curated categories that are tested for scale. These categories are created in accordance with IAB guidelines and include arts and entertainment, sports, finance, and so on. Standard categories are organized hierarchically.

Custom categories, as the name suggests, are lists of keywords and phrases that you or a data provider can build with customizations based on specific requirements.

## Next steps

- To create your own custom categories, see TTD contextual custom categories.
- To organize your categories, whether third-party or TTD contextual custom, into contextual groups and entities and assign them to ad groups, see Contextual category configuration.

## FAQs

The following is a list of commonly asked questions about contextual targeting.

### What endpoints do I use to create different types of contextual categories?

The following table lists the endpoints available for each contextual category type.

| Category Type | Standard | Custom |
| --- | --- | --- |
| TTD contextual | N/A. Standard categories are automatically available in the platform. | /customcategory endpoints. For usage, see The Trade Desk contextual custom categories. |
| Third-party | N/A. Standard categories are uploaded by providers and available in the platform. | `contextualdata` endpoints, which available only to third-party data providers. Advertisers cannot create third-party custom categories. |

### I see the CustomCategorySourceType property in the custom category endpoints. Can I use them to create third-party contextual custom categories?

No. Only third-party data providers can create third-party contextual custom categories.

### Can I look up other custom categories for a specific advertiser or partner, not just TTD contextual ones?

Yes. Use the POST /v3/customcategory/query and select the source type you are interested in.

### Is direct URL targeting a type of contextual targeting?

No. As the name suggests, this type of targeting matches the specified URLs directly, not text context on a page.

### How often does The Trade Desk crawl websites and apps?

Daily. The crawler estimates how frequently a webpage changes. If the page has not changed since it was last time scraped, the interval is doubled up to a maximum of eight days. If the page has changed, the interval is halved to a minimum of one day. Therefore, the most frequently changing webpages are scraped daily.
