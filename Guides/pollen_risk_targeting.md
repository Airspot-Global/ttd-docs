# Pollen Risk Targeting

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/Pollen
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/Pollen (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Pollen risk targeting

Pollen risk targeting helps advertisers in the healthcare industry and those selling indoor air treatment products reach their target audiences more effectively. You can use this information to direct your media spend to areas with the highest pollen concentration (and subsequently have more people suffering from allergies and also looking for air purifiers or allergy medication).

To help you target areas based on the current or forecast severity level of pollen concentration in the atmosphere, The Trade Desk has partnered with Ambee to provide the following bid list dimension properties for your campaigns:

| Step | Description |
| --- | --- |
| 1 | Add the `AtmosphericCondition` property to the `Bidlines` object array in the bid list or ad group endpoints with the pollen concentration level you want to target. **NOTE**: There are two sets of values for this enumeration: those that indicate the areas _forecast_ to reach the specified severity level within the next 48 hours and those that indicate the _current_ level of pollen concentration. |
| 2 | Set the `BidListDimensions` enum value to `HasAtmosphericCondition` in the partner, advertiser, bid list, ad group, or campaign endpoints. |

> **NOTE**: This feature is disabled in the European Economic Area, the United Kingdom (under the UK GDPR), or Switzerland, collectively General Data Protection Regulation (GDPR) regions.
