# The Trade Desk contextual custom categories

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/ContextualCategoriesTTD
- Retrieved: 2026-11-14
- Category: Guides

---

# The Trade Desk contextual custom categories

> **NOTE**: This guide is intended for advertisers who want to create their own customized contextual categories in The Trade Desk platform, not third-party data providers.

Contextual targeting with The Trade Desk (also known as "TTD contextual") focuses on extracted text content and user-declared keywords rather than relying on contextual categories offered by a publisher. For category types, benefits of using contextual targeting, and other details, see Contextual categories.

> **TIP**: To assign them to ad groups, organize your categories into contextual groups and entities, which you can reuse across multiple ad groups and manage your targeting in one place. For details, see Contextual category configuration.

## Benefits

Here are some benefits of using contextual targeting:

- This is an alternative to ID-based advertising: analyze the content being consumed instead of the person consuming it.
- Spend only on inventory that meets your specific business goals with custom contextual categories.
- Leverage the matching capabilities of contextual targeting to better match your ad placements.
- Contextual targeting is supported both on web browsers and in in-app environments.
- Troubleshoot the impact of your selected keywords by using the scale insights in the UI. Scale insights give you a clear view of the projected scale in-platform at the keyword and category level.

To get started, create TTD contextual custom categories and apply them to your ad groups via Bid lists. After you enable your ad groups, they will include (target) or exclude (block) URLs where page content has text that matches your keywords or phrases.

For details on how this feature works in the platform UI, see The Trade Desk's contextual targeting solution in the Knowledge Portal.

## TTD contextual custom category anatomy

A TTD contextual custom category consists of the following major properties that are used for category targeting:

- A name that describes the category.
- An ID that is assigned at creation and is subsequently used to manage the category or apply it to ad groups.
- The category type:

  - `Target` (or `1`) for inclusion categories, which allow bids on the URLs and apps that match your keywords and phrases.
  - `Block` (or `0`) for exclusion categories, which block bids on the URLs and apps that match your keywords and phrases.

- A list made up of at least one keyword of phrase.
- A tactic that defines how impressions are evaluated against the category before a bid is placed. For details, see Contextual category configuration.

Each keyword in a category has the following properties:

| Property | Description |
| --- | --- |
| `Value` | The word or phrase to be searched for on webpages or in apps. For details, see Keyword value guidelines. |
| `MatchType` | The logic to be used for matching the keyword to webpages or apps. The possible values include the following: - `ExactMatch`: At least one specified keyword must be present on matched pages. (Or) - `ExactRequired`: All specified keywords must be present on matched pages. (And) - `ExactAvoid`: None of the specified keywords must be present on matched pages. (Not) See also Keyword matching examples and Create a TTD contextual custom category. |
| `MatchApplication` | The method for matching each keyword to webpages or apps. The possible values include the following: - `Exact`: Search only for words and phrases that exactly match the keyword string specified in the `Value` property. For example, for the keyword `"cat"`, the exact match would be `"cat"`.If there are multiple words in a phrase, they must appear in the same order on webpages and in apps. - `Similar`: Based on the specified language, search for words and phrases that are similar to the keyword string in the `Value` property. For example, for the keyword `"cat"`, similar words in English would be `"cat"`, `"cats"`, `"bobcats"`, `"catnip"`, and so on.If there are multiple words in a phrase, their order on webpages or in apps might be different, and other words that are not part of the keyword phrase might appear between the matched words. See also Keyword value guidelines. |

Here's a keyword example:

```
{
    "Value": "cat",
    "MatchType": "ExactRequired",
    "MatchApplication": "Similar"
}
```

## Keyword matching examples

Depending on the category type (Block or Target), keywords with the `ExactAvoid` match type value result in different bidding outcomes. Hence, it's worth taking time to understand the logic by reviewing the following examples.

> **NOTE**: The following simplified examples are provided to illustrate only the logic of the `ExactAvoid` match type. Ultimately, bidding is allowed or blocked based on _all_ category match settings satisfied in addition to the specific ones discussed in each example.

### Example 1

For example, the following Target category would match all webpages and apps that mention pets, but not cats. If you change the custom category type to `Block`, then you match content only about cats, pets in general, and any other content that complies with the other match settings. In other words, instead of avoiding content with references to cats and blocking bidding on those pages, a Block category does the opposite.

```
{
  "CustomCategoryName": "Pets",
  "CustomCategoryType": "Target",
  "Keywords": [
    {
      "Value": "cat",
      "MatchType": "ExactAvoid",
      "MatchApplication": "Similar"
    },
    {
      "Value": "pets",
      "MatchType": "ExactMatch",
      "MatchApplication": "Similar"
    }
  ],
  "LanguageCode": "eng",
  "AdvertiserId": "abcd1234",
  "CustomCategorySourceType": "TTDContextualCategory"
}
```

### Example 2

Here's another example of a list of keywords in a TTD contextual custom category. Depending on the category type, bidding is either allowed or blocked for webpages and apps with the word `religion` that has its match type set to `ExactAvoid`, assuming that all other match conditions are met.

```
[
    {
      "Value": "christmas",
      "MatchType": "ExactRequired",
      "MatchApplication": "Similar"
    },
    {
      "Value": "easter",
      "MatchType": "ExactRequired",
      "MatchApplication": "Similar"
    },
    {
      "Value": "baking",
      "MatchType": "ExactMatch",
      "MatchApplication": "Similar"
    },
    {
      "Value": "religion",
      "MatchType": "ExactAvoid",
      "MatchApplication": "Similar"
    }
]
```

Let's assume there are two sample inventories:

-

Website A that includes the following text: `This is a blog about preparing for Easter and Christmas. The blog includes recipes, religious practices, and more!`

-

Website B that includes the following text: `This is a blog about preparing for Easter and Christmas. The blog includes a guide to preparing all the food and baked goods you could dream of! Click the "Recipes" tab for more.`

If the keywords were used in an include (Target) category, then you would bid only on website B. If the keywords were used in an exclude (Block) category, then you would bid only on website A and any other website that is not like website B.

## TTD contextual custom category tasks

The following table lists the common tasks for TTD contextual custom categories and the respective endpoints.

| Task | Endpoint | Notes |
| --- | --- | --- |
| Create a category. | POST /v3/customcategory | Be sure to review the Category keyword list requirements and Keyword value guidelines. |
| Update the keywords, category type, or language code of an existing category. | PUT /v3/customcategory | To rename a category, use the POST /v3/customcategory/rename endpoint. |
| Look up a specific category and its TTD contextual category ID. | GET /v3/customcategory/{customCategoryId} | Just specify the custom category ID as the path parameter in your request. **IMPORTANT**: The response includes the `TTDContextualCategoryId` value that is required for including the category in bid lists. |
| Look up all custom categories for a specific advertiser. | GET /v3/customcategory/advertiser/{advertiserId} | Just specify the advertiser ID as the path parameter in your request. |
| Look up all custom categories for a specific partner. | POST /v3/customcategory/query | In the body of your request, specify the partner ID and set the `CustomCategorySourceType` property to `TTDContextualCategory`. |
| Delete a category. | DELETE /v3/customcategory/{customCategoryId} | Just specify the custom category ID as the path parameter in your request. **IMPORTANT**: Deleting categories removes them from ad groups, which may result in the loss of historical usage data. |
| Include a category as a bid line in a bid list. | POST /v3/bidlist PUT /v3/bidlist | Bid lines require the `TTDContextualCategoryId` value returned by GET /v3/customcategory/{customCategoryId} calls with the `ttd-ct-` prefix added to it. |

## Create a TTD contextual custom category

To create a contextual custom category in The Trade Desk platform, in a POST /v3/customcategory request, specify its name, type, your advertiser or partner ID, and at least one keyword. For guidelines and requirements, see the following sections.

### Category keyword list requirements

Here's what you need to know about keywords and phrases in a TTD contextual custom category:

- The maximum limit is 5,000. For best results, lists should contain fewer than 2,000 keywords or phrases.
- A category must have at least one keyword with the `MatchType` property value set to `ExactMatch` (Or).
- You can add a maximum of five keywords with the `MatchType` property value set to `ExactRequired` (And) per category.
- For any keywords with the `MatchApplication` property value set to `Similar`, be sure to specify the three-letter ISO639-3 language code. To get the list of supported languages and their codes, use the GET/customcategory/ttd/languages endpoint.

> **IMPORTANT**: For exclusion categories (with the `CustomCategoryType` property set to `Block`), setting the keyword `MatchType` property value to `ExactAvoid` allows bids on pages and apps containing the specified keywords rather than blocking bids. For details, see Keyword matching examples.

### Keyword value guidelines

You can specify any word or phrase as a keyword in a contextual custom category. Here's what you need to know:

- Keywords and phrases are not case-sensitive. For example, `"USA"` and `"usa"` will result in duplicate keywords.
- You can use only alphanumeric characters, spaces between words in the middle of a phrase, and apostrophes.
- Spaces around keywords (namely, at the beginning or the end of the phrase) will be automatically removed. For example, `"cat food"` and `" cat food "` will result in duplicate keywords.
- Do not use quotation marks when you enter keywords or phrases. If you use any special characters and punctuation other than apostrophes when you enter keywords or phrases, these be automatically removed during the matching and might result in duplicate keywords.
- The maximum keyword string length is 100 characters, including spaces.
- For any keywords with the `MatchApplication` property set to `Similar`, you don't need to enter permutations of the same word, such as the plural and singular nouns or different forms of the same verb. For example, if you enter keyword `work`, all other forms like `works`, `worked`, `has been working`, `will have been worked`, and `workings` are matched.

### Create request body example

The following is an example of POST /v3/customcategory request body that creates a TTD contextual custom category.

```
{
  "CustomCategoryName": "Cat Food",
  "CustomCategoryType": "Target",
  "Keywords": [
    {
      "Value": "cat",
      "MatchType": "ExactRequired",
      "MatchApplication": "Similar"
    },
    {
      "Value": "food",
      "MatchType": "ExactRequired",
      "MatchApplication": "Similar"
    },
    {
      "Value": "feline",
      "MatchType": "ExactMatch",
      "MatchApplication": "Similar"
    },
    {
      "Value": "pet",
      "MatchType": "ExactMatch",
      "MatchApplication": "Similar"
    },
    {
      "Value": "dog",
      "MatchType": "ExactAvoid",
      "MatchApplication": "Similar"
    }
  ],
  "LanguageCode": "eng",
  "AdvertiserId": "abcd1234",
  "CustomCategorySourceType": "TTDContextualCategory"
}
```

### Response example

The response returns the platform ID assigned to the category, its keyword count, and status.

```
{
 "CustomCategoryId": "123456",
 "CustomCategoryName": "Cat Food",
 "CustomCategoryType": 1,
 "KeywordCount": 5,
 "AdvertiserId": "abcd1234",
 "PartnerId": null,
 "Status": "NotReady",
 "LanguageCode": "eng"
}
```

For details on applying categories to ad groups, see Include TTD contextual custom category in bid lines.

> **IMPORTANT**: Be sure to wait until the category is live before enabling your ad groups, especially for exclusion categories (with the `CustomCategoryType` property value set to `Block`). It takes up to three hours to process a category, and any bidding on inventory before the category is fully processed might result in not blocking webpages or apps with the specified keywords.

## Update a TTD contextual custom category

To update the keywords, category type, or language code of an existing category, in a PUT /v3/customcategory request, specify the category ID, your advertiser or partner ID, and the keyword or language changes you want to make. To rename a category, use the POST /v3/customcategory/rename endpoint.

> **IMPORTANT**: If updating keywords, be sure to review the Category keyword list requirements and Keyword value guidelines and send the whole list for every update, even if you are updating only the language code.

The following is an example of PUT /v3/customcategory request body with a keyword added to the list.

```
{
  "CustomCategoryId": "123456",
  "Keywords": [
    {
      "Value": "cat",
      "MatchType": "ExactRequired",
      "MatchApplication": "Similar"
    },
    {
      "Value": "food",
      "MatchType": "ExactRequired",
      "MatchApplication": "Similar"
    },
    {
      "Value": "feline",
      "MatchType": "ExactMatch",
      "MatchApplication": "Similar"
    },
    {
      "Value": "pet",
      "MatchType": "ExactMatch",
      "MatchApplication": "Similar"
    },
    {
      "Value": "dog",
      "MatchType": "ExactAvoid",
      "MatchApplication": "Similar"
    },
    {
      "Value": "canine",
      "MatchType": "ExactAvoid",
      "MatchApplication": "Similar"
    }
  ],
  "LanguageCode": "eng",
  "AdvertiserId": "abcd1234",
  "CustomCategorySourceType": "TTDContextualCategory"
}
```

## Include a TTD contextual custom category in bid lines

> **TIP**: For a more flexible, reusable approach to applying categories to campaigns, use contextual entities instead of bid lists. Contextual entities enable you organize categories into groups, reuse configurations across ad groups, and manage your targeting in one place. For details, see Contextual category configuration.

To apply a TTD contextual custom category to an ad group, you need to include the category ID as a `TTDContextualCategoryId` bid line to a bid list associated with the ad group.

Here's what you need to know:

- You can add a contextual category to a bid list when creating or updating the bid list.
- The bid line `TTDContextualCategoryId` value is not the same as the `CustomCategoryId` value returned by the Custom category endpoints. It must be formatted for use in bid lists.
- The Bid list endpoints ignore the custom category type specified for the custom category when it was created. Instead, be sure to set the bid line `BidAdjustment` property to `1` (target) or `0` (block).

To add a TTD contextual custom category to a bid list, follow these steps:

1. If you don't know your custom category ID, use the GET /v3/customcategory/advertiser/{advertiserId} to look it up.
2. Use the returned `CustomCategoryId` value as the path parameter in a GET /v3/customcategory/{customCategoryId} call, which returns the preformatted `TTDContextualCategoryId` value for the category.
3. Add the `ttd-ct-` prefix to the returned `TTDContextualCategoryId` value. For example, if the returned value is `123456`, update it to `ttd-ct-123456`.
4. In a POST /v3/bidlist or PUT /v3/bidlist call, include the updated ID value with the prefix in the `TTDContextualCategoryId` bid line property.

Here's an example of a bid list request body snippet with an exclusion TTD contextual custom category included as a bid line with the bid adjustment set to `0` (block):

```
{
    "Name": "CustomCategoryBidListTest",
    "BidListAdjustmentType": "BlockList",
    "ResolutionType": "ApplyMultiplyAdjustment",
    "BidLines": [
        {
            "BidAdjustment": 0,
            "TTDContextualCategoryId": "ttd-ct-123456"
        }
    ],
    "BidListOwner": "Advertiser",
    "BidListOwnerId": "abcd1234"
}
```

## FAQs

The following is a list of commonly asked questions about custom categories. See also the The Trade Desk's contextual targeting solution FAQs in the Knowledge Portal and Contextual categories FAQs.

### Does "TTD contextual" refer only to The Trade Desk contextual custom categories?

No. Even though this term is most commonly used with reference to The Trade Desk contextual custom categories, it may also refer to The Trade Desk contextual standard categories.

### What happens if I have duplicate keywords in a category?

You will receive a validation error, and your category will not be created or updated.

> **IMPORTANT**: Duplicate keywords might result from using different capitalization for the same words, spaces around key value strings, and special characters. For details, see Keyword value guidelines.

### How can I tell how many keywords are in a category?

All Custom category query endpoints, except GET /v3/customcategory/{customCategoryId}, return the number of keywords and phrases in the `KeywordCount` response property. The GET /v3/customcategory/{customCategoryId} endpoint returns a list of keywords.

### How long does it take to process a newly created or updated category?

It takes up to three hours to process a category, and any bidding on inventory before the category is fully processed might result in not blocking webpages or apps with the specified keywords.

### What happens if I assign categories in NotReady status to ad groups?

Assigning categories that are not processed yet to an ad group might result in unexpected bidding behavior.

> **IMPORTANT**: We strongly recommend waiting until the category is live before enabling your ad groups, especially for exclusion categories (with the `CustomCategoryType` property value set to `Block`). It takes up to three hours to process a category, and any bidding on inventory before the category is fully processed might result in not blocking webpages or apps with the specified keywords.

### Can I send a PUT request only with the keywords that I want to update?

No, you must send the whole list every time you update a category.

### How do I apply TTD contextual custom categories to ad groups?

By including TTD contextual category IDs in bid lines of bid lists, which you then associate with ad groups when creating or updating ad groups. For details, see Include a TTD contextual custom category in bid line.

### What's the difference between the CustomCategoryId and TTDContextualCategoryId property values?

The `CustomCategoryId` value returned by the Custom category endpoints. The `TTDContextualCategoryId` value is the formatted TTD contextual custom category ID intended for use in bid lists. For details, see Include a TTD contextual custom category in bid line.

### How do I target webpages by their URLs instead of their content?

By using the Direct URL targeting category endpoints. Be sure to contact your Technical Account Manager for access.

## Troubleshooting

### Why are webpages with the keywords that I expressly set to avoid get matched instead?

The following table provides possible solutions.

| Possible Issue | Description | Solution |
| --- | --- | --- |
| Category status | Your category might be still in `NotReady` status. It takes up to three hours to process a category, and any bidding on inventory before the category is fully processed might result in not blocking webpages or apps with the specified keywords. | Be sure to wait until the category is live before enabling your ad groups, especially for exclusion categories (with the `CustomCategoryType` property value set to `Block`). |
| Category and match type mismatch | The `CustomCategoryType` property to `Block` and the keyword `MatchType` property value to `ExactAvoid`. This allows bids on pages and apps that contain the specified keywords rather than blocking bids. | To block bidding on webpages or apps with certain keywords or phrases, change the `CustomCategoryType` property to `Target`. See the example after this table. |

For example, with the following Block category, you bid only on content about cats and pets in general but won't bid on content about other specific pets. If you change the custom category type to `Target`, then you bid only on all webpages and apps that mention pets, but not cats. See also Keyword matching examples.

```
{
  "CustomCategoryName": "Pets",
  "CustomCategoryType": "Block",
  "Keywords": [
    {
      "Value": "cat",
      "MatchType": "ExactAvoid",
      "MatchApplication": "Similar"
    },
    {
      "Value": "pets",
      "MatchType": "ExactMatch",
      "MatchApplication": "Similar"
    }
  ],
  "LanguageCode": "eng",
  "AdvertiserId": "abcd1234",
  "CustomCategorySourceType": "TTDContextualCategory"
}
```
