# Frequency Config

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Frequency%20Config
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Frequency%20Config (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/frequency/config

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-frequency-config

Create a frequency configuration. This endpoint enables you to streamline the creation of a [frequency counter](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Frequency%20Counter), associating entities to increment the counter, applying the frequency configuration to <a href="/v3/portal/api/area/Bid%20List">bid lists</a>, and associating bid lists to entities. See also [Basic Frequency Configuration Guidelines](/v3/portal/api/doc/FrequencyConfigurationBasic).

### PUT /v3/frequency/config

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-frequency-config

Update a frequency configuration.  
This endpoint enables you to streamline updating a [frequency counter](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Frequency%20Counter)  
associating entities to increment the counter, applying the frequency configuration to [bid lists](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Bid%20List), and associating the bid lists to entities. See also [Basic Frequency Configuration Guidelines](/v3/portal/api/doc/FrequencyConfigurationBasic).

### GET /v3/frequency/config/{counterId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-frequency-config-counterid

Retrieve the frequency configuration for the specified counter ID.  
This endpoint returns information for the [frequency counter](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Frequency%20Counter)  
entities associated to increment the counter, and [bid lists](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Bid%20List) where this frequency configuration is associated.

### DELETE /v3/frequency/config/{counterId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/delete-frequency-config-counterid

Delete the frequency configuration for the specified counter ID.  
IMPORTANT: This also deletes all bid lines and increments that reference the specified counter ID and the counter itself. If a bid list includes only one bid line, the entire bid list is deleted.

### POST /v3/frequency/config/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-frequency-config-query

Retrieve a paged, sorted, and filterable list of frequency configurations for the specified entity.

### POST /v3/frequency/config/query/bidlist

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-frequency-config-query-bidlist

Retrieve a paged, sorted, and filterable list of frequency configurations for specified bid list IDs.

### POST /v3/frequency/config/query/counter

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-frequency-config-query-counter

Retrieve a paged, sorted, and filterable list of frequency configurations for specified frequency counter IDs.
