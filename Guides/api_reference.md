# API Reference

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/ApiReferencePlatform
- Category: Guides

---

# API Reference

The Platform API reference is an auto-generated alphabetical list of all platform endpoints, with the most up-to-date information. This reference describes the Platform API endpoint structure, along with other APIs that can be used with the Platform API, such as the Data API. Here's what you need to know:

*   Each endpoint that uses REST starts with `/v3/`.
*   Most endpoints are grouped by their area group, which go directly after `/v3/`, such as `/v3/advertiser/`.
*   Endpoints follow the REST convention and have `GET`, `PUT`, `POST`, or `DELETE` tags.
*   Endpoint properties have `SOLIMAR` and `KOKAI` labels to differentiate between incompatible versions of the Platform API.
*   Hidden endpoints may require additional access through your Technical Account Manager.
*   There are exceptions to the list order, such as `/v3/ecommerce`, which contains a large set of endpoints that are grouped differently.

> **NOTE**: There are multiple authentication methods to access our APIs. If you haven't done so, follow the [API Token Authentication](/v3/portal/api/doc/Authentication) steps to call any of the endpoints in this reference. For data onboarding and management, additionally follow the [Signature Header Authentication](/v3/portal/data/doc/DataAuthentication) steps to use the [Data API](/v3/portal/data/doc/DataApiReference).