# Campaign Creation Payload Guide

- Source: https://partner.thetradedesk.com/v3/portal/api/area/Campaign
- Category: Guides

---

# Creating a Campaign in The Trade Desk

To create a campaign, you can use either the modern **GraphQL API** (recommended) or the legacy **REST API**. In both cases, a successful creation requires defining the advertiser, budget, dates (via a Flight), and at least one primary goal.

---

## 1. GraphQL approach (Recommended)

The `campaignCreate` mutation is the prioritized method for creating campaigns in the Kokai platform. It allows for complex batching and provides improved performance.

### Mutation
```graphql
mutation CreateNewCampaign($input: [CampaignCreateInput!]!) {
  campaignCreate(input: $input) {
    campaigns {
      campaignId
      campaignName
      status
    }
    errors {
      code
      message
      field
    }
  }
}
```

### JSON Variables Example
> [!IMPORTANT]
> Modern campaigns in Kokai **require a Seed ID**. Ensure you have created a seed prior to campaign creation.

```json
{
  "input": [
    {
      "advertiserId": "adv-12345",
      "campaignName": "Spring 2026 Brand Awareness",
      "channel": "DISPLAY",
      "campaignPrimaryGoal": {
        "type": "CPC" 
      },
      "flights": [
        {
          "budgetName": "Initial Launch Flight",
          "budgetInAdvertiserCurrency": 5000.00,
          "startDate": "2026-04-10T00:00:00Z"
        }
      ],
      "seedId": "seed-67890"
    }
  ]
}
```

---

## 2. REST API Approach (Legacy)

If you are using the REST API, you must ensure you are targeting the current platform version by specifying `Version: "Kokai"`.

### Endpoint
`POST /v3/campaign`

### Request Payload
```json
{
  "AdvertiserId": "adv-12345",
  "CampaignName": "Spring 2026 Brand Awareness",
  "PrimaryChannel": "Display",
  "Version": "Kokai",
  "IncludeDefaultsFromAdvertiser": true,
  "PrimaryGoal": {
    "MaximizeReach": true
  },
  "SecondaryGoal": {
    "MaximizeLtvIncrementalReach": true
  },
  "CampaignConversionReportingColumns": [],
  "MarketplaceOptOut": false
}
```
*Note: In the REST API, a follow-up request is typically required to define the Flight if not included in the default advertiser settings.*

---

## 3. Targeting & Ad Group Creation

> [!IMPORTANT]
> **Ad Group Level Targeting**: While Campaigns serve as containers, specific targeting constraints like **Demographics** and **Geography** are defined at the **Ad Group** level within the `RTBAttributes` object.

### Demographic Targeting
Pass these in the `DemographicTargeting` object.
- **Age Ranges**: `AgeRangeTargeting.AgeRanges` (e.g., `["Age_18_24", "Age_25_34"]`)
- **Genders**: `GenderTargeting.Genders` (e.g., `["Male", "Female"]`)

### Geographic Targeting
Pass these in the `GeographyTargeting` object.
- **Geography**: `LocationTargeting.Locations` as an array of objects with `LocationId`.

---

## 4. Ad Group Creation Payloads

### GraphQL `adGroupCreate` (Recommended)
```json
{
  "input": {
    "campaignId": "campaign-123",
    "name": "Targeted Ad Group",
    "rtbAttributes": {
      "maxBidCPM": { "amount": 5.0, "currencyCode": "USD" },
      "demographicTargeting": {
        "ageRangeTargeting": { "ageRanges": ["Age_18_24", "Age_25_34"] },
        "genderTargeting": { "genders": ["Male"] }
      },
      "geographyTargeting": {
        "locationTargeting": { "locations": [ { "locationId": 1234 } ] }
      }
    }
  }
}
```

### REST `POST /v3/adgroup` (Legacy)
```json
{
  "CampaignId": "campaign-123",
  "AdGroupName": "Targeted Ad Group",
  "RTBAttributes": {
    "MaxBidCPM": { "Amount": 5.0, "CurrencyCode": "USD" },
    "DemographicTargeting": {
      "AgeRangeTargeting": { "AgeRanges": ["Age_18_24", "Age_25_34"] },
      "GenderTargeting": { "Genders": ["Male"] }
    },
    "GeographyTargeting": {
      "LocationTargeting": { "Locations": [ { "LocationId": 1234 } ] }
    }
  }
}
```

---

## 5. Key Field Definitions

| Field | API | Level | Description |
| :--- | :--- | :--- | :--- |
| `AdvertiserId` | Both | Campaign | The platform ID for the advertiser entity. |
| `CampaignName` | Both | Campaign | A descriptive name for the campaign. |
| `PrimaryChannel`| Both | Campaign | The main inventory channel (e.g., `Display`, `Video`). |
| `RTBAttributes` | Both | Ad Group | Container for all real-time bidding targeting logic. |
| `LocationId` | Both | Ad Group | Unique ID from the TTD Geography taxonomy. |

---

## 6. Best Practices
- **Ad Group for Granularity**: Use different Ad Groups for different demographic segments or geographic regions to optimize bidding more effectively.
- **Use GraphQL**: For new integrations, GraphQL is the only API that supports all modern Kokai features natively.
- **Set Up Seeds First**: You cannot create a Kokai campaign without a valid `SeedId`.

---

## 7. Creative Association & Variation Linking

In the Kokai campaign provisioning workflow:
1. **Ad Variation Resolution**: Each variation in the campaign must be resolved to a valid Trade Desk Creative ID (`dsp_creative_id` / `ttd_creative_id`) before provisioning.
2. **Ad Group Assignment**: Ad variations map directly to generated ad groups within the campaign container.
3. **Draft vs Launch Rules**:
   - **Draft Campaigns**: Can be persisted in Airspot DB without assigned creatives or DSP identifiers. No calls are dispatched to external DSPs.
   - **Active Launches**: Must have valid creative assignments for all ad variations prior to calling `POST /api/campaigns/provider`. Any variation lacking a creative ID must be rejected with validation errors to prevent upstream DSP provisioning failure.

### Campaign Lifecycle Status & Availability Normalization

Kokai GraphQL and REST APIs handle campaign status differently depending on whether you are creating or updating an existing campaign:

1. **Initial Creation**: In `campaignCreate`, status can be passed as `AVAILABLE` or `PAUSED`. (`ACTIVE` is not a valid enum value in Kokai GraphQL).
2. **Status Updates (Pause / Resume)**:
   > [!WARNING]
   > **`CampaignUpdateInput` Has No Status Field**:
   > In Kokai GraphQL, `campaignUpdate` mutation takes `CampaignUpdateInput`, which **strictly does not define a `status` or `availability` field** (`GRAPHQL_VALIDATION_FAILED: Field "status" is not defined by type "CampaignUpdateInput"`).
   >
   > **TTD REST `Availability` Constraint**:
   > On REST `PUT /v3/campaign`, the `Availability` field represents entity persistence and **only accepts `"Available"` or `"Archived"`**.
   > Passing `"Paused"` causes an HTTP 400 .NET deserialization error:
   > `"Error deserializing the request as JSON: The value 'Paused' is not valid for this property."`
   >
   > **Canonical Status Update Procedure via Child Ad Groups**:
   > In The Trade Desk, a campaign's bidding status is an aggregate state driven by its child ad groups:
   > - `PAUSED`: Campaign has current flight, but none of its ad groups are enabled.
   > - `LIVE`: Campaign has current flight with enabled ad groups.
   >
   > To **pause** a campaign, query its child ad groups directly via the campaign-scoped query (`POST /v3/adgroup/query/campaign` or GraphQL `campaign.adGroups`) and disable each ad group concurrently via `PUT /v3/adgroup` with `IsEnabled: false`.
   > To **resume** a campaign, enable its child ad groups via `PUT /v3/adgroup` with `IsEnabled: true`, and ensure the campaign container has `Availability: "Available"`.
   >
   > **Container Update Bypass**: When only operational status (`active`) is toggled without changes to container fields (`CampaignName`, `Budget`, `StartDate`, `EndDate`), bypass `PUT /v3/campaign` entirely. This eliminates redundant roundtrips and avoids partner-tier permission failures.
   >
   > When updating container fields, always sanitize the update payload: purge read-only audit fields (`CreatedAtUTC`, `LastUpdatedAtUTC`, `CreatedBy`, `LastUpdatedBy`, `AuditTrail`), partner-restricted settings (`FrequencySettings` - which triggers `HTTP 403 Forbidden` if the partner seat lacks campaign-level capping; `PartnerCostPercentageFee`, `PartnerCPCFee`, `PurchaseOrderNumber`), and permanently deprecated attributes (`CtvTargetingAndAttribution` - sunset January 12, 2026; `UseIdentityAlliance`; `AdBrainHouseholdCrossDeviceEnabled*`).

| Airspot Status | Initial Creation (GraphQL) | Status Updates (REST & Ad Groups) | Description |
| :--- | :--- | :--- | :--- |
| `ACTIVE` | `status: AVAILABLE` | `Availability: "Available"` + Child Ad Groups `IsEnabled: true` | Campaign is active and bidding across ad groups. |
| `PAUSED` | `status: PAUSED` | `Availability: "Available"` + Child Ad Groups `IsEnabled: false` | Campaign is paused; bidding is halted by disabling child ad groups. |
| `ARCHIVED` | N/A | `campaignsArchive` GraphQL mutation or `Availability: "Archived"` | Campaign is archived; read-only. |
| `DRAFT` | *Local DB Only (no API call)* | *Local DB Only (no API call)* | Campaign is stored locally in Airspot; no DSP entity exists yet. |

### 7.1 Ad Group Resolution Strategy for Child Variations

When provisioning variations for a newly cloned or created campaign, resolving existing base ad groups must be resilient against schema or network nuances:

1. **REST-First Discovery**: Query the campaign-scoped REST endpoint `POST /v3/adgroup/query/campaign` (`TtdRestService.listAdGroups`). This delivers high-throughput, structured responses without GraphQL query parsing overhead.
2. **GraphQL Fallback with Strict `ID!` Scalar**: If REST is unavailable or returns an empty list, fall back to GraphQL:
   ```graphql
   query GetAdGroups($campaignId: ID!) {
      campaign(id: $campaignId) {
        adGroups {
          nodes {
            id
            name
          }
        }
      }
   }
   ```
   > **CRITICAL**: The `$campaignId` variable must be declared as `ID!`. Declaring it as `String!` triggers GraphQL schema validation failure (`GRAPHQL_VALIDATION_FAILED`) because the root `campaign(id: ID!)` query field enforces scalar type compatibility.
3. **Property Normalization**: Map both REST attributes (`AdGroupId`, `AdGroupName`) and GraphQL nodes (`id`, `name`) into a normalized entity shape prior to applying creative associations or targeting parameters.


