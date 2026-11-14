# Creative

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Creative
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Creative (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL creative Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/creative

Get a creative.

### GraphQL creatives Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/creatives

Get creatives

### GraphQL creativeUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/creative-update

Update Creative.

### GraphQL creativeAdGroupAssociate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/creative-ad-group-associate

Associate adgroups with the specified creative

### GraphQL adGroupCreativeSettingsUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-creative-settings-update

Set the ad group creative settings for the ad group

### POST /v3/creative

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-creative

Create a new [creative](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/Creative). See also [Creative Connector](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CreativeConnector).

### PUT /v3/creative

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-creative

Update an existing creative.

### GET /v3/creative/{creativeId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-creative-creativeid

Get a creative.

### POST /v3/creative/generateuploadurlforaudiocreative

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-creative-generateuploadurlforaudiocreative

Generates a URL which can be used to upload audio files before calling POST creative.  
The CreativeAudioUploadUrlAttributes returned in this call contains an AudioUploadAttributes property that must be cycled back to the POST creative call.

### POST /v3/creative/generateuploadurlforvideocreative

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-creative-generateuploadurlforvideocreative

Generates a URL which can be used to upload video files before calling POST creative.  
The CreativeVideoUploadUrlAttributes returned in this call contains a VideoUploadAttributes property that must be cycled back to the POST creative call.

### GET /v3/creative/name/{creativeId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-creative-name-creativeid

Get the identifier and name for a Creative based on identifier

### POST /v3/creative/query/advertiser

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-creative-query-advertiser

Get a page of Creatives that belong to the specified Advertiser.

### GET /v3/creative/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-creative-query-facets

Get the facets of Creatives that can be queried.
