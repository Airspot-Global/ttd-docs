# GET /v3/ispot/reportsettings/campaign/{campaignId} → Campaign(id:).incrementalReachSettings.iSpotReachSetting

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-ispot-reportsettings-campaign-campaignid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/ispot/reportsettings/campaign/{campaignId} → Campaign(id:).incrementalReachSettings.iSpotReachSetting

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/ispot/reportsettings/campaign/{campaignId}` |
| GraphQL query | `Query.campaign.incrementalReachSettings.iSpotReachSetting` |
| Return type | `ISpotIncrementalReachProviderSetting` (nested on `Campaign`) |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `Campaign.id` | ID! | Not nullable | Path `{campaignId}` maps to `Campaign.id`. |
| `IsActive` | `CampaignIncrementalReachSettings.iSpotReachSetting.isActive` | Boolean! | Not nullable | N/A |
| `BrandId` | `iSpotReachSetting.brand.id` | ID! | Not nullable | Nested `brand { id }` replaces flat `BrandId`. |
| `BrandName` | `iSpotReachSetting.brand.name` | String! | Not nullable | Read-only in REST; available on nested `brand.name`. |
| `IsVideoEnabled` | `iSpotReachSetting.isVideoEnabled` | Boolean! | Not nullable | N/A |
| `IsAudioEnabled` | `iSpotReachSetting.isAudioEnabled` | Boolean! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### ISpotIncrementalReachProviderSetting

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `IsActive` | `isActive` | Boolean! | Not nullable | N/A |
| `BrandId` | `brand.id` | ID! | Not nullable | Nested under `brand`. |
| `BrandName` | `brand.name` | String! | Not nullable | Read-only in REST. |
| `IsVideoEnabled` | `isVideoEnabled` | Boolean! | Not nullable | N/A |
| `IsAudioEnabled` | `isAudioEnabled` | Boolean! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/ispot/reportsettings/campaign/{campaignId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ISpotCampaignSettings {
  campaign(id: "<campaign-id>") {
    incrementalReachSettings {
      iSpotReachSetting {
        isActive
        isVideoEnabled
        isAudioEnabled
        brand {
          id
          name
        }
      }
    }
  }
}
```
