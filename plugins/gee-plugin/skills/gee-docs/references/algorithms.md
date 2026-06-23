# Algoritmos — ee.Algorithms.*

> 35 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.Algorithms.CannyEdgeDetector`](#ee-algorithms-cannyedgedetector)
- [`ee.Algorithms.Collection`](#ee-algorithms-collection)
- [`ee.Algorithms.CrossCorrelation`](#ee-algorithms-crosscorrelation)
- [`ee.Algorithms.Date`](#ee-algorithms-date)
- [`ee.Algorithms.Describe`](#ee-algorithms-describe)
- [`ee.Algorithms.Dictionary`](#ee-algorithms-dictionary)
- [`ee.Algorithms.FMask.fillMinima`](#ee-algorithms-fmask-fillminima)
- [`ee.Algorithms.FMask.matchClouds`](#ee-algorithms-fmask-matchclouds)
- [`ee.Algorithms.Feature`](#ee-algorithms-feature)
- [`ee.Algorithms.HillShadow`](#ee-algorithms-hillshadow)
- [`ee.Algorithms.HoughTransform`](#ee-algorithms-houghtransform)
- [`ee.Algorithms.If`](#ee-algorithms-if)
- [`ee.Algorithms.Image.Segmentation.GMeans`](#ee-algorithms-image-segmentation-gmeans)
- [`ee.Algorithms.Image.Segmentation.KMeans`](#ee-algorithms-image-segmentation-kmeans)
- [`ee.Algorithms.Image.Segmentation.SNIC`](#ee-algorithms-image-segmentation-snic)
- [`ee.Algorithms.Image.Segmentation.seedGrid`](#ee-algorithms-image-segmentation-seedgrid)
- [`ee.Algorithms.IsEqual`](#ee-algorithms-isequal)
- [`ee.Algorithms.Landsat.TOA`](#ee-algorithms-landsat-toa)
- [`ee.Algorithms.Landsat.calibratedRadiance`](#ee-algorithms-landsat-calibratedradiance)
- [`ee.Algorithms.Landsat.pathRowLimit`](#ee-algorithms-landsat-pathrowlimit)
- [`ee.Algorithms.Landsat.simpleCloudScore`](#ee-algorithms-landsat-simplecloudscore)
- [`ee.Algorithms.Landsat.simpleComposite`](#ee-algorithms-landsat-simplecomposite)
- [`ee.Algorithms.ObjectType`](#ee-algorithms-objecttype)
- [`ee.Algorithms.ProjectionTransform`](#ee-algorithms-projectiontransform)
- [`ee.Algorithms.Sentinel2.CDI`](#ee-algorithms-sentinel2-cdi)
- [`ee.Algorithms.String`](#ee-algorithms-string)
- [`ee.Algorithms.TemporalSegmentation.C2c`](#ee-algorithms-temporalsegmentation-c2c)
- [`ee.Algorithms.TemporalSegmentation.Ccdc`](#ee-algorithms-temporalsegmentation-ccdc)
- [`ee.Algorithms.TemporalSegmentation.Ewmacd`](#ee-algorithms-temporalsegmentation-ewmacd)
- [`ee.Algorithms.TemporalSegmentation.LandTrendr`](#ee-algorithms-temporalsegmentation-landtrendr)
- [`ee.Algorithms.TemporalSegmentation.LandTrendrFit`](#ee-algorithms-temporalsegmentation-landtrendrfit)
- [`ee.Algorithms.TemporalSegmentation.StructuralChangeBreakpoints`](#ee-algorithms-temporalsegmentation-structuralchangebreakpoints)
- [`ee.Algorithms.TemporalSegmentation.VCT`](#ee-algorithms-temporalsegmentation-vct)
- [`ee.Algorithms.TemporalSegmentation.Verdet`](#ee-algorithms-temporalsegmentation-verdet)
- [`ee.Algorithms.Terrain`](#ee-algorithms-terrain)

---

## ee.Algorithms.CannyEdgeDetector

Applies the Canny edge detection algorithm to an image. The output is an image whose bands have the same names as the input bands, and in which non-zero values indicate edges, and the magnitude of the value is the gradient magnitude.

| Usage | Returns |
|---|---|
| `ee.Algorithms.CannyEdgeDetector(image, threshold, *sigma*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image on which to apply edge detection. |
| `threshold` | Float | Threshold value. The pixel is only considered for edge detection if the gradient magnitude is higher than this threshold. |
| `sigma` | Float, default: 1 | Sigma value for a gaussian filter applied before edge detection. 0 means apply no filtering. |

## ee.Algorithms.Collection

Returns a Collection containing the specified features.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Collection(features)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| `features` | List | The features comprising the collection. |

## ee.Algorithms.CrossCorrelation

Gives information on the quality of image registration between two (theoretically) co-registered images. The input is two images with the same number of bands. This function outputs an image composed of four bands of information. The first three are distances: the deltaX, deltaY, and the Euclidean distance for each pixel in imageA to the pixel which has the highest corresponding correlation coefficient in imageB. The fourth band is the value of the correlation coefficient for that pixel \[-1 : +1\].

| Usage | Returns |
|---|---|
| `ee.Algorithms.CrossCorrelation(imageA, imageB, maxGap, windowSize, *maxMaskedFrac*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `imageA` | Image | First image, with N bands. |
| `imageB` | Image | Second image, must have the same number of bands as imageA. |
| `maxGap` | Integer | The greatest distance a pixel may shift in either X or Y. |
| `windowSize` | Integer | Size of the window to be compared. |
| `maxMaskedFrac` | Float, default: 0 | The maximum fraction of pixels within the correlation window that are allowed to be masked. This test is applied at each offset location within the search region. For each offset, the overlapping image patches are compared and a correlation score computed. A pixel within these overlapping patches is considered masked if either of the patches is masked there. If the test fails at any single location in the search region, the output pixel for which the correlation is being computed is considered invalid, and will be masked. |

## ee.Algorithms.Date

Creates a Date.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Date(value, *timeZone*)` | Date |

| Argument | Type | Details |
|---|---|---|
| `value` | Object | A number (interpreted as milliseconds since 1970-01-01T00:00:00Z), or string such as '1996-01-01' or '1996-001' or '1996-01-01T08:00'. |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Algorithms.Describe

Describes an object using a simple JSON-compatible structure.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Describe(input)` | Object |

| Argument | Type | Details |
|---|---|---|
| `input` | Object | The object to describe. |

## ee.Algorithms.Dictionary

Constructs a dictionary.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Dictionary(*input*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| `input` | Object, default: null | An object to convert to a dictionary. Either a JSON dictionary or a list of alternating key/value pairs. Keys must be strings. |

## ee.Algorithms.FMask.fillMinima

Fills local minima. Only works on INT types.

| Usage | Returns |
|---|---|
| `ee.Algorithms.FMask.fillMinima(image, *borderValue*, *neighborhood*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to fill. |
| `borderValue` | Long, default: null | The border value. |
| `neighborhood` | Integer, default: 50 | The size of the neighborhood to compute over. |

## ee.Algorithms.FMask.matchClouds

Runs the FMask cloud and shadow matching. Outputs a single band ('csm'), containing the computed cloud and shadow masks.

| Usage | Returns |
|---|---|
| `ee.Algorithms.FMask.matchClouds(input, cloud, shadow, btemp, sceneLow, sceneHigh, *neighborhood*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `input` | Image | The scene for which to compute cloud and shadow masks. |
| `cloud` | Image | Potential cloud mask image. Expected to contain 1s for cloudy pixels and masked pixels everywhere else. |
| `shadow` | Image | Potential shadow mask image. Expected to contain 1s for shadow pixels and masked pixels everywhere else. |
| `btemp` | Image | Brightness temperature image, in Celsius. |
| `sceneLow` | Float | The 0.175 percentile brightness temperature of the scene. |
| `sceneHigh` | Float | The 0.825 percentile brightness temperature of the scene. |
| `neighborhood` | Integer, default: 50 | The neighborhood to pad around each tile. |

## ee.Algorithms.Feature

Returns a Feature composed of the given geometry and metadata.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Feature(*geometry*, *metadata*, *geometryKey*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| `geometry` | Geometry, default: null | The geometry of the feature. |
| `metadata` | Dictionary, default: {} | The properties of the feature. |
| `geometryKey` | String, default: null | Obsolete; has no effect. |

## ee.Algorithms.HillShadow

Creates a shadow band, with output 1 where pixels are illuminated and 0 where they are shadowed.

Takes as input an elevation band, azimuth and zenith of the light source in degrees, a neighborhood size, and whether or not to apply hysteresis when a shadow appears. Currently, this algorithm only works for Mercator projections, in which light rays are parallel.

| Usage | Returns |
|---|---|
| `ee.Algorithms.HillShadow(image, azimuth, zenith, *neighborhoodSize*, *hysteresis*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to which to apply the shadow algorithm, in which each pixel should represent an elevation in meters. |
| `azimuth` | Float | Azimuth in degrees. |
| `zenith` | Float | Zenith in degrees. |
| `neighborhoodSize` | Integer, default: 0 | Neighborhood size. |
| `hysteresis` | Boolean, default: false | Use hysteresis. Less physically accurate, but may generate better images. |

## ee.Algorithms.HoughTransform

Applies the Hough transform to an image. For every input band, outputs a band where lines are detected by thresholding the Hough transform with a value of lineThreshold.

The output band is named \[input\]_lines, where \[input\] is the name of the original band. The defaults provided for the parameters are intended as a starting point for use with UINT8 images.

| Usage | Returns |
|---|---|
| `ee.Algorithms.HoughTransform(image, *gridSize*, *inputThreshold*, *lineThreshold*, *smooth*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to which to apply the transform. |
| `gridSize` | Integer, default: 256 | The size of the grid over which to perform the computation. |
| `inputThreshold` | Float, default: 64 | Value threshold for input image. Pixels equal to or above this value are considered active. |
| `lineThreshold` | Float, default: 72 | Threshold for line detection. Values equal to or above this threshold on the Hough transform are considered to be detected lines. |
| `smooth` | Boolean, default: true | Whether to smooth the Hough transform before line detection. |

## ee.Algorithms.If

Selects one of its inputs based on a condition, similar to an if-then-else construct.

| Usage | Returns |
|---|---|
| `ee.Algorithms.If(*condition*, *trueCase*, *falseCase*)` | Object |

| Argument | Type | Details |
|---|---|---|
| `condition` | Object, default: null | The condition that determines which result is returned. If this is not a boolean, it is interpreted as a boolean by the following rules: <br /> - Numbers that are equal to 0 or a NaN are false. - Empty strings, lists and dictionaries are false. - Null is false. - Everything else is true. |
| `trueCase` | Object, default: null | The result to return if the condition is true. |
| `falseCase` | Object, default: null | The result to return if the condition is false. |

## ee.Algorithms.Image.Segmentation.GMeans

Performs G-Means clustering on the input image. Iteratively applies k-means followed by a normality test to automatically determine the number of clusters to use. The output contains a 'clusters' band containing the integer ID of the cluster that each pixel belongs to.

The algorithm can work either on a fixed grid of non-overlapping cells (gridSize, which can be smaller than a tile) or on tiles with overlap (neighborhoodSize). The default is to use tiles with no overlap. Clusters in one cell or tile are unrelated to clusters in another. Any cluster that spans a cell or tile boundary may receive two different labels in the two halves. Any input pixels with partial masks are fully masked in the output. This algorithm is only expected to perform well for images with a narrow dynamic range (i.e., bytes or shorts).

See: G. Hamerly and C. Elkan. 'Learning the k in k-means'. NIPS, 2003.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Image.Segmentation.GMeans(image, *numIterations*, *pValue*, *neighborhoodSize*, *gridSize*, *uniqueLabels*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The input image for clustering. |
| `numIterations` | Integer, default: 10 | Number of iterations. Default 10. |
| `pValue` | Float, default: 50 | Significance level for normality test. |
| `neighborhoodSize` | Integer, default: 0 | Neighborhood size. The amount to extend each tile (overlap) when computing the clusters. This option is mutually exclusive with gridSize. |
| `gridSize` | Integer, default: null | Grid cell-size. If greater than 0, kMeans will be run independently on cells of this size. This has the effect of limiting the size of any cluster to be gridSize or smaller. This option is mutually exclusive with neighborhoodSize. |
| `uniqueLabels` | Boolean, default: true | If true, clusters are assigned unique IDs. Otherwise, they repeat per tile or grid cell. |

## ee.Algorithms.Image.Segmentation.KMeans

Performs K-Means clustering on the input image. Outputs a 1-band image containing the ID of the cluster that each pixel belongs to. The algorithm can work either on a fixed grid of non-overlapping cells (gridSize, which can be smaller than a tile) or on tiles with overlap (neighborhoodSize). The default is to use tiles with no overlap.

Clusters in one cell or tile are unrelated to clusters in another. Any cluster that spans a cell or tile boundary may receive two different labels in the two halves. Any input pixels with partial masks are fully masked in the output.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Image.Segmentation.KMeans(image, *numClusters*, *numIterations*, *neighborhoodSize*, *gridSize*, *forceConvergence*, *uniqueLabels*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The input image for clustering. |
| `numClusters` | Integer, default: 8 | Number of clusters. |
| `numIterations` | Integer, default: 20 | Number of iterations. |
| `neighborhoodSize` | Integer, default: 0 | Neighborhood size. The amount to extend each tile (overlap) when computing the clusters. This option is mutually exclusive with gridSize. |
| `gridSize` | Integer, default: null | Grid cell-size. If greater than 0, kMeans will be run independently on cells of this size. This has the effect of limiting the size of any cluster to be gridSize or smaller. This option is mutually exclusive with neighborhoodSize. |
| `forceConvergence` | Boolean, default: false | If true, an error is thrown if convergence is not achieved before numIterations. |
| `uniqueLabels` | Boolean, default: true | If true, clusters are assigned unique IDs. Otherwise, they repeat per tile or grid cell. |

## ee.Algorithms.Image.Segmentation.SNIC

Superpixel clustering based on SNIC (Simple Non-Iterative Clustering). Outputs a band of cluster IDs and the per-cluster averages for each of the input bands. If the 'seeds' image isn't provided as input, the output will include a 'seeds' band containing the generated seed locations.

See: Achanta, Radhakrishna and Susstrunk, Sabine, 'Superpixels and Polygons using Simple Non-Iterative Clustering', CVPR, 2017.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Image.Segmentation.SNIC(image, *size*, *compactness*, *connectivity*, *neighborhoodSize*, *seeds*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The input image for clustering. |
| `size` | Integer, default: 5 | The superpixel seed location spacing, in pixels. If 'seeds' image is provided, no grid is produced. |
| `compactness` | Float, default: 1 | Compactness factor. Larger values cause clusters to be more compact (square). Setting this to 0 disables spatial distance weighting. |
| `connectivity` | Integer, default: 8 | Connectivity. Either 4 or 8. |
| `neighborhoodSize` | Integer, default: null | Tile neighborhood size (to avoid tile boundary artifacts). Defaults to 2 \* size. |
| `seeds` | Image, default: null | If provided, any non-zero valued pixels are used as seed locations. Pixels that touch (as specified by 'connectivity') are considered to belong to the same cluster. |

## ee.Algorithms.Image.Segmentation.seedGrid

Selects seed pixels for clustering.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Image.Segmentation.seedGrid(*size*, *gridType*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `size` | Integer, default: 5 | The superpixel seed location spacing, in pixels. |
| `gridType` | String, default: "square" | Type of grid. One of 'square' or 'hex'. |

## ee.Algorithms.IsEqual

Returns whether two objects are equal.

| Usage | Returns |
|---|---|
| `ee.Algorithms.IsEqual(*left*, *right*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| `left` | Object, default: null |   |
| `right` | Object, default: null |   |

## ee.Algorithms.Landsat.TOA

Calibrates Landsat DN to TOA reflectance and brightness temperature for Landsat and similar data. For recently-acquired scenes calibration coefficients are extracted from the image metadata; for older scenes the coefficients are derived from:

Chander, Gyanesh, Brian L. Markham, and Dennis L. Helder. "Summary of current radiometric calibration coefficients for Landsat MSS, TM, ETM+, and EO-1 ALI sensors." Remote sensing of environment 113.5 (2009): 893-903.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Landsat.TOA(input)` | Image |

| Argument | Type | Details |
|---|---|---|
| `input` | Image | The Landsat image to process. |

## ee.Algorithms.Landsat.calibratedRadiance

Calibrates each band of an image by applying linear transformation with slope `RADIANCE_MULT_BAND_N` and y-intercept `RADIANCE_ADD_BAND_N`; these values are extracted from the image metadata.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Landsat.calibratedRadiance(image)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The input Landsat image. |

## ee.Algorithms.Landsat.pathRowLimit

Limits requests to an ImageCollection of Landsat scenes to return a controllable number of the best scenes for each request. This is intended for use with statistical algorithms like median composites that need a certain amount of good data to perform well, but that do not benefit substantially from additional data beyond that while becoming needlessly expensive. The default arguments select approximately one year's worth of good data.

Note that in rare circumstances, when the tile boundary aligns with a Landsat WRS cell boundary, queries for adjacent tiles may yield conflicting results. This is why it is important that this algorithm only be used with statistical methods that can tolerate these inconsistencies.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Landsat.pathRowLimit(collection, *maxScenesPerPathRow*, *maxScenesTotal*)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| `collection` | ImageCollection | The Landsat ImageCollection to limit. |
| `maxScenesPerPathRow` | Integer, default: 25 | The max number of scenes to return per path/row. |
| `maxScenesTotal` | Integer, default: 100 | The max number of scenes to return per request total. |

## ee.Algorithms.Landsat.simpleCloudScore

Computes a simple cloud-likelihood score in the range \[0,100\] using a combination of brightness, temperature, and NDSI. This is not a robust cloud detector, and is intended mainly to compare multiple looks at the same point for *relative* cloud likelihood.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Landsat.simpleCloudScore(image)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The Landsat TOA image to process. |

## ee.Algorithms.Landsat.simpleComposite

Computes a Landsat TOA composite from a collection of raw Landsat scenes. It applies standard TOA calibration and then assigns a cloud score to each pixel using the SimpleLandsatCloudScore algorithm. It selects the lowest possible range of cloud scores at each point and then computes per-band percentile values from the accepted pixels. This algorithm also uses the LandsatPathRowLimit algorithm to select only the least-cloudy scenes in regions where more than maxDepth input scenes are available.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Landsat.simpleComposite(collection, *percentile*, *cloudScoreRange*, *maxDepth*, *asFloat*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `collection` | ImageCollection | The raw Landsat ImageCollection to composite. |
| `percentile` | Integer, default: 50 | The percentile value to use when compositing each band. |
| `cloudScoreRange` | Integer, default: 10 | The size of the range of cloud scores to accept per pixel. |
| `maxDepth` | Integer, default: 40 | An approximate limit on the maximum number of scenes used to compute each pixel. |
| `asFloat` | Boolean, default: false | If true, output bands are in the same units as the Landsat.TOA algorithm; if false, TOA values are converted to uint8 by multiplying by 255 (reflective bands) or subtracting 100 (thermal bands) and rounding to the nearest integer. |

## ee.Algorithms.ObjectType

Returns a string representing the type of the given object.

| Usage | Returns |
|---|---|
| `ee.Algorithms.ObjectType(*value*)` | String |

| Argument | Type | Details |
|---|---|---|
| `value` | Object, default: null | The object to get the type of. |

## ee.Algorithms.ProjectionTransform

Transforms the geometry of a feature to a specific projection.

| Usage | Returns |
|---|---|
| `ee.Algorithms.ProjectionTransform(feature, *proj*, *maxError*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| `feature` | Element | The feature the geometry of which is being converted. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Algorithms.Sentinel2.CDI

Computes the Cloud Displacement Index (CDI) from a Sentinel-2 Level 1C image. CDI is a measure of the optical separation in elevated objects due to sensor parallax.

Returns a floating point band named "cdi".

See Frantz, D., Hass, E., Uhl, A., Stoffels, J., \& Hill, J. (2018). Improvement of the Fmask algorithm for Sentinel-2 images: Separating clouds from bright surfaces based on parallax effects. Remote sensing of environment, 215, 471-481.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Sentinel2.CDI(source)` | Image |

| Argument | Type | Details |
|---|---|---|
| `source` | Image | The source image. |

## ee.Algorithms.String

Converts the input to a string.

| Usage | Returns |
|---|---|
| `ee.Algorithms.String(input)` | String |

| Argument | Type | Details |
|---|---|---|
| `input` | Object | The object to convert. |

## ee.Algorithms.TemporalSegmentation.C2c

An implementation of the Composite 2 Change (C2C) algorithm. This algorithm segments a time series using a piecewise linear fit with the minimum number of segments required to fit the data within the given maximum root mean squared error (RMSE). For each input band, the algorithm returns the following output bands:

- **changeDate** (Array\[Double\]): The dates at which changes are detected. The date format is determined by the dateFormat argument.
- **value** (Array\[Double\]): Value of the band at each changeDate.
- **magnitude** (Array\[Double\]): The difference between the values before and after a change date. The first magnitude is always NaN.
- **duration** (Array\[Double\]): The duration of the segment preceding the change date. The first duration is always NaN.
- **rate** (Array\[Double\]): Rate of change of the data preceding the change date. The first rate is always NaN.

If **includePostMetrics** is true the following variables are included per-band.

- **postMagnitude** (Array\[Double\]): The absolute difference between the value at the start of the next segment and the value at the change date. The last postMagnitude is always NaN.
- **postDuration** (Array\[Double\]): The duration of the segment following the change date. The last postDuration is always NaN.
- **postRate** (Array\[Double\]): The rate of change of the data following the change date. The last postRate is always NaN.

If **includeRegrowth** is true the following variables are included per-band.

- **indexRegrowth** (Array\[Double\]): The difference between the value at the change date and the value five data points after.
- **recoveryIndicator** (Array\[Double\]): The ratio of indexRegrowth to magnitude.
- **regrowth60** (Array\[Double\]): Time difference between the change date and the data point where the series value is 60% of the pre-disturbance value.
- **regrowth80** (Array\[Double\]): Time difference between the change date and the data point where the series value is 80% of the pre-disturbance value.
- **regrowth100** (Array\[Double\]): Time difference between the change date and the data point where the series value is 100% of the pre-disturbance value.

See: Hermosilla et al. (2015) https://doi.org/10.1016/j.rse.2014.11.005 for further details on the original algorithm. Algorithm implementation can be found on GitHub: https://github.com/saveriofrancini/C2C-GEE Acknowledgements: FORWARDS and NextGenCarbon.

Citation: Txomin Hermosilla, Michael A. Wulder, Joanne C. White, Nicholas C. Coops, Daniel Coelho, Giovanni Ciatto, Noel Gorelick, and Saverio Francini. In preparation. Image compositing, time-series change detection and temporal metrics: Implementation of the Composite2Change (C2C) algorithm on Google Earth Engine.

This algorithm is in preview and is subject to change.

| Usage | Returns |
|---|---|
| `ee.Algorithms.TemporalSegmentation.C2c(collection, *dateFormat*, *maxErrorList*, *spikesToleranceList*, *spikeRemovalMagnitudeList*, *maxError*, *maxSegments*, *infill*, *spikesTolerance*, *spikeRemovalMagnitude*, *includePostMetrics*, *includeRegrowth*, *interpolateRegrowth*, *useRelativeRegrowth*, *negativeMagnitudeOnly*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `collection` | ImageCollection | Collection of images on which to run C2C. |
| `dateFormat` | Integer, default: 0 | The time representation to use during fitting: 0 = jDays, 1 = fractional years, 2 = unix time in milliseconds. The start, end and break times for each temporal segment will be encoded this way. |
| `maxErrorList` | List, default: {} | List of maximum error (RMSE) values to be used for each band. If not provided, the maxError value will be used for all bands. |
| `spikesToleranceList` | List, default: {} | List of spike tolerance values to be used for each band. A value of 1 indicates no spike removal. If not provided, the spikesTolerance value will be used for all bands. |
| `spikeRemovalMagnitudeList` | List, default: {} | List of spike removal magnitude values to be used for each band. Spikes with a magnitude above this value are removed. If not provided, the spikeRemovalMagnitude value will be used for all bands. |
| `maxError` | Float, default: 0.075 | Maximum allowed RMSE of the piecewise linear fit; controls segmentation sensitivity. |
| `maxSegments` | Integer, default: 6 | Maximum number of segments permitted in the fitted tajectory. |
| `infill` | Boolean, default: true | Enables gap infilling within the time series to support stable fitting in the presence of missing values (i.e., values equal to 0). |
| `spikesTolerance` | Float, default: 0.85 | Controls tolerance of spikes in the time series. Ranges from 0 to 1. A value of 1 indicates no spike removal, lower values are more aggressive. |
| `spikeRemovalMagnitude` | Float, default: 0.1 | Spike removal magnitude threshold. Spikes with a magnitude (absolute difference from the average of neighbors) above this value are removed. |
| `includePostMetrics` | Boolean, default: true | Returns post-change descriptors (postMagnitude, postDuration, postRate). |
| `includeRegrowth` | Boolean, default: false | Returns recovery/regrowth metrics (indexRegrowth, recoveryIndicator, regrowth60/80/100). |
| `interpolateRegrowth` | Boolean, default: true | Linearly interpolate the time series using the detected changes before calculating the regrowth metrics. |
| `useRelativeRegrowth` | Boolean, default: false | Computes regrowth thresholds in relative terms to pre-disturbance conditions. |
| `negativeMagnitudeOnly` | Boolean, default: false | Retains only breakpoints associated with negative changes (directional filtering). |

## ee.Algorithms.TemporalSegmentation.Ccdc

Implements the Continuous Change Detection and Classification temporal breakpoint algorithm. This algorithm finds temporal breakpoints in an image collection by iteratively fitting harmonic functions to the data. Fit coefficients are produced for all input bands, but the bands used for breakpoint detection can be specified with the 'breakpointBands' argument.

For more details, see Zhu, Z. and Woodcock, C.E., 2014. Continuous change detection and classification of land cover using all available Landsat data. Remote sensing of Environment, 144, pp.152-171.

| Usage | Returns |
|---|---|
| `ee.Algorithms.TemporalSegmentation.Ccdc(collection, *breakpointBands*, *tmaskBands*, *minObservations*, *chiSquareProbability*, *minNumOfYearsScaler*, *dateFormat*, *lambda*, *maxIterations*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `collection` | ImageCollection | Collection of images on which to run CCDC. |
| `breakpointBands` | List, default: null | The name or index of the bands to use for change detection. If unspecified, all bands are used. |
| `tmaskBands` | List, default: null | The name or index of the bands to use for iterative TMask cloud detection. These are typically the green band and the SWIR1 band. If unspecified, TMask is not used. If specified, 'tmaskBands' must be included in 'breakpointBands'. |
| `minObservations` | Integer, default: 6 | The number of observations required to flag a change. |
| `chiSquareProbability` | Float, default: 0.99 | The chi-square probability threshold for change detection in the range of \[0, 1\]. |
| `minNumOfYearsScaler` | Float, default: 1.33 | Factors of minimum number of years to apply new fitting. |
| `dateFormat` | Integer, default: 0 | The time representation to use during fitting: 0 = jDays, 1 = fractional years, 2 = unix time in milliseconds. The start, end and break times for each temporal segment will be encoded this way. |
| `lambda` | Float, default: 20 | Lambda for LASSO regression fitting. If set to 0, regular OLS is used instead of LASSO. |
| `maxIterations` | Integer, default: 25000 | Maximum number of runs for LASSO regression convergence. If set to 0, regular OLS is used instead of LASSO. |

## ee.Algorithms.TemporalSegmentation.Ewmacd

Exponentially Weighted Moving Average Change Detection. This algorithm computes a harmonic model for the 'training' portion of the input data and subtracts that from the original results. The residuals are then subjected to Shewhart X-bar charts and an exponentially weighted moving average. Disturbed pixels are indicated when the charts signal a deviation from the given control limits.

The output is a 5 band image containing the bands:

- ewma: a 1D array of the EWMA score for each input image. Negative values represent disturbance and positive values represent recovery.
- harmonicCoefficients: A 1-D array of the computed harmonic coefficient pairs. The coefficients are ordered as \[constant, sin0, cos0, sin1, cos1...\]
- rmse: the RMSE from the harmonic regression.
- rSquared: r-squared value from the harmonic regression.
- residuals: 1D array of residuals from the harmonic regression.

See: Brooks, E.B., Wynne, R.H., Thomas, V.A., Blinn, C.E. and Coulston, J.W., 2014. On-the-fly massively multitemporal change detection using statistical quality control charts and Landsat data. IEEE Transactions on Geoscience and Remote Sensing, 52(6), pp.3316-3332.

<br />

| Usage | Returns |
|---|---|
| `ee.Algorithms.TemporalSegmentation.Ewmacd(timeSeries, vegetationThreshold, trainingStartYear, trainingEndYear, *harmonicCount*, *xBarLimit1*, *xBarLimit2*, *lambda*, *lambdasigs*, *rounding*, *persistence*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `timeSeries` | ImageCollection | Collection from which to extract EWMA. This collection is expected to contain 1 image for each year and be sorted temporally. |
| `vegetationThreshold` | Float | Threshold for vegetation. Values below this are considered non-vegetation. |
| `trainingStartYear` | Integer | Start year of training period, inclusive. |
| `trainingEndYear` | Integer | End year of training period, exclusive. |
| `harmonicCount` | Integer, default: 2 | Number of harmonic function pairs (sine and cosine) used. |
| `xBarLimit1` | Float, default: 1.5 | Threshold for initial training xBar limit. |
| `xBarLimit2` | Integer, default: 20 | Threshold for running xBar limit. |
| `lambda` | Float, default: 0.3 | The 'lambda' tuning parameter weighting new years vs the running average. |
| `lambdasigs` | Float, default: 3 | EWMA control bounds, in units of standard deviations. |
| `rounding` | Boolean, default: true | Should rounding be performed for EWMA. |
| `persistence` | Integer, default: 3 | Minimum number of observations needed to consider a change. |

## ee.Algorithms.TemporalSegmentation.LandTrendr

Landsat-based detection of Trends in Disturbance and Recovery: temporally segments a time-series of images by extracting the spectral trajectories of change over time. The first band of each image is used to find breakpoints, and those breakpoints are used to perform fitting on all subsequent bands. The breakpoints are returned as a 2-D matrix of 4 rows and as many columns as images. The first two rows are the original X and Y values. The third row contains the Y values fitted to the estimated segments, and the 4th row contains a 1 if the corresponding point was used as a segment vertex or 0 if not. Any additional fitted bands are appended as rows in the output. Breakpoint fitting assumes that increasing values represent disturbance and decreasing values represent recovery.

See: Kennedy, R.E., Yang, Z. and Cohen, W.B., 2010. Detecting trends in forest disturbance and recovery using yearly Landsat time series: 1. LandTrendr - Temporal segmentation algorithms. Remote Sensing of Environment, 114(12), pp.2897-2910.

| Usage | Returns |
|---|---|
| `ee.Algorithms.TemporalSegmentation.LandTrendr(timeSeries, maxSegments, *spikeThreshold*, *vertexCountOvershoot*, *preventOneYearRecovery*, *recoveryThreshold*, *pvalThreshold*, *bestModelProportion*, *minObservationsNeeded*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `timeSeries` | ImageCollection | Yearly time-series from which to extract breakpoints. The first band is used to find breakpoints, and all subsequent bands are fitted using those breakpoints. |
| `maxSegments` | Integer | Maximum number of segments to be fitted on the time series. |
| `spikeThreshold` | Float, default: 0.9 | Threshold for dampening the spikes (1.0 means no dampening). |
| `vertexCountOvershoot` | Integer, default: 3 | The initial model can overshoot the maxSegments + 1 vertices by this amount. Later, it will be pruned down to maxSegments + 1. |
| `preventOneYearRecovery` | Boolean, default: false | Prevent segments that represent one year recoveries. |
| `recoveryThreshold` | Float, default: 0.25 | If a segment has a recovery rate faster than 1/recoveryThreshold (in years), then the segment is disallowed. |
| `pvalThreshold` | Float, default: 0.1 | If the p-value of the fitted model exceeds this threshold, then the current model is discarded and another one is fitted using the Levenberg-Marquardt optimizer. |
| `bestModelProportion` | Float, default: 0.75 | Allows models with more vertices to be chosen if their p-value is no more than (2 - bestModelProportion) times the p-value of the best model. |
| `minObservationsNeeded` | Integer, default: 6 | Min observations needed to perform output fitting. |

## ee.Algorithms.TemporalSegmentation.LandTrendrFit

Interpolates a time series using a set of LandTrendr breakpoint years. For each input band in the timeSeries, outputs a new 1D array-valued band containing the input values interpolated between the breakpoint times identified by the vertices image. See the LandTrendr Algorithm for more details.

| Usage | Returns |
|---|---|
| `ee.Algorithms.TemporalSegmentation.LandTrendrFit(timeSeries, vertices, *spikeThreshold*, *minObservationsNeeded*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `timeSeries` | ImageCollection | Time series to interpolate. |
| `vertices` | Image | Vertices image. A 1D array of LandTrendr breakpoint years. |
| `spikeThreshold` | Float, default: 0.9 | Threshold for dampening input spikes (1.0 means no dampening). |
| `minObservationsNeeded` | Integer, default: 6 | Min observations needed. |

## ee.Algorithms.TemporalSegmentation.StructuralChangeBreakpoints

Runs breakpoint detection, similar to R's strucchange::breakpoints function.

Each pixel is fit by a piecewise linear/harmonic model, of the form Y = A + B \* t + C \* cos(2 \* pi \* season(t)) + D \* sin(2 \* pi \* season(t)) + E \* cos(4 \* pi \* season(t)) + F \* sin(4 \* pi \* season(t)) + ...

In this equation, 't' is the start time of the image in the format specified by 'dateFormat', and 'season(t)' is the fractional year of that start time (see the description of dateFormat for details). The maximum order of the harmonic terms is determined by 'seasonalModelOrder'.

The result is an image containing two bands, plus two bands per band in the input:

- `tStart`, `tEnd`: each of these holds a 1D array, with one entry per segment in the piecewise linear fit; each entry contains the start time of the first or last images in that segment. By default the values here are in fractional years, for easy use with the coefficients.
- `coefs_BANDNAME`: there will be one such output band per input band. Each of these holds a 2D array, with one row per segment. The values in that row are the coefficients of the linear fit for that segment - that is, the values of A, B, C, ... for that segment. As described above, the values here are affected by 'dateFormat'.
- `rmse_BANDNAME`: there will be one such output band per input band. This holds a 1D array, with one entry per segment. The value for each segment is the RMSE for the linear fit residuals for that segment.

<br />

| Usage | Returns |
|---|---|
| `ee.Algorithms.TemporalSegmentation.StructuralChangeBreakpoints(collection, *breakpointBand*, *seasonalModelOrder*, *minSpacing*, *maxBreaks*, *dateFormat*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `collection` | ImageCollection | Collection of images on which to detect breakpoints. |
| `breakpointBand` | String, default: null | The name of the band to use for breakpoint detection. Optional only if the images have only a single band. |
| `seasonalModelOrder` | Integer, default: 3 | The order of the harmonic seasonal model. |
| `minSpacing` | Float, default: 0.15 | The minimum spacing between breakpoints. If this is between 0 and 1 (exclusive), it will be interpreted as a fraction of the number of images in the collection. Otherwise, it will be interpreted as a number of samples. |
| `maxBreaks` | Integer, default: 0 | The maximum number of breakpoints. |
| `dateFormat` | Integer, default: 1 | The time representation to use in the results: 1 = fractional years, 2 = unix time in milliseconds. This affects the values in the tStart and tEnd bands and the 't' values used in the harmonic model. The fractional years used here and in that model are defined as the fractional number of 365.25-day years since 1 Jan 1970. |

## ee.Algorithms.TemporalSegmentation.VCT

Vegetation Change Tracker, an automated approach for reconstructing recent forest disturbance history using dense Landsat time series stacks.

The output is a 2D array per pixel containing 6 rows x N years. The output rows contain: input years, VCT landcover mask, magnitude in terms of the UD composite, magnitude of disturbance in B4, magnitude of disturbance in NDVI, magnitude of disturbance in dNBR.

See: Huang, C., Goward, S.N., Masek, J.G., Thomas, N., Zhu, Z. and Vogelmann, J.E., 2010. An automated approach for reconstructing recent forest disturbance history using dense Landsat time series stacks. Remote Sensing of Environment, 114(1), pp.183-198.

| Usage | Returns |
|---|---|
| `ee.Algorithms.TemporalSegmentation.VCT(timeSeries, landCover, *maxUd*, *minNdvi*, *forThrMax*, *nYears*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `timeSeries` | ImageCollection | Collection from which to extract VCT disturbances, containing the bands: B3, B4, B5, B7, thermal, NDVI, DNBR, and COMP. This collection is expected to contain 1 image for each year, sorted by time. |
| `landCover` | ImageCollection | Collection from which to extract VCT masks. This collection is expected to contain 1 image for each image in the timeSeries, sorted by time. |
| `maxUd` | Float, default: 4 | Maximum Z-score composite value for detecting forest. |
| `minNdvi` | Float, default: 0.45 | Minimum NDVI value for forest. |
| `forThrMax` | Float, default: 3 | Maximum threshold for forest. |
| `nYears` | Integer, default: 30 | Maximum number of years. |

## ee.Algorithms.TemporalSegmentation.Verdet

Vegetation Regeneration and Disturbance Estimates through Time, forest change detection algorithm. This algorithm generates a yearly clear-sky composite from satellite imagery, calculates a spectral vegetation index for each pixel in that composite, spatially segments the vegetation index image into patches, temporally divides the time series into differently sloped segments, and then labels those segments as disturbed, stable, or regenerating. Segmentation at both the spatial and temporal steps are performed using total variation regularization.

The output consists of a 1D array per pixel containing the slope of fitted trend lines. Negative values indicate disturbance and positive values regeneration.

See: Hughes, M.J., Kaylor, S.D. and Hayes, D.J., 2017. Patch-based forest change detection from Landsat time series. Forests, 8(5), p.166.

| Usage | Returns |
|---|---|
| `ee.Algorithms.TemporalSegmentation.Verdet(timeSeries, *tolerance*, *alpha*, *nRuns*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `timeSeries` | ImageCollection | Collection from which to extract VeRDET scores. This collection is expected to contain 1 image for each year, sorted temporally. |
| `tolerance` | Float, default: 0.0001 | Convergence tolerance. |
| `alpha` | Float, default: 0.03333333333333333 | Regularization parameter for segmentation. |
| `nRuns` | Integer, default: 100 | Maximum number of runs for convergence. |

## ee.Algorithms.Terrain

Calculates slope, aspect, and a simple hillshade from a terrain DEM.

Expects an image containing either a single band of elevation, measured in meters, or if there's more than one band, one named 'elevation'. Adds output bands named 'slope' and 'aspect' measured in degrees plus an unsigned byte output band named 'hillshade' for visualization. All other bands and metadata are copied from the input image. The local gradient is computed using the 4-connected neighbors of each pixel, so missing values will occur around the edges of an image.

| Usage | Returns |
|---|---|
| `ee.Algorithms.Terrain(input)` | Image |

| Argument | Type | Details |
|---|---|---|
| `input` | Image | An elevation image, in meters. |

