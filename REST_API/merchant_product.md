# Merchant Product

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Merchant%20Product
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Merchant%20Product (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### PUT /v3/ecommerce/advertiser/product/batch

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-advertiser-product-batch

Allow brands or advertisers to access specified product SKUs in a merchant's catalog. For details, see [Merchant Product Catalog](/v3/portal/data/doc/CommerceMerchantProductCatalog).

### PUT /v3/ecommerce/advertiser/products/add

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-advertiser-products-add

Allow a brand or advertiser to access specified product SKUs in a merchant's catalog. For details, see [Merchant Product Catalog](/v3/portal/data/doc/CommerceMerchantProductCatalog).

### POST /v3/ecommerce/advertiser/products/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-advertiser-products-query

Get a list of product SKUs associated with a brand or advertiser.

### PUT /v3/ecommerce/advertiser/products/remove

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-advertiser-products-remove

Remove access to product SKUs in a merchant's catalog from a brand or advertiser.

### PUT /v3/ecommerce/product/advertisers/add

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-product-advertisers-add

Allow multiple brands or advertisers to access a specific product SKU.

### POST /v3/ecommerce/product/advertisers/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-product-advertisers-query

Get Advertiser ID(s) associated to a Merchant SKU

### PUT /v3/ecommerce/product/advertisers/remove

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-product-advertisers-remove

Remove access to a product SKU in a merchant's catalog from multiple brands or advertisers.

### PUT /v3/ecommerce/product/batch

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-ecommerce-product-batch

Create new or update existing multiple products in a merchant's catalog. For details, see [Merchant Product Catalog](/v3/portal/data/doc/CommerceMerchantProductCatalog).  
This is an upsert batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### POST /v3/ecommerce/product/batch/delete

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-product-batch-delete

Delete products from a merchant's catalog. For details, see [Merchant Product Catalog](/v3/portal/data/doc/CommerceMerchantProductCatalog).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).

### POST /v3/ecommerce/product/batch/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-ecommerce-product-batch-query

Get multiple product details from a merchant's catalog. For details, see [Merchant Product Catalog](/v3/portal/data/doc/CommerceMerchantProductCatalog).  
This is a batch endpoint, which supports partial success. For details, see the _Commerce API Usage Overview_ section in [Retail Data Integration API](/v3/portal/data/doc/CommerceSolutionsAPI).
