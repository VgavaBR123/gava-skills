# Vetor — ee.FeatureCollection, ee.Feature, ee.Filter, ee.Join

> 154 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.Feature`](#ee-feature)
- [`ee.Feature.area`](#ee-feature-area)
- [`ee.Feature.aside`](#ee-feature-aside)
- [`ee.Feature.bounds`](#ee-feature-bounds)
- [`ee.Feature.buffer`](#ee-feature-buffer)
- [`ee.Feature.centroid`](#ee-feature-centroid)
- [`ee.Feature.closestPoint`](#ee-feature-closestpoint)
- [`ee.Feature.closestPoints`](#ee-feature-closestpoints)
- [`ee.Feature.containedIn`](#ee-feature-containedin)
- [`ee.Feature.contains`](#ee-feature-contains)
- [`ee.Feature.convexHull`](#ee-feature-convexhull)
- [`ee.Feature.copyProperties`](#ee-feature-copyproperties)
- [`ee.Feature.cutLines`](#ee-feature-cutlines)
- [`ee.Feature.difference`](#ee-feature-difference)
- [`ee.Feature.disjoint`](#ee-feature-disjoint)
- [`ee.Feature.dissolve`](#ee-feature-dissolve)
- [`ee.Feature.distance`](#ee-feature-distance)
- [`ee.Feature.evaluate`](#ee-feature-evaluate)
- [`ee.Feature.geometry`](#ee-feature-geometry)
- [`ee.Feature.get`](#ee-feature-get)
- [`ee.Feature.getArray`](#ee-feature-getarray)
- [`ee.Feature.getInfo`](#ee-feature-getinfo)
- [`ee.Feature.getMapId`](#ee-feature-getmapid)
- [`ee.Feature.getNumber`](#ee-feature-getnumber)
- [`ee.Feature.getString`](#ee-feature-getstring)
- [`ee.Feature.hersDescriptor`](#ee-feature-hersdescriptor)
- [`ee.Feature.id`](#ee-feature-id)
- [`ee.Feature.intersection`](#ee-feature-intersection)
- [`ee.Feature.intersects`](#ee-feature-intersects)
- [`ee.Feature.length`](#ee-feature-length)
- [`ee.Feature.perimeter`](#ee-feature-perimeter)
- [`ee.Feature.propertyNames`](#ee-feature-propertynames)
- [`ee.Feature.select`](#ee-feature-select)
- [`ee.Feature.serialize`](#ee-feature-serialize)
- [`ee.Feature.set`](#ee-feature-set)
- [`ee.Feature.setGeometry`](#ee-feature-setgeometry)
- [`ee.Feature.simplify`](#ee-feature-simplify)
- [`ee.Feature.symmetricDifference`](#ee-feature-symmetricdifference)
- [`ee.Feature.toArray`](#ee-feature-toarray)
- [`ee.Feature.toDictionary`](#ee-feature-todictionary)
- [`ee.Feature.transform`](#ee-feature-transform)
- [`ee.Feature.union`](#ee-feature-union)
- [`ee.Feature.withinDistance`](#ee-feature-withindistance)
- [`ee.FeatureCollection`](#ee-featurecollection)
- [`ee.FeatureCollection.aggregate_array`](#ee-featurecollection-aggregate-array)
- [`ee.FeatureCollection.aggregate_count`](#ee-featurecollection-aggregate-count)
- [`ee.FeatureCollection.aggregate_count_distinct`](#ee-featurecollection-aggregate-count-distinct)
- [`ee.FeatureCollection.aggregate_first`](#ee-featurecollection-aggregate-first)
- [`ee.FeatureCollection.aggregate_histogram`](#ee-featurecollection-aggregate-histogram)
- [`ee.FeatureCollection.aggregate_max`](#ee-featurecollection-aggregate-max)
- [`ee.FeatureCollection.aggregate_mean`](#ee-featurecollection-aggregate-mean)
- [`ee.FeatureCollection.aggregate_min`](#ee-featurecollection-aggregate-min)
- [`ee.FeatureCollection.aggregate_product`](#ee-featurecollection-aggregate-product)
- [`ee.FeatureCollection.aggregate_sample_sd`](#ee-featurecollection-aggregate-sample-sd)
- [`ee.FeatureCollection.aggregate_sample_var`](#ee-featurecollection-aggregate-sample-var)
- [`ee.FeatureCollection.aggregate_stats`](#ee-featurecollection-aggregate-stats)
- [`ee.FeatureCollection.aggregate_sum`](#ee-featurecollection-aggregate-sum)
- [`ee.FeatureCollection.aggregate_total_sd`](#ee-featurecollection-aggregate-total-sd)
- [`ee.FeatureCollection.aggregate_total_var`](#ee-featurecollection-aggregate-total-var)
- [`ee.FeatureCollection.aside`](#ee-featurecollection-aside)
- [`ee.FeatureCollection.bounds`](#ee-featurecollection-bounds)
- [`ee.FeatureCollection.classify`](#ee-featurecollection-classify)
- [`ee.FeatureCollection.cluster`](#ee-featurecollection-cluster)
- [`ee.FeatureCollection.copyProperties`](#ee-featurecollection-copyproperties)
- [`ee.FeatureCollection.distance`](#ee-featurecollection-distance)
- [`ee.FeatureCollection.distinct`](#ee-featurecollection-distinct)
- [`ee.FeatureCollection.draw`](#ee-featurecollection-draw)
- [`ee.FeatureCollection.errorMatrix`](#ee-featurecollection-errormatrix)
- [`ee.FeatureCollection.evaluate`](#ee-featurecollection-evaluate)
- [`ee.FeatureCollection.filter`](#ee-featurecollection-filter)
- [`ee.FeatureCollection.filterBounds`](#ee-featurecollection-filterbounds)
- [`ee.FeatureCollection.filterDate`](#ee-featurecollection-filterdate)
- [`ee.FeatureCollection.first`](#ee-featurecollection-first)
- [`ee.FeatureCollection.flatten`](#ee-featurecollection-flatten)
- [`ee.FeatureCollection.geometry`](#ee-featurecollection-geometry)
- [`ee.FeatureCollection.get`](#ee-featurecollection-get)
- [`ee.FeatureCollection.getArray`](#ee-featurecollection-getarray)
- [`ee.FeatureCollection.getDownloadURL`](#ee-featurecollection-getdownloadurl)
- [`ee.FeatureCollection.getInfo`](#ee-featurecollection-getinfo)
- [`ee.FeatureCollection.getMapId`](#ee-featurecollection-getmapid)
- [`ee.FeatureCollection.getNumber`](#ee-featurecollection-getnumber)
- [`ee.FeatureCollection.getString`](#ee-featurecollection-getstring)
- [`ee.FeatureCollection.inverseDistance`](#ee-featurecollection-inversedistance)
- [`ee.FeatureCollection.iterate`](#ee-featurecollection-iterate)
- [`ee.FeatureCollection.kriging`](#ee-featurecollection-kriging)
- [`ee.FeatureCollection.limit`](#ee-featurecollection-limit)
- [`ee.FeatureCollection.loadBigQueryTable`](#ee-featurecollection-loadbigquerytable)
- [`ee.FeatureCollection.makeArray`](#ee-featurecollection-makearray)
- [`ee.FeatureCollection.map`](#ee-featurecollection-map)
- [`ee.FeatureCollection.merge`](#ee-featurecollection-merge)
- [`ee.FeatureCollection.propertyNames`](#ee-featurecollection-propertynames)
- [`ee.FeatureCollection.randomColumn`](#ee-featurecollection-randomcolumn)
- [`ee.FeatureCollection.randomPoints`](#ee-featurecollection-randompoints)
- [`ee.FeatureCollection.reduceColumns`](#ee-featurecollection-reducecolumns)
- [`ee.FeatureCollection.reduceToImage`](#ee-featurecollection-reducetoimage)
- [`ee.FeatureCollection.remap`](#ee-featurecollection-remap)
- [`ee.FeatureCollection.runBigQuery`](#ee-featurecollection-runbigquery)
- [`ee.FeatureCollection.select`](#ee-featurecollection-select)
- [`ee.FeatureCollection.serialize`](#ee-featurecollection-serialize)
- [`ee.FeatureCollection.set`](#ee-featurecollection-set)
- [`ee.FeatureCollection.size`](#ee-featurecollection-size)
- [`ee.FeatureCollection.sort`](#ee-featurecollection-sort)
- [`ee.FeatureCollection.style`](#ee-featurecollection-style)
- [`ee.FeatureCollection.toDictionary`](#ee-featurecollection-todictionary)
- [`ee.FeatureCollection.toList`](#ee-featurecollection-tolist)
- [`ee.FeatureCollection.union`](#ee-featurecollection-union)
- [`ee.Filter`](#ee-filter)
- [`ee.Filter.and`](#ee-filter-and)
- [`ee.Filter.area`](#ee-filter-area)
- [`ee.Filter.aside`](#ee-filter-aside)
- [`ee.Filter.bounds`](#ee-filter-bounds)
- [`ee.Filter.calendarRange`](#ee-filter-calendarrange)
- [`ee.Filter.contains`](#ee-filter-contains)
- [`ee.Filter.date`](#ee-filter-date)
- [`ee.Filter.dateRangeContains`](#ee-filter-daterangecontains)
- [`ee.Filter.dayOfYear`](#ee-filter-dayofyear)
- [`ee.Filter.disjoint`](#ee-filter-disjoint)
- [`ee.Filter.eq`](#ee-filter-eq)
- [`ee.Filter.equals`](#ee-filter-equals)
- [`ee.Filter.evaluate`](#ee-filter-evaluate)
- [`ee.Filter.expression`](#ee-filter-expression)
- [`ee.Filter.getInfo`](#ee-filter-getinfo)
- [`ee.Filter.greaterThan`](#ee-filter-greaterthan)
- [`ee.Filter.greaterThanOrEquals`](#ee-filter-greaterthanorequals)
- [`ee.Filter.gt`](#ee-filter-gt)
- [`ee.Filter.gte`](#ee-filter-gte)
- [`ee.Filter.hasType`](#ee-filter-hastype)
- [`ee.Filter.inList`](#ee-filter-inlist)
- [`ee.Filter.intersects`](#ee-filter-intersects)
- [`ee.Filter.isContained`](#ee-filter-iscontained)
- [`ee.Filter.lessThan`](#ee-filter-lessthan)
- [`ee.Filter.lessThanOrEquals`](#ee-filter-lessthanorequals)
- [`ee.Filter.listContains`](#ee-filter-listcontains)
- [`ee.Filter.lt`](#ee-filter-lt)
- [`ee.Filter.lte`](#ee-filter-lte)
- [`ee.Filter.maxDifference`](#ee-filter-maxdifference)
- [`ee.Filter.neq`](#ee-filter-neq)
- [`ee.Filter.not`](#ee-filter-not)
- [`ee.Filter.notEquals`](#ee-filter-notequals)
- [`ee.Filter.notNull`](#ee-filter-notnull)
- [`ee.Filter.or`](#ee-filter-or)
- [`ee.Filter.rangeContains`](#ee-filter-rangecontains)
- [`ee.Filter.serialize`](#ee-filter-serialize)
- [`ee.Filter.stringContains`](#ee-filter-stringcontains)
- [`ee.Filter.stringEndsWith`](#ee-filter-stringendswith)
- [`ee.Filter.stringStartsWith`](#ee-filter-stringstartswith)
- [`ee.Filter.withinDistance`](#ee-filter-withindistance)
- [`ee.Join.apply`](#ee-join-apply)
- [`ee.Join.inner`](#ee-join-inner)
- [`ee.Join.inverted`](#ee-join-inverted)
- [`ee.Join.saveAll`](#ee-join-saveall)
- [`ee.Join.saveBest`](#ee-join-savebest)
- [`ee.Join.saveFirst`](#ee-join-savefirst)
- [`ee.Join.simple`](#ee-join-simple)

---

## ee.Feature

Features can be constructed from one of the following arguments plus an optional dictionary of properties:

- An ee.Geometry.

- A GeoJSON Geometry.

- A GeoJSON Feature.

- A computed object: reinterpreted as a geometry if properties are specified, and as a feature if they aren't.

| Usage | Returns |
|---|---|
| `ee.Feature(geometry, *properties*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| `geometry` | ComputedObject\|Feature\|Geometry\|Object | A geometry or feature. |
| `properties` | Object, optional | A dictionary of metadata properties. If the first parameter is a Feature (instead of a geometry), this is unused. |

## ee.Feature.area

Returns the area of the feature's default geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `Feature.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature from which the geometry is taken. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Feature.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Feature.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Feature.bounds

Returns a feature containing the bounding box of the geometry of a given feature.

| Usage | Returns |
|---|---|
| `Feature.bounds(*maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature the bound of which is being calculated. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Feature.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `Feature.buffer(distance, *maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature the geometry of which is being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Feature.centroid

Returns a feature containing the point at the center of the highest-dimension components of the geometry of a feature. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `Feature.centroid(*maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | Calculates the centroid of this feature's default geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Feature.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `Feature.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.closestPoints

Returns a dictionary containing up to two entries representing a point on each input feature's geometry that is closest to the geometry of the other input. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `Feature.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.containedIn

Returns true if and only if the geometry of one feature is contained in the geometry of another.

| Usage | Returns |
|---|---|
| `Feature.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.contains

Returns true if and only if the geometry of one feature contains the geometry of another.

| Usage | Returns |
|---|---|
| `Feature.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.convexHull

Returns the feature with the geometry replaced by the convex hull of the original geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `Feature.convexHull(*maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature containing the geometry whole hull is being calculated. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.copyProperties

Copies metadata properties from one element to another.

| Usage | Returns |
|---|---|
| `Feature.copyProperties(*source*, *properties*, *exclude*)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `destination` | Element, default: null | The object whose properties to override. |
| `source` | Element, default: null | The object from which to copy the properties. |
| `properties` | List, default: null | The properties to copy. If omitted, all ordinary (i.e. non-system) properties are copied. |
| `exclude` | List, default: null | The list of properties to exclude when copying all properties. Must not be specified if properties is. |

## ee.Feature.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `Feature.cutLines(distances, *maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | Cuts the lines of this feature's default geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Feature.difference

Returns a feature with the properties of the 'left' feature, and the geometry that results from subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `Feature.difference(right, *maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. The properties of the result will be copied from this object. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. The properties of this object are ignored. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.disjoint

Returns true if and only if the feature geometries are disjoint.

| Usage | Returns |
|---|---|
| `Feature.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.dissolve

Returns a feature containing the union of the geometry of a feature. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `Feature.dissolve(*maxError*, *proj*)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature the geometry of which is being unioned. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Feature.distance

Returns the minimum distance between the geometries of two features.

| Usage | Returns |
|---|---|
| `Feature.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Feature.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Feature.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Feature.geometry

Returns the geometry of a given feature in a given projection.

| Usage | Returns |
|---|---|
| `Feature.geometry(*maxError*, *proj*, *geodesics*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature from which the geometry is taken. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the geometry will be in this projection. If unspecified, the geometry will be in its default projection. |
| `geodesics` | Boolean, default: null | If true, the geometry will have geodesic edges. If false, it will have edges as straight lines in the specified projection. If null, the edge interpretation will be the same as the original geometry. This argument is ignored if proj is not specified. |

## ee.Feature.get

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `Feature.get(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.Feature.getArray

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `Feature.getArray(property)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.Feature.getInfo

An imperative function that returns information about this feature via an AJAX call.

Returns a description of the feature.

| Usage | Returns |
|---|---|
| `Feature.getInfo(*callback*)` | GeoJSONFeature |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Feature | The Feature instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. If supplied, will be called with the first parameter if successful and the second if unsuccessful. |

## ee.Feature.getMapId

An imperative function that returns a map ID and optional token, suitable for generating a Map overlay.

Returns an object which may be passed to ee.data.getTileUrl or ui.Map.addLayer, including an additional 'image' field, containing a Collection.draw image wrapping a FeatureCollection containing this feature. Undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `Feature.getMapId(*visParams*, *callback*)` | MapId\|Object |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Feature | The Feature instance. |
| `visParams` | Object, optional | The visualization parameters. Currently only one parameter, 'color', containing an RGB color string is allowed. If visParams is not specified, black ("000000") is used. |
| `callback` | Function, optional | An async callback. |

## ee.Feature.getNumber

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `Feature.getNumber(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.Feature.getString

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `Feature.getString(property)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.Feature.hersDescriptor

Creates a dictionary of Histogram Error Ring Statistic (HERS) descriptor arrays from square array properties of an element. The HERS radius is taken to be the array's (side_length - 1) / 2.

| Usage | Returns |
|---|---|
| `Feature.hersDescriptor(*selectors*, *buckets*, *peakWidthScale*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The element with array properties. |
| `selectors` | List, default: null | The array properties for which descriptors will be created. Selected array properties must be square, floating point arrays. Defaults to all array properties. |
| `buckets` | Integer, default: 100 | The number of HERS buckets. Defaults to 100. |
| `peakWidthScale` | Float, default: 1 | The HERS peak width scale. Defaults to 1.0. |

## ee.Feature.id

Returns the ID of a given element within a collection. Objects outside collections are not guaranteed to have IDs.

| Usage | Returns |
|---|---|
| `Feature.id()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The element from which the ID is taken. |

## ee.Feature.intersection

Returns a feature containing the intersection of the geometries of two features, with the properties of the left feature.

| Usage | Returns |
|---|---|
| `Feature.intersection(right, *maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. The properties of the result will be copied from this object. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. The properties of this object are ignored. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.intersects

Returns true if and only if the feature geometries intersect.

| Usage | Returns |
|---|---|
| `Feature.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.length

Returns the length of the linear parts of the geometry of a given feature. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `Feature.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature from which the geometry is taken. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Feature.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry of a given feature. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `Feature.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature from which the geometry is taken. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Feature.propertyNames

Returns the names of properties on this element.

| Usage | Returns |
|---|---|
| `Feature.propertyNames()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element |   |

## ee.Feature.select

Selects properties from a feature by name or RE2-compatible regex and optionally renames them.

| Usage | Returns |
|---|---|
| `Feature.select(propertySelectors, *newProperties*, *retainGeometry*)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Element | The feature to select properties from. |
| `propertySelectors` | List | A list of names or regexes specifying the properties to select. |
| `newProperties` | List, default: null | Optional new names for the output properties. Must match the number of properties selected. |
| `retainGeometry` | Boolean, default: true | When false, the result will have a NULL geometry. |

## ee.Feature.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Feature.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Feature.set

Overrides one or more metadata properties of an Element.

Returns the element with the specified properties overridden.

| Usage | Returns |
|---|---|
| `Feature.set(var_args)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The Element instance. |
| `var_args` | VarArgs\[Object\] | Either a dictionary of properties, or a vararg sequence of properties, e.g. key1, value1, key2, value2, ... |

## ee.Feature.setGeometry

Returns the feature with the geometry replaced by the specified geometry.

| Usage | Returns |
|---|---|
| `Feature.setGeometry(*geometry*)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature on which to set the geometry. |
| `geometry` | Geometry, default: null | The geometry to set. |

## ee.Feature.simplify

Simplifies the geometry of a feature to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `Feature.simplify(maxError, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature whose geometry is being simplified. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Feature.symmetricDifference

Returns a feature containing the symmetric difference between geometries of two features.

| Usage | Returns |
|---|---|
| `Feature.symmetricDifference(right, *maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. The properties of the result will be copied from this object. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. The properties of this object are ignored. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.toArray

Creates an array from the given properties of an object, which must all be numbers.

| Usage | Returns |
|---|---|
| `Feature.toArray(properties)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Feature | The object from which to select array properties. |
| `properties` | List | The property selectors for each array element. |

## ee.Feature.toDictionary

Extract properties from a feature as a dictionary.

| Usage | Returns |
|---|---|
| `Feature.toDictionary(*properties*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The feature to extract the property from. |
| `properties` | List, default: null | The list of properties to extract. Defaults to all non-system properties. |

## ee.Feature.transform

Transforms the geometry of a feature to a specific projection.

| Usage | Returns |
|---|---|
| `Feature.transform(*proj*, *maxError*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature the geometry of which is being converted. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Feature.union

Returns a feature containing the union of the geometries of two features.

| Usage | Returns |
|---|---|
| `Feature.union(right, *maxError*, *proj*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. The properties of the result will be copied from this object. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. The properties of this object are ignored. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Feature.withinDistance

Returns true if and only if the geometries of two features are within a specified distance.

| Usage | Returns |
|---|---|
| `Feature.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Element | The feature containing the geometry used as the left operand of the operation. |
| `right` | Element | The feature containing the geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.FeatureCollection

FeatureCollections can be constructed from the following arguments:

- A string: assumed to be the name of a collection.

- A single geometry.

- A single feature.

- A list of features.

- A GeoJSON FeatureCollection

- A computed object: reinterpreted as a collection.

| Usage | Returns |
|---|---|
| `ee.FeatureCollection(args, *column*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| `args` | ComputedObject\|Feature\|FeatureCollection\|Geometry\|List\|List\[Object\]\|Number\|String | The constructor arguments. |
| `column` | String, optional | The name of the geometry column to use. Only useful when working with a named collection. |

## ee.FeatureCollection.aggregate_array

Aggregates over a given property of the objects in a collection, calculating a list of all the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_array(property)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_count

Aggregates over a given property of the objects in a collection, calculating the number of non-null values of the property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_count(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_count_distinct

Aggregates over a given property of the objects in a collection, calculating the number of distinct values for the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_count_distinct(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_first

Aggregates over a given property of the objects in a collection, calculating the property value of the first object in the collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_first(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_histogram

Aggregates over a given property of the objects in a collection, calculating a histogram of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_histogram(property)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_max

Aggregates over a given property of the objects in a collection, calculating the maximum of the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_max(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_mean

Aggregates over a given property of the objects in a collection, calculating the mean of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_mean(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_min

Aggregates over a given property of the objects in a collection, calculating the minimum of the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_min(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_product

Aggregates over a given property of the objects in a collection, calculating the product of the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_product(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_sample_sd

Aggregates over a given property of the objects in a collection, calculating the sample std. deviation of the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_sample_sd(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_sample_var

Aggregates over a given property of the objects in a collection, calculating the sample variance of the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_sample_var(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_stats

Aggregates over a given property of the objects in a collection, calculating the sum, min, max, mean, sample standard deviation, sample variance, total standard deviation and total variance of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_stats(property)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_sum

Aggregates over a given property of the objects in a collection, calculating the sum of the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_sum(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_total_sd

Aggregates over a given property of the objects in a collection, calculating the total std. deviation of the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_total_sd(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aggregate_total_var

Aggregates over a given property of the objects in a collection, calculating the total variance of the values of the selected property.

| Usage | Returns |
|---|---|
| `FeatureCollection.aggregate_total_var(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.FeatureCollection.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `FeatureCollection.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.FeatureCollection.bounds

Constructs a bounding box around the geometries in a collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection whose bounds will be constructed. |
| `maxError` | ErrorMargin, optional | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, optional | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.FeatureCollection.classify

Classifies each feature in a collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.classify(classifier, *outputName*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `features` | FeatureCollection | The collection of features to classify. Each feature must contain all the properties in the classifier's schema. |
| `classifier` | Classifier | The classifier to use. |
| `outputName` | String, default: "classification" | The name of the output property to be added. This argument is ignored if the classifier has more than one output. |

## ee.FeatureCollection.cluster

Clusters each feature in a collection, adding a new column to each feature containing the cluster number to which it has been assigned.

| Usage | Returns |
|---|---|
| `FeatureCollection.cluster(clusterer, *outputName*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `features` | FeatureCollection | The collection of features to cluster. Each feature must contain all the properties in the clusterer's schema. |
| `clusterer` | Clusterer | The clusterer to use. |
| `outputName` | String, default: "cluster" | The name of the output property to be added. |

## ee.FeatureCollection.copyProperties

Copies metadata properties from one element to another.

| Usage | Returns |
|---|---|
| `FeatureCollection.copyProperties(*source*, *properties*, *exclude*)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `destination` | Element, default: null | The object whose properties to override. |
| `source` | Element, default: null | The object from which to copy the properties. |
| `properties` | List, default: null | The properties to copy. If omitted, all ordinary (i.e. non-system) properties are copied. |
| `exclude` | List, default: null | The list of properties to exclude when copying all properties. Must not be specified if properties is. |

## ee.FeatureCollection.distance

Produces a DOUBLE image where each pixel is the distance in meters from the pixel center to the nearest Point, LineString, or polygonal boundary in the collection.

Note distance is also measured within interiors of polygons. Pixels that are not within 'searchRadius' meters of a geometry will be masked out.

Distances are computed on a sphere, so there is a small error proportional to the latitude difference between each pixel and the nearest geometry.

| Usage | Returns |
|---|---|
| `FeatureCollection.distance(*searchRadius*, *maxError*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `features` | FeatureCollection | Feature collection from which to get features used to compute pixel distances. |
| `searchRadius` | Float, default: 100000 | Maximum distance in meters from each pixel to look for edges. Pixels will be masked unless there are edges within this distance. |
| `maxError` | Float, default: 100 | Maximum reprojection error in meters, only used if the input polylines require reprojection. If '0' is provided, then this operation will fail if projection is required. |

## ee.FeatureCollection.distinct

Removes duplicates from a collection. Note that duplicates are determined using a strong hash over the serialized form of the selected properties.

| Usage | Returns |
|---|---|
| `FeatureCollection.distinct(properties)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection from which objects will be selected. |
| `properties` | Object | A property name or a list of property names to use for comparison. The '.geo' property can be included to compare object geometries. |

## ee.FeatureCollection.draw

Paints a vector collection for visualization. Not intended for use as input to other algorithms.

| Usage | Returns |
|---|---|
| `FeatureCollection.draw(color, *pointRadius*, *strokeWidth*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to draw. |
| `color` | String | A hex string in the format RRGGBB specifying the color to use for drawing the features. |
| `pointRadius` | Integer, default: 3 | The radius in pixels of the point markers. |
| `strokeWidth` | Integer, default: 2 | The width in pixels of lines and polygon borders. |

## ee.FeatureCollection.errorMatrix

Computes a 2D error matrix for a collection by comparing two columns of a collection: one containing the actual values, and one containing predicted values. The values are expected to be small contiguous integers, starting from 0. Axis 0 (the rows) of the matrix correspond to the actual values, and Axis 1 (the columns) to the predicted values.

| Usage | Returns |
|---|---|
| `FeatureCollection.errorMatrix(actual, predicted, *order*)` | ConfusionMatrix |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection. |
| `actual` | String | The name of the property containing the actual value. |
| `predicted` | String | The name of the property containing the predicted value. |
| `order` | List, default: null | A list of the expected values. If this argument is not specified, the values are assumed to be contiguous and span the range 0 to maxValue. If specified, only values matching this list are used, and the matrix will have dimensions and order matching this list. |

## ee.FeatureCollection.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `FeatureCollection.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.FeatureCollection.filter

Apply a filter to this collection.

Returns the filtered collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.filter(filter)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `filter` | Filter | A filter to apply to this collection. |

## ee.FeatureCollection.filterBounds

Shortcut to filter a collection by intersection with geometry. Items in the collection with a footprint that fails to intersect the given geometry will be excluded.

This is equivalent to this.filter(ee.Filter.bounds(...)).

> [!CAUTION]
> **Caution:** providing a large or complex collection as the `geometry` argument can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.

Returns the filtered collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.filterBounds(geometry)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `geometry` | ComputedObject\|FeatureCollection\|Geometry | The geometry, feature or collection to intersect with. |

## ee.FeatureCollection.filterDate

Shortcut to filter a collection by a date range. The start and end may be Dates, numbers (interpreted as milliseconds since 1970-01-01T00:00:00Z), or strings (such as '1996-01-01T08:00'). Based on 'system:time_start'.

This is equivalent to this.filter(ee.Filter.date(...)); see the ee.Filter type for other date filtering options.

Returns the filtered collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.filterDate(start, *end*)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `start` | Date\|Number\|String | The start date (inclusive). |
| `end` | Date\|Number\|String, optional | The end date (exclusive). Optional. If not specified, a 1-millisecond range starting at 'start' is created. |

## ee.FeatureCollection.first

Returns the first entry from a given collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.first()` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection from which to select the first entry. |

## ee.FeatureCollection.flatten

Flattens collections of collections.

| Usage | Returns |
|---|---|
| `FeatureCollection.flatten()` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection of collections. |

## ee.FeatureCollection.geometry

Extracts and merges the geometries of a collection. Requires that all the geometries in the collection share the projection and edge interpretation.

> [!CAUTION]
> **Caution:** providing a large or complex collection as input can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection that is required to achieve the desired outcome.

> [!NOTE]
> **Note:** If only a bounding box around the collection is needed, consider using Collection.bounds instead.

| Usage | Returns |
|---|---|
| `FeatureCollection.geometry(*maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection whose geometries will be extracted. |
| `maxError` | ErrorMargin, optional | An error margin to use when merging geometries. |

## ee.FeatureCollection.get

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `FeatureCollection.get(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.FeatureCollection.getArray

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `FeatureCollection.getArray(property)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.FeatureCollection.getDownloadURL

Gets a download URL. When the URL is accessed, the FeatureCollection is downloaded in one of several formats.

Returns a download URL or undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `FeatureCollection.getDownloadURL(*format*, *selectors*, *filename*, *callback*)` | Object\|String |

| Argument | Type | Details |
|---|---|---|
| this: `featurecollection` | FeatureCollection | The FeatureCollection instance. |
| `format` | String, optional | The format of download, one of: "csv", "json", "geojson", "kml", "kmz" ("json" outputs GeoJSON). If unspecified, defaults to "csv". |
| `selectors` | List\[String\]\|String, optional | Feature property names used to select the attributes to be downloaded. If unspecified, all properties are included. |
| `filename` | String, optional | Name of the file to be downloaded; extension is appended by default. If unspecified, defaults to "table". |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.FeatureCollection.getInfo

An imperative function that returns all the known information about this collection via an AJAX call.

Returns a collection description whose fields include:

- features: a list containing metadata about the features in the collection.

- properties: an optional dictionary containing the collection's metadata properties.

| Usage | Returns |
|---|---|
| `FeatureCollection.getInfo(*callback*)` | FeatureCollectionDescription\|Object |

| Argument | Type | Details |
|---|---|---|
| this: `featurecollection` | FeatureCollection | The FeatureCollection instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. If supplied, will be called with the first parameter if successful and the second if unsuccessful. |

## ee.FeatureCollection.getMapId

An imperative function that returns a map ID and optional token, suitable for generating a Map overlay.

Returns an object which may be passed to ee.data.getTileUrl or ui.Map.addLayer, including an additional 'image' field, containing a Collection.draw image wrapping a FeatureCollection containing this feature. Undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `FeatureCollection.getMapId(*visParams*, *callback*)` | MapId\|Object |

| Argument | Type | Details |
|---|---|---|
| this: `featurecollection` | FeatureCollection | The FeatureCollection instance. |
| `visParams` | Object, optional | The visualization parameters. Currently only one parameter, 'color', containing an RGB color string is allowed. If visParams is not specified, black ("000000") is used. |
| `callback` | Function, optional | An async callback. |

## ee.FeatureCollection.getNumber

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `FeatureCollection.getNumber(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.FeatureCollection.getString

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `FeatureCollection.getString(property)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.FeatureCollection.inverseDistance

Returns an inverse-distance weighted estimate of the value at each pixel.

| Usage | Returns |
|---|---|
| `FeatureCollection.inverseDistance(range, propertyName, mean, stdDev, *gamma*, *reducer*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | Feature collection to use as source data for the estimation. |
| `range` | Float | Size of the interpolation window (in meters). |
| `propertyName` | String | Name of the numeric property to be estimated. |
| `mean` | Float | Global expected mean. |
| `stdDev` | Float | Global standard deviation. |
| `gamma` | Float, default: 1 | Determines how quickly the estimates tend towards the global mean. |
| `reducer` | Reducer, default: null | Reducer used to collapse the 'propertyName' value of overlapping points into a single value. |

## ee.FeatureCollection.iterate

Applies a user-supplied function to each element of a collection. The user-supplied function is given two arguments: the current element, and the value returned by the previous call to iterate() or the first argument, for the first iteration. The result is the value returned by the final call to the user-supplied function.

Returns the result of the Collection.iterate() call.

| Usage | Returns |
|---|---|
| `FeatureCollection.iterate(algorithm, *first*)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `algorithm` | Function | The function to apply to each element. Must take two arguments: an element of the collection and the value from the previous iteration. |
| `first` | Object, optional | The initial state. |

## ee.FeatureCollection.kriging

Returns the results of sampling a Kriging estimator at each pixel.

| Usage | Returns |
|---|---|
| `FeatureCollection.kriging(propertyName, shape, range, sill, nugget, *maxDistance*, *reducer*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | Feature collection to use as source data for the estimation. |
| `propertyName` | String | Property to be estimated (must be numeric). |
| `shape` | String | Semivariogram shape (one of {exponential, gaussian, spherical}). |
| `range` | Float | Semivariogram range, in meters. |
| `sill` | Float | Semivariogram sill. |
| `nugget` | Float | Semivariogram nugget. |
| `maxDistance` | Float, default: null | Radius which determines which features are included in each pixel's computation, in meters. Defaults to the semivariogram's range. |
| `reducer` | Reducer, default: null | Reducer used to collapse the 'propertyName' value of overlapping points into a single value. |

## ee.FeatureCollection.limit

Limit a collection to the specified number of elements, optionally sorting them by a specified property first.

Returns the limited collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.limit(max, *property*, *ascending*)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `max` | Number | The number to limit the collection to. |
| `property` | String, optional | The property to sort by, if sorting. |
| `ascending` | Boolean, optional | Whether to sort in ascending or descending order. The default is true (ascending). |

## ee.FeatureCollection.loadBigQueryTable

Reads data from a BigQuery table and presents the results as a FeatureCollection.

| Usage | Returns |
|---|---|
| `ee.FeatureCollection.loadBigQueryTable(table, *geometryColumn*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| `table` | String | Path to BigQuery table in a \`project.dataset.table\` format. |
| `geometryColumn` | String, default: null | The name of the column to use as the main feature geometry. If not specified, the first column with GEOGRAPHY type will be used. |

## ee.FeatureCollection.makeArray

Add a 1-D Array to each feature in a collection by combining a list of properties for each feature into a 1-D Array. All of the properties must be numeric values. If a feature doesn't contain all of the named properties, or any of them aren't numeric, the feature will be dropped from the resulting collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.makeArray(properties, *name*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection from which properties will be selected. |
| `properties` | List | The properties to select. |
| `name` | String, default: "array" | The name of the new array property. |

## ee.FeatureCollection.map

Maps an algorithm over a collection.

Returns the mapped collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.map(algorithm, *dropNulls*)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `algorithm` | Function | The operation to map over the images or features of the collection. A JavaScript function that receives an image or features and returns one. The function is called only once and the result is captured as a description, so it cannot perform imperative operations or rely on external state. |
| `dropNulls` | Boolean, optional | If true, the mapped algorithm is allowed to return nulls, and the elements for which it returns nulls will be dropped. |

## ee.FeatureCollection.merge

Merges two collections into one. The result has all the elements that were in either collection.

Elements from the first collection will have IDs prefixed with "1*" and elements from the second collection will have IDs prefixed with "2*".

Note: If many collections need to be merged, consider placing them all in a collection and using FeatureCollection.flatten() instead. Repeated use of FeatureCollection.merge() will result in increasingly long element IDs and reduced performance.

| Usage | Returns |
|---|---|
| `FeatureCollection.merge(collection2)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection1` | FeatureCollection | The first collection to merge. |
| `collection2` | FeatureCollection | The second collection to merge. |

## ee.FeatureCollection.propertyNames

Returns the names of properties on this element.

| Usage | Returns |
|---|---|
| `FeatureCollection.propertyNames()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element |   |

## ee.FeatureCollection.randomColumn

Adds a column of deterministic pseudorandom numbers to a collection. The outputs are double-precision floating point numbers. When using the 'uniform' distribution (default), outputs are in the range of \[0, 1). Using the 'normal' distribution, outputs have μ=0, σ=1, but have no explicit limits.

| Usage | Returns |
|---|---|
| `FeatureCollection.randomColumn(*columnName*, *seed*, *distribution*, *rowKeys*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection to which to add a random column. |
| `columnName` | String, default: "random" | The name of the column to add. |
| `seed` | Long, default: 0 | A seed used when generating the random numbers. |
| `distribution` | String, default: "uniform" | The distribution type of random numbers to produce; one of 'uniform' or 'normal'. |
| `rowKeys` | List, optional | A list of properties that should uniquely and repeatably identify an element of the collection, used to generate the random number. Defaults to \[system:index\]. |

## ee.FeatureCollection.randomPoints

Generates points that are uniformly random in the given geometry. If the geometry is two-dimensional (polygon or multi-polygon) then the returned points are uniformly distributed on the given region of the sphere. If the geometry is one-dimensional (linestrings), the returned points are interpolated uniformly along the geometry's edges. If the geometry has dimension zero (points), the returned points are sampled uniformly from the input points. If a multi-geometry of mixed dimension is given, points are sampled from the component geometries with the highest dimension.

| Usage | Returns |
|---|---|
| `ee.FeatureCollection.randomPoints(region, *points*, *seed*, *maxError*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| `region` | Geometry | The region to generate points for. |
| `points` | Integer, default: 1000 | The number of points to generate. |
| `seed` | Long, default: 0 | A seed for the random number generator. |
| `maxError` | ErrorMargin, optional | The maximum amount of error tolerated when performing any necessary reprojection. |

## ee.FeatureCollection.reduceColumns

Apply a reducer to each element of a collection, using the given selectors to determine the inputs.

Returns a dictionary of results, keyed with the output names.

| Usage | Returns |
|---|---|
| `FeatureCollection.reduceColumns(reducer, selectors, *weightSelectors*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `reducer` | Reducer | The reducer to apply. |
| `selectors` | List | A selector for each input of the reducer. |
| `weightSelectors` | List, default: null | A selector for each weighted input of the reducer. |

## ee.FeatureCollection.reduceToImage

Creates an image from a feature collection by applying a reducer over the selected properties of all the features that intersect each pixel.

| Usage | Returns |
|---|---|
| `FeatureCollection.reduceToImage(properties, reducer)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | Feature collection to intersect with each output pixel. |
| `properties` | List | Properties to select from each feature and pass into the reducer. |
| `reducer` | Reducer | A Reducer to combine the properties of each intersecting feature into a final result to store in the pixel. |

## ee.FeatureCollection.remap

Remaps the value of a specific property in a collection. Takes two parallel lists and maps values found in one to values in the other. Any element with a value that is not specified in the first list is dropped from the output collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.remap(lookupIn, lookupOut, columnName)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to be modified. |
| `lookupIn` | List | The input mapping values. Restricted to strings and integers. |
| `lookupOut` | List | The output mapping values. Must be the same size as lookupIn. |
| `columnName` | String | The name of the property to remap. |

## ee.FeatureCollection.runBigQuery

Runs a BigQuery query, fetches the results and presents the them as a FeatureCollection.

| Usage | Returns |
|---|---|
| `ee.FeatureCollection.runBigQuery(query, *geometryColumn*, *maxBytesBilled*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| `query` | String | GoogleSQL query to perform on the BigQuery resources. |
| `geometryColumn` | String, default: null | The name of the column to use as the main feature geometry. If not specified, the first geometry column will be used. |
| `maxBytesBilled` | Long, default: 100000000000 | Maximum number of bytes billed while processing the query. Any BigQuery job that exceeds this limit will fail and won't be billed. |

## ee.FeatureCollection.select

Select properties from each Feature in a collection. It is also possible to call this function with only string arguments; they will be all be interpreted as propertySelectors (varargs).

Returns the feature collection with selected properties.

| Usage | Returns |
|---|---|
| `FeatureCollection.select(propertySelectors, *newProperties*, *retainGeometry*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `featurecollection` | FeatureCollection | The FeatureCollection instance. |
| `propertySelectors` | List\[String\] | A list of names or regexes specifying the attributes to select. |
| `newProperties` | List\[String\], optional | A list of new names for the output properties. Must match the number of properties selected. |
| `retainGeometry` | Boolean, optional | When false, the result will have a NULL geometry. Defaults to true. |

## ee.FeatureCollection.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `FeatureCollection.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.FeatureCollection.set

Overrides one or more metadata properties of an Element.

Returns the element with the specified properties overridden.

| Usage | Returns |
|---|---|
| `FeatureCollection.set(var_args)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The Element instance. |
| `var_args` | VarArgs\[Object\] | Either a dictionary of properties, or a vararg sequence of properties, e.g. key1, value1, key2, value2, ... |

## ee.FeatureCollection.size

Returns the number of elements in the collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.size()` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to count. |

## ee.FeatureCollection.sort

Sort a collection by the specified property.

Returns the sorted collection.

| Usage | Returns |
|---|---|
| `FeatureCollection.sort(property, *ascending*)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `property` | String | The property to sort by. |
| `ascending` | Boolean, optional | Whether to sort in ascending or descending order. The default is true (ascending). |

## ee.FeatureCollection.style

Draw a vector collection for visualization using a simple style language.

| Usage | Returns |
|---|---|
| `FeatureCollection.style(*color*, *pointSize*, *pointShape*, *width*, *fillColor*, *styleProperty*, *neighborhood*, *lineType*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to draw. |
| `color` | String, default: "black" | A default color (CSS 3.0 color value e.g., 'FF0000' or 'red') to use for drawing the features. Supports opacity (e.g., 'FF000088' for 50% transparent red). |
| `pointSize` | Integer, default: 3 | The default size in pixels of the point markers. |
| `pointShape` | String, default: "circle" | The default shape of the marker to draw at each point location. One of: \`circle\`, \`square\`, \`diamond\`, \`cross\`, \`plus\`, \`pentagram\`, \`hexagram\`, \`triangle\`, \`triangle_up\`, \`triangle_down\`, \`triangle_left\`, \`triangle_right\`, \`pentagon\`, \`hexagon\`, \`star5\`, \`star6\`. This argument also supports these Matlab marker abbreviations: \`o\`, \`s\`, \`d\`, \`x\`, \`+\`, \`p\`, \`h\`, \`\^\`, \`v\`, \`\<\`, \`\>\`. |
| `width` | Float, default: 2 | The default line width for lines and outlines for polygons and point shapes. |
| `fillColor` | String, default: null | The color for filling polygons and point shapes. Defaults to 'color' at 0.66 opacity. |
| `styleProperty` | String, default: null | A per-feature property expected to contain a dictionary. Values in the dictionary override any default values for that feature. |
| `neighborhood` | Integer, default: 5 | If styleProperty is used and any feature has a pointSize or width larger than the defaults, tiling artifacts can occur. Specifies the maximum neighborhood (pointSize + width) needed for any feature. |
| `lineType` | String, default: "solid" | The default line style for lines and outlines of polygons and point shapes. Defaults to 'solid'. One of: solid, dotted, dashed. |

## ee.FeatureCollection.toDictionary

Extract properties from a feature as a dictionary.

| Usage | Returns |
|---|---|
| `FeatureCollection.toDictionary(*properties*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The feature to extract the property from. |
| `properties` | List, default: null | The list of properties to extract. Defaults to all non-system properties. |

## ee.FeatureCollection.toList

Returns the elements of a collection as a list.

| Usage | Returns |
|---|---|
| `FeatureCollection.toList(count, *offset*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection to fetch. |
| `count` | Integer | The maximum number of elements to fetch. |
| `offset` | Integer, default: 0 | The number of elements to discard from the start. If set, (offset + count) elements will be fetched and the first offset elements will be discarded. |

## ee.FeatureCollection.union

Merges all geometries in a given collection into one and returns a collection containing a single feature with only an ID of 'union_result' and a geometry.

| Usage | Returns |
|---|---|
| `FeatureCollection.union(*maxError*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection being merged. |
| `maxError` | ErrorMargin, default: null | The maximum error allowed when performing any necessary reprojections. If not specified, defaults to the error margin requested from the output. |

## ee.Filter

Constructs a new filter. This constructor accepts the following args:

- Another filter.

- A list of filters (which are implicitly ANDed together).

- A ComputedObject returning a filter. Users shouldn't be making these; they're produced by the generator functions below.

| Usage | Returns |
|---|---|
| `ee.Filter(*filter*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `filter` | Filter\|List\[Object\]\|Object, optional | Optional filter to add. |

## ee.Filter.and

Combine two or more filters using boolean AND.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.and(var_args)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `var_args` | VarArgs\[Filter\] | The filters to combine. |

## ee.Filter.area

Returns a filter that passes if the specified geometry has an area within the given range (inclusive).

| Usage | Returns |
|---|---|
| `ee.Filter.area(min, max, *maxError*, *geometrySelector*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `min` | Float | Minimum area in square meters (inclusive). |
| `max` | Float | Maximum area in square meters (inclusive). |
| `maxError` | ErrorMargin, default: null | The maximum allowed error for computing the geometry's area. |
| `geometrySelector` | String, default: null | The name of the geometry property to use for filtering. Leave blank or use '.geo' to operate on the object's geometry. |

## ee.Filter.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Filter.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Filter.bounds

Creates a filter that passes if the object's geometry intersects the given geometry.

> [!CAUTION]
> **Caution:** providing a large or complex collection as the `geometry` argument can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.bounds(geometry, *errorMargin*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `geometry` | ComputedObject\|FeatureCollection\|Geometry | The geometry, feature or collection to intersect with. |
| `errorMargin` | ComputedObject\|Number, optional | An optional error margin. If a number, interpreted as sphere surface meters. |

## ee.Filter.calendarRange

Returns a filter that passes if the object's timestamp falls within the given range of a calendar field. The `month`, `day_of_year`, `day_of_month`, and `day_of_week` are 1-based. Times are assumed to be in UTC. Weeks are assumed to begin on Monday as day 1.

If `end` \< `start` then this tests for `value` \>= `start` OR `value` \<= `end`, to allow for wrapping.

| Usage | Returns |
|---|---|
| `ee.Filter.calendarRange(start, *end*, *field*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `start` | Integer | The start of the desired calendar field, inclusive. |
| `end` | Integer, default: null | The end of the desired calendar field, inclusive. Defaults to the same value as start. |
| `field` | String, default: "day_of_year" | The calendar field to filter over. Options are: \`year\`, \`month\`, \`hour\`, \`minute\`, \`day_of_year\`, \`day_of_month\`, and \`day_of_week\`. |

## ee.Filter.contains

Creates a unary or binary filter that passes if the left geometry contains the right geometry (empty geometries are not contained in anything).

| Usage | Returns |
|---|---|
| `ee.Filter.contains(*leftField*, *rightValue*, *rightField*, *leftValue*, *maxError*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |
| `maxError` | ErrorMargin, optional | The maximum reprojection error allowed during filter application. |

## ee.Filter.date

Filter a collection by date range. The start and end may be Dates, numbers

(interpreted as milliseconds since 1970-01-01T00:00:00Z), or strings (such as '1996-01-01T08:00'). Based on 'system:time_start' property.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.date(start, *end*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `start` | Date\|Number\|String | The start date (inclusive). |
| `end` | Date\|Number\|String, optional | The end date (exclusive). Optional. If not specified, a 1-millisecond range starting at 'start' is created. |

## ee.Filter.dateRangeContains

Creates a unary or binary filter that passes if the left operand, a date range, contains the right operand, a date.

| Usage | Returns |
|---|---|
| `ee.Filter.dateRangeContains(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.dayOfYear

Returns a filter that passes if the object's timestamp falls within the given day-of-year range.

| Usage | Returns |
|---|---|
| `ee.Filter.dayOfYear(start, end)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `start` | Integer | The start of the desired day range, inclusive. |
| `end` | Integer | The end of the desired day range, inclusive. |

## ee.Filter.disjoint

Creates a unary or binary filter that passes unless the left geometry intersects the right geometry.

| Usage | Returns |
|---|---|
| `ee.Filter.disjoint(*leftField*, *rightValue*, *rightField*, *leftValue*, *maxError*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |
| `maxError` | ErrorMargin, optional | The maximum reprojection error allowed during filter application. |

## ee.Filter.eq

Filter to metadata equal to the given value.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.eq(name, value)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `name` | String | The property name to filter on. |
| `value` | Object | The value to compare against. |

## ee.Filter.equals

Creates a unary or binary filter that passes if the two operands are equals.

| Usage | Returns |
|---|---|
| `ee.Filter.equals(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Filter.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Filter.expression

Constructs a filter tree from a string.

| Usage | Returns |
|---|---|
| `ee.Filter.expression(expression)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `expression` | String | A string to be parsed into a Filter object (e.g., "property \> value"). Supported operators include: \>, \>=, \<, \<=, ==, !=, (), !, \&\&, and \|\|. |

## ee.Filter.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `Filter.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Filter.greaterThan

Creates a unary or binary filter that passes if the left operand is greater than the right operand.

| Usage | Returns |
|---|---|
| `ee.Filter.greaterThan(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.greaterThanOrEquals

Creates a unary or binary filter that passes unless the left operand is less than the right operand.

| Usage | Returns |
|---|---|
| `ee.Filter.greaterThanOrEquals(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.gt

Filter on metadata greater than the given value.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.gt(name, value)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `name` | String | The property name to filter on. |
| `value` | Object | The value to compare against. |

## ee.Filter.gte

Filter on metadata greater than or equal to the given value.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.gte(name, value)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `name` | String | The property name to filter on. |
| `value` | Object | The value to compare against. |

## ee.Filter.hasType

Creates a unary or binary filter that passes if the left operand has the type, or is a subtype of the type named in the right operand.

| Usage | Returns |
|---|---|
| `ee.Filter.hasType(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.inList

Filter on metadata contained in a list.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.inList(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, optional | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | List\[Object\]\|Object, optional | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, optional | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | List\[Object\]\|Object, optional | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.intersects

Creates a unary or binary filter that passes if the left geometry intersects the right geometry.

| Usage | Returns |
|---|---|
| `ee.Filter.intersects(*leftField*, *rightValue*, *rightField*, *leftValue*, *maxError*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |
| `maxError` | ErrorMargin, optional | The maximum reprojection error allowed during filter application. |

## ee.Filter.isContained

Creates a unary or binary filter that passes if the right geometry contains the left geometry (empty geometries are not contained in anything).

| Usage | Returns |
|---|---|
| `ee.Filter.isContained(*leftField*, *rightValue*, *rightField*, *leftValue*, *maxError*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |
| `maxError` | ErrorMargin, optional | The maximum reprojection error allowed during filter application. |

## ee.Filter.lessThan

Creates a unary or binary filter that passes if the left operand is less than the right operand.

| Usage | Returns |
|---|---|
| `ee.Filter.lessThan(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.lessThanOrEquals

Creates a unary or binary filter that passes unless the left operand is greater than the right operand.

| Usage | Returns |
|---|---|
| `ee.Filter.lessThanOrEquals(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.listContains

Creates a unary or binary filter that passes if the left operand, a list, contains the right operand.

| Usage | Returns |
|---|---|
| `ee.Filter.listContains(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.lt

Filter to metadata less than the given value.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.lt(name, value)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `name` | String | The property name to filter on. |
| `value` | Object | The value to compare against. |

## ee.Filter.lte

Filter on metadata less than or equal to the given value.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.lte(name, value)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `name` | String | The property name to filter on. |
| `value` | Object | The value to compare against. |

## ee.Filter.maxDifference

Creates a unary or binary filter that passes if the left and right operands, both numbers, are within a given maximum difference. If used as a join condition, this numeric difference is used as a join measure.

| Usage | Returns |
|---|---|
| `ee.Filter.maxDifference(difference, *leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `difference` | Float | The maximum difference for which the filter will return true. |
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.neq

Filter to metadata not equal to the given value.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.neq(name, value)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `name` | String | The property name to filter on. |
| `value` | Object | The value to compare against. |

## ee.Filter.not

Returns the opposite of the input filter, i.e. the resulting filter will match if and only if the input filter doesn't match.

| Usage | Returns |
|---|---|
| `Filter.not()` | Filter |

| Argument | Type | Details |
|---|---|---|
| this: `filter` | Filter | The Filter instance. |

## ee.Filter.notEquals

Creates a unary or binary filter that passes unless the two operands are equals.

| Usage | Returns |
|---|---|
| `ee.Filter.notEquals(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.notNull

Returns a filter that passes if all the named properties are not null.

| Usage | Returns |
|---|---|
| `ee.Filter.notNull(properties)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `properties` | List |   |

## ee.Filter.or

Combine two or more filters using boolean OR.

Returns the constructed filter.

| Usage | Returns |
|---|---|
| `ee.Filter.or(var_args)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `var_args` | VarArgs\[Filter\] | The filters to combine. |

## ee.Filter.rangeContains

Returns a filter that passes if the value of the selected field is in the specified range (inclusive).

| Usage | Returns |
|---|---|
| `ee.Filter.rangeContains(field, minValue, maxValue)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `field` | String | A selector for the property being tested. |
| `minValue` | Object | The lower bound of the range. |
| `maxValue` | Object | The upper bound of the range. |

## ee.Filter.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Filter.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Filter.stringContains

Creates a unary or binary filter that passes if the left operand, a string, contains the right operand, also a string.

| Usage | Returns |
|---|---|
| `ee.Filter.stringContains(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.stringEndsWith

Creates a unary or binary filter that passes if the left operand, a string, ends with the right operand, also a string.

| Usage | Returns |
|---|---|
| `ee.Filter.stringEndsWith(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.stringStartsWith

Creates a unary or binary filter that passes if the left operand, a string, starts with the right operand, also a string.

| Usage | Returns |
|---|---|
| `ee.Filter.stringStartsWith(*leftField*, *rightValue*, *rightField*, *leftValue*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |

## ee.Filter.withinDistance

Creates a unary or binary filter that passes if the left geometry is within a specified distance of the right geometry. If used as a join condition, this distance is used as a join measure.

| Usage | Returns |
|---|---|
| `ee.Filter.withinDistance(distance, *leftField*, *rightValue*, *rightField*, *leftValue*, *maxError*)` | Filter |

| Argument | Type | Details |
|---|---|---|
| `distance` | Float | The maximum distance for which the filter will return true. |
| `leftField` | String, default: null | A selector for the left operand. Should not be specified if leftValue is specified. |
| `rightValue` | Object, default: null | The value of the right operand. Should not be specified if rightField is specified. |
| `rightField` | String, default: null | A selector for the right operand. Should not be specified if rightValue is specified. |
| `leftValue` | Object, default: null | The value of the left operand. Should not be specified if leftField is specified. |
| `maxError` | ErrorMargin, optional | The maximum reprojection error allowed during filter application. |

## ee.Join.apply

Joins two collections.

| Usage | Returns |
|---|---|
| `Join.apply(primary, secondary, condition)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `join` | Join | The join to apply; determines how the results are constructed. |
| `primary` | FeatureCollection | The primary collection. |
| `secondary` | FeatureCollection | The secondary collection. |
| `condition` | Filter | The join condition used to select the matches from the two collections. |

## ee.Join.inner

Returns a join that pairs elements from the primary collection with matching elements from the secondary collection. Each result has a 'primary' property that contains the element from the primary collection, and a 'secondary' property containing the matching element from the secondary collection. If measureKey is specified, the join measure is also attached to the object as a property.

| Usage | Returns |
|---|---|
| `ee.Join.inner(*primaryKey*, *secondaryKey*, *measureKey*)` | Join |

| Argument | Type | Details |
|---|---|---|
| `primaryKey` | String, default: "primary" | The property name used to save the primary match. |
| `secondaryKey` | String, default: "secondary" | The property name used to save the secondary match. |
| `measureKey` | String, default: null | An optional property name used to save the measure of the join condition. |

## ee.Join.inverted

Returns a join that produces the elements of the primary collection that match no elements of the secondary collection. No properties are added to the results.

| Usage | Returns |
|---|---|
| `ee.Join.inverted()` | Join |

**No arguments.**

## ee.Join.saveAll

Returns a join that pairs each element from the first collection with a group of matching elements from the second collection. The list of matches is added to each result as an additional property. If measureKey is specified, each match has the value of its join measure attached.

Join measures are produced when withinDistance or maxDifference filters are used as the join condition.

| Usage | Returns |
|---|---|
| `ee.Join.saveAll(matchesKey, *ordering*, *ascending*, *measureKey*, *outer*)` | Join |

| Argument | Type | Details |
|---|---|---|
| `matchesKey` | String | The property name used to save the matches list. |
| `ordering` | String, default: null | The property on which to sort the matches list. |
| `ascending` | Boolean, default: true | Whether the ordering is ascending. |
| `measureKey` | String, default: null | An optional property name used to save the measure of the join condition on each match. |
| `outer` | Boolean, default: false | If true, primary rows without matches will be included in the result. |

## ee.Join.saveBest

Returns a join that pairs each element from the first collection with a matching element from the second collection. The match with the best join measure is added to each result as an additional property.

Join measures are produced when withinDistance or maxDifference filters are used as the join condition.

| Usage | Returns |
|---|---|
| `ee.Join.saveBest(matchKey, measureKey, *outer*)` | Join |

| Argument | Type | Details |
|---|---|---|
| `matchKey` | String | The key used to save the match. |
| `measureKey` | String | The key used to save the measure of the join condition on the match. |
| `outer` | Boolean, default: false | If true, primary rows without matches will be included in the result. |

## ee.Join.saveFirst

Returns a join that pairs each element from the first collection with a matching element from the second collection. The first match is added to the result as an additional property.

| Usage | Returns |
|---|---|
| `ee.Join.saveFirst(matchKey, *ordering*, *ascending*, *measureKey*, *outer*)` | Join |

| Argument | Type | Details |
|---|---|---|
| `matchKey` | String | The property name used to save the match. |
| `ordering` | String, default: null | The property on which to sort the matches before selecting the first. |
| `ascending` | Boolean, default: true | Whether the ordering is ascending. |
| `measureKey` | String, default: null | An optional property name used to save the measure of the join condition on the match. |
| `outer` | Boolean, default: false | If true, primary rows without matches will be included in the result. |

## ee.Join.simple

Returns a join that produces the elements of the primary collection that match any element of the secondary collection. No properties are added to the results.

| Usage | Returns |
|---|---|
| `ee.Join.simple()` | Join |

**No arguments.**

