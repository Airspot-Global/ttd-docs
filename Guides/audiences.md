# Audiences

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/Audience
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/Audience (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Building audiences

An audience is a specific person or group of people that you want to reach with a campaign. Audiences are made up of included and excluded data groups. Data groups are made up of data elements (first-party data segments or third-party data segments). When you add multiple elements to a data group, you grow the audience. When you add multiple data groups to an audience, you shrink the audience.

## Data elements

Data elements are segments of information like cookies and various IDs (such as device IDs and Unified IDs like UID2 and EUID).

| Data Element Type | Description |
| --- | --- |
| First-Party | First-party data elements are segments that you've sent to the platform or that you've authorized another data provider to send to our platform on your behalf. There are no fees associated with using your own data. |
| Third-Party | Third-party data elements are segments that data providers have sent to the platform and are available for you to purchase and target in your audiences. These use a flat-fee CPM, a percentage of media cost, or a combination of both. These fees are clearly outlined in the platform. |

Data elements can be combined into data groups.

## Data groups

A _data group_ is a collection of first-party and/or third-party data elements that are combined using an OR (union) operator. For example, a data group with data element 1 and data element 2 would look for users that match both data element 1 or data element 2.

When creating an audience, you can use data groups to include or exclude their data elements for targeting. Included data groups target only the specified segments of users, while excluded data groups target everyone except the specified segments of users. You can use both included and excluded groups to create the audience you want to target.

Here's what you need to know about data groups when building your audience:

- If more than one data group is _included_ in an audience, a user must match _all of the included_ data groups to be targeted.
- If more than one data group is excluded in an audience, a user may match _any of the excluded_ data groups to be removed from targeting.
- If a user matches _both_ included and excluded data groups, the user will be _excluded_ from the audience.
- Excluding third-party data elements from a data group has a $0.09 CPM fee, in addition to any fee charged by the data provider to use the segment.

The following diagram illustrates the audience segment that is targeted when multiple data groups are included and excluded within an audience.

## Audience creation workflow

To create an audience, complete the following steps:

1. Send first-party data or use third-party data buyable within the platform.
2. Look up first-party data and third-party data element IDs to use within a data group.
3. Create data groups to include in or exclude from audiences.
4. Assign data groups to audiences.
5. Assign audiences to ad groups.

The following sections provide examples for these and other related tasks.

## Data element tasks

The following table lists the tasks for managing data elements in both the Platform and Data API.

> **NOTE**: The Data API requires a different authentication.

| Task | API Suite | Endpoint or Further Reference | Notes |
| --- | --- | --- | --- |
| Populate first-party segment data. | Data | POST /data/advertiser | Populate your segments with cookies or acceptable types of IDs. For details, see Getting started with data onboarding. |
| Create geofence segments. | Platform | Geofence targeting | Create your own geofence segment and use points to define virtual boundaries to target specific areas. |
| Look up first-party data elements. | Platform | POST /v3/dmp/firstparty/advertiser | To find the `FirstPartyDataId` to use in a data group, use the `Data.Name` value that you assigned to the segment when populating first-party segment data as a `SearchTerm`. |
| Look up third-party data elements. | Platform | POST /v3/dmp/thirdparty/advertiser | Look up the `ThirdPartyDataId` to add to a data group. |
| Remove inactive users from first-party data segments. | Data | POST /data/advertiser | To remove an inactive user, set the `TTLInMinutes` property to `0` for that user in the request. **TIP**: To delete the whole segment, set the `TTLInMinutes` property to `0` for all IDs in the segment. |
| Look up third-party data elements similar to your first-party data elements. | Platform | GET /v3/dmp/lookalikemodel/build/{firstPartyDataId} POST /v3/dmp/lookalikethirdpartydata/query | Build a lookalike model and find similar `ThirdPartyDataIds` to your `FirstPartyDataId`. |

### First-party data elements: Look-up task examples

> **IMPORTANT**: The POST /v3/dmp/firstparty/advertiser endpoint is deprecated. Existing integrations continue to work, but we recommend using the GraphQL examples in this section for improved performance and expanded functionality.

You can look up first-party data elements by using a variety of filters and sorting, which can be combined to find relevant segments more efficiently.

> **NOTE**: The lookup endpoints return the number of active IDs from the last 7 days and received IDs from the last 30 days. For details, see Unique ID counting methodologies.

The following sections provide examples of different ways of looking up first-party data elements:

- By advertiser
- By unique count
- By search terms
- By data types
- By lookalike model result status

#### Look up all first-party data elements for an advertiser

The following is a POST /v3/dmp/firstparty/advertiser request body example with the `AdvertiserId` property.

```
{
	"AdvertiserId": "advabc",
	"PageStartIndex": 0,
	"PageSize": 10
}
```

The following GraphQL query returns the ID and display name of each first-party data segment that belongs to the advertiser:

```
query GetFirstPartyDataByAdvertiserExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { targetingDataOwnerTypes: { in: [ADVERTISER] } }) {
      nodes {
        ... on FirstPartyTargetingDataSegment {
          id
          displayName
        }
      }
    }
  }
}
```

#### Look up first-party data elements by unique count

> **NOTE**: A minimum-count filter isn't currently available in GraphQL. Use the following REST endpoint instead.

The following is a POST /v3/dmp/firstparty/advertiser request body example with the `AdvertiserId` and `UniqueCountMinimum` properties.

```
{
	"AdvertiserId": "advabc",
	"UniqueCountMinimum": 5000,
	"PageStartIndex": 0,
	"PageSize": 10
}
```

In GraphQL, you can use one of the following fields to sort first-party data elements, for example `order: [{ activeCounts: DESC }]`. Sorting only orders results; it doesn't exclude elements below a threshold the way `UniqueCountMinimum` does.

| Field | Data types |
| --- | --- |
| `activeCounts` | First-party and third-party data |
| `name` | First-party data only |
| `receivedCounts` | First-party data only |

#### Look up first-party data elements by search terms

Search terms may be added to the request to filter results where the search term matches the first-party data ID, name, or data type of the data element.

The following is a POST /v3/dmp/firstparty/advertiser request body example with search terms.

```
{
	"AdvertiserId": "advabc",
	"SearchTerms": ["auto"],
	"PageStartIndex": 0,
	"PageSize": 10
}
```

When the search term is a number or an ID, exact matches against the segment ID and tracking tag ID are also considered, and those results are ranked at the top. The `searchTerm.contains` filter matches segments by name and display name.

The following GraphQL query example returns the ID and display name of first-party data segments matching `auto`:

```
query GetFirstPartyDataBySearchTermExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { targetingDataOwnerTypes: { in: [ADVERTISER] }, searchTerm: { contains: "auto" } }) {
      nodes {
        ... on FirstPartyTargetingDataSegment {
          id
          displayName
        }
      }
    }
  }
}
```

#### Look up first-party data elements by data types

The following is a POST /v3/dmp/firstparty/advertiser request body example with data types.

```
{
	"AdvertiserId": "advabc",
	"DataTypes": ["ImportedAdvertiserData","Keyword"],
	"PageStartIndex": 0,
	"PageSize": 10
}
```

The following GraphQL query example returns the ID and display name of first-party data segments with the data type `IMPORTED_ADVERTISER_DATA`:

```
query GetFirstPartyDataByDataTypeExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { targetingDataOwnerTypes: { in: [ADVERTISER] }, dataType: { eq: IMPORTED_ADVERTISER_DATA } }) {
      nodes {
        ... on FirstPartyTargetingDataSegment {
          id
          displayName
        }
      }
    }
  }
}
```

GraphQL can also filter first-party data by eligibility for targeting and by tracking tag type, using the `targetingEligibility` and `type` filters in the `firstPartyData` object.

The `targetingEligibility` filter takes a single value and defaults to `TARGETING_ELIGIBLE_ONLY` when omitted. For example, `firstPartyData: { targetingEligibility: { eq: ALL } }` returns all segments regardless of eligibility. The following table lists the `TargetingEligibilityFilterInput` values:

| Enum value | Description |
| --- | --- |
| `TARGETING_ELIGIBLE_ONLY` | Return only segments eligible for audience targeting. |
| `NOT_TARGETING_ELIGIBLE` | Return only conversion-only offline pixel segments whose provider opted them out of targeting. |
| `ALL` | Return all segments regardless of targeting eligibility. |

The `type` filter matches the type of tracking tag, such as an image pixel or an offline tracking tag. For example, `firstPartyData: { trackingTagType: { eq: OFFLINE_TRACKING_TAG } }` returns only segments with an offline tracking tag. The following table lists the `TrackingTagDataTypeInput` values:

| Enum value | Description |
| --- | --- |
| `APP_DATA_EVENT_TRACKING_TAG` | Tracking tag corresponding to a single app data event. |
| `DYNAMIC_RULE_TRACKING_TAG` | Nested tracking tag specified using dynamic rules. |
| `IMAGE_PIXEL_TRACKING_TAG` | Image pixel tracking tag. |
| `MERCHANT_EVENT_TRACKING_TAG` | Tracking tag for specific merchant product catalog events. |
| `OFFLINE_TRACKING_TAG` | Offline tracking tag. |
| `ROOT_MERCHANT_TRACKING_TAG` | Root tracking tag for the merchant product catalog. |
| `UNIVERSAL_PIXEL_MAPPING_TRACKING_TAG` | Tracking tag corresponding to a single mapping on a universal pixel. |

#### Look up first-party data elements by lookalike model result status

> **NOTE**: This filter isn't currently available in GraphQL. Use the following REST endpoint instead.

The following is a POST /v3/dmp/firstparty/advertiser request body example with a `LookAlikeModelResultStatuses` property.

```
{
	"AdvertiserId": "ADVERTISER_ID_PLACEHOLDER",
	"LookAlikeModelResultStatuses": "Ready",
	"PageStartIndex": 0,
	"PageSize": 10
}
```

### Remove inactive users from first-party data segments

To remove inactive users from your data segment, in a POST /data/advertiser call, set the `TTLInMinutes` property to `0` for that user.

> **TIP**: To delete the whole segment, set the `TTLInMinutes` property to `0` for all IDs in the segment.

```
{
   "AdvertiserId":"ADVERTISER_ID_PLACEHOLDER",
   "Items":[
      {
         "TDID":"123e4567-e89b-12d3-a456-426652340000",
         "Data":[
            {
               "Name":"1210",
               "TimestampUtc": "2023-11-11T10:11:30+5000",
               "TTLInMinutes":0
            },
            {
               "Name":"1160",
               "TimestampUtc": "2023-11-13T09:35:30+5000",
               "TTLInMinutes":0
            }
         ]
      }
   ]
}
```

Removing inactive users in GraphQL is a two-step process that uses the `crmDropBind` mutation to generate a data drop endpoint, to which you then upload the list of inactive users. For details, see Remove inactive users from a data segment.

> **TIP**: To archive an entire data segment, use the `crmDataSegmentArchive` mutation, specifying the data segment ID to archive. For details, see Archive a data segment.

### Third-party data elements: Look-up task examples

You can look up third-party data elements by using a variety of filters and sorting, which can be combined to find relevant segments more efficiently.

> **NOTE**: The lookup endpoints return the number of active IDs from the last 7 days and received IDs from the last 30 days. For details, see Unique ID counting methodologies.

The following sections provide examples of different ways of looking up third-party data elements:

- By advertiser
- By ID
- By unique count
- By search terms
- By any demographic data
- By demographic category
- By data rate
- By relevance and value score
- By ad environment

#### Look up all third-party data elements for an advertiser

The following is a POST /v3/dmp/thirdparty/advertiser request body example with the `AdvertiserId` property.

```
{
	"AdvertiserId": "advabc",
	"PageStartIndex": 0,
	"PageSize": 10
}
```

The following GraphQL query example returns the ID and full path of each third-party data segment from data providers:

```
query GetThirdPartyDataByAdvertiserExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { targetingDataOwnerTypes: { in: [DATA_PROVIDER] } }) {
      nodes {
        ... on ThirdPartyTargetingDataSegment {
          id
          fullPath
        }
      }
    }
  }
}
```

#### Look up third-party data elements by ID

The following is a POST /v3/dmp/thirdparty/advertiser request body example with the `ThirdPartyDataIds` property.

```
{
	"AdvertiserId": "advabc",
	"ThirdPartyDataIds": [123456, 789012],
	"PageStartIndex": 0,
	"PageSize": 10
}
```

The `targetingDataId` filter goes directly in the `where` argument, not inside the `thirdPartyData` object. It's also available for first-party data (for example `targetingDataId: { eq: "123456" }`).

The following GraphQL query example returns the ID and full path of third-party data segments with the targeting data IDs `123456` or `789012`:

```
query GetThirdPartyDataByIdExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { targetingDataOwnerTypes: { in: [DATA_PROVIDER] }, targetingDataId: { in: ["123456", "789012"] } }) {
      nodes {
        ... on ThirdPartyTargetingDataSegment {
          id
          fullPath
        }
      }
    }
  }
}
```

#### Look up third-party data elements by unique count

> **NOTE**: A minimum-count filter isn't currently available in GraphQL. Use the following REST endpoint instead.

The following is a POST /v3/dmp/thirdparty/advertiser request body example with the `AdvertiserId` and `UniqueCountMinimum` properties.

```
{
	"AdvertiserId": "advabc",
	"UniqueCountMinimum": 5000,
	"PageStartIndex": 0,
	"PageSize": 10
}
```

#### Look up third-party data elements by search terms

The following is a POST /v3/dmp/thirdparty/advertiser request body example with search terms.

> **IMPORTANT**: All terms must be matched in the `Name` or `FullPath` in order for a result to be returned.

```
{
	"AdvertiserId": "advabc",
	"SearchTerms": ["auto"],
	"PageStartIndex": 0,
	"PageSize": 10
}
```

Numeric search terms match exactly against the `id`, `providerElementId` (the ID that the data provider assigns), or `thirdPartyDataId` fields. Text terms match the `name`, `fullPath`, and `providerElementId` fields, and also return semantically related segments (for example, searching `auto` can also return segments about cars), all ranked together by relevance.

The following GraphQL query example returns the ID and full path of third-party data segments that match `auto`:

```
query GetThirdPartyDataBySearchTermExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { targetingDataOwnerTypes: { in: [DATA_PROVIDER] }, searchTerm: { contains: "auto" } }) {
      nodes {
        ... on ThirdPartyTargetingDataSegment {
          id
          fullPath
        }
      }
    }
  }
}
```

#### Look up all third-party data elements with demographic data

GraphQL can return third-party data segments that have demographic data. To do this, set `demographicThirdPartyData` to an empty object, so the query doesn't narrow the results by age, gender, or country.

The following GraphQL query example returns the ID and full path of each third-party data segment that has demographic data:

```
query GetAllDemographicThirdPartyDataExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { demographicThirdPartyData: {} }) {
      nodes {
        ... on ThirdPartyTargetingDataSegment {
          id
          fullPath
        }
      }
    }
  }
}
```

#### Look up third-party data elements by demographic category

To look up category IDs, use the GET /v3/dmp/thirdparty/facets/{advertiserId} endpoint.

The following is a POST /v3/dmp/thirdparty/advertiser request body example with the `CategoryId` of `526` for the demographic category including ages 18-24 years.

```
{
	"AdvertiserId": "advabc",
	"CategoryIds": [526],
	"PageStartIndex": 0,
	"PageSize": 10
}
```

> **NOTE**: GraphQL doesn't use an opaque category ID for demographic filtering. Instead, filter on the underlying demographic attributes directly, using the `demographicThirdPartyData` object. Setting this object routes the query through a separate search path that ignores the `targetingDataOwnerTypes` filter, so you don't need to include the `targetingDataOwnerTypes` filter in the same `where` argument.

The following GraphQL query example returns the ID and full path of third-party data segments for ages 18 to 24:

```
query GetThirdPartyDataByDemographicCategoryExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { demographicThirdPartyData: { startAge: { eq: EIGHTEEN }, endAge: { eq: TWENTY_FOUR } } }) {
      nodes {
        ... on ThirdPartyTargetingDataSegment {
          id
          fullPath
        }
      }
    }
  }
}
```

The `startAge` and `endAge` filters each take a single `TargetingStartAgeInput` or `TargetingEndAgeInput` enum value, spelled out because GraphQL enum members can't start with a digit. Start age and end age are separate enums with different member sets, not symmetric halves of the same bracket boundaries, so don't assume an end-age member exists just because the matching start-age member does (for example, `TWENTY_FOUR` is a valid end age but not a valid start age).

| Start age enum value | Age | End age enum value | Age |
| --- | --- | --- | --- |
| `TWO` | 2 | `SEVENTEEN` | 17 |
| `THIRTEEN` | 13 | `TWENTY` | 20 |
| `EIGHTEEN` | 18 | `TWENTY_FOUR` | 24 |
| `TWENTY_ONE` | 21 | `TWENTY_NINE` | 29 |
| `TWENTY_FIVE` | 25 | `THIRTY_FOUR` | 34 |
| `THIRTY` | 30 | `THIRTY_NINE` | 39 |
| `THIRTY_FIVE` | 35 | `FORTY_FOUR` | 44 |
| `FORTY` | 40 | `FORTY_NINE` | 49 |
| `FORTY_FIVE` | 45 | `FIFTY_FOUR` | 54 |
| `FIFTY` | 50 | `SIXTY_FOUR` | 64 |
| `FIFTY_FIVE` | 55 | `SIXTY_FOUR_PLUS` | 64 and up |
| `SIXTY_FIVE` | 65 |  |  |

You can also filter by gender and country, using the `genderCode` and `countryId` filters. The `genderCode` filter takes one of `BOTH`, `FEMALE`, or `MALE`. The `countryId` filter takes an integer. Demographic segments use the same country list as Nielsen reporting. To look up a country's ID, use Query.nielsenReportingCountries, which returns the ID as a string. In the filter, write the value without quotes so it's treated as an integer, for example `demographicThirdPartyData: { countryId: { eq: 2 } }` for the United States.

The following is a GraphQL query example that returns the country IDs:

```
query GetNielsenReportingCountriesExample {
  nielsenReportingCountries(first: 100, where: { isActive: { eq: true } }) {
    nodes {
      id
      code
      displayName
    }
  }
}
```

Relevance and value scores are also available for demographic third-party segments, the same way as for general third-party segments—see Look up third-party data elements by relevance and value score.

#### Look up third-party data elements by data rate

You can filter segments that have a certain data rate or data rate type.

The following is a POST /v3/dmp/thirdparty/advertiser request body example with the `CPMFilter` filter.

```
{
	"AdvertiserId": "advabc",
	"DataRateFilters": {
    	"CPMFilter": {
      		"MinimumCPM": {
        		"Amount": 3,
        		"CurrencyCode": "USD"
      		},
      		"MaximumCPM": {
        		"Amount": 7,
        		"CurrencyCode": "USD"
     		}
    	}
  	},
	"PageStartIndex": 0,
	"PageSize": 10
}
```

> **NOTE**: GraphQL filters by predefined cost bands instead of an arbitrary minimum and maximum CPM amount.

The following GraphQL query example returns the ID and full path of third-party data segments priced between $1.00 and $2.00 CPM:

```
query GetThirdPartyDataByDataRateExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(where: { targetingDataOwnerTypes: { in: [DATA_PROVIDER] }, thirdPartyData: { cost: { in: [BETWEEN1_TO2_CPM] } } }) {
      nodes {
        ... on ThirdPartyTargetingDataSegment {
          id
          fullPath
        }
      }
    }
  }
}
```

The `cost` filter accepts one or more band values. Data rate is priced either as a flat CPM or as a percentage of media cost. The following table lists the `CostInput` values:

| Enum value | Description |
| --- | --- |
| `LESS_THAN50_CPM` | CPM less than $0.50 |
| `BETWEEN50_TO1_CPM` | CPM between $0.50 and $1.00 |
| `BETWEEN1_TO2_CPM` | CPM between $1.00 and $2.00 |
| `MORE_THAN2_CPM` | CPM more than $2.00 |
| `LESS_THAN15_REV_SHARE` | Percent of media cost less than 15% |
| `BETWEEN15_TO20_REV_SHARE` | Percent of media cost between 15% and 20% |
| `MORE_THAN20_REV_SHARE` | Percent of media cost more than 20% |

GraphQL can also filter third-party data by `thirdPartyData.brandName`. The `brandName` field takes a list of brand names, for example `thirdPartyData: { brandName: { in: ["Acme Corp"] } }`. This filters by name directly, unlike the ID-based `BrandIds` values on REST endpoints.

#### Look up third-party data elements by relevance and value score

GraphQL can also return a relevance score and a value score for each third-party data segment, calculated against a modeling source you provide.

The following GraphQL query example returns the relevance score and value score of each third-party data segment:

```
query GetThirdPartyDataByModelingSourceExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(
      where: { targetingDataOwnerTypes: { in: [DATA_PROVIDER] } }
      relevanceModelingSource: { channel: DISPLAY, modelingSourceTargetingDataId: 338942495 }
    ) {
      edges {
        relevanceScore {
          value
        }
        node {
          ... on ThirdPartyTargetingDataSegment {
            id
            fullPath
          }
        }
        dataRates {
          valueScore {
            value
          }
          brand {
            id
            name
          }
        }
      }
    }
  }
}
```

The `modelingSourceTargetingDataId` field is the seed ID used to calculate both scores. Write it as a number, without quotes.

You can also filter results to a minimum or maximum score, instead of just retrieving the values, using the `thirdPartyData.relevanceScoreRange` and `thirdPartyData.valueScoreRange` objects. Each object can take an optional `min` integer and an optional `max` integer, for example `thirdPartyData: { relevanceScoreRange: { min: 50 } }` to return only segments scoring 50 or above.

To sort results, add an `order` array to the `targetingDataSegments` call with one of the following third-party data fields, for example `order: [{ relevance: DESC }]`:

| Field | Data types |
| --- | --- |
| `activeCounts` | First-party and third-party data |
| `cost` | Third-party data only |
| `relevance` | Third-party data only |
| `valueScore` | Third-party data only |

#### Look up third-party data elements by ad environment

You can filter segments by either `Web` or `InApp` ad environment.

The following is a POST /v3/dmp/thirdparty/advertiser request body example with the `InApp` filter.

```
{
	"AdvertiserId": "advabc",
	"AdEnvironment": "InApp",
	"PageStartIndex": 0,
	"PageSize": 10
}
```

### Third-party data elements similar to your first-party data element: Look-up tasks

> **NOTE**: Third-party data elements are available only in our production environment.

| Task | API Suite | Endpoint |
| --- | --- | --- |
| Look up eligible first-party data segments | Platform | POST /v3/dmp/firstparty/advertiser |
| Build a lookalike model of third-party data elements | Platform | GET /v3/dmp/lookalikemodel/build/{firstPartyDataId} |
| Check the lookalike model build status | Platform | GET /v3/dmp/lookalikemodel/{firstPartyDataId} |
| Retrieve third-party data elements from the lookalike model | Platform | POST /v3/dmp/lookalikethirdpartydata/query/ |

#### Look up eligible first-party data segments

For the best probability of having enough first-party data to generate a lookalike model, search for eligible first-party segments that have a minimum unique count ranging from 1000 to 5000.

The following is a POST /v3/dmp/firstparty/advertiser request body example.

```
{
	"AdvertiserId": "advabc",
	"UniqueCountMinimum": 4000,
	"LookAlikeModelEligibilities": ["Eligible"],
	"PageStartIndex": 0,
	"PageSize": 10
}
```

#### Build a lookalike model of third-party data elements

Building a lookalike model is available in REST only. Make a request to the GET /v3/dmp/lookalikemodel/build/{firstPartyDataId} endpoint.

#### Check the lookalike model build status

Checking the build status of a lookalike model is available in REST only. Make a request to the GET /v3/dmp/lookalikemodel/{firstPartyDataId} endpoint.

The response includes a `LookAlikeBuildStatus` value, which indicates whether the lookalike model build is processing (`Queued`) or was completed (`Built`). The response also includes a `LookAlikeModelResultStatus` value.

The following table explains the `LookAlikeModelResultStatus` values.

| Status Value | Description |
| --- | --- |
| `NoResults` | The first-party data segment the model was generated from did not have enough overlap with third-party data to generate model. |
| `Ready` | The lookalike model has been generated and `ThirdPartyDataIds` can be retrieved to use in an audience. |

#### Retrieve third-party data elements from the lookalike model

Search for the results of the build using the query endpoint. The `Result` object shows the third-party data segments similar to the first-party data segment, as well as a relevance ratio and value ratio to help you evaluate the best segments to use in your audience. Use `Result.ThirdPartyData.ThirdPartyDataId` in your data groups.

The following is a POST /v3/dmp/lookalikethirdpartydata/query request body example.

```
{
	"FirstPartyDataId": 1234567,
	"PageStartIndex": 0,
	"PageSize": 10
}
```

To retrieve lookalike results in GraphQL, look up the first-party segment by its targeting data ID, then select the `lookAlikeThirdPartyData` field under `edges`. The field returns `null` when the segment isn't a first-party segment.

The following GraphQL query example returns the relevance ratio, ID, and full path of up to 10 third-party data segments that are similar to the first-party segment with the ID `1234567`:

```
query GetLookalikeThirdPartyDataExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    targetingDataSegments(first: 1, where: { targetingDataId: { eq: "1234567" } }) {
      edges {
        lookAlikeThirdPartyData(first: 10) {
          nodes {
            relevanceRatio
            targetingDataSegment {
              ... on ThirdPartyTargetingDataSegment {
                id
                fullPath
              }
            }
          }
        }
      }
    }
  }
}
```

The value ratio and the REST filters (such as search terms, unique count and relevance ratio) aren't currently available in GraphQL.

## Data group tasks

| Task | API Suite | Endpoint | Notes |
| --- | --- | --- | --- |
| Create a data group | Platform | POST /v3/datagroup | All third-party data IDs in segments will be validated for biddability. Data group workflows will fail if the `ThirdPartyDataIds` array contains non-biddable IDs. |
| Retrieve details for an individual data group by ID | Platform | GET /v3/datagroup/{dataGroupId} | N/A |
| Look up all data groups for an advertiser | Platform | POST /v3/datagroup/query/advertiser | Use `SearchTerms` to search for matching terms in `DataGroupId`, `DataGroupName`, or `Description`. |
| Look up all data groups since the last change tracking version | Platform | POST /v3/delta/dmp/query/advertiser/firstparty | N/A |
| Update a data group | Platform | PUT /v3/datagroup | All third-party data IDs in segments will be validated for biddability. Data group workflows will fail if the `ThirdPartyDataIds` array contains non-biddable IDs. |

### Create data groups

> **NOTE**: Data groups are created using the Platform API endpoints. For details, see Foundations.

Here's what you need to know about data groups:

- You share data groups among multiple audiences. Just set the `IsSharable` property to `true`.
- To create the data group without third-party data segments that you are not authorized to use, set the `SkipUnauthorizedThirdPartyData` property to `true` when specifying third-party IDs. If not specified or set to `false`, attempting to create a data group with third-party data IDs you are unauthorized to use will result in an error.
- All third-party data IDs in segments will be validated for biddability. Data group workflows will fail if the `ThirdPartyDataIds` array contains non-biddable IDs.

> **TIP**: To check if segments are buyable beforehand, use the POST /v3/dmp/thirdparty/advertiser endpoint. Include only third-party data IDs listed in the response.

The following is a POST /v3/datagroup request body example.

```
{
	"AdvertiserId": "advabc",
	"DataGroupName": "Auto Interest",
	"IsSharable": true,
	"FirstPartyDataIds": [
		1234567
	],
	"ThirdPartyDataIds": [
		"1234567|bluekai"
	],
	"SkipUnauthorizedThirdPartyData": true
}
```

## Audience tasks

| Task | API Suite | Endpoint | Notes |
| --- | --- | --- | --- |
| Create an audience | Platform | POST /v3/audience | For details on what you need to know about data groups when creating audiences, see Data groups. |
| Retrieve Details For An Individual Audience By Id | Platform | GET /v3/audience/{audienceId} | N/A |
| Look up all audiences for an advertiser | Platform | POST /v3/audience/query/advertiser | Use `SearchTerms` to search for matching terms in `AudienceId`, `Audience`, or `Description`. |
| Update an audience | Platform | PUT /v3/audience | For examples, see Assign an audience to an ad group. |

### Create an audience

The following is POST /v3/audience request body examples.

#### Target certain data groups and exclude one data group

```
{
  "AdvertiserId": "adv123",
  "AudienceName": "24-35 Cats Minus Low Value",
  "Description": "Users in the age range 24-35 who are interested in cats and are not low-value users.",
  "IncludedDataGroupIds": [
    "aud1234",
    "aud2345"
  ],
  "ExcludedDataGroupIds": [
    "aud3456"
  ]
}
```

#### Target everyone except one data group

```
{
  "AdvertiserId": "adv123",
  "AudienceName": "Everyone Except Low-Value Users",
  "Description": "Exclude low value users",
  "IncludedDataGroupIds": [],
  "ExcludedDataGroupIds": [
    "aud3456"
  ]
}
```

#### Assign an audience to an ad group

The following is a PUT /v3/adgroup request example that shows how to assign an audience to an existing ad group.

```
{
	"AdGroupId": "adgr123",
	"RTBAttributes": {
		"AudienceTargeting": {
			"AudienceId": "aud1234"
		}
	}
}
```

- To target everyone (run-of-exchange), do not enable any properties in the `RTBAttributes.AudienceTargeting` object of the ad group.
- To target only trackable users, on the ad group, enable `RTBAttributes.AudienceTargeting.TargetTrackableUsersEnabled` to restrict targeting only to users that we can track (users we have a `TDID` or a device ID for).
We'll create a new audience for you that includes only trackable users.

> **NOTE**: There is a fee to use this feature which you can look up by using the ad group's `RTBAttributes.AudienceTargeting.TargetTrackableUsersFee` object.

To view a full list of Koa features, see Ad groups.

## FAQs

We've got answers to your most commonly asked questions.

### How is audience different from seed?

Audience and seed are not the same. They are two discrete entities.

A seed is a specific, concentrated group of individuals who represent the core group of people that you want to target. This group typically consists of individuals who have taken valuable actions or exhibit traits that align with your campaign goals. An audience, on the other hand, is an expanded version of the core group, which includes not only the individuals in your seed but also extends to others who share similar traits or behaviors.

### Can I create an audience with geolocation data?

Yes. To do this, include your third-party or first-party geofence segment ID in a data group and add it to your audience. For details on how to create first-party geofence data segments, see Geofence targeting.
