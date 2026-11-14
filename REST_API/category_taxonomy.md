# Category Taxonomy

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Category%20Taxonomy
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Category%20Taxonomy (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GET /v3/categorytaxonomy/{categoryTaxonomyId}/category/industrycategories

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-categorytaxonomy-categorytaxonomyid-category-industrycategories

Get a complete tree of industry categories, including root categories, for the specified taxonomy ID.  
You can traverse root categories to sub-categories within the taxonomy tree.

### GET /v3/categorytaxonomy/industrycategorytaxonomies

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-categorytaxonomy-industrycategorytaxonomies

Get a list of the available industry category taxonomies.
