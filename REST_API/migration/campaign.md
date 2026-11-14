# Campaign: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/campaign-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Campaign: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/campaign/{campaignId}` | `Query.campaign` | N/A |
| `POST /v3/campaign/query/advertiser` | `Advertiser.campaigns` | N/A |
| `POST /v3/campaign/template/query/advertiser` | `Advertiser.campaignTemplates` | N/A |
| `GET /v3/campaign/name/{campaignId}` | `Query.campaign` | Lightweight ID/name—no new fields |
| `GET /v3/campaign/{campaignId}/metrics` | `Query.campaign` | N/A |
| `GET /v3/campaign/template/{campaignId}` | `Query.campaign` | N/A |
| `GET /v3/campaign/clone/status/{referenceId}` | `Query.campaignCloneProgress` | N/A |
| `GET /v3/campaign/bidlist/{campaignId}` | `Campaign.associatedBidLists` | Associated bid lists—same fields as main campaign read |
| `GET /v3/campaignflight/{campaignFlightId}` | `Query.campaign` | Campaign flight by ID via parent campaign filter |
| `POST /v3/campaign` | `campaignCreate` | GraphQL create; flights required on input—requires additional mutations |
| `PUT /v3/campaign` | `campaignUpdate` | GraphQL update; budget/flights/bid lists require separate mutations |
| `POST /v3/campaign/clone` | `campaignClonesCreate` | Async clone job; track via `campaignCloneProgress` |
| `POST /v3/campaign/bidlist` | `campaignAssociateBidList` | Associate one bid list |
| `DELETE /v3/campaign/bidlist` | `campaignAssociateBidList` | Remove via `bidListIdsToRemove` |
| `PUT /v3/campaign/bidlist` | `campaignAssociateBidList` | Replace full bid list association set |
| `POST /v3/campaign/buildcomplete` | — | **Not currently available in GraphQL** |
| `PUT /v3/campaign/template` | `campaignUpdate` | Template fields; publish/share type read-only |
| `POST /v3/campaign/template/clone` | `campaignClonesCreate` | Clone campaign template async job |
| `POST /v3/campaignflight` | `campaignFlightCreate` | Create campaign flight |
| `PUT /v3/campaignflight` | `campaignFlightUpdate` | Update campaign flight |
| `DELETE /v3/campaignflight/{campaignFlightId}` | `campaignFlightDelete` | Delete campaign flight |

## Shared nested types and enums

### CampaignFlight

Used on `Campaign.flights` and reachable via the campaign flight read endpoint.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CampaignFlightId` | `id` | ID! | Not nullable | Entity key. |
| `CampaignId` | `campaignId` | String | Nullable | Parent campaign reference. |
| `StartDateInclusiveUTC` | `startDateInclusiveUTC` | DateTime! | Not nullable | N/A |
| `EndDateExclusiveUTC` | `endDateExclusiveUTC` | DateTime | Nullable | N/A |
| `BudgetInAdvertiserCurrency` | `budgetInAdvertiserCurrency` | Decimal! | Not nullable | N/A |
| `BudgetInImpressions` | `budgetInImpressions` | Long | Nullable | N/A |
| `DailyTargetInAdvertiserCurrency` | `dailyTargetInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `DailyTargetInImpressions` | `dailyTargetInImpressions` | Long | Nullable | N/A |

### AssociatedBidList (bid list association)

Used on `Campaign.associatedBidLists` (an `AssociatedBidListsConnection`) from both the main campaign read and the dedicated bid-list endpoint.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `bidList.id` | String! | Not nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |
| `BidListSource` | `bidList.source` | BidListSource! | Not nullable | N/A |
| `BidListAdjustmentType` | `bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `BidListDimensions` | `bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |

### ShareType

Used on `Campaign.templateShareType` for campaign templates.

| REST value | GraphQL enum value | Notes |
| --- | --- | --- |
| `Advertiser` | `ADVERTISER` | N/A |
| `Partner` | `PARTNER` | N/A |
| `Global` | `GLOBAL` | N/A |
| `None` | `NONE` | N/A |
