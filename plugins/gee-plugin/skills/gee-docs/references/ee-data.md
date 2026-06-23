# Acesso a dados — ee.data.*

> 42 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.data.authenticateViaOauth`](#ee-data-authenticateviaoauth)
- [`ee.data.authenticateViaPopup`](#ee-data-authenticateviapopup)
- [`ee.data.authenticateViaPrivateKey`](#ee-data-authenticateviaprivatekey)
- [`ee.data.cancelOperation`](#ee-data-canceloperation)
- [`ee.data.computeValue`](#ee-data-computevalue)
- [`ee.data.copyAsset`](#ee-data-copyasset)
- [`ee.data.createAsset`](#ee-data-createasset)
- [`ee.data.createAssetHome`](#ee-data-createassethome)
- [`ee.data.createFolder`](#ee-data-createfolder)
- [`ee.data.deleteAsset`](#ee-data-deleteasset)
- [`ee.data.getAsset`](#ee-data-getasset)
- [`ee.data.getAssetAcl`](#ee-data-getassetacl)
- [`ee.data.getAssetRootQuota`](#ee-data-getassetrootquota)
- [`ee.data.getDownloadId`](#ee-data-getdownloadid)
- [`ee.data.getFeatureViewTilesKey`](#ee-data-getfeatureviewtileskey)
- [`ee.data.getFilmstripThumbId`](#ee-data-getfilmstripthumbid)
- [`ee.data.getMapId`](#ee-data-getmapid)
- [`ee.data.getOperation`](#ee-data-getoperation)
- [`ee.data.getTableDownloadId`](#ee-data-gettabledownloadid)
- [`ee.data.getThumbId`](#ee-data-getthumbid)
- [`ee.data.getTileUrl`](#ee-data-gettileurl)
- [`ee.data.getVideoThumbId`](#ee-data-getvideothumbid)
- [`ee.data.getWorkloadTag`](#ee-data-getworkloadtag)
- [`ee.data.listAssets`](#ee-data-listassets)
- [`ee.data.listBuckets`](#ee-data-listbuckets)
- [`ee.data.listFeatures`](#ee-data-listfeatures)
- [`ee.data.listImages`](#ee-data-listimages)
- [`ee.data.listOperations`](#ee-data-listoperations)
- [`ee.data.makeDownloadUrl`](#ee-data-makedownloadurl)
- [`ee.data.makeTableDownloadUrl`](#ee-data-maketabledownloadurl)
- [`ee.data.makeThumbUrl`](#ee-data-makethumburl)
- [`ee.data.newTaskId`](#ee-data-newtaskid)
- [`ee.data.renameAsset`](#ee-data-renameasset)
- [`ee.data.resetWorkloadTag`](#ee-data-resetworkloadtag)
- [`ee.data.setAssetAcl`](#ee-data-setassetacl)
- [`ee.data.setDefaultWorkloadTag`](#ee-data-setdefaultworkloadtag)
- [`ee.data.setWorkloadTag`](#ee-data-setworkloadtag)
- [`ee.data.startIngestion`](#ee-data-startingestion)
- [`ee.data.startProcessing`](#ee-data-startprocessing)
- [`ee.data.startTableIngestion`](#ee-data-starttableingestion)
- [`ee.data.updateAsset`](#ee-data-updateasset)
- [`ee.data.updateTask`](#ee-data-updatetask)

---

## ee.data.authenticateViaOauth

Configures client-side authentication of EE API calls through the Google APIs Client Library for JavaScript. The library will be loaded automatically if it is not already loaded on the page. The user will be asked to grant the application identified by clientId access to their EE data if they have not done so previously.

This or another authentication method should be called before ee.initialize().

Note that if the user has not previously granted access to the application identified by the client ID, by default this will try to pop up a dialog window prompting the user to grant the required permission. However, this popup can be blocked by the browser. To avoid this, specify the opt_onImmediateFailed callback, and in it render an in-page login button, then call ee.data.authenticateViaPopup() from the click event handler of this button. This stops the browser from blocking the popup, as it is now the direct result of a user action.

The auth token will be refreshed automatically when possible. You can safely assume that all async calls will be sent with the appropriate credentials. For synchronous calls, however, you should check for an auth token with ee.data.getAuthToken() and call ee.data.refreshAuthToken() manually if there is none. The token refresh operation is asynchronous and cannot be performed behind-the-scenes on-demand prior to synchronous calls.

| Usage | Returns |
|---|---|
| `ee.data.authenticateViaOauth(clientId, success, *error*, *extraScopes*, *onImmediateFailed*, *suppressDefaultScopes*)` |   |

| Argument | Type | Details |
|---|---|---|
| `clientId` | String | The application's OAuth client ID, or null to disable authenticated calls. This can be obtained through the Google Developers Console. The project must have a JavaScript origin that corresponds to the domain where the script is running. |
| `success` | Function | The function to call if authentication succeeded. |
| `error` | Function, optional | The function to call if authentication failed, passed the error message. If authentication in immediate (behind-the-scenes) mode fails and opt_onImmediateFailed is specified, that function is called instead of opt_error. |
| `extraScopes` | List\[String\], optional | Extra OAuth scopes to request. |
| `onImmediateFailed` | Function, optional | The function to call if automatic behind-the-scenes authentication fails. Defaults to ee.data.authenticateViaPopup(), bound to the passed callbacks. |
| `suppressDefaultScopes` | Boolean, optional | When true, only scopes specified in opt_extraScopes are requested; the default scopes are not requested unless explicitly specified in opt_extraScopes. |

## ee.data.authenticateViaPopup

Shows a popup asking for the user's permission. Should only be called if ee.data.authenticate() called its opt_onImmediateFailed argument in the past.

May be blocked by pop-up blockers if called outside a user-initiated handler.

| Usage | Returns |
|---|---|
| `ee.data.authenticateViaPopup(*success*, *error*)` |   |

| Argument | Type | Details |
|---|---|---|
| `success` | Function, optional | The function to call if authentication succeeds. |
| `error` | Function, optional | The function to call if authentication fails, passing the error message. |

## ee.data.authenticateViaPrivateKey

Configures server-side authentication of EE API calls through the Google APIs Node.js Client. Private key authentication is strictly for server-side API calls: for browser-based applications, use ee.data.authenticateViaOauth(). No user interaction (e.g. authentication popup) is necessary when using server-side authentication.

This or another authentication method should be called before ee.initialize().

The auth token will be refreshed automatically when possible. You can safely assume that all async calls will be sent with the appropriate credentials. For synchronous calls, however, you should check for an auth token with ee.data.getAuthToken() and call ee.data.refreshAuthToken() manually if there is none. The token refresh operation is asynchronous and cannot be performed behind-the-scenes, on demand, prior to synchronous calls.

| Usage | Returns |
|---|---|
| `ee.data.authenticateViaPrivateKey(privateKey, *success*, *error*, *extraScopes*, *suppressDefaultScopes*)` |   |

| Argument | Type | Details |
|---|---|---|
| `privateKey` | AuthPrivateKey | JSON content of private key. |
| `success` | Function, optional | The function to call if authentication succeeded. |
| `error` | Function, optional | The function to call if authentication failed, passed the error message. |
| `extraScopes` | List\[String\], optional | Extra OAuth scopes to request. |
| `suppressDefaultScopes` | Boolean, optional | When true, only scopes specified in opt_extraScopes are requested; the default scopes are not not requested unless explicitly specified in opt_extraScopes. |

## ee.data.cancelOperation

Cancels the given operation(s).

| Usage | Returns |
|---|---|
| `ee.data.cancelOperation(operationName, *callback*)` |   |

| Argument | Type | Details |
|---|---|---|
| `operationName` | List\[String\]\|String | Operation name(s). |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. The callback is passed an empty object. |

## ee.data.computeValue

Sends a request to compute a value.

Returns result

| Usage | Returns |
|---|---|
| `ee.data.computeValue(obj, *callback*)` | Object\|Value |

| Argument | Type | Details |
|---|---|---|
| `obj` | Object |   |
| `callback` | Function, optional |   |

## ee.data.copyAsset

Copies the asset from sourceId into destinationId.

| Usage | Returns |
|---|---|
| `ee.data.copyAsset(sourceId, destinationId, *overwrite*, *callback*)` |   |

| Argument | Type | Details |
|---|---|---|
| `sourceId` | String | The ID of the asset to copy. |
| `destinationId` | String | The ID of the new asset created by copying. |
| `overwrite` | Boolean, optional | Overwrite any existing destination asset ID. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. The callback is passed an empty object and an error message, if any. |

## ee.data.createAsset

Creates an asset from a JSON value. To create an empty image collection or folder, pass in a "value" object with a "type" key whose value is one of ee.data.AssetType.\* (i.e. "ImageCollection" or "Folder").

Returns a description of the saved asset, including a generated ID, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.createAsset(value, *path*, *force*, *properties*, *callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| `value` | Object | An object describing the asset to create. |
| `path` | String, optional | An optional desired ID, including full path. |
| `force` | Boolean, optional | Force overwrite. |
| `properties` | Object, optional | The keys and values of the properties to set |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.createAssetHome

Attempts to create a home root folder (e.g. "users/joe") for the current user. This results in an error if the user already has a home root folder or the requested ID is unavailable.

| Usage | Returns |
|---|---|
| `ee.data.createAssetHome(requestedId, *callback*)` |   |

| Argument | Type | Details |
|---|---|---|
| `requestedId` | String | The requested ID of the home folder (e.g. "users/joe"). |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.createFolder

Creates an asset folder.

Returns a description of the newly created folder.

| Usage | Returns |
|---|---|
| `ee.data.createFolder(path, *force*, *callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| `path` | String | The path of the folder to create. |
| `force` | Boolean, optional | Force overwrite. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.deleteAsset

Deletes the asset with the given id.

| Usage | Returns |
|---|---|
| `ee.data.deleteAsset(assetId, *callback*)` |   |

| Argument | Type | Details |
|---|---|---|
| `assetId` | String | The ID of the asset to delete. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. The callback is passed an empty object and an error message, if any. |

## ee.data.getAsset

Load info for an asset, given an asset id.

Returns the value call results, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.getAsset(id, *callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| `id` | String | The asset to be retrieved. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getAssetAcl

Returns the access control list of the asset with the given ID.

The authenticated user must be a writer or owner of an asset to see its ACL.

| Usage | Returns |
|---|---|
| `ee.data.getAssetAcl(assetId, *callback*)` | AssetAcl |

| Argument | Type | Details |
|---|---|---|
| `assetId` | String | The ID of the asset to check. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getAssetRootQuota

Returns quota usage details for the asset root with the given ID.

Usage notes:

- The id *must* be a root folder like "users/foo" (not "users/foo/bar").

- The authenticated user must own the asset root to see its quota usage.

| Usage | Returns |
|---|---|
| `ee.data.getAssetRootQuota(rootId, *callback*)` | AssetQuotaDetails |

| Argument | Type | Details |
|---|---|---|
| `rootId` | String | The ID of the asset root to check, e.g. "users/foo". |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getDownloadId

Get a Download ID.

Returns a download id and token, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.getDownloadId(params, *callback*)` | DownloadId |

| Argument | Type | Details |
|---|---|---|
| `params` | Object | An object containing download options with the following possible values: |---| | ` name: ` a base name to use when constructing filenames. Only applicable when format is "ZIPPED_GEO_TIFF" (default), "ZIPPED_GEO_TIFF_PER_BAND", or filePerBand is true. Defaults to the image id (or "download" for computed images) when format is "ZIPPED_GEO_TIFF", "ZIPPED_GEO_TIFF_PER_BAND", or filePerBand is true, otherwise a random character string is generated. Band names are appended when filePerBand is true. | | ` bands: ` a description of the bands to download. Must be an array of band names or an array of dictionaries, each with the following keys (optional parameters apply only when filePerBand is true): - ` id: ` the name of the band, a string, required. - ` crs: ` an optional CRS string defining the band projection. - ` crs_transform: ` an optional array of 6 numbers specifying an affine transform from the specified CRS, in row-major order: \[xScale, xShearing, xTranslation, yShearing, yScale, yTranslation\] - ` dimensions: ` an optional array of two integers defining the width and height to which the band is cropped. - ` scale: ` an optional number, specifying the scale in meters of the band; ignored if crs and crs_transform are specified. | | ` crs: ` a default CRS string to use for any bands that do not explicitly specify one. | | ` crs_transform: ` a default affine transform to use for any bands that do not specify one, of the same format as the `crs_transform` of bands. | | ` dimensions: ` default image cropping dimensions to use for any bands that do not specify them. | | ` scale: ` a default scale to use for any bands that do not specify one; ignored if `crs` and `crs_transform` are specified. | | ` region: ` a polygon specifying a region to download; ignored if `crs` and `crs_transform` is specified. | | ` filePerBand: ` whether to produce a separate GeoTIFF per band (boolean). Defaults to true. If false, a single GeoTIFF is produced and all band-level transformations will be ignored. Note that this is ignored if the format is "ZIPPED_GEO_TIFF" or "ZIPPED_GEO_TIFF_PER_BAND". | | ` format: ` the download format. One of: - "ZIPPED_GEO_TIFF" (GeoTIFF file wrapped in a zip file, default) - "ZIPPED_GEO_TIFF_PER_BAND" (Multiple GeoTIFF files wrapped in a zip file) - "NPY" (NumPy binary format) If "GEO_TIFF" or "NPY", filePerBand and all band-level transformations will be ignored. Loading a NumPy output results in a structured array. | | ` id: ` deprecated, use image parameter. | |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getFeatureViewTilesKey

Get a tiles key for a given map or asset. The tiles key can be passed to an instance of FeatureViewTileSource which can be rendered on a base map outside of the Code Editor.

Returns the call results. Null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.getFeatureViewTilesKey(params, *callback*)` | FeatureViewTilesKey |

| Argument | Type | Details |
|---|---|---|
| `params` | FeatureViewVisualizationParameters | The visualization parameters as a (client-side) JavaScript object. For FeatureView assets: |---| | ` assetId ` (string) The asset ID for which to obtain a tiles key. | | ` visParams ` (Object) The visualization parameters for this layer. | |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getFilmstripThumbId

Get a Filmstrip Thumbnail Id for a given asset.

Returns the thumb ID and optional token, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.getFilmstripThumbId(params, *callback*)` | ThumbnailId |

| Argument | Type | Details |
|---|---|---|
| `params` | FilmstripThumbnailOptions | Parameters to make the request with. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getMapId

Get a Map ID for a given asset

Returns the mapId call results, which may be passed to ee.data.getTileUrl or ui.Map.addLayer. Null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.getMapId(params, *callback*)` | RawMapId |

| Argument | Type | Details |
|---|---|---|
| `params` | ImageVisualizationParameters | The visualization parameters as a (client-side) JavaScript object. For Images and ImageCollections: |---| | ` image ` (JSON string) The image to render. | | ` version ` (number) Version number of image (or latest). | | ` bands ` (comma-separated strings) Comma-delimited list of band names to be mapped to RGB. | | ` min ` (comma-separated numbers) Value (or one per band) to map onto 00. | | ` max ` (comma-separated numbers) Value (or one per band) to map onto FF. | | ` gain ` (comma-separated numbers) Gain (or one per band) to map onto 00-FF. | | ` bias ` (comma-separated numbers) Offset (or one per band) to map onto 00-FF. | | ` gamma ` (comma-separated numbers) Gamma correction factor (or one per band). | | ` palette ` (comma-separated strings) List of CSS-style color strings (single-band previews only). | | ` opacity ` (number) a number between 0 and 1 for opacity. | | ` format ` (string) Either "jpg" or "png". | |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getOperation

Gets information on an operation or list of operations.

See more details on Operations here: https://cloud.google.com/apis/design/design_patterns#long_running_operations

Returns operation status, or a map from operation names to status. Each Operation contains:

- name: operation name in the format projects/X/operations/Y

- done: true when operation has finished running.

- error: may be set when done=true. Contains message and other fields from https://cloud.google.com/tasks/docs/reference/rpc/google.rpc#status

- metadata, which contains

+ state: PENDING, RUNNING, CANCELLING, SUCCEEDED, CANCELLED, or FAILED

+ description: Supplied task description

+ type: EXPORT_IMAGE, EXPORT_FEATURES, etc.

+ create_time: Time the operation was first submitted.

+ update_time: Timestamp of most recent update.

+ start_time: Time the operation started, when so.

+ end_time: Time the operation finished running, when so.

+ attempt: Number of retries of this task, starting at 1.

+ destination_uris: Resources output by this operation.

+ batch_eecu_usage_seconds: CPU used by this operation.

| Usage | Returns |
|---|---|
| `ee.data.getOperation(operationName, *callback*)` | Dictionary\[api.Operation\]\|api.Operation |

| Argument | Type | Details |
|---|---|---|
| `operationName` | List\[String\]\|String | Operation name(s). |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getTableDownloadId

Get a download ID.

Returns a download id and token, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.getTableDownloadId(params, *callback*)` | DownloadId |

| Argument | Type | Details |
|---|---|---|
| `params` | Object | An object containing table download options with the following possible values: |---| | ` table: ` The feature collection to download. | | ` format: ` The download format, CSV, JSON, KML, KMZ or TF_RECORD. | | ` selectors: ` List of strings of selectors that can be used to determine which attributes will be downloaded. | | ` filename: ` The name of the file that will be downloaded. | |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getThumbId

Get a Thumbnail Id for a given asset.

Returns the thumb ID and optional token, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.getThumbId(params, *callback*)` | ThumbnailId |

| Argument | Type | Details |
|---|---|---|
| `params` | ThumbnailOptions | An object containing thumbnail options with the following possible values: |---| | ` image ` (ee.Image) The image to make a thumbnail. | | ` bands ` (array of strings) An array of band names. | | ` format ` (string) The file format ("png", "jpg", "geotiff"). | | ` name ` (string): The base name. | Use ee.Image.getThumbURL for region, dimensions, and visualization options support. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getTileUrl

Generate a URL for map tiles from a Map ID and coordinates. If formatTileUrl is not present, we generate it by using or guessing the urlFormat string, and add urlFormat and formatTileUrl to `id` for future use.

Returns the tile URL.

| Usage | Returns |
|---|---|
| `ee.data.getTileUrl(id, x, y, z)` | String |

| Argument | Type | Details |
|---|---|---|
| `id` | RawMapId | The Map ID to generate tiles for. |
| `x` | Number | The tile x coordinate. |
| `y` | Number | The tile y coordinate. |
| `z` | Number | The tile zoom level. |

## ee.data.getVideoThumbId

Get a Video Thumbnail Id for a given asset.

Returns the thumb ID and optional token, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.getVideoThumbId(params, *callback*)` | ThumbnailId |

| Argument | Type | Details |
|---|---|---|
| `params` | VideoThumbnailOptions | Parameters to make the request with. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.getWorkloadTag

Returns the currently set workload tag.

| Usage | Returns |
|---|---|
| `ee.data.getWorkloadTag()` | String |

**No arguments.**

## ee.data.listAssets

Returns a list of the contents in an asset collection or folder, in an object that includes an \`assets\` array and an optional \`nextPageToken\`.

| Usage | Returns |
|---|---|
| `ee.data.listAssets(parent, *params*, *callback*)` | api.ListAssetsResponse |

| Argument | Type | Details |
|---|---|---|
| `parent` | String | The ID of the collection or folder to list. |
| `params` | api.ProjectsAssetsListAssetsNamedParameters, optional | An object containing optional request parameters with the following possible values: |---| | ` pageSize ` (string) The number of results to return. If not specified, all results are returned. | | ` pageToken ` (string) The token for the page of results to return. | | ` filter ` (string) An additional filter query to apply. Example query: `properties.my_property>=1 AND properties.my_property<2 AND startTime >= "2019-01-01T00:00:00.000Z" AND endTime < "2020-01-01T00:00:00.000Z" AND intersects("{'type':'Point','coordinates':[0,0]}")` See https://google.aip.dev/160 for how to construct a query. | | ` view ` (string) Specifies how much detail is returned in the list. Either "FULL" (default) for all image properties or "BASIC". | |
| `callback` | Function, optional | If not supplied, the call is made synchronously. |

## ee.data.listBuckets

Returns top-level assets and folders for the Cloud Project or user. Leave the project field blank to use the current project.

| Usage | Returns |
|---|---|
| `ee.data.listBuckets(*project*, *callback*)` | api.ListAssetsResponse |

| Argument | Type | Details |
|---|---|---|
| `project` | String, optional | Project to query, e.g. "projects/my-project". Defaults to current project. Use "projects/earthengine-legacy" for user home folders. |
| `callback` | Function, optional | If not supplied, the call is made synchronously. |

## ee.data.listFeatures

List features for a given table asset.

Returns the call results. Null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.listFeatures(asset, params, *callback*)` | api.ListFeaturesResponse |

| Argument | Type | Details |
|---|---|---|
| `asset` | String | The table asset ID to query. |
| `params` | api.ProjectsAssetsListFeaturesNamedParameters | An object containing request parameters with the following possible values: |---| | ` pageSize ` (number): An optional maximum number of results per page, default is 1000. | | ` pageToken ` (string): An optional token identifying a page of results the server should return, usually taken from the response object. | | ` region ` (string): If present, a geometry defining a query region, specified as a GeoJSON geometry string (see RFC 7946). | | ` filter ` (comma-separated strings): If present, specifies additional simple property filters (see https://google.aip.dev/160). | |
| `callback` | Function, optional | An optional callback, called with two parameters: the first is the resulting list of features and the second is an error string on failure. If not supplied, the call is made synchronously. |

## ee.data.listImages

Returns a list of the contents in an image collection, in an object that includes an `images` array and an optional `nextPageToken`.

| Usage | Returns |
|---|---|
| `ee.data.listImages(parent, *params*, *callback*)` | ListImagesResponse |

| Argument | Type | Details |
|---|---|---|
| `parent` | String | The ID of the image collection to list. |
| `params` | Object, optional | An object containing optional request parameters with the following possible values: |---| | ` pageSize ` (string) The number of results to return. If not specified, all results are returned. | | ` pageToken ` (string) The token page of results to return. | | ` startTime ` (ISO 8601 string) The minimum start time (inclusive). | | ` endTime ` (ISO 8601 string) The maximum end time (exclusive). | | ` region ` (GeoJSON or WKT string) A region to filter on. | | ` properties ` (list of strings) A list of property filters to apply, for example: \["classification=urban", "size\>=2"\]. | | ` filter ` (string) An additional filter query to apply. Example query: `properties.my_property>=1 AND properties.my_property<2 AND startTime >= "2019-01-01T00:00:00.000Z" AND endTime < "2020-01-01T00:00:00.000Z" AND intersects("{'type':'Point','coordinates':[0,0]}")` See https://google.aip.dev/160 for how to construct a query. | | ` view ` (string) Specifies how much detail is returned in the list. Either "FULL" (default) for all image properties or "BASIC". | |
| `callback` | Function, optional | If not supplied, the call is made synchronously. |

## ee.data.listOperations

Returns see getOperation for details on the Operation object.

| Usage | Returns |
|---|---|
| `ee.data.listOperations(*limit*, *callback*)` | List\[api.Operation\] |

| Argument | Type | Details |
|---|---|---|
| `limit` | Number, optional | Maximum number of results to return. |
| `callback` | Function, optional |   |

## ee.data.makeDownloadUrl

Create a download URL from a docid and token.

Returns the download URL.

| Usage | Returns |
|---|---|
| `ee.data.makeDownloadUrl(id)` | String |

| Argument | Type | Details |
|---|---|---|
| `id` | DownloadId | A download id and token. |

## ee.data.makeTableDownloadUrl

Create a table download URL from a docid and token.

Returns the download URL.

| Usage | Returns |
|---|---|
| `ee.data.makeTableDownloadUrl(id)` | String |

| Argument | Type | Details |
|---|---|---|
| `id` | DownloadId | A table download id and token. |

## ee.data.makeThumbUrl

Create a thumbnail URL from a thumbid and token.

Returns the thumbnail URL.

| Usage | Returns |
|---|---|
| `ee.data.makeThumbUrl(id)` | String |

| Argument | Type | Details |
|---|---|---|
| `id` | ThumbnailId | A thumbnail ID and token. |

## ee.data.newTaskId

Generates an "unsubmitted" ID for a long-running task.

Before tasks are submitted, they may be assigned IDs to track them. The server ensures that the same ID cannot be reused. These IDs have a UUID format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.

Tasks that are running on the server have a ID without hyphens. This is returned by ee.data.startProcessing and other batch methods.

Returns an array containing generated ID strings, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.newTaskId(*count*, *callback*)` | List\[String\] |

| Argument | Type | Details |
|---|---|---|
| `count` | Number, optional | The number of IDs to generate, one by default. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.renameAsset

Renames the asset from sourceId to destinationId.

| Usage | Returns |
|---|---|
| `ee.data.renameAsset(sourceId, destinationId, *callback*)` |   |

| Argument | Type | Details |
|---|---|---|
| `sourceId` | String | The ID of the asset to rename. |
| `destinationId` | String | The new ID of the asset. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. The callback is passed an empty object and an error message, if any. |

## ee.data.resetWorkloadTag

Resets the tag back to the default. If resetDefault parameter is set to true, the default will be set to empty before resetting.

| Usage | Returns |
|---|---|
| `ee.data.resetWorkloadTag(*resetDefault*)` |   |

| Argument | Type | Details |
|---|---|---|
| `resetDefault` | Boolean, optional |   |

## ee.data.setAssetAcl

Sets the access control list of the asset with the given ID.

The owner ACL cannot be changed, and the final ACL of the asset is constructed by merging the OWNER entries of the old ACL with the incoming ACL record.

The authenticated user must be a writer or owner of an asset to set its ACL.

| Usage | Returns |
|---|---|
| `ee.data.setAssetAcl(assetId, aclUpdate, *callback*)` |   |

| Argument | Type | Details |
|---|---|---|
| `assetId` | String | The ID of the asset to set the ACL on. |
| `aclUpdate` | AssetAclUpdate | The updated ACL. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. The callback is passed an empty object. |

## ee.data.setDefaultWorkloadTag

Sets the workload tag, and as the default for which to reset back to.

For example, calling `ee.data.resetWorkloadTag()` will reset the workload tag back to the default chosen here. To reset the default back to none, pass in an empty string or pass in true to `ee.data.resetWorkloadTag(true)`, like so.

Workload tag must be 1 - 63 characters, beginning and ending with an alphanumeric character (\[a-z0-9A-Z\]) with dashes (-), underscores (_), dots

(.), and alphanumerics between, or an empty string to reset the default back to none.

| Usage | Returns |
|---|---|
| `ee.data.setDefaultWorkloadTag(tag)` |   |

| Argument | Type | Details |
|---|---|---|
| `tag` | String |   |

## ee.data.setWorkloadTag

Sets the workload tag, used to label computation and exports.

Workload tag must be 1 - 63 characters, beginning and ending with an alphanumeric character (\[a-z0-9A-Z\]) with dashes (-), underscores (_), dots

(.), and alphanumerics between, or an empty string to clear the workload tag.

| Usage | Returns |
|---|---|
| `ee.data.setWorkloadTag(tag)` |   |

| Argument | Type | Details |
|---|---|---|
| `tag` | String |   |

## ee.data.startIngestion

Creates an image asset ingestion task.

See ee.data.startProcessing for details on task IDs and response format.

| Usage | Returns |
|---|---|
| `ee.data.startIngestion(taskId, request, *callback*)` | ProcessingResponse |

| Argument | Type | Details |
|---|---|---|
| `taskId` | String | Unsubmitted ID for the task (obtained from newTaskId). |
| `request` | IngestionRequest | The object that describes the ingestion. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.startProcessing

Create processing task that exports or pre-renders an image.

Return value is null if a callback is specified.

Returns an object with fields:

- taskId: Submitted task ID (without hyphens).

- name: Full operation name in the format projects/X/operations/Y

- started: will be 'OK'

- note: may have value 'ALREADY_EXISTS' if an identical task with the same unsubmitted ID already exists.

| Usage | Returns |
|---|---|
| `ee.data.startProcessing(taskId, params, *callback*)` | ProcessingResponse |

| Argument | Type | Details |
|---|---|---|
| `taskId` | String | Unsubmitted ID for the task (obtained from newTaskId). Used to identify duplicated tasks; may be null. The server will create and return a submitted ID. |
| `params` | Object | The object that describes the processing task; only fields that are common for all processing types are documented here. type (string) Either 'EXPORT_IMAGE', 'EXPORT_FEATURES', 'EXPORT_VIDEO' or 'EXPORT_TILES'. json (string) JSON description of the image. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.startTableIngestion

Creates a table asset ingestion task.

See ee.data.startProcessing for details on task IDs and response format.

| Usage | Returns |
|---|---|
| `ee.data.startTableIngestion(taskId, request, *callback*)` | ProcessingResponse |

| Argument | Type | Details |
|---|---|---|
| `taskId` | String | Unsubmitted ID for the task (obtained from newTaskId). |
| `request` | TableIngestionRequest | The object that describes the ingestion. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.updateAsset

Updates an asset.

The authenticated user must be a writer or owner of the asset.

| Usage | Returns |
|---|---|
| `ee.data.updateAsset(assetId, asset, updateFields, *callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| `assetId` | String | The ID of the asset to update. |
| `asset` | api.EarthEngineAsset | The updated version of the asset, containing only the new values of the fields to be updated. Only the "start_time", "end_time", and "properties" fields can be updated. If a value is named in "updateMask", but is unset in "asset", then that value will be deleted from the asset. |
| `updateFields` | List\[String\] | A list of the field names to update. This may contain: "start_time" or "end_time" to update the corresponding timestamp, "properties.PROPERTY_NAME" to update a given property, or "properties" to update all properties. If the list is empty, all properties and both timestamps will be updated. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.data.updateTask

Update one or more tasks' properties. For now, only the following properties may be updated: State (to CANCELLED)

Returns an array of updated tasks, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `ee.data.updateTask(taskId, action, *callback*)` | List\[TaskStatus\] |

| Argument | Type | Details |
|---|---|---|
| `taskId` | List\[String\]\|String | Submitted ID of the task or an array of multiple task IDs. May also contain operation names. |
| `action` | TaskUpdateActions | Action performed on tasks. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

