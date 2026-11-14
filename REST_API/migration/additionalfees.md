# Additional fees: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/additionalfees-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Additional fees: REST → GraphQL migration guide

**Not currently available in GraphQL**—standalone create and stop (see quick reference). Attaching fees when creating a new campaign is a separate workflow and is not a substitute for `POST /v3/additionalfees`.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/additionalfees/defaultfeecard/{advertiserId}` | `Advertiser.defaultFeeCard` | Synthetic default card for campaign creation |
| `GET /v3/additionalfees/{ownerType}/{ownerId}` | `Campaign.passThroughFeeCards` | Current fee card; filter by owner type and ID |
| `POST /v3/additionalfees/changelog` | `Campaign.passThroughFeeCards` | Changelog list with optional date filters |
| `POST /v3/reseller/additionalfees/changelog` | N/A | Not currently available in GraphQL |
| `GET /v3/reseller/additionalfees/{ownerId}` | `Partner.resellerAdditionalFeeCard` | Current reseller fee card |
| `POST /v3/additionalfees` | N/A | Not currently available in GraphQL |
| `PUT /v3/additionalfees` | `additionalFeeCardUpdate` | N/A |
| `POST /v3/additionalfees/stop` | N/A | Not currently available in GraphQL |

## Shared nested types and enums

### PassThroughFeeType

Used when reading `passThroughFeeCards` / `passThroughFees` on campaign and ad group fee cards.

| REST `AdditionalFeeType` | GraphQL `PassThroughFeeType` | Notes |
| --- | --- | --- |
| None | NONE | N/A |
| MediaCostPercentage | MEDIA_COST_PERCENTAGE | N/A |
| DataCostPercentage | DATA_COST_PERCENTAGE | N/A |
| MediaPlusDataCostPercentage | MEDIA_PLUS_DATA_COST_PERCENTAGE | N/A |
| PartnerCostPercentage | _(no exact GraphQL value)_ | Closest: `PARTNER_DATA_COST_PERCENTAGE`—verify amount semantics. |
| PartnerDataCostPercentage | PARTNER_DATA_COST_PERCENTAGE | N/A |
| FeeCPM | FEE_CPM | N/A |
| RateCPM | RATE_CPM | N/A |
| RateCPC | RATE_CPC | N/A |
| CustomPMP_PartnerCostPercentage | CUSTOM_PMP_PARTNER_DATA_COST_PERCENTAGE | Name differs; same business intent. |
