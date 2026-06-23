# Geometria — ee.Geometry, construtores, projeções

> 402 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.Algorithms.GeometryConstructors.BBox`](#ee-algorithms-geometryconstructors-bbox)
- [`ee.Algorithms.GeometryConstructors.LineString`](#ee-algorithms-geometryconstructors-linestring)
- [`ee.Algorithms.GeometryConstructors.LinearRing`](#ee-algorithms-geometryconstructors-linearring)
- [`ee.Algorithms.GeometryConstructors.MultiGeometry`](#ee-algorithms-geometryconstructors-multigeometry)
- [`ee.Algorithms.GeometryConstructors.MultiLineString`](#ee-algorithms-geometryconstructors-multilinestring)
- [`ee.Algorithms.GeometryConstructors.MultiPoint`](#ee-algorithms-geometryconstructors-multipoint)
- [`ee.Algorithms.GeometryConstructors.MultiPolygon`](#ee-algorithms-geometryconstructors-multipolygon)
- [`ee.Algorithms.GeometryConstructors.Point`](#ee-algorithms-geometryconstructors-point)
- [`ee.Algorithms.GeometryConstructors.Polygon`](#ee-algorithms-geometryconstructors-polygon)
- [`ee.Algorithms.GeometryConstructors.Rectangle`](#ee-algorithms-geometryconstructors-rectangle)
- [`ee.ErrorMargin`](#ee-errormargin)
- [`ee.Geometry`](#ee-geometry)
- [`ee.Geometry.BBox`](#ee-geometry-bbox)
- [`ee.Geometry.BBox.area`](#ee-geometry-bbox-area)
- [`ee.Geometry.BBox.aside`](#ee-geometry-bbox-aside)
- [`ee.Geometry.BBox.bounds`](#ee-geometry-bbox-bounds)
- [`ee.Geometry.BBox.buffer`](#ee-geometry-bbox-buffer)
- [`ee.Geometry.BBox.centroid`](#ee-geometry-bbox-centroid)
- [`ee.Geometry.BBox.closestPoint`](#ee-geometry-bbox-closestpoint)
- [`ee.Geometry.BBox.closestPoints`](#ee-geometry-bbox-closestpoints)
- [`ee.Geometry.BBox.containedIn`](#ee-geometry-bbox-containedin)
- [`ee.Geometry.BBox.contains`](#ee-geometry-bbox-contains)
- [`ee.Geometry.BBox.convexHull`](#ee-geometry-bbox-convexhull)
- [`ee.Geometry.BBox.coordinates`](#ee-geometry-bbox-coordinates)
- [`ee.Geometry.BBox.coveringGrid`](#ee-geometry-bbox-coveringgrid)
- [`ee.Geometry.BBox.cutLines`](#ee-geometry-bbox-cutlines)
- [`ee.Geometry.BBox.difference`](#ee-geometry-bbox-difference)
- [`ee.Geometry.BBox.disjoint`](#ee-geometry-bbox-disjoint)
- [`ee.Geometry.BBox.dissolve`](#ee-geometry-bbox-dissolve)
- [`ee.Geometry.BBox.distance`](#ee-geometry-bbox-distance)
- [`ee.Geometry.BBox.edgesAreGeodesics`](#ee-geometry-bbox-edgesaregeodesics)
- [`ee.Geometry.BBox.evaluate`](#ee-geometry-bbox-evaluate)
- [`ee.Geometry.BBox.geodesic`](#ee-geometry-bbox-geodesic)
- [`ee.Geometry.BBox.geometries`](#ee-geometry-bbox-geometries)
- [`ee.Geometry.BBox.getInfo`](#ee-geometry-bbox-getinfo)
- [`ee.Geometry.BBox.intersection`](#ee-geometry-bbox-intersection)
- [`ee.Geometry.BBox.intersects`](#ee-geometry-bbox-intersects)
- [`ee.Geometry.BBox.isUnbounded`](#ee-geometry-bbox-isunbounded)
- [`ee.Geometry.BBox.length`](#ee-geometry-bbox-length)
- [`ee.Geometry.BBox.perimeter`](#ee-geometry-bbox-perimeter)
- [`ee.Geometry.BBox.projection`](#ee-geometry-bbox-projection)
- [`ee.Geometry.BBox.serialize`](#ee-geometry-bbox-serialize)
- [`ee.Geometry.BBox.simplify`](#ee-geometry-bbox-simplify)
- [`ee.Geometry.BBox.symmetricDifference`](#ee-geometry-bbox-symmetricdifference)
- [`ee.Geometry.BBox.toGeoJSON`](#ee-geometry-bbox-togeojson)
- [`ee.Geometry.BBox.toGeoJSONString`](#ee-geometry-bbox-togeojsonstring)
- [`ee.Geometry.BBox.transform`](#ee-geometry-bbox-transform)
- [`ee.Geometry.BBox.type`](#ee-geometry-bbox-type)
- [`ee.Geometry.BBox.union`](#ee-geometry-bbox-union)
- [`ee.Geometry.BBox.withinDistance`](#ee-geometry-bbox-withindistance)
- [`ee.Geometry.LineString`](#ee-geometry-linestring)
- [`ee.Geometry.LineString.area`](#ee-geometry-linestring-area)
- [`ee.Geometry.LineString.aside`](#ee-geometry-linestring-aside)
- [`ee.Geometry.LineString.bounds`](#ee-geometry-linestring-bounds)
- [`ee.Geometry.LineString.buffer`](#ee-geometry-linestring-buffer)
- [`ee.Geometry.LineString.centroid`](#ee-geometry-linestring-centroid)
- [`ee.Geometry.LineString.closestPoint`](#ee-geometry-linestring-closestpoint)
- [`ee.Geometry.LineString.closestPoints`](#ee-geometry-linestring-closestpoints)
- [`ee.Geometry.LineString.containedIn`](#ee-geometry-linestring-containedin)
- [`ee.Geometry.LineString.contains`](#ee-geometry-linestring-contains)
- [`ee.Geometry.LineString.convexHull`](#ee-geometry-linestring-convexhull)
- [`ee.Geometry.LineString.coordinates`](#ee-geometry-linestring-coordinates)
- [`ee.Geometry.LineString.coveringGrid`](#ee-geometry-linestring-coveringgrid)
- [`ee.Geometry.LineString.cutLines`](#ee-geometry-linestring-cutlines)
- [`ee.Geometry.LineString.difference`](#ee-geometry-linestring-difference)
- [`ee.Geometry.LineString.disjoint`](#ee-geometry-linestring-disjoint)
- [`ee.Geometry.LineString.dissolve`](#ee-geometry-linestring-dissolve)
- [`ee.Geometry.LineString.distance`](#ee-geometry-linestring-distance)
- [`ee.Geometry.LineString.edgesAreGeodesics`](#ee-geometry-linestring-edgesaregeodesics)
- [`ee.Geometry.LineString.evaluate`](#ee-geometry-linestring-evaluate)
- [`ee.Geometry.LineString.geodesic`](#ee-geometry-linestring-geodesic)
- [`ee.Geometry.LineString.geometries`](#ee-geometry-linestring-geometries)
- [`ee.Geometry.LineString.getInfo`](#ee-geometry-linestring-getinfo)
- [`ee.Geometry.LineString.intersection`](#ee-geometry-linestring-intersection)
- [`ee.Geometry.LineString.intersects`](#ee-geometry-linestring-intersects)
- [`ee.Geometry.LineString.isUnbounded`](#ee-geometry-linestring-isunbounded)
- [`ee.Geometry.LineString.length`](#ee-geometry-linestring-length)
- [`ee.Geometry.LineString.perimeter`](#ee-geometry-linestring-perimeter)
- [`ee.Geometry.LineString.projection`](#ee-geometry-linestring-projection)
- [`ee.Geometry.LineString.serialize`](#ee-geometry-linestring-serialize)
- [`ee.Geometry.LineString.simplify`](#ee-geometry-linestring-simplify)
- [`ee.Geometry.LineString.symmetricDifference`](#ee-geometry-linestring-symmetricdifference)
- [`ee.Geometry.LineString.toGeoJSON`](#ee-geometry-linestring-togeojson)
- [`ee.Geometry.LineString.toGeoJSONString`](#ee-geometry-linestring-togeojsonstring)
- [`ee.Geometry.LineString.transform`](#ee-geometry-linestring-transform)
- [`ee.Geometry.LineString.type`](#ee-geometry-linestring-type)
- [`ee.Geometry.LineString.union`](#ee-geometry-linestring-union)
- [`ee.Geometry.LineString.withinDistance`](#ee-geometry-linestring-withindistance)
- [`ee.Geometry.LinearRing`](#ee-geometry-linearring)
- [`ee.Geometry.LinearRing.area`](#ee-geometry-linearring-area)
- [`ee.Geometry.LinearRing.aside`](#ee-geometry-linearring-aside)
- [`ee.Geometry.LinearRing.bounds`](#ee-geometry-linearring-bounds)
- [`ee.Geometry.LinearRing.buffer`](#ee-geometry-linearring-buffer)
- [`ee.Geometry.LinearRing.centroid`](#ee-geometry-linearring-centroid)
- [`ee.Geometry.LinearRing.closestPoint`](#ee-geometry-linearring-closestpoint)
- [`ee.Geometry.LinearRing.closestPoints`](#ee-geometry-linearring-closestpoints)
- [`ee.Geometry.LinearRing.containedIn`](#ee-geometry-linearring-containedin)
- [`ee.Geometry.LinearRing.contains`](#ee-geometry-linearring-contains)
- [`ee.Geometry.LinearRing.convexHull`](#ee-geometry-linearring-convexhull)
- [`ee.Geometry.LinearRing.coordinates`](#ee-geometry-linearring-coordinates)
- [`ee.Geometry.LinearRing.coveringGrid`](#ee-geometry-linearring-coveringgrid)
- [`ee.Geometry.LinearRing.cutLines`](#ee-geometry-linearring-cutlines)
- [`ee.Geometry.LinearRing.difference`](#ee-geometry-linearring-difference)
- [`ee.Geometry.LinearRing.disjoint`](#ee-geometry-linearring-disjoint)
- [`ee.Geometry.LinearRing.dissolve`](#ee-geometry-linearring-dissolve)
- [`ee.Geometry.LinearRing.distance`](#ee-geometry-linearring-distance)
- [`ee.Geometry.LinearRing.edgesAreGeodesics`](#ee-geometry-linearring-edgesaregeodesics)
- [`ee.Geometry.LinearRing.evaluate`](#ee-geometry-linearring-evaluate)
- [`ee.Geometry.LinearRing.geodesic`](#ee-geometry-linearring-geodesic)
- [`ee.Geometry.LinearRing.geometries`](#ee-geometry-linearring-geometries)
- [`ee.Geometry.LinearRing.getInfo`](#ee-geometry-linearring-getinfo)
- [`ee.Geometry.LinearRing.intersection`](#ee-geometry-linearring-intersection)
- [`ee.Geometry.LinearRing.intersects`](#ee-geometry-linearring-intersects)
- [`ee.Geometry.LinearRing.isUnbounded`](#ee-geometry-linearring-isunbounded)
- [`ee.Geometry.LinearRing.length`](#ee-geometry-linearring-length)
- [`ee.Geometry.LinearRing.perimeter`](#ee-geometry-linearring-perimeter)
- [`ee.Geometry.LinearRing.projection`](#ee-geometry-linearring-projection)
- [`ee.Geometry.LinearRing.serialize`](#ee-geometry-linearring-serialize)
- [`ee.Geometry.LinearRing.simplify`](#ee-geometry-linearring-simplify)
- [`ee.Geometry.LinearRing.symmetricDifference`](#ee-geometry-linearring-symmetricdifference)
- [`ee.Geometry.LinearRing.toGeoJSON`](#ee-geometry-linearring-togeojson)
- [`ee.Geometry.LinearRing.toGeoJSONString`](#ee-geometry-linearring-togeojsonstring)
- [`ee.Geometry.LinearRing.transform`](#ee-geometry-linearring-transform)
- [`ee.Geometry.LinearRing.type`](#ee-geometry-linearring-type)
- [`ee.Geometry.LinearRing.union`](#ee-geometry-linearring-union)
- [`ee.Geometry.LinearRing.withinDistance`](#ee-geometry-linearring-withindistance)
- [`ee.Geometry.MultiLineString`](#ee-geometry-multilinestring)
- [`ee.Geometry.MultiLineString.area`](#ee-geometry-multilinestring-area)
- [`ee.Geometry.MultiLineString.aside`](#ee-geometry-multilinestring-aside)
- [`ee.Geometry.MultiLineString.bounds`](#ee-geometry-multilinestring-bounds)
- [`ee.Geometry.MultiLineString.buffer`](#ee-geometry-multilinestring-buffer)
- [`ee.Geometry.MultiLineString.centroid`](#ee-geometry-multilinestring-centroid)
- [`ee.Geometry.MultiLineString.closestPoint`](#ee-geometry-multilinestring-closestpoint)
- [`ee.Geometry.MultiLineString.closestPoints`](#ee-geometry-multilinestring-closestpoints)
- [`ee.Geometry.MultiLineString.containedIn`](#ee-geometry-multilinestring-containedin)
- [`ee.Geometry.MultiLineString.contains`](#ee-geometry-multilinestring-contains)
- [`ee.Geometry.MultiLineString.convexHull`](#ee-geometry-multilinestring-convexhull)
- [`ee.Geometry.MultiLineString.coordinates`](#ee-geometry-multilinestring-coordinates)
- [`ee.Geometry.MultiLineString.coveringGrid`](#ee-geometry-multilinestring-coveringgrid)
- [`ee.Geometry.MultiLineString.cutLines`](#ee-geometry-multilinestring-cutlines)
- [`ee.Geometry.MultiLineString.difference`](#ee-geometry-multilinestring-difference)
- [`ee.Geometry.MultiLineString.disjoint`](#ee-geometry-multilinestring-disjoint)
- [`ee.Geometry.MultiLineString.dissolve`](#ee-geometry-multilinestring-dissolve)
- [`ee.Geometry.MultiLineString.distance`](#ee-geometry-multilinestring-distance)
- [`ee.Geometry.MultiLineString.edgesAreGeodesics`](#ee-geometry-multilinestring-edgesaregeodesics)
- [`ee.Geometry.MultiLineString.evaluate`](#ee-geometry-multilinestring-evaluate)
- [`ee.Geometry.MultiLineString.geodesic`](#ee-geometry-multilinestring-geodesic)
- [`ee.Geometry.MultiLineString.geometries`](#ee-geometry-multilinestring-geometries)
- [`ee.Geometry.MultiLineString.getInfo`](#ee-geometry-multilinestring-getinfo)
- [`ee.Geometry.MultiLineString.intersection`](#ee-geometry-multilinestring-intersection)
- [`ee.Geometry.MultiLineString.intersects`](#ee-geometry-multilinestring-intersects)
- [`ee.Geometry.MultiLineString.isUnbounded`](#ee-geometry-multilinestring-isunbounded)
- [`ee.Geometry.MultiLineString.length`](#ee-geometry-multilinestring-length)
- [`ee.Geometry.MultiLineString.perimeter`](#ee-geometry-multilinestring-perimeter)
- [`ee.Geometry.MultiLineString.projection`](#ee-geometry-multilinestring-projection)
- [`ee.Geometry.MultiLineString.serialize`](#ee-geometry-multilinestring-serialize)
- [`ee.Geometry.MultiLineString.simplify`](#ee-geometry-multilinestring-simplify)
- [`ee.Geometry.MultiLineString.symmetricDifference`](#ee-geometry-multilinestring-symmetricdifference)
- [`ee.Geometry.MultiLineString.toGeoJSON`](#ee-geometry-multilinestring-togeojson)
- [`ee.Geometry.MultiLineString.toGeoJSONString`](#ee-geometry-multilinestring-togeojsonstring)
- [`ee.Geometry.MultiLineString.transform`](#ee-geometry-multilinestring-transform)
- [`ee.Geometry.MultiLineString.type`](#ee-geometry-multilinestring-type)
- [`ee.Geometry.MultiLineString.union`](#ee-geometry-multilinestring-union)
- [`ee.Geometry.MultiLineString.withinDistance`](#ee-geometry-multilinestring-withindistance)
- [`ee.Geometry.MultiPoint`](#ee-geometry-multipoint)
- [`ee.Geometry.MultiPoint.area`](#ee-geometry-multipoint-area)
- [`ee.Geometry.MultiPoint.aside`](#ee-geometry-multipoint-aside)
- [`ee.Geometry.MultiPoint.bounds`](#ee-geometry-multipoint-bounds)
- [`ee.Geometry.MultiPoint.buffer`](#ee-geometry-multipoint-buffer)
- [`ee.Geometry.MultiPoint.centroid`](#ee-geometry-multipoint-centroid)
- [`ee.Geometry.MultiPoint.closestPoint`](#ee-geometry-multipoint-closestpoint)
- [`ee.Geometry.MultiPoint.closestPoints`](#ee-geometry-multipoint-closestpoints)
- [`ee.Geometry.MultiPoint.containedIn`](#ee-geometry-multipoint-containedin)
- [`ee.Geometry.MultiPoint.contains`](#ee-geometry-multipoint-contains)
- [`ee.Geometry.MultiPoint.convexHull`](#ee-geometry-multipoint-convexhull)
- [`ee.Geometry.MultiPoint.coordinates`](#ee-geometry-multipoint-coordinates)
- [`ee.Geometry.MultiPoint.coveringGrid`](#ee-geometry-multipoint-coveringgrid)
- [`ee.Geometry.MultiPoint.cutLines`](#ee-geometry-multipoint-cutlines)
- [`ee.Geometry.MultiPoint.difference`](#ee-geometry-multipoint-difference)
- [`ee.Geometry.MultiPoint.disjoint`](#ee-geometry-multipoint-disjoint)
- [`ee.Geometry.MultiPoint.dissolve`](#ee-geometry-multipoint-dissolve)
- [`ee.Geometry.MultiPoint.distance`](#ee-geometry-multipoint-distance)
- [`ee.Geometry.MultiPoint.edgesAreGeodesics`](#ee-geometry-multipoint-edgesaregeodesics)
- [`ee.Geometry.MultiPoint.evaluate`](#ee-geometry-multipoint-evaluate)
- [`ee.Geometry.MultiPoint.geodesic`](#ee-geometry-multipoint-geodesic)
- [`ee.Geometry.MultiPoint.geometries`](#ee-geometry-multipoint-geometries)
- [`ee.Geometry.MultiPoint.getInfo`](#ee-geometry-multipoint-getinfo)
- [`ee.Geometry.MultiPoint.intersection`](#ee-geometry-multipoint-intersection)
- [`ee.Geometry.MultiPoint.intersects`](#ee-geometry-multipoint-intersects)
- [`ee.Geometry.MultiPoint.isUnbounded`](#ee-geometry-multipoint-isunbounded)
- [`ee.Geometry.MultiPoint.length`](#ee-geometry-multipoint-length)
- [`ee.Geometry.MultiPoint.perimeter`](#ee-geometry-multipoint-perimeter)
- [`ee.Geometry.MultiPoint.projection`](#ee-geometry-multipoint-projection)
- [`ee.Geometry.MultiPoint.serialize`](#ee-geometry-multipoint-serialize)
- [`ee.Geometry.MultiPoint.simplify`](#ee-geometry-multipoint-simplify)
- [`ee.Geometry.MultiPoint.symmetricDifference`](#ee-geometry-multipoint-symmetricdifference)
- [`ee.Geometry.MultiPoint.toGeoJSON`](#ee-geometry-multipoint-togeojson)
- [`ee.Geometry.MultiPoint.toGeoJSONString`](#ee-geometry-multipoint-togeojsonstring)
- [`ee.Geometry.MultiPoint.transform`](#ee-geometry-multipoint-transform)
- [`ee.Geometry.MultiPoint.type`](#ee-geometry-multipoint-type)
- [`ee.Geometry.MultiPoint.union`](#ee-geometry-multipoint-union)
- [`ee.Geometry.MultiPoint.withinDistance`](#ee-geometry-multipoint-withindistance)
- [`ee.Geometry.MultiPolygon`](#ee-geometry-multipolygon)
- [`ee.Geometry.MultiPolygon.area`](#ee-geometry-multipolygon-area)
- [`ee.Geometry.MultiPolygon.aside`](#ee-geometry-multipolygon-aside)
- [`ee.Geometry.MultiPolygon.bounds`](#ee-geometry-multipolygon-bounds)
- [`ee.Geometry.MultiPolygon.buffer`](#ee-geometry-multipolygon-buffer)
- [`ee.Geometry.MultiPolygon.centroid`](#ee-geometry-multipolygon-centroid)
- [`ee.Geometry.MultiPolygon.closestPoint`](#ee-geometry-multipolygon-closestpoint)
- [`ee.Geometry.MultiPolygon.closestPoints`](#ee-geometry-multipolygon-closestpoints)
- [`ee.Geometry.MultiPolygon.containedIn`](#ee-geometry-multipolygon-containedin)
- [`ee.Geometry.MultiPolygon.contains`](#ee-geometry-multipolygon-contains)
- [`ee.Geometry.MultiPolygon.convexHull`](#ee-geometry-multipolygon-convexhull)
- [`ee.Geometry.MultiPolygon.coordinates`](#ee-geometry-multipolygon-coordinates)
- [`ee.Geometry.MultiPolygon.coveringGrid`](#ee-geometry-multipolygon-coveringgrid)
- [`ee.Geometry.MultiPolygon.cutLines`](#ee-geometry-multipolygon-cutlines)
- [`ee.Geometry.MultiPolygon.difference`](#ee-geometry-multipolygon-difference)
- [`ee.Geometry.MultiPolygon.disjoint`](#ee-geometry-multipolygon-disjoint)
- [`ee.Geometry.MultiPolygon.dissolve`](#ee-geometry-multipolygon-dissolve)
- [`ee.Geometry.MultiPolygon.distance`](#ee-geometry-multipolygon-distance)
- [`ee.Geometry.MultiPolygon.edgesAreGeodesics`](#ee-geometry-multipolygon-edgesaregeodesics)
- [`ee.Geometry.MultiPolygon.evaluate`](#ee-geometry-multipolygon-evaluate)
- [`ee.Geometry.MultiPolygon.geodesic`](#ee-geometry-multipolygon-geodesic)
- [`ee.Geometry.MultiPolygon.geometries`](#ee-geometry-multipolygon-geometries)
- [`ee.Geometry.MultiPolygon.getInfo`](#ee-geometry-multipolygon-getinfo)
- [`ee.Geometry.MultiPolygon.intersection`](#ee-geometry-multipolygon-intersection)
- [`ee.Geometry.MultiPolygon.intersects`](#ee-geometry-multipolygon-intersects)
- [`ee.Geometry.MultiPolygon.isUnbounded`](#ee-geometry-multipolygon-isunbounded)
- [`ee.Geometry.MultiPolygon.length`](#ee-geometry-multipolygon-length)
- [`ee.Geometry.MultiPolygon.perimeter`](#ee-geometry-multipolygon-perimeter)
- [`ee.Geometry.MultiPolygon.projection`](#ee-geometry-multipolygon-projection)
- [`ee.Geometry.MultiPolygon.serialize`](#ee-geometry-multipolygon-serialize)
- [`ee.Geometry.MultiPolygon.simplify`](#ee-geometry-multipolygon-simplify)
- [`ee.Geometry.MultiPolygon.symmetricDifference`](#ee-geometry-multipolygon-symmetricdifference)
- [`ee.Geometry.MultiPolygon.toGeoJSON`](#ee-geometry-multipolygon-togeojson)
- [`ee.Geometry.MultiPolygon.toGeoJSONString`](#ee-geometry-multipolygon-togeojsonstring)
- [`ee.Geometry.MultiPolygon.transform`](#ee-geometry-multipolygon-transform)
- [`ee.Geometry.MultiPolygon.type`](#ee-geometry-multipolygon-type)
- [`ee.Geometry.MultiPolygon.union`](#ee-geometry-multipolygon-union)
- [`ee.Geometry.MultiPolygon.withinDistance`](#ee-geometry-multipolygon-withindistance)
- [`ee.Geometry.Point`](#ee-geometry-point)
- [`ee.Geometry.Point.area`](#ee-geometry-point-area)
- [`ee.Geometry.Point.aside`](#ee-geometry-point-aside)
- [`ee.Geometry.Point.bounds`](#ee-geometry-point-bounds)
- [`ee.Geometry.Point.buffer`](#ee-geometry-point-buffer)
- [`ee.Geometry.Point.centroid`](#ee-geometry-point-centroid)
- [`ee.Geometry.Point.closestPoint`](#ee-geometry-point-closestpoint)
- [`ee.Geometry.Point.closestPoints`](#ee-geometry-point-closestpoints)
- [`ee.Geometry.Point.containedIn`](#ee-geometry-point-containedin)
- [`ee.Geometry.Point.contains`](#ee-geometry-point-contains)
- [`ee.Geometry.Point.convexHull`](#ee-geometry-point-convexhull)
- [`ee.Geometry.Point.coordinates`](#ee-geometry-point-coordinates)
- [`ee.Geometry.Point.coveringGrid`](#ee-geometry-point-coveringgrid)
- [`ee.Geometry.Point.cutLines`](#ee-geometry-point-cutlines)
- [`ee.Geometry.Point.difference`](#ee-geometry-point-difference)
- [`ee.Geometry.Point.disjoint`](#ee-geometry-point-disjoint)
- [`ee.Geometry.Point.dissolve`](#ee-geometry-point-dissolve)
- [`ee.Geometry.Point.distance`](#ee-geometry-point-distance)
- [`ee.Geometry.Point.edgesAreGeodesics`](#ee-geometry-point-edgesaregeodesics)
- [`ee.Geometry.Point.evaluate`](#ee-geometry-point-evaluate)
- [`ee.Geometry.Point.geodesic`](#ee-geometry-point-geodesic)
- [`ee.Geometry.Point.geometries`](#ee-geometry-point-geometries)
- [`ee.Geometry.Point.getInfo`](#ee-geometry-point-getinfo)
- [`ee.Geometry.Point.intersection`](#ee-geometry-point-intersection)
- [`ee.Geometry.Point.intersects`](#ee-geometry-point-intersects)
- [`ee.Geometry.Point.isUnbounded`](#ee-geometry-point-isunbounded)
- [`ee.Geometry.Point.length`](#ee-geometry-point-length)
- [`ee.Geometry.Point.perimeter`](#ee-geometry-point-perimeter)
- [`ee.Geometry.Point.projection`](#ee-geometry-point-projection)
- [`ee.Geometry.Point.serialize`](#ee-geometry-point-serialize)
- [`ee.Geometry.Point.simplify`](#ee-geometry-point-simplify)
- [`ee.Geometry.Point.symmetricDifference`](#ee-geometry-point-symmetricdifference)
- [`ee.Geometry.Point.toGeoJSON`](#ee-geometry-point-togeojson)
- [`ee.Geometry.Point.toGeoJSONString`](#ee-geometry-point-togeojsonstring)
- [`ee.Geometry.Point.transform`](#ee-geometry-point-transform)
- [`ee.Geometry.Point.type`](#ee-geometry-point-type)
- [`ee.Geometry.Point.union`](#ee-geometry-point-union)
- [`ee.Geometry.Point.withinDistance`](#ee-geometry-point-withindistance)
- [`ee.Geometry.Polygon`](#ee-geometry-polygon)
- [`ee.Geometry.Polygon.area`](#ee-geometry-polygon-area)
- [`ee.Geometry.Polygon.aside`](#ee-geometry-polygon-aside)
- [`ee.Geometry.Polygon.bounds`](#ee-geometry-polygon-bounds)
- [`ee.Geometry.Polygon.buffer`](#ee-geometry-polygon-buffer)
- [`ee.Geometry.Polygon.centroid`](#ee-geometry-polygon-centroid)
- [`ee.Geometry.Polygon.closestPoint`](#ee-geometry-polygon-closestpoint)
- [`ee.Geometry.Polygon.closestPoints`](#ee-geometry-polygon-closestpoints)
- [`ee.Geometry.Polygon.containedIn`](#ee-geometry-polygon-containedin)
- [`ee.Geometry.Polygon.contains`](#ee-geometry-polygon-contains)
- [`ee.Geometry.Polygon.convexHull`](#ee-geometry-polygon-convexhull)
- [`ee.Geometry.Polygon.coordinates`](#ee-geometry-polygon-coordinates)
- [`ee.Geometry.Polygon.coveringGrid`](#ee-geometry-polygon-coveringgrid)
- [`ee.Geometry.Polygon.cutLines`](#ee-geometry-polygon-cutlines)
- [`ee.Geometry.Polygon.difference`](#ee-geometry-polygon-difference)
- [`ee.Geometry.Polygon.disjoint`](#ee-geometry-polygon-disjoint)
- [`ee.Geometry.Polygon.dissolve`](#ee-geometry-polygon-dissolve)
- [`ee.Geometry.Polygon.distance`](#ee-geometry-polygon-distance)
- [`ee.Geometry.Polygon.edgesAreGeodesics`](#ee-geometry-polygon-edgesaregeodesics)
- [`ee.Geometry.Polygon.evaluate`](#ee-geometry-polygon-evaluate)
- [`ee.Geometry.Polygon.geodesic`](#ee-geometry-polygon-geodesic)
- [`ee.Geometry.Polygon.geometries`](#ee-geometry-polygon-geometries)
- [`ee.Geometry.Polygon.getInfo`](#ee-geometry-polygon-getinfo)
- [`ee.Geometry.Polygon.intersection`](#ee-geometry-polygon-intersection)
- [`ee.Geometry.Polygon.intersects`](#ee-geometry-polygon-intersects)
- [`ee.Geometry.Polygon.isUnbounded`](#ee-geometry-polygon-isunbounded)
- [`ee.Geometry.Polygon.length`](#ee-geometry-polygon-length)
- [`ee.Geometry.Polygon.perimeter`](#ee-geometry-polygon-perimeter)
- [`ee.Geometry.Polygon.projection`](#ee-geometry-polygon-projection)
- [`ee.Geometry.Polygon.serialize`](#ee-geometry-polygon-serialize)
- [`ee.Geometry.Polygon.simplify`](#ee-geometry-polygon-simplify)
- [`ee.Geometry.Polygon.symmetricDifference`](#ee-geometry-polygon-symmetricdifference)
- [`ee.Geometry.Polygon.toGeoJSON`](#ee-geometry-polygon-togeojson)
- [`ee.Geometry.Polygon.toGeoJSONString`](#ee-geometry-polygon-togeojsonstring)
- [`ee.Geometry.Polygon.transform`](#ee-geometry-polygon-transform)
- [`ee.Geometry.Polygon.type`](#ee-geometry-polygon-type)
- [`ee.Geometry.Polygon.union`](#ee-geometry-polygon-union)
- [`ee.Geometry.Polygon.withinDistance`](#ee-geometry-polygon-withindistance)
- [`ee.Geometry.Rectangle`](#ee-geometry-rectangle)
- [`ee.Geometry.Rectangle.area`](#ee-geometry-rectangle-area)
- [`ee.Geometry.Rectangle.aside`](#ee-geometry-rectangle-aside)
- [`ee.Geometry.Rectangle.bounds`](#ee-geometry-rectangle-bounds)
- [`ee.Geometry.Rectangle.buffer`](#ee-geometry-rectangle-buffer)
- [`ee.Geometry.Rectangle.centroid`](#ee-geometry-rectangle-centroid)
- [`ee.Geometry.Rectangle.closestPoint`](#ee-geometry-rectangle-closestpoint)
- [`ee.Geometry.Rectangle.closestPoints`](#ee-geometry-rectangle-closestpoints)
- [`ee.Geometry.Rectangle.containedIn`](#ee-geometry-rectangle-containedin)
- [`ee.Geometry.Rectangle.contains`](#ee-geometry-rectangle-contains)
- [`ee.Geometry.Rectangle.convexHull`](#ee-geometry-rectangle-convexhull)
- [`ee.Geometry.Rectangle.coordinates`](#ee-geometry-rectangle-coordinates)
- [`ee.Geometry.Rectangle.coveringGrid`](#ee-geometry-rectangle-coveringgrid)
- [`ee.Geometry.Rectangle.cutLines`](#ee-geometry-rectangle-cutlines)
- [`ee.Geometry.Rectangle.difference`](#ee-geometry-rectangle-difference)
- [`ee.Geometry.Rectangle.disjoint`](#ee-geometry-rectangle-disjoint)
- [`ee.Geometry.Rectangle.dissolve`](#ee-geometry-rectangle-dissolve)
- [`ee.Geometry.Rectangle.distance`](#ee-geometry-rectangle-distance)
- [`ee.Geometry.Rectangle.edgesAreGeodesics`](#ee-geometry-rectangle-edgesaregeodesics)
- [`ee.Geometry.Rectangle.evaluate`](#ee-geometry-rectangle-evaluate)
- [`ee.Geometry.Rectangle.geodesic`](#ee-geometry-rectangle-geodesic)
- [`ee.Geometry.Rectangle.geometries`](#ee-geometry-rectangle-geometries)
- [`ee.Geometry.Rectangle.getInfo`](#ee-geometry-rectangle-getinfo)
- [`ee.Geometry.Rectangle.intersection`](#ee-geometry-rectangle-intersection)
- [`ee.Geometry.Rectangle.intersects`](#ee-geometry-rectangle-intersects)
- [`ee.Geometry.Rectangle.isUnbounded`](#ee-geometry-rectangle-isunbounded)
- [`ee.Geometry.Rectangle.length`](#ee-geometry-rectangle-length)
- [`ee.Geometry.Rectangle.perimeter`](#ee-geometry-rectangle-perimeter)
- [`ee.Geometry.Rectangle.projection`](#ee-geometry-rectangle-projection)
- [`ee.Geometry.Rectangle.serialize`](#ee-geometry-rectangle-serialize)
- [`ee.Geometry.Rectangle.simplify`](#ee-geometry-rectangle-simplify)
- [`ee.Geometry.Rectangle.symmetricDifference`](#ee-geometry-rectangle-symmetricdifference)
- [`ee.Geometry.Rectangle.toGeoJSON`](#ee-geometry-rectangle-togeojson)
- [`ee.Geometry.Rectangle.toGeoJSONString`](#ee-geometry-rectangle-togeojsonstring)
- [`ee.Geometry.Rectangle.transform`](#ee-geometry-rectangle-transform)
- [`ee.Geometry.Rectangle.type`](#ee-geometry-rectangle-type)
- [`ee.Geometry.Rectangle.union`](#ee-geometry-rectangle-union)
- [`ee.Geometry.Rectangle.withinDistance`](#ee-geometry-rectangle-withindistance)
- [`ee.Geometry.area`](#ee-geometry-area)
- [`ee.Geometry.aside`](#ee-geometry-aside)
- [`ee.Geometry.bounds`](#ee-geometry-bounds)
- [`ee.Geometry.buffer`](#ee-geometry-buffer)
- [`ee.Geometry.centroid`](#ee-geometry-centroid)
- [`ee.Geometry.closestPoint`](#ee-geometry-closestpoint)
- [`ee.Geometry.closestPoints`](#ee-geometry-closestpoints)
- [`ee.Geometry.containedIn`](#ee-geometry-containedin)
- [`ee.Geometry.contains`](#ee-geometry-contains)
- [`ee.Geometry.convexHull`](#ee-geometry-convexhull)
- [`ee.Geometry.coordinates`](#ee-geometry-coordinates)
- [`ee.Geometry.coveringGrid`](#ee-geometry-coveringgrid)
- [`ee.Geometry.cutLines`](#ee-geometry-cutlines)
- [`ee.Geometry.difference`](#ee-geometry-difference)
- [`ee.Geometry.disjoint`](#ee-geometry-disjoint)
- [`ee.Geometry.dissolve`](#ee-geometry-dissolve)
- [`ee.Geometry.distance`](#ee-geometry-distance)
- [`ee.Geometry.edgesAreGeodesics`](#ee-geometry-edgesaregeodesics)
- [`ee.Geometry.evaluate`](#ee-geometry-evaluate)
- [`ee.Geometry.fromS2CellId`](#ee-geometry-froms2cellid)
- [`ee.Geometry.fromS2CellToken`](#ee-geometry-froms2celltoken)
- [`ee.Geometry.geodesic`](#ee-geometry-geodesic)
- [`ee.Geometry.geometries`](#ee-geometry-geometries)
- [`ee.Geometry.getInfo`](#ee-geometry-getinfo)
- [`ee.Geometry.intersection`](#ee-geometry-intersection)
- [`ee.Geometry.intersects`](#ee-geometry-intersects)
- [`ee.Geometry.isUnbounded`](#ee-geometry-isunbounded)
- [`ee.Geometry.length`](#ee-geometry-length)
- [`ee.Geometry.perimeter`](#ee-geometry-perimeter)
- [`ee.Geometry.projection`](#ee-geometry-projection)
- [`ee.Geometry.s2Cell`](#ee-geometry-s2cell)
- [`ee.Geometry.serialize`](#ee-geometry-serialize)
- [`ee.Geometry.simplify`](#ee-geometry-simplify)
- [`ee.Geometry.symmetricDifference`](#ee-geometry-symmetricdifference)
- [`ee.Geometry.toGeoJSON`](#ee-geometry-togeojson)
- [`ee.Geometry.toGeoJSONString`](#ee-geometry-togeojsonstring)
- [`ee.Geometry.transform`](#ee-geometry-transform)
- [`ee.Geometry.type`](#ee-geometry-type)
- [`ee.Geometry.union`](#ee-geometry-union)
- [`ee.Geometry.withinDistance`](#ee-geometry-withindistance)
- [`ee.Projection`](#ee-projection)
- [`ee.Projection.atScale`](#ee-projection-atscale)
- [`ee.Projection.crs`](#ee-projection-crs)
- [`ee.Projection.nominalScale`](#ee-projection-nominalscale)
- [`ee.Projection.scale`](#ee-projection-scale)
- [`ee.Projection.transform`](#ee-projection-transform)
- [`ee.Projection.translate`](#ee-projection-translate)
- [`ee.Projection.wkt`](#ee-projection-wkt)

---

## ee.Algorithms.GeometryConstructors.BBox

Constructs a rectangle whose edges are lines of latitude and longitude.

The result is a planar WGS84 rectangle.

If (east - west) ≥ 360 then the longitude range will be normalized to -180 to +180; otherwise they will be treated as designating points on a circle (e.g., east may be numerically less than west).

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.BBox(west, south, east, north)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `west` | Float | The westernmost enclosed longitude. Will be adjusted to lie in the range -180 to 180. |
| `south` | Float | The southernmost enclosed latitude. If less than -90 (south pole), will be treated as -90. |
| `east` | Float | The easternmost enclosed longitude. |
| `north` | Float | The northernmost enclosed latitude. If greater than +90 (north pole), will be treated as +90. |

## ee.Algorithms.GeometryConstructors.LineString

Constructs a LineString from the given coordinates.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.LineString(coordinates, *crs*, *geodesic*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | The list of Points or pairs of Numbers in x,y order. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, default: null | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, default: null | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |

## ee.Algorithms.GeometryConstructors.LinearRing

Constructs a LinearRing from the given coordinates, automatically adding the first point at the end if the ring is not explicitly closed.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.LinearRing(coordinates, *crs*, *geodesic*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | The list of Points or pairs of Numbers in x,y order. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, default: null | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, default: null | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |

## ee.Algorithms.GeometryConstructors.MultiGeometry

Constructs a MultiGeometry from the given list of geometry elements.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.MultiGeometry(geometries, *crs*, *geodesic*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `geometries` | List | The list of geometries for the MultiGeometry. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, default: null | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, default: null | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |

## ee.Algorithms.GeometryConstructors.MultiLineString

Constructs a MultiLineString from the given coordinates.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.MultiLineString(coordinates, *crs*, *geodesic*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | The list of LineStrings, or to wrap a single LineString, the list of Points or pairs of Numbers in x,y order. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, default: null | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, default: null | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |

## ee.Algorithms.GeometryConstructors.MultiPoint

Constructs a MultiPoint from the given coordinates.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.MultiPoint(coordinates, *crs*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | The list of Points or pairs of Numbers in x,y order. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |

## ee.Algorithms.GeometryConstructors.MultiPolygon

Constructs a MultiPolygon from the given coordinates.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.MultiPolygon(coordinates, *crs*, *geodesic*, *maxError*, *evenOdd*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | A list of Polygons, or for one simple polygon, a list of Points or pairs of Numbers in x,y order. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, default: null | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, default: null | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |
| `evenOdd` | Boolean, default: true | If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left-inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. |

## ee.Algorithms.GeometryConstructors.Point

Constructs a new Point from the given x,y coordinates.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.Point(coordinates, *crs*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | The coordinates of this Point in x,y order. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |

## ee.Algorithms.GeometryConstructors.Polygon

Constructs a Polygon from the given coordinates.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.Polygon(coordinates, *crs*, *geodesic*, *maxError*, *evenOdd*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | A list of LinearRings where the first is the shell and the rest are holes, or for a simple polygon, a list of Points or pairs of Numbers in x,y order. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, default: null | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, default: null | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |
| `evenOdd` | Boolean, default: true | If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left-inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. |

## ee.Algorithms.GeometryConstructors.Rectangle

Constructs a rectangular polygon from the given corner points.

| Usage | Returns |
|---|---|
| `ee.Algorithms.GeometryConstructors.Rectangle(coordinates, *crs*, *geodesic*, *evenOdd*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | The low and then high corners of the Rectangle, as a list of Points or pairs of Numbers in x,y order. |
| `crs` | Projection, default: null | The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, default: null | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `evenOdd` | Boolean, default: true | If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left-inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. |

## ee.ErrorMargin

Returns an ErrorMargin of the given type with the given value.

| Usage | Returns |
|---|---|
| `ee.ErrorMargin(*value*, *unit*)` | ErrorMargin |

| Argument | Type | Details |
|---|---|---|
| `value` | Float, default: null | The maximum error value allowed by the margin. Ignored if the unit is 'infinite'. |
| `unit` | String, default: "meters" | The unit of this margin: 'meters', 'projected' or 'infinite'. |

## ee.Geometry

Creates a geometry.

| Usage | Returns |
|---|---|
| `ee.Geometry(geoJson, *proj*, *geodesic*, *evenOdd*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `geoJson` | Object | The GeoJSON object describing the geometry or a ComputedObject to be reinterpreted as a Geometry. Supports CRS specifications as per the GeoJSON spec, but only allows named (rather than "linked" CRSs). If this includes a 'geodesic' field, and opt_geodesic is not specified, it will be used as opt_geodesic. |
| `proj` | Projection, optional | An optional projection specification, either as a CRS ID code or as a WKT string. If specified, overrides any CRS found in the geoJson parameter. If unspecified and the geoJson does not declare a CRS, defaults to "EPSG:4326" (x=longitude, y=latitude). |
| `geodesic` | Boolean, optional | Whether line segments should be interpreted as spherical geodesics. If false, indicates that line segments should be interpreted as planar lines in the specified CRS. If absent, defaults to true if the CRS is geographic (including the default EPSG:4326), or to false if the CRS is projected. |
| `evenOdd` | Boolean, optional | If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left- inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. If unspecified, defaults to true. |

## ee.Geometry.BBox

Constructs a rectangle whose edges are lines of latitude and longitude.

The result is a planar rectangle in EPSG:4326.

If (east - west) ≥ 360 then the longitude range will be normalized to -180 to

+180; otherwise they will be treated as designating points on a circle (e.g. east may be numerically less than west).

| Usage | Returns |
|---|---|
| `ee.Geometry.BBox(west, south, east, north)` | Geometry.BBox |

| Argument | Type | Details |
|---|---|---|
| `west` | Number | The westernmost enclosed longitude. Will be adjusted to lie in the range -180° to 180°. |
| `south` | Number | The southernmost enclosed latitude. If less than -90° (south pole), will be treated as -90°. |
| `east` | Number | The easternmost enclosed longitude. |
| `north` | Number | The northernmost enclosed latitude. If greater than +90° (north pole), will be treated as +90°. |

## ee.Geometry.BBox.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `BBox.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.BBox.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `BBox.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.BBox.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `BBox.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.BBox.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `BBox.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.BBox.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `BBox.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.BBox.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `BBox.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `BBox.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `BBox.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `BBox.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `BBox.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `BBox.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.BBox.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `BBox.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.BBox.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `BBox.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.BBox.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `BBox.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `BBox.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `BBox.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.BBox.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `BBox.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.BBox.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `BBox.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.BBox.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `BBox.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.BBox.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `BBox.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.BBox.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `BBox.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.BBox.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `BBox.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.BBox.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `BBox.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `BBox.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `BBox.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.BBox.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `BBox.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.BBox.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `BBox.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.BBox.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `BBox.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.BBox.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `BBox.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.BBox.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `BBox.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.BBox.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `BBox.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `BBox.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.BBox.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `BBox.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.BBox.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `BBox.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.BBox.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `BBox.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.BBox.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `BBox.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.BBox.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `BBox.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString

Constructs an ee.Geometry describing a LineString.

For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 LineStrings given an even number of arguments, e.g. ee.Geometry.LineString(aLng, aLat, bLng, bLat, ...).

| Usage | Returns |
|---|---|
| `ee.Geometry.LineString(coords, *proj*, *geodesic*, *maxError*)` | Geometry.LineString |

| Argument | Type | Details |
|---|---|---|
| `coords` | List\[Geometry\]\|List\[List\[Number\]\]\|List\[Number\] | A list of at least two points. May be a list of coordinates in the GeoJSON 'LineString' format, a list of at least two ee.Geometry objects describing a point, or a list of at least four numbers defining the \[x,y\] coordinates of at least two points. |
| `proj` | Projection, optional | The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs. |
| `geodesic` | Boolean, optional | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, optional | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |

## ee.Geometry.LineString.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `LineString.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.LineString.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `LineString.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.LineString.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `LineString.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.LineString.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `LineString.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.LineString.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `LineString.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.LineString.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `LineString.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `LineString.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `LineString.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `LineString.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `LineString.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `LineString.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LineString.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `LineString.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.LineString.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `LineString.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.LineString.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `LineString.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `LineString.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `LineString.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.LineString.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `LineString.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.LineString.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `LineString.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LineString.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `LineString.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.LineString.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `LineString.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LineString.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `LineString.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LineString.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `LineString.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.LineString.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `LineString.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `LineString.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `LineString.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LineString.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `LineString.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.LineString.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `LineString.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.LineString.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `LineString.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LineString.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `LineString.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.LineString.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `LineString.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.LineString.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `LineString.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `LineString.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.LineString.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `LineString.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.LineString.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `LineString.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.LineString.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `LineString.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LineString.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `LineString.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LineString.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `LineString.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing

Constructs an ee.Geometry describing a LinearRing. If the last point is not equal to the first, a duplicate of the first point will be added at the end.

For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 LinearRings given an even number of arguments, e.g. ee.Geometry.LinearRing(aLng, aLat, bLng, bLat, ..., aLng, aLat).

| Usage | Returns |
|---|---|
| `ee.Geometry.LinearRing(coords, *proj*, *geodesic*, *maxError*)` | Geometry.LinearRing |

| Argument | Type | Details |
|---|---|---|
| `coords` | List\[Geometry\]\|List\[List\[Number\]\]\|List\[Number\] | A list of points in the ring. May be a list of coordinates in the GeoJSON 'LinearRing' format, a list of at least three ee.Geometry objects describing a point, or a list of at least six numbers defining the \[x,y\] coordinates of at least three points. |
| `proj` | Projection, optional | The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs. |
| `geodesic` | Boolean, optional | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, optional | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |

## ee.Geometry.LinearRing.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `LinearRing.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.LinearRing.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `LinearRing.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.LinearRing.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `LinearRing.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.LinearRing.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `LinearRing.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.LinearRing.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `LinearRing.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.LinearRing.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `LinearRing.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `LinearRing.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `LinearRing.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `LinearRing.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `LinearRing.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `LinearRing.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LinearRing.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `LinearRing.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.LinearRing.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `LinearRing.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.LinearRing.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `LinearRing.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `LinearRing.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `LinearRing.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.LinearRing.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `LinearRing.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.LinearRing.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `LinearRing.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LinearRing.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `LinearRing.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.LinearRing.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `LinearRing.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LinearRing.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `LinearRing.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LinearRing.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `LinearRing.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.LinearRing.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `LinearRing.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `LinearRing.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `LinearRing.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LinearRing.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `LinearRing.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.LinearRing.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `LinearRing.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.LinearRing.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `LinearRing.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LinearRing.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `LinearRing.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.LinearRing.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `LinearRing.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.LinearRing.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `LinearRing.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `LinearRing.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.LinearRing.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `LinearRing.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.LinearRing.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `LinearRing.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.LinearRing.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `LinearRing.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.LinearRing.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `LinearRing.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.LinearRing.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `LinearRing.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString

Constructs an ee.Geometry describing a MultiLineString.

For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 MultiLineStrings with a single LineString, given an even number of arguments, e.g. ee.Geometry.MultiLineString(aLng, aLat, bLng, bLat, ...).

| Usage | Returns |
|---|---|
| `ee.Geometry.MultiLineString(coords, *proj*, *geodesic*, *maxError*)` | Geometry.MultiLineString |

| Argument | Type | Details |
|---|---|---|
| `coords` | List\[Geometry\]\|List\[List\[List\[Number\]\]\]\|List\[Number\] | A list of linestrings. May be a list of coordinates in the GeoJSON 'MultiLineString' format, a list of at least two ee.Geometry objects describing a LineString, or a list of numbers defining a single linestring. |
| `proj` | Projection, optional | The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs. |
| `geodesic` | Boolean, optional | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, optional | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |

## ee.Geometry.MultiLineString.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `MultiLineString.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.MultiLineString.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `MultiLineString.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.MultiLineString.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `MultiLineString.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.MultiLineString.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `MultiLineString.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.MultiLineString.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `MultiLineString.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.MultiLineString.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `MultiLineString.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `MultiLineString.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `MultiLineString.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `MultiLineString.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `MultiLineString.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `MultiLineString.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiLineString.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `MultiLineString.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.MultiLineString.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `MultiLineString.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.MultiLineString.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `MultiLineString.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `MultiLineString.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `MultiLineString.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.MultiLineString.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `MultiLineString.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.MultiLineString.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `MultiLineString.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiLineString.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `MultiLineString.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.MultiLineString.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `MultiLineString.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiLineString.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `MultiLineString.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiLineString.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `MultiLineString.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.MultiLineString.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `MultiLineString.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `MultiLineString.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `MultiLineString.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiLineString.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `MultiLineString.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.MultiLineString.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `MultiLineString.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.MultiLineString.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `MultiLineString.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiLineString.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `MultiLineString.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.MultiLineString.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `MultiLineString.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.MultiLineString.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `MultiLineString.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `MultiLineString.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.MultiLineString.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `MultiLineString.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.MultiLineString.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `MultiLineString.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.MultiLineString.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `MultiLineString.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiLineString.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `MultiLineString.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiLineString.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `MultiLineString.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint

Constructs an ee.Geometry describing a MultiPoint.

For convenience, varargs may be used when all arguments are numbers. This allows creating EPSG:4326 MultiPoints given an even number of arguments, e.g. ee.Geometry.MultiPoint(aLng, aLat, bLng, bLat, ...).

| Usage | Returns |
|---|---|
| `ee.Geometry.MultiPoint(coords, *proj*)` | Geometry.MultiPoint |

| Argument | Type | Details |
|---|---|---|
| `coords` | List\[Geometry\]\|List\[List\[Number\]\]\|List\[Number\] | A list of points, each in the GeoJSON 'coordinates' format of a Point, or a list of the x,y coordinates in the given projection, or an ee.Geometry describing a point. |
| `proj` | Projection, optional | The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs. |

## ee.Geometry.MultiPoint.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `MultiPoint.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.MultiPoint.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `MultiPoint.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.MultiPoint.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `MultiPoint.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.MultiPoint.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `MultiPoint.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.MultiPoint.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `MultiPoint.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.MultiPoint.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `MultiPoint.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `MultiPoint.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `MultiPoint.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `MultiPoint.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `MultiPoint.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `MultiPoint.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPoint.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `MultiPoint.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.MultiPoint.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `MultiPoint.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.MultiPoint.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `MultiPoint.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `MultiPoint.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `MultiPoint.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.MultiPoint.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `MultiPoint.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.MultiPoint.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `MultiPoint.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPoint.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `MultiPoint.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.MultiPoint.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `MultiPoint.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPoint.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `MultiPoint.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPoint.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `MultiPoint.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.MultiPoint.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `MultiPoint.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `MultiPoint.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `MultiPoint.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPoint.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `MultiPoint.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.MultiPoint.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `MultiPoint.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.MultiPoint.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `MultiPoint.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPoint.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `MultiPoint.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.MultiPoint.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `MultiPoint.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.MultiPoint.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `MultiPoint.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `MultiPoint.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.MultiPoint.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `MultiPoint.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.MultiPoint.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `MultiPoint.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.MultiPoint.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `MultiPoint.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPoint.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `MultiPoint.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPoint.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `MultiPoint.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon

Constructs an ee.Geometry describing a MultiPolygon.

For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 MultiPolygons with a single Polygon with a single LinearRing given an even number of arguments, e.g. ee.Geometry.MultiPolygon(aLng, aLat, bLng, bLat, ..., aLng, aLat).

| Usage | Returns |
|---|---|
| `ee.Geometry.MultiPolygon(coords, *proj*, *geodesic*, *maxError*, *evenOdd*)` | Geometry.MultiPolygon |

| Argument | Type | Details |
|---|---|---|
| `coords` | List\[Geometry\]\|List\[List\[List\[List\[Number\]\]\]\]\|List\[Number\] | A list of polygons. May be a list of coordinates in the GeoJSON 'MultiPolygon' format, a list of ee.Geometry objects describing a Polygon, or a list of numbers defining a single polygon boundary. |
| `proj` | Projection, optional | The projection of this geometry. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, optional | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, optional | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |
| `evenOdd` | Boolean, optional | If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left- inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. If unspecified, defaults to true. |

## ee.Geometry.MultiPolygon.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `MultiPolygon.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.MultiPolygon.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `MultiPolygon.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.MultiPolygon.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `MultiPolygon.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.MultiPolygon.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `MultiPolygon.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.MultiPolygon.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `MultiPolygon.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.MultiPolygon.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `MultiPolygon.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `MultiPolygon.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `MultiPolygon.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `MultiPolygon.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `MultiPolygon.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `MultiPolygon.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPolygon.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `MultiPolygon.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.MultiPolygon.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `MultiPolygon.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.MultiPolygon.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `MultiPolygon.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `MultiPolygon.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `MultiPolygon.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.MultiPolygon.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `MultiPolygon.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.MultiPolygon.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `MultiPolygon.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPolygon.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `MultiPolygon.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.MultiPolygon.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `MultiPolygon.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPolygon.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `MultiPolygon.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPolygon.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `MultiPolygon.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.MultiPolygon.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `MultiPolygon.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `MultiPolygon.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `MultiPolygon.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPolygon.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `MultiPolygon.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.MultiPolygon.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `MultiPolygon.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.MultiPolygon.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `MultiPolygon.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPolygon.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `MultiPolygon.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.MultiPolygon.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `MultiPolygon.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.MultiPolygon.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `MultiPolygon.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `MultiPolygon.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.MultiPolygon.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `MultiPolygon.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.MultiPolygon.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `MultiPolygon.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.MultiPolygon.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `MultiPolygon.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.MultiPolygon.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `MultiPolygon.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.MultiPolygon.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `MultiPolygon.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point

Constructs an ee.Geometry describing a point.

For convenience, varargs may be used when all arguments are numbers. This allows creating EPSG:4326 points, e.g. ee.Geometry.Point(lng, lat).

| Usage | Returns |
|---|---|
| `ee.Geometry.Point(coords, *proj*)` | Geometry.Point |

| Argument | Type | Details |
|---|---|---|
| `coords` | List\[Number\] | A list of two \[x,y\] coordinates in the given projection. |
| `proj` | Projection, optional | The projection of this geometry, or EPSG:4326 if unspecified. |

## ee.Geometry.Point.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `Point.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.Point.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Point.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.Point.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `Point.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.Point.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `Point.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.Point.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `Point.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.Point.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `Point.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `Point.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `Point.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `Point.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `Point.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `Point.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Point.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `Point.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.Point.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `Point.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.Point.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `Point.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `Point.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `Point.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.Point.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `Point.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.Point.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `Point.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Point.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Point.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.Point.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `Point.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Point.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `Point.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Point.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `Point.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.Point.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `Point.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `Point.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `Point.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Point.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `Point.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.Point.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `Point.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.Point.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `Point.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Point.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Point.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.Point.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `Point.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.Point.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `Point.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `Point.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.Point.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `Point.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.Point.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `Point.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.Point.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `Point.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Point.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `Point.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Point.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `Point.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon

Constructs an ee.Geometry describing a polygon.

For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 Polygons with a single LinearRing given an even number of arguments, e.g. ee.Geometry.Polygon(aLng, aLat, bLng, bLat, ..., aLng, aLat).

| Usage | Returns |
|---|---|
| `ee.Geometry.Polygon(coords, *proj*, *geodesic*, *maxError*, *evenOdd*)` | Geometry.Polygon |

| Argument | Type | Details |
|---|---|---|
| `coords` | List\[Geometry\]\|List\[List\[List\[Number\]\]\]\|List\[Number\] | A list of rings defining the boundaries of the polygon. May be a list of coordinates in the GeoJSON 'Polygon' format, a list of ee.Geometry objects describing a LinearRing, or a list of numbers defining a single polygon boundary. |
| `proj` | Projection, optional | The projection of this geometry. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326. |
| `geodesic` | Boolean, optional | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `maxError` | ErrorMargin, optional | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state. |
| `evenOdd` | Boolean, optional | If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left- inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. If unspecified, defaults to true. |

## ee.Geometry.Polygon.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `Polygon.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.Polygon.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Polygon.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.Polygon.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `Polygon.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.Polygon.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `Polygon.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.Polygon.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `Polygon.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.Polygon.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `Polygon.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `Polygon.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `Polygon.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `Polygon.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `Polygon.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `Polygon.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Polygon.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `Polygon.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.Polygon.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `Polygon.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.Polygon.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `Polygon.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `Polygon.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `Polygon.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.Polygon.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `Polygon.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.Polygon.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `Polygon.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Polygon.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Polygon.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.Polygon.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `Polygon.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Polygon.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `Polygon.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Polygon.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `Polygon.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.Polygon.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `Polygon.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `Polygon.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `Polygon.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Polygon.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `Polygon.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.Polygon.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `Polygon.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.Polygon.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `Polygon.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Polygon.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Polygon.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.Polygon.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `Polygon.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.Polygon.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `Polygon.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `Polygon.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.Polygon.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `Polygon.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.Polygon.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `Polygon.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.Polygon.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `Polygon.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Polygon.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `Polygon.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Polygon.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `Polygon.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle

Constructs an ee.Geometry describing a rectangular polygon.

For convenience, varargs may be used when all arguments are numbers. This allows creating EPSG:4326 Polygons given exactly four coordinates, e.g. ee.Geometry.Rectangle(minLng, minLat, maxLng, maxLat).

| Usage | Returns |
|---|---|
| `ee.Geometry.Rectangle(coords, *proj*, *geodesic*, *evenOdd*)` | Geometry.Rectangle |

| Argument | Type | Details |
|---|---|---|
| `coords` | List\[Geometry\]\|List\[List\[Number\]\]\|List\[Number\] | The minimum and maximum corners of the rectangle, as a list of two points each in the format of GeoJSON 'Point' coordinates, or a list of two ee.Geometry objects describing a point, or a list of four numbers in the order xMin, yMin, xMax, yMax. |
| `proj` | Projection, optional | The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs. |
| `geodesic` | Boolean, optional | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers. |
| `evenOdd` | Boolean, optional | If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left- inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. If unspecified, defaults to true. |

## ee.Geometry.Rectangle.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `Rectangle.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.Rectangle.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Rectangle.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.Rectangle.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `Rectangle.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.Rectangle.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `Rectangle.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.Rectangle.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `Rectangle.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.Rectangle.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `Rectangle.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `Rectangle.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `Rectangle.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `Rectangle.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `Rectangle.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `Rectangle.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Rectangle.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `Rectangle.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.Rectangle.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `Rectangle.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.Rectangle.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `Rectangle.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `Rectangle.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `Rectangle.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.Rectangle.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `Rectangle.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.Rectangle.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `Rectangle.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Rectangle.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Rectangle.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.Rectangle.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `Rectangle.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Rectangle.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `Rectangle.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Rectangle.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `Rectangle.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.Rectangle.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `Rectangle.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `Rectangle.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `Rectangle.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Rectangle.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `Rectangle.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.Rectangle.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `Rectangle.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.Rectangle.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `Rectangle.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Rectangle.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Rectangle.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.Rectangle.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `Rectangle.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.Rectangle.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `Rectangle.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `Rectangle.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.Rectangle.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `Rectangle.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.Rectangle.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `Rectangle.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.Rectangle.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `Rectangle.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.Rectangle.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `Rectangle.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.Rectangle.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `Rectangle.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.area

Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).

| Usage | Returns |
|---|---|
| `Geometry.area(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry input. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters. |

## ee.Geometry.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Geometry.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Geometry.bounds

Returns the bounding rectangle of the geometry.

| Usage | Returns |
|---|---|
| `Geometry.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Return the bounding box of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.buffer

Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted.

| Usage | Returns |
|---|---|
| `Geometry.buffer(distance, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry being buffered. |
| `distance` | Float | The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance. |
| `proj` | Projection, default: null | If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system. |

## ee.Geometry.centroid

Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.

| Usage | Returns |
|---|---|
| `Geometry.centroid(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the centroid of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.Geometry.closestPoint

Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned.

| Usage | Returns |
|---|---|
| `Geometry.closestPoint(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.closestPoints

Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.

| Usage | Returns |
|---|---|
| `Geometry.closestPoints(right, *maxError*, *proj*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.containedIn

Returns true if and only if one geometry is contained in the other.

| Usage | Returns |
|---|---|
| `Geometry.containedIn(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.contains

Returns true if and only if one geometry contains the other.

| Usage | Returns |
|---|---|
| `Geometry.contains(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.convexHull

Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.

| Usage | Returns |
|---|---|
| `Geometry.convexHull(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Calculates the convex hull of this geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.coordinates

Returns a GeoJSON-style list of the geometry's coordinates.

| Usage | Returns |
|---|---|
| `Geometry.coordinates()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.coveringGrid

Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection.

| Usage | Returns |
|---|---|
| `Geometry.coveringGrid(proj, *scale*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The result is the grid cells that intersect with this region. |
| `proj` | Projection | The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale. |
| `scale` | Float, default: null | Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled. |

## ee.Geometry.cutLines

Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString.

| Usage | Returns |
|---|---|
| `Geometry.cutLines(distances, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | Cuts the lines of this geometry. |
| `distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified. |

## ee.Geometry.difference

Returns the result of subtracting the 'right' geometry from the 'left' geometry.

| Usage | Returns |
|---|---|
| `Geometry.difference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.disjoint

Returns true if and only if the geometries are disjoint.

| Usage | Returns |
|---|---|
| `Geometry.disjoint(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.dissolve

Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.

| Usage | Returns |
|---|---|
| `Geometry.dissolve(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to union. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system. |

## ee.Geometry.distance

Returns the minimum distance between two geometries.

| Usage | Returns |
|---|---|
| `Geometry.distance(right, *maxError*, *proj*, *spherical*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |
| `spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false. |

## ee.Geometry.edgesAreGeodesics

Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.

| Usage | Returns |
|---|---|
| `Geometry.edgesAreGeodesics()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Geometry.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Geometry.fromS2CellId

Constructs the Polygon corresponding to an S2 cell id.

| Usage | Returns |
|---|---|
| `ee.Geometry.fromS2CellId(cellId)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `cellId` | Long | The S2 cell id as 64 bit integer. From Javascript, which does not support integers larger than 53 bits, use fromS2CellToken instead. |

## ee.Geometry.fromS2CellToken

Constructs the Polygon corresponding to an S2 cell id as a hex string.

| Usage | Returns |
|---|---|
| `ee.Geometry.fromS2CellToken(cellToken)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `cellToken` | String | The S2 cell id as a hex string. Trailing zeros are required, e.g., the top level face containing Antarctica is 0xb000000000000000. |

## ee.Geometry.geodesic

If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.

| Usage | Returns |
|---|---|
| `Geometry.geodesic()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.geometries

Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries.

| Usage | Returns |
|---|---|
| `Geometry.geometries()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `Geometry.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Geometry.intersection

Returns the intersection of the two geometries.

| Usage | Returns |
|---|---|
| `Geometry.intersection(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.intersects

Returns true if and only if the geometries intersect.

| Usage | Returns |
|---|---|
| `Geometry.intersects(right, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.isUnbounded

Returns whether the geometry is unbounded.

| Usage | Returns |
|---|---|
| `Geometry.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.length

Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.

| Usage | Returns |
|---|---|
| `Geometry.length(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.perimeter

Returns the length of the perimeter of the polygonal parts of the geometry. The perimeter of multi geometries is the sum of the perimeters of their components.

| Usage | Returns |
|---|---|
| `Geometry.perimeter(*maxError*, *proj*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The input geometry. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters. |

## ee.Geometry.projection

Returns the projection of the geometry.

| Usage | Returns |
|---|---|
| `Geometry.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.s2Cell

Constructs the Polygon corresponding to an S2 cell id.

| Usage | Returns |
|---|---|
| `ee.Geometry.s2Cell(cellId)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| `cellId` | Long | The S2 cell id as 64 bit integer. From Javascript, which does not support integers larger than 53 bits, use fromS2CellToken instead. |

## ee.Geometry.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Geometry.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Geometry.simplify

Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null.

This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.

| Usage | Returns |
|---|---|
| `Geometry.simplify(maxError, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to simplify. |
| `maxError` | ErrorMargin | The maximum amount of error by which the result may differ from the input. |
| `proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection. |

## ee.Geometry.symmetricDifference

Returns the symmetric difference between two geometries.

| Usage | Returns |
|---|---|
| `Geometry.symmetricDifference(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.toGeoJSON

Returns a GeoJSON representation of the geometry.

| Usage | Returns |
|---|---|
| `Geometry.toGeoJSON()` | GeoJSONGeometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.toGeoJSONString

Returns a GeoJSON string representation of the geometry.

| Usage | Returns |
|---|---|
| `Geometry.toGeoJSONString()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The Geometry instance. |

## ee.Geometry.transform

Transforms the geometry to a specific projection.

| Usage | Returns |
|---|---|
| `Geometry.transform(*proj*, *maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry | The geometry to reproject. |
| `proj` | Projection, optional | The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection. |
| `maxError` | ErrorMargin, default: null | The maximum projection error. |

## ee.Geometry.type

Returns the GeoJSON type of the geometry.

| Usage | Returns |
|---|---|
| `Geometry.type()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `geometry` | Geometry |   |

## ee.Geometry.union

Returns the union of the two geometries.

| Usage | Returns |
|---|---|
| `Geometry.union(right, *maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Geometry.withinDistance

Returns true if and only if the geometries are within a specified distance.

| Usage | Returns |
|---|---|
| `Geometry.withinDistance(right, distance, *maxError*, *proj*)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Geometry | The geometry used as the left operand of the operation. |
| `right` | Geometry | The geometry used as the right operand of the operation. |
| `distance` | Float | The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere. |

## ee.Projection

Returns a Projection with the given base coordinate system and the given transform between projected coordinates and the base. If no transform is specified, the identity transform is assumed.

| Usage | Returns |
|---|---|
| `ee.Projection(crs, *transform*, *transformWkt*)` | Projection |

| Argument | Type | Details |
|---|---|---|
| `crs` | Object | The base coordinate reference system of this Projection, given as a well-known authority code (e.g., 'EPSG:4326') or a WKT string. |
| `transform` | List, default: null | The transform between projected coordinates and the base coordinate system, specified as a 2x3 affine transform matrix in row-major order: \[xScale, xShearing, xTranslation, yShearing, yScale, yTranslation\]. May not specify both this and 'transformWkt'. |
| `transformWkt` | String, default: null | The transform between projected coordinates and the base coordinate system, specified as a WKT string. May not specify both this and 'transform'. |

## ee.Projection.atScale

Returns the projection scaled such that its units have the given scale in linear meters, as measured at the point of true scale.

| Usage | Returns |
|---|---|
| `Projection.atScale(meters)` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `projection` | Projection |   |
| `meters` | Float | The scale in linear meters. |

## ee.Projection.crs

Returns the authority code (e.g., 'EPSG:4326') for the base coordinate system of this projection, or null if the base coordinate system is not found in any available database.

| Usage | Returns |
|---|---|
| `Projection.crs()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `projection` | Projection |   |

## ee.Projection.nominalScale

Returns the linear scale in meters of the units of this projection, as measured at the point of true scale.

| Usage | Returns |
|---|---|
| `Projection.nominalScale()` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `proj` | Projection |   |

## ee.Projection.scale

Returns the projection scaled by the given amount in each axis.

| Usage | Returns |
|---|---|
| `Projection.scale(x, y)` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `projection` | Projection |   |
| `x` | Float | The amount to scale by in the x axis. |
| `y` | Float | The amount to scale by in the y axis. |

## ee.Projection.transform

Returns a WKT representation of the transform of this Projection. This is the transform that converts from projected coordinates to the base coordinate system.

| Usage | Returns |
|---|---|
| `Projection.transform()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `projection` | Projection |   |

## ee.Projection.translate

Returns the projection translated by the given amount in each axis.

| Usage | Returns |
|---|---|
| `Projection.translate(x, y)` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `projection` | Projection |   |
| `x` | Float | The amount to translate by in the x axis. |
| `y` | Float | The amount to translate by in the y axis. |

## ee.Projection.wkt

Returns a WKT representation of the base coordinate system of this Projection.

| Usage | Returns |
|---|---|
| `Projection.wkt()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `projection` | Projection |   |

