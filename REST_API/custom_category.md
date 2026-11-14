# Custom Category

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Custom%20Category
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Custom%20Category (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/customcategory

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-customcategory

Create a contextual custom category. NOTE: This endpoint is only for creating [TTD contextual custom categories](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/ContextualCategoriesTTD). For third-party contextual custom categories, consider requesting access to the [Contextual Custom Category](/v3/portal/api/area/Contextual%20Custom%20Category) endpoints designated specifically for third-party data providers. Similarly, for direct URL targeting categories, consider requesting access to the [Direct Url Targeting Category](/v3/portal/api/area/Direct%20Url%20Targeting%20Category) endpoints.

### PUT /v3/customcategory

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-customcategory

Update the keywords or the language code of an existing contextual custom category.

### GET /v3/customcategory/advertiser/{advertiserId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-customcategory-advertiser-advertiserid

Retrieve a list of all TTD contextual custom categories that belong to a specific advertiser.

### GET /v3/customcategory/{customCategoryId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-customcategory-customcategoryid

Get an existing TTD contextual custom category.

### DELETE /v3/customcategory/{customCategoryId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/delete-customcategory-customcategoryid

Delete an existing custom category. Will not remove from any bid lists of ad groups.

### GET /v3/customcategory/name/{customCategoryId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-customcategory-name-customcategoryid

Retrieve the name of a custom category based on its ID.

### POST /v3/customcategory/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-customcategory-query

Retrieve a list of all custom categories that belong to a specific partner or advertiser by category type and data provider.

### POST /v3/customcategory/rename

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-customcategory-rename

Rename an existing custom category.

### GET /v3/customcategory/ttd/languages

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-customcategory-ttd-languages

Retrieve the names and codes of the supported languages for matching TTD contextual custom category keywords to webpages and apps.
