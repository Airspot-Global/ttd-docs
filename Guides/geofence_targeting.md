# Geofence Targeting

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/GeofenceTargeting
- Category: Guides

---

# Geofence Targeting

As an advertiser, you can target [audiences](/v3/portal/api/doc/Audience) using geofence segments, which group users by location rather than individual IDs.

Here's what you need to know about creating geofence segments:

*   Geofence segments enable you to target geographic areas without a third-party provider.
*   You can define the virtual boundary of a geofence as a circle or a polygon, with coordinates that define the location of the following:
    *   The center of the circle
    *   The vertices (also known as points) of the polygon
*   The area within a geofence segment must cover at least 31,400 square meters in total. For example, you can have a geofence that covers 100 meters, or multiple circles or polygon points that sum up to a total area of 31,400 square meters.
*   For polygons, you must use a combination of the GraphQL and REST APIs.
*   To access the REST endpoint for creating circle geofence segments, contact your Technical Account Manager.

Geofence segments are also subject to certain policies and laws. The following sections detail these policies and outline the steps for creating and managing geofence segments.

## 

Data Policies and Restrictions[](#policies)

Depending on the areas and locations you want to target, geofence segments must adhere to the relevant data privacy policies based on these locations. See also [Data Privacy and Transparency](/v3/portal/resources/doc/PrivacyTransparencyRegulations).

Here's what you need to know about these privacy policies:

*   Due to legal requirements in the United States, geofences that contain coordinates in the states of _Connecticut_, _Washington_, _Nevada_, or _New York_, require a minimum area coverage of 3000 feet (914 meters).
*   You may not create a geofence segment that covers the mainland China region.
*   Sensitive locations, such as hospitals and municipal buildings, can be in the geofence area, but bidding is blocked within a 50-meter radius of these sensitive locations.

## 

Workflow Diagram[](#diagram)

The following diagram illustrates the [process](#process) outlined in the next section, which includes links to the respective step-by-step instructions and also provides additional guidance on the decisions you might need to make along the way.

![Add Geo Data to Data Elements Diagram](/v3/content/docs/Images/geofence-data.svg)

## 

Process Overview[](#process)

The following table outlines the process step by step, while the [diagram](#diagram) in the preceding section illustrates the decision-making workflow.

| Step |  | Task | API | Endpoint, Operation, or Further Reference | Notes |
| **1** |  | Choose the type of geofence segment you want to create. | N/A | N/A | None. |
|  | **a** | Create a [circle](#circles) geofence segment. | REST | [POST /v3/selfservegeofence](/v3/portal/api/ref/post-selfservegeofence) | A successful response returns the geofence segment ID as the `ThirdPartyDataId` value for creating data groups. |
|  | **b** | Create a [polygon](#polygons) geofence segment. | GraphQL | `fileUpload` mutation  
`customPolygonGeofenceCreate` mutation | A successful response returns the geofence segment ID as the `data.id` value for creating data groups. |
| **2** |  | Add your geofence segments to bid lists or data groups. | REST or GraphQL | N/A | To add a geofence segment, you must include the geofence segment ID and the brand ID with the `ttdgeofence` value.  
**TIP**: To [retrieve](#retrieve-geofences) your geofence segment ID and other details, use the GraphQL `customGeofencesSearch` query. |
|  | **a** | For targeting users within the geofence, add it to a data group. | REST | [Audiences](/v3/portal/api/doc/Audience) | For details on adding a geofence, see [Data Group Example](#data-groups). |
|  | **b** | For optimizing bids on impressions within the geofence, add it to a bid list. | REST or GraphQL | [Bid Lists](/v3/portal/api/doc/BidList) | For details on adding a geofence, see [Bid List Example](#bid-lists). |

### 

Create a Circle Geofence Segment[](#circles)

A circle geofence segment, also known as radius targeting, is defined by a center point specified by latitude and longitude coordinates, and a radius that extends in all directions to form a circular area.

To create a circle geofence segment, in a [POST /v3/selfservegeofence](/v3/portal/api/ref/post-selfservegeofence) call, include the following:

*   A display name for your geofence segment that appears in the platform UI.
*   Either your advertiser ID or partner ID.
*   A list of up to 10,000 circles that define the geographic areas you want to target.

> **IMPORTANT**: After you create a geofence segment, you cannot modify or delete it.

To add a circle to your geofence segment, in the `Points` list, include the following values for each point you want to add.

| Property | Value |
| `LngDeg` | The longitude (X) coordinate. |
| `LatDeg` | The latitude (Y) coordinate. |
| `RadMet` | The radius of the circle, in meters. |

> **TIP**: You can include multiple circles within the same geofence segment.

#### Request Example

Here's an example of a [POST /v3/selfservegeofence](/v3/portal/api/ref/post-selfservegeofence) request with two sets of coordinates and radii listed.

{

  "AdvertiserId": "abcd1234",

  "DisplayName": "Hiking Geofence",

  "Description": "Areas to target for hiking.",

  "Points": \[

    {

      "LngDeg": 65.82137,

      "LatDeg": \-82.327429,

      "RadMet": 3000

    },

    {

      "LngDeg": \-17.600772,

      "LatDeg": \-66.155554,

      "RadMet": 3000

    }

  \]

}

#### Response Example

A successful response returns the geofence segment ID as the `ThirdPartyDataId` value.

> **IMPORTANT**: Be sure to take note of the returned `ThirdPartyDataId` value. You need this ID to create audience [data groups](/v3/portal/api/doc/Audience#createdatagroups).

{

  "ThirdPartyDataBrandId": "ttdgeofence",

  "ThirdPartyDataId": 30047,

  "Points": \[

    {

      "LngDeg": 65.821370000000002,

      "LatDeg": \-82.327428999999995,

      "RadMet": 3000

    },

    {

      "LngDeg": \-17.600771999999999,

      "LatDeg": \-66.155553999999995,

      "RadMet": 3000

    }

  \]

}

### 

Create a Polygon Geofence Segment[](#polygons)

A polygon geofence segment contains coordinates for each vertex of its shape. To create a polygon geofence segment, complete the following steps:

1.  Create a [GeoJSON file](#geojson-file).
2.  Generate a URL to [upload the GeoJSON file](#upload-url).
3.  Create the [polygon geofence segment](#create-polygon-segment).

#### Create the GeoJSON File

To define the shape of a polygon geofence, you must create a GeoJSON file and include the latitude and longitude coordinates for each vertex in your polygon.

> **NOTE**: You can add up to 10,000 points to a single polygon geofence.

Here's an example of a GeoJSON object that includes all of the required properties and the coordinates of a polygon that has six vertices.

{

  "type": "Feature",

  "geometry": {

    "type": "Polygon",

    "coordinates": \[

      \[

        \[\-122.198802243051, 47.6259927781354\],

        \[\-122.198754376278, 47.6258714779866\],

        \[\-122.198551421159, 47.6259514844992\],

        \[\-122.198568653198, 47.6260160057918\],

        \[\-122.198693106808, 47.626012134516\],

        \[\-122.198802243051, 47.6259927781354\]

      \]

    \]

  },

  "properties": {}

}

After you create the GeoJSON file, you must [upload it](#upload-url) to the platform.

#### Upload the GeoJSON File

To upload the GeoJSON file to the platform, complete the following steps.

| Step | Task | Notes |
| **1** | Generate the upload URL. | Be sure to save the file ID for future reference—otherwise, you'll have to re-upload the file before proceeding.  
**IMPORTANT**: The generated URL expires after 30 minutes. |
| **2** | Use the URL to upload the file. | You can upload only GeoJSON files. |

To generate an upload URL, use the `fileUpload` mutation and set the `fileExtension` field to `geojson`.

mutation {

  fileUpload(fileExtension: "geojson") {

    id

    uploadUrl

  }

}

Here's a cURL call example with two placeholders: one for the upload URL returned in the `uploadUrl` field and the other for the file name with the `geojson` extension.

curl -X UPLOAD\_URL\_PLACEHOLDER

 -H "File-Extension: geojson"

 -H "x-ms-blob-type: BlockBlob"

 --data-binary "GEOJSON\_FILE\_NAME\_WITH\_EXTENSION\_PLACEHOLDER"

After you upload the file, you must [create the segment](#create-polygon-segment).

#### Create the Polygon Geofence Segment

To create the polygon geofence segment, use the GraphQL `customPolygonGeofenceCreate` mutation.

mutation {

  customPolygonGeofenceCreate(

    customPolygonGeofenceCreateInput: {

      advertiserId: "ADVERTISER\_ID\_PLACEHOLDER"

      name: "GEOFENCE\_SEGMENT\_NAME\_PLACEHOLDER"

      description: "GEOFENCE\_SEGMENT\_DESCRIPTION\_PLACEHOLDER"

      fileId: "GEOJSON\_FILE\_ID\_PLACEHOLDER"

    }

  ) {

    data {

      name

      description

      id

    }

    errors {

      ... on CustomGeofenceValidationError{

        message

        field

      }

    }

  }

}

A successful response returns the geofence segment ID as the `data.id` value.

> **IMPORTANT**: Be sure to take note of the returned `data.id` value. You need this ID to create audience [data groups](/v3/portal/api/doc/Audience#createdatagroups).

## 

Retrieve Geofence Segments[](#retrieve-geofences)

After you create a circle or polygon geofence segment, you can retrieve details about your segment such as the shape, GeoJSON download link, and the geofence segment ID you need to create data groups.

To retrieve a list of geofence segments you created, use the GraphQL `customGeofencesSearch` query and include your advertiser ID.

query GetAdvertiserGeofencesExample {

  customGeofencesSearch(

    input: { advertiserId: "ADVERTISER\_ID\_PLACEHOLDER"}

  ) {

    nodes {

      description

      geoTargets {

        nodes {

          geoTargetType

          id

          latitudeDegrees

          longitudeDegrees

          polygonFileDownloadUrl

          radiusInMeters

        }

      }

    }

  }

}

## 

Add Geofence Segments to Audience Data Groups and Bid Lists[](#audiences-bid-lists)

To add your geofence segment to an audience or bid list, you must include its ID and the brand ID `ttdgeofence` value.

#### Bid List Example

Here's a code snippet of a GraphQL `bidListCreate` mutation that shows how to add a geofence segment to a bid line.

bidLines: \[

  {

    geofenceThirdPartyDataAndBrand: {

      brandId: "ttdgeofence",

      dataId: "GEOFENCE\_ID\_PLACEHOLDER"

    }

  }

\]

For details about creating bid lists, see [Create and Manage Bid Lists in GraphQL](/v3/portal/api/doc/BidListsCreateManageGQL).

#### Data Group Example

Here's a code snippet of a [POST /v3/datagroup](/v3/portal/api/ref/post-datagroup) request, which shows how to add a geofence segment ID and the brand ID as a single value separated by a pipe (|) with no spaces around it.

"ThirdPartyDataIds": \[

  "GEOFENCE\_ID\_PLACEHOLDER|ttdgeofence"

\]

For details about creating data groups and audiences, see [Audiences](/v3/portal/api/doc/Audience).

## 

FAQs[](#faqs)

The following is a list of commonly asked questions about geofence segments.

### 

Do I have to design a taxonomy for my geofence segments?

No. Each geofence segment is created at the root level and does not have a parent-child relationship.

### 

How do I update my geofence segment after I create it?

You cannot update or change any information in your geofence segment after you create it.

### 

How many circles or polygon points can I add to a geofence segment?

You can create a maximum of 10,000 circles or polygon points in a single geofence segment. However, The Trade Desk recommends creating no more than 2000 circles or polygon points.

### 

Who provides the data used to create these geofence segments?

The Trade Desk provides the data used for geofence segments.

### 

Can other advertisers use a geofence segment that I created?

No. Each geofence segment is unique to the advertiser it was created under.

### 

How do I associate a different advertiser to my geofence segment?

You cannot associate a different advertiser to your geofence segment. Alternatively, you can create a new segment with the same name and geofence data and use the ID of the advertiser to which you want to associate.

### 

Are there any locations I can't target with geofence segments?

Yes. Sensitive locations, such as hospitals and municipal buildings, can be in the geofence area, but bidding is blocked within a 50-meter radius of these sensitive locations.

### 

What is the difference between geofence segments and geo-interest segments?

Geofence segments target based on locations that you specify while [geo-interest](/v3/portal/api/doc/GeoInterestExpansion) segments target areas based on interest.

### 

How do I retrieve my geofence segment ID for my segment?

Use the GraphQL `customGeofencesSearch` query and include your advertiser ID. For details, see [Retrieve Geofence Segments](#retrieve-geofences).