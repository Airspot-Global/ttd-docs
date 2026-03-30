# Audiences

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/Audience
- Category: Guides

---

# Audiences

An audience is a specific person or group of people that you want to reach with a campaign. Audiences are made up of included and excluded data groups. Data groups are made up of data elements (first-party data segments or third-party data segments). When you add multiple elements to a data group, you grow the audience. When you add multiple data groups to an audience, you shrink the audience.

## 

Data Elements[](#data-elements)

Data elements are segments of information like cookies and various IDs (such as device IDs and [Unified IDs](/v3/portal/data/doc/UnifiedIDs) like UID2 and EUID).

| Data Element Type | Description |
| First-Party | First-party data elements are segments that you've sent to the platform or that you've authorized another data provider to send to our platform on your behalf. There are no fees associated with using your own data. |
| Third-Party | Third-party data elements are segments that data providers have sent to the platform and are available for you to purchase and target in your audiences. These use a flat-fee CPM, a percentage of media cost, or a combination of both. These fees are clearly outlined in the platform. |

Data elements can be combined into data groups.

## 

Data Groups[](#data-groups)

A _data group_ is a collection of first-party and/or third-party data elements that are combined using an OR (union) operator. For example, a data group with data element 1 and data element 2 would look for users that match both data element 1 or data element 2.

When creating an audience, you can use data groups to include or exclude their data elements for targeting. Included data groups target only the specified segments of users, while excluded data groups target everyone except the specified segments of users. You can use both included and excluded groups to create the audience you want to target.

Here's what you need to know about data groups when building your audience:

*   If more than one data group is _included_ in an audience, a user must match _all of the included_ data groups to be targeted.
*   If more than one data group is excluded in an audience, a user may match _any of the excluded_ data groups to be removed from targeting.
*   If a user matches _both_ included and excluded data groups, the user will be _excluded_ from the audience.
*   Excluding third-party data elements from a data group has a $0.09 CPM fee, in addition to any fee charged by the data provider to use the segment.

The following diagram illustrates the audience segment that is targeted when multiple data groups are included and excluded within an audience.

## 

Audience Creation Workflow[](#audiencecreationworkflow)

To create an audience, complete the following steps:

1.  [Send first-party data](/v3/portal/data/doc/post-data-advertiser-firstparty) or use third-party data buyable within the platform.
2.  Look up [first-party data](#data-elements-1p-lookup-tasks) and [third-party data](#lookup-3p-data-elements-lookup-tasks) element IDs to use within a data group.
3.  [Create data groups](#createdatagroups) to include in or exclude from audiences.
4.  Assign data groups to audiences.
5.  [Assign audiences to ad groups](#assignaudience).

The following sections provide examples for these and other related tasks.

## 

Data Element Tasks[](#dataelements)

The following table lists the tasks for managing data elements in both the platform and data API.

> **NOTE**: The data API requires a different authentication.

| Task | API Suite | Endpoint or Further Reference | Notes |
| Populate first-party segment data. | Data | [POST /data/advertiser](/v3/portal/data/doc/post-data-advertiser-firstparty) | Populate your segments with cookies or acceptable types of IDs. For details, see [Getting Started with Data Onboarding](/v3/portal/data/doc/DataGetStartedAdvertiser). |
| Create geofence segments. | Platform | [Geofence Targeting](/v3/portal/api/doc/GeofenceTargeting) | Create your own geofence segment and use points to define virtual boundaries to target specific areas. |
| [Look up first-party data elements](#data-elements-1p-lookup-tasks). | Platform | [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) | To find the `FirstPartyDataId` to use in a data group, use the `Data.Name` value that you assigned to the segment when [populating first-party segment data](/v3/portal/data/doc/post-data-advertiser-firstparty) as a `SearchTerm`. |
| [Look up third-party data elements](#lookup-3p-data-elements-lookup-tasks). | Platform | [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) | Look up the `ThirdPartyDataId` to add to a data group. |
| [Remove inactive users](#data-elements-1p-remove) from first-party data segments. | Data | [POST /data/advertiser](/v3/portal/data/doc/post-data-advertiser-firstparty) | To remove an inactive user, set the `TTLInMinutes` property to `0` for that user in the request.  
**TIP**: To delete the whole segment, set the `TTLInMinutes` property to `0` for all IDs in the segment. |
| [Look up third-party data elements similar to your first-party data elements](#lookup-lookalike-3p-data-elements). | Platform | [GET /v3/dmp/lookalikemodel/build/{firstPartyDataId}](/v3/portal/api/ref/get-dmp-lookalikemodel-build-firstpartydataid)  
[POST /v3/dmp/lookalikethirdpartydata/query](/v3/portal/api/ref/post-dmp-lookalikethirdpartydata-query) | Build a lookalike model and find similar `ThirdPartyDataIds` to your `FirstPartyDataId`. |

### 

First-Party Data Elements: Look-up Task Examples[](#data-elements-1p-lookup-tasks)

You can look up first-party data elements by using a variety of filters and sorting, which can be combined to find relevant segments more efficiently.

> **NOTE**: The lookup endpoints return the number of active IDs from the last 7 days and received IDs from the last 30 days. For details, see [Unique ID Counting Methodologies](/v3/portal/api/doc/IdCountingMethodologies).

The following sections provide examples of different ways of looking up first-party data elements:

*   [By Advertiser](#lookup-1p-data-elements-all)
*   [By Unique Count](#lookup-1p-data-elements-unique-count)
*   [By Search Terms](#lookup-1p-data-elements-search-terms)
*   [By Data Types](#lookup-1p-data-elements-data-types)
*   [By Lookalike Model Result Status](#lookup-1p-data-elements-lookalike)

#### Look up All First-Party Data Elements for an Advertiser

The following is a [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) request body example with the `AdvertiserId` property.

{

  "AdvertiserId": "advabc",

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up First-Party Data Elements by Unique Count

The following is a [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) request body example with the `AdvertiserId` and `UniqueCountMinimum` properties.

{

  "AdvertiserId": "advabc",

  "UniqueCountMinimum": 5000,

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up First-Party Data Elements by Search Terms

Search terms may be added to the request to filter results where the search term matches the data element's `FirstPartyDataId`, `Name`, or `DataType`.

The following is a [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) request body example with search terms.

{

  "AdvertiserId": "advabc",

  "SearchTerms": \["auto"\],

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up First-Party Data Elements by Data Types

The following is a [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) request body example with data types.

{

  "AdvertiserId": "advabc",

  "DataTypes": \["ImportedAdvertiserData","Keyword"\],

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up First-Party Data Elements by Lookalike Model Result Status

The following is a [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) request body example with a `LookAlikeModelResultStatuses` property.

{

  "AdvertiserId": "advabc",

  "LookAlikeModelResultStatuses": "Ready",

  "PageStartIndex": 0,

  "PageSize": 10

}

### 

Remove Inactive Users from First-Party Data Segments[](#data-elements-1p-remove)

To remove inactive users from your data segment, in a [POST /data/advertiser](/v3/portal/data/doc/post-data-advertiser-firstparty) call, set the `TTLInMinutes` property to `0` for that user.

> **TIP**: To delete the whole segment, set the `TTLInMinutes` property to `0` for all IDs in the segment.

{

   "AdvertiserId":"yourAdvertiserId",

   "Items":\[

      {

         "TDID":"123e4567-e89b-12d3-a456-426652340000",

         "Data":\[

            {

               "Name":"1210",

               "TimestampUtc": "2023-11-11T10:11:30+5000",

               "TTLInMinutes":0

            },

            {

               "Name":"1160",

               "TimestampUtc": "2023-11-13T09:35:30+5000",

               "TTLInMinutes":0

            }

         \]

      }

   \]

}

### 

Third-Party Data Elements: Look-up Task Examples[](#lookup-3p-data-elements-lookup-tasks)

You can look up third-party data elements by using a variety of filters and sorting, which can be combined to find relevant segments more efficiently.

> **NOTE**: The lookup endpoints return the number of active IDs from the last 7 days and received IDs from the last 30 days. For details, see [Unique ID Counting Methodologies](/v3/portal/api/doc/IdCountingMethodologies).

The following sections provide examples of different ways of looking up third-party data elements:

*   [By Advertiser](#lookup-3p-data-elements-all)
*   [By Unique Count](#lookup-3p-data-elements-unique-count)
*   [By Search Terms](#lookup-3p-data-elements-search-terms)
*   [By Demographic Category](#lookup-3p-data-elements-category)
*   [By Data Rate](#lookup-3p-data-elements-data-rate)
*   [By Ad Environment](#lookup-3p-data-elements-ad-environment)

#### Look up All Third-Party Data Elements for an Advertiser

The following is a [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) request body example with the `AdvertiserId` property.

{

  "AdvertiserId": "advabc",

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up Third-Party Data Elements by Unique Count

The following is a [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) request body example with the `AdvertiserId` and `UniqueCountMinimum` properties.

{

  "AdvertiserId": "advabc",

  "UniqueCountMinimum": 5000,

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up Third-Party Data Elements by Search Terms

The following is a [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) request body example with search terms.

> **IMPORTANT**: All terms must be matched in the `Name` or `FullPath` in order for a result to be returned.

{

  "AdvertiserId": "advabc",

  "SearchTerms": \["auto"\],

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up Third-Party Data Elements by Demographic Category

To look up category IDs, use [GET /v3/dmp/thirdparty/facets/{advertiserId}](/v3/portal/api/ref/get-dmp-thirdparty-facets-advertiserid).

The following is a [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) request body example with the `CategoryId` of `526` for the demographic category including ages 18-24 years.

{

  "AdvertiserId": "advabc",

  "CategoryIds": \[526\],

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up Third-Party Data Elements by Data Rate

You can filter segments that have a certain data rate or data rate type.

The following is a [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) request body example with the `CPMFilter` filter.

{

  "AdvertiserId": "advabc",

  "DataRateFilters": {

      "CPMFilter": {

          "MinimumCPM": {

            "Amount": 3,

            "CurrencyCode": "USD"

          },

          "MaximumCPM": {

            "Amount": 7,

            "CurrencyCode": "USD"

        }

      }

    },

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Look up Third-Party Data Elements by Ad Environment

You can filter segments by either `Web` or `InApp` ad environment.

The following is a [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) request body example with the `InApp` filter.

{

  "AdvertiserId": "advabc",

  "AdEnvironment": "InApp",

  "PageStartIndex": 0,

  "PageSize": 10

}

### 

Third-Party Data Elements Similar to Your First-Party Data Element: Look-up Tasks[](#lookup-lookalike-3p-data-elements)

> **NOTE**: Third-party data elements are only available in our production environment. They are not available in our sandbox environment.

| Task | API Suite | Endpoint |
| [Look up eligible first-party data segments](#lookalikeeligible) | Platform | [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) |
| [Build a lookalike model of third-party data elements](#lookalikebuild) | Platform | [GET /v3/dmp/lookalikemodel/build/{firstPartyDataId}](/v3/portal/api/ref/get-dmp-lookalikemodel-build-firstpartydataid) |
| [Check the lookalike model build status](#lookalikecheck) | Platform | [GET /v3/dmp/lookalikemodel/{firstPartyDataId}](/v3/portal/api/ref/get-dmp-lookalikemodel-firstpartydataid) |
| [Retrieve third-party data elements from the lookalike model](#lookalikeretrieve) | Platform | [POST /v3/dmp/lookalikethirdpartydata/query/](/v3/portal/api/ref/post-dmp-lookalikethirdpartydata-query) |

#### Look up Eligible First-Party Data Segments

For the best probability of having enough first-party data to generate a lookalike model, search for eligible first-party segments that have a minimum unique count ranging from 1000 to 5000.

The following is a [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) request body example.

{

  "AdvertiserId": "advabc",

  "UniqueCountMinimum": 4000,

  "LookAlikeModelEligibilities": \["Eligible"\],

  "PageStartIndex": 0,

  "PageSize": 10

}

#### Build a Lookalike Model of Third-Party Data Elements

To build a lookalike model, make a request to [GET /v3/dmp/lookalikemodel/build/{firstPartyDataId}](/v3/portal/api/ref/get-dmp-lookalikemodel-build-firstpartydataid).

#### Check the Lookalike Model Build Status

To check the build status of lookalike model, make a request to [GET /v3/dmp/lookalikemodel/{firstPartyDataId}](/v3/portal/api/ref/get-dmp-lookalikemodel-firstpartydataid).

The response includes a `LookAlikeBuildStatus`, which indicates whether the lookalike model build is processing (`Queued`) or was completed (`Built`). The response also includes a `LookAlikeModelResultStatus`.

The following table explains the `LookAlikeModelResultStatus` values.

| Status Value | Description |
| `NoResults` | The first-party data segment the model was generated from did not have enough overlap with third-party data to generate model. |
| `Ready` | The lookalike model has been generated and `ThirdPartyDataIds` can be retrieved to use in an audience. |

#### Retrieve Third-Party Data Elements from the Lookalike Model

Search for the results of the build using the query endpoint. The `Result` object shows the third-party data segments similar to the first-party data segment, as well as a relevance ratio and value ratio to help you evaluate the best segments to use in your audience. Use `Result.ThirdPartyData.ThirdPartyDataId` in your data groups.

The following is a [POST /v3/dmp/lookalikethirdpartydata/query](/v3/portal/api/ref/post-dmp-lookalikethirdpartydata-query) request body example.

{

  "FirstPartyDataId": 1234567,

  "PageStartIndex": 0,

  "PageSize": 10

}

## 

Data Group Tasks[](#datagroups)

| Task | API Suite | Endpoint | Notes |
| [Create a data group](#createdatagroups) | Platform | [POST /v3/datagroup](/v3/portal/api/ref/post-datagroup) | All third-party data IDs in segments will be validated for biddability. Data group workflows will fail if the `ThirdPartyDataIds` array contains non-biddable IDs. |
| Retrieve details for an individual data group by ID | Platform | [GET /v3/datagroup/{dataGroupId}](/v3/portal/api/ref/get-datagroup-datagroupid) | N/A |
| Look up all data groups for an advertiser | Platform | [POST /v3/datagroup/query/advertiser](/v3/portal/api/ref/post-datagroup-query-advertiser) | Use `SearchTerms` to search for matching terms in `DataGroupId`, `DataGroupName`, or `Description`. |
| Look up all data groups since the last change tracking version | Platform | [POST /v3/delta/dmp/query/advertiser/firstparty](/v3/portal/api/ref/post-delta-dmp-query-advertiser-firstparty) | N/A |
| Update a data group | Platform | [PUT /v3/datagroup](/v3/portal/api/ref/put-datagroup) | All third-party data IDs in segments will be validated for biddability. Data group workflows will fail if the `ThirdPartyDataIds` array contains non-biddable IDs. |

### 

Create Data Groups[](#createdatagroups)

> **NOTE**: Data groups are created using the platform API endpoints. For details, see [API Token Authentication](/v3/portal/api/doc/Authentication).

Here's what you need to know about data groups:

*   You share data groups among multiple audiences. Just set the `IsSharable` property to `true`.
*   To create the data group without third-party data segments that you are not authorized to use, set the `SkipUnauthorizedThirdPartyData` property to `true` when specifying third-party IDs. If not specified or set to `false`, attempting to create a data group with `ThirdPartyDataIds` you are unauthorized to use will result in an error.
*   All third-party data IDs in segments will be validated for biddability. Data group workflows will fail if the `ThirdPartyDataIds` array contains non-biddable IDs.

> **TIP**: To check if segments are buyable beforehand, use the [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) endpoint. Include only third-party data IDs listed in the response.

The following is a [POST /v3/datagroup](/v3/portal/api/ref/post-datagroup) request body example.

{

  "AdvertiserId": "advabc",

  "DataGroupName": "Auto Interest",

  "IsSharable": true,

  "FirstPartyDataIds": \[

    1234567

  \],

  "ThirdPartyDataIds": \[

    "1234567|bluekai"

  \],

  "SkipUnauthorizedThirdPartyData": true

}

## 

Audience Tasks[](#audience)

| Task | API Suite | Endpoint | Notes |
| [Create an Audience](#createaudience) | Platform | [POST /v3/audience](/v3/portal/api/ref/post-audience) | For details on what you need to know about data groups when creating audiences, see [Data Groups](#data-groups). |
| Retrieve Details For An Individual Audience By Id | Platform | [GET /v3/audience/{audienceId}](/v3/portal/api/ref/get-audience-audienceid) | N/A |
| Look up all audiences for an advertiser | Platform | [POST /v3/audience/query/advertiser](/v3/portal/api/ref/post-audience-query-advertiser) | Use `SearchTerms` to search for matching terms in `AudienceId`, `Audience`, or `Description`. |
| Update an audience | Platform | [PUT /v3/audience](/v3/portal/api/ref/put-audience) | For examples, see [Assign an Audience to an Ad Group](#assignaudience). |

### 

Create an Audience[](#createaudience)

The following is [POST /v3/audience](/v3/portal/api/ref/post-audience) request body examples.

#### Target Certain Data Groups and Exclude One Data Group

{

  "AdvertiserId": "adv123",

  "AudienceName": "24-35 Cats Minus Low Value",

  "Description": "Users in the age range 24-35 who are interested in 

  cats and are not low-value users.",

  "IncludedDataGroupIds": \[

    "aud1234",

    "aud2345"

  \],

  "ExcludedDataGroupIds": \[

    "aud3456"

  \]

}

#### Target Everyone Except One Data Group

{

  "AdvertiserId": "adv123",

  "AudienceName": "Everyone Except Low-Value Users",

  "Description": "Exclude low value users",

  "IncludedDataGroupIds": \[\],

  "ExcludedDataGroupIds": \[

    "aud3456"

  \]

}

#### Assign an Audience to an Ad Group

The following is a [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) request example that shows how to assign an audience to an existing ad group.

{

  "AdGroupId": "adgr123",

  "RTBAttributes": {

    "AudienceTargeting": {

      "AudienceId": "aud1234"

    }

  }

}

*   To target everyone (run-of-exchange), do not enable any properties in the `RTBAttributes.AudienceTargeting` object of the ad group.
*   To target only trackable users, on the ad group, enable `RTBAttributes.AudienceTargeting.TargetTrackableUsersEnabled` to restrict targeting only to users that we can track (users we have a `TDID` or a device ID for).  
    We'll create a new audience for you that includes only trackable users.

> **NOTE**: There is a fee to use this feature which you can be look up by using the ad group's `RTBAttributes.AudienceTargeting.TargetTrackableUsersFee` object.

To view a full list of Koa features, see [Ad Groups](/v3/portal/api/doc/AdGroup).

## 

FAQs[](#faqs)

We've got answers to your most commonly asked questions.

### 

How is audience different from seed?

Audience and [seed](/v3/portal/api/doc/Seed) are not the same. They are two discrete entities.

A seed is a specific, concentrated group of individuals who represent the core group of people that you want to target. This group typically consists of individuals who have taken valuable actions or exhibit traits that align with your campaign goals. An audience, on the other hand, is an expanded version of the core group, which includes not only the individuals in your seed but also extends to others who share similar traits or behaviors.