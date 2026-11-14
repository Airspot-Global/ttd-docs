# API Reference

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/ApiReferencePlatform
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/ApiReferencePlatform (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Platform API reference

The Platform API reference is an auto-generated alphabetical list of all platform operations, with the most up-to-date information. This reference describes the Platform API structure for both GraphQL operations and REST endpoints.

Here's what you need to know about operations and endpoints:

- Both methods follow the same API token authentication.
- Both operations and endpoints are grouped by area, also known as domain.
- Not all API domains support both REST and GraphQL options, and the two formats do not map to each other one‑to‑one.

> **TIP**: If you're new to the platform and don't have any existing integrations, we recommend building on GraphQL. If you have an existing REST integration you're looking to move over, see the REST → GraphQL migration guide for a complete field-level mapping between every REST endpoint and its GraphQL equivalent.

The following sections provide specific details on GraphQL operations and REST endpoints.

## GraphQL operations

The following conventions apply across all GraphQL resources:

- There are two types of GraphQL operations: **Query** (read data) and **Mutation** (create/update data).
- Each GraphQL operation has a `GQL` tag.
- Each operation page includes a description, basic code snippet of required fields, arguments, type section, and entity section, containing fields.
- Click on the children of the type section to open an expandable entity section that shows all fields, nested types, and nullability.

> **TIP**: If you are new to GraphQL, check out our GraphQL API Resource Hub and familiarize yourself with the basics.

## REST endpoints

The following conventions apply across all REST API resources:

- Each REST endpoint starts with `/v3/`.
- Most endpoints are grouped by their area, which goes directly after `/v3/`, such as `/v3/advertiser/`.
- Endpoints follow the REST convention and have `GET`, `PUT`, `POST`, or `DELETE` tags.
- Endpoint properties have `SOLIMAR` and `KOKAI` labels to differentiate between incompatible versions of the Platform API.
- Hidden endpoints may require additional access through your Technical Account Manager.
- There are exceptions to the list order, such as `/v3/ecommerce`, which contains a large set of endpoints that are grouped differently.
