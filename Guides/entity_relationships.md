# Entity Relationships

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/EntityRelationships
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/EntityRelationships (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Entity relationships

To manage your campaigns efficiently, it's helpful to understand the relationship between entities within the API platform. There are two primary types of relationships: ownership and assignment.

For more details on these entities, their properties, and their relationships, see our API reference.

## Ownership relationships

Owned entities exist within a hierarchical structure where the owner is the parent entity. For example, an advertiser owns key entities such as creatives, seeds, data, audiences, and campaigns, granting them the authority to create, update, or delete them. To create any of these items, you need an advertiser ID.

Owned entities automatically inherit certain properties or settings from their parent entities, with the option to override inherited attributes. This streamlines the setup process, ensures consistency across campaigns, and helps you focus on advertising strategy instead of repetitive manual configuration. By defining key properties like the currency code, default frequency, and bid lists at the advertiser level, you can automatically propagate these settings to all associated campaigns and ad groups as needed. For details on bid lists, see Bid list relationships.

The following diagram shows the ownership relationships among API platform entities, from the partner to the ad-group level. The one-to-many arrows indicate how an entity can own multiple child entities. For example, a single advertiser can own multiple campaigns, but each campaign can only belong to one advertiser.

## Assignment relationships

In addition to ownership relationships, entities have assignment relationships, also known as associations. These relationships define how entities are associated with each other, often indicating specific roles or responsibilities. They determine how resources are allocated and performance is measured. Unlike ownership relationships, assignments can be transferred from one entity to another.

For example, the advertiser can assign creatives to multiple ad groups, each with different goals and targeting parameters. They can also reuse these creatives in different ad groups as needed.

The following diagram shows the ownership and assignment relationships among API platform entities, from the partner to the creative level. Solid lines represent ownership relationships, while dashed lines represent assignment relationships. Bid lists are an exception and are not shown in this diagram. These can be owned and assigned at any level of the major core entities: partner, advertiser, campaign, and ad group.
