# Custom label: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/customlabel-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Custom label: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/label/{customLabelId}` | `Query.customLabel(id: ID!)` | N/A |
| `POST /v3/label/query/partner` | `Query.customLabels(input: CustomLabelsFilterInput!)` | GraphQL returns labels assigned to entities of `entityType` in scope, not the full partner catalog |
| `POST /v3/label` | `customLabelCreate` | N/A |
