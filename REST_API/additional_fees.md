# Additional Fees

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Additional%20Fees
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Additional%20Fees (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/additionalfees

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-additionalfees

Creates an additional fee card with the given properties, including a list of fees to be applied, on the given owner type/id.  
Note that all additional fee card creates/updates must be scheduled at least one hour in the future unless the fee rate card is created within two minutes of campaign/ad group creation.

### PUT /v3/additionalfees

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-additionalfees

Updates the card with the given owner type/id with the given fees list, scheduled to become active at the given start time. Overwrites any and all fees with the given fee list at that start time. There can only be one pending update at any given time - using this method will overwrite any other pending updates for the given owner type/id, including pending stoppages/enddates. Note that all additional fee card creates/updates must be scheduled at least one hour in the future.

### POST /v3/additionalfees/changelog

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-additionalfees-changelog

Returns a list of changes to the additional fee card made (or scheduled to be made) between the start and end dates for the given owner type/id. Each additional fee card in the returned list represents the card as it was/is/will be between the start and end dates on that card.

### GET /v3/additionalfees/defaultfeecard/{advertiserId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-additionalfees-defaultfeecard-advertiserid

Returns the default fee card for the partner, useful for populating the InitialFeeCard property on the create campaign endpoint.

### GET /v3/additionalfees/{ownerType}/{ownerId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-additionalfees-ownertype-ownerid

Gets the current fee card for the given owner type/id. Note: in some cases, there will be no current fee card. Use the additionalfees/changelog endpoint instead to view future/past fee cards for this owner type/id.

### POST /v3/additionalfees/stop

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-additionalfees-stop

Ends the card at the end date given. Note: if any updates exist after the supplied end date, they will be deleted. This cannot be undone, so only use this endpoint when you're sure you want the card to end forever. Otherwise, use update and pass in an empty list of fees (nullifying the effect of the fee card). Note that all additional fee card ends must be scheduled at least one hour in the future.
