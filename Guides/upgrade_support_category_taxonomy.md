# Industry category taxonomy migration

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/UpgradeSupportCategoryTaxonomy
- Retrieved: 2026-11-14
- Category: Guides

---

# Industry category taxonomy migration

In June 2023, The Trade Desk announced the migration from the currently supported version (1.0) of the IAB Tech Lab Content Taxonomy to version 2.2, which provides a common language that all parties—publishers, Server-Side Providers (SSPs), Demand-Side Providers (DSPs), verification vendors, and advertisers—can use and understand when describing the content of a page, app, or other user environment.

## Benefits

The IAB Tech Lab Content Taxonomy categorizes advertisers and their ad groups by industry within our platform, which is particularly useful for contextual targeting and brand safety. By upgrading to version 2.2, The Trade Desk accomplishes the following objectives:

- Improve support for partners and advertisers with multiple business lines or products.
- Surface more modern and detailed advertiser category options for general use.
- Improve support and protection for advertisers deemed to be associated with sensitive verticals, such as political, medical health, pharma, and financial.

## What you need to know

Here's what you need to know about this taxonomy migration:

-

With the introduction of new category options in version 2.2 of the IAB Tech Lab Content Taxonomy, your API integrations will be affected. You must update your advertiser and ad group workflows for the new taxonomy version by July 1, 2024.

-

The Trade Desk will complete the migration and map all categories for you on August 2, 2023.

-

Some categories in the old (1.0) taxonomy have one-to-one (1:1) relationships to the categories in the new taxonomy, while others have one-to-many (1:N) relationships. For details, see Category relationships between taxonomies. If your current industry category has a one-to-many (1:N) relationship to the new 2.2 taxonomy categories, and you want to change the automatically mapped category to a new one, you can request the change by contacting your Account Manager. If you want to see how version 1.0 maps to version 2.2, see IAB content taxonomy mapping: Version 1.0 to 2.2.

-

Two new properties will be introduced in the advertiser and ad group endpoints, `AdvertiserCategory` and `AdGroupCategory`, respectively, as well as two new endpoints. For details, see API updates.

-

Even though we recommend that you complete all required actions as soon as possible, the current version of the taxonomy will be supported in the API until July 1, 2024. Until then, the new properties will be optional.

### Current and new taxonomy information

The following table summarizes key details about the current and new taxonomies.

| IAB Taxonomy | IAB Taxonomy Version | The Trade Desk Taxonomy ID |
| --- | --- | --- |
| Current | 1.0 | `2` |
| New | 2.2 | `13` |

> **TIP**: You can look up this information by using the GET categorytaxonomy/industrycategorytaxonomies endpoint. For details, see Retrieve industry category taxonomy information.

### Category relationships between taxonomies

The following table lists the possible mapping relationship between the categories in taxonomy 1.0 to those in taxonomy 2.2.

| Relationship | 1.0 category example | 2.2 Equivalent | Migration description | Action required? |
| --- | --- | --- | --- | --- |
| 1:1 | IAB1-2 (Celebrity Fan/Gossip) | 432 (Pop Culture) | Categories with one-to-one relationships are automatically mapped on August 2, 2023. | No |
| 1:N | IAB18-5 (Clothing) | 567 (Women's Business Wear) 583 (Men's Business Wear) | If your IAB 1.0 category has multiple corresponding categories in the 2.2 taxonomy, it will be automatically mapped to a default category. | Only to change default category, if needed |

### Impact on your integration

Starting July 1, 2024, the POST, PUT, and GET advertiser and ad group endpoints will return only version 2.2 taxonomy categories and will require the new `AdvertiserCategory` and `AdGroupCategory` properties, respectively. The corresponding overview and bulk-edit endpoints will be also affected. Failure to update your workflows will result in 400 (Bad Request) errors.

### Required action

Update your advertiser and ad group workflows for the new taxonomy by July 1, 2024. For details, see Update advertiser and ad group workflows.

## Migration timeline

The following table lists the key dates in the industry taxonomy migration.

| Start date | Description | Action required? | End date |
| --- | --- | --- | --- |
| Aug 1, 2023 | The Trade Desk releases the API endpoints for the taxonomy migration. | No | N/A |
| Aug 2, 2023 | The Trade Desk automatically upgrades and migrates workflows with the new category mappings. | No | N/A |
| Nov 23, 2023 | With the introduction of the new properties, update all advertiser and ad group API workflows for the new taxonomy. Failure to do so will result in 400 (Bad Request) errors for the affected advertiser and ad group endpoints. For details, see Update advertiser and ad group workflows. | Yes | July 1, 2024 |

## API updates

As part the taxonomy migration, the following changes have been made to the Platform API:

- New and updated endpoints
- New properties in advertiser and ad group endpoint

### New and updated endpoints

The following table lists the new and existing endpoints that are affected by the migration.

| Endpoint | Description |
| --- | --- |
| GET categorytaxonomy/industrycategorytaxonomies | This new endpoint returns the ID, name, and version of the available industry category taxonomies. See response example. **NOTE**: There are only two taxonomies in the list: version 1.0 and version 2.2. This endpoint does not include the categories in each taxonomy. |
| GET categorytaxonomy/{categoryTaxonomyId}/category/industrycategories | This endpoint replaces GET /v3/categorytaxonomy/industrycategorytaxonomies and enables you to retrieve categories by their taxonomy ID. Responses include taxonomy mapping information, as shown in the provided response snippet examples. |
| POST, PUT, and GET advertiser POST, PUT, and GET ad group Corresponding overview and bulk-editing endpoints | Starting July 1, 2024, these endpoints will return only version 2.2 taxonomy categories and will require the `AdvertiserCategory` and `AdGroupCategory` properties, respectively. For details, see New properties in advertiser and ad group endpoint and Update advertiser and ad group workflows. |

### New properties in advertiser and ad group endpoints

Here's what you need to know about the new `AdvertiserCategory` and `AdGroupCategory` properties in the advertiser and ad group endpoints:

- The properties will be optional and will supersede the legacy `IndustryCategoryID` property, which will continue to return IAB 1.0 category IDs until July 1, 2024.
- Starting July 1, 2024, the two new properties will become required, while the legacy `IndustryCategoryID` property will be ignored.
- Both properties are object data types with the following structure:

```
{
  "CategoryId": 8311,
  "CategoryName": "Women's Fashion",
  "CategoryTaxonomyId": 13,
  "CategoryTaxonomyName": "IAB Content Categories v2.2",
  "CategoryTaxonomyVersion": "2.2",
  "Mappings":[
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
  ]
}
```

- Responses will always return the entire structure.
- In requests, only the `CategoryId` property will be required.
- Starting March 19, 2024, all responses will automatically return a list of category mappings in the `AdvertiserCategory` and `AdGroupCategory` properties.

For more details and examples, see Update advertiser and ad group workflows.

## Update advertiser and ad group workflows

By July 1, 2024, you must update all your POST, PUT, and GET advertiser and ad group endpoints and the corresponding overview and bulk-edit endpoints to include the new category information. For example, as shown in the following snippets with the required fields. See also New properties in advertiser and ad group endpoints.

### Request update examples

Here's an example snippet with the required new property for the advertiser create and update requests.

```
{
  "AdvertiserCategory":
  {
    "CategoryId": 8311
  }
}
```

Here's an example snippet with the required new property for the ad group create and update requests.

```
{
  "AdGroupCategory":
  {
    "CategoryId": 8311
  }
}
```

### New response example

Starting March 19, 2024, all advertiser and ad group responses will automatically return the respective industry category mappings in the `AdvertiserCategory` and `AdGroupCategory` properties, respectively.

Here's an example snippet of response to an advertiser call with the legacy `IndustryCategoryId` property, and new `AdvertiserCategory` property with all its metadata.

> **NOTE**: For ad group calls, the response will be identical in structure, except instead of the `AdvertiserCategory` property on line 3, there will be `AdGroupCategory` property.

```
{
   "IndustryCategoryId":292,
   "AdvertiserCategory":{
      "CategoryId":8311,
      "CategoryName":"Women's Fashion",
      "CategoryTaxonomyId":13,
      "CategoryTaxonomyName":"IAB Content Categories v2.2",
      "CategoryTaxonomyVersion":"2.2",
      "Mappings":[
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
      ]
   },
   "IndustryCategoryMapping":{
      "CategoryTaxonomyId":2,
      "CategoryId":8311,
      "ExternalId":"568"
   }
}
```

### Using legacy and new category properties

> **IMPORTANT**: Starting July 1, 2024, `AdvertiserCategory` and `AdGroupCategory` will be required properties in the respective advertiser and ad group workflows. You must update all your workflows. Otherwise, 400 (Bad Request) errors will be returned.

Since the new properties will be optional and will be used alongside the legacy `IndustryCategoryID` property until July 1, 2024, here's what you need to know about the new and legacy category ID properties in the advertiser and ad group requests:

- The legacy `IndustryCategoryId`property will be used exclusively for IAB 1.0 categories.

  - All responses in the updated workflows will automatically include the mapped 2.2 category information, even if only the legacy property is passed in a request.
  - If you pass a 2.2 category ID in this property, it will return a 1.0 category ID and set the `AdvertiserCategory` (or `AdGroupCategory`) property to the 2.2 category ID.
  - If a UI user creates an advertiser with a new, IAB 2.2 category, the `IndustryCategoryId`property will be automatically set to the matched 1.0 category ID.

- The new `AdvertiserCategory` and `AdGroupCategory` property will be used exclusively for IAB 2.2 categories in the respective advertiser and ad group workflows.

  - Each property will return the category ID as well as additional metadata, such as taxonomy name and version.
  - If you pass a 1.0 category ID in this property, it will return an error.

- If you pass both `IndustryCategoryId` property and `AdvertiserCategory` (or `AdGroupCategory`) property, the legacy value will be ignored, and the mapping information will be based on the `AdvertiserCategory` (or `AdGroupCategory`) property value.
- Starting July 1, 2024, the two new properties will become required, while the legacy `IndustryCategoryID` property will be ignored.

## Using new endpoints

The following sections provide examples of responses that the new endpoints return:

- Retrieve industry category taxonomy information
- Retrieve categories for a taxonomy ID

### Retrieve industry category taxonomy information

Here's an example of a GET categorytaxonomy/industrycategorytaxonomies response.

```
[
  {
    "CategoryTaxonomyId": 2,
    "CategoryTaxonomyName": "IAB Content Categories",
    "CategoryTaxonomyVersion": "1.0"
  },
  {
    "CategoryTaxonomyId": 13,
    "CategoryTaxonomyName": "IAB Content Categories v2.2",
    "CategoryTaxonomyVersion": "2.2"
  }
]
```

### Retrieve categories for a taxonomy ID

To retrieve categories in a taxonomy, do either of the following:

- To retrieve all 1.0 categories, make a GET categorytaxonomy/2/category/industrycategories call where `2` in the path is the old (1.0) taxonomy ID.
- To retrieve all 2.2 categories, make a GET categorytaxonomy/13/category/industrycategories call where `13` in the path is the new (2.2) taxonomy ID.

#### IAB 1.0 taxonomy categories response example

Here's a GET categorytaxonomy/2/category/industrycategories response snippet with two sample categories in IAB 1.0 taxonomy.

```
[
  {
    "categoryId": 292,
    "externalId": "IAB18-5",
    "parentCategoryId": "287",
    "name": "Fashion",
    "path": "Style & Fashion\\Fashion",
    "children": [],
    "mappingInformation": [
      {
        "CategoryTaxonomyId": 13,
        "CategoryId": 8311,
        "externalId": "568"
      },
      {
        "CategoryTaxonomyId": 13,
        "categoryId": 7498,
        "externalId": "579"
      }
    ]
  },
  {
    "categoryId": 3,
    "externalId": "IAB1-2",
    "parentCategoryId": "1",
    "name": "Celebrity Fan/Gossip",
    "path": "Arts & Entertainment\\Celebrity Fan/Gossip",
    "children": [],
    "mappingInformation": [
      {
        "CategoryTaxonomyId": 13,
        "categoryId": 7168,
        "externalId": "432"
      }
    ]
  }
]
```

#### IAB 2.2 taxonomy categories response example

Here's a GET categorytaxonomy/13/category/industrycategories response snippet with two sample categories in IAB 2.2 taxonomy.

```
[
  {
    "CategoryId": 8311,
    "externalId": "568",
    "parentCategoryId": "1234",
    "name": "Women's Fashion",
    "path": "Style & Fashion\\Fashion",
    "children": [],
    "mappingInformation": [
      {
         "CategoryTaxonomyId":2,
         "CategoryId":292,
         "ExternalId":"IAB18-5"
      }
    ]
  },
  {
    "categoryId": 7168,
    "externalId": "432",
    "parentCategoryId": "1234",
    "name": "Celebrity Fan/Gossip",
    "path": "Arts & Entertainment\\Celebrity Fan/Gossip",
    "children": [],
    "mappingInformation": [
      {
        "CategoryTaxonomyId": 13,
        "categoryId": 3,
        "externalId": "IAB1-2"
      }
    ]
  }
]
```

## FAQs

The following is a list of commonly asked questions about the advertiser category taxonomy migration.

### Do I have to take any action if my industry category is mapped automatically?

If you use the platform API, you must update all your advertiser and ad group workflows for the new taxonomy by July 1, 2024. For details, see Update Advertiser and Ad Group Workflows.

### Can I update my automatically mapped industry category?

Yes. Please contact your Account Manager.

> **IMPORTANT**: Be sure to update your API workflows accordingly. For details, see Update Advertiser and Ad Group Workflows.

### Should I include the IndustryCategoryMapping object in all my advertiser and ad group calls?

No. The `IndustryCategoryMapping` information will be automatically returned in all advertiser and ad group responses in the updated workflows.
