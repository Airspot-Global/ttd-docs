# API Changes

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/ApiChanges
- Retrieved: 2026-11-14
- Category: Guides

---

# API Changes

This page explains how The Trade Desk introduces and manages changes to the API (GraphQL and REST), including when we provide advance notice and where you can track upcoming and past changes, so you can plan integration updates with confidence. It applies across our APIs, including Platform API and Data API.

## Change examples

A change is any modification to the API. It can be entirely additive (a non-breaking change), or it can cause an existing integration to fail, return errors, or behave incorrectly without code changes on your part (a breaking change). We don't employ a formal versioning policy, and group changes into the following four categories.

### Additions

An addition is an expansion to the API, and does not require code changes on your part to keep your integration working. For example:

- A new endpoint, GraphQL field, query, or mutation.
- A new optional request field or parameter.
- A new field in a response payload.
- A new value in an existing enum.
- A new optional query parameter or request header.
- An expanded error message that keeps the same error code.

> **TIP**: Additions are not expected to disrupt existing integrations, but building clients that tolerate unrecognized fields and new enum values (rather than failing on them) will make your integration more resilient to these changes.

### Behavior changes

The endpoint doesn't return an error and its status doesn't change; it simply behaves differently. Depending on your use case, this may or may not require code changes to accommodate. Examples are:

- Changing a default value or default behavior, such as switching a setting from opt-in to opt-out.
- Changing the meaning or format of an existing field's response value.

### New requirements

Something that used to be optional becomes required. Depending on your use case and implementation, this may or may not require code changes to accommodate. For example:

- Making a previously optional request field or parameter required.
- Adding new, stricter validation to an existing field or parameter.

### Removals and replacements

An element is removed, renamed, or changed in a way that requires code changes on your part. This typically requires code changes from all callers. For example:

- Removing an endpoint, GraphQL field, query, or mutation.
- Renaming a field, parameter, endpoint, or enum value.
- Removing a value from an existing enum.
- Changing the data type of a field (for example, string to integer).

## Advance notice

Our guidelines are to communicate at least 3 months before planned changes that require integration changes take effect. Unplanned mandatory changes—such as security, compliance, or business continuity—and non-impacting changes are not communicated ahead of time.

When announcing changes, where practical, we aim to do the following:

- Publish the change with a clearly stated decommission date, at least 3 months out.
- Describe the specific action required to remain unaffected, including a migration target (a replacement field, endpoint, or type) where one exists.
- Support the deprecated and replacement behavior side by side during the notice period, so you can migrate on your own schedule rather than at the last minute.

## Where to track changes

Breaking changes are announced and tracked on the _Upcoming changes_ page under the **News** hub, which lists quarterly schedules, the effective date, what's changing, and the action required for each upcoming change.

The following table lists all **News** pages for each user type:

| User | Upcoming changes | Release notes | Archives |
| --- | --- | --- | --- |
| Advertiser | Upcoming changes | Release notes | News archives |
| Provider | Upcoming changes | Release notes | News archives |
| Seller | Upcoming changes | Release notes PDP API release notes | News archives |

> **TIP**: You can also track all Platform API changes in the API Usage Dashboard. It flags any upcoming breaking changes detected in the API usage associated with your account.
