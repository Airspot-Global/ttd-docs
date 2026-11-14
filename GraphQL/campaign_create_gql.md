# Campaign creation workflows

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CampaignCreateGQL
- Retrieved: 2026-11-14
- Category: GraphQL

---

# Campaign creation workflows

This page outlines the options and steps you need to take if you want to create a campaign using the GraphQL API.

## Workflow diagram

The following diagram illustrates the process outlined in the next section, which also includes links to the respective user guides and scripts that provide additional guidance on the decisions you might need to make along the way.

## Process overview

The following table outlines the process step by step and provides links to detailed user guides, while the diagram in the preceding section illustrates the decision-making workflow.

| Step |  | Description | Mutation or Query | User Guide | Notes |
| --- | --- | --- | --- | --- | --- |
| **1** |  | Ensure that you have a seed for your campaign. | `seedCreate` mutation | Seeds | To run impactful campaigns in Kokai, you need at least one high-quality seed, ideally sourced from first-party data. See also the Seed sample scripts in Python. |
| **2** |  | Choose how you want to create your Kokai campaign. | N/A | N/A | With GraphQL, you can create one or more campaigns at once with each operation. |
|  | **a** | Create a single campaign from scratch. | `campaignCreate` mutation | Create campaigns | See also the Creating sample scripts in Python. |
|  | **b** | Create multiple campaigns from scratch. | `bulkCreateCampaigns` mutation | GraphQL API bulk operations | This option is best suited for creating over 100 campaigns at once. |
|  | **c** | Create one or more copies of one or more existing campaigns at once. | `campaignClonesCreate` mutation | Clone campaigns | You can clone up to 50 different campaigns and create up to 1000 copies in a single call. For more details, see the user guide. See also the Cloning sample scripts in Python. |
| **3** |  | (Optional) Review the newly created campaigns, their versions, budgets, and other settings. | `campaign` query | GraphQL campaign query examples | See also the Querying sample scripts in Python. |
