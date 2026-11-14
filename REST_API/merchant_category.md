# Merchant Category

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Merchant%20Category
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Merchant%20Category (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### PUT /v3/ecommerce/category/batch

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-category-batch

Create new or update existing First Party categories in a merchant's product catalog. For details, see [Merchant Product Catalog](/v3/portal/data/doc/CommerceMerchantProductCatalog).  
This is an upsert batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).  
If your merchant is setup with a Third Party Category Provider such as Google, Facebook, or Shopify, you are not authorized to modify categories via this endpoint.

### POST /v3/ecommerce/category/batch/delete

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-category-batch-delete

Delete multiple categories from a merchant's product catalog.  
IMPORTANT: To delete a category, you must reassign or delete any associated products and reassign or delete its child categories, if the category has any. For details, see [Merchant Product Catalog](/v3/portal/data/doc/CommerceMerchantProductCatalog).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).  
If your merchant is setup with a Third Party Category Provider such as Google, Facebook, or Shopify, you are not authorized to modify categories via this endpoint.

### POST /v3/ecommerce/category/batch/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-category-batch-query

Get multiple category details from a merchant's product catalog. For details, see [Merchant Product Catalog](/v3/portal/data/doc/CommerceMerchantProductCatalog).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).
