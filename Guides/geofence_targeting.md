# Geofence Targeting

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/GeofenceTargeting
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/GeofenceTargeting (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Geofence targeting

Geofence targeting enables you to deliver ads in specific locations by targeting geofence segments, which group users by geographical area rather than individual IDs, as part of an audience. Geofence segments are also subject to certain policies and laws.

The following sections detail the policies and laws that apply to geofence segments, and outline the steps for creating and managing them.

## Data policies and restrictions

Depending on the areas and locations you want to target, geofence segments must adhere to the relevant data privacy policies based on these locations. See also Data privacy and transparency.

Here's what you need to know about these privacy policies:

- Due to legal requirements in the United States, geofences that contain coordinates in the states of **Connecticut**, **Washington**, **Nevada**, or **New York** require a minimum area coverage of 3000 feet (914 meters).
- You may not create a geofence segment that covers the mainland China region.
- Sensitive locations, such as hospitals and municipal buildings, can be in the geofence area, but bidding is blocked within a 50-meter radius of these sensitive locations.

## Geofence segment types

To target impressions based on location, you can create a geofence segment with the area you want to target, and add that segment to your audiences or bid lists. Here's what you need to know about creating geofence segments:

- You can define the virtual boundary of a geofence as a circle or a polygon, with coordinates that define the location of the following:

  - The center of the circle
  - The vertices (also known as points) of the polygon

- The area within a geofence segment must cover at least 31,400 square meters in total. For example, you can have one geofence that covers 31,400 square meters, or multiple circles or polygon points that sum up to a total area of 31,400 square meters.

The following table summarizes each geofence type and the operations to create it.

| Geofence segment type | Description | Operation | Supported file types |
| --- | --- | --- | --- |
| Circles | One or more circles, each surrounding a point on the map such as a store, event, or venue. | `fileUpload` mutation (optional) `customCircularGeofenceCreate` mutation | XLSX |
| Polygon | A precise or irregular boundary around an area such as a stadium, neighborhood, or city. | `fileUpload` mutation `customPolygonGeofenceCreate` mutation | GeoJSON |

After you create a geofence segment, you can update it without creating a new one. For details, see Management tasks.

## Create a circle geofence segment

A circle geofence segment, also known as radius targeting, is a container of circles, each defined by a center point of latitude and longitude coordinates and a radius size. Here's what you need to know about creating circle geofence segments:

- You must provide your center point coordinates in `latitude, longitude` format.
- You can provide your coordinates as a file or include them in the mutation.
- There are two ways you can set the radii of circles in the segment: same size for all circles, or a different size for each circle.

If needed, you can view individual circles in the Geofence Performance Report. To do this, contact your Technical Account Manager to request access, then include the required properties in your GeoJSON file. For details, see Include circles in reporting.

There are two ways you can provide your coordinates and radii to create circle geofence segments: by file or directly in the mutation. The following table summarizes and compares both methods.

| Use case | Method | Required fields | Notes |
| --- | --- | --- | --- |
| You want a streamlined, single-step workflow. | Provide coordinates in the mutation field values. | `data.text` | None. |
| You have a large number of coordinates you want to add. | Upload an XLSX file. | `data.fileId` | - This is a four-step process. - The generated upload URL expires after 30 minutes. |

### Provide coordinates in the mutation

To create a circle segment and provide your coordinates in the mutation, use the `customCircularGeofenceCreate` mutation and include the `radiusUnit` field and provide your center point coordinates in the `data.text` field.

There are two ways you can provide your coordinates and set the size of your circles:

- To set the same size for all circles in your segment, include the `radii` field. To create multiple segments, specify multiple values in the `radii` field.
- To set a different size for each circle, include the radius in your coordinates. You can create only one segment at a time this way.

The following `customCircularGeofenceCreate` mutation example shows how to create two segments with circles that have the same size with placeholder values for the shape ID and name. Segment A has two circles that have a radius of 50 meters, while segment B has two circles that have a radius of 26 meters.

```
mutation {
  customCircularGeofenceCreate(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      name: "GEOFENCE_SEGMENT_NAME_PLACEHOLDER"
      radiusUnit: METERS
      radii: [50, 26]
      data: {
        text: [
          "46.047, 14.522",
          "-27.111, -52.636"
          ]
        }
      }
  ) {
    data {
      id
      name
      description
      geoTargets {
        nodes {
          id
          latitudeDegrees
          longitudeDegrees
          radiusInMeters
        }
      }
    }
    errors {
      __typename
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

A successful response returns a list of the segments you created. After you create your geofence segment, use its ID to add it to your audiences or bid lists. For details, see Next steps.

### Provide coordinates in an XLSX file

If you have a large number of center point coordinates, you can consider including them in a file and upload it to the platform to create the segment. To provide your coordinates in a file, complete the following steps:

1.

Create the XLSX file and provide your coordinates in latitude, longitude format with one row per center point. There are two ways you can set the size of your circles:

  - To set different sizes for all circles in the segment, include a radius column.
  - To set the same size for all circles in the segment, include only the latitude and longitude columns. You will specify the radius when you create the segment. The following table demonstrates how to provide coordinates for circles that have different sizes.

| Latitude | Longitude | Radius |
| --- | --- | --- |
| 46.047 | 14.522 | 50 |
| -27.111 | -52.636 | 75 |

2.

Use the `fileUpload` mutation and set the `fileExtension` field to `xlsx`.

```
mutation {
  fileUpload(fileExtension: "xlsx") {
    id
    uploadUrl
  }
}
```

3.

Use the URL returned in the `uploadUrl` field and make a cURL call. The following cURL call example shows how to upload the XLSX file. There are two placeholders: one for the upload URL returned in the `uploadUrl` field and the other for the file name with the `xlsx` extension.

```
curl -X PUT "UPLOAD_URL_PLACEHOLDER" \
 -H "Content-Type:" \
 -H "File-Extension: xlsx" \
 -H "x-ms-blob-type: BlockBlob" \
 --data-binary "@XLSX_FILE_NAME_WITH_EXTENSION_PLACEHOLDER" \
 -v \
 -w "\nHTTP Status: %{http_code} | Bytes sent: %{size_upload}\n"
```

4.

To create the segments from the file you uploaded, use the `customCircularGeofenceCreate` mutation and include the file ID you generated in step 2 in the `data.fileId` field. Depending on how you want to set the radii of your circles, do either of the following:

  - To set the same size for all circles in your segment, include the `radii` field. To create multiple segments, specify multiple values in the `radii` field.
  - To set a different size for each circle, include the radius in your coordinates. You can create only one segment at a time this way.

> **IMPORTANT**: Do not specify any radii in your XLSX file and include the `radii` field in the mutation. This will result in an error.

The following `customCircularGeofenceCreate` mutation example shows how to create a segment from an uploaded file.

```
mutation {
  customCircularGeofenceCreate(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      name: "GEOFENCE_SEGMENT_NAME_PLACEHOLDER"
      radiusUnit: METERS
      data: { fileId: "XLSX_FILE_ID_PLACEHOLDER" }
    }
  ) {
    data {
      id
      name
    }
    errors {
      __typename
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

### Include circles in reporting

By default, the Geofence Performance Report provides metrics for an entire geofence segment. If you want to compare how individual circles within a segment perform, you can include and identify them individually in the report to view metrics for each circle instead of the segment as a whole.

> **IMPORTANT**: You must have access to the Geofence Performance Report to include a shape ID or name with your coordinates. Contact your Technical Account Manager to request access.

To include and identify individual circles on a Geofence Performance Report, provide coordinates using the following pattern: `latitude, longitude, radius, ID, name`. Here's what you need to know about including individual circles in the report:

- You must separate each field with a comma.
- The `radius` field is optional per coordinate. Leave it blank (`,,`) to use the shared `radii` list instead.
- The ID and name values are optional.
- To exclude the shape from the report, do not include the shape ID and name. If you're using a spreadsheet, leave both cells blank.
- To group multiple circles together in the report, assign them the same ID and name.

> **IMPORTANT**: You cannot assign the same name to circles with different ID values.

The following sections show how to apply the shape ID and name depending on the input provided in your request when you create your circles.

#### Set the same radius size for multiple circles

The following example shows how to provide two coordinates that have a shared `radii` list, with the ID and name values provided for reporting.

```
radii: [50, 26]
data: {
  text: [
    "46.047, 14.522 ,, SHAPE_A_ID_PLACEHOLDER, SHAPE_A_NAME_PLACEHOLDER"
    "-27.111, -52.636 ,, SHAPE_B_ID_PLACEHOLDER, SHAPE_B_NAME_PLACEHOLDER"
  ]
}
```

#### Set a different radius for each circle

The following example shows how to create two circles with different radii: one includes a shape ID and name for reporting, and the other omits them.

```
data: {
  text: [
    "46.047, 14.522, 50, SHAPE_ID_PLACEHOLDER, SHAPE_NAME_PLACEHOLDER"
    "-27.111, -52.636, 75"
  ]
}
```

#### Use the shared radius for all circles

To apply the same radius to all circles in the segment, leave the `radius` position blank and include the `radii` field instead. The following example shows one circle with a shape ID and name included for reporting, and one circle omitted from the report.

```
radii: [50, 75]
data: {
  text: [
    "46.047, 14.522 ,, SHAPE_ID_PLACEHOLDER, SHAPE_NAME_PLACEHOLDER"
    "-27.111, -52.636"
  ]
}
```

#### Group multiple circles under the same shape

To group multiple circles together in the report, assign them the same `ID` and `name`. The following example creates three circles, with the first two grouped under the same shape identifier and the third excluded from the report.

```
radii: [50, 50, 75]
data: {
  text: [
    "46.047, 14.522 ,, SHAPE_A_ID_PLACEHOLDER, SHAPE_A_NAME_PLACEHOLDER"
    "46.052, 14.530 ,, SHAPE_A_ID_PLACEHOLDER, SHAPE_A_NAME_PLACEHOLDER"
    "-27.111, -52.636"
  ]
}
```

To generate the report, you must search for the Geofence Performance Report template and use its report type ID to generate the report. For details, see User-defined reports.

### Response example

A successful response returns the list of geofence segments as objects in the `data` field. Depending on the input provided in your request, the system automatically adds prefixes and suffixes to the segment ID and name. The `Selfserve >` prefix in the name indicates that the segment was created by you, and `-ttdgeofence` is the brand ID you use to include your geofence segments in your bid lists.

```
{
  "data": {
    "customCircularGeofenceCreate": {
      "data": [
        {
          "id": "GEOFENCE_A_ID_PLACEHOLDER-ttdgeofence",
          "name": "Selfserve > GEOFENCE_SEGMENT_NAME_PLACEHOLDER - 50 meters"
        },
        {
          "id": "GEOFENCE_B_ID_PLACEHOLDER-ttdgeofence",
          "name": "Selfserve > GEOFENCE_SEGMENT_NAME_PLACEHOLDER - 26 meters"
        }
      ],
      "errors": null
    }
  }
}
```

After you create your geofence segments, you can add them to your bid lists and audiences. For details, see Next steps.

## Create a polygon geofence segment

A polygon geofence segment lets you define a custom, irregularly shaped boundary, such as a stadium, campus, retail complex, or event venue, using coordinates for each vertex of its shape. You can define a single shape or multiple shapes in one file. For details on supported geometry types, coordinate systems, and file structures, see Polygon file format requirements. Polygon targeting gives you more precise control over ad delivery than shapes like circles or ZIP codes, and is especially effective for the following use cases:

- Hyper-local campaigns focused on unique locations that don't align with fixed-radius, postal codes, or other boundaries.
- Activating first-party geo data you've collected around your own proprietary locations.
- Reaching users in high-value, custom-drawn areas, such as event venues or delivery zones.

If needed, you can view individual polygons in the Geofence Performance Report. To do this, contact your Technical Account Manager to request access, then include the required properties in your GeoJSON file. For details, see Include polygons in reporting.

To create a polygon geofence segment, complete the following steps:

1.

To define the shape of a polygon geofence, create a GeoJSON file and include coordinates in **longitude and latitude** format for each vertex in your polygon. The following GeoJSON object example shows how to include the coordinates of a polygon with six vertices.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-122.198802243051, 47.6259927781354],
            [-122.198754376278, 47.6258714779866],
            [-122.198551421159, 47.6259514844992],
            [-122.198568653198, 47.6260160057918],
            [-122.198693106808, 47.626012134516],
            [-122.198802243051, 47.6259927781354]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-118.488674, 34.069353],
            [-118.483674, 34.074353],
            [-118.478674, 34.069353],
            [-118.483674, 34.064353],
            [-118.488674, 34.069353]
          ]
        ]
      }
    }
  ]
}
```

2.

To generate an upload URL, use the `fileUpload` mutation and set the `fileExtension` field to `geojson`.

> **IMPORTANT**: The generated URL expires after 30 minutes.

```
mutation {
  fileUpload(fileExtension: "geojson") {
    id
    uploadUrl
  }
}
```

> **IMPORTANT**: The upload URL returned in the `uploadUrl` field of the `fileUpload` mutation response contains special characters (such as `&` and `%`) that most shells treat as special. To avoid parsing errors, wrap the URL in quotes.

3.

Use the upload URL you generated in step 2 and make a cURL call.
 The following cURL call example shows how to upload the GeoJSON file. There are two placeholders: one for the upload URL returned in the `uploadUrl` field and the other for the file name with the `geojson` extension.

```
curl -X PUT "UPLOAD_URL_PLACEHOLDER" \
 -H "Content-Type:" \
 -H "File-Extension: geojson" \
 -H "x-ms-blob-type: BlockBlob" \
 --data-binary "@GEOJSON_FILE_NAME_WITH_EXTENSION_PLACEHOLDER" \
 -v \
 -w "\nHTTP Status: %{http_code} | Bytes sent: %{size_upload}\n"
```

4.

To create the polygon geofence segment, use the GraphQL `customPolygonGeofenceCreate` mutation and include the file ID you generated in step 2 before you uploaded the file.

```
mutation {
  customPolygonGeofenceCreate(
    customPolygonGeofenceCreateInput: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      name: "GEOFENCE_SEGMENT_NAME_PLACEHOLDER"
      description: "GEOFENCE_SEGMENT_DESCRIPTION_PLACEHOLDER"
      fileId: "GEOJSON_FILE_ID_PLACEHOLDER"
    }
  ) {
    data {
      name
      description
      id
    }
    errors {
      __typename
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

## Polygon file format requirements

The following sections describe the requirements and best practices for formatting your GeoJSON file:

- Coordinate reference system (CRS)
- Supported geometry types
- Supported file structures
- Best practices

### Coordinate reference system (CRS)

A coordinate reference system (CRS) defines how the numbers in a set of coordinates map to actual locations on Earth — including the unit of measurement (such as degrees or meters) and the model of the Earth's shape used to calculate them. The same coordinate values can represent entirely different locations depending on which coordinate reference system is used to interpret them.

Your coordinates must use the WGS 84 (`EPSG:4326`) CRS, which expresses longitude and latitude in degrees. This is the CRS required by the GeoJSON standard (RFC 7946).

The following example shows a GeoJSON file using the EPSG:4326 CRS.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "name": "Simple polygon" },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-80.0, 25.0],
            [-80.0, 26.0],
            [-79.0, 26.0],
            [-79.0, 25.0],
            [-80.0, 25.0]
          ]
        ]
      }
    }
  ]
}
```

> **IMPORTANT**: The Trade Desk does not recommend using coordinates from a custom coordinate reference system. The platform supports them only for legacy compatibility.

If you must use a different coordinate reference system, such as `EPSG:3857` (Web Mercator, which uses meters instead of degrees), you must include a `crs` object in your GeoJSON file to specify it, as shown in the following snippet.

```
{
  "type": "FeatureCollection",
  "crs": {
    "type": "name",
    "properties": {
      "name": "EPSG:3857"
    }
  },
  // Features array goes here.
}
```

> **NOTE**: The platform recognizes only the `type` and `properties` attributes of the `crs` object. All other attributes are ignored.

### Supported geometry types

The platform supports the following geometry type values in your GeoJSON file:

- `Polygon`
- `MultiPolygon`, which lets you define multiple, disconnected shapes (for example, several store footprints) as a single feature.

Each shape must use `longitude, latitude` coordinate order, not latitude, longitude.

The following example shows a MultiPolygon feature that defines two separate shapes.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "name": "MultiPolygon example" },
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [-70.0, 30.0],
              [-70.0, 31.0],
              [-69.0, 31.0],
              [-69.0, 30.0],
              [-70.0, 30.0]
            ]
          ],
          [
            [
              [-68.0, 30.0],
              [-68.0, 31.0],
              [-67.0, 31.0],
              [-67.0, 30.0],
              [-68.0, 30.0]
            ]
          ]
        ]
      }
    }
  ]
}
```

### Supported file structures

You can structure your GeoJSON file in either of the following ways.

| File structure | Description |
| --- | --- |
| Multi-feature | Multiple shapes as Feature objects within a single FeatureCollection. This is the most common format, and supports single-line or multi-line formatting. |
| Single-feature | One GeoJSON Feature object per line, also known as newline-delimited JSON (NDJSON). |

> **TIP**: For faster processing, we recommend single-line formatting, including for NDJSON files.

The following NDJSON example shows how to define a Polygon and a MultiPolygon feature in single-feature format, with one Feature object per line.

```
{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[10.0,10.0],[20.0,10.0],[20.0,20.0],[10.0,20.0],[10.0,10.0]]]},"properties":{"name":"Simple polygon"}}
{"type":"Feature","geometry":{"type":"MultiPolygon","coordinates":[[[[30.0,10.0],[40.0,10.0],[40.0,20.0],[30.0,20.0],[30.0,10.0]]],[[[50.0,10.0],[60.0,10.0],[60.0,20.0],[50.0,20.0],[50.0,10.0]]]]},"properties":{"name":"MultiPolygon example"}}
```

### Best practices

Follow these best practices to make sure your GeoJSON file processes without errors:

 Coordinates must be given in `longitude, latitude` order, not `latitude, longitude`.
 Polygon edges must not intersect themselves, except at shared vertices.
 All polygons must be closed: the first and last coordinate pairs must match. This includes polygon shapes placed within other shapes to form rings or holes.
 Holes within a polygon must be fully inside the outer polygon boundary, without overlapping or touching the outer boundary except possibly at a single point.

### Include polygons in reporting

By default, the Geofence Performance Report provides metrics for an entire geofence segment. If you want to compare how individual polygons within a segment perform, you can assign an ID and name to identify them individually in the report to view metrics for each polygon instead of the segment as a whole.

> **IMPORTANT**: You must have access to the Geofence Performance Report to include a shape ID or name with your coordinates. Contact your Technical Account Manager to request access.

Here's what you need to know about assigning IDs and names to your polygons for reporting:

- You can assign a polygon ID using any value, or you can assign the H3 grid cell it falls within.
- The ID and name properties are optional per polygon feature object.
- To exclude a polygon from the report, do not include any names or IDs in the polygon feature `properties` object.

The following sections show how to apply each identification method to a polygon feature.

#### Assign a shape ID and name to a polygon

To identify a polygon by its own shape, include the `polygon_id` and `name` properties. The following example shows a polygon feature identified this way.

```
{
  "type": "Feature",
  "properties": {
    "polygon_id": "SHAPE_ID_PLACEHOLDER",
    "name": "SHAPE_NAME_PLACEHOLDER"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-122.198802243051, 47.6259927781354],
        [-122.198754376278, 47.6258714779866],
        [-122.198551421159, 47.6259514844992],
        [-122.198568653198, 47.6260160057918],
        [-122.198693106808, 47.626012134516],
        [-122.198802243051, 47.6259927781354]
      ]
    ]
  }
}
```

#### Assign an H3 grid cell ID to a polygon

To assign an H3 grid cell a polygon falls within, include the `H3` and `resolution` properties. For details on H3, see the official H3 geo documentation. The following example shows how to assign an H3 grid cell ID to a polygon.

```
{
  "type": "Feature",
  "properties": {
    "H3": "UBER_HEX_GRID_CELL_ID_PLACEHOLDER",
    "resolution": "9"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-118.488674, 34.069353],
        [-118.483674, 34.074353],
        [-118.478674, 34.069353],
        [-118.483674, 34.064353],
        [-118.488674, 34.069353]
      ]
    ]
  }
}
```

To generate the report, you must search for the Geofence Performance Report template and use its report type ID to generate the report. For details, see User-defined reports.

### Response example

A successful response for creating a polygon segment returns the geofence segment ID as the `data.id` value.

```
{
  "data": {
    "customPolygonGeofenceCreate": {
      "data": {
        "name": "GEOFENCE_SEGMENT_NAME_PLACEHOLDER",
        "description": "GEOFENCE_SEGMENT_DESCRIPTION_PLACEHOLDER",
        "id": "cg_9b4e72d1f3a805c6"
      },
      "errors": null
    }
  }
}
```

> **IMPORTANT**: Be sure to take note of the returned `data.id` value. You need this ID to create audience data groups.

## Management tasks

After you create a geofence segment, you can retrieve details about it or update it as needed. The following table lists the relevant operations for each management task.

| Task | Operation |
| --- | --- |
| Check the status of geofence segments. | `advertiser` query |
| Retrieve geofence segments details. | `advertiser` query |
| Update a circle geofence segment. | `customCircularGeofenceUpdate` mutation |
| Update a polygon geofence segment. | `customPolygonGeofenceUpdate` mutation |

### Check the status of geofence segments

To check the progress and status of a geofence segment you created, use the `advertiser.customGeofences` query and include the `status` field.

Here's an `advertiser.customGeofences` query example that shows how to retrieve the status of a geofence.

```
query GeofenceStatusAndType($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    customGeofences(first: 10) {
      nodes {
        id
        name
        status
        type
      }
    }
  }
}
```

The following table lists the possible `status` values and indicates when the platform can target the segment.

| Status value | Description |
| --- | --- |
| `PENDING` | The segment is still being processed by the platform. **NOTE**: You can use this segment for targeting, however, the platform will not serve ads to the area until processing is complete. |
| `READY` | The platform finished processing the geofence segment and it is ready for targeting. |
| `INVALID_POLYGON` | The shape of the polygon is invalid. |
| `TOO_SMALL` | The total area of coverage in the segment is under 31,400 square meters. |
| `TOO_SMALL_IN_SOME_STATES` | The shape size does not meet the minimum requirements of the state. For example, states such as Connecticut, Washington, Nevada, or New York mentioned in the Data policies and restrictions. |
| `PARTIALLY_TOO_SMALL_IN_SOME_STATES` | The segment shape is too small for one of the states it overlaps with. For example, a shape that covers part of the border between Washington and Oregon does not fulfill Washington's minimum 914-meter requirement if the entire shape size is too small. |
| `DELETED` | The segment was deleted. |

### Retrieve geofence segment details

After you create a circle or polygon geofence segment, you can retrieve details about your segment, such as the shape, the file download link, and the geofence segment ID you need to create data groups.

To retrieve a list of geofence segments you created, use the GraphQL `customGeofencesSearch` query and include your advertiser ID.

> **TIP**: To distinguish between segments that are owned by you, a third-party, or The Trade Desk, include the `type` field.

```
query CustomGeofencesSearch($advertiserId: ID!, $searchTerm: String) {
  advertiser(id: $advertiserId) {
    customGeofences(searchTerm: $searchTerm) {
      nodes {
        name
        id
        type
        fileDownloadUrl
        geoTargets {
          nodes {
            latitudeDegrees
            longitudeDegrees
            polygonFileNamePrefix
            radiusInMeters
            geoTargetType
          }
        }
      }
    }
  }
}
```

### Update a circle geofence segment

If needed, you can update and replace the coordinates and radii of all circles in your existing geofence segment.

Here's what you need to know about updating geofence segments:

- If you update the center point coordinates of a segment, you will replace all existing coordinates. Be sure to provide the coordinates you want to keep when you update the segment.
- You can update the center point coordinates and radii using the same methods as creating the segment: by uploading a file or providing the coordinates in the mutation.
- You can set the radius of your circles by doing either of the following:

  - To set the same size for all circles in your segment, include the `radius` field.
  - To set a different size for each circle, include the radius in your coordinates.

To update a circle geofence segment, use the `customCircularGeofenceUpdate` mutation and include the new center point coordinates and radii.

> **IMPORTANT**: If you include a `radius` value and provide coordinates with different radii, you will receive an error.

The following `customCircularGeofenceUpdate` mutation example shows how to apply a new radius to all existing coordinates.

```
mutation {
  customCircularGeofenceUpdate(
    input: {
      id: "GEOFENCE_ID_PLACEHOLDER"
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      radiusUnit: METERS
      radius: 500
    }
  ) {
    data {
      id
      name
      description
    }
    errors {
      __typename
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

Here's a `customCircularGeofenceUpdate` mutation example that shows how to update a segment and set the size of each circle individually.

```
mutation {
  customCircularGeofenceUpdate(
    input: {
      id: "GEOFENCE_ID_PLACEHOLDER"
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      radiusUnit: METERS
      data: { text: ["46.047, 14.522, 50", "-27.111, -52.636, 26"] }
    }
  ) {
    data {
      id
      name
      description
    }
    errors {
      __typename
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

### Update a polygon geofence segment

You can update a polygon geofence segment when you want to replace its shape or change its name.

To update a polygon geofence segment, use the `customPolygonGeofenceUpdate` mutation. To replace the shape, upload a new GeoJSON file and include the returned file ID in the `fileId` field.

The following `customPolygonGeofenceUpdate` mutation example shows how to update the name and replace the shape of a polygon geofence segment.

```
mutation {
  customPolygonGeofenceUpdate(
    input: {
      id: "GEOFENCE_ID_PLACEHOLDER"
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      name: "GEOFENCE_SEGMENT_NAME_PLACEHOLDER"
      fileId: "GEOJSON_FILE_ID_PLACEHOLDER"
    }
  ) {
    data {
      id
      name
    }
    errors {
      __typename
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

## Next steps

After you create your geofence segments, you can add them to your audiences or bid lists. The following table lists the operations for each task and their use cases.

| Use case | Targeting setting | API | Operation or endpoint |
| --- | --- | --- | --- |
| Optimize bids on impressions within the geofence. | Bid list | GraphQL | `bidListCreate` mutation |
| Target users within the geofence. | Audience | REST | POST /v3/datagroup |
| Estimate a device's location from its IP address when raw coordinates aren't available. | IP geolocation | GraphQL | Partner, advertiser, campaign, or ad group create or update mutation |

### Bid list example

To add your segment to a bid list and optimize bids on impressions within the geofence, use the `bidListCreate` mutation and include the following:

 The `HAS_GEOFENCE_THIRD_PARTY_DATA_AND_BRAND` dimension
 The geofence segment ID
 The `ttdgeofence` brand ID

The following `$input` variable example for a `bidListCreate` mutation shows how to add a geofence segment to a bid line and add the bid list to an ad group. For details on how to create bid lists, see Bid lists.

```
{
  "input": {
    "name": "BID_LIST_NAME_PLACEHOLDER",
    "dimensions": [
      "HAS_GEOFENCE_THIRD_PARTY_DATA_AND_BRAND"
    ],
    "adjustmentType": "INCLUSION",
    "bidLines": [
      {
        "bidAdjustment": 0,
        "geofenceThirdPartyDataAndBrand": {
          "brandId": "ttdgeofence",
          "dataId": "GEOFENCE_ID_PLACEHOLDER"
        }
      }
    ],
    "owner": {
      "adGroupId": "AD_GROUP_ID_PLACEHOLDER"
    }
  }
}
```

For details about creating bid lists, see Create and manage bid lists in GraphQL.

### Audience example

To target users within the geofence, add your segment to a data group and add that data group to an audience.

To add your geofence segment to a data group, use the POST /v3/datagroup endpoint. Include the geofence segment ID and the brand ID as a single value separated by a pipe (|) with no spaces around it.

Here's a code snippet of a POST /v3/datagroup request, which shows how to add a geofence segment to a data group.

```
"ThirdPartyDataIds": [
  "GEOFENCE_ID_PLACEHOLDER|ttdgeofence"
]
```

For details about adding data groups to audiences, see Building audiences.

### IP geolocation

When raw device or SSP coordinates aren't available, IP geolocation estimates a device's location from its IP address instead. When you turn on IP geolocation, the platform evaluates impressions in the following order:

1. Raw device or SSP latitude and longitude coordinates
2. IP-resolved location (if raw coordinates are missing)
3. If neither is available, the impression is ineligible

Here's what you need to know about IP geolocation:

- IP geolocation is less precise than raw coordinates. In other words, some impressions might be outside the geofence boundary even when the IP address suggests otherwise.
- IP geolocation affects only geofence bidding eligibility. It does not affect geofence setup or reporting.
- The same data policies and restrictions as raw coordinates apply.

> **TIP**: Use IP geolocation when maximizing reach matters more than ensuring every impression falls within your geofence boundary.

You can turn on IP geolocation at all entity levels (partner, advertiser, campaign, or ad group). To turn on IP geolocation for your geofence segments, set the `isIPResolutionEnabled` value to `true` in any entity create or update mutation.

To turn off IP geolocation, set `isIPResolutionEnabled` to `false`.

The following code snippet is an `input` variable object for a partner, advertiser, campaign or ad group mutation that turns on IP geolocation.

```
{
  "input": {
    "id": "ENTITY_ID_PLACEHOLDER",
    "isIPResolutionEnabled": true
  }
}
```

## FAQs

The following is a list of commonly asked questions about geofence segments.

### Do I have to design a taxonomy for my geofence segments?

No. Each geofence segment is created at the root level and does not have a parent-child relationship.

### How do I update my geofence segment after I create it?

For details on how to update both circle and polygon geofences, see Management tasks.

### How many circles or polygons can I add to a geofence segment?

The Trade Desk recommends limiting each geofence segment to no more than 10,000 circles or shape IDs. Larger segments are possible but may cause processing delays.

### Can other advertisers use a geofence segment that I created?

No. Each geofence segment is unique to the advertiser it was created under.

### How do I assign my geofence segment to a different advertiser?

You cannot assign a geofence segment to a different advertiser. Alternatively, you can create a new segment with the same name and geofence data and assign it to a different advertiser.

### Can I include sensitive locations, like hospitals, in my geofence?

Yes, but bidding is blocked within a 50-meter radius of these locations. See also Data policies and restrictions.

### What is the difference between geofence segments and geo-interest segments?

Geofence segments target areas based on locations that you specify, while geo-interest segments target areas based on interest.

### How do I retrieve the ID of my geofence segment?

Use the `customGeofencesSearch` query and include your advertiser ID. For details, see Retrieve geofence segment details.

### How can I tell how well my geofence boundaries are performing individually?

To identify individual circles on the geofence performance report, include a `ShapeId` and `ShapeName` with the circle coordinates and use the Geofence Performance Report template to create a report. For details on how to create reports, see User-defined Reports.

### Can I include an H3 ID with my polygons?

Yes. To do this, in the GeoJSON file, include the `H3` and `resolution` properties. For details, see Create a polygon geofence segment.

### Can I create multiple circle geofence segments at once?

Yes, but only if you want your circles to have the same size and if you want to create multiple segments with the same coordinates. For details, see Create a circle geofence segment.

### Can I use REST to create a geofence segment?

Yes, but only for circle geofence segments. To access the REST endpoint, contact your Technical Account Manager.

### Why doesn't the update mutation response show the `Selfserve > ` prefix in my segment name?

The update mutations always return the name without the prefix, but the platform still applies the prefix to the stored segment. To retrieve the full name with the prefixes, use the `customGeofencesSearch` query. For details, see Retrieve geofence segment details.

### How do I access the geofence performance report?

Contact your Technical Account Manager, and use the Geofence Performance Report template. For details on how to create reports from templates, see User-defined reports.

### If I want to change the name of a circle segment, do I have to include the prefixes and suffixes of the original name?

No. However, if you do not include the radius suffix in the new name, the system will not automatically attach it. For example, if your segment is named `Selfserve > Geofence Segment A - 26 meters` and you rename it to `Geo Segment B`, the new name will be `Selfserve > Geofence Segment B`.

### Can I target users based on their home location instead of real-time location?

Not for geofence segments. You can, however, create a bid list with geographic segments that targets the home locations of geographic dimensions.

To target or block users based on home location, create a bid list and set the `locationContextType` value to `HOME`.

Here's an `$input` variable example snippet for a `bidListCreate` mutation that shows how to configure the bid list to include users based on their home addresses.

```
{
  "input": {
    "dimensionConfig": {
      "geo": {
        "locationContextType": "HOME"
      }
    }
  }
}
```
