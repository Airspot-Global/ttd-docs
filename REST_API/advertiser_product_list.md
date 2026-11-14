# Advertiser Product List

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Advertiser%20Product%20List
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Advertiser%20Product%20List (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/ecommerce/list/batch

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-list-batch

Create multiple lists for retargeting and measurement using a merchant's product data. For details, see [Advertiser Product Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceAdvertiserProductList).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### PUT /v3/ecommerce/list/batch

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-list-batch

Update the names and/or descriptions of multiple product lists. For details, see [Advertiser Product Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceAdvertiserProductList).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### POST /v3/ecommerce/list/batch/clone

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-list-batch-clone

Clone multiple product lists along with their contents (product SKUs from a merchant's catalog). For details, see [Advertiser Product Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceAdvertiserProductList).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### POST /v3/ecommerce/list/batch/delete

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-list-batch-delete

Delete multiple product lists. For details, see [Advertiser Product Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceAdvertiserProductList).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### POST /v3/ecommerce/list/batch/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-list-batch-query

Get the names, descriptions, and creation and last update timestamps for multiple product lists. For details, see [Advertiser Product Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceAdvertiserProductList).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### PUT /v3/ecommerce/list/products/add

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-list-products-add

Add multiple SKUs from a merchant's catalog to a product list. For details, see [Advertiser Product Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceAdvertiserProductList).

### PUT /v3/ecommerce/list/products/remove

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-list-products-remove

Remove multiple SKUs from a product list. For details, see [Advertiser Product Lists](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceAdvertiserProductList).

### PUT /v3/ecommerce/list/rules/add

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-list-rules-add

Ensure the provided rules are applied to a dynamic list. Missing rules are created, existing ones are validated.

### POST /v3/ecommerce/list/rules/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-list-rules-query

Query rules applied to a dynamic list.

### PUT /v3/ecommerce/list/rules/remove

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-list-rules-remove

Remove the specified rules applied to a dynamic list.

### POST /v3/ecommerce/list/sku/batch/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-list-sku-batch-query

Get SKUs of all products added to multiple product lists.  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### POST /v3/ecommerce/list/targetingdata

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-list-targetingdata

Create multiple targeting data for a product list  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### POST /v3/ecommerce/list/trackingtag

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-list-trackingtag

Create product list tracking tags for merchant event names.  
This is a batch endpoint, which supports partial success. For details, see [Product List Tracking Tags](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CommerceTrackingTag).
