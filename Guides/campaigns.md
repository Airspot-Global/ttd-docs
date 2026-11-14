# Campaigns

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/Campaigns
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/Campaigns (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Campaigns

A campaign is a strategy for purchasing ad inventory that is driven by goals, or KPIs, and a seed that represents your idea customer. You can set your campaigns to run with a set budget for a set period of time and allow our platform to drive performance more effectively to ensure that every ad impression you’re buying is the right one, at the right price.

Kokai campaigns also enable you to take advantage of innovative features like value-driven budgeting, a full-funnel approach at the ad group level, and Sellers and Publishers 500+ marketplace, a new inventory buying option that represents the easiest and most efficient way to buy the best of the open internet. These enhancements ensure you get the best value and relevance, optimizing your budget and delivering superior results.

## The campaign success checklist

Here's a list of key tasks to help you set up an effective Kokai campaign that drives your KPIs to success.

| Task | Description |
| --- | --- |
| Create your seed. | You might have already created a default seed as part of your advertiser setup, but to run the most impactful campaigns in Kokai, we recommend creating a specialized seed for each campaign. |
| Define your Goals and KPIs. | Be as specific as possible in what you want to achieve for your campaign by setting multiple ad group goals in addition to your campaign primary goal. |
| Set the primary channel. | Expand your reach by dedicating multiple campaigns to specific channels. This omnichannel approach enables the platform to provide specific recomendations based on the channel you set for each campaign. |
| Set your budgets. | Create a campaign budget and decide if you want the platform to automatically purchase impressions that are most valuable and likely to convert, or, if you have specific needs, assign a budget to each strategy or ad group in your campaign. **NOTE**: By default, the platform maximizes performance while prioritizing full budget delivery. For details, see Koa bidding strategy. |
| Target quality inventory. | Choose the Sellers and Publishers 500+ (SP500+) marketplace and use inventory controls to buy the best of the open internet. |
| Consider the full funnel. | As you create your Ad groups, be sure that your settings are balance across the awareness, consideration, and conversion marketing objectives. |
| Optimize the setup before launch. | Get key metrics through custom GraphQL queries, such as forecasted spend and relevance updates in real time, to help you fine tune your setup before launch. |

## Get started

To get started with creating and managing campaigns, consider the following options:

- Decide whether to create a new campaign from scratch or clone an existing one.
- Choose the API that best suits your workflows: GraphQL API or REST API.

For details, see Campaign creation workflows.

## FAQs

The following is a list of frequently asked questions about campaign management.

### What's a Kokai campaign?

Any campaign that has its `Version` property set to `Kokai`. All campaigns created or cloned in Kokai, or any existing Solimar campaign upgraded to utilize Kokai enhancements, are Kokai campaigns by default.

### How can I differentiate between Solimar and Kokai campaigns?

To check if a campaign can take advantage of the Kokai enhancements, use the GET /v3/campaign/{campaignId} REST endpoint or run a `campaign` GraphQL query for the campaign, and look up the `Version` property value.

### How do I choose the right API?

You can use either the REST or GraphQL API to create and manage campaigns. Both are fully supported.

However, if you want to create, clone, or update multiple campaigns in one call, GraphQL is the better fit. It's also required for features that are exclusive to Kokai, like Kokai budget allocation and seed management.

If you’re managing campaigns with Solimar budgets, or you're only updating a single campaign at a time, REST is still a great choice, especially for legacy workflows.

### Can I convert a Kokai campaign back to a Solimar campaign?

No. You will need to rebuild the campaign in Solimar.

### Can I upgrade a campaign by changing its version from Solimar to Kokai?

No. You cannot change the campaign version. To upgrade a Solimar campaign to Kokai, you must run the `campaignVersionUpgrade` mutation. For details, see Upgrade Solimar campaigns to Kokai.

### Can I use the REST API to update a Kokai campaign?

Yes. You can use both the REST API and GraphQL API to create and update campaigns.

### How can I archive a campaign?

In REST, use the PUT /v3/campaign endpoint and set the `Availability` property to `Archived`. In GraphQL, run the `campaignsArchive` mutation.

### Can I use the campaignUpdate mutation to update a campaign flight?

No. To update the campaign flight, use the `campaignFlightUpdate` mutation.

### How do I query for flight IDs in a specific campaign?

Use the `flights` filter in a GraphQL query to retrieve campaign flight IDs and the maximum amount each flight may spend. To learn more about using filters, see GraphQL API queries in our GraphQL Resource Hub.

```
query GetFlightIDsExample {
  campaign(id: "CAMPAIGN_ID_PLACEHOLDER"){
    id
    name
    flights(where: {id: {in: ["FLIGHT_ID_1", "FLIGHT_ID_2"]}}){
      nodes{
        id
        budgetInAdvertiserCurrency
      }
    }
  }
}
```
