# REDS schema update: Combined identifier

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/REDSUpdatesCombinedID
- Retrieved: 2026-11-14
- Category: Guides

---

# REDS schema update: Combined identifier

> **IMPORTANT**: Effective December 2, 2024, the Legacy Identifier REDS schema will be fully discontinued for both new and existing clients. All existing feeds must transition to the Combined ID schema as detailed on this page. Additionally, all new feeds will be required to use the Combined ID schema.

As announced in the REDS release notes, to address the increasing complexity of the identity landscape, the usage of cross-device graphs, and the onboarding of more ID types, we introduced the combined identifier schema—a scalable solution that can report different IDs without adding columns for each ID type. The new schema enables reporting of various types of IDs currently supported and possibly new ones added in the future without creating a separate column for each ID type.

## New and deprecated columns

The following table summarizes the columns that will be deprecated and added in the REDS impressions, clicks, and conversions feeds.

| COLUMN / FIELD | UPDATE TYPE | AFFECTED FEEDS | COMMENTS |
| --- | --- | --- | --- |
| `TDID` | Deprecated | Impressions, Clicks, Conversions | Replaced by `CombinedIdentifier` only for impressions and conversions. **NOTE**: For clicks, the `CombinedIdentifier` will not replace the `TDID`. |
| `DeviceAdvertisingId` | Deprecated | Impressions, Clicks | Replaced by `CombinedIdentifier` only for impressions. **NOTE**: For clicks, the `CombinedIdentifier` will not replace the `DeviceAdvertisingId`. |
| `CombinedIdentifier` | Newly added | Impressions, Conversions | The unique ID associated with the impression or conversion. |
| `CombinedIdentifierType` | Newly added | Impressions, Conversions | The type of the ID specified in the `CombinedIdentifier` column. |
| `CombinedIdentifierForm` | Newly added | Impressions | Additional insights about the ID specified in the `CombinedIdentifier` column. |

> **NOTE**: This schema change does not affect the Video Events feed. See also Data available in REDS.

Here's what you need to know about the combined identifier columns:

- The value in the `CombinedIdentifier` column can be one of the following: user ID, cookie ID, device advertising ID, or any other supported ID. The ID type is specified in the `CombinedIdentifierType` column.
- The `CombinedIdentifierForm` column will be enhanced in the future to provide more detailed insights about the ID in the `CombinedIdentifier` field. See also Legacy and originating IDs.
- Certain IDs such as UID2 might also be subject to specific data usage and sharing guidelines and may require additional development or integration effort. For a quick overview of UIDs, see Unified IDs. Otherwise, see the UID2 documentation.

## Legacy and originating IDs

In addition to the ID and its type, the new schema adds a new column, the `CombinedIdentifierForm`, that provides additional insights about the IDs associated with the impression or conversion. For example, additional insights include where the data came from and how it was processed for privacy regulations. The following table explains the difference between the originating and legacy IDs in the combined identifier schema.

| ID | Description |
| --- | --- |
| Legacy ID | The TDID or DAID used to purchase the impression in the bidstream, which is returned by default. |
| Originating ID (OGID) | The ID used to target the user, such as a raw UID2, UID2 token, or RampID. Here's what you need to know about this ID: - This is any known ID that comes from your first-party or third-party data segments. - This ID is available only when targeting is based on an identifier (non-contextual or non-programmatic guaranteed). Otherwise, a legacy ID is returned. - To turn on the ability to receive OGIDs, contact your Technical Account Manager. - For details, see Originating ID. |

## Upgrade overview

Currently, the combined identifier schema is in beta. To opt in and take advantage of Originating IDs, contact your Technical Account Manager.

### Timeline

Effective December 2, 2024, the Legacy Identifier REDS schema will be discontinued for both new and existing clients.

### Impact on your integration

Here's how the combined identifier schema will affect your integration going forward:

- After upgrading to the new schema, the existing TDID and DAID columns will be removed and replaced with the new combined identifier columns.
- By default, the `CombinedIdentifier` column will be populated by legacy IDs unless you enable the ability to receive originating IDs. For details, see Legacy and originating IDs.

If you are an existing REDS client who has enabled UID2:

-

The value in the `CombinedIdentifierType` column will be `UID2Token` instead of `UID2`.

-

If the value in the `CombinedIdentifierType` column is `UID2Token`, the value in the `CombinedIdentifier` column will be a UID2 token.

-

Alternatively, you can choose to receive raw UID2s. In that case, the value in the `CombinedIdentifierType` column will be `RawUID2` and the value in the `CombinedIdentifier` column will be a raw UID2.

An example of current values and new values if you choose to receive UID2 tokens is shown in the following table.

| Version | CombinedIdentifier | CombinedIdentifierType |
| --- | --- | --- |
| Current | A4AAAAZDYDRLTbzUTTH5nZ32V6j1tyHOA7Cqzt2LxfYqQ_1bP9XniuTU2xaox3k7dxMc51iarkrExeoHel7tpbaJFqRJjMvDxDvWIbMuwRlT_rTJtJ_jHs3kBNG1noc1ZENxAI-dWCRVEv8ZKqPdFl4PQZgHxeQ9qX07qZUymPTXIa_Z5eLKiGB4E4S4Y6TrvPwk-Rey74OqX8YtmWzGZCC9uQ | `UID2` |
| New | A4AAAAZDYDRLTbzUTTH5nZ32V6j1tyHOA7Cqzt2LxfYqQ_1bP9XniuTU2xaox3k7dxMc51iarkrExeoHel7tpbaJFqRJjMvDxDvWIbMuwRlT_rTJtJ_jHs3kBNG1noc1ZENxAI-dWCRVEv8ZKqPdFl4PQZgHxeQ9qX07qZUymPTXIa_Z5eLKiGB4E4S4Y6TrvPwk-Rey74OqX8YtmWzGZCC9uQ | `UID2Token` |

An example of current values and new values if you choose to receive raw UID2s is shown in the following table.

| Version | CombinedIdentifier | CombinedIdentifierType |
| --- | --- | --- |
| Current | A4AAAAZDYDRLTbzUTTH5nZ32V6j1tyHOA7Cqzt2LxfYqQ_1bP9XniuTU2xaox3k7dxMc51iarkrExeoHel7tpbaJFqRJjMvDxDvWIbMuwRlT_rTJtJ_jHs3kBNG1noc1ZENxAI-dWCRVEv8ZKqPdFl4PQZgHxeQ9qX07qZUymPTXIa_Z5eLKiGB4E4S4Y6TrvPwk-Rey74OqX8YtmWzGZCC9uQ | `UID2` |
| New | xpaiAogG2B4tLlrNhB/olf4eGIn85gjCz2BHw9WVu70= | `RawUID2` |

### Action required

Here's what you need to do to opt in and upgrade to the new combined identifier schema:

- If you are an existing REDS user, work with your Technical Account Manager to upgrade to the new combined identifier schema and turn on the ability to receive originating IDs.
- If you are new to REDS, there is no action required to start using the new schema. To turn on the ability to receive originating IDs, contact your Technical Account Manager.
- Work with your Technical Account Manager to understand the benefits of receiving raw UID2s rather than UID2 tokens.

## FAQs

The following is a list of commonly asked questions about the combined identifier schema.

### Does the combined identifier field list several IDs in a single field per impression?

No. The value in the `CombinedIdentifier` column is not a combination of several IDs, it is one ID per impression. For example, a TDID or a DAID, but not both.

### What's the difference between the old and new REDS schemas for user and device IDs?

The following tables illustrate the difference between the old and new REDS schemas for user and device IDs.

For example, in the old schema, each ID type had its own column for an impression.

| TDID | Device Advertising ID |
| --- | --- |
| 45b58e4d-2d4d-4248-ae89-24b54bd4484e | 82952842-42da-4985-985d-3a2daad4494a |

In the new schema, the new columns report only one ID for the same impression regardless of the ID type. For example, it can be one of the following sets of information, but not both.

| Combined Identifier | Combined Identifier Type | Combined Identifier Form |
| --- | --- | --- |
| 45b58e4d-2d4d-4248-ae89-24b54bd4484e | TDID | Originating |

OR

| Combined Identifier | Combined Identifier Type | Combined Identifier Form |
| --- | --- | --- |
| 82952842-42da-4985-985d-3a2daad4494a | DAID | Legacy |

### Does the combined identifier support UID2 and RampID?

Yes, support for UID2 and RampID is available for the combined identifier beta. UID2 support includes either raw UID2s or UID2 tokens. To opt in for the combined identifier beta, contact your Technical Account Manager.

### How will the REDS data be processed or altered per regulatory restrictions?

Cleansed data reported with combined identifier is subject to the contractual, policy, and regulatory restrictions outlined in REDS data practices.
