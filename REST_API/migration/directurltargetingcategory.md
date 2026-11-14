# Direct url targeting category: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/directurltargetingcategory-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Direct url targeting category: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/directurltargetingcategory/{categoryId}` | `Query.directUrlTargetingCategory(categoryId:)` | Load a single category by ID |
| `POST /v3/directurltargetingcategory/query/partner` | `Partner.directUrlTargetingCategories` | Paged collection on `Partner` |
| `POST /v3/directurltargetingcategory` | `directUrlTargetingCategoryCreate` | Create a direct URL targeting category |
| `PUT /v3/directurltargetingcategory` | `directUrlTargetingCategoryUpdate` | Update a direct URL targeting category |

## Shared nested types and enums

### DirectUrlTargetingCategory

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CategoryId` | `categoryId` | ID! | Not nullable | Un-prefixed ID in API responses. |
| `CategoryName` | `categoryName` | String! | Not nullable | N/A |
| `CategoryType` | `categoryType` | CustomCategoryTypeREST! | Not nullable | N/A |
| `PartnerId` | `partner.id` | ID! | Not nullable | Nested `Partner` reference on read/query responses; create/update mutation `data` returns flat `partnerId`. |
| `IsDisabled` | `isDisabled` | Boolean | Nullable | Write-only on update; not populated on GET responses. |
| `Status` | `status` | CustomCategoryStatusREST | Nullable | Read-only on read/query responses. |

### CustomCategoryTypeREST

| REST value | GraphQL value |
| --- | --- |
| `Block` | `BLOCK` |
| `Target` | `TARGET` |
| `Unspecified` | `UNSPECIFIED` |

### CustomCategoryStatusREST

| REST value | GraphQL value |
| --- | --- |
| `NotReady` | `NOT_READY` |
| `Live` | `LIVE` |
| `Unusable` | `UNUSABLE` |
