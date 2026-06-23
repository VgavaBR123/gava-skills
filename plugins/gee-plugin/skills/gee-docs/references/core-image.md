# Raster — ee.Image, ee.ImageCollection, Kernel, Terrain

> 352 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.Image`](#ee-image)
- [`ee.Image.abs`](#ee-image-abs)
- [`ee.Image.acos`](#ee-image-acos)
- [`ee.Image.add`](#ee-image-add)
- [`ee.Image.addBands`](#ee-image-addbands)
- [`ee.Image.and`](#ee-image-and)
- [`ee.Image.arrayAccum`](#ee-image-arrayaccum)
- [`ee.Image.arrayArgmax`](#ee-image-arrayargmax)
- [`ee.Image.arrayCat`](#ee-image-arraycat)
- [`ee.Image.arrayDimensions`](#ee-image-arraydimensions)
- [`ee.Image.arrayDotProduct`](#ee-image-arraydotproduct)
- [`ee.Image.arrayFlatten`](#ee-image-arrayflatten)
- [`ee.Image.arrayGet`](#ee-image-arrayget)
- [`ee.Image.arrayLength`](#ee-image-arraylength)
- [`ee.Image.arrayLengths`](#ee-image-arraylengths)
- [`ee.Image.arrayMask`](#ee-image-arraymask)
- [`ee.Image.arrayPad`](#ee-image-arraypad)
- [`ee.Image.arrayProject`](#ee-image-arrayproject)
- [`ee.Image.arrayReduce`](#ee-image-arrayreduce)
- [`ee.Image.arrayRepeat`](#ee-image-arrayrepeat)
- [`ee.Image.arrayReshape`](#ee-image-arrayreshape)
- [`ee.Image.arraySlice`](#ee-image-arrayslice)
- [`ee.Image.arraySort`](#ee-image-arraysort)
- [`ee.Image.arrayTranspose`](#ee-image-arraytranspose)
- [`ee.Image.aside`](#ee-image-aside)
- [`ee.Image.asin`](#ee-image-asin)
- [`ee.Image.atan`](#ee-image-atan)
- [`ee.Image.atan2`](#ee-image-atan2)
- [`ee.Image.bandNames`](#ee-image-bandnames)
- [`ee.Image.bandTypes`](#ee-image-bandtypes)
- [`ee.Image.bitCount`](#ee-image-bitcount)
- [`ee.Image.bitsToArrayImage`](#ee-image-bitstoarrayimage)
- [`ee.Image.bitwiseAnd`](#ee-image-bitwiseand)
- [`ee.Image.bitwiseNot`](#ee-image-bitwisenot)
- [`ee.Image.bitwiseOr`](#ee-image-bitwiseor)
- [`ee.Image.bitwiseXor`](#ee-image-bitwisexor)
- [`ee.Image.blend`](#ee-image-blend)
- [`ee.Image.byte`](#ee-image-byte)
- [`ee.Image.cast`](#ee-image-cast)
- [`ee.Image.cat`](#ee-image-cat)
- [`ee.Image.cbrt`](#ee-image-cbrt)
- [`ee.Image.ceil`](#ee-image-ceil)
- [`ee.Image.changeProj`](#ee-image-changeproj)
- [`ee.Image.clamp`](#ee-image-clamp)
- [`ee.Image.classify`](#ee-image-classify)
- [`ee.Image.clip`](#ee-image-clip)
- [`ee.Image.clipToBoundsAndScale`](#ee-image-cliptoboundsandscale)
- [`ee.Image.clipToCollection`](#ee-image-cliptocollection)
- [`ee.Image.cluster`](#ee-image-cluster)
- [`ee.Image.connectedComponents`](#ee-image-connectedcomponents)
- [`ee.Image.connectedPixelCount`](#ee-image-connectedpixelcount)
- [`ee.Image.constant`](#ee-image-constant)
- [`ee.Image.convolve`](#ee-image-convolve)
- [`ee.Image.copyProperties`](#ee-image-copyproperties)
- [`ee.Image.cos`](#ee-image-cos)
- [`ee.Image.cosh`](#ee-image-cosh)
- [`ee.Image.cumulativeCost`](#ee-image-cumulativecost)
- [`ee.Image.date`](#ee-image-date)
- [`ee.Image.derivative`](#ee-image-derivative)
- [`ee.Image.digamma`](#ee-image-digamma)
- [`ee.Image.directionalDistanceTransform`](#ee-image-directionaldistancetransform)
- [`ee.Image.displace`](#ee-image-displace)
- [`ee.Image.displacement`](#ee-image-displacement)
- [`ee.Image.distance`](#ee-image-distance)
- [`ee.Image.divide`](#ee-image-divide)
- [`ee.Image.double`](#ee-image-double)
- [`ee.Image.entropy`](#ee-image-entropy)
- [`ee.Image.eq`](#ee-image-eq)
- [`ee.Image.erf`](#ee-image-erf)
- [`ee.Image.erfInv`](#ee-image-erfinv)
- [`ee.Image.erfc`](#ee-image-erfc)
- [`ee.Image.erfcInv`](#ee-image-erfcinv)
- [`ee.Image.evaluate`](#ee-image-evaluate)
- [`ee.Image.exp`](#ee-image-exp)
- [`ee.Image.expression`](#ee-image-expression)
- [`ee.Image.fastDistanceTransform`](#ee-image-fastdistancetransform)
- [`ee.Image.first`](#ee-image-first)
- [`ee.Image.firstNonZero`](#ee-image-firstnonzero)
- [`ee.Image.float`](#ee-image-float)
- [`ee.Image.floor`](#ee-image-floor)
- [`ee.Image.focalMax`](#ee-image-focalmax)
- [`ee.Image.focalMean`](#ee-image-focalmean)
- [`ee.Image.focalMedian`](#ee-image-focalmedian)
- [`ee.Image.focalMin`](#ee-image-focalmin)
- [`ee.Image.focalMode`](#ee-image-focalmode)
- [`ee.Image.gamma`](#ee-image-gamma)
- [`ee.Image.gammainc`](#ee-image-gammainc)
- [`ee.Image.geometry`](#ee-image-geometry)
- [`ee.Image.get`](#ee-image-get)
- [`ee.Image.getArray`](#ee-image-getarray)
- [`ee.Image.getDownloadURL`](#ee-image-getdownloadurl)
- [`ee.Image.getInfo`](#ee-image-getinfo)
- [`ee.Image.getMapId`](#ee-image-getmapid)
- [`ee.Image.getNumber`](#ee-image-getnumber)
- [`ee.Image.getString`](#ee-image-getstring)
- [`ee.Image.getThumbId`](#ee-image-getthumbid)
- [`ee.Image.getThumbURL`](#ee-image-getthumburl)
- [`ee.Image.glcmTexture`](#ee-image-glcmtexture)
- [`ee.Image.gradient`](#ee-image-gradient)
- [`ee.Image.gt`](#ee-image-gt)
- [`ee.Image.gte`](#ee-image-gte)
- [`ee.Image.hersDescriptor`](#ee-image-hersdescriptor)
- [`ee.Image.hersFeature`](#ee-image-hersfeature)
- [`ee.Image.hersImage`](#ee-image-hersimage)
- [`ee.Image.hsvToRgb`](#ee-image-hsvtorgb)
- [`ee.Image.hypot`](#ee-image-hypot)
- [`ee.Image.id`](#ee-image-id)
- [`ee.Image.int`](#ee-image-int)
- [`ee.Image.int16`](#ee-image-int16)
- [`ee.Image.int32`](#ee-image-int32)
- [`ee.Image.int64`](#ee-image-int64)
- [`ee.Image.int8`](#ee-image-int8)
- [`ee.Image.interpolate`](#ee-image-interpolate)
- [`ee.Image.lanczos`](#ee-image-lanczos)
- [`ee.Image.leftShift`](#ee-image-leftshift)
- [`ee.Image.linkCollection`](#ee-image-linkcollection)
- [`ee.Image.load`](#ee-image-load)
- [`ee.Image.loadGeoTIFF`](#ee-image-loadgeotiff)
- [`ee.Image.loadZarrV2Array`](#ee-image-loadzarrv2array)
- [`ee.Image.log`](#ee-image-log)
- [`ee.Image.log10`](#ee-image-log10)
- [`ee.Image.long`](#ee-image-long)
- [`ee.Image.lt`](#ee-image-lt)
- [`ee.Image.lte`](#ee-image-lte)
- [`ee.Image.mask`](#ee-image-mask)
- [`ee.Image.matrixCholeskyDecomposition`](#ee-image-matrixcholeskydecomposition)
- [`ee.Image.matrixDeterminant`](#ee-image-matrixdeterminant)
- [`ee.Image.matrixDiagonal`](#ee-image-matrixdiagonal)
- [`ee.Image.matrixFnorm`](#ee-image-matrixfnorm)
- [`ee.Image.matrixIdentity`](#ee-image-matrixidentity)
- [`ee.Image.matrixInverse`](#ee-image-matrixinverse)
- [`ee.Image.matrixLUDecomposition`](#ee-image-matrixludecomposition)
- [`ee.Image.matrixMultiply`](#ee-image-matrixmultiply)
- [`ee.Image.matrixPseudoInverse`](#ee-image-matrixpseudoinverse)
- [`ee.Image.matrixQRDecomposition`](#ee-image-matrixqrdecomposition)
- [`ee.Image.matrixSingularValueDecomposition`](#ee-image-matrixsingularvaluedecomposition)
- [`ee.Image.matrixSolve`](#ee-image-matrixsolve)
- [`ee.Image.matrixToDiag`](#ee-image-matrixtodiag)
- [`ee.Image.matrixTrace`](#ee-image-matrixtrace)
- [`ee.Image.matrixTranspose`](#ee-image-matrixtranspose)
- [`ee.Image.max`](#ee-image-max)
- [`ee.Image.medialAxis`](#ee-image-medialaxis)
- [`ee.Image.metadata`](#ee-image-metadata)
- [`ee.Image.min`](#ee-image-min)
- [`ee.Image.mod`](#ee-image-mod)
- [`ee.Image.multiply`](#ee-image-multiply)
- [`ee.Image.neighborhoodToArray`](#ee-image-neighborhoodtoarray)
- [`ee.Image.neighborhoodToBands`](#ee-image-neighborhoodtobands)
- [`ee.Image.neq`](#ee-image-neq)
- [`ee.Image.normalizedDifference`](#ee-image-normalizeddifference)
- [`ee.Image.not`](#ee-image-not)
- [`ee.Image.or`](#ee-image-or)
- [`ee.Image.paint`](#ee-image-paint)
- [`ee.Image.pixelArea`](#ee-image-pixelarea)
- [`ee.Image.pixelCoordinates`](#ee-image-pixelcoordinates)
- [`ee.Image.pixelLonLat`](#ee-image-pixellonlat)
- [`ee.Image.polynomial`](#ee-image-polynomial)
- [`ee.Image.pow`](#ee-image-pow)
- [`ee.Image.projection`](#ee-image-projection)
- [`ee.Image.propertyNames`](#ee-image-propertynames)
- [`ee.Image.random`](#ee-image-random)
- [`ee.Image.randomVisualizer`](#ee-image-randomvisualizer)
- [`ee.Image.reduce`](#ee-image-reduce)
- [`ee.Image.reduceConnectedComponents`](#ee-image-reduceconnectedcomponents)
- [`ee.Image.reduceNeighborhood`](#ee-image-reduceneighborhood)
- [`ee.Image.reduceRegion`](#ee-image-reduceregion)
- [`ee.Image.reduceRegions`](#ee-image-reduceregions)
- [`ee.Image.reduceResolution`](#ee-image-reduceresolution)
- [`ee.Image.reduceToVectors`](#ee-image-reducetovectors)
- [`ee.Image.regexpRename`](#ee-image-regexprename)
- [`ee.Image.register`](#ee-image-register)
- [`ee.Image.remap`](#ee-image-remap)
- [`ee.Image.rename`](#ee-image-rename)
- [`ee.Image.reproject`](#ee-image-reproject)
- [`ee.Image.resample`](#ee-image-resample)
- [`ee.Image.rgb`](#ee-image-rgb)
- [`ee.Image.rgbToHsv`](#ee-image-rgbtohsv)
- [`ee.Image.rightShift`](#ee-image-rightshift)
- [`ee.Image.round`](#ee-image-round)
- [`ee.Image.rsedTransform`](#ee-image-rsedtransform)
- [`ee.Image.sample`](#ee-image-sample)
- [`ee.Image.sampleRectangle`](#ee-image-samplerectangle)
- [`ee.Image.sampleRegions`](#ee-image-sampleregions)
- [`ee.Image.select`](#ee-image-select)
- [`ee.Image.selfMask`](#ee-image-selfmask)
- [`ee.Image.serialize`](#ee-image-serialize)
- [`ee.Image.set`](#ee-image-set)
- [`ee.Image.setDefaultProjection`](#ee-image-setdefaultprojection)
- [`ee.Image.short`](#ee-image-short)
- [`ee.Image.signum`](#ee-image-signum)
- [`ee.Image.sin`](#ee-image-sin)
- [`ee.Image.sinh`](#ee-image-sinh)
- [`ee.Image.sldStyle`](#ee-image-sldstyle)
- [`ee.Image.slice`](#ee-image-slice)
- [`ee.Image.spectralDilation`](#ee-image-spectraldilation)
- [`ee.Image.spectralDistance`](#ee-image-spectraldistance)
- [`ee.Image.spectralErosion`](#ee-image-spectralerosion)
- [`ee.Image.spectralGradient`](#ee-image-spectralgradient)
- [`ee.Image.sqrt`](#ee-image-sqrt)
- [`ee.Image.stratifiedSample`](#ee-image-stratifiedsample)
- [`ee.Image.subtract`](#ee-image-subtract)
- [`ee.Image.tan`](#ee-image-tan)
- [`ee.Image.tanh`](#ee-image-tanh)
- [`ee.Image.toArray`](#ee-image-toarray)
- [`ee.Image.toByte`](#ee-image-tobyte)
- [`ee.Image.toDictionary`](#ee-image-todictionary)
- [`ee.Image.toDouble`](#ee-image-todouble)
- [`ee.Image.toFloat`](#ee-image-tofloat)
- [`ee.Image.toInt`](#ee-image-toint)
- [`ee.Image.toInt16`](#ee-image-toint16)
- [`ee.Image.toInt32`](#ee-image-toint32)
- [`ee.Image.toInt64`](#ee-image-toint64)
- [`ee.Image.toInt8`](#ee-image-toint8)
- [`ee.Image.toLong`](#ee-image-tolong)
- [`ee.Image.toShort`](#ee-image-toshort)
- [`ee.Image.toUint16`](#ee-image-touint16)
- [`ee.Image.toUint32`](#ee-image-touint32)
- [`ee.Image.toUint8`](#ee-image-touint8)
- [`ee.Image.translate`](#ee-image-translate)
- [`ee.Image.trigamma`](#ee-image-trigamma)
- [`ee.Image.uint16`](#ee-image-uint16)
- [`ee.Image.uint32`](#ee-image-uint32)
- [`ee.Image.uint8`](#ee-image-uint8)
- [`ee.Image.unitScale`](#ee-image-unitscale)
- [`ee.Image.unmask`](#ee-image-unmask)
- [`ee.Image.unmix`](#ee-image-unmix)
- [`ee.Image.updateMask`](#ee-image-updatemask)
- [`ee.Image.visualize`](#ee-image-visualize)
- [`ee.Image.where`](#ee-image-where)
- [`ee.Image.zeroCrossing`](#ee-image-zerocrossing)
- [`ee.ImageCollection`](#ee-imagecollection)
- [`ee.ImageCollection.aggregate_array`](#ee-imagecollection-aggregate-array)
- [`ee.ImageCollection.aggregate_count`](#ee-imagecollection-aggregate-count)
- [`ee.ImageCollection.aggregate_count_distinct`](#ee-imagecollection-aggregate-count-distinct)
- [`ee.ImageCollection.aggregate_first`](#ee-imagecollection-aggregate-first)
- [`ee.ImageCollection.aggregate_histogram`](#ee-imagecollection-aggregate-histogram)
- [`ee.ImageCollection.aggregate_max`](#ee-imagecollection-aggregate-max)
- [`ee.ImageCollection.aggregate_mean`](#ee-imagecollection-aggregate-mean)
- [`ee.ImageCollection.aggregate_min`](#ee-imagecollection-aggregate-min)
- [`ee.ImageCollection.aggregate_product`](#ee-imagecollection-aggregate-product)
- [`ee.ImageCollection.aggregate_sample_sd`](#ee-imagecollection-aggregate-sample-sd)
- [`ee.ImageCollection.aggregate_sample_var`](#ee-imagecollection-aggregate-sample-var)
- [`ee.ImageCollection.aggregate_stats`](#ee-imagecollection-aggregate-stats)
- [`ee.ImageCollection.aggregate_sum`](#ee-imagecollection-aggregate-sum)
- [`ee.ImageCollection.aggregate_total_sd`](#ee-imagecollection-aggregate-total-sd)
- [`ee.ImageCollection.aggregate_total_var`](#ee-imagecollection-aggregate-total-var)
- [`ee.ImageCollection.and`](#ee-imagecollection-and)
- [`ee.ImageCollection.aside`](#ee-imagecollection-aside)
- [`ee.ImageCollection.bounds`](#ee-imagecollection-bounds)
- [`ee.ImageCollection.cast`](#ee-imagecollection-cast)
- [`ee.ImageCollection.combine`](#ee-imagecollection-combine)
- [`ee.ImageCollection.copyProperties`](#ee-imagecollection-copyproperties)
- [`ee.ImageCollection.count`](#ee-imagecollection-count)
- [`ee.ImageCollection.distance`](#ee-imagecollection-distance)
- [`ee.ImageCollection.distinct`](#ee-imagecollection-distinct)
- [`ee.ImageCollection.draw`](#ee-imagecollection-draw)
- [`ee.ImageCollection.errorMatrix`](#ee-imagecollection-errormatrix)
- [`ee.ImageCollection.evaluate`](#ee-imagecollection-evaluate)
- [`ee.ImageCollection.filter`](#ee-imagecollection-filter)
- [`ee.ImageCollection.filterBounds`](#ee-imagecollection-filterbounds)
- [`ee.ImageCollection.filterDate`](#ee-imagecollection-filterdate)
- [`ee.ImageCollection.first`](#ee-imagecollection-first)
- [`ee.ImageCollection.flatten`](#ee-imagecollection-flatten)
- [`ee.ImageCollection.formaTrend`](#ee-imagecollection-formatrend)
- [`ee.ImageCollection.fromImages`](#ee-imagecollection-fromimages)
- [`ee.ImageCollection.geometry`](#ee-imagecollection-geometry)
- [`ee.ImageCollection.get`](#ee-imagecollection-get)
- [`ee.ImageCollection.getArray`](#ee-imagecollection-getarray)
- [`ee.ImageCollection.getFilmstripThumbURL`](#ee-imagecollection-getfilmstripthumburl)
- [`ee.ImageCollection.getInfo`](#ee-imagecollection-getinfo)
- [`ee.ImageCollection.getMapId`](#ee-imagecollection-getmapid)
- [`ee.ImageCollection.getNumber`](#ee-imagecollection-getnumber)
- [`ee.ImageCollection.getRegion`](#ee-imagecollection-getregion)
- [`ee.ImageCollection.getString`](#ee-imagecollection-getstring)
- [`ee.ImageCollection.getVideoThumbURL`](#ee-imagecollection-getvideothumburl)
- [`ee.ImageCollection.iterate`](#ee-imagecollection-iterate)
- [`ee.ImageCollection.limit`](#ee-imagecollection-limit)
- [`ee.ImageCollection.linkCollection`](#ee-imagecollection-linkcollection)
- [`ee.ImageCollection.load`](#ee-imagecollection-load)
- [`ee.ImageCollection.loadZarrV2Array`](#ee-imagecollection-loadzarrv2array)
- [`ee.ImageCollection.map`](#ee-imagecollection-map)
- [`ee.ImageCollection.max`](#ee-imagecollection-max)
- [`ee.ImageCollection.mean`](#ee-imagecollection-mean)
- [`ee.ImageCollection.median`](#ee-imagecollection-median)
- [`ee.ImageCollection.merge`](#ee-imagecollection-merge)
- [`ee.ImageCollection.min`](#ee-imagecollection-min)
- [`ee.ImageCollection.mode`](#ee-imagecollection-mode)
- [`ee.ImageCollection.mosaic`](#ee-imagecollection-mosaic)
- [`ee.ImageCollection.or`](#ee-imagecollection-or)
- [`ee.ImageCollection.product`](#ee-imagecollection-product)
- [`ee.ImageCollection.propertyNames`](#ee-imagecollection-propertynames)
- [`ee.ImageCollection.qualityMosaic`](#ee-imagecollection-qualitymosaic)
- [`ee.ImageCollection.randomColumn`](#ee-imagecollection-randomcolumn)
- [`ee.ImageCollection.reduce`](#ee-imagecollection-reduce)
- [`ee.ImageCollection.reduceColumns`](#ee-imagecollection-reducecolumns)
- [`ee.ImageCollection.reduceToImage`](#ee-imagecollection-reducetoimage)
- [`ee.ImageCollection.remap`](#ee-imagecollection-remap)
- [`ee.ImageCollection.select`](#ee-imagecollection-select)
- [`ee.ImageCollection.serialize`](#ee-imagecollection-serialize)
- [`ee.ImageCollection.set`](#ee-imagecollection-set)
- [`ee.ImageCollection.size`](#ee-imagecollection-size)
- [`ee.ImageCollection.sort`](#ee-imagecollection-sort)
- [`ee.ImageCollection.style`](#ee-imagecollection-style)
- [`ee.ImageCollection.sum`](#ee-imagecollection-sum)
- [`ee.ImageCollection.toArray`](#ee-imagecollection-toarray)
- [`ee.ImageCollection.toArrayPerBand`](#ee-imagecollection-toarrayperband)
- [`ee.ImageCollection.toBands`](#ee-imagecollection-tobands)
- [`ee.ImageCollection.toDictionary`](#ee-imagecollection-todictionary)
- [`ee.ImageCollection.toList`](#ee-imagecollection-tolist)
- [`ee.ImageCollection.union`](#ee-imagecollection-union)
- [`ee.Kernel.add`](#ee-kernel-add)
- [`ee.Kernel.chebyshev`](#ee-kernel-chebyshev)
- [`ee.Kernel.circle`](#ee-kernel-circle)
- [`ee.Kernel.compass`](#ee-kernel-compass)
- [`ee.Kernel.cross`](#ee-kernel-cross)
- [`ee.Kernel.diamond`](#ee-kernel-diamond)
- [`ee.Kernel.euclidean`](#ee-kernel-euclidean)
- [`ee.Kernel.fixed`](#ee-kernel-fixed)
- [`ee.Kernel.gaussian`](#ee-kernel-gaussian)
- [`ee.Kernel.inverse`](#ee-kernel-inverse)
- [`ee.Kernel.kirsch`](#ee-kernel-kirsch)
- [`ee.Kernel.laplacian4`](#ee-kernel-laplacian4)
- [`ee.Kernel.laplacian8`](#ee-kernel-laplacian8)
- [`ee.Kernel.manhattan`](#ee-kernel-manhattan)
- [`ee.Kernel.octagon`](#ee-kernel-octagon)
- [`ee.Kernel.plus`](#ee-kernel-plus)
- [`ee.Kernel.prewitt`](#ee-kernel-prewitt)
- [`ee.Kernel.rectangle`](#ee-kernel-rectangle)
- [`ee.Kernel.roberts`](#ee-kernel-roberts)
- [`ee.Kernel.rotate`](#ee-kernel-rotate)
- [`ee.Kernel.sobel`](#ee-kernel-sobel)
- [`ee.Kernel.square`](#ee-kernel-square)
- [`ee.PixelType`](#ee-pixeltype)
- [`ee.PixelType.dimensions`](#ee-pixeltype-dimensions)
- [`ee.PixelType.double`](#ee-pixeltype-double)
- [`ee.PixelType.float`](#ee-pixeltype-float)
- [`ee.PixelType.int16`](#ee-pixeltype-int16)
- [`ee.PixelType.int32`](#ee-pixeltype-int32)
- [`ee.PixelType.int64`](#ee-pixeltype-int64)
- [`ee.PixelType.int8`](#ee-pixeltype-int8)
- [`ee.PixelType.maxValue`](#ee-pixeltype-maxvalue)
- [`ee.PixelType.minValue`](#ee-pixeltype-minvalue)
- [`ee.PixelType.precision`](#ee-pixeltype-precision)
- [`ee.PixelType.uint16`](#ee-pixeltype-uint16)
- [`ee.PixelType.uint32`](#ee-pixeltype-uint32)
- [`ee.PixelType.uint8`](#ee-pixeltype-uint8)
- [`ee.Terrain.aspect`](#ee-terrain-aspect)
- [`ee.Terrain.fillMinima`](#ee-terrain-fillminima)
- [`ee.Terrain.hillShadow`](#ee-terrain-hillshadow)
- [`ee.Terrain.hillshade`](#ee-terrain-hillshade)
- [`ee.Terrain.products`](#ee-terrain-products)
- [`ee.Terrain.slope`](#ee-terrain-slope)

---

## ee.Image

An object to represent an Earth Engine image. This constructor accepts a variety of arguments:

- A string: an Earth Engine asset id,

- A string and a number: an Earth Engine asset id and version,

- A number or ee.Array: creates a constant image,

- A list: creates an image out of each list element and combines them into a single image,

- An ee.Image: returns the argument,

- Nothing: results in an empty transparent image.

| Usage | Returns |
|---|---|
| `ee.Image(*args*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `args` | Image\|List\[Object\]\|Number\|Object\|String, optional | Constructor argument. |

## ee.Image.abs

Computes the absolute value of the input.

| Usage | Returns |
|---|---|
| `Image.abs()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.acos

Computes the arccosine in radians of the input.

| Usage | Returns |
|---|---|
| `Image.acos()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.add

Adds the first value to the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.add(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.addBands

Returns an image containing all bands copied from the first input and selected bands from the second input, optionally overwriting bands in the first image with the same name. The new image has the metadata and footprint from the first input image.

| Usage | Returns |
|---|---|
| `Image.addBands(srcImg, *names*, *overwrite*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `dstImg` | Image | An image into which to copy bands. |
| `srcImg` | Image | An image containing bands to copy. |
| `names` | List, default: null | Optional list of band names to copy. If names is omitted, all bands from srcImg will be copied over. |
| `overwrite` | Boolean, default: false | If true, bands from \`srcImg\` will override bands with the same names in \`dstImg\`. Otherwise the new band will be renamed with a numerical suffix (\`foo\` to \`foo_1\` unless \`foo_1\` exists, then \`foo_2\` unless it exists, etc). |

## ee.Image.and

Returns 1 if and only if both values are non-zero for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean.

| Usage | Returns |
|---|---|
| `Image.and(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.arrayAccum

Accumulates elements of each array pixel along the given axis, by setting each element of the result array pixel to the reduction of elements in that pixel along the given axis, up to and including the current position on the axis. May be used to make a cumulative sum, a monotonically increasing sequence, etc.

| Usage | Returns |
|---|---|
| `Image.arrayAccum(axis, *reducer*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |
| `axis` | Integer | Axis along which to perform the cumulative sum. |
| `reducer` | Reducer, default: null | Reducer to accumulate values. Default is SUM, to produce the cumulative sum of each vector along the given axis. |

## ee.Image.arrayArgmax

Computes the positional indices of the maximum value in image of array values. If there are multiple occurrences of the maximum, the indices reflect the first.

| Usage | Returns |
|---|---|
| `Image.arrayArgmax()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |

## ee.Image.arrayCat

Creates an array image by concatenating each array pixel along the given axis in each band.

| Usage | Returns |
|---|---|
| `Image.arrayCat(image2, axis)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | First array image to concatenate. |
| `image2` | Image | Second array image to concatenate. |
| `axis` | Integer | Axis to concatenate along. |

## ee.Image.arrayDimensions

Returns the number of dimensions in each array band, and 0 for scalar image bands.

| Usage | Returns |
|---|---|
| `Image.arrayDimensions()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |

## ee.Image.arrayDotProduct

Computes the dot product of each pair of 1-D arrays in the bands of the input images.

| Usage | Returns |
|---|---|
| `Image.arrayDotProduct(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | First array image of 1-D vectors. |
| `image2` | Image | Second array image of 1-D vectors. |

## ee.Image.arrayFlatten

Converts a single-band image of equal-shape multidimensional pixels to an image of scalar pixels, with one band for each element of the array.

| Usage | Returns |
|---|---|
| `Image.arrayFlatten(coordinateLabels, *separator*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Image of multidimensional pixels to flatten. |
| `coordinateLabels` | List | Name of each position along each axis. For example, 2x2 arrays with axes meaning 'day' and 'color' could have labels like \[\['monday', 'tuesday'\], \['red', 'green'\]\], resulting in band names'monday_red', 'monday_green', 'tuesday_red', and 'tuesday_green'. |
| `separator` | String, default: "_" | Separator between array labels in each band name. |

## ee.Image.arrayGet

For each band, an output band of the same name is created with the value at the given position extracted from the input multidimensional pixel in that band.

| Usage | Returns |
|---|---|
| `Image.arrayGet(position)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Array to get an element from. |
| `position` | Image | The coordinates of the element to get. There must be as many scalar bands as there are dimensions in the input image. |

## ee.Image.arrayLength

Returns the length of each pixel's array along the given axis.

| Usage | Returns |
|---|---|
| `Image.arrayLength(axis)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |
| `axis` | Integer | The axis along which to take the length. |

## ee.Image.arrayLengths

Returns a 1D array image with the length of each array axis.

| Usage | Returns |
|---|---|
| `Image.arrayLengths()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |

## ee.Image.arrayMask

Creates an array image where each array-valued pixel is masked with another array-valued pixel, retaining only the elements where the mask is non-zero. If the mask image has one band it will be applied to all the bands of 'input', otherwise they must have the same number of bands.

| Usage | Returns |
|---|---|
| `Image.arrayMask(mask)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Array image to mask. |
| `mask` | Image | Array image to mask with. |

## ee.Image.arrayPad

Pads the array values in each pixel to be a fixed length. The pad value will be appended to each array to extend it to given length along each axis. All bands of the image must be array-valued and have the same dimensions.

| Usage | Returns |
|---|---|
| `Image.arrayPad(lengths, *pad*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Array image to pad. |
| `lengths` | List | A list of desired lengths for each axis in the output arrays. Arrays are already as large or larger than the given length will be unchanged along that axis. |
| `pad` | Number, default: 0 | The value to pad with. |

## ee.Image.arrayProject

Projects the array in each pixel to a lower dimensional space by specifying the axes to retain. Dropped axes must be at most length 1.

| Usage | Returns |
|---|---|
| `Image.arrayProject(axes)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |
| `axes` | List | The axes to retain. Other axes will be discarded and must be at most length 1. |

## ee.Image.arrayReduce

Reduces elements of each array pixel.

| Usage | Returns |
|---|---|
| `Image.arrayReduce(reducer, axes, *fieldAxis*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |
| `reducer` | Reducer | The reducer to apply. |
| `axes` | List | The list of array axes to reduce in each pixel. The output will have a length of 1 in all these axes. |
| `fieldAxis` | Integer, default: null | The axis for the reducer's input and output fields. Only required if the reducer has multiple inputs or outputs. |

## ee.Image.arrayRepeat

Repeats each array pixel along the given axis. Each output pixel will have the shape of the input pixel, except length along the repeated axis, which will be multiplied by the number of copies.

| Usage | Returns |
|---|---|
| `Image.arrayRepeat(axis, copies)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Image of array pixels to be repeated. |
| `axis` | Integer | Axis along which to repeat each pixel's array. |
| `copies` | Image | Number of copies of each pixel. |

## ee.Image.arrayReshape

Converts array bands of an image with equally-shaped, possibly multidimensional pixels to an image of arrays with a new shape.

| Usage | Returns |
|---|---|
| `Image.arrayReshape(lengths, dimensions)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image of arrays to reshape. |
| `lengths` | Image | A 1-band image specifying the new lengths of each axis of the input image specified as a 1-D array per pixel. There should be 'dimensions' lengths values in each shape' array. If one of the lengths is -1, then the corresponding length for that axis will be computed such that the total size remains constant. In particular, a shape of \[-1\] flattens into 1-D. At most one component of shape can be -1. |
| `dimensions` | Integer | The number of dimensions shared by all output array pixels. |

## ee.Image.arraySlice

Creates a subarray by slicing out each position along the given axis from the 'start' (inclusive) to 'end' (exclusive) by increments of 'step'.

The result will have as many dimensions as the input, and the same length in all directions except the slicing axis, where the length will be the number of positions from 'start' to 'end' by 'step' that are in range of the input array's length along 'axis'. This means the result can be length 0 along the given axis if start=end, or if the start or end values are entirely out of range.

| Usage | Returns |
|---|---|
| `Image.arraySlice(*axis*, *start*, *end*, *step*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input array image. |
| `axis` | Integer, default: 0 | Axis to subset. |
| `start` | Image, default: null | The coordinate of the first slice (inclusive) along 'axis'. Negative numbers are used to position the start of slicing relative to the end of the array, where -1 starts at the last position on the axis, -2 starts at the next to last position, etc. There must one band for start indices, or one band per 'input' band. If this argument is not set or masked at some pixel, then the slice at that pixel will start at index 0. |
| `end` | Image, default: null | The coordinate (exclusive) at which to stop taking slices. By default this will be the length of the given axis. Negative numbers are used to position the end of slicing relative to the end of the array, where -1 will exclude the last position, -2 will exclude the last two positions, etc. There must be one band for end indices, or one band per 'input' band. If this argument is not set or masked at some pixel, then the slice at that pixel will end just after the last index. |
| `step` | Integer, default: 1 | The separation between slices along 'axis'; a slice will be taken at each whole multiple of 'step' from 'start' (inclusive) to 'end' (exclusive). Must be positive. |

## ee.Image.arraySort

Sorts elements of each array pixel along one axis.

| Usage | Returns |
|---|---|
| `Image.arraySort(*keys*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Array image to sort. |
| `keys` | Image, default: null | Optional keys to sort by. If not provided, the values are used as the keys. The keys can only have multiple elements along one axis, which determines the direction to sort in. |

## ee.Image.arrayTranspose

Transposes two dimensions of each array pixel.

| Usage | Returns |
|---|---|
| `Image.arrayTranspose(*axis1*, *axis2*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |
| `axis1` | Integer, default: 0 | First axis to swap. |
| `axis2` | Integer, default: 1 | Second axis to swap. |

## ee.Image.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Image.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Image.asin

Computes the arcsine in radians of the input.

| Usage | Returns |
|---|---|
| `Image.asin()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.atan

Computes the arctangent in radians of the input.

| Usage | Returns |
|---|---|
| `Image.atan()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.atan2

Calculates the angle formed by the 2D vector \[x, y\] for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is float.

| Usage | Returns |
|---|---|
| `Image.atan2(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.bandNames

Returns a list containing the names of the bands of an image.

| Usage | Returns |
|---|---|
| `Image.bandNames()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image from which to get band names. |

## ee.Image.bandTypes

Returns a dictionary of the image's band types.

| Usage | Returns |
|---|---|
| `Image.bandTypes()` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image from which to get band types. |

## ee.Image.bitCount

Calculates the number of one-bits in the 64-bit two's complement binary representation of the input.

| Usage | Returns |
|---|---|
| `Image.bitCount()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.bitsToArrayImage

Turns the bits of an integer into a 1-D array. The array has a length up to the highest 'on' bit in the input.

| Usage | Returns |
|---|---|
| `Image.bitsToArrayImage()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |

## ee.Image.bitwiseAnd

Calculates the bitwise AND of the input values for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.bitwiseAnd(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.bitwiseNot

Calculates the bitwise NOT of the input, in the smallest signed integer type that can hold the input.

| Usage | Returns |
|---|---|
| `Image.bitwiseNot()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.bitwiseOr

Calculates the bitwise OR of the input values for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.bitwiseOr(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.bitwiseXor

Calculates the bitwise XOR of the input values for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.bitwiseXor(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.blend

Overlays one image on top of another. The images are blended together using the masks as opacity. If either of images has only 1 band, it is replicated to match the number of bands in the other image.

| Usage | Returns |
|---|---|
| `Image.blend(top)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `bottom` | Image | The bottom image. |
| `top` | Image | The top image. |

## ee.Image.byte

Casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Image.byte()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.cast

Casts some or all bands of an image to the specified types.

| Usage | Returns |
|---|---|
| `Image.cast(bandTypes, *bandOrder*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to cast. |
| `bandTypes` | Dictionary | A dictionary from band name to band types. Types can be PixelTypes or strings. The valid strings are: 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'byte', 'short', 'int', 'long', 'float', and 'double'. If bandTypes includes bands that are not already in the input image, they will be added to the image as transparent bands. If bandOrder isn't also specified, new bands will be appended in alphabetical order. |
| `bandOrder` | List, default: null | A list specifying the order of the bands in the result. If specified, must match the full list of bands in the result. |

## ee.Image.cat

Combines the given images into a single image which contains all bands from all of the images.

If two or more bands share a name, they are suffixed with an incrementing index.

The resulting image will have the metadata from the first input image, only.

This function will promote constant values into constant images.

Returns the combined image.

| Usage | Returns |
|---|---|
| `ee.Image.cat(var_args)` | Image |

| Argument | Type | Details |
|---|---|---|
| `var_args` | VarArgs\[Image\] | The images to be combined. |

## ee.Image.cbrt

Computes the cubic root of the input.

| Usage | Returns |
|---|---|
| `Image.cbrt()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.ceil

Computes the smallest integer greater than or equal to the input.

| Usage | Returns |
|---|---|
| `Image.ceil()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.changeProj

Tweaks the projection of the input image, moving each pixel from its location in srcProj to the same coordinates in dstProj.

| Usage | Returns |
|---|---|
| `Image.changeProj(srcProj, dstProj)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image |   |
| `srcProj` | Projection | The original projection. |
| `dstProj` | Projection | The new projection. |

## ee.Image.clamp

Clamps the values in all bands of an image to all lie within the specified range.

| Usage | Returns |
|---|---|
| `Image.clamp(low, high)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The image to clamp. |
| `low` | Float | The minimum allowed value in the range. |
| `high` | Float | The maximum allowed value in the range. |

## ee.Image.classify

Classifies an image.

| Usage | Returns |
|---|---|
| `Image.classify(classifier, *outputName*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to classify. Bands are extracted from this image by name and it must contain all the bands named in the classifier's schema. |
| `classifier` | Classifier | The classifier to use. |
| `outputName` | String, default: "classification" | The name of the band to be added. If the classifier produces more than 1 output, this name is ignored. |

## ee.Image.clip

Clips an image to a Geometry or Feature.

The output bands correspond exactly to the input bands, except data not covered by the geometry is masked. The output image retains the metadata of the input image.

Use clipToCollection to clip an image to a FeatureCollection.

Returns the clipped image.

| Usage | Returns |
|---|---|
| `Image.clip(geometry)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `geometry` | Feature\|Geometry\|Object | The Geometry or Feature to clip to. |

## ee.Image.clipToBoundsAndScale

Clips an image to the bounds of a Geometry, and scales the clipped image to a particular size or scale.

> [!CAUTION]
> **Caution:** providing a large or complex collection as the `geometry` argument can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.

| Usage | Returns |
|---|---|
| `Image.clipToBoundsAndScale(*geometry*, *width*, *height*, *maxDimension*, *scale*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The image to clip and scale. |
| `geometry` | Geometry, default: null | The Geometry to clip the image to. The image will be clipped to the bounding box, in the image's projection, of this geometry. |
| `width` | Integer, default: null | The width to scale the image to, in pixels. Must be provided along with "height". Exclusive with "maxDimension" and "scale". |
| `height` | Integer, default: null | The height to scale the image to, in pixels. Must be provided along with "width". Exclusive with "maxDimension" and "scale". |
| `maxDimension` | Integer, default: null | The maximum dimension to scale the image to, in pixels. Exclusive with "width", "height" and "scale". |
| `scale` | Float, default: null | If scale is specified, then the projection is scaled by dividing the specified scale value by the nominal size of a meter in the image's projection. Exclusive with "width", "height", and "maxDimension". |

## ee.Image.clipToCollection

Clips an image to a FeatureCollection. The output bands correspond exactly the input bands, except data not covered by the geometry of at least one feature from the collection is masked. The output image retains the metadata of the input image.

| Usage | Returns |
|---|---|
| `Image.clipToCollection(collection)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The image to clip. |
| `collection` | Object | The FeatureCollection to clip to. |

## ee.Image.cluster

Applies a clusterer to an image. Returns a new image with a single band containing values from 0 to N, indicating the cluster each pixel is assigned to.

| Usage | Returns |
|---|---|
| `Image.cluster(clusterer, *outputName*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to cluster. Must contain all the bands in the clusterer's schema. |
| `clusterer` | Clusterer | The clusterer to use. |
| `outputName` | String, default: "cluster" | The name of the output band. |

## ee.Image.connectedComponents

Finds connected components with the same value of the first band of the input and labels them with a globally unique value. Connectedness is specified by the given kernel. Objects larger than maxSize are considered background, and are masked.

| Usage | Returns |
|---|---|
| `Image.connectedComponents(connectedness, maxSize)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to label. |
| `connectedness` | Kernel | Connectedness kernel. |
| `maxSize` | Integer | Maximum size of objects to be labeled. |

## ee.Image.connectedPixelCount

Generate an image where each pixel contains the number of 4- or 8-connected neighbors (including itself).

| Usage | Returns |
|---|---|
| `Image.connectedPixelCount(*maxSize*, *eightConnected*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The input image. |
| `maxSize` | Integer, default: 100 | The maximum size of the neighborhood in pixels. |
| `eightConnected` | Boolean, default: true | Whether to use 8-connected rather 4-connected rules. |

## ee.Image.constant

Generates an image containing a constant value everywhere.

| Usage | Returns |
|---|---|
| `ee.Image.constant(value)` | Image |

| Argument | Type | Details |
|---|---|---|
| `value` | Object | The value of the pixels in the constant image. Must be a number or an Array or a list of numbers or Arrays. |

## ee.Image.convolve

Convolves each band of an image with the given kernel.

| Usage | Returns |
|---|---|
| `Image.convolve(kernel)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to convolve. |
| `kernel` | Kernel | The kernel to convolve with. |

## ee.Image.copyProperties

Copies metadata properties from one element to another.

| Usage | Returns |
|---|---|
| `Image.copyProperties(*source*, *properties*, *exclude*)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `destination` | Element, default: null | The object whose properties to override. |
| `source` | Element, default: null | The object from which to copy the properties. |
| `properties` | List, default: null | The properties to copy. If omitted, all ordinary (i.e. non-system) properties are copied. |
| `exclude` | List, default: null | The list of properties to exclude when copying all properties. Must not be specified if properties is. |

## ee.Image.cos

Computes the cosine of the input in radians.

| Usage | Returns |
|---|---|
| `Image.cos()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.cosh

Computes the hyperbolic cosine of the input.

| Usage | Returns |
|---|---|
| `Image.cosh()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.cumulativeCost

Computes a cumulative cost map based on an image containing costs to traverse each pixel and an image containing source locations.

Each output band represents the cumulative cost over the corresponding input cost band.

| Usage | Returns |
|---|---|
| `Image.cumulativeCost(source, maxDistance, *geodeticDistance*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `cost` | Image | An image representing the cost to traverse each pixel. Masked pixels can't be traversed. When comparing pixel traversal costs, we use band-wise dictionary ordering. Ancillary cost bands are only considered when paths over primary bands are equal cost. |
| `source` | Image | A single-band image representing the sources. A pixel value different from 0 defines a source pixel. |
| `maxDistance` | Float | Maximum distance for computation, in meters. |
| `geodeticDistance` | Boolean, default: true | If true, geodetic distance along the curved surface is used, assuming a spherical Earth of radius 6378137.0. If false, Euclidean distance in the 2D plane of the map projection is used (faster, but less accurate). |

## ee.Image.date

Returns the acquisition time of an image as a Date object. This helper function is equivalent to `ee.Date(image.get('system:time_start'))`.

| Usage | Returns |
|---|---|
| `Image.date()` | Date |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image whose acquisition time to return. |

## ee.Image.derivative

Computes the X and Y discrete derivatives for each band in the input image, in pixel coordinates.

For each band of the input image, the output image will have two bands named with the suffixes `_x` and `_y`, containing the respective derivatives.

| Usage | Returns |
|---|---|
| `Image.derivative()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |

## ee.Image.digamma

Computes the digamma function of the input.

| Usage | Returns |
|---|---|
| `Image.digamma()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.directionalDistanceTransform

For each zero-valued pixel in the source, get the distance to the nearest non-zero pixels in the given direction.

Returns a band of floating point distances called distance.

| Usage | Returns |
|---|---|
| `Image.directionalDistanceTransform(angle, maxDistance, *labelBand*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `source` | Image | The source image. |
| `angle` | Float | The angle, in degrees, at which to search for non-zero pixels. |
| `maxDistance` | Integer | The maximum distance, in pixels, over which to search. |
| `labelBand` | String, default: null | If provided, multi-band inputs are permitted and only this band is used for searching. All other bands are returned and populated with the per-band values found at the searched non-zero pixels in the label band. |

## ee.Image.displace

Warps an image using an image of displacements.

| Usage | Returns |
|---|---|
| `Image.displace(displacement, *mode*, *maxOffset*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to warp. |
| `displacement` | Image | An image containing displacement values. The first band is interpreted as the 'X' displacement and the second as the 'Y' displacement. Each displacement pixel is a \[dx,dy\] vector added to the pixel location to determine the corresponding pixel location in 'image'. Displacements are interpreted as meters in the default projection of the displacement image. |
| `mode` | String, default: "bicubic" | The interpolation mode to use. One of 'nearest_neighbor', 'bilinear', or 'bicubic'. |
| `maxOffset` | Float, default: null | The maximum absolute offset in the displacement image. Providing this may improve processing performance. |

## ee.Image.displacement

Determines displacements required to register an image to a reference image while allowing local, rubber sheet deformations. Displacements are computed in the CRS of the reference image, at a scale dictated by the lowest resolution of the following three projections: input image projection, reference image projection, and requested projection. The displacements are then transformed into the user-specified projection for output.

| Usage | Returns |
|---|---|
| `Image.displacement(referenceImage, maxOffset, *projection*, *patchWidth*, *stiffness*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to register. |
| `referenceImage` | Image | The image to register to. |
| `maxOffset` | Float | The maximum offset allowed when attempting to align the input images, in meters. Using a smaller value can reduce computation time significantly, but it must still be large enough to cover the greatest displacement within the entire image region. |
| `projection` | Projection, default: null | The projection in which to output displacement values. The default is the projection of the first band of the reference image. |
| `patchWidth` | Float, default: null | Patch size for detecting image offsets, in meters. This should be set large enough to capture texture, as well as large enough that ignorable objects are small within the patch. Default is null. Patch size will be determined automatically if not provided. |
| `stiffness` | Float, default: 5 | Enforces a stiffness constraint on the solution. Valid values are in the range \[0,10\]. The stiffness is used for outlier rejection when determining displacements at adjacent grid points. Higher values move the solution towards a rigid transformation. Lower values allow more distortion or warping of the image during registration. |

## ee.Image.distance

Computes the distance to the nearest non-zero pixel in each band, using the specified distance kernel.

| Usage | Returns |
|---|---|
| `Image.distance(*kernel*, *skipMasked*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `kernel` | Kernel, default: null | The distance kernel. One of chebyshev, euclidean, or manhattan. |
| `skipMasked` | Boolean, default: true | Mask output pixels if the corresponding input pixel is masked. |

## ee.Image.divide

Divides the first value by the second, returning 0 for division by 0 for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.divide(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.double

Casts the input value to a 64-bit float.

| Usage | Returns |
|---|---|
| `Image.double()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.entropy

Computes the windowed entropy for each band using the specified kernel centered on each input pixel. Entropy is computed as -sum(p \* log2(p)), where p is the normalized probability of occurrence of the values encountered in each window.

| Usage | Returns |
|---|---|
| `Image.entropy(kernel)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image for which to compute the entropy. |
| `kernel` | Kernel | A kernel specifying the window in which to compute. |

## ee.Image.eq

Returns 1 if and only if the first value is equal to the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean.

| Usage | Returns |
|---|---|
| `Image.eq(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.erf

Computes the error function of the input.

| Usage | Returns |
|---|---|
| `Image.erf()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.erfInv

Computes the inverse error function of the input.

| Usage | Returns |
|---|---|
| `Image.erfInv()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.erfc

Computes the complementary error function of the input.

| Usage | Returns |
|---|---|
| `Image.erfc()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.erfcInv

Computes the inverse complementary error function of the input.

| Usage | Returns |
|---|---|
| `Image.erfcInv()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Image.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Image.exp

Computes the Euler's number e raised to the power of the input.

| Usage | Returns |
|---|---|
| `Image.exp()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.expression

Evaluates an arithmetic expression on an image, possibly involving additional images.

The bands of the primary input image are available using the built-in function b(), as b(0) or b('band_name').

Variables in the expression are interpreted as additional image parameters which must be supplied in opt_map. The bands of each such image can be accessed like image.band_name or image\[0\].

Both b() and image\[\] allow multiple arguments, to specify multiple bands, such as b(1, 'name', 3). Calling b() with no arguments, or using a variable by itself, returns all bands of the image.

If the result of an expression is a single band, it can be assigned a name using the '=' operator (e.g.: x = a + b).

Returns the image computed by the provided expression.

| Usage | Returns |
|---|---|
| `Image.expression(expression, *map*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `expression` | String | The expression to evaluate. |
| `map` | Dictionary\[Image\], optional | A map of input images available by name. |

## ee.Image.fastDistanceTransform

Returns the distance, as determined by the specified distance metric, to the nearest non-zero valued pixel in the input. The output contains values for all pixels within the given neighborhood size, regardless of the input's mask. Note: the default distance metric returns squared distance.

| Usage | Returns |
|---|---|
| `Image.fastDistanceTransform(*neighborhood*, *units*, *metric*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `neighborhood` | Integer, default: 256 | Neighborhood size in pixels. |
| `units` | String, default: "pixels" | The units of the neighborhood, currently only 'pixels' are supported. |
| `metric` | String, default: "squared_euclidean" | Distance metric to use: options are \`squared_euclidean\`, \`manhattan\` or \`chebyshev\`. |

## ee.Image.first

Selects the value of the first value for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.first(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.firstNonZero

Selects the first value if it is non-zero, and the second value otherwise for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.firstNonZero(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.float

Casts the input value to a 32-bit float.

| Usage | Returns |
|---|---|
| `Image.float()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.floor

Computes the largest integer less than or equal to the input.

| Usage | Returns |
|---|---|
| `Image.floor()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.focalMax

Applies a morphological reducer() filter to each band of an image using a named or custom kernel.

| Usage | Returns |
|---|---|
| `Image.focalMax(*radius*, *kernelType*, *units*, *iterations*, *kernel*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to which to apply the operations. |
| `radius` | Float, default: 1.5 | The radius of the kernel to use. |
| `kernelType` | String, default: "circle" | The type of kernel to use. Options include: 'circle', 'square', 'cross', 'plus', 'octagon', and 'diamond'. |
| `units` | String, default: "pixels" | If a kernel is not specified, this determines whether the kernel is in meters or pixels. |
| `iterations` | Integer, default: 1 | The number of times to apply the given kernel. |
| `kernel` | Kernel, default: null | A custom kernel. If used, kernelType and radius are ignored. |

## ee.Image.focalMean

Applies a morphological mean filter to each band of an image using a named or custom kernel.

| Usage | Returns |
|---|---|
| `Image.focalMean(*radius*, *kernelType*, *units*, *iterations*, *kernel*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to which to apply the operations. |
| `radius` | Float, default: 1.5 | The radius of the kernel to use. |
| `kernelType` | String, default: "circle" | The type of kernel to use. Options include: 'circle', 'square', 'cross', 'plus', 'octagon', and 'diamond'. |
| `units` | String, default: "pixels" | If a kernel is not specified, this determines whether the kernel is in meters or pixels. |
| `iterations` | Integer, default: 1 | The number of times to apply the given kernel. |
| `kernel` | Kernel, default: null | A custom kernel. If used, kernelType and radius are ignored. |

## ee.Image.focalMedian

Applies a morphological reducer() filter to each band of an image using a named or custom kernel.

| Usage | Returns |
|---|---|
| `Image.focalMedian(*radius*, *kernelType*, *units*, *iterations*, *kernel*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to which to apply the operations. |
| `radius` | Float, default: 1.5 | The radius of the kernel to use. |
| `kernelType` | String, default: "circle" | The type of kernel to use. Options include: 'circle', 'square', 'cross', 'plus', 'octagon', and 'diamond'. |
| `units` | String, default: "pixels" | If a kernel is not specified, this determines whether the kernel is in meters or pixels. |
| `iterations` | Integer, default: 1 | The number of times to apply the given kernel. |
| `kernel` | Kernel, default: null | A custom kernel. If used, kernelType and radius are ignored. |

## ee.Image.focalMin

Applies a morphological reducer() filter to each band of an image using a named or custom kernel.

| Usage | Returns |
|---|---|
| `Image.focalMin(*radius*, *kernelType*, *units*, *iterations*, *kernel*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to which to apply the operations. |
| `radius` | Float, default: 1.5 | The radius of the kernel to use. |
| `kernelType` | String, default: "circle" | The type of kernel to use. Options include: 'circle', 'square', 'cross', 'plus', 'octagon', and 'diamond'. |
| `units` | String, default: "pixels" | If a kernel is not specified, this determines whether the kernel is in meters or pixels. |
| `iterations` | Integer, default: 1 | The number of times to apply the given kernel. |
| `kernel` | Kernel, default: null | A custom kernel. If used, kernelType and radius are ignored. |

## ee.Image.focalMode

Applies a morphological reducer() filter to each band of an image using a named or custom kernel.

| Usage | Returns |
|---|---|
| `Image.focalMode(*radius*, *kernelType*, *units*, *iterations*, *kernel*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to which to apply the operations. |
| `radius` | Float, default: 1.5 | The radius of the kernel to use. |
| `kernelType` | String, default: "circle" | The type of kernel to use. Options include: 'circle', 'square', 'cross', 'plus', 'octagon', and 'diamond'. |
| `units` | String, default: "pixels" | If a kernel is not specified, this determines whether the kernel is in meters or pixels. |
| `iterations` | Integer, default: 1 | The number of times to apply the given kernel. |
| `kernel` | Kernel, default: null | A custom kernel. If used, kernelType and radius are ignored. |

## ee.Image.gamma

Computes the gamma function of the input.

| Usage | Returns |
|---|---|
| `Image.gamma()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.gammainc

Calculates the regularized lower incomplete Gamma function γ(x,a) for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is float.

| Usage | Returns |
|---|---|
| `Image.gammainc(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.geometry

Returns the geometry of a given feature in a given projection.

| Usage | Returns |
|---|---|
| `Image.geometry(*maxError*, *proj*, *geodesics*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `feature` | Element | The feature from which the geometry is taken. |
| `maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, default: null | If specified, the geometry will be in this projection. If unspecified, the geometry will be in its default projection. |
| `geodesics` | Boolean, default: null | If true, the geometry will have geodesic edges. If false, it will have edges as straight lines in the specified projection. If null, the edge interpretation will be the same as the original geometry. This argument is ignored if proj is not specified. |

## ee.Image.get

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `Image.get(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.Image.getArray

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `Image.getArray(property)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.Image.getDownloadURL

Get a download URL for small chunks of image data in GeoTIFF or NumPy format. Maximum request size is 32 MB, maximum grid dimension is 10000.

Use getThumbURL for RGB visualization formats PNG and JPG.

Returns returns a download URL, or undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `Image.getDownloadURL(params, *callback*)` | Object\|String |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `params` | Object | An object containing download options with the following possible values: |---| | ` name: ` a base name to use when constructing filenames. Only applicable when format is "ZIPPED_GEO_TIFF" (default) or filePerBand is true. Defaults to the image id (or "download" for computed images) when format is "ZIPPED_GEO_TIFF" or filePerBand is true, otherwise a random character string is generated. Band names are appended when filePerBand is true. | | ` bands: ` a description of the bands to download. Must be an array of band names or an array of dictionaries, each with the following keys (optional parameters apply only when filePerBand is true): - ` id: ` the name of the band, a string, required. - ` crs: ` an optional CRS string defining the band projection. - ` crs_transform: ` an optional array of 6 numbers specifying an affine transform from the specified CRS, in row-major order: \[xScale, xShearing, xTranslation, yShearing, yScale, yTranslation\] - ` dimensions: ` an optional array of two integers defining the width and height to which the band is cropped. - ` scale: ` an optional number, specifying the scale in meters of the band; ignored if crs and crs_transform are specified. | | ` crs: ` a default CRS string to use for any bands that do not explicitly specify one. | | ` crs_transform: ` a default affine transform to use for any bands that do not specify one, of the same format as the `crs_transform` of bands. | | ` dimensions: ` default image cropping dimensions to use for any bands that do not specify them. | | ` scale: ` a default scale to use for any bands that do not specify one; ignored if `crs` and `crs_transform` are specified. | | ` region: ` a polygon specifying a region to download; ignored if `crs` and `crs_transform` is specified. | | ` filePerBand: ` whether to produce a separate GeoTIFF per band (boolean). Defaults to true. If false, a single GeoTIFF is produced and all band-level transformations will be ignored. | | ` format: ` the download format. One of: - "ZIPPED_GEO_TIFF" (GeoTIFF file(s) wrapped in a zip file, default) - "GEO_TIFF" (GeoTIFF file) - "NPY" (NumPy binary format) If "GEO_TIFF" or "NPY", filePerBand and all band-level transformations will be ignored. Loading a NumPy output results in a structured array. | |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Image.getInfo

An imperative function that returns information about this image via an AJAX call.

Returns a description of the image, or undefined if a callback is specified. Includes:

- bands - a list containing metadata about the bands in the collection.

- properties - a dictionary containing the image's metadata properties.

| Usage | Returns |
|---|---|
| `Image.getInfo(*callback*)` | ImageDescription\|Object |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. If supplied, will be called with the first parameter if successful and the second if unsuccessful. |

## ee.Image.getMapId

An imperative function that returns a map ID and optional token, suitable for generating a Map overlay.

Returns an object which may be passed to ee.data.getTileUrl or ui.Map.addLayer. Undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `Image.getMapId(*visParams*, *callback*)` | MapId\|Object |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `visParams` | ImageVisualizationParameters, optional | The visualization parameters. |
| `callback` | Function, optional | An async callback. If not supplied, the call is made synchronously. |

## ee.Image.getNumber

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `Image.getNumber(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.Image.getString

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `Image.getString(property)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.Image.getThumbId

Applies transformations and returns the thumbId.

Returns the thumb ID and optional token, or null if a callback is specified.

| Usage | Returns |
|---|---|
| `Image.getThumbId(params, *callback*)` | ThumbnailId |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `params` | Object | Parameters identical to ee.data.getMapId, plus, optionally: |---| | ` dimensions ` (a number or pair of numbers in format WIDTHxHEIGHT) Maximum dimensions of the thumbnail to render, in pixels. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling. | | ` region ` Geospatial region of the image to render, it may be an ee.Geometry, GeoJSON, or an array of lat/lon points (E,S,W,N). If not set the default is the bounds image. | |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Image.getThumbURL

Get a thumbnail URL for this image.

Returns a thumbnail URL, or undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `Image.getThumbURL(params, *callback*)` | Object\|String |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `params` | Object | Parameters identical to ee.data.getMapId, plus, optionally: |---| | ` dimensions ` (a number or pair of numbers in format WIDTHxHEIGHT) Maximum dimensions of the thumbnail to render, in pixels. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling. | | ` region ` Geospatial region of the image to render, it may be an ee.Geometry, GeoJSON, or an array of lat/lon points (E,S,W,N). If not set the default is the bounds image. | | ` format ` (string) Either 'png' or 'jpg'. | |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Image.glcmTexture

Computes texture metrics from the Gray Level Co-occurrence Matrix around each pixel of every band. The GLCM is a tabulation of how often different combinations of pixel brightness values (grey levels) occur in an image. It counts the number of times a pixel of value X lies next to a pixel of value Y, in a particular direction and distance. and then derives statistics from this tabulation.

This implementation computes the 14 GLCM metrics proposed by Haralick, and 4 additional metrics from Conners. Inputs are required to be integer valued.

The output consists of 18 bands per input band if directional averaging is on and 18 bands per directional pair in the kernel, if not:

- **ASM:** f1, Angular Second Moment; measures the number of repeated pairs
- **CONTRAST:** f2, Contrast; measures the local contrast of an image
- **CORR:** f3, Correlation; measures the correlation between pairs of pixels
- **VAR:** f4, Variance; measures how spread out the distribution of gray-levels is
- **IDM:** f5, Inverse Difference Moment; measures the homogeneity
- **SAVG:** f6, Sum Average
- **SVAR:** f7, Sum Variance
- **SENT:** f8, Sum Entropy
- **ENT:** f9, Entropy. Measures the randomness of a gray-level distribution
- **DVAR:** f10, Difference variance
- **DENT:** f11, Difference entropy
- **IMCORR1:** f12, Information Measure of Corr. 1
- **IMCORR2:** f13, Information Measure of Corr. 2
- **MAXCORR:** f14, Max Corr. Coefficient. (not computed)
- **DISS:** Dissimilarity
- **INERTIA:** Inertia
- **SHADE:** Cluster Shade
- **PROM:** Cluster prominence

More information can be found in the two papers: Haralick et. al, 'Textural Features for Image Classification', https://doi.org/10.1109/TSMC.1973.4309314 and Conners, et al, 'Segmentation of a high-resolution urban scene using texture operators', https://doi.org/10.1016/0734-189X(84)90197-X.

<br />

| Usage | Returns |
|---|---|
| `Image.glcmTexture(*size*, *kernel*, *average*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image for which to compute texture metrics. |
| `size` | Integer, default: 1 | The size of the neighborhood to include in each GLCM. For example, the size of 1 corresponds to a 3x3 square, the size of 2 corresponds to a 5x5 square, the size of 3 corresponds to a 7x7 square, etc. |
| `kernel` | Kernel, default: null | A kernel specifying the x and y offsets over which to compute the GLCMs. A GLCM is computed for each pixel in the kernel that is non-zero, except the center pixel and as long as a GLCM hasn't already been computed for the same direction and distance. For example, if either or both of the east and west pixels are set, only 1 (horizontal) GLCM is computed. Kernels are scanned from left to right and top to bottom. The default is a 3x3 square, resulting in 4 GLCMs with the offsets (-1, -1), (0, -1), (1, -1) and (-1, 0). |
| `average` | Boolean, default: true | If true, the directional bands for each metric are averaged. |

## ee.Image.gradient

Calculates the x and y gradient.

| Usage | Returns |
|---|---|
| `Image.gradient()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The input image. |

## ee.Image.gt

Returns 1 if and only if the first value is greater than the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean.

| Usage | Returns |
|---|---|
| `Image.gt(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.gte

Returns 1 if and only if the first value is greater than or equal to the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean.

| Usage | Returns |
|---|---|
| `Image.gte(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.hersDescriptor

Creates a dictionary of Histogram Error Ring Statistic (HERS) descriptor arrays from square array properties of an element. The HERS radius is taken to be the array's (side_length - 1) / 2.

| Usage | Returns |
|---|---|
| `Image.hersDescriptor(*selectors*, *buckets*, *peakWidthScale*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The element with array properties. |
| `selectors` | List, default: null | The array properties for which descriptors will be created. Selected array properties must be square, floating point arrays. Defaults to all array properties. |
| `buckets` | Integer, default: 100 | The number of HERS buckets. Defaults to 100. |
| `peakWidthScale` | Float, default: 1 | The HERS peak width scale. Defaults to 1.0. |

## ee.Image.hersFeature

Computes the Histogram Error Ring Statistic (HERS) for each pixel in each band matching the keys in the descriptor. Only the bands for which HERS could be computed are returned.

| Usage | Returns |
|---|---|
| `Image.hersFeature(reference, *peakWidthScale*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `reference` | Dictionary | The reference descriptor computed with ee.Feature.hersDescriptor(...). |
| `peakWidthScale` | Float, default: 1 | The HERS peak width scale. |

## ee.Image.hersImage

Computes the Histogram Error Ring Statistic (HERS) for each pair of pixels in each band present in both images. Only the bands for which HERS could be computed are returned.

| Usage | Returns |
|---|---|
| `Image.hersImage(image2, radius, *buckets*, *peakWidthScale*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `image2` | Image | The image to compare. |
| `radius` | Integer | The radius of the window. |
| `buckets` | Integer, default: 100 | The number of HERS buckets. |
| `peakWidthScale` | Float, default: 1 | The HERS peak width scale. |

## ee.Image.hsvToRgb

Transforms the image from the HSV color space to the RGB color space. Expects a 3-band image in the range \[0, 1\], and produces 3 bands: red, green and blue with values in the range \[0, 1\].

| Usage | Returns |
|---|---|
| `Image.hsvToRgb()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to transform. |

## ee.Image.hypot

Calculates the magnitude of the 2D vector \[x, y\] for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is float.

| Usage | Returns |
|---|---|
| `Image.hypot(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.id

Returns the ID of a given element within a collection. Objects outside collections are not guaranteed to have IDs.

| Usage | Returns |
|---|---|
| `Image.id()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The element from which the ID is taken. |

## ee.Image.int

Casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Image.int()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.int16

Casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Image.int16()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.int32

Casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Image.int32()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.int64

Casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Image.int64()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.int8

Casts the input value to a signed 8-bit integer.

| Usage | Returns |
|---|---|
| `Image.int8()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.interpolate

Interpolates each point in the first band of the input image into the piecewise-linear function specified by the x and y arrays. The x values must be strictly increasing. If an input point is less than the first or greater than the last x value, then the output is specified by the "behavior" argument:

1. "extrapolate" specifies the output value is extrapolated from the two nearest points.
2. "clamp" specifies the output value is taken from the nearest point.
3. "input" specifies the output value is copied from the input.
4. "mask" specifies the output value is masked.

<br />

| Usage | Returns |
|---|---|
| `Image.interpolate(x, y, *behavior*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to which the interpolation is applied. |
| `x` | List | The x axis (input) values in the piecewise function. |
| `y` | List | The y axis (output) values in the piecewise function. |
| `behavior` | String, default: "extrapolate" | The behavior for points that are outside of the range of the supplied function. Options are: 'extrapolate', 'clamp', 'mask', or 'input'. |

## ee.Image.lanczos

Computes the Lanczos approximation of the input.

| Usage | Returns |
|---|---|
| `Image.lanczos()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.leftShift

Calculates the left shift of v1 by v2 bits for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.leftShift(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.linkCollection

Links the source image to a matching image from an image collection.

Any specified bands or metadata will be added to the source image from the image found in the collection, and if the bands or metadata are already present they will be overwritten. If a matching image is not found, any new or updated bands will be fully masked and any new or updated metadata will be null. The output footprint will be the same as the source image footprint.

A match is determined if the source image and an image in the collection have a specific equivalent metadata property. If more than one collection image would match, the collection image selected is arbitrary. By default, images are matched on their 'system:index' metadata property.

This linking function is a convenience method for adding bands to a target image based on a specified shared metadata property and is intended to support linking collections that apply different processing/product generation to the same source imagery. For more expressive linking known as 'joining', see https://developers.google.com/earth-engine/guides/joins_intro.

| Usage | Returns |
|---|---|
| `Image.linkCollection(imageCollection, *linkedBands*, *linkedProperties*, *matchPropertyName*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The source image a matching image in the collection will be linked to. |
| `imageCollection` | ImageCollection | The image collection searched to extract an image matching the source. |
| `linkedBands` | Object, default: null | A band name or list of band names to add or update from the matching image. |
| `linkedProperties` | Object, default: null | A metadata property or list of properties to add or update from the matching image. |
| `matchPropertyName` | String, default: "system:index" | The metadata property name to use as a match criteria. |

## ee.Image.load

Returns the image given its ID.

| Usage | Returns |
|---|---|
| `ee.Image.load(id, *version*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `id` | String | The asset ID of the image. |
| `version` | Long, default: -1 | The version of the asset. -1 signifies the latest version. |

## ee.Image.loadGeoTIFF

Loads a GeoTIFF as an Image.

| Usage | Returns |
|---|---|
| `ee.Image.loadGeoTIFF(uri)` | Image |

| Argument | Type | Details |
|---|---|---|
| `uri` | String | The Cloud Storage URI of the GeoTIFF to load. The bucket metadata must be accessible (requires the \`storage.buckets.get\` permission which is provided by the role "Storage Legacy Bucket Reader" among others, see https://cloud.google.com/storage/docs/access-control/iam-roles) and the bucket must be located in the US multi-region, a dual-region including US-CENTRAL1, or the US-CENTRAL1 region. |

## ee.Image.loadZarrV2Array

Loads a Zarr v2 array as an Image. The array attributes (.zattrs) must contain the field '_ARRAY_DIMENSIONS', which is a list of the names of each dimension (e.g., \['time', 'y', 'x'\]). There must be at least two dimensions, with the final two representing Y and X respectively (e.g., \['lat', 'lon'\]). The supported compression codecs are 'blosc', 'gzip', 'lz4', 'zlib', and 'zstd'. The supported blosc meta-compression codecs are 'lz4', lz4hc', 'zlib', and 'zstd' ('blosclz' is not supported).

| Usage | Returns |
|---|---|
| `ee.Image.loadZarrV2Array(uri, proj, *starts*, *ends*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `uri` | String | The Cloud Storage URI of the .zarray file to load. A .zmetadata file must be present in the parent directory of the array's directory (e.g., for 'gs://b/o/.zarray', 'gs://b/.zmetadata' must be present). The bucket metadata must be accessible (requires the \`storage.buckets.get\` permission which is provided by the role "Storage Legacy Bucket Reader" among others, see https://cloud.google.com/storage/docs/access-control/iam-roles) and the bucket must be located in the US multi-region, a dual-region including US-CENTRAL1, or the US-CENTRAL1 region. |
| `proj` | Projection | The projection of the array. |
| `starts` | List, default: null | The indices (inclusive) at which to start taking slices along each non-spatial dimension. If null, slices will start at index 0 for all non-spatial dimensions. If specified, this list must have a length equal to the number of non-spatial dimensions (total dimensions - 2). An individual element within the list may be null, which defaults to 0 for that dimension. Negative indices are counted from the end of the dimension (e.g., -1 is the last element). |
| `ends` | List, default: null | The indices (exclusive) at which to stop taking slices along each non-spatial dimension. If null, slices will extend to the end of each corresponding non-spatial dimension (i.e., defaults to the length of the dimension). If specified, this list must have a length equal to the number of non-spatial dimensions (total dimensions - 2). An individual element within the list may be null, which also defaults to the length of that dimension. Negative indices are counted from the end of the dimension (e.g., -1 is the last element). |

## ee.Image.log

Computes the natural logarithm of the input.

| Usage | Returns |
|---|---|
| `Image.log()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.log10

Computes the base-10 logarithm of the input.

| Usage | Returns |
|---|---|
| `Image.log10()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.long

Casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Image.long()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.lt

Returns 1 if and only if the first value is less than the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean.

| Usage | Returns |
|---|---|
| `Image.lt(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.lte

Returns 1 if and only if the first value is less than or equal to the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean.

| Usage | Returns |
|---|---|
| `Image.lte(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.mask

Gets or sets an image's mask. The output image retains the metadata and footprint of the input image. Pixels where the mask changes from zero to another value will be filled with zeros, or the values closest to zero within the range of the pixel type.

Note: the version that sets a mask will be deprecated. To set a mask from an image on previously unmasked pixels, use Image.updateMask. To unmask previously masked pixels, use Image.unmask.

| Usage | Returns |
|---|---|
| `Image.mask(*mask*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `mask` | Image, default: null | The mask image. If specified, the input image is copied to the output but given the mask by the values of this image. If this is a single band, it is used for all bands in the input image. If not specified, returns an image created from the mask of the input image, scaled to the range \[0:1\] (invalid = 0, valid = 1.0). |

## ee.Image.matrixCholeskyDecomposition

Calculates the Cholesky decomposition of a matrix. The Cholesky decomposition is a decomposition into the form L \* L' where L is a lower triangular matrix. The input must be a symmetric positive-definite matrix. Returns an image with 1 band named 'L'.

| Usage | Returns |
|---|---|
| `Image.matrixCholeskyDecomposition()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Image of 2-D matrices to be decomposed. |

## ee.Image.matrixDeterminant

Computes the determinant of the matrix.

| Usage | Returns |
|---|---|
| `Image.matrixDeterminant()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.matrixDiagonal

Computes the diagonal of the matrix in a single column.

| Usage | Returns |
|---|---|
| `Image.matrixDiagonal()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.matrixFnorm

Computes the Frobenius norm of the matrix.

| Usage | Returns |
|---|---|
| `Image.matrixFnorm()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.matrixIdentity

Creates an image where each pixel is a 2D identity matrix of the given size.

| Usage | Returns |
|---|---|
| `ee.Image.matrixIdentity(size)` | Image |

| Argument | Type | Details |
|---|---|---|
| `size` | Integer | The length of each axis. |

## ee.Image.matrixInverse

Computes the inverse of the matrix.

| Usage | Returns |
|---|---|
| `Image.matrixInverse()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.matrixLUDecomposition

Calculates the LU matrix decomposition such that P×input=L×U, where L is lower triangular (with unit diagonal terms), U is upper triangular and P is a partial pivot permutation matrix. The input matrix must be square. Returns an image with bands named 'L', 'U' and 'P'.

| Usage | Returns |
|---|---|
| `Image.matrixLUDecomposition()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Image of 2-D matrices to be decomposed. |

## ee.Image.matrixMultiply

Returns the matrix multiplication A \* B for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.matrixMultiply(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.matrixPseudoInverse

Computes the Moore-Penrose pseudoinverse of the matrix.

| Usage | Returns |
|---|---|
| `Image.matrixPseudoInverse()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.matrixQRDecomposition

Calculates the QR-decomposition of a matrix into two matrices Q and R such that input = QR, where Q is orthogonal, and R is upper triangular. Returns an image with bands named 'Q' and 'R'.

| Usage | Returns |
|---|---|
| `Image.matrixQRDecomposition()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Image of 2-D matrices to be decomposed. |

## ee.Image.matrixSingularValueDecomposition

Calculates the Singular Value Decomposition of the input matrix into U×S×V', such that U and V are orthogonal and S is diagonal. Returns an image with bands named 'U', 'S' and 'V'.

| Usage | Returns |
|---|---|
| `Image.matrixSingularValueDecomposition()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Image of 2-D matrices to be decomposed. |

## ee.Image.matrixSolve

Solves for x in the matrix equation A \* x = B, finding a least-squares solution if A is overdetermined for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.matrixSolve(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.matrixToDiag

Computes a square diagonal matrix from a single column matrix.

| Usage | Returns |
|---|---|
| `Image.matrixToDiag()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.matrixTrace

Computes the trace of the matrix.

| Usage | Returns |
|---|---|
| `Image.matrixTrace()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.matrixTranspose

Transposes two dimensions of each array pixel.

| Usage | Returns |
|---|---|
| `Image.matrixTranspose(*axis1*, *axis2*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |
| `axis1` | Integer, default: 0 | First axis to swap. |
| `axis2` | Integer, default: 1 | Second axis to swap. |

## ee.Image.max

Selects the maximum of the first and second values for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.max(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.medialAxis

Computes the discrete medial axis of the zero valued pixels of the first band of the input. Outputs 4 bands:

<br />

1. medial - the medial axis points, scaled by the distance.
2. coverage - the number of points supporting each medial axis point.
3. xlabel - the horizontal distance to the power point for each pixel.
4. ylabel - the vertical distance to the power point for each pixel.

<br />

| Usage | Returns |
|---|---|
| `Image.medialAxis(*neighborhood*, *units*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `neighborhood` | Integer, default: 256 | Neighborhood size in pixels. |
| `units` | String, default: "pixels" | The units of the neighborhood, currently only 'pixels' are supported. |

## ee.Image.metadata

Generates a constant image of type double from a metadata property.

| Usage | Returns |
|---|---|
| `Image.metadata(property, *name*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image from which to get the metadata |
| `property` | String | The property from which to take the value. |
| `name` | String, default: null | The name for the output band. If unspecified, it will be the same as the property name. |

## ee.Image.min

Selects the minimum of the first and second values for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.min(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.mod

Calculates the remainder of the first value divided by the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.mod(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.multiply

Multiplies the first value by the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.multiply(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.neighborhoodToArray

Turns the neighborhood of each pixel in a scalar image into a 2D array. Axes 0 and 1 of the output array correspond to Y and X axes of the image, respectively. The output image will have as many bands as the input; each output band has the same mask as the corresponding input band. The footprint and metadata of the input image are preserved.

| Usage | Returns |
|---|---|
| `Image.neighborhoodToArray(kernel, *defaultValue*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to get pixels from; must be scalar-valued. |
| `kernel` | Kernel | The kernel specifying the shape of the neighborhood. Only fixed, square and rectangle kernels are supported. Weights are ignored; only the shape of the kernel is used. |
| `defaultValue` | Float, default: 0 | The value to use in the output arrays to replace the invalid (masked) pixels of the input. If the band type is integral, the fractional part of this value is discarded; in all cases, the value is clamped to the value range of the band. |

## ee.Image.neighborhoodToBands

Turns the neighborhood of a pixel into a set of bands. The neighborhood is specified using a Kernel and only non-zero-weight kernel values are used. The weights of the kernel is otherwise ignored.

Each input band produces x \* y output bands. Each output band is named 'input_x_y' where x and y indicate the pixel's location in the kernel. For example, a 3x3 kernel operating on a 2-band image produces 18 output bands.

| Usage | Returns |
|---|---|
| `Image.neighborhoodToBands(kernel)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to get pixels from. |
| `kernel` | Kernel | The kernel specifying the neighborhood. Zero-weight values are ignored. |

## ee.Image.neq

Returns 1 if and only if the first value is not equal to the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean.

| Usage | Returns |
|---|---|
| `Image.neq(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.normalizedDifference

Computes the normalized difference between two bands. If the bands to use are not specified, uses the first two bands. The normalized difference is computed as (first − second) / (first + second).

Note that the returned image band name is 'nd', the input image properties are not retained in the output image, and a negative pixel value in either input band will cause the output pixel to be masked. To avoid masking negative input values, use `ee.Image.expression()` to compute normalized difference.

| Usage | Returns |
|---|---|
| `Image.normalizedDifference(*bandNames*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The input image. |
| `bandNames` | List, default: null | A list of names specifying the bands to use. If not specified, the first and second bands are used. |

## ee.Image.not

Returns 0 if the input is non-zero, and 1 otherwise.

| Usage | Returns |
|---|---|
| `Image.not()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.or

Returns 1 if and only if either input value is non-zero for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean.

| Usage | Returns |
|---|---|
| `Image.or(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.paint

Paints the geometries of a collection onto an image, using the given 'color' value to replace each band's values where any geometry covers the image (or, if a line width is specified, where the perimeters do).

This algorithm is most suitable for converting categorical data from feature properties to pixels in an image; if you wish to visualize a collection, consider using FeatureCollection.style instead, which supports RGB colors whereas this algorithm is strictly 'monochrome' (using single numeric values).

| Usage | Returns |
|---|---|
| `Image.paint(featureCollection, *color*, *width*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image on which the collection is painted. |
| `featureCollection` | FeatureCollection | The collection painted onto the image. |
| `color` | Object, default: 0 | The pixel value to paint into every band of the input image, either as a number which will be used for all features, or the name of a numeric property to take from each feature in the collection. |
| `width` | Object, default: null | Line width, either as a number which will be the line width for all geometries, or the name of a numeric property to take from each feature in the collection. If unspecified, the geometries will be filled instead of outlined. |

## ee.Image.pixelArea

Generate an image in which the value of each pixel is the area of that pixel in square meters. The returned image has a single band called "area."

| Usage | Returns |
|---|---|
| `ee.Image.pixelArea()` | Image |

**No arguments.**

## ee.Image.pixelCoordinates

Creates a two-band image containing the x and y coordinates of each pixel in the given projection.

| Usage | Returns |
|---|---|
| `ee.Image.pixelCoordinates(projection)` | Image |

| Argument | Type | Details |
|---|---|---|
| `projection` | Projection | The projection in which to provide pixels. |

## ee.Image.pixelLonLat

Creates an image with two bands named 'longitude' and 'latitude', containing the longitude and latitude at each pixel, in degrees.

| Usage | Returns |
|---|---|
| `ee.Image.pixelLonLat()` | Image |

**No arguments.**

## ee.Image.polynomial

Compute a polynomial at each pixel using the given coefficients.

| Usage | Returns |
|---|---|
| `Image.polynomial(coefficients)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `coefficients` | List | The polynomial coefficients in increasing order of degree starting with the constant term. |

## ee.Image.pow

Raises the first value to the power of the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is float.

| Usage | Returns |
|---|---|
| `Image.pow(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.projection

Returns the default projection of an Image. Throws an error if the bands of the image don't all have the same projection.

| Usage | Returns |
|---|---|
| `Image.projection()` | Projection |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image from which to get the projection. |

## ee.Image.propertyNames

Returns the names of properties on this element.

| Usage | Returns |
|---|---|
| `Image.propertyNames()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element |   |

## ee.Image.random

Generates a random number at each pixel location. When using the 'uniform' distribution, outputs are in the range of \[0, 1). Using the 'normal' distribution, the outputs have μ=0, σ=1, but no explicit limits.

| Usage | Returns |
|---|---|
| `ee.Image.random(*seed*, *distribution*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `seed` | Long, default: 0 | Seed for the random number generator. |
| `distribution` | String, default: "uniform" | The distribution type of random numbers to produce. One of 'uniform' or 'normal'. |

## ee.Image.randomVisualizer

Creates a visualization image by assigning a random color to each unique value of the pixels of the first band. The first three bands of the output image will contain 8-bit R, G and B values, followed by all bands of the input image.

| Usage | Returns |
|---|---|
| `Image.randomVisualizer()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Image with at least one band. |

## ee.Image.reduce

Applies a reducer to all of the bands of an image.

The reducer must have a single input and will be called at each pixel to reduce the stack of band values.

The output image will have one band for each reducer output.

| Usage | Returns |
|---|---|
| `Image.reduce(reducer)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to reduce. |
| `reducer` | Reducer | The reducer to apply to the given image. |

## ee.Image.reduceConnectedComponents

Applies a reducer to all of the pixels inside of each 'object'. Pixels are considered to belong to an object if they are connected (8-way) and have the same value in the 'label' band. The label band is only used to identify the connectedness; the rest are provided as inputs to the reducer.

| Usage | Returns |
|---|---|
| `Image.reduceConnectedComponents(reducer, *labelBand*, *maxSize*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `reducer` | Reducer | The reducer to apply to pixels within the connected component. |
| `labelBand` | String, default: null | The name of the band to use to detect connectedness. If unspecified, the first band is used. |
| `maxSize` | Integer, default: 256 | Size of the neighborhood to consider when aggregating values. Any objects larger than maxSize in either the horizontal or vertical dimension will be masked, since portions of the object might be outside of the neighborhood. |

## ee.Image.reduceNeighborhood

Applies the given reducer to the neighborhood around each pixel, as determined by the given kernel. If the reducer has a single input, it will be applied separately to each band of the collection; otherwise it must have the same number of inputs as the input image has bands.

The reducer output names determine the names of the output bands:

- Reducers with multiple inputs will use the output names directly.
- Reducers with a single input will prefix the output name with the input band name (e.g., '10_mean', '20_mean').

Reducers with weighted inputs can have the input weight based on the input mask, the kernel value, or the smaller of those two.

| Usage | Returns |
|---|---|
| `Image.reduceNeighborhood(reducer, kernel, *inputWeight*, *skipMasked*, *optimization*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `reducer` | Reducer | The reducer to apply to pixels within the neighborhood. |
| `kernel` | Kernel | The kernel defining the neighborhood. |
| `inputWeight` | String, default: "kernel" | One of 'mask', 'kernel', or 'min'. |
| `skipMasked` | Boolean, default: true | Mask output pixels if the corresponding input pixel is masked. |
| `optimization` | String, default: null | Optimization strategy. Options are 'boxcar' and 'window'. The 'boxcar' method is a fast method for computing count, sum or mean. It requires a homogeneous kernel, a single-input reducer and either MASK, KERNEL or no weighting. The 'window' method uses a running window, and has the same requirements as 'boxcar', but can use any single input reducer. Both methods require considerable additional memory. |

## ee.Image.reduceRegion

Apply a reducer to all the pixels in a specific region.

Either the reducer must have the same number of inputs as the input image has bands, or it must have a single input and will be repeated for each band.

Returns a dictionary of the reducer's outputs.

| Usage | Returns |
|---|---|
| `Image.reduceRegion(reducer, *geometry*, *scale*, *crs*, *crsTransform*, *bestEffort*, *maxPixels*, *tileScale*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to reduce. |
| `reducer` | Reducer | The reducer to apply. |
| `geometry` | Geometry, default: null | The region over which to reduce data. Defaults to the footprint of the image's first band. |
| `scale` | Float, default: null | A nominal scale in meters of the projection to work in. |
| `crs` | Projection, default: null | The projection to work in. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale. |
| `crsTransform` | List, default: null | The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with 'scale', and replaces any transform already set on the projection. |
| `bestEffort` | Boolean, default: false | If the polygon would contain too many pixels at the given scale, compute and use a larger scale which would allow the operation to succeed. |
| `maxPixels` | Long, default: 10000000 | The maximum number of pixels to reduce. |
| `tileScale` | Float, default: 1 | A scaling factor between 0.1 and 16 used to adjust aggregation tile size; setting a larger tileScale (e.g., 2 or 4) uses smaller tiles and may enable computations that run out of memory with the default. |

## ee.Image.reduceRegions

Apply a reducer over the area of each feature in the given collection.

The reducer must have the same number of inputs as the input image has bands.

Returns the input features, each augmented with the corresponding reducer outputs.

| Usage | Returns |
|---|---|
| `Image.reduceRegions(collection, reducer, *scale*, *crs*, *crsTransform*, *tileScale*, *maxPixelsPerRegion*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to reduce. |
| `collection` | FeatureCollection | The features to reduce over. |
| `reducer` | Reducer | The reducer to apply. |
| `scale` | Float, default: null | A nominal scale in meters of the projection to work in. |
| `crs` | Projection, default: null | The projection to work in. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale. |
| `crsTransform` | List, default: null | The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with 'scale', and will replace any transform already set on the projection. |
| `tileScale` | Float, default: 1 | A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default. |
| `maxPixelsPerRegion` | Long, default: null | The maximum number of pixels to reduce per region. |

## ee.Image.reduceResolution

Enables reprojection using the given reducer to combine all input pixels corresponding to each output pixel. If the reducer has a single input, it will be applied separately to each band of the collection; otherwise it must have the same number of inputs as the input image has bands.

The reducer output names determine the names of the output bands: reducers with multiple inputs will use the output names directly, reducers with a single input and single output will preserve the input band names, and reducers with a single input and multiple outputs will prefix the output name with the input band name (e.g., '10_mean', '10_stdDev', '20_mean', '20_stdDev').

Reducer input weights will be the product of the input mask and the fraction of the output pixel covered by the input pixel.

| Usage | Returns |
|---|---|
| `Image.reduceResolution(reducer, *bestEffort*, *maxPixels*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `reducer` | Reducer | The reducer to apply to be used for combining pixels. |
| `bestEffort` | Boolean, default: false | If using the input at its default resolution would require too many pixels, start with already-reduced input pixels from a pyramid level that allows the operation to succeed. |
| `maxPixels` | Integer, default: 64 | The maximum number of input pixels to combine for each output pixel. Setting this too large will cause out-of-memory problems. |

## ee.Image.reduceToVectors

Convert an image to a feature collection by reducing homogeneous regions.

Given an image containing a band of labeled segments and zero or more additional bands, runs a reducer over the pixels in each segment producing a feature per segment.

Either the reducer must have one fewer inputs than the image has bands, or it must have a single input and will be repeated for each band.

| Usage | Returns |
|---|---|
| `Image.reduceToVectors(*reducer*, *geometry*, *scale*, *geometryType*, *eightConnected*, *labelProperty*, *crs*, *crsTransform*, *bestEffort*, *maxPixels*, *tileScale*, *geometryInNativeProjection*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. The first band is expected to be an integer type; adjacent pixels will be in the same segment if they have the same value in this band. |
| `reducer` | Reducer, default: null | The reducer to apply. Its inputs will be taken from the image's bands after dropping the first band. Defaults to Reducer.countEvery(). |
| `geometry` | Geometry, default: null | The region over which to reduce data. Defaults to the footprint of the image's first band. |
| `scale` | Float, default: null | A nominal scale in meters of the projection to work in. |
| `geometryType` | String, default: "polygon" | How to choose the geometry of each generated feature; one of 'polygon' (a polygon enclosing the pixels in the segment), 'bb' (a rectangle bounding the pixels), or 'centroid' (the centroid of the pixels). |
| `eightConnected` | Boolean, default: true | If true, diagonally-connected pixels are considered adjacent; otherwise only pixels that share an edge are. |
| `labelProperty` | String, default: "label" | If non-null, the value of the first band will be saved as the specified property of each feature. |
| `crs` | Projection, default: null | The projection to work in. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale. |
| `crsTransform` | List, default: null | The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with 'scale', and replaces any transform already set on the projection. |
| `bestEffort` | Boolean, default: false | If the polygon would contain too many pixels at the given scale, compute and use a larger scale which would allow the operation to succeed. |
| `maxPixels` | Long, default: 10000000 | The maximum number of pixels to reduce. |
| `tileScale` | Float, default: 1 | A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default. |
| `geometryInNativeProjection` | Boolean, default: false | Create geometries in the pixel projection, rather than EPSG:4326. |

## ee.Image.regexpRename

Renames the bands of an image by applying a regular expression replacement to the current band names. Any bands not matched by the regex will be copied over without renaming.

| Usage | Returns |
|---|---|
| `Image.regexpRename(regex, replacement, *all*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The image containing the bands to rename. |
| `regex` | String | A regular expression to match in each band name. |
| `replacement` | String | The text with which to replace each match. Supports $n syntax for captured values. |
| `all` | Boolean, default: true | If true, all matches in a given string will be replaced. Otherwise, only the first match in each string will be replaced. |

## ee.Image.register

Registers an image to a reference image while allowing local, rubber sheet deformations. Displacements are computed in the CRS of the reference image, at a scale dictated by the lowest resolution of the following three projections: input image projection, reference image projection, and requested projection. The displacements then applied to the input image to register it with the reference.

| Usage | Returns |
|---|---|
| `Image.register(referenceImage, maxOffset, *patchWidth*, *stiffness*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to register. |
| `referenceImage` | Image | The image to register to. |
| `maxOffset` | Float | The maximum offset allowed when attempting to align the input images, in meters. Using a smaller value can reduce computation time significantly, but it must still be large enough to cover the greatest displacement within the entire image region. |
| `patchWidth` | Float, default: null | Patch size for detecting image offsets, in meters. This should be set large enough to capture texture, as well as large enough that ignorable objects are small within the patch. Default is null. Patch size will be determined automatically if not provided. |
| `stiffness` | Float, default: 5 | Enforces a stiffness constraint on the solution. Valid values are in the range \[0,10\]. The stiffness is used for outlier rejection when determining displacements at adjacent grid points. Higher values move the solution towards a rigid transformation. Lower values allow more distortion or warping of the image during registration. |

## ee.Image.remap

Maps from input values to output values, represented by two parallel lists. Any input values not included in the input list are either set to defaultValue if it is given or masked if it isn't. Note that inputs containing floating point values might sometimes fail to match due to floating point precision errors.

| Usage | Returns |
|---|---|
| `Image.remap(from, to, *defaultValue*, *bandName*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to which the remapping is applied. |
| `from` | List | The source values (numbers or ee.Array). All values in this list will be mapped to the corresponding value in 'to'. |
| `to` | List | The destination values (numbers or ee.Array). These are used to replace the corresponding values in 'from'. Must have the same number of values as 'from'. |
| `defaultValue` | Object, default: null | The default value to replace values that weren't matched by a value in 'from'. If not specified, unmatched values are masked out. |
| `bandName` | String, default: null | The name of the band to remap. If not specified, the first band in the image is used. |

## ee.Image.rename

Rename the bands of an image.

Returns the renamed image.

| Usage | Returns |
|---|---|
| `Image.rename(var_args)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `var_args` | List\[String\]\|Object\|VarArgs\[String\] | The new names for the bands. Must match the number of bands in the Image. |

## ee.Image.reproject

Force an image to be computed in a given projection and resolution.

| Usage | Returns |
|---|---|
| `Image.reproject(crs, *crsTransform*, *scale*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to reproject. |
| `crs` | Projection | The CRS to project the image to. |
| `crsTransform` | List, default: null | The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with the scale option, and replaces any transform already on the projection. |
| `scale` | Float, default: null | If scale is specified, then the projection is scaled by dividing the specified scale value by the nominal size of a meter in the specified projection. If scale is not specified, then the scale of the given projection will be used. |

## ee.Image.resample

An algorithm that returns an image identical to its argument, but which uses bilinear or bicubic interpolation (rather than the default nearest-neighbor) to compute pixels in projections other than its native projection or other levels of the same image pyramid.

This relies on the input image's default projection being meaningful, and so cannot be used on composites, for example. (Instead, you should resample the images that are used to create the composite.)

| Usage | Returns |
|---|---|
| `Image.resample(*mode*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image to resample. |
| `mode` | String, default: "bilinear" | The interpolation mode to use. One of 'bilinear' or 'bicubic'. |

## ee.Image.rgb

Create a 3-band image specifically for visualization. This uses the first band in each image.

Returns the combined image.

| Usage | Returns |
|---|---|
| `ee.Image.rgb(r, g, b)` | Image |

| Argument | Type | Details |
|---|---|---|
| `r` | Image | The red image. |
| `g` | Image | The green image. |
| `b` | Image | The blue image. |

## ee.Image.rgbToHsv

Transforms the image from the RGB color space to the HSV color space. Expects a 3-band image in the range \[0, 1\], and produces 3 bands: hue, saturation and value with values in the range \[0, 1\].

| Usage | Returns |
|---|---|
| `Image.rgbToHsv()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to transform. |

## ee.Image.rightShift

Calculates the signed right shift of v1 by v2 bits for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.rightShift(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.round

Computes the integer nearest to the input.

| Usage | Returns |
|---|---|
| `Image.round()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.rsedTransform

Reverse Squared Euclidean Distance (RSED) computes the 2D maximal height surface created by placing an inverted parabola over each non-zero pixel of the input image, where the pixel's value is the height of the parabola. Viewed as a binary image (zero/not-zero) this is equivalent to buffering each non-zero input pixel by the square root of its value, in pixels.

| Usage | Returns |
|---|---|
| `Image.rsedTransform(*neighborhood*, *units*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `neighborhood` | Integer, default: 256 | Neighborhood size in pixels. |
| `units` | String, default: "pixels" | The units of the neighborhood, currently only 'pixels' are supported. |

## ee.Image.sample

Samples the pixels of an image, returning them as a FeatureCollection. Each feature will have 1 property per band in the input image. Note that the default behavior is to drop features that intersect masked pixels, which result in null-valued properties (see dropNulls argument).

| Usage | Returns |
|---|---|
| `Image.sample(*region*, *scale*, *projection*, *factor*, *numPixels*, *seed*, *dropNulls*, *tileScale*, *geometries*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to sample. |
| `region` | Geometry, default: null | The region to sample from. If unspecified, uses the image's whole footprint. |
| `scale` | Float, default: null | A nominal scale in meters of the projection to sample in. |
| `projection` | Projection, default: null | The projection in which to sample. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale. |
| `factor` | Float, default: null | A subsampling factor, within (0, 1\]. If specified, 'numPixels' must not be specified. Defaults to no subsampling. |
| `numPixels` | Long, default: null | The approximate number of pixels to sample. If specified, 'factor' must not be specified. |
| `seed` | Integer, default: 0 | A randomization seed to use for subsampling. |
| `dropNulls` | Boolean, default: true | Post filter the result to drop features that have null-valued properties. |
| `tileScale` | Float, default: 1 | A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default. |
| `geometries` | Boolean, default: false | If true, adds the center of the sampled pixel as the geometry property of the output feature. Otherwise, geometries will be omitted (saving memory). |

## ee.Image.sampleRectangle

Extracts a rectangular region of pixels from an image into a ND array per band. The arrays are returned in a feature retaining the same properties as the image and a geometry the same as that used to sample the image (or the image footprint if unspecified). Each band is sampled in its input projection, and if no geometry is specified, sampled using its footprint. For scalar bands, the output array is 2D. For array bands the output array is (2+N)D where N is the number of dimensions in the original band. If sampling array bands, all arrays must have the same number of elements. If a band's sampled region is entirely masked and a default array value is specified, the default array value is used in-lieu of sampling the image.

| Usage | Returns |
|---|---|
| `Image.sampleRectangle(*region*, *properties*, *defaultValue*, *defaultArrayValue*)` | Feature |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to sample. |
| `region` | Geometry, default: null | The region whose projected bounding box is used to sample the image. Defaults to the footprint in each band. |
| `properties` | List, default: null | The properties to copy over from the sampled image. Defaults to all non-system properties. |
| `defaultValue` | Float, default: null | A default value used when a sampled pixel is masked or outside a band's footprint. |
| `defaultArrayValue` | Array, default: null | A default value used when a sampled array pixel is masked or outside a band's footprint. |

## ee.Image.sampleRegions

Converts each pixel of an image (at a given scale) that intersects one or more regions to a Feature, returning them as a FeatureCollection. Each output feature will have one property per band of the input image, as well as any specified properties copied from the input feature.

Note that geometries will be snapped to pixel centers.

| Usage | Returns |
|---|---|
| `Image.sampleRegions(collection, *properties*, *scale*, *projection*, *tileScale*, *geometries*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to sample. |
| `collection` | FeatureCollection | The regions to sample over. |
| `properties` | List, default: null | The list of properties to copy from each input feature. Defaults to all non-system properties. |
| `scale` | Float, default: null | A nominal scale in meters of the projection to sample in. If unspecified, the scale of the image's first band is used. |
| `projection` | Projection, default: null | The projection in which to sample. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale. |
| `tileScale` | Float, default: 1 | A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default. |
| `geometries` | Boolean, default: false | If true, the results will include a point geometry per sampled pixel. Otherwise, geometries will be omitted (saving memory). |

## ee.Image.select

Selects bands from an image.

Returns an image with the selected bands.

| Usage | Returns |
|---|---|
| `Image.select(var_args)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The Image instance. |
| `var_args` | VarArgs\[Object\] | One of two possibilities: - Any number of non-list arguments. All of these will be interpreted as band selectors. These can be band names, regexes, or numeric indices. E.g. selected = image.select('a', 'b', 3, 'd'); - Two lists. The first will be used as band selectors and the second as new names for the selected bands. The number of new names must match the number of selected bands. E.g. selected = image.select(\['a', 4\], \['newA', 'newB'\]); |

## ee.Image.selfMask

Updates an image's mask at all positions where the existing mask is not zero using the value of the image as the new mask value. The output image retains the metadata and footprint of the input image.

| Usage | Returns |
|---|---|
| `Image.selfMask()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to mask with itself. |

## ee.Image.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Image.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Image.set

Overrides one or more metadata properties of an Element.

Returns the element with the specified properties overridden.

| Usage | Returns |
|---|---|
| `Image.set(var_args)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The Element instance. |
| `var_args` | VarArgs\[Object\] | Either a dictionary of properties, or a vararg sequence of properties, e.g. key1, value1, key2, value2, ... |

## ee.Image.setDefaultProjection

Set a default projection to be applied to this image. The projection's resolution may be overridden by later operations.

| Usage | Returns |
|---|---|
| `Image.setDefaultProjection(crs, *crsTransform*, *scale*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to reproject. |
| `crs` | Projection | The CRS to project the image to. |
| `crsTransform` | List, default: null | The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with the scale option, and replaces any transform already on the projection. |
| `scale` | Float, default: null | If scale is specified, then the projection is scaled by dividing the specified scale value by the nominal size of a meter in the specified projection. If scale is not specified, then the scale of the given projection will be used. |

## ee.Image.short

Casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Image.short()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.signum

Computes the signum function (sign) of the input; 0 if the input is 0, 1 if the input is greater than 0, -1 if the input is less than 0.

| Usage | Returns |
|---|---|
| `Image.signum()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.sin

Computes the sine of the input in radians.

| Usage | Returns |
|---|---|
| `Image.sin()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.sinh

Computes the hyperbolic sine of the input.

| Usage | Returns |
|---|---|
| `Image.sinh()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.sldStyle

Styles a raster input with the provided OGC SLD styling.

Points of note:

- OGC SLD 1.0 and OGC SE 1.1 are supported.
- The XML document passed in can be complete, or just the SldRasterSymbolizer element and down.
- Exactly one SldRasterSymbolizer is required.
- Bands may be selected by their proper Earth Engine names or using numeric identifiers ("1", "2", ...). Proper Earth Engine names are tried first.
- The Histogram and Normalize contrast stretch mechanisms are supported.
- The type="values", type="intervals" and type="ramp" attributes for ColorMap element in SLD 1.0 (GeoServer extensions) are supported.
- Opacity is only taken into account when it is 0.0 (transparent). Non-zero opacity values are treated as completely opaque.
- The OverlapBehavior definition is currently ignored.
- The ShadedRelief mechanism is not currently supported.
- The ImageOutline mechanism is not currently supported.
- The Geometry element is ignored.

The output image will have histogram_bandname metadata if histogram equalization or normalization is requested.

<br />

| Usage | Returns |
|---|---|
| `Image.sldStyle(sldXml)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The image to rendering using the SLD. |
| `sldXml` | String | The OGC SLD 1.0 or 1.1 document (or fragment). |

## ee.Image.slice

Selects a contiguous group of bands from an image by position.

| Usage | Returns |
|---|---|
| `Image.slice(start, *end*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image from which to select bands. |
| `start` | Integer | Where to start the selection. Negative numbers select from the end, counting backwards. |
| `end` | Integer, default: null | Where to end the selection. If omitted, selects all bands from the start position to the end. |

## ee.Image.spectralDilation

Computes the spectral/spatial dilation of an image by computing the spectral distance of each pixel under a structuring kernel from the centroid of all pixels under the kernel and taking the most distant result.

See 'Spatial/spectral endmember extraction by multidimensional morphological operations.' IEEE transactions on geoscience and remote sensing 40.9 (2002): 2025-2041.

| Usage | Returns |
|---|---|
| `Image.spectralDilation(*metric*, *kernel*, *useCentroid*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `metric` | String, default: "sam" | The spectral distance metric to use. One of 'sam' (spectral angle mapper), 'sid' (spectral information divergence), 'sed' (squared Euclidean distance), or 'emd' (earth movers distance). |
| `kernel` | Kernel, default: null | Connectedness kernel. Defaults to a square of radius 1 (8-way connected). |
| `useCentroid` | Boolean, default: false | If true, distances are computed from the mean of all pixels under the kernel instead of the kernel's center pixel. |

## ee.Image.spectralDistance

Computes the per-pixel spectral distance between two images. If the images are array based then only the first band of each image is used; otherwise all bands are involved in the distance computation. The two images are therefore expected to contain the same number of bands or have the same 1-dimensional array length.

| Usage | Returns |
|---|---|
| `Image.spectralDistance(image2, *metric*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The first image. |
| `image2` | Image | The second image. |
| `metric` | String, default: "sam" | The spectral distance metric to use. One of 'sam' (spectral angle mapper), 'sid' (spectral information divergence), 'sed' (squared Euclidean distance), or 'emd' (earth movers distance). |

## ee.Image.spectralErosion

Computes the spectral/spatial erosion of an image by computing the spectral distance of each pixel under a structuring kernel from the centroid of all pixels under the kernel and taking the closest result.

See 'Spatial/spectral endmember extraction by multidimensional morphological operations.' IEEE transactions on geoscience and remote sensing 40.9 (2002): 2025-2041.

| Usage | Returns |
|---|---|
| `Image.spectralErosion(*metric*, *kernel*, *useCentroid*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `metric` | String, default: "sam" | The spectral distance metric to use. One of 'sam' (spectral angle mapper), 'sid' (spectral information divergence), 'sed' (squared Euclidean distance), or 'emd' (earth movers distance). |
| `kernel` | Kernel, default: null | Connectedness kernel. Defaults to a square of radius 1 (8-way connected). |
| `useCentroid` | Boolean, default: false | If true, distances are computed from the mean of all pixels under the kernel instead of the kernel's center pixel. |

## ee.Image.spectralGradient

Computes the spectral gradient over all bands of an image (or the first band if the image is Array typed) by computing the per-pixel difference between the spectral erosion and dilation with a given structuring kernel and distance metric.

See: Plaza, Antonio, et al. 'Spatial/spectral endmember extraction by multidimensional morphological operations.' IEEE transactions on geoscience and remote sensing 40.9 (2002): 2025-2041.

| Usage | Returns |
|---|---|
| `Image.spectralGradient(*metric*, *kernel*, *useCentroid*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `metric` | String, default: "sam" | The spectral distance metric to use. One of 'sam' (spectral angle mapper), 'sid' (spectral information divergence), 'sed' (squared Euclidean distance), or 'emd' (earth movers distance). |
| `kernel` | Kernel, default: null | Connectedness kernel. Defaults to a square of radius 1 (8-way connected). |
| `useCentroid` | Boolean, default: false | If true, distances are computed from the mean of all pixels under the kernel instead of the kernel's center pixel. |

## ee.Image.sqrt

Computes the square root of the input.

| Usage | Returns |
|---|---|
| `Image.sqrt()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.stratifiedSample

Extracts a stratified random sample of points from an image. Extracts the specified number of samples for each distinct value discovered within the 'classBand'. Returns a FeatureCollection of 1 Feature per extracted point, with each feature having 1 property per band in the input image. If there are less than the specified number of samples available for a given class value, then all of the points for that class will be included. Requires that the classBand contain integer values.

| Usage | Returns |
|---|---|
| `Image.stratifiedSample(numPoints, *classBand*, *region*, *scale*, *projection*, *seed*, *classValues*, *classPoints*, *dropNulls*, *tileScale*, *geometries*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to sample. |
| `numPoints` | Integer | The default number of points to sample in each class. Can be overridden for specific classes using the 'classValues' and 'classPoints' properties. |
| `classBand` | String, default: null | The name of the band containing the classes to use for stratification. If unspecified, the first band of the input image is used. |
| `region` | Geometry, default: null | The region to sample from. If unspecified, the input image's whole footprint is used. |
| `scale` | Float, default: null | A nominal scale in meters of the projection to sample in. Defaults to the scale of the first band of the input image. |
| `projection` | Projection, default: null | The projection in which to sample. If unspecified, the projection of the input image's first band is used. If specified in addition to scale, rescaled to the specified scale. |
| `seed` | Integer, default: 0 | A randomization seed to use for subsampling. |
| `classValues` | List, default: null | A list of class values for which to override the numPoints parameter. Must be the same size as classPoints or null. |
| `classPoints` | List, default: null | A list of the per-class maximum number of pixels to sample for each class in the classValues list. Must be the same size as classValues or null. |
| `dropNulls` | Boolean, default: true | Skip pixels in which any band is masked. |
| `tileScale` | Float, default: 1 | A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default. |
| `geometries` | Boolean, default: false | If true, the results will include a geometry per sampled pixel. Otherwise, geometries will be omitted (saving memory). |

## ee.Image.subtract

Subtracts the second value from the first for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types.

| Usage | Returns |
|---|---|
| `Image.subtract(image2)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image1` | Image | The image from which the left operand bands are taken. |
| `image2` | Image | The image from which the right operand bands are taken. |

## ee.Image.tan

Computes the tangent of the input in radians.

| Usage | Returns |
|---|---|
| `Image.tan()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.tanh

Computes the hyperbolic tangent of the input.

| Usage | Returns |
|---|---|
| `Image.tanh()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toArray

Concatenates pixels from each band into a single array per pixel. The result will be masked if any input bands are masked.

| Usage | Returns |
|---|---|
| `Image.toArray(*axis*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Image of bands to convert to an array per pixel. Bands must have scalar pixels, or array pixels with equal dimensionality. |
| `axis` | Integer, default: 0 | Axis to concatenate along; must be at least 0 and at most the dimension of the inputs. If the axis equals the dimension of the inputs, the result will have 1 more dimension than the inputs. |

## ee.Image.toByte

Casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Image.toByte()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toDictionary

Extract properties from a feature as a dictionary.

| Usage | Returns |
|---|---|
| `Image.toDictionary(*properties*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The feature to extract the property from. |
| `properties` | List, default: null | The list of properties to extract. Defaults to all non-system properties. |

## ee.Image.toDouble

Casts the input value to a 64-bit float.

| Usage | Returns |
|---|---|
| `Image.toDouble()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toFloat

Casts the input value to a 32-bit float.

| Usage | Returns |
|---|---|
| `Image.toFloat()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toInt

Casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Image.toInt()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toInt16

Casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Image.toInt16()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toInt32

Casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Image.toInt32()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toInt64

Casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Image.toInt64()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toInt8

Casts the input value to a signed 8-bit integer.

| Usage | Returns |
|---|---|
| `Image.toInt8()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toLong

Casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Image.toLong()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toShort

Casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Image.toShort()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toUint16

Casts the input value to an unsigned 16-bit integer.

| Usage | Returns |
|---|---|
| `Image.toUint16()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toUint32

Casts the input value to an unsigned 32-bit integer.

| Usage | Returns |
|---|---|
| `Image.toUint32()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.toUint8

Casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Image.toUint8()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.translate

Translate the input image.

| Usage | Returns |
|---|---|
| `Image.translate(x, y, *units*, *proj*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image |   |
| `x` | Float | The amount to translate the image in the x direction. |
| `y` | Float | The amount to translate the image in the y direction. |
| `units` | String, default: "meters" | The units for x and y; 'meters' or 'pixels'. |
| `proj` | Projection, default: null | The projection in which to translate the image; defaults to the projection of the first band. |

## ee.Image.trigamma

Computes the trigamma function of the input.

| Usage | Returns |
|---|---|
| `Image.trigamma()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.uint16

Casts the input value to an unsigned 16-bit integer.

| Usage | Returns |
|---|---|
| `Image.uint16()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.uint32

Casts the input value to an unsigned 32-bit integer.

| Usage | Returns |
|---|---|
| `Image.uint32()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.uint8

Casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Image.uint8()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `value` | Image | The image to which the operation is applied. |

## ee.Image.unitScale

Scales the input so that the range of input values \[low, high\] becomes \[0, 1\]. Values outside the range are NOT clamped. This algorithm always produces floating point pixels.

| Usage | Returns |
|---|---|
| `Image.unitScale(low, high)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The image to scale. |
| `low` | Float | The value mapped to 0. |
| `high` | Float | The value mapped to 1. |

## ee.Image.unmask

Replaces mask and value of the input image with the mask and value of another image at all positions where the input mask is zero.

The output image retains the metadata of the input image. By default, the output image also retains the footprint of the input, but setting sameFootprint to false allows to extend the footprint.

| Usage | Returns |
|---|---|
| `Image.unmask(*value*, *sameFootprint*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | Input image. |
| `value` | Image, default: null | New value and mask for the masked pixels of the input image. If not specified, defaults to constant zero image which is valid everywhere. |
| `sameFootprint` | Boolean, default: true | If true (or unspecified), the output retains the footprint of the input image. If false, the footprint of the output is the union of the input footprint with the footprint of the value image. |

## ee.Image.unmix

Unmix each pixel with the given endmembers, by computing the pseudo-inverse and multiplying it through each pixel. Returns an image of doubles with the same number of bands as endmembers.

| Usage | Returns |
|---|---|
| `Image.unmix(endmembers, *sumToOne*, *nonNegative*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The input image. |
| `endmembers` | List | The endmembers to unmix with. |
| `sumToOne` | Boolean, default: false | Constrain the outputs to sum to one. |
| `nonNegative` | Boolean, default: false | Constrain the outputs to be non-negative. |

## ee.Image.updateMask

Updates an image's mask at all positions where the existing mask is not zero. The output image retains the metadata and footprint of the input image.

| Usage | Returns |
|---|---|
| `Image.updateMask(mask)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | Input image. |
| `mask` | Image | New mask for the image, as a floating-point value in the range \[0, 1\] (invalid = 0, valid = 1). If this image has a single band, it is used for all bands in the input image; otherwise, must have the same number of bands as the input image. |

## ee.Image.visualize

Produces an RGB or grayscale visualization of an image. Each of the gain, bias, min, max and gamma arguments can take either a single value, which will be applied to all bands, or a list of values the same length as bands.

| Usage | Returns |
|---|---|
| `Image.visualize(*bands*, *gain*, *bias*, *min*, *max*, *gamma*, *opacity*, *palette*, *forceRgbOutput*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image to visualize. |
| `bands` | Object, default: null | A list of the bands to visualize. If empty, the first 3 are used. |
| `gain` | Object, default: null | The visualization gain(s) to use. |
| `bias` | Object, default: null | The visualization bias(es) to use. |
| `min` | Object, default: null | The value(s) to map to RGB8 value 0. |
| `max` | Object, default: null | The value(s) to map to RGB8 value 255. |
| `gamma` | Object, default: null | The gamma correction factor(s) to use. |
| `opacity` | Number, default: null | The opacity scaling factor to use. |
| `palette` | Object, default: null | The color palette to use. List of CSS color identifiers or hexadecimal color strings (e.g., \['red', '00FF00', 'blueviolet'\]). |
| `forceRgbOutput` | Boolean, default: false | Whether to produce RGB output even for single-band inputs. |

## ee.Image.where

Performs conditional replacement of values.

For each pixel in each band of 'input', if the corresponding pixel in 'test' is nonzero, output the corresponding pixel in value, otherwise output the input pixel.

If at a given pixel, either test or value is masked, the input value is used. If the input is masked, nothing is done.

The output bands have the same names as the input bands. The output type of each band is the larger of the input and value types. The output image retains the metadata and footprint of the input image.

| Usage | Returns |
|---|---|
| `Image.where(test, value)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Image | The input image. |
| `test` | Image | The test image. The pixels of this image determines which of the input pixels is returned. If this is a single band, it is used for all bands in the input image. This may not be an array image. |
| `value` | Image | The output value to use where test is not zero. If this is a single band, it is used for all bands in the input image. |

## ee.Image.zeroCrossing

Finds zero-crossings on each band of an image.

| Usage | Returns |
|---|---|
| `Image.zeroCrossing()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `image` | Image | The image from which to compute zero crossings. |

## ee.ImageCollection

ImageCollections can be constructed from the following arguments:

- A string: assumed to be the name of a collection,

- A list of images, or anything that can be used to construct an image.

- A single image.

- A computed object - reinterpreted as a collection.

| Usage | Returns |
|---|---|
| `ee.ImageCollection(args)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| `args` | ComputedObject\|Image\|List\[Object\]\|String | The constructor arguments. |

## ee.ImageCollection.aggregate_array

Aggregates over a given property of the objects in a collection, calculating a list of all the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_array(property)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_count

Aggregates over a given property of the objects in a collection, calculating the number of non-null values of the property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_count(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_count_distinct

Aggregates over a given property of the objects in a collection, calculating the number of distinct values for the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_count_distinct(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_first

Aggregates over a given property of the objects in a collection, calculating the property value of the first object in the collection.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_first(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_histogram

Aggregates over a given property of the objects in a collection, calculating a histogram of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_histogram(property)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_max

Aggregates over a given property of the objects in a collection, calculating the maximum of the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_max(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_mean

Aggregates over a given property of the objects in a collection, calculating the mean of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_mean(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_min

Aggregates over a given property of the objects in a collection, calculating the minimum of the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_min(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_product

Aggregates over a given property of the objects in a collection, calculating the product of the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_product(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_sample_sd

Aggregates over a given property of the objects in a collection, calculating the sample std. deviation of the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_sample_sd(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_sample_var

Aggregates over a given property of the objects in a collection, calculating the sample variance of the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_sample_var(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_stats

Aggregates over a given property of the objects in a collection, calculating the sum, min, max, mean, sample standard deviation, sample variance, total standard deviation and total variance of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_stats(property)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_sum

Aggregates over a given property of the objects in a collection, calculating the sum of the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_sum(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_total_sd

Aggregates over a given property of the objects in a collection, calculating the total std. deviation of the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_total_sd(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.aggregate_total_var

Aggregates over a given property of the objects in a collection, calculating the total variance of the values of the selected property.

| Usage | Returns |
|---|---|
| `ImageCollection.aggregate_total_var(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `property` | String | The property to use from each element of the collection. |

## ee.ImageCollection.and

Reduces an image collection by setting each pixel to 1 if and only if all the non-masked values at that pixel are non-zero across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.and()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `ImageCollection.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.ImageCollection.bounds

Constructs a bounding box around the geometries in a collection.

| Usage | Returns |
|---|---|
| `ImageCollection.bounds(*maxError*, *proj*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection whose bounds will be constructed. |
| `maxError` | ErrorMargin, optional | The maximum amount of error tolerated when performing any necessary reprojection. |
| `proj` | Projection, optional | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326. |

## ee.ImageCollection.cast

Casts some or all bands of each image in an ImageCollection to the specified types.

| Usage | Returns |
|---|---|
| `ImageCollection.cast(bandTypes, bandOrder)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to cast. |
| `bandTypes` | Dictionary | A dictionary from band name to band types. Types can be PixelTypes or strings. The valid strings are: 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'byte', 'short', 'int', 'long', 'float', and 'double'. Must include all bands already in any image in the collection. If this includes bands that are not already in an input image, they will be added to the image as transparent bands. |
| `bandOrder` | List | A list specifying the order of the bands in the result. Must match the keys of bandTypes. |

## ee.ImageCollection.combine

Makes a new collection that is a copy of the images in primary, adding all the bands from the image in secondary with a matching ID. If there are no matching IDs, the resulting collection will be empty. This is equivalent to an inner join on ID with merging of the bands of the result.

Note that this algorithm assumes that for a matching pair of inputs, both have the same footprint and metadata.

| Usage | Returns |
|---|---|
| `ImageCollection.combine(secondary, *overwrite*)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| this: `primary` | ImageCollection | The primary collection to join. |
| `secondary` | ImageCollection | The secondary collection to join. |
| `overwrite` | Boolean, default: false | If true, bands with the same name will get overwritten. If false, bands with the same name will be renamed. |

## ee.ImageCollection.copyProperties

Copies metadata properties from one element to another.

| Usage | Returns |
|---|---|
| `ImageCollection.copyProperties(*source*, *properties*, *exclude*)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `destination` | Element, default: null | The object whose properties to override. |
| `source` | Element, default: null | The object from which to copy the properties. |
| `properties` | List, default: null | The properties to copy. If omitted, all ordinary (i.e. non-system) properties are copied. |
| `exclude` | List, default: null | The list of properties to exclude when copying all properties. Must not be specified if properties is. |

## ee.ImageCollection.count

Reduces an image collection by calculating the number of images with a valid mask at each pixel across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.count()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.distance

Produces a DOUBLE image where each pixel is the distance in meters from the pixel center to the nearest Point, LineString, or polygonal boundary in the collection.

Note distance is also measured within interiors of polygons. Pixels that are not within 'searchRadius' meters of a geometry will be masked out.

Distances are computed on a sphere, so there is a small error proportional to the latitude difference between each pixel and the nearest geometry.

| Usage | Returns |
|---|---|
| `ImageCollection.distance(*searchRadius*, *maxError*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `features` | FeatureCollection | Feature collection from which to get features used to compute pixel distances. |
| `searchRadius` | Float, default: 100000 | Maximum distance in meters from each pixel to look for edges. Pixels will be masked unless there are edges within this distance. |
| `maxError` | Float, default: 100 | Maximum reprojection error in meters, only used if the input polylines require reprojection. If '0' is provided, then this operation will fail if projection is required. |

## ee.ImageCollection.distinct

Removes duplicates from a collection. Note that duplicates are determined using a strong hash over the serialized form of the selected properties.

| Usage | Returns |
|---|---|
| `ImageCollection.distinct(properties)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection from which objects will be selected. |
| `properties` | Object | A property name or a list of property names to use for comparison. The '.geo' property can be included to compare object geometries. |

## ee.ImageCollection.draw

Paints a vector collection for visualization. Not intended for use as input to other algorithms.

| Usage | Returns |
|---|---|
| `ImageCollection.draw(color, *pointRadius*, *strokeWidth*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to draw. |
| `color` | String | A hex string in the format RRGGBB specifying the color to use for drawing the features. |
| `pointRadius` | Integer, default: 3 | The radius in pixels of the point markers. |
| `strokeWidth` | Integer, default: 2 | The width in pixels of lines and polygon borders. |

## ee.ImageCollection.errorMatrix

Computes a 2D error matrix for a collection by comparing two columns of a collection: one containing the actual values, and one containing predicted values. The values are expected to be small contiguous integers, starting from 0. Axis 0 (the rows) of the matrix correspond to the actual values, and Axis 1 (the columns) to the predicted values.

| Usage | Returns |
|---|---|
| `ImageCollection.errorMatrix(actual, predicted, *order*)` | ConfusionMatrix |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection. |
| `actual` | String | The name of the property containing the actual value. |
| `predicted` | String | The name of the property containing the predicted value. |
| `order` | List, default: null | A list of the expected values. If this argument is not specified, the values are assumed to be contiguous and span the range 0 to maxValue. If specified, only values matching this list are used, and the matrix will have dimensions and order matching this list. |

## ee.ImageCollection.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `ImageCollection.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.ImageCollection.filter

Apply a filter to this collection.

Returns the filtered collection.

| Usage | Returns |
|---|---|
| `ImageCollection.filter(filter)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `filter` | Filter | A filter to apply to this collection. |

## ee.ImageCollection.filterBounds

Shortcut to filter a collection by intersection with geometry. Items in the collection with a footprint that fails to intersect the given geometry will be excluded.

This is equivalent to this.filter(ee.Filter.bounds(...)).

> [!CAUTION]
> **Caution:** providing a large or complex collection as the `geometry` argument can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.

Returns the filtered collection.

| Usage | Returns |
|---|---|
| `ImageCollection.filterBounds(geometry)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `geometry` | ComputedObject\|FeatureCollection\|Geometry | The geometry, feature or collection to intersect with. |

## ee.ImageCollection.filterDate

Shortcut to filter a collection by a date range. The start and end may be Dates, numbers (interpreted as milliseconds since 1970-01-01T00:00:00Z), or strings (such as '1996-01-01T08:00'). Based on 'system:time_start'.

This is equivalent to this.filter(ee.Filter.date(...)); see the ee.Filter type for other date filtering options.

Returns the filtered collection.

| Usage | Returns |
|---|---|
| `ImageCollection.filterDate(start, *end*)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `start` | Date\|Number\|String | The start date (inclusive). |
| `end` | Date\|Number\|String, optional | The end date (exclusive). Optional. If not specified, a 1-millisecond range starting at 'start' is created. |

## ee.ImageCollection.first

Returns the first entry from a given collection.

| Usage | Returns |
|---|---|
| `ImageCollection.first()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `imagecollection` | ImageCollection | The ImageCollection instance. |

## ee.ImageCollection.flatten

Flattens collections of collections.

| Usage | Returns |
|---|---|
| `ImageCollection.flatten()` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection of collections. |

## ee.ImageCollection.formaTrend

Computes the long and short term trends of a time series or optionally, the trends of the ratio of the time series and a covariate. The long term trend is estimated from the linear term of a regression on the full time series. The short term trend is computed as the windowed minimum over the time series.

The time series and covariate series are expected to contain a single band each, and the time series is expected to be evenly spaced in time. The output is 4 float bands: the long and short term trends, the t-test of the long term trend against the time series, and the Bruce Hansen test of parameter stability.

| Usage | Returns |
|---|---|
| `ImageCollection.formaTrend(*covariates*, *windowSize*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `timeSeries` | ImageCollection | Collection from which to extract trends. |
| `covariates` | ImageCollection, default: null | Cofactors to use in the trend analysis. |
| `windowSize` | Integer, default: 6 | Short term trend analysis window size, in images. |

## ee.ImageCollection.fromImages

Returns the image collection containing the given images.

| Usage | Returns |
|---|---|
| `ee.ImageCollection.fromImages(images)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| `images` | List | The images to include in the collection. |

## ee.ImageCollection.geometry

Extracts and merges the geometries of a collection. Requires that all the geometries in the collection share the projection and edge interpretation.

> [!CAUTION]
> **Caution:** providing a large or complex collection as input can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection that is required to achieve the desired outcome.

> [!NOTE]
> **Note:** If only a bounding box around the collection is needed, consider using Collection.bounds instead.

| Usage | Returns |
|---|---|
| `ImageCollection.geometry(*maxError*)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection whose geometries will be extracted. |
| `maxError` | ErrorMargin, optional | An error margin to use when merging geometries. |

## ee.ImageCollection.get

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `ImageCollection.get(property)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.ImageCollection.getArray

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `ImageCollection.getArray(property)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.ImageCollection.getFilmstripThumbURL

Get the URL of a tiled thumbnail for this ImageCollection.

Returns a thumbnail URL, or undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `ImageCollection.getFilmstripThumbURL(params, *callback*)` | Object\|String |

| Argument | Type | Details |
|---|---|---|
| this: `imagecollection` | ImageCollection | The ImageCollection instance. |
| `params` | Object | Parameters identical to ee.data.getMapId, plus, optionally: |---| | ` dimensions ` (a number or pair of numbers in format WIDTHxHEIGHT) Maximum dimensions of each thumbnail frame to render, in pixels. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling. | | ` region ` (E,S,W,N or GeoJSON) Geospatial region of the image to render. By default, the whole image. | | ` format ` (string) Encoding format. Only 'png' or 'jpg' are accepted. | |
| `callback` | Function, optional | An optional callback which handles the resulting URL string. If not supplied, the call is made synchronously. |

## ee.ImageCollection.getInfo

An imperative function that returns all the known information about this collection via an AJAX call.

Returns a collection description whose fields include:

- features: a list containing metadata about the images in the collection.

- bands: a dictionary describing the bands of the images in this collection.

- properties: an optional dictionary containing the collection's metadata properties.

| Usage | Returns |
|---|---|
| `ImageCollection.getInfo(*callback*)` | ImageCollectionDescription |

| Argument | Type | Details |
|---|---|---|
| this: `imagecollection` | ImageCollection | The ImageCollection instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. If supplied, will be called with the first parameter if successful and the second if unsuccessful. |

## ee.ImageCollection.getMapId

An imperative function that returns a map ID via a synchronous AJAX call.

This mosaics the collection to a single image and return a map ID suitable for building a Google Maps overlay.

Returns returns a map ID and optional token, which may be passed to ee.data.getTileUrl or ui.Map.addLayer. Undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `ImageCollection.getMapId(*visParams*, *callback*)` | MapId\|Object |

| Argument | Type | Details |
|---|---|---|
| this: `imagecollection` | ImageCollection | The ImageCollection instance. |
| `visParams` | Object, optional | The visualization parameters. |
| `callback` | Function, optional | An async callback. If not supplied, the call is made synchronously. |

## ee.ImageCollection.getNumber

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `ImageCollection.getNumber(property)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.ImageCollection.getRegion

Output an array of values for each \[pixel, band, image\] tuple in an ImageCollection. The output contains rows of id, lon, lat, time, and all bands for each image that intersects each pixel in the given region. Attempting to extract more than 1048576 values will result in an error.

| Usage | Returns |
|---|---|
| `ImageCollection.getRegion(geometry, *scale*, *crs*, *crsTransform*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to extract data from. |
| `geometry` | Geometry | The region over which to extract data. |
| `scale` | Float, default: null | A nominal scale in meters of the projection to work in. |
| `crs` | Projection, optional | The projection to work in. If unspecified, defaults to EPSG:4326. If specified in addition to scale, the projection is rescaled to the specified scale. |
| `crsTransform` | List, default: null | The array of CRS transform values. This is a row-major ordering of a 3x2 affine transform. This option is mutually exclusive with the scale option, and will replace any transform already set on the given projection. |

## ee.ImageCollection.getString

Extract a property from a feature.

| Usage | Returns |
|---|---|
| `ImageCollection.getString(property)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `object` | Element | The feature to extract the property from. |
| `property` | String | The property to extract. |

## ee.ImageCollection.getVideoThumbURL

Get the URL of an animated thumbnail for this ImageCollection.

Returns a thumbnail URL, or undefined if a callback was specified.

| Usage | Returns |
|---|---|
| `ImageCollection.getVideoThumbURL(params, *callback*)` | Object\|String |

| Argument | Type | Details |
|---|---|---|
| this: `imagecollection` | ImageCollection | The ImageCollection instance. |
| `params` | Object | Parameters identical to ee.data.getMapId, plus, optionally: |---| | ` dimensions ` (a number or pair of numbers in format WIDTHxHEIGHT) Maximum dimensions of the thumbnail to render, in pixels. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling. | | ` region ` (E,S,W,N or GeoJSON) Geospatial region of the image to render. By default, the whole image. | | ` format ` (string) Encoding format. Only 'gif' is accepted. | | ` framesPerSecond ` (number) Animation speed. | |
| `callback` | Function, optional | An optional callback which handles the resulting URL string. If not supplied, the call is made synchronously. |

## ee.ImageCollection.iterate

Applies a user-supplied function to each element of a collection. The user-supplied function is given two arguments: the current element, and the value returned by the previous call to iterate() or the first argument, for the first iteration. The result is the value returned by the final call to the user-supplied function.

Returns the result of the Collection.iterate() call.

| Usage | Returns |
|---|---|
| `ImageCollection.iterate(algorithm, *first*)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `algorithm` | Function | The function to apply to each element. Must take two arguments: an element of the collection and the value from the previous iteration. |
| `first` | Object, optional | The initial state. |

## ee.ImageCollection.limit

Limit a collection to the specified number of elements, optionally sorting them by a specified property first.

Returns the limited collection.

| Usage | Returns |
|---|---|
| `ImageCollection.limit(max, *property*, *ascending*)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `max` | Number | The number to limit the collection to. |
| `property` | String, optional | The property to sort by, if sorting. |
| `ascending` | Boolean, optional | Whether to sort in ascending or descending order. The default is true (ascending). |

## ee.ImageCollection.linkCollection

Links images in this collection to matching images from `imageCollection`.

For each source image in this collection, any specified bands or metadata will be added to the source image from the matching image found in

`imageCollection`. If bands or metadata are already present, they will be overwritten. If matching images are not found, any new or updated bands will be fully masked and any new or updated metadata will be null. The output footprint will be the same as the source image footprint.

Matches are determined if a source image and an image in `imageCollection` have a specific equivalent metadata property. If more than one collection image would match, the collection image selected is arbitrary. By default, images are matched on their 'system:index' metadata property.

This linking function is a convenience method for adding bands to target images based on a specified shared metadata property and is intended to support linking collections that apply different processing/product generation to the same source imagery. For more expressive linking known as

'joining', see https://developers.google.com/earth-engine/guides/joins_intro.

Returns the linked image collection.

| Usage | Returns |
|---|---|
| `ImageCollection.linkCollection(imageCollection, *linkedBands*, *linkedProperties*, *matchPropertyName*)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| this: `imagecollection` | ImageCollection | The ImageCollection instance. |
| `imageCollection` | ImageCollection | The image collection searched to find matches from this collection. |
| `linkedBands` | List\[String\], optional | Optional list of band names to add or update from matching images. |
| `linkedProperties` | List\[String\], optional | Optional list of metadata properties to add or update from matching images. |
| `matchPropertyName` | String, optional | The metadata property name to use as a match criteria. Defaults to "system:index". |

## ee.ImageCollection.load

Returns the image collection given its ID.

| Usage | Returns |
|---|---|
| `ee.ImageCollection.load(id, *version*)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| `id` | String | The asset ID of the image collection. |
| `version` | Long, default: null | The version of the asset. -1 signifies the latest version. |

## ee.ImageCollection.loadZarrV2Array

Loads a Zarr v2 array with 3 or more dimensions (i.e., 1 or more non-spatial dimensions) as an ImageCollection by slicing along a specified non-spatial axis. The array attributes (.zattrs) must contain the field '_ARRAY_DIMENSIONS', which is a list of the names of each dimension (e.g., \['time', 'y', 'x'\]). There must be at least two dimensions, with the final two representing Y and X respectively (e.g., \['lat', 'lon'\]). The supported compression codecs are 'blosc', 'gzip', 'lz4', 'zlib', and 'zstd'. The supported blosc meta-compression codecs are 'lz4', lz4hc', 'zlib', and 'zstd' ('blosclz' is not supported).

| Usage | Returns |
|---|---|
| `ee.ImageCollection.loadZarrV2Array(uri, proj, *axis*, *starts*, *ends*)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| `uri` | String | The Cloud Storage URI of the .zarray file to load. A .zmetadata file must be present in the parent directory of the array's directory (e.g., for 'gs://b/o/.zarray', 'gs://b/.zmetadata' must be present). The bucket metadata must be accessible (requires the \`storage.buckets.get\` permission which is provided by the role "Storage Legacy Bucket Reader" among others, see https://cloud.google.com/storage/docs/access-control/iam-roles) and the bucket must be located in the US multi-region, a dual-region including US-CENTRAL1, or the US-CENTRAL1 region. |
| `proj` | Projection | The projection of the array. |
| `axis` | Integer, default: null | The non-spatial axis (0-indexed) along which to slice the array to create an ImageCollection. Each image in the collection represents a single slice (length 1) along this axis. If null, defaults to 0. The value must be in the range \[0, N-1\], where N is the number of non-spatial dimensions (i.e., total dimensions - 2). The array must have at least one non-spatial dimension (i.e., be at least 3 dimensional). |
| `starts` | List, default: null | The indices (inclusive) at which to start taking slices along each non-spatial dimension. If null, slices will start at index 0 for all non-spatial dimensions. If specified, this list must have a length equal to the number of non-spatial dimensions (total dimensions - 2). An individual element within the list may be null, which defaults to 0 for that dimension. Negative indices are counted from the end of the dimension (e.g., -1 is the last element). |
| `ends` | List, default: null | The indices (exclusive) at which to stop taking slices along each non-spatial dimension. If null, slices will extend to the end of each corresponding non-spatial dimension (i.e., defaults to the length of the dimension). If specified, this list must have a length equal to the number of non-spatial dimensions (total dimensions - 2). An individual element within the list may be null, which also defaults to the length of that dimension. Negative indices are counted from the end of the dimension (e.g., -1 is the last element). |

## ee.ImageCollection.map

Maps an algorithm over a collection.

Returns the mapped collection.

| Usage | Returns |
|---|---|
| `ImageCollection.map(algorithm, *dropNulls*)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `algorithm` | Function | The operation to map over the images or features of the collection. A JavaScript function that receives an image or features and returns one. The function is called only once and the result is captured as a description, so it cannot perform imperative operations or rely on external state. |
| `dropNulls` | Boolean, optional | If true, the mapped algorithm is allowed to return nulls, and the elements for which it returns nulls will be dropped. |

## ee.ImageCollection.max

Reduces an image collection by calculating the maximum value of each pixel across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.max()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.mean

Reduces an image collection by calculating the mean of all values at each pixel across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.mean()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.median

Reduces an image collection by calculating the median of all values at each pixel across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.median()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.merge

Merges two image collections into one. The result has all the images that were in either collection.

| Usage | Returns |
|---|---|
| `ImageCollection.merge(collection2)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection1` | ImageCollection | The first collection to merge. |
| `collection2` | ImageCollection | The second collection to merge. |

## ee.ImageCollection.min

Reduces an image collection by calculating the minimum value of each pixel across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.min()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.mode

Reduces an image collection by calculating the most common value at each pixel across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.mode()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.mosaic

Composites all the images in a collection, using the mask.

| Usage | Returns |
|---|---|
| `ImageCollection.mosaic()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The collection to mosaic. |

## ee.ImageCollection.or

Reduces an image collection by setting each pixel to 1 if and only if any of the non-masked values at that pixel are non-zero across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.or()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.product

Reduces an image collection by calculating the product of all values at each pixel across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.product()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.propertyNames

Returns the names of properties on this element.

| Usage | Returns |
|---|---|
| `ImageCollection.propertyNames()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element |   |

## ee.ImageCollection.qualityMosaic

Composites all the images in a collection, using a quality band as a per-pixel ordering function.

| Usage | Returns |
|---|---|
| `ImageCollection.qualityMosaic(qualityBand)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The collection to mosaic. |
| `qualityBand` | String | The name of the quality band in the collection. |

## ee.ImageCollection.randomColumn

Adds a column of deterministic pseudorandom numbers to a collection. The outputs are double-precision floating point numbers. When using the 'uniform' distribution (default), outputs are in the range of \[0, 1). Using the 'normal' distribution, outputs have μ=0, σ=1, but have no explicit limits.

| Usage | Returns |
|---|---|
| `ImageCollection.randomColumn(*columnName*, *seed*, *distribution*, *rowKeys*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection to which to add a random column. |
| `columnName` | String, default: "random" | The name of the column to add. |
| `seed` | Long, default: 0 | A seed used when generating the random numbers. |
| `distribution` | String, default: "uniform" | The distribution type of random numbers to produce; one of 'uniform' or 'normal'. |
| `rowKeys` | List, optional | A list of properties that should uniquely and repeatably identify an element of the collection, used to generate the random number. Defaults to \[system:index\]. |

## ee.ImageCollection.reduce

Applies a reducer across all of the images in a collection.

If the reducer has a single input, it will be applied separately to each band of the collection; otherwise it must have the same number of inputs as the collection has bands.

The reducer output names determine the names of the output bands: reducers with multiple inputs will use the output names directly, while reducers with a single input will prefix the output name with the input band name (e.g., '10_mean', '20_mean').

| Usage | Returns |
|---|---|
| `ImageCollection.reduce(reducer, *parallelScale*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |
| `reducer` | Reducer | The reducer to apply to the given collection. |
| `parallelScale` | Float, default: 1 | A scaling factor used to limit memory use; using a larger parallelScale (e.g., 2 or 4) may enable computations that run out of memory with the default. |

## ee.ImageCollection.reduceColumns

Apply a reducer to each element of a collection, using the given selectors to determine the inputs.

Returns a dictionary of results, keyed with the output names.

| Usage | Returns |
|---|---|
| `ImageCollection.reduceColumns(reducer, selectors, *weightSelectors*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to aggregate over. |
| `reducer` | Reducer | The reducer to apply. |
| `selectors` | List | A selector for each input of the reducer. |
| `weightSelectors` | List, default: null | A selector for each weighted input of the reducer. |

## ee.ImageCollection.reduceToImage

Creates an image from a feature collection by applying a reducer over the selected properties of all the features that intersect each pixel.

| Usage | Returns |
|---|---|
| `ImageCollection.reduceToImage(properties, reducer)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | Feature collection to intersect with each output pixel. |
| `properties` | List | Properties to select from each feature and pass into the reducer. |
| `reducer` | Reducer | A Reducer to combine the properties of each intersecting feature into a final result to store in the pixel. |

## ee.ImageCollection.remap

Remaps the value of a specific property in a collection. Takes two parallel lists and maps values found in one to values in the other. Any element with a value that is not specified in the first list is dropped from the output collection.

| Usage | Returns |
|---|---|
| `ImageCollection.remap(lookupIn, lookupOut, columnName)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to be modified. |
| `lookupIn` | List | The input mapping values. Restricted to strings and integers. |
| `lookupOut` | List | The output mapping values. Must be the same size as lookupIn. |
| `columnName` | String | The name of the property to remap. |

## ee.ImageCollection.select

Select bands from each image in a collection.

Returns the image collection with selected bands.

| Usage | Returns |
|---|---|
| `ImageCollection.select(selectors, *names*)` | ImageCollection |

| Argument | Type | Details |
|---|---|---|
| this: `imagecollection` | ImageCollection | The ImageCollection instance. |
| `selectors` | List\[Object\] | A list of names, regexes or numeric indices specifying the bands to select. |
| `names` | List\[String\], optional | A list of new names for the output bands. Must match the number of bands selected. |

## ee.ImageCollection.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `ImageCollection.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.ImageCollection.set

Overrides one or more metadata properties of an Element.

Returns the element with the specified properties overridden.

| Usage | Returns |
|---|---|
| `ImageCollection.set(var_args)` | Element |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The Element instance. |
| `var_args` | VarArgs\[Object\] | Either a dictionary of properties, or a vararg sequence of properties, e.g. key1, value1, key2, value2, ... |

## ee.ImageCollection.size

Returns the number of elements in the collection.

| Usage | Returns |
|---|---|
| `ImageCollection.size()` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection to count. |

## ee.ImageCollection.sort

Sort a collection by the specified property.

Returns the sorted collection.

| Usage | Returns |
|---|---|
| `ImageCollection.sort(property, *ascending*)` | Collection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | Collection | The Collection instance. |
| `property` | String | The property to sort by. |
| `ascending` | Boolean, optional | Whether to sort in ascending or descending order. The default is true (ascending). |

## ee.ImageCollection.style

Draw a vector collection for visualization using a simple style language.

| Usage | Returns |
|---|---|
| `ImageCollection.style(*color*, *pointSize*, *pointShape*, *width*, *fillColor*, *styleProperty*, *neighborhood*, *lineType*)` | Image |

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

## ee.ImageCollection.sum

Reduces an image collection by calculating the sum of all values at each pixel across the stack of all matching bands. Bands are matched by name.

| Usage | Returns |
|---|---|
| `ImageCollection.sum()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The image collection to reduce. |

## ee.ImageCollection.toArray

Converts an image collection into an image of 2D arrays. At each pixel, the images that have valid (unmasked) values in all bands are laid out along the first axis of the array in the order they appear in the image collection. The bands of each image are laid out along the second axis of the array, in the order the bands appear in that image. The array element type will be the union of the types of each band.

| Usage | Returns |
|---|---|
| `ImageCollection.toArray()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | Image collection to convert to an array image. Bands must have scalar values, not array values. |

## ee.ImageCollection.toArrayPerBand

Concatenates multiple images into a single array image.

| Usage | Returns |
|---|---|
| `ImageCollection.toArrayPerBand(*axis*, *dropMasked*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | Images to concatenate. A separate concatenation is done per band, so all the images must have the same dimensionality and shape per band, except length along the concatenation axis. |
| `axis` | Integer, default: 0 | Axis to concatenate along; must be at least 0 and at most the minimum dimension of any band in the collection. |
| `dropMasked` | Boolean, default: false | If false (the default), the mask value of the output pixel is the minimum of the masks of the input pixels. If any image in the collection within the computation bounding box is completely masked at a pixel, that output pixel will be masked. As a result, every unmasked output pixel array will have the same size. If true, the mask value of the output pixel is the maximum of the mask of the inputs. Completely masked images at that pixel are ignored and do not contribute data to the output array. The output arrays will therefore not necessarily have the same size for each pixel. |

## ee.ImageCollection.toBands

Converts a collection to a single multi-band image containing all of the bands of every image in the collection. Output bands are named by prefixing the existing band names with the image id from which it came (e.g., 'image1_band1').

Note: The maximum number of bands is 5000.

| Usage | Returns |
|---|---|
| `ImageCollection.toBands()` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | ImageCollection | The input collection. |

## ee.ImageCollection.toDictionary

Extract properties from a feature as a dictionary.

| Usage | Returns |
|---|---|
| `ImageCollection.toDictionary(*properties*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `element` | Element | The feature to extract the property from. |
| `properties` | List, default: null | The list of properties to extract. Defaults to all non-system properties. |

## ee.ImageCollection.toList

Returns the elements of a collection as a list.

| Usage | Returns |
|---|---|
| `ImageCollection.toList(count, *offset*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The input collection to fetch. |
| `count` | Integer | The maximum number of elements to fetch. |
| `offset` | Integer, default: 0 | The number of elements to discard from the start. If set, (offset + count) elements will be fetched and the first offset elements will be discarded. |

## ee.ImageCollection.union

Merges all geometries in a given collection into one and returns a collection containing a single feature with only an ID of 'union_result' and a geometry.

| Usage | Returns |
|---|---|
| `ImageCollection.union(*maxError*)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `collection` | FeatureCollection | The collection being merged. |
| `maxError` | ErrorMargin, default: null | The maximum error allowed when performing any necessary reprojections. If not specified, defaults to the error margin requested from the output. |

## ee.Kernel.add

Adds two kernels (pointwise) after aligning their centers.

| Usage | Returns |
|---|---|
| `Kernel.add(kernel2, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| this: `kernel1` | Kernel | The first kernel. |
| `kernel2` | Kernel | The second kernel. |
| `normalize` | Boolean, default: false | Normalize the kernel. |

## ee.Kernel.chebyshev

Generates a distance kernel based on Chebyshev distance (greatest distance along any dimension).

| Usage | Returns |
|---|---|
| `ee.Kernel.chebyshev(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.circle

Generates a circle-shaped boolean kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.circle(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: true | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.compass

Generates a 3x3 Prewitt's Compass edge-detection kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.compass(*magnitude*, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `magnitude` | Float, default: 1 | Scale each value by this amount. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |

## ee.Kernel.cross

Generates a cross-shaped boolean kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.cross(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: true | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.diamond

Generates a diamond-shaped boolean kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.diamond(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: true | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.euclidean

Generates a distance kernel based on Euclidean (straight-line) distance.

| Usage | Returns |
|---|---|
| `ee.Kernel.euclidean(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.fixed

Creates a Kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.fixed(*width*, *height*, weights, *x*, *y*, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `width` | Integer, default: -1 | The width of the kernel in pixels. |
| `height` | Integer, default: -1 | The height of the kernel in pixels. |
| `weights` | List | A 2-D list of \[height\] x \[width\] values to use as the weights of the kernel. |
| `x` | Integer, default: -1 | The location of the focus, as an offset from the left. |
| `y` | Integer, default: -1 | The location of the focus, as an offset from the top. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |

## ee.Kernel.gaussian

Generates a Gaussian kernel from a sampled continuous Gaussian.

| Usage | Returns |
|---|---|
| `ee.Kernel.gaussian(radius, *sigma*, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `sigma` | Float, default: 1 | Standard deviation of the Gaussian function (same units as radius). |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: true | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.inverse

Returns a kernel which has each of its weights multiplicatively inverted. Weights with a value of zero are not inverted and remain zero.

| Usage | Returns |
|---|---|
| `Kernel.inverse()` | Kernel |

| Argument | Type | Details |
|---|---|---|
| this: `kernel` | Kernel | The kernel to have its entries inverted. |

## ee.Kernel.kirsch

Generates a 3x3 Kirsch's Compass edge-detection kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.kirsch(*magnitude*, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `magnitude` | Float, default: 1 | Scale each value by this amount. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |

## ee.Kernel.laplacian4

Generates a 3x3 Laplacian-4 edge-detection kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.laplacian4(*magnitude*, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `magnitude` | Float, default: 1 | Scale each value by this amount. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |

## ee.Kernel.laplacian8

Generates a 3x3 Laplacian-8 edge-detection kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.laplacian8(*magnitude*, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `magnitude` | Float, default: 1 | Scale each value by this amount. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |

## ee.Kernel.manhattan

Generates a distance kernel based on rectilinear (city-block) distance.

| Usage | Returns |
|---|---|
| `ee.Kernel.manhattan(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.octagon

Generates an octagon-shaped boolean kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.octagon(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: true | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.plus

Generates a plus-shaped boolean kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.plus(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: true | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.prewitt

Generates a 3x3 Prewitt edge-detection kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.prewitt(*magnitude*, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `magnitude` | Float, default: 1 | Scale each value by this amount. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |

## ee.Kernel.rectangle

Generates a rectangular-shaped kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.rectangle(xRadius, yRadius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `xRadius` | Float | The horizontal radius of the kernel to generate. |
| `yRadius` | Float | The vertical radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ("pixels" or "meters"). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: true | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.Kernel.roberts

Generates a 2x2 Roberts edge-detection kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.roberts(*magnitude*, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `magnitude` | Float, default: 1 | Scale each value by this amount. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |

## ee.Kernel.rotate

Creates a Kernel.

| Usage | Returns |
|---|---|
| `Kernel.rotate(rotations)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| this: `kernel` | Kernel | The kernel to be rotated. |
| `rotations` | Integer | Number of 90 degree rotations to make. Negative numbers rotate counterclockwise. |

## ee.Kernel.sobel

Generates a 3x3 Sobel edge-detection kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.sobel(*magnitude*, *normalize*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `magnitude` | Float, default: 1 | Scale each value by this amount. |
| `normalize` | Boolean, default: false | Normalize the kernel values to sum to 1. |

## ee.Kernel.square

Generates a square-shaped boolean kernel.

| Usage | Returns |
|---|---|
| `ee.Kernel.square(radius, *units*, *normalize*, *magnitude*)` | Kernel |

| Argument | Type | Details |
|---|---|---|
| `radius` | Float | The radius of the kernel to generate. |
| `units` | String, default: "pixels" | The system of measurement for the kernel ('pixels' or 'meters'). If the kernel is specified in meters, it will resize when the zoom-level is changed. |
| `normalize` | Boolean, default: true | Normalize the kernel values to sum to 1. |
| `magnitude` | Float, default: 1 | Scale each value by this amount. |

## ee.PixelType

Returns a PixelType of the given precision with the given limits per element, and an optional dimensionality.

| Usage | Returns |
|---|---|
| `ee.PixelType(precision, *minValue*, *maxValue*, *dimensions*)` | PixelType |

| Argument | Type | Details |
|---|---|---|
| `precision` | Object | The pixel precision, one of 'int', 'float', or 'double'. |
| `minValue` | Number, default: null | The minimum value of pixels of this type. If precision is 'float' or 'double', this can be null, signifying negative infinity. |
| `maxValue` | Number, default: null | The maximum value of pixels of this type. If precision is 'float' or 'double', this can be null, signifying positive infinity. |
| `dimensions` | Integer, default: 0 | The number of dimensions in which pixels of this type can vary; 0 is a scalar, 1 is a vector, 2 is a matrix, etc. |

## ee.PixelType.dimensions

Returns the number of dimensions for this type. Will be 0 for scalar values and \>= 1 for array values.

| Usage | Returns |
|---|---|
| `PixelType.dimensions()` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `pixelType` | PixelType |   |

## ee.PixelType.double

Returns the 64-bit floating point pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.double()` | PixelType |

**No arguments.**

## ee.PixelType.float

Returns the 32-bit floating point pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.float()` | PixelType |

**No arguments.**

## ee.PixelType.int16

Returns the 16-bit signed integer pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.int16()` | PixelType |

**No arguments.**

## ee.PixelType.int32

Returns the 32-bit signed integer pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.int32()` | PixelType |

**No arguments.**

## ee.PixelType.int64

Returns the 64-bit signed integer pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.int64()` | PixelType |

**No arguments.**

## ee.PixelType.int8

Returns the 8-bit signed integer pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.int8()` | PixelType |

**No arguments.**

## ee.PixelType.maxValue

Returns the maximum value of the PixelType.

| Usage | Returns |
|---|---|
| `PixelType.maxValue()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `pixelType` | PixelType |   |

## ee.PixelType.minValue

Returns the minimum value of the PixelType.

| Usage | Returns |
|---|---|
| `PixelType.minValue()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `pixelType` | PixelType |   |

## ee.PixelType.precision

Returns the precision of the PixelType. One of 'int', 'float', or 'double'.

| Usage | Returns |
|---|---|
| `PixelType.precision()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `pixelType` | PixelType |   |

## ee.PixelType.uint16

Returns the 16-bit unsigned integer pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.uint16()` | PixelType |

**No arguments.**

## ee.PixelType.uint32

Returns the 32-bit unsigned integer pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.uint32()` | PixelType |

**No arguments.**

## ee.PixelType.uint8

Returns the 8-bit unsigned integer pixel type.

| Usage | Returns |
|---|---|
| `ee.PixelType.uint8()` | PixelType |

**No arguments.**

## ee.Terrain.aspect

Calculates aspect in degrees from a terrain DEM.

The local gradient is computed using the 4-connected neighbors of each pixel, so missing values will occur around the edges of an image.

| Usage | Returns |
|---|---|
| `ee.Terrain.aspect(input)` | Image |

| Argument | Type | Details |
|---|---|---|
| `input` | Image | An elevation image, in meters. |

## ee.Terrain.fillMinima

Fills local minima. Only works on INT types.

| Usage | Returns |
|---|---|
| `ee.Terrain.fillMinima(image, *borderValue*, *neighborhood*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to fill. |
| `borderValue` | Long, default: null | The border value. |
| `neighborhood` | Integer, default: 50 | The size of the neighborhood to compute over. |

## ee.Terrain.hillShadow

Creates a shadow band, with output 1 where pixels are illuminated and 0 where they are shadowed.

Takes as input an elevation band, azimuth and zenith of the light source in degrees, a neighborhood size, and whether or not to apply hysteresis when a shadow appears. Currently, this algorithm only works for Mercator projections, in which light rays are parallel.

| Usage | Returns |
|---|---|
| `ee.Terrain.hillShadow(image, azimuth, zenith, *neighborhoodSize*, *hysteresis*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to which to apply the shadow algorithm, in which each pixel should represent an elevation in meters. |
| `azimuth` | Float | Azimuth in degrees. |
| `zenith` | Float | Zenith in degrees. |
| `neighborhoodSize` | Integer, default: 0 | Neighborhood size. |
| `hysteresis` | Boolean, default: false | Use hysteresis. Less physically accurate, but may generate better images. |

## ee.Terrain.hillshade

Computes a simple hillshade from a DEM.

| Usage | Returns |
|---|---|
| `ee.Terrain.hillshade(input, *azimuth*, *elevation*)` | Image |

| Argument | Type | Details |
|---|---|---|
| `input` | Image | An elevation image, in meters. |
| `azimuth` | Float, default: 270 | The illumination azimuth in degrees from north. |
| `elevation` | Float, default: 45 | The illumination elevation in degrees. |

## ee.Terrain.products

Calculates slope, aspect, and a simple hillshade from a terrain DEM.

Expects an image containing either a single band of elevation, measured in meters, or if there's more than one band, one named 'elevation'. Adds output bands named 'slope' and 'aspect' measured in degrees plus an unsigned byte output band named 'hillshade' for visualization. All other bands and metadata are copied from the input image. The local gradient is computed using the 4-connected neighbors of each pixel, so missing values will occur around the edges of an image.

| Usage | Returns |
|---|---|
| `ee.Terrain.products(input)` | Image |

| Argument | Type | Details |
|---|---|---|
| `input` | Image | An elevation image, in meters. |

## ee.Terrain.slope

Calculates slope in degrees from a terrain DEM.

The local gradient is computed using the 4-connected neighbors of each pixel, so missing values will occur around the edges of an image.

| Usage | Returns |
|---|---|
| `ee.Terrain.slope(input)` | Image |

| Argument | Type | Details |
|---|---|---|
| `input` | Image | An elevation image, in meters. |

