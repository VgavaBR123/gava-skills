# Exportação e Mapa — Export.*, Map.*

> 38 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`Export.classifier.toAsset`](#export-classifier-toasset)
- [`Export.image.toAsset`](#export-image-toasset)
- [`Export.image.toCloudStorage`](#export-image-tocloudstorage)
- [`Export.image.toDrive`](#export-image-todrive)
- [`Export.map.toCloudStorage`](#export-map-tocloudstorage)
- [`Export.table.toAsset`](#export-table-toasset)
- [`Export.table.toBigQuery`](#export-table-tobigquery)
- [`Export.table.toCloudStorage`](#export-table-tocloudstorage)
- [`Export.table.toDrive`](#export-table-todrive)
- [`Export.table.toFeatureView`](#export-table-tofeatureview)
- [`Export.video.toCloudStorage`](#export-video-tocloudstorage)
- [`Export.video.toDrive`](#export-video-todrive)
- [`Map.add`](#map-add)
- [`Map.addLayer`](#map-addlayer)
- [`Map.centerObject`](#map-centerobject)
- [`Map.clear`](#map-clear)
- [`Map.drawingTools`](#map-drawingtools)
- [`Map.getBounds`](#map-getbounds)
- [`Map.getCenter`](#map-getcenter)
- [`Map.getScale`](#map-getscale)
- [`Map.getZoom`](#map-getzoom)
- [`Map.layers`](#map-layers)
- [`Map.onChangeBounds`](#map-onchangebounds)
- [`Map.onChangeCenter`](#map-onchangecenter)
- [`Map.onChangeZoom`](#map-onchangezoom)
- [`Map.onClick`](#map-onclick)
- [`Map.onIdle`](#map-onidle)
- [`Map.onTileLoaded`](#map-ontileloaded)
- [`Map.remove`](#map-remove)
- [`Map.setCenter`](#map-setcenter)
- [`Map.setControlVisibility`](#map-setcontrolvisibility)
- [`Map.setGestureHandling`](#map-setgesturehandling)
- [`Map.setLocked`](#map-setlocked)
- [`Map.setOptions`](#map-setoptions)
- [`Map.setZoom`](#map-setzoom)
- [`Map.style`](#map-style)
- [`Map.unlisten`](#map-unlisten)
- [`Map.widgets`](#map-widgets)

---

## Export.classifier.toAsset

Creates a batch task to export an ee.Classifier as an Earth Engine asset. Only supported for ee.Classifier.smileRandomForest, ee.Classifier.smileCart, ee.Classifier.DecisionTree and ee.Classifier.DecisionTreeEnsemble.

| Usage | Returns |
|---|---|
| `Export.classifier.toAsset(classifier, *description*, *assetId*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `classifier` | ComputedObject | The classifier to export. |
| `description` | String, optional | A human-readable name of the task. Defaults to "myExportClassifierTask". |
| `assetId` | String, optional | The destination asset ID. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.image.toAsset

Creates a batch task to export an Image as a raster to an Earth Engine asset. Tasks can be started from the Tasks tab.

| Usage | Returns |
|---|---|
| `Export.image.toAsset(image, *description*, *assetId*, *pyramidingPolicy*, *dimensions*, *region*, *scale*, *crs*, *crsTransform*, *maxPixels*, *shardSize*, *priority*, *overwrite*)` |   |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to export. |
| `description` | String, optional | A human-readable name of the task. Defaults to "myExportImageTask". |
| `assetId` | String, optional | The destination asset ID. |
| `pyramidingPolicy` | Object, optional | The pyramiding policy to apply to each band in the image, keyed by band name. Values must be one of: mean, sample, min, max, or mode. Defaults to "mean". A special key, ".default" may be used to change the default for all bands. |
| `dimensions` | Number\|String, optional | The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers. |
| `region` | Geometry.LinearRing\|Geometry.Polygon\|String, optional | A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string. |
| `scale` | Number, optional | Resolution in meters per pixel. Defaults to 1000. |
| `crs` | String, optional | CRS to use for the exported image. |
| `crsTransform` | List\[Number\]\|String, optional | Affine transform to use for the exported image. Requires "crs" to be defined. |
| `maxPixels` | Number, optional | Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit. |
| `shardSize` | Number, optional | Size in pixels of the tiles in which this image will be computed. Defaults to 256. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |
| `overwrite` | Boolean, optional | Whether to overwrite the asset if it already exists. Defaults to false. |

## Export.image.toCloudStorage

Creates a batch task to export an Image as a raster to Google Cloud Storage. Tasks can be started from the Tasks tab.

"crsTransform", "scale", and "dimensions" are mutually exclusive.

| Usage | Returns |
|---|---|
| `Export.image.toCloudStorage(image, *description*, *bucket*, *fileNamePrefix*, *dimensions*, *region*, *scale*, *crs*, *crsTransform*, *maxPixels*, *shardSize*, *fileDimensions*, *skipEmptyTiles*, *fileFormat*, *formatOptions*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to export. |
| `description` | String, optional | A human-readable name of the task. Defaults to "myExportImageTask". |
| `bucket` | String, optional | The Cloud Storage destination bucket. |
| `fileNamePrefix` | String, optional | The string used as the output's prefix. A trailing "/" indicates a path. Defaults to the task's description. |
| `dimensions` | Number\|String, optional | The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers. |
| `region` | Geometry.LinearRing\|Geometry.Polygon\|String, optional | A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string. |
| `scale` | Number, optional | Resolution in meters per pixel. Defaults to 1000. |
| `crs` | String, optional | CRS to use for the exported image. |
| `crsTransform` | List\[Number\]\|String, optional | Affine transform to use for the exported image. Requires "crs" to be defined. |
| `maxPixels` | Number, optional | Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit. |
| `shardSize` | Number, optional | Size in pixels of the tiles in which this image will be computed. Defaults to 256. |
| `fileDimensions` | List\[Number\]\|Number, optional | The dimensions in pixels of each image file, if the image is too large to fit in a single file. May specify a single number to indicate a square shape, or an array of two dimensions to indicate (width,height). Note that the image will still be clipped to the overall image dimensions. Must be a multiple of shardSize. |
| `skipEmptyTiles` | Boolean, optional | If true, skip writing empty (i.e., fully-masked) image tiles. Defaults to false. Only supported on GeoTIFF exports. |
| `fileFormat` | String, optional | The string file format to which the image is exported. Currently only 'GeoTIFF' and 'TFRecord' are supported, defaults to 'GeoTIFF'. |
| `formatOptions` | ImageExportFormatConfig, optional | A dictionary of string keys to format-specific options. For 'GeoTIFF': 'cloudOptimized' (Boolean), 'noData' (float). For 'TFRecord': see https://developers.google.com/earth-engine/guides/tfrecord#formatoptions |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.image.toDrive

Creates a batch task to export an Image as a raster to Drive. Tasks can be started from the Tasks tab. "crsTransform", "scale", and "dimensions" are mutually exclusive.

| Usage | Returns |
|---|---|
| `Export.image.toDrive(image, *description*, *folder*, *fileNamePrefix*, *dimensions*, *region*, *scale*, *crs*, *crsTransform*, *maxPixels*, *shardSize*, *fileDimensions*, *skipEmptyTiles*, *fileFormat*, *formatOptions*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to export. |
| `description` | String, optional | A human-readable name of the task. May contain letters, numbers, -, _ (no spaces). Defaults to "myExportImageTask". |
| `folder` | String, optional | The Google Drive Folder that the export will reside in. Note: (a) if the folder name exists at any level, the output is written to it, (b) if duplicate folder names exist, output is written to the most recently modified folder, (c) if the folder name does not exist, a new folder will be created at the root, and (d) folder names with separators (e.g., 'path/to/file') are interpreted as literal strings, not system paths. Defaults to Drive root. |
| `fileNamePrefix` | String, optional | The filename prefix. May contain letters, numbers, -, _ (no spaces). Defaults to the description. |
| `dimensions` | Number\|String, optional | The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers. |
| `region` | Geometry.LinearRing\|Geometry.Polygon\|String, optional | A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string. |
| `scale` | Number, optional | Resolution in meters per pixel. Defaults to 1000. |
| `crs` | String, optional | CRS to use for the exported image. |
| `crsTransform` | List\[Number\]\|String, optional | Affine transform to use for the exported image. Requires "crs" to be defined. |
| `maxPixels` | Number, optional | Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit. |
| `shardSize` | Number, optional | Size in pixels of the tiles in which this image will be computed. Defaults to 256. |
| `fileDimensions` | List\[Number\]\|Number, optional | The dimensions in pixels of each image file, if the image is too large to fit in a single file. May specify a single number to indicate a square shape, or an array of two dimensions to indicate (width,height). Note that the image will still be clipped to the overall image dimensions. Must be a multiple of shardSize. |
| `skipEmptyTiles` | Boolean, optional | If true, skip writing empty (i.e., fully-masked) image tiles. Defaults to false. Only supported on GeoTIFF exports. |
| `fileFormat` | String, optional | The string file format to which the image is exported. Currently only 'GeoTIFF' and 'TFRecord' are supported, defaults to 'GeoTIFF'. |
| `formatOptions` | ImageExportFormatConfig, optional | A dictionary of string keys to format-specific options. For 'GeoTIFF': 'cloudOptimized' (Boolean), 'noData' (float). For 'TFRecord': see https://developers.google.com/earth-engine/guides/tfrecord#formatoptions |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.map.toCloudStorage

Creates a batch task to export an Image as a rectangular pyramid of map tiles for use with web map viewers. The map tiles will be accompanied by a reference index.html file that displays them using the Google Maps API, and an earth.html file for opening the map on Google Earth.

| Usage | Returns |
|---|---|
| `Export.map.toCloudStorage(image, *description*, *bucket*, *fileFormat*, *path*, *writePublicTiles*, *maxZoom*, *scale*, *minZoom*, *region*, *skipEmptyTiles*, *mapsApiKey*, *bucketCorsUris*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to export as tiles. |
| `description` | String, optional | A human-readable name of the task. Defaults to "myExportMapTask". |
| `bucket` | String, optional | The destination bucket to write to. |
| `fileFormat` | String, optional | The map tiles' file format, one of "auto", "png", or "jpg". Defaults to "auto", which means that opaque tiles will be encoded as "jpg" and tiles with transparency will be encoded as "png". |
| `path` | String, optional | The string used as the output's path. A trailing "/" is optional. Defaults to the task's description. |
| `writePublicTiles` | Boolean, optional | Whether to write public tiles instead of using the bucket's default object ACL. Defaults to true and requires invoker to be OWNER of bucket. |
| `maxZoom` | Number, optional | The maximum zoom level of the map tiles to export. |
| `scale` | Number, optional | The max image resolution in meters per pixel, as an alternative to "maxZoom". The scale will be converted to the most appropriate maximum zoom level at the equator. |
| `minZoom` | Number, optional | The optional minimum zoom level of the map tiles to export. Defaults to zero. |
| `region` | Geometry.LinearRing\|Geometry.Polygon\|String, optional | A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string. Map tiles will be produced in the rectangular region containing this geometry. |
| `skipEmptyTiles` | Boolean, optional | If true, skip writing empty (i.e., fully-transparent) map tiles. Defaults to false. Only supported on GeoTIFF exports. |
| `mapsApiKey` | String, optional | Used in index.html to initialize the Google Maps API. This removes the "development purposes only" message from the map. |
| `bucketCorsUris` | List\[String\], optional | A list of domains (e.g., https://code.earthengine.google.com) that are allowed to retrieve the exported tiles from JavaScript. Setting the tiles to public is not enough to allow them to be accessible by a web page, so you must explicitly give domains access to the bucket. This is known as Cross-Origin-Resource-Sharing, or CORS. You can allow all domains to have access using "\*", but this is generally discouraged. See https://cloud.google.com/storage/docs/cross-origin for more details. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.table.toAsset

Creates a batch task to export a feature collection to an Earth Engine table asset. Tasks can be started from the Tasks tab.

| Usage | Returns |
|---|---|
| `Export.table.toAsset(collection, *description*, *assetId*, *maxVertices*, *priority*, *overwrite*)` |   |

| Argument | Type | Details |
|---|---|---|
| `collection` | FeatureCollection | The feature collection to export. |
| `description` | String, optional | A human-readable name of the task. Defaults to "myExportTableTask". |
| `assetId` | String, optional | The destination asset ID. |
| `maxVertices` | Number, optional | Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |
| `overwrite` | Boolean, optional | Whether to overwrite the asset if it already exists. Defaults to false. |

## Export.table.toBigQuery

Creates a batch task to export a FeatureCollection to BigQuery. Tasks can be started from the Tasks tab.

Note that this feature is in Preview, and the API and behavior may change significantly. For more information, see https://developers.google.com/earth-engine/guides/export_to_bigquery

| Usage | Returns |
|---|---|
| `Export.table.toBigQuery(collection, *description*, *table*, *overwrite*, *append*, *selectors*, *maxVertices*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `collection` | FeatureCollection | The feature collection to export. |
| `description` | String, optional | A human-readable name of the task. Defaults to "myExportTableTask". |
| `table` | String, optional | The fully-qualifed BigQuery destination table in the following format: "project_id.dataset_id.table_id". |
| `overwrite` | Boolean, optional | Whether the existing table should be overwritten by the result of this export. Defaults to false. The \`overwrite\` and \`append\` parameters cannot be \`true\` simultaneously. The export fails if the table already exists and both \`overwrite\` and \`append\` are \`false\`. |
| `append` | Boolean, optional | Whether table data should be appended if the table already exists and has a compatible schema. Defaults to false. The \`overwrite\` and \`append\` parameters cannot be \`true\` simultaneously. The export fails if the table already exists and both \`overwrite\` and \`append\` are \`false\`. |
| `selectors` | List\[String\]\|String, optional | A list of properties to include in the export; either a single string with comma-separated names or a list of strings. |
| `maxVertices` | Number, optional | Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.table.toCloudStorage

Creates a batch task to export a FeatureCollection as a table to Google Cloud Storage. Tasks can be started from the Tasks tab.

| Usage | Returns |
|---|---|
| `Export.table.toCloudStorage(collection, *description*, *bucket*, *fileNamePrefix*, *fileFormat*, *selectors*, *maxVertices*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `collection` | FeatureCollection | The feature collection to export. |
| `description` | String, optional | A human-readable name of the task. Defaults to "myExportTableTask". |
| `bucket` | String, optional | The Cloud Storage destination bucket. |
| `fileNamePrefix` | String, optional | The string used as the output's prefix. A trailing "/" indicates a path. Defaults to the description. |
| `fileFormat` | String, optional | The output format: "CSV" (default), "GeoJSON", "KML", "KMZ", "SHP", or "TFRecord". |
| `selectors` | List\[String\]\|String, optional | A list of properties to include in the export; either a single string with comma-separated names or a list of strings. |
| `maxVertices` | Number, optional | Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.table.toDrive

Creates a batch task to export a FeatureCollection as a table to Drive. Tasks can be started from the Tasks tab.

| Usage | Returns |
|---|---|
| `Export.table.toDrive(collection, *description*, *folder*, *fileNamePrefix*, *fileFormat*, *selectors*, *maxVertices*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `collection` | FeatureCollection | The feature collection to export. |
| `description` | String, optional | A human-readable name of the task. May contain letters, numbers, -, _ (no spaces). Defaults to "myExportTableTask". |
| `folder` | String, optional | The Google Drive Folder that the export will reside in. Note: (a) if the folder name exists at any level, the output is written to it, (b) if duplicate folder names exist, output is written to the most recently modified folder, (c) if the folder name does not exist, a new folder will be created at the root, and (d) folder names with separators (e.g., 'path/to/file') are interpreted as literal strings, not system paths. Defaults to Drive root. |
| `fileNamePrefix` | String, optional | The filename prefix. May contain letters, numbers, -, _ (no spaces). Defaults to the description. |
| `fileFormat` | String, optional | The output format: "CSV" (default), "GeoJSON", "KML", "KMZ", or "SHP", or "TFRecord". |
| `selectors` | List\[String\]\|String, optional | A list of properties to include in the export; either a single string with comma-separated names or a list of strings. |
| `maxVertices` | Number, optional | Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.table.toFeatureView

Creates a batch task to export a FeatureCollection to a FeatureView asset. Tasks can be started from the Tasks tab.

| Usage | Returns |
|---|---|
| `Export.table.toFeatureView(collection, *description*, *assetId*, *maxFeaturesPerTile*, *thinningStrategy*, *thinningRanking*, *zOrderRanking*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `collection` | FeatureCollection | The feature collection to export. |
| `description` | String, optional | A human-readable name of the task. May contain letters, numbers, -, _ (no spaces). Defaults to "myExportTableTask". |
| `assetId` | String, optional | The destination asset ID. May contain letters, numbers, -, _, and / (no spaces). |
| `maxFeaturesPerTile` | Number, optional | The max number of features that can intersect a tile. Can be a value between 0 and 2000; defaults to 500. Warning: Setting the max number of features to a value higher than 1000 may result in dropped tiles. |
| `thinningStrategy` | String, optional | The thinning strategy to use. Can either be HIGHER_DENSITY or GLOBALLY_CONSISTENT. Defaults to HIGHER_DENSITY. When thinning at a particular level of detail on the map, a higher density thinning strategy means that it tries to come as close as possible to the maxFeaturesPerTile limit for each tile. Globally-consistent thinning means that if a feature is removed by thinning, then all other features with equal or worse thinning rank will also be removed. |
| `thinningRanking` | List\[String\]\|String, optional | Comma-separated ranking rules defining the priority of how features should be thinned on the map. Defaults to ".minZoomLevel ASC". Each rule should be defined by a rule type and a direction (ASC or DESC), separated by a space. Valid rule types are: ".geometryType", ".minZoomLevel", or a feature property name. The value ".geometryType" refers to points, lines, and polygons. The value ".minZoomLevel" refers to the minimum zoom level that a feature is visible. Points are visible at all zoom levels, so they have the smallest minZoomLevel. For example, a valid set of ranking rules could be: 'my-property DESC, .geometryType ASC, .minZoomLevel ASC'. The same set of rules expressed as a list of strings would be: \['my-property DESC', '.geometryType ASC', '.minZoomLevel ASC'\]. This means when thinning at a particular level of detail on the map, prioritize features with a larger "my-property" value first (thin features with a smaller value of "my-property"), prioritize features with a smaller geometry type (e.g., thin out polygons before lines and thinning out lines before points), and prioritize features with a smaller minimum zoom level (points over large polygons over smaller polygons). |
| `zOrderRanking` | List\[String\]\|String, optional | Comma-separated ranking rules defining the z-order (stack order) of features displayed on the map. Defaults to ".minZoomLevel ASC". Uses the same format as thinningRanking. Each rule should be defined by a rule type and a direction (ASC or DESC), separated by a space. Valid rule types are: ".geometryType", ".minZoomLevel", or a feature property name. The value ".geometryType" refers to points, lines, and polygons. The value ".minZoomLevel" refers to the minimum zoom level that a feature is visible. Points are visible at all zoom levels, so they have the smallest minZoomLevel. For example, a valid set of ranking rules could be: 'my-property DESC, .geometryType ASC, .minZoomLevel ASC'. The same set of rules expressed as a list of strings would be: \['my-property DESC', '.geometryType ASC', '.minZoomLevel ASC'\]. This means when determining z-order of features at a particular level of detail on the map, features with a larger "my-property" value appear under features with a smaller value, features with a smaller geometry type appear under features with a larger geometry type (e.g., points appear under lines and lines under polygons), and features with a smaller min zoom level (larger features) appear under features with a larger min zoom level (smaller features). |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.video.toCloudStorage

Creates a batch task to export an ImageCollection as a video to Google Cloud Storage. The collection must only contain RGB images. Tasks can be started from the Tasks tab. "crsTransform", "scale", and "dimensions" are mutually exclusive.

| Usage | Returns |
|---|---|
| `Export.video.toCloudStorage(collection, *description*, *bucket*, *fileNamePrefix*, *framesPerSecond*, *dimensions*, *region*, *scale*, *crs*, *crsTransform*, *maxPixels*, *maxFrames*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `collection` | ImageCollection | The image collection to export. |
| `description` | String, optional | A human-readable name of the task. Defaults to "myExportVideoTask". |
| `bucket` | String, optional | The Cloud Storage destination bucket. |
| `fileNamePrefix` | String, optional | The string used as the output's prefix. A trailing "/" indicates a path. Defaults to the description. |
| `framesPerSecond` | Number, optional | The framerate of the exported video. Must be a value between 0.1 and 100. Defaults to 1. |
| `dimensions` | Number\|String, optional | The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers. |
| `region` | Geometry.LinearRing\|Geometry.Polygon\|String, optional | A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string. |
| `scale` | Number, optional | Resolution in meters per pixel. |
| `crs` | String, optional | CRS to use for the exported image. Defaults to the Google Maps Mercator projection, SR-ORG:6627. |
| `crsTransform` | String, optional | Affine transform to use for the exported image. Requires "crs" to be defined. |
| `maxPixels` | Number, optional | Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit. |
| `maxFrames` | Number, optional | Set the maximum number of frames to export. By default, a maximum of 1000 frames may be exported. By setting this explicitly, you may raise or lower this limit. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Export.video.toDrive

Creates a batch task to export an ImageCollection as a video to Drive. The collection must only contain RGB images. Tasks can be started from the Tasks tab. "crsTransform", "scale", and "dimensions" are mutually exclusive.

| Usage | Returns |
|---|---|
| `Export.video.toDrive(collection, *description*, *folder*, *fileNamePrefix*, *framesPerSecond*, *dimensions*, *region*, *scale*, *crs*, *crsTransform*, *maxPixels*, *maxFrames*, *priority*)` |   |

| Argument | Type | Details |
|---|---|---|
| `collection` | ImageCollection | The image collection to export. |
| `description` | String, optional | A human-readable name of the task. May contain letters, numbers, -, _ (no spaces). Defaults to "myExportVideoTask". |
| `folder` | String, optional | The Google Drive Folder that the export will reside in. Note: (a) if the folder name exists at any level, the output is written to it, (b) if duplicate folder names exist, output is written to the most recently modified folder, (c) if the folder name does not exist, a new folder will be created at the root, and (d) folder names with separators (e.g., 'path/to/file') are interpreted as literal strings, not system paths. Defaults to Drive root. |
| `fileNamePrefix` | String, optional | The filename prefix. May contain letters, numbers, -, _ (no spaces). Defaults to the description. |
| `framesPerSecond` | Number, optional | The framerate of the exported video. Must be a value between 0.1 and 100. Defaults to 1. |
| `dimensions` | Number\|String, optional | The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers. |
| `region` | Geometry.LinearRing\|Geometry.Polygon\|String, optional | A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string. |
| `scale` | Number, optional | Resolution in meters per pixel. |
| `crs` | String, optional | CRS to use for the exported image. Defaults to the Google Maps Mercator projection, SR-ORG:6627. |
| `crsTransform` | String, optional | Affine transform to use for the exported image. Requires "crs" to be defined. |
| `maxPixels` | Number, optional | Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit. |
| `maxFrames` | Number, optional | Set the maximum number of frames to export. By default, a maximum of 1000 frames may be exported. By setting this explicitly, you may raise or lower this limit. |
| `priority` | Number, optional | The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100. |

## Map.add

Adds an item to the map. Can also be used to add widgets like ui.Label as well as some non-widget objects like ui.Map.Layer.

Returns the map.

| Usage | Returns |
|---|---|
| `Map.add(item)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| `item` | Object | The item to add. |

## Map.addLayer

Adds a given EE object to the map as a layer.

Returns the new map layer.

| Usage | Returns |
|---|---|
| `Map.addLayer(eeObject, *visParams*, *name*, *shown*, *opacity*)` | ui.Map.Layer |

| Argument | Type | Details |
|---|---|---|
| `eeObject` | Collection\|Feature\|Image\|RawMapId | The object to add to the map. |
| `visParams` | FeatureVisualizationParameters\|ImageVisualizationParameters, optional | The visualization parameters. For Images and ImageCollection, see ee.data.getMapId for valid parameters. For Features and FeatureCollections, the only supported key is "color", as a CSS 3.0 color string or a hex string in "RRGGBB" format. Ignored when eeObject is a map ID. |
| `name` | String, optional | The name of the layer. Defaults to "Layer N". |
| `shown` | Boolean, optional | A flag indicating whether the layer should be on by default. |
| `opacity` | Number, optional | The layer's opacity represented as a number between 0 and 1. Defaults to 1. |

## Map.centerObject

Centers the map view on a given object.

> [!CAUTION]
> **Caution:** providing a large or complex collection as input can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.

Returns the map.

| Usage | Returns |
|---|---|
| `Map.centerObject(object, *zoom*, *onComplete*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| `object` | Element\|Geometry | An object to center on - a geometry, image or feature. |
| `zoom` | Number, optional | The zoom level, from 0 to 24. If unspecified, computed based on the object's bounding box. |
| `onComplete` | Function, optional | A callback which is triggered after the recentering completes successfully. Passing this parameter causes the \`centerObject\` operation to run asynchronously. |

## Map.clear

Clears the map by removing all layers, listeners, and widgets and restoring the options to their defaults.

Returns the map.

| Usage | Returns |
|---|---|
| `Map.clear()` | ui.Map |

**No arguments.**

## Map.drawingTools

Returns the Map's drawing tools, which can be used to create and edit shapes on the map.

| Usage | Returns |
|---|---|
| `Map.drawingTools()` | ui.Map.DrawingTools |

**No arguments.**

## Map.getBounds

Returns the bounds of the current map view, as a list in the format \[west, south, east, north\] in degrees.

| Usage | Returns |
|---|---|
| `Map.getBounds(*asGeoJSON*)` | GeoJSONGeometry\|List\[Number\]\|String |

| Argument | Type | Details |
|---|---|---|
| `asGeoJSON` | Boolean, optional | If true, returns map bounds as GeoJSON. |

## Map.getCenter

Returns the coordinates at the center of the map.

| Usage | Returns |
|---|---|
| `Map.getCenter()` | Geometry.Point |

**No arguments.**

## Map.getScale

Returns the approximate pixel scale of the current map view, in meters.

| Usage | Returns |
|---|---|
| `Map.getScale()` | Number\|String |

**No arguments.**

## Map.getZoom

Returns the current zoom level of the map.

| Usage | Returns |
|---|---|
| `Map.getZoom()` | Number |

**No arguments.**

## Map.layers

Returns the list of layers associated with the default map.

| Usage | Returns |
|---|---|
| `Map.layers()` | ui.data.ActiveList\[ui.Map.AbstractLayer\] |

**No arguments.**

## Map.onChangeBounds

Registers a callback that's fired when the map bounds change. This is fired during pan, zoom, and when the map's bounds are changed programmatically. Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onChangeBounds(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| `callback` | Function | The callback to fire when the map bounds change. The callback is passed two parameters: an object containing the coordinates of the new map center (with keys lon, lat, and zoom) and the map widget itself. |

## Map.onChangeCenter

Registers a callback that's fired when the map center changes. This is fired during pan or when the map's center is changed programmatically.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onChangeCenter(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| `callback` | Function | The callback to fire when the map center changes. The callback is passed two parameters: an object containing the coordinates of the new center (with keys lon and lat) and the map widget itself. |

## Map.onChangeZoom

Registers a callback that's fired when the map zoom level changes.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onChangeZoom(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| `callback` | Function | The callback to fire when the map zoom change. The callback is passed two parameters: the new zoom level and the map widget itself. |

## Map.onClick

Registers a callback that's fired when the map is clicked.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onClick(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| `callback` | Function | The callback to fire when the map is clicked. The callback is passed an object containing the coordinates of the clicked point (with keys lon and lat) and the map widget. |

## Map.onIdle

Registers a callback that's fired when the map stops moving.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onIdle(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| `callback` | Function | The callback to fire when the map becomes idle. The callback is passed two parameters: an object containing the coordinates of the map center (with keys lon, lat, and zoom) and the map widget itself. |

## Map.onTileLoaded

Registers a callback that's fired when a map tile has been loaded.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onTileLoaded(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| `callback` | Function | Called with an array of per layer values. Each value is the fraction of tiles still pending: a value of 0 means there are no more tiles to load for the layer. |

## Map.remove

Removes the given item from the map, if it exists.

Returns the removed item or null if it hadn't been added to the map.

| Usage | Returns |
|---|---|
| `Map.remove(item)` | Object |

| Argument | Type | Details |
|---|---|---|
| `item` | Object | The item to remove. |

## Map.setCenter

Centers the map view at a given coordinates with the given zoom level.

Returns the map.

| Usage | Returns |
|---|---|
| `Map.setCenter(lon, lat, *zoom*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| `lon` | Number | The longitude of the center, in degrees. |
| `lat` | Number | The latitude of the center, in degrees. |
| `zoom` | Number, optional | The zoom level, from 0 to 24. |

## Map.setControlVisibility

Sets the visibility of the controls on the map.

Returns this ui.Map.

| Usage | Returns |
|---|---|
| `Map.setControlVisibility(*all*, *layerList*, *zoomControl*, *scaleControl*, *mapTypeControl*, *fullscreenControl*, *drawingToolsControl*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| `all` | Boolean, optional | Whether to show all controls. False hides all controls; true shows all controls. Overridden by individually set parameters. Note that setting this explicitly will affect any additional controls added in the future. |
| `layerList` | Boolean, optional | When false, hides the layer list panel or, when true, allows the layer list panel's visibility to be determined by the presence of layers in the list. The default is to show the list. |
| `zoomControl` | Boolean, optional | Whether the zoom control is visible. Defaults to true. |
| `scaleControl` | Boolean, optional | Whether to show the control which indicates the scale at the map's current zoom level. Defaults to true. |
| `mapTypeControl` | Boolean, optional | Whether to show the control that allows the user to change the base map. Defaults to true. |
| `fullscreenControl` | Boolean, optional | Whether to show the control that allows the user to make the map full-screen. Defaults to true. |
| `drawingToolsControl` | Boolean, optional | Whether to show the control that allows the user to add or edit the geometry drawing tools. Defaults to true. |

## Map.setGestureHandling

Controls how gestures are handled on the map.

See https://developers.google.com/maps/documentation/javascript/reference/map#MapOptions.gestureHandling.

| Usage | Returns |
|---|---|
| `Map.setGestureHandling(option)` |   |

| Argument | Type | Details |
|---|---|---|
| `option` | String | The option that controls how gestures are handled on the map. Allowed values: - "cooperative": Scroll events and one-finger touch gestures scroll the page, and do not zoom or pan the map. Two-finger touch gestures pan and zoom the map. Scroll events with a ctrl key or ⌘ key pressed zoom the map. In this mode the map cooperates with the page. - "greedy": All touch gestures and scroll events pan or zoom the map. - "none": The map cannot be panned or zoomed by user gestures. - "auto": (default) Gesture handling is either cooperative or greedy, depending on whether the page is scrollable or in an iframe. |

## Map.setLocked

Limits panning and zooming on the map.

- To lock both panning and zooming, set locked to true and nothing else.

- To allow panning and limit the min and max zoom, set locked to false and supply the minZoom and maxZoom parameters.

- To disallow panning and limit min and max zoom, set locked to true and supply the minZoom and maxZoom parameters.

- To reset the map to default, set locked to false and nothing else.

| Usage | Returns |
|---|---|
| `Map.setLocked(locked, *minZoom*, *maxZoom*)` |   |

| Argument | Type | Details |
|---|---|---|
| `locked` | Boolean | Whether the map should be locked or not. |
| `minZoom` | Number, optional | (optional) The minimum zoom for the map, between 0 and 24, inclusive. |
| `maxZoom` | Number, optional | (optional) The maximum zoom for the map, between 0 and 24, inclusive. |

## Map.setOptions

Modifies the Google Maps basemap. Allows for:

1) Setting the current MapType. 2) Providing custom styles for the basemap (MapTypeStyles). 3) Setting the list of available mapTypesIds for the basemap.

If called with no parameters, resets the map type to the google default.

Returns the map.

| Usage | Returns |
|---|---|
| `Map.setOptions(*mapTypeId*, *styles*, *types*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| `mapTypeId` | String, optional | A mapTypeId to set the basemap to. Can be one of "ROADMAP", "SATELLITE", "HYBRID" or "TERRAIN" to select one of the standard Google Maps API map types, or one of the keys specified in the opt_styles dictionary. If left as null and only 1 style is specified in opt_styles, that style will be used. |
| `styles` | Object, optional | A dictionary of custom MapTypeStyle objects keyed with a name that will appear in the map's Map Type Controls. See: https://developers.google.com/maps/documentation/javascript/reference#MapTypeStyle |
| `types` | List\[String\], optional | A list of mapTypeIds to make available. If omitted, but opt_styles is specified, appends all of the style keys to the standard Google Maps API map types. |

## Map.setZoom

Sets the zoom level of the map.

Returns this ui.Map.

| Usage | Returns |
|---|---|
| `Map.setZoom(zoom)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| `zoom` | Number | The zoom level, from 0 to 24, to set for the map. |

## Map.style

Returns the Map's style ActiveDictionary, which can be modified to update the Map's styles.

In addition to the standard UI API styles listed in the ui.Panel.style() documentation, the Map supports the following custom style option:

- cursor, which can be 'crosshair' or 'hand' (default)

| Usage | Returns |
|---|---|
| `Map.style()` | ui.data.ActiveDictionary |

**No arguments.**

## Map.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Map.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| `idOrType` | String, optional | Either an ID returned by listen() when a callback was registered, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks registered with that event type are deleted. If nothing is passed, all callbacks are deleted. |

## Map.widgets

Returns the list of the widgets currently on the map.

| Usage | Returns |
|---|---|
| `Map.widgets()` | ui.data.ActiveList\[ui.Widget\] |

**No arguments.**

