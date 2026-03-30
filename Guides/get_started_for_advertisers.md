# Get Started for Advertisers

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/Advertisers
- Category: Guides

---

# Get Started for Advertisers

If you are an advertiser looking to purchase media for your brand, you've come to the right place. After you've received your [API credentials](/v3/portal/api/doc/ApiPlatformGetStarted), follow this guide for an [overview](#workflow) of the steps involved in creating your advertiser account and setting up your campaigns. You'll also discover a variety of [resources](#resources) to help you explore new features and optimize performance. By using these resources, you can unlock the full potential of your campaigns and get the best return on investment.

Here's what you need to know about advertisers before you continue:

*   To create campaigns, tracking tags, and data elements in the API platform, as well as upload creatives, you must first [create](/v3/portal/api/doc/AdvertiserCreate) your advertiser account. That generates the advertiser ID, which is required for all these entities. In the entity hierarchy, advertisers are the owners of campaigns, ad groups, and creatives. For more information, see [Entity Relationships](/v3/portal/api/doc/EntityRelationships).
*   You can create, update, and manage your advertiser information using the GraphQL and REST endpoints. You can also use the GraphQL API to create custom queries, enabling you to retrieve specific data from multiple entities and records. For details, see [FAQs](#faqs).

## 

Workflow[](#workflow)

The following tiles offer a high-level overview of the end-to-end workflow for creating your advertiser, setting up your campaign, optimizing performance, and generating reports. We recommend following the steps sequentially from left to right and top to bottom, but the specific order may depend on your situation.

Create an Advertiser

To begin buying ad space, you must first create an advertiser. An advertiser ID is required for most calls, including onboarding data, and creating campaigns.

[

GET STARTED



](/v3/portal/api/doc/AdvertiserCreate)

Onboard Data

Lay the groundwork for audience-based buying by uploading first-party data. Your customer data is your most valuable asset.

[

GET STARTED



](/v3/portal/data/doc/DataGetStartedAdvertiser)

Create Seeds

Seeds form the core of your campaign strategy. Create the most accurate representation of your most valuable, converted customers to drive real-time insights and enhance AI-driven optimizations.

[

GET STARTED



](/v3/portal/api/doc/Seed)

Create Campaigns

Manage budgets and pacing settings to optimize your campaigns effectively. Expand your audience reach and improve performance by adding new channels like Connected TV.

[

GET STARTED



](/v3/portal/api/doc/Campaigns)

Create Ad Groups

Optimize your ad group goals and evaluate your campaign balance across the funnel. Assign your [creatives](/v3/portal/api/doc/Creative) to the ad groups, using different formats across different [channels](/v3/portal/api/doc/Channel).

[

GET STARTED



](/v3/portal/api/doc/AdGroup)

Drive KPIs

Discover how our AI-driven algorithms can help you bid for value over cost. Learn how maximizing expressiveness can empower the platform to make decisions that drive your KPIs toward success.

[

GET STARTED



](/v3/portal/api/doc/DriveKPIs)

Inform Decisions with Reports

Tailor your reports to gain valuable insights into performance metrics and audience behavior, enabling you to refine campaign strategies.

[

GET STARTED



](/v3/portal/reds/overview)

> **TIP**: For users with access, you can also [explore](https://desk.thetradedesk.com/knowledge-portal/en/kokai-key-workflows.html) the interactive workflow maps in the Knowledge Portal and visualize the programmatic process from left to right.

## 

Implementation Resources[](#resources)

The following resources are available to help implement your campaigns.

| Documentation Resource | Description |
| [Entity Relationships Diagrams](/v3/portal/api/doc/EntityRelationships) | Take a look at the diagrams to better understand the ownership and assignment relationships between API platform entities from the partner level to the ad-group level. |
| [Platform API: REST and GraphQL](/v3/portal/api/doc/ApisPlatform) | While the GraphQL API is designed to support newer Kokai-first experiences, both the GraphQL and REST APIs can be used interchangeably for most core features. You can use them concurrently depending on your needs. REST remains essential for accessing legacy functionality, such as Solimar budgets, while GraphQL offers streamlined access to new Kokai-exclusive features and more efficient capabilities, such as bulk queries. |
| [Partner Sandbox](/v3/portal/api/doc/PartnerSandbox) | To ensure your workflows are running smoothly before implementing any changes in production, be sure to test and verify your workflows in our new partner sandbox environment.  
This sandbox has the same data and users as our production environment and is wiped clean weekly. This allows you to experiment freely, knowing that next week your data in the sandbox will be fully restored to match your data in production. To access this sandbox environment, use your production Public API keys. In other words, no need to change anything in your code except the URL to test everything. |

## 

FAQs[](#faqs)

The following is a list of frequently asked questions about advertisers and the campaign setup.

### 

How do I choose the right API?

You can use either the REST and GraphQL API to create and manage campaigns. Both are fully supported. However, if you want to create, clone, or update multiple campaigns in one call, GraphQL is the better fit. It's also required for features that are exclusive to Kokai, like Kokai budget allocation and seed management.

If you’re managing campaigns with Solimar budgets, or you're only updating a single campaign at a time, REST is still a great choice, especially for legacy workflows.

### 

What is the difference between the REST and GraphQL API? When would I use each option?

REST and GraphQL are technologies used for designing and querying APIs in web development, but they have different approaches, philosophies, and intended uses in our platform. You can use GraphQL to access new features, enable more flexible queries, and perform bulk operations. For details, see [Platform API: REST and GraphQL](/v3/portal/api/doc/ApisPlatform). See also [Campaign Creation Workflows](/v3/portal/api/doc/CampaignCreateWorkflows).

### 

Do I need to create a seed before creating an advertiser?

No. You must [create](/v3/portal/api/doc/AdvertiserCreate) an advertiser before creating a seed. When you create the initial seed, it will automatically get attached to the advertiser, saving you a step. Unless specified otherwise, the seed will also be attached to new campaigns by default.