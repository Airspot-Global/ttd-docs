# Create Advertisers

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/AdvertiserCreate
- Category: GraphQL / REST_API

---

## What You Need to Know (WYNTK)

Before you begin creating advertisers via the API, keep the following key points in mind:

*   **Partner ID:** You must have a valid `PartnerId` (provided during onboarding) to create an advertiser.
*   **Industry Categories:** The API uses **IAB Tech Lab Content Taxonomy version 2.2**. Certain sensitive categories (e.g., Lotteries, Scratchcards) require a valid subcategory for transparency.
*   **Currency:** The default currency is **USD**. If you choose another currency during creation, **this choice is permanent** and cannot be changed later for that advertiser.
*   **Settings Propagation:** Preferences set at the advertiser level (default frequency, bid lists, Prism settings) automatically propagate to child campaigns and ad groups but can be overridden individually.
*   **Additional Identifiers:** Tasks like data uploads may require the `AdvertiserKey` (secret key).

## REST API Endpoint

*   **Method:** `POST`
*   **URL:** `/v3/advertiser`

## Required Fields and Example Request (REST)

The following table describes the primary fields used to create an advertiser:

| Field | Type | Description |
| :--- | :--- | :--- |
| `PartnerId` | String | Unique identifier for your partner account (Required). |
| `AdvertiserName` | String | Name of the advertiser. |
| `Description` | String | Text description of the advertiser. |
| `Country` | String | Country code (e.g., "US", "FR"). |
| `CurrencyCode` | String | Currency code (e.g., "USD", "EUR"). Permanent after creation. |
| `AttributionClickLookbackWindowInSeconds` | Integer | Click-through conversion window (in seconds). |
| `AttributionImpressionLookbackWindowInSeconds` | Integer | View-through conversion window (in seconds). |
| `ClickDedupWindowInSeconds` | Integer | Click deduplication window. |
| `ConversionDedupWindowInSeconds` | Integer | Conversion deduplication window. |
| `AdvertiserCategory` | Object | Contains the `CategoryId` based on IAB 2.2 taxonomy. |
| `DomainAddress` | String | URL of the advertiser's domain. |

## Additional Requirements and Recommendations

*   **Political Campaigns:** Specific requirements apply for electoral campaigns (federal, state, or local).
*   **Regional Compliance (DSA/GDPR):** In regions like the EEA, UK, and Switzerland, you must include properties related to the **Digital Services Act (DSA)** and comply with EU health policies.
*   **Cost Transparency:** You can configure the sharing of monthly partner cost reports with retailers.
*   **Marketplace:** For audience-based buying, explore the *Sellers and Publishers 500+ Marketplace*.

## GraphQL Mutation

While the REST endpoint remains available, it is recommended to use the `advertiserCreate` mutation for expanded functionality.

```graphql
mutation CreateAdvertiser($advertiser: AdvertiserCreateInput!) {
  advertiserCreate(input: $advertiser) {
    advertiser {
      id
      name
    }
  }
}
```
