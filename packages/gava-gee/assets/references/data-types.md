# Tipos de dado — Number, String, List, Dictionary, Date, Array

> 327 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.Array`](#ee-array)
- [`ee.Array.abs`](#ee-array-abs)
- [`ee.Array.accum`](#ee-array-accum)
- [`ee.Array.acos`](#ee-array-acos)
- [`ee.Array.add`](#ee-array-add)
- [`ee.Array.and`](#ee-array-and)
- [`ee.Array.argmax`](#ee-array-argmax)
- [`ee.Array.asin`](#ee-array-asin)
- [`ee.Array.atan`](#ee-array-atan)
- [`ee.Array.atan2`](#ee-array-atan2)
- [`ee.Array.bitCount`](#ee-array-bitcount)
- [`ee.Array.bitsToArray`](#ee-array-bitstoarray)
- [`ee.Array.bitwiseAnd`](#ee-array-bitwiseand)
- [`ee.Array.bitwiseNot`](#ee-array-bitwisenot)
- [`ee.Array.bitwiseOr`](#ee-array-bitwiseor)
- [`ee.Array.bitwiseXor`](#ee-array-bitwisexor)
- [`ee.Array.byte`](#ee-array-byte)
- [`ee.Array.cat`](#ee-array-cat)
- [`ee.Array.cbrt`](#ee-array-cbrt)
- [`ee.Array.ceil`](#ee-array-ceil)
- [`ee.Array.cos`](#ee-array-cos)
- [`ee.Array.cosh`](#ee-array-cosh)
- [`ee.Array.cut`](#ee-array-cut)
- [`ee.Array.digamma`](#ee-array-digamma)
- [`ee.Array.divide`](#ee-array-divide)
- [`ee.Array.dotProduct`](#ee-array-dotproduct)
- [`ee.Array.double`](#ee-array-double)
- [`ee.Array.eigen`](#ee-array-eigen)
- [`ee.Array.eq`](#ee-array-eq)
- [`ee.Array.erf`](#ee-array-erf)
- [`ee.Array.erfInv`](#ee-array-erfinv)
- [`ee.Array.erfc`](#ee-array-erfc)
- [`ee.Array.erfcInv`](#ee-array-erfcinv)
- [`ee.Array.exp`](#ee-array-exp)
- [`ee.Array.first`](#ee-array-first)
- [`ee.Array.firstNonZero`](#ee-array-firstnonzero)
- [`ee.Array.float`](#ee-array-float)
- [`ee.Array.floor`](#ee-array-floor)
- [`ee.Array.gamma`](#ee-array-gamma)
- [`ee.Array.gammainc`](#ee-array-gammainc)
- [`ee.Array.get`](#ee-array-get)
- [`ee.Array.gt`](#ee-array-gt)
- [`ee.Array.gte`](#ee-array-gte)
- [`ee.Array.hypot`](#ee-array-hypot)
- [`ee.Array.identity`](#ee-array-identity)
- [`ee.Array.int`](#ee-array-int)
- [`ee.Array.int16`](#ee-array-int16)
- [`ee.Array.int32`](#ee-array-int32)
- [`ee.Array.int64`](#ee-array-int64)
- [`ee.Array.int8`](#ee-array-int8)
- [`ee.Array.lanczos`](#ee-array-lanczos)
- [`ee.Array.leftShift`](#ee-array-leftshift)
- [`ee.Array.length`](#ee-array-length)
- [`ee.Array.log`](#ee-array-log)
- [`ee.Array.log10`](#ee-array-log10)
- [`ee.Array.long`](#ee-array-long)
- [`ee.Array.lt`](#ee-array-lt)
- [`ee.Array.lte`](#ee-array-lte)
- [`ee.Array.mask`](#ee-array-mask)
- [`ee.Array.matrixCholeskyDecomposition`](#ee-array-matrixcholeskydecomposition)
- [`ee.Array.matrixDeterminant`](#ee-array-matrixdeterminant)
- [`ee.Array.matrixDiagonal`](#ee-array-matrixdiagonal)
- [`ee.Array.matrixFnorm`](#ee-array-matrixfnorm)
- [`ee.Array.matrixInverse`](#ee-array-matrixinverse)
- [`ee.Array.matrixLUDecomposition`](#ee-array-matrixludecomposition)
- [`ee.Array.matrixMultiply`](#ee-array-matrixmultiply)
- [`ee.Array.matrixPseudoInverse`](#ee-array-matrixpseudoinverse)
- [`ee.Array.matrixQRDecomposition`](#ee-array-matrixqrdecomposition)
- [`ee.Array.matrixSingularValueDecomposition`](#ee-array-matrixsingularvaluedecomposition)
- [`ee.Array.matrixSolve`](#ee-array-matrixsolve)
- [`ee.Array.matrixToDiag`](#ee-array-matrixtodiag)
- [`ee.Array.matrixTrace`](#ee-array-matrixtrace)
- [`ee.Array.matrixTranspose`](#ee-array-matrixtranspose)
- [`ee.Array.max`](#ee-array-max)
- [`ee.Array.min`](#ee-array-min)
- [`ee.Array.mod`](#ee-array-mod)
- [`ee.Array.multiply`](#ee-array-multiply)
- [`ee.Array.neq`](#ee-array-neq)
- [`ee.Array.not`](#ee-array-not)
- [`ee.Array.or`](#ee-array-or)
- [`ee.Array.pad`](#ee-array-pad)
- [`ee.Array.pow`](#ee-array-pow)
- [`ee.Array.project`](#ee-array-project)
- [`ee.Array.reduce`](#ee-array-reduce)
- [`ee.Array.repeat`](#ee-array-repeat)
- [`ee.Array.reshape`](#ee-array-reshape)
- [`ee.Array.rightShift`](#ee-array-rightshift)
- [`ee.Array.round`](#ee-array-round)
- [`ee.Array.short`](#ee-array-short)
- [`ee.Array.signum`](#ee-array-signum)
- [`ee.Array.sin`](#ee-array-sin)
- [`ee.Array.sinh`](#ee-array-sinh)
- [`ee.Array.slice`](#ee-array-slice)
- [`ee.Array.sort`](#ee-array-sort)
- [`ee.Array.sqrt`](#ee-array-sqrt)
- [`ee.Array.subtract`](#ee-array-subtract)
- [`ee.Array.tan`](#ee-array-tan)
- [`ee.Array.tanh`](#ee-array-tanh)
- [`ee.Array.toByte`](#ee-array-tobyte)
- [`ee.Array.toDouble`](#ee-array-todouble)
- [`ee.Array.toFloat`](#ee-array-tofloat)
- [`ee.Array.toInt`](#ee-array-toint)
- [`ee.Array.toInt16`](#ee-array-toint16)
- [`ee.Array.toInt32`](#ee-array-toint32)
- [`ee.Array.toInt64`](#ee-array-toint64)
- [`ee.Array.toInt8`](#ee-array-toint8)
- [`ee.Array.toList`](#ee-array-tolist)
- [`ee.Array.toLong`](#ee-array-tolong)
- [`ee.Array.toShort`](#ee-array-toshort)
- [`ee.Array.toUint16`](#ee-array-touint16)
- [`ee.Array.toUint32`](#ee-array-touint32)
- [`ee.Array.toUint8`](#ee-array-touint8)
- [`ee.Array.transpose`](#ee-array-transpose)
- [`ee.Array.trigamma`](#ee-array-trigamma)
- [`ee.Array.uint16`](#ee-array-uint16)
- [`ee.Array.uint32`](#ee-array-uint32)
- [`ee.Array.uint8`](#ee-array-uint8)
- [`ee.Blob`](#ee-blob)
- [`ee.Blob.string`](#ee-blob-string)
- [`ee.Blob.url`](#ee-blob-url)
- [`ee.Date`](#ee-date)
- [`ee.Date.advance`](#ee-date-advance)
- [`ee.Date.aside`](#ee-date-aside)
- [`ee.Date.difference`](#ee-date-difference)
- [`ee.Date.evaluate`](#ee-date-evaluate)
- [`ee.Date.format`](#ee-date-format)
- [`ee.Date.fromYMD`](#ee-date-fromymd)
- [`ee.Date.get`](#ee-date-get)
- [`ee.Date.getFraction`](#ee-date-getfraction)
- [`ee.Date.getInfo`](#ee-date-getinfo)
- [`ee.Date.getRange`](#ee-date-getrange)
- [`ee.Date.getRelative`](#ee-date-getrelative)
- [`ee.Date.millis`](#ee-date-millis)
- [`ee.Date.parse`](#ee-date-parse)
- [`ee.Date.serialize`](#ee-date-serialize)
- [`ee.Date.unitRatio`](#ee-date-unitratio)
- [`ee.Date.update`](#ee-date-update)
- [`ee.DateRange`](#ee-daterange)
- [`ee.DateRange.contains`](#ee-daterange-contains)
- [`ee.DateRange.end`](#ee-daterange-end)
- [`ee.DateRange.intersection`](#ee-daterange-intersection)
- [`ee.DateRange.intersects`](#ee-daterange-intersects)
- [`ee.DateRange.isEmpty`](#ee-daterange-isempty)
- [`ee.DateRange.isUnbounded`](#ee-daterange-isunbounded)
- [`ee.DateRange.start`](#ee-daterange-start)
- [`ee.DateRange.unbounded`](#ee-daterange-unbounded)
- [`ee.DateRange.union`](#ee-daterange-union)
- [`ee.Dictionary`](#ee-dictionary)
- [`ee.Dictionary.aside`](#ee-dictionary-aside)
- [`ee.Dictionary.combine`](#ee-dictionary-combine)
- [`ee.Dictionary.contains`](#ee-dictionary-contains)
- [`ee.Dictionary.evaluate`](#ee-dictionary-evaluate)
- [`ee.Dictionary.fromLists`](#ee-dictionary-fromlists)
- [`ee.Dictionary.get`](#ee-dictionary-get)
- [`ee.Dictionary.getArray`](#ee-dictionary-getarray)
- [`ee.Dictionary.getGeometry`](#ee-dictionary-getgeometry)
- [`ee.Dictionary.getInfo`](#ee-dictionary-getinfo)
- [`ee.Dictionary.getNumber`](#ee-dictionary-getnumber)
- [`ee.Dictionary.getString`](#ee-dictionary-getstring)
- [`ee.Dictionary.keys`](#ee-dictionary-keys)
- [`ee.Dictionary.map`](#ee-dictionary-map)
- [`ee.Dictionary.remove`](#ee-dictionary-remove)
- [`ee.Dictionary.rename`](#ee-dictionary-rename)
- [`ee.Dictionary.select`](#ee-dictionary-select)
- [`ee.Dictionary.serialize`](#ee-dictionary-serialize)
- [`ee.Dictionary.set`](#ee-dictionary-set)
- [`ee.Dictionary.size`](#ee-dictionary-size)
- [`ee.Dictionary.toArray`](#ee-dictionary-toarray)
- [`ee.Dictionary.toImage`](#ee-dictionary-toimage)
- [`ee.Dictionary.values`](#ee-dictionary-values)
- [`ee.List`](#ee-list)
- [`ee.List.add`](#ee-list-add)
- [`ee.List.aside`](#ee-list-aside)
- [`ee.List.cat`](#ee-list-cat)
- [`ee.List.contains`](#ee-list-contains)
- [`ee.List.containsAll`](#ee-list-containsall)
- [`ee.List.distinct`](#ee-list-distinct)
- [`ee.List.equals`](#ee-list-equals)
- [`ee.List.evaluate`](#ee-list-evaluate)
- [`ee.List.filter`](#ee-list-filter)
- [`ee.List.flatten`](#ee-list-flatten)
- [`ee.List.frequency`](#ee-list-frequency)
- [`ee.List.get`](#ee-list-get)
- [`ee.List.getArray`](#ee-list-getarray)
- [`ee.List.getGeometry`](#ee-list-getgeometry)
- [`ee.List.getInfo`](#ee-list-getinfo)
- [`ee.List.getNumber`](#ee-list-getnumber)
- [`ee.List.getString`](#ee-list-getstring)
- [`ee.List.indexOf`](#ee-list-indexof)
- [`ee.List.indexOfSublist`](#ee-list-indexofsublist)
- [`ee.List.insert`](#ee-list-insert)
- [`ee.List.iterate`](#ee-list-iterate)
- [`ee.List.join`](#ee-list-join)
- [`ee.List.lastIndexOfSubList`](#ee-list-lastindexofsublist)
- [`ee.List.length`](#ee-list-length)
- [`ee.List.map`](#ee-list-map)
- [`ee.List.reduce`](#ee-list-reduce)
- [`ee.List.remove`](#ee-list-remove)
- [`ee.List.removeAll`](#ee-list-removeall)
- [`ee.List.repeat`](#ee-list-repeat)
- [`ee.List.replace`](#ee-list-replace)
- [`ee.List.replaceAll`](#ee-list-replaceall)
- [`ee.List.reverse`](#ee-list-reverse)
- [`ee.List.rotate`](#ee-list-rotate)
- [`ee.List.sequence`](#ee-list-sequence)
- [`ee.List.serialize`](#ee-list-serialize)
- [`ee.List.set`](#ee-list-set)
- [`ee.List.shuffle`](#ee-list-shuffle)
- [`ee.List.size`](#ee-list-size)
- [`ee.List.slice`](#ee-list-slice)
- [`ee.List.sort`](#ee-list-sort)
- [`ee.List.splice`](#ee-list-splice)
- [`ee.List.swap`](#ee-list-swap)
- [`ee.List.unzip`](#ee-list-unzip)
- [`ee.List.zip`](#ee-list-zip)
- [`ee.Number`](#ee-number)
- [`ee.Number.abs`](#ee-number-abs)
- [`ee.Number.acos`](#ee-number-acos)
- [`ee.Number.add`](#ee-number-add)
- [`ee.Number.and`](#ee-number-and)
- [`ee.Number.aside`](#ee-number-aside)
- [`ee.Number.asin`](#ee-number-asin)
- [`ee.Number.atan`](#ee-number-atan)
- [`ee.Number.atan2`](#ee-number-atan2)
- [`ee.Number.bitCount`](#ee-number-bitcount)
- [`ee.Number.bitwiseAnd`](#ee-number-bitwiseand)
- [`ee.Number.bitwiseNot`](#ee-number-bitwisenot)
- [`ee.Number.bitwiseOr`](#ee-number-bitwiseor)
- [`ee.Number.bitwiseXor`](#ee-number-bitwisexor)
- [`ee.Number.byte`](#ee-number-byte)
- [`ee.Number.cbrt`](#ee-number-cbrt)
- [`ee.Number.ceil`](#ee-number-ceil)
- [`ee.Number.clamp`](#ee-number-clamp)
- [`ee.Number.cos`](#ee-number-cos)
- [`ee.Number.cosh`](#ee-number-cosh)
- [`ee.Number.digamma`](#ee-number-digamma)
- [`ee.Number.divide`](#ee-number-divide)
- [`ee.Number.double`](#ee-number-double)
- [`ee.Number.eq`](#ee-number-eq)
- [`ee.Number.erf`](#ee-number-erf)
- [`ee.Number.erfInv`](#ee-number-erfinv)
- [`ee.Number.erfc`](#ee-number-erfc)
- [`ee.Number.erfcInv`](#ee-number-erfcinv)
- [`ee.Number.evaluate`](#ee-number-evaluate)
- [`ee.Number.exp`](#ee-number-exp)
- [`ee.Number.expression`](#ee-number-expression)
- [`ee.Number.first`](#ee-number-first)
- [`ee.Number.firstNonZero`](#ee-number-firstnonzero)
- [`ee.Number.float`](#ee-number-float)
- [`ee.Number.floor`](#ee-number-floor)
- [`ee.Number.format`](#ee-number-format)
- [`ee.Number.gamma`](#ee-number-gamma)
- [`ee.Number.gammainc`](#ee-number-gammainc)
- [`ee.Number.getInfo`](#ee-number-getinfo)
- [`ee.Number.gt`](#ee-number-gt)
- [`ee.Number.gte`](#ee-number-gte)
- [`ee.Number.hypot`](#ee-number-hypot)
- [`ee.Number.int`](#ee-number-int)
- [`ee.Number.int16`](#ee-number-int16)
- [`ee.Number.int32`](#ee-number-int32)
- [`ee.Number.int64`](#ee-number-int64)
- [`ee.Number.int8`](#ee-number-int8)
- [`ee.Number.lanczos`](#ee-number-lanczos)
- [`ee.Number.leftShift`](#ee-number-leftshift)
- [`ee.Number.log`](#ee-number-log)
- [`ee.Number.log10`](#ee-number-log10)
- [`ee.Number.long`](#ee-number-long)
- [`ee.Number.lt`](#ee-number-lt)
- [`ee.Number.lte`](#ee-number-lte)
- [`ee.Number.max`](#ee-number-max)
- [`ee.Number.min`](#ee-number-min)
- [`ee.Number.mod`](#ee-number-mod)
- [`ee.Number.multiply`](#ee-number-multiply)
- [`ee.Number.neq`](#ee-number-neq)
- [`ee.Number.not`](#ee-number-not)
- [`ee.Number.or`](#ee-number-or)
- [`ee.Number.parse`](#ee-number-parse)
- [`ee.Number.pow`](#ee-number-pow)
- [`ee.Number.rightShift`](#ee-number-rightshift)
- [`ee.Number.round`](#ee-number-round)
- [`ee.Number.serialize`](#ee-number-serialize)
- [`ee.Number.short`](#ee-number-short)
- [`ee.Number.signum`](#ee-number-signum)
- [`ee.Number.sin`](#ee-number-sin)
- [`ee.Number.sinh`](#ee-number-sinh)
- [`ee.Number.sqrt`](#ee-number-sqrt)
- [`ee.Number.subtract`](#ee-number-subtract)
- [`ee.Number.tan`](#ee-number-tan)
- [`ee.Number.tanh`](#ee-number-tanh)
- [`ee.Number.toByte`](#ee-number-tobyte)
- [`ee.Number.toDouble`](#ee-number-todouble)
- [`ee.Number.toFloat`](#ee-number-tofloat)
- [`ee.Number.toInt`](#ee-number-toint)
- [`ee.Number.toInt16`](#ee-number-toint16)
- [`ee.Number.toInt32`](#ee-number-toint32)
- [`ee.Number.toInt64`](#ee-number-toint64)
- [`ee.Number.toInt8`](#ee-number-toint8)
- [`ee.Number.toLong`](#ee-number-tolong)
- [`ee.Number.toShort`](#ee-number-toshort)
- [`ee.Number.toUint16`](#ee-number-touint16)
- [`ee.Number.toUint32`](#ee-number-touint32)
- [`ee.Number.toUint8`](#ee-number-touint8)
- [`ee.Number.trigamma`](#ee-number-trigamma)
- [`ee.Number.uint16`](#ee-number-uint16)
- [`ee.Number.uint32`](#ee-number-uint32)
- [`ee.Number.uint8`](#ee-number-uint8)
- [`ee.Number.unitScale`](#ee-number-unitscale)
- [`ee.String`](#ee-string)
- [`ee.String.aside`](#ee-string-aside)
- [`ee.String.cat`](#ee-string-cat)
- [`ee.String.compareTo`](#ee-string-compareto)
- [`ee.String.decodeJSON`](#ee-string-decodejson)
- [`ee.String.encodeJSON`](#ee-string-encodejson)
- [`ee.String.equals`](#ee-string-equals)
- [`ee.String.evaluate`](#ee-string-evaluate)
- [`ee.String.getInfo`](#ee-string-getinfo)
- [`ee.String.index`](#ee-string-index)
- [`ee.String.length`](#ee-string-length)
- [`ee.String.match`](#ee-string-match)
- [`ee.String.replace`](#ee-string-replace)
- [`ee.String.rindex`](#ee-string-rindex)
- [`ee.String.serialize`](#ee-string-serialize)
- [`ee.String.slice`](#ee-string-slice)
- [`ee.String.split`](#ee-string-split)
- [`ee.String.toLowerCase`](#ee-string-tolowercase)
- [`ee.String.toUpperCase`](#ee-string-touppercase)
- [`ee.String.trim`](#ee-string-trim)

---

## ee.Array

Returns an array with the given coordinates.

| Usage | Returns |
|---|---|
| `ee.Array(values, *pixelType*)` | Array |

| Argument | Type | Details |
|---|---|---|
| `values` | Object | An existing array to cast, or a number/list of numbers/nested list of numbers of any depth to create an array from. For nested lists, all inner arrays at the same depth must have the same length and numbers may only be present at the deepest level. |
| `pixelType` | PixelType, default: null | The type of each number in the values argument. If the pixel type is not provided, it will be inferred from the numbers in 'values'. If there aren't any numbers in 'values', this type must be provided. |

## ee.Array.abs

On an element-wise basis, computes the absolute value of the input.

| Usage | Returns |
|---|---|
| `Array.abs()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.accum

Accumulates elements of an array along the given axis, by setting each element of the result to the reduction of elements along that axis up to and including the current position. May be used to make a cumulative sum, a monotonically increasing sequence, etc.

| Usage | Returns |
|---|---|
| `Array.accum(axis, *reducer*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to accumulate. |
| `axis` | Integer | Axis along which to perform the accumulation. |
| `reducer` | Reducer, default: null | Reducer to accumulate values. Default is SUM, to produce the cumulative sum of each vector along the given axis. |

## ee.Array.acos

On an element-wise basis, computes the arccosine in radians of the input.

| Usage | Returns |
|---|---|
| `Array.acos()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.add

On an element-wise basis, adds the first value to the second.

| Usage | Returns |
|---|---|
| `Array.add(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.and

On an element-wise basis, returns 1 if and only if both values are non-zero.

| Usage | Returns |
|---|---|
| `Array.and(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.argmax

Returns the position, as a list of indices in each array axis, of the maximum value in an array, or null if the array is empty. If there are multiple occurrences of the maximum, returns the position of the first.

| Usage | Returns |
|---|---|
| `Array.argmax()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array |   |

## ee.Array.asin

On an element-wise basis, computes the arcsine in radians of the input.

| Usage | Returns |
|---|---|
| `Array.asin()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.atan

On an element-wise basis, computes the arctangent in radians of the input.

| Usage | Returns |
|---|---|
| `Array.atan()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.atan2

On an element-wise basis, calculates the angle formed by the 2D vector \[x, y\].

| Usage | Returns |
|---|---|
| `Array.atan2(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.bitCount

On an element-wise basis, calculates the number of one-bits in the 64-bit two's complement binary representation of the input.

| Usage | Returns |
|---|---|
| `Array.bitCount()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.bitsToArray

Converts the bits of an integer to an Array. The array has as many elements as the position of the highest set bit, or a single 0 for a value of 0.

| Usage | Returns |
|---|---|
| `ee.Array.bitsToArray(input)` | Array |

| Argument | Type | Details |
|---|---|---|
| `input` | Number | The integer to transform. |

## ee.Array.bitwiseAnd

On an element-wise basis, calculates the bitwise AND of the input values.

| Usage | Returns |
|---|---|
| `Array.bitwiseAnd(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.bitwiseNot

On an element-wise basis, calculates the bitwise NOT of the input, in the smallest signed integer type that can hold the input.

| Usage | Returns |
|---|---|
| `Array.bitwiseNot()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.bitwiseOr

On an element-wise basis, calculates the bitwise OR of the input values.

| Usage | Returns |
|---|---|
| `Array.bitwiseOr(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.bitwiseXor

On an element-wise basis, calculates the bitwise XOR of the input values.

| Usage | Returns |
|---|---|
| `Array.bitwiseXor(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.byte

On an element-wise basis, casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Array.byte()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.cat

Concatenates multiple arrays into a single array along the given axis. Each array must have the same dimensionality and the same length on all axes except the concatenation axis.

| Usage | Returns |
|---|---|
| `ee.Array.cat(arrays, *axis*)` | Array |

| Argument | Type | Details |
|---|---|---|
| `arrays` | List | Arrays to concatenate. |
| `axis` | Integer, default: 0 | Axis to concatenate along. |

## ee.Array.cbrt

On an element-wise basis, computes the cubic root of the input.

| Usage | Returns |
|---|---|
| `Array.cbrt()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.ceil

On an element-wise basis, computes the smallest integer greater than or equal to the input.

| Usage | Returns |
|---|---|
| `Array.ceil()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.cos

On an element-wise basis, computes the cosine of the input in radians.

| Usage | Returns |
|---|---|
| `Array.cos()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.cosh

On an element-wise basis, computes the hyperbolic cosine of the input.

| Usage | Returns |
|---|---|
| `Array.cosh()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.cut

Cut an array along one or more axes.

| Usage | Returns |
|---|---|
| `Array.cut(position)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | The array to cut. |
| `position` | List | Cut an array along one or more axes. The positions args specifies either a single value for each axis of the array, or -1, indicating the whole axis. The output will be an array that has the same dimensions as the input, with a length of 1 on each axis that was not -1 in the positions array. |

## ee.Array.digamma

On an element-wise basis, computes the digamma function of the input.

| Usage | Returns |
|---|---|
| `Array.digamma()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.divide

On an element-wise basis, divides the first value by the second, returning 0 for division by 0.

| Usage | Returns |
|---|---|
| `Array.divide(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.dotProduct

Compute the dot product between two 1-D arrays.

| Usage | Returns |
|---|---|
| `Array.dotProduct(array2)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `array1` | Array | The first 1-D array. |
| `array2` | Array | The second 1-D array. |

## ee.Array.double

On an element-wise basis, casts the input value to a 64-bit float.

| Usage | Returns |
|---|---|
| `Array.double()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.eigen

Computes the real eigenvectors and eigenvalues of a square 2D array of A rows and A columns. Returns an array with A rows and A+1 columns, where each row contains an eigenvalue in the first column, and the corresponding eigenvector in the remaining A columns. The rows are sorted by eigenvalue, in descending order.

This implementation uses DecompositionFactory.eig() from https://ejml.org.

| Usage | Returns |
|---|---|
| `Array.eigen()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | A square, 2D array from which to compute the eigenvalue decomposition. |

## ee.Array.eq

On an element-wise basis, returns 1 if and only if the first value is equal to the second.

| Usage | Returns |
|---|---|
| `Array.eq(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.erf

On an element-wise basis, computes the error function of the input.

| Usage | Returns |
|---|---|
| `Array.erf()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.erfInv

On an element-wise basis, computes the inverse error function of the input.

| Usage | Returns |
|---|---|
| `Array.erfInv()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.erfc

On an element-wise basis, computes the complementary error function of the input.

| Usage | Returns |
|---|---|
| `Array.erfc()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.erfcInv

On an element-wise basis, computes the inverse complementary error function of the input.

| Usage | Returns |
|---|---|
| `Array.erfcInv()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.exp

On an element-wise basis, computes the Euler's number e raised to the power of the input.

| Usage | Returns |
|---|---|
| `Array.exp()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.first

On an element-wise basis, selects the value of the first value.

| Usage | Returns |
|---|---|
| `Array.first(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.firstNonZero

On an element-wise basis, selects the first value if it is non-zero, and the second value otherwise.

| Usage | Returns |
|---|---|
| `Array.firstNonZero(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.float

On an element-wise basis, casts the input value to a 32-bit float.

| Usage | Returns |
|---|---|
| `Array.float()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.floor

On an element-wise basis, computes the largest integer less than or equal to the input.

| Usage | Returns |
|---|---|
| `Array.floor()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.gamma

On an element-wise basis, computes the gamma function of the input.

| Usage | Returns |
|---|---|
| `Array.gamma()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.gammainc

On an element-wise basis, calculates the regularized lower incomplete Gamma function γ(x,a).

| Usage | Returns |
|---|---|
| `Array.gammainc(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.get

Extracts the value at the given position from the input array.

| Usage | Returns |
|---|---|
| `Array.get(position)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | The array to extract from. |
| `position` | List | The coordinates of the element to get. |

## ee.Array.gt

On an element-wise basis, returns 1 if and only if the first value is greater than the second.

| Usage | Returns |
|---|---|
| `Array.gt(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.gte

On an element-wise basis, returns 1 if and only if the first value is greater than or equal to the second.

| Usage | Returns |
|---|---|
| `Array.gte(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.hypot

On an element-wise basis, calculates the magnitude of the 2D vector \[x, y\].

| Usage | Returns |
|---|---|
| `Array.hypot(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.identity

Creates a 2D identity matrix of the given size.

| Usage | Returns |
|---|---|
| `ee.Array.identity(size)` | Array |

| Argument | Type | Details |
|---|---|---|
| `size` | Integer | The length of each axis. |

## ee.Array.int

On an element-wise basis, casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Array.int()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.int16

On an element-wise basis, casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Array.int16()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.int32

On an element-wise basis, casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Array.int32()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.int64

On an element-wise basis, casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Array.int64()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.int8

On an element-wise basis, casts the input value to a signed 8-bit integer.

| Usage | Returns |
|---|---|
| `Array.int8()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.lanczos

On an element-wise basis, computes the Lanczos approximation of the input.

| Usage | Returns |
|---|---|
| `Array.lanczos()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.leftShift

On an element-wise basis, calculates the left shift of v1 by v2 bits.

| Usage | Returns |
|---|---|
| `Array.leftShift(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.length

Returns a 1-D ee.Array containing the length of each dimension of the given ee.Array.

| Usage | Returns |
|---|---|
| `Array.length()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | The array from which to extract the axis lengths. |

## ee.Array.log

On an element-wise basis, computes the natural logarithm of the input.

| Usage | Returns |
|---|---|
| `Array.log()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.log10

On an element-wise basis, computes the base-10 logarithm of the input.

| Usage | Returns |
|---|---|
| `Array.log10()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.long

On an element-wise basis, casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Array.long()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.lt

On an element-wise basis, returns 1 if and only if the first value is less than the second.

| Usage | Returns |
|---|---|
| `Array.lt(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.lte

On an element-wise basis, returns 1 if and only if the first value is less than or equal to the second.

| Usage | Returns |
|---|---|
| `Array.lte(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.mask

Creates a subarray by slicing out each position in an input array that is parallel to a non-zero element of the given mask array.

| Usage | Returns |
|---|---|
| `Array.mask(mask)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | Array to mask. |
| `mask` | Array | Mask array. |

## ee.Array.matrixCholeskyDecomposition

Calculates the Cholesky decomposition of a matrix. The Cholesky decomposition is a decomposition into the form L \* L' where L is a lower triangular matrix. The input must be a symmetric positive-definite matrix. Returns a dictionary with 1 entry named 'L'.

| Usage | Returns |
|---|---|
| `Array.matrixCholeskyDecomposition()` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | The array to decompose. |

## ee.Array.matrixDeterminant

Computes the determinant of the matrix.

| Usage | Returns |
|---|---|
| `Array.matrixDeterminant()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The array to compute on. |

## ee.Array.matrixDiagonal

Computes the diagonal of the matrix in a single column.

| Usage | Returns |
|---|---|
| `Array.matrixDiagonal()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.matrixFnorm

Computes the Frobenius norm of the matrix.

| Usage | Returns |
|---|---|
| `Array.matrixFnorm()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The array to compute on. |

## ee.Array.matrixInverse

Computes the inverse of the matrix.

| Usage | Returns |
|---|---|
| `Array.matrixInverse()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.matrixLUDecomposition

Calculates the LU matrix decomposition such that P×input=L×U, where L is lower triangular (with unit diagonal terms), U is upper triangular and P is a partial pivot permutation matrix. The input matrix must be square. Returns a dictionary with entries named 'L', 'U' and 'P'.

| Usage | Returns |
|---|---|
| `Array.matrixLUDecomposition()` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | The array to decompose. |

## ee.Array.matrixMultiply

Returns the matrix multiplication A \* B.

| Usage | Returns |
|---|---|
| `Array.matrixMultiply(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.matrixPseudoInverse

Computes the Moore-Penrose pseudoinverse of the matrix.

| Usage | Returns |
|---|---|
| `Array.matrixPseudoInverse()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.matrixQRDecomposition

Calculates the QR-decomposition of a matrix into two matrices Q and R such that input = QR, where Q is orthogonal, and R is upper triangular. Returns a dictionary with entries named 'Q' and 'R'.

| Usage | Returns |
|---|---|
| `Array.matrixQRDecomposition()` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | The array to decompose. |

## ee.Array.matrixSingularValueDecomposition

Calculates the Singular Value Decomposition of the input matrix into U×S×V', such that U and V are orthogonal and S is diagonal. Returns a dictionary with entries named 'U', 'S' and 'V'.

| Usage | Returns |
|---|---|
| `Array.matrixSingularValueDecomposition()` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | The array to decompose. |

## ee.Array.matrixSolve

Solves for x in the matrix equation A \* x = B, finding a least-squares solution if A is overdetermined.

| Usage | Returns |
|---|---|
| `Array.matrixSolve(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.matrixToDiag

Computes a square diagonal matrix from a single column matrix.

| Usage | Returns |
|---|---|
| `Array.matrixToDiag()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.matrixTrace

Computes the trace of the matrix.

| Usage | Returns |
|---|---|
| `Array.matrixTrace()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The array to compute on. |

## ee.Array.matrixTranspose

Transposes two dimensions of an array.

| Usage | Returns |
|---|---|
| `Array.matrixTranspose(*axis1*, *axis2*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to transpose. |
| `axis1` | Integer, default: 0 | First axis to swap. |
| `axis2` | Integer, default: 1 | Second axis to swap. |

## ee.Array.max

On an element-wise basis, selects the maximum of the first and second values.

| Usage | Returns |
|---|---|
| `Array.max(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.min

On an element-wise basis, selects the minimum of the first and second values.

| Usage | Returns |
|---|---|
| `Array.min(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.mod

On an element-wise basis, calculates the remainder of the first value divided by the second.

| Usage | Returns |
|---|---|
| `Array.mod(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.multiply

On an element-wise basis, multiplies the first value by the second.

| Usage | Returns |
|---|---|
| `Array.multiply(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.neq

On an element-wise basis, returns 1 if and only if the first value is not equal to the second.

| Usage | Returns |
|---|---|
| `Array.neq(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.not

On an element-wise basis, returns 0 if the input is non-zero, and 1 otherwise.

| Usage | Returns |
|---|---|
| `Array.not()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.or

On an element-wise basis, returns 1 if and only if either input value is non-zero.

| Usage | Returns |
|---|---|
| `Array.or(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.pad

Pad an array to a given length. The pad value will be repeatedly appended to the array to extend it to given length along each axis. If the array is already as large or larger than a given length, it will remain unchanged along that axis.

| Usage | Returns |
|---|---|
| `Array.pad(lengths, *pad*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to pad. |
| `lengths` | List | A list of new lengths for each axis. |
| `pad` | Number, default: 0 | The value with which to pad the array. |

## ee.Array.pow

On an element-wise basis, raises the first value to the power of the second.

| Usage | Returns |
|---|---|
| `Array.pow(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.project

Projects an array to a lower dimensional space by specifying the axes to retain. Dropped axes must be at most length 1.

| Usage | Returns |
|---|---|
| `Array.project(axes)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to project. |
| `axes` | List | The axes to project onto. Other axes will be discarded, and must be at most length 1. |

## ee.Array.reduce

Apply a reducer to an array by collapsing all the input values along each specified axis into a single output value computed by the reducer.

The output always has the same dimensionality as the input, and the individual axes are affected as follows:

<br />

- The axes specified in the 'axes' parameter have their length reduced to 1 (by applying the reducer).
- If the reducer has multiple inputs or multiple outputs, the axis specified in 'fieldAxis' will be used to provide the reducer's inputs and store the reducer's outputs.
- All other axes are unaffected (independent reductions are performed).

<br />

| Usage | Returns |
|---|---|
| `Array.reduce(reducer, axes, *fieldAxis*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | The array. |
| `reducer` | Reducer | The reducer to apply. Each of its outputs must be a number, not an array or other type. |
| `axes` | List | The list of axes over which to reduce. The output will have a length of 1 in all these axes. |
| `fieldAxis` | Integer, default: null | The axis to use as the reducer's input and output fields. Only required if the reducer has multiple inputs or multiple outputs, in which case the axis must have length equal to the number of reducer inputs, and in the result it will have length equal to the number of reducer outputs. |

## ee.Array.repeat

Repeats the array along the given axis. The result will have the shape of the input, except length along the repeated axis will be multiplied by the given number of copies.

| Usage | Returns |
|---|---|
| `Array.repeat(*axis*, *copies*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to repeat. |
| `axis` | Integer, default: 0 | The axis along which to repeat the array. |
| `copies` | Integer, default: 2 | The number of copies of this array to concatenate along the given axis. |

## ee.Array.reshape

Reshapes an array to a new list of dimension lengths.

| Usage | Returns |
|---|---|
| `Array.reshape(shape)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to reshape. |
| `shape` | Array | New shape to which arrays are converted. If one component of the shape is the special value -1, the size of that dimension is computed so that the total size remains constant. In particular, a shape of \[-1\] flattens into 1-D. At most one component of shape can be -1. |

## ee.Array.rightShift

On an element-wise basis, calculates the signed right shift of v1 by v2 bits.

| Usage | Returns |
|---|---|
| `Array.rightShift(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.round

On an element-wise basis, computes the integer nearest to the input.

| Usage | Returns |
|---|---|
| `Array.round()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.short

On an element-wise basis, casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Array.short()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.signum

On an element-wise basis, computes the signum function (sign) of the input; 0 if the input is 0, 1 if the input is greater than 0, -1 if the input is less than 0.

| Usage | Returns |
|---|---|
| `Array.signum()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.sin

On an element-wise basis, computes the sine of the input in radians.

| Usage | Returns |
|---|---|
| `Array.sin()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.sinh

On an element-wise basis, computes the hyperbolic sine of the input.

| Usage | Returns |
|---|---|
| `Array.sinh()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.slice

Creates a subarray by slicing out each position along the given axis from the 'start' (inclusive) to 'end' (exclusive) by increments of 'step'. The result will have as many dimensions as the input, and the same length in all directions except the slicing axis, where the length will be the number of positions from 'start' to 'end' by 'step' that are in range of the input array's length along 'axis'. This means the result can be length 0 along the given axis if start=end, or if the start or end values are entirely out of range.

| Usage | Returns |
|---|---|
| `Array.slice(*axis*, *start*, *end*, *step*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to slice. |
| `axis` | Integer, default: 0 | The axis to slice on. |
| `start` | Integer, default: 0 | The coordinate of the first slice (inclusive) along 'axis'. Negative numbers are used to position the start of slicing relative to the end of the array, where -1 starts at the last position on the axis, -2 starts at the next to last position, etc. |
| `end` | Integer, default: null | The coordinate (exclusive) at which to stop taking slices. By default this will be the length of the given axis. Negative numbers are used to position the end of slicing relative to the end of the array, where -1 will exclude the last position, -2 will exclude the last two positions, etc. |
| `step` | Integer, default: 1 | The separation between slices along 'axis'; a slice will be taken at each whole multiple of 'step' from 'start' (inclusive) to 'end' (exclusive). Must be positive. |

## ee.Array.sort

Sorts elements of the array along one axis.

| Usage | Returns |
|---|---|
| `Array.sort(*keys*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array image to sort. |
| `keys` | Array, default: null | Optional keys to sort by. If not provided, the values are used as the keys. The keys can only have multiple elements along one axis, which determines the direction to sort in. |

## ee.Array.sqrt

On an element-wise basis, computes the square root of the input.

| Usage | Returns |
|---|---|
| `Array.sqrt()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.subtract

On an element-wise basis, subtracts the second value from the first.

| Usage | Returns |
|---|---|
| `Array.subtract(right)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Array | The left-hand value. |
| `right` | Array | The right-hand value. |

## ee.Array.tan

On an element-wise basis, computes the tangent of the input in radians.

| Usage | Returns |
|---|---|
| `Array.tan()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.tanh

On an element-wise basis, computes the hyperbolic tangent of the input.

| Usage | Returns |
|---|---|
| `Array.tanh()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toByte

On an element-wise basis, casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Array.toByte()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toDouble

On an element-wise basis, casts the input value to a 64-bit float.

| Usage | Returns |
|---|---|
| `Array.toDouble()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toFloat

On an element-wise basis, casts the input value to a 32-bit float.

| Usage | Returns |
|---|---|
| `Array.toFloat()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toInt

On an element-wise basis, casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Array.toInt()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toInt16

On an element-wise basis, casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Array.toInt16()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toInt32

On an element-wise basis, casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Array.toInt32()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toInt64

On an element-wise basis, casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Array.toInt64()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toInt8

On an element-wise basis, casts the input value to a signed 8-bit integer.

| Usage | Returns |
|---|---|
| `Array.toInt8()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toList

Turns an Array into a list of lists of numbers.

| Usage | Returns |
|---|---|
| `Array.toList()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to convert. |

## ee.Array.toLong

On an element-wise basis, casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Array.toLong()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toShort

On an element-wise basis, casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Array.toShort()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toUint16

On an element-wise basis, casts the input value to an unsigned 16-bit integer.

| Usage | Returns |
|---|---|
| `Array.toUint16()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toUint32

On an element-wise basis, casts the input value to an unsigned 32-bit integer.

| Usage | Returns |
|---|---|
| `Array.toUint32()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.toUint8

On an element-wise basis, casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Array.toUint8()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.transpose

Transposes two dimensions of an array.

| Usage | Returns |
|---|---|
| `Array.transpose(*axis1*, *axis2*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `array` | Array | Array to transpose. |
| `axis1` | Integer, default: 0 | First axis to swap. |
| `axis2` | Integer, default: 1 | Second axis to swap. |

## ee.Array.trigamma

On an element-wise basis, computes the trigamma function of the input.

| Usage | Returns |
|---|---|
| `Array.trigamma()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.uint16

On an element-wise basis, casts the input value to an unsigned 16-bit integer.

| Usage | Returns |
|---|---|
| `Array.uint16()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.uint32

On an element-wise basis, casts the input value to an unsigned 32-bit integer.

| Usage | Returns |
|---|---|
| `Array.uint32()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Array.uint8

On an element-wise basis, casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Array.uint8()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Array | The input array. |

## ee.Blob

Loads a Blob from a Google Cloud Storage URL.

| Usage | Returns |
|---|---|
| `ee.Blob(url)` | Blob |

| Argument | Type | Details |
|---|---|---|
| `url` | String | The Blob's Google Cloud Storage URL. The bucket metadata must be accessible (requires the \`storage.buckets.get\` permission which is provided by the role "Storage Legacy Bucket Reader" among others, see https://cloud.google.com/storage/docs/access-control/iam-roles) and the bucket must be located in the US multi-region, a dual-region including US-CENTRAL1, or the US-CENTRAL1 region. |

## ee.Blob.string

Returns the contents of the blob as a String.

| Usage | Returns |
|---|---|
| `Blob.string(*encoding*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `blob` | Blob |   |
| `encoding` | String, default: null | The character set encoding to use when decoding the blob. Options include, but are not limited to: <br /> - \`US-ASCII\` - \`UTF-8\` - \`UTF-16\` |

## ee.Blob.url

Returns the Blob's Google Cloud Storage URL. The bucket metadata must be accessible (requires the `storage.buckets.get` permission which is provided by the role "Storage Legacy Bucket Reader" among others, see https://cloud.google.com/storage/docs/access-control/iam-roles) and the bucket must be located in the US multi-region, a dual-region including US-CENTRAL1, or the US-CENTRAL1 region.

| Usage | Returns |
|---|---|
| `Blob.url()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `blob` | Blob |   |

## ee.Date

Constructs a new Date object.

| Usage | Returns |
|---|---|
| `ee.Date(date, *tz*)` | Date |

| Argument | Type | Details |
|---|---|---|
| `date` | ComputedObject\|Date\|Number\|String | The date to convert, one of: a number (number of milliseconds since the epoch), an ISO Date string, a JavaScript Date or a ComputedObject. |
| `tz` | String, optional | An optional timezone only to be used with a string date. |

## ee.Date.advance

Create a new Date by adding the specified units to the given Date.

| Usage | Returns |
|---|---|
| `Date.advance(delta, unit, *timeZone*)` | Date |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |
| `delta` | Float |   |
| `unit` | String | One of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'. |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Date.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Date.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Date.difference

Returns the difference between two Dates in the specified units; the result is floating-point and based on the average length of the unit.

| Usage | Returns |
|---|---|
| `Date.difference(start, unit)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |
| `start` | Date |   |
| `unit` | String | One of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'. |

## ee.Date.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Date.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Date.format

Convert a date to string.

| Usage | Returns |
|---|---|
| `Date.format(*format*, *timeZone*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |
| `format` | String, default: null | A pattern, as described at http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html; if omitted will use ISO standard date formatting. |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Date.fromYMD

Returns a Date given year, month, day.

| Usage | Returns |
|---|---|
| `ee.Date.fromYMD(year, month, day, *timeZone*)` | Date |

| Argument | Type | Details |
|---|---|---|
| `year` | Integer | The year, 2013, for example. |
| `month` | Integer | The month, 3, for example. |
| `day` | Integer | The day, 15, for example. |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Date.get

Returns the specified unit of this date.

| Usage | Returns |
|---|---|
| `Date.get(unit, *timeZone*)` | Long |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |
| `unit` | String | One of 'year', 'month' (returns 1-12), 'week' (1-53), 'day' (1-31), 'hour' (0-23), 'minute' (0-59), or 'second' (0-59). |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Date.getFraction

Returns this date's elapsed fraction of the specified unit (between 0 and 1).

| Usage | Returns |
|---|---|
| `Date.getFraction(unit, *timeZone*)` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |
| `unit` | String | One of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'. |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Date.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `Date.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Date.getRange

Returns a DateRange covering the unit of the specified type that contains this date, e.g., Date('2013-3-15').getRange('year') returns DateRange('2013-1-1', '2014-1-1').

| Usage | Returns |
|---|---|
| `Date.getRange(unit, *timeZone*)` | DateRange |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |
| `unit` | String | One of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'. |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Date.getRelative

Returns the specified (0-based) unit of this date relative to a larger unit, e.g., getRelative('day', 'year') returns a value between 0 and 365.

| Usage | Returns |
|---|---|
| `Date.getRelative(unit, inUnit, *timeZone*)` | Long |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |
| `unit` | String | One of 'month', 'week', 'day', 'hour', 'minute', or 'second'. |
| `inUnit` | String | One of 'year', 'month', 'week', 'day', 'hour', or 'minute'. |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Date.millis

The number of milliseconds since 1970-01-01T00:00:00Z.

| Usage | Returns |
|---|---|
| `Date.millis()` | Long |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |

## ee.Date.parse

Parse a date string, given a string describing its format.

| Usage | Returns |
|---|---|
| `ee.Date.parse(format, date, *timeZone*)` | Date |

| Argument | Type | Details |
|---|---|---|
| `format` | String | A pattern, as described at http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html. |
| `date` | String | A string matching the given pattern. |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.Date.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Date.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Date.unitRatio

Returns the ratio of the length of one unit to the length of another, e.g., unitRatio('day', 'minute') returns 1440. Valid units are 'year', 'month', 'week', 'day', 'hour', 'minute', and 'second'.

| Usage | Returns |
|---|---|
| `ee.Date.unitRatio(numerator, denominator)` | Float |

| Argument | Type | Details |
|---|---|---|
| `numerator` | String |   |
| `denominator` | String |   |

## ee.Date.update

Create a new Date by setting one or more of the units of the given Date to a new value. If a timeZone is given the new value(s) is interpreted in that zone.

| Usage | Returns |
|---|---|
| `Date.update(*year*, *month*, *day*, *hour*, *minute*, *second*, *timeZone*)` | Date |

| Argument | Type | Details |
|---|---|---|
| this: `date` | Date |   |
| `year` | Integer, default: null |   |
| `month` | Integer, default: null |   |
| `day` | Integer, default: null |   |
| `hour` | Integer, default: null |   |
| `minute` | Integer, default: null |   |
| `second` | Number, default: null |   |
| `timeZone` | String, default: null | The time zone (e.g., 'America/Los_Angeles'); defaults to UTC. |

## ee.DateRange

Creates a DateRange with the given start (inclusive) and end (exclusive), which may be Dates, numbers (interpreted as milliseconds since 1970-01-01T00:00:00Z), or strings (such as '1996-01-01T08:00'). If 'end' is not specified, a 1-millisecond range starting at 'start' is created.

| Usage | Returns |
|---|---|
| `ee.DateRange(start, *end*, *timeZone*)` | DateRange |

| Argument | Type | Details |
|---|---|---|
| `start` | Object |   |
| `end` | Object, default: null |   |
| `timeZone` | String, default: null | If start and/or end are provided as strings, the time zone in which to interpret them; defaults to UTC. |

## ee.DateRange.contains

Returns true if the given Date or DateRange is within this DateRange.

| Usage | Returns |
|---|---|
| `DateRange.contains(other)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `dateRange` | DateRange |   |
| `other` | Object |   |

## ee.DateRange.end

Returns the (exclusive) end of this DateRange.

| Usage | Returns |
|---|---|
| `DateRange.end()` | Date |

| Argument | Type | Details |
|---|---|---|
| this: `dateRange` | DateRange |   |

## ee.DateRange.intersection

Returns a DateRange that contains all points in the intersection of this DateRange and another.

| Usage | Returns |
|---|---|
| `DateRange.intersection(other)` | DateRange |

| Argument | Type | Details |
|---|---|---|
| this: `dateRange` | DateRange |   |
| `other` | DateRange |   |

## ee.DateRange.intersects

Returns true if the given DateRange has at least one point in common with this DateRange.

| Usage | Returns |
|---|---|
| `DateRange.intersects(other)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `dateRange` | DateRange |   |
| `other` | DateRange |   |

## ee.DateRange.isEmpty

Returns true if this DateRange contains no dates (i.e. start \>= end).

| Usage | Returns |
|---|---|
| `DateRange.isEmpty()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `dateRange` | DateRange |   |

## ee.DateRange.isUnbounded

Returns true if this DateRange contains all dates.

| Usage | Returns |
|---|---|
| `DateRange.isUnbounded()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `dateRange` | DateRange |   |

## ee.DateRange.start

Returns the (inclusive) start of this DateRange.

| Usage | Returns |
|---|---|
| `DateRange.start()` | Date |

| Argument | Type | Details |
|---|---|---|
| this: `dateRange` | DateRange |   |

## ee.DateRange.unbounded

Returns a DateRange that includes all possible dates.

| Usage | Returns |
|---|---|
| `ee.DateRange.unbounded()` | DateRange |

**No arguments.**

## ee.DateRange.union

Returns a DateRange that contains all points in the union of this DateRange and another.

| Usage | Returns |
|---|---|
| `DateRange.union(other)` | DateRange |

| Argument | Type | Details |
|---|---|---|
| this: `dateRange` | DateRange |   |
| `other` | DateRange |   |

## ee.Dictionary

Constructs a new Dictionary.

| Usage | Returns |
|---|---|
| `ee.Dictionary(*dict*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| `dict` | ComputedObject\|Object, optional | An object to convert to a dictionary. This constructor accepts the following types: 1) Another dictionary. 2) A list of key/value pairs. 3) A null or no argument (producing an empty dictionary) |

## ee.Dictionary.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Dictionary.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Dictionary.combine

Combines two dictionaries. In the case of duplicate names, the output will contain the value of the second dictionary unless overwrite is false. Null values in both dictionaries are ignored / removed.

| Usage | Returns |
|---|---|
| `Dictionary.combine(second, *overwrite*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `first` | Dictionary |   |
| `second` | Dictionary |   |
| `overwrite` | Boolean, default: true |   |

## ee.Dictionary.contains

Returns true if the dictionary contains the given key.

| Usage | Returns |
|---|---|
| `Dictionary.contains(key)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `key` | String |   |

## ee.Dictionary.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Dictionary.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Dictionary.fromLists

Construct a dictionary from two parallel lists of keys and values.

| Usage | Returns |
|---|---|
| `ee.Dictionary.fromLists(keys, values)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| `keys` | List | A list of keys. |
| `values` | List | A list of values. |

## ee.Dictionary.get

Extracts a named value from a dictionary. If the dictionary does not contain the given key, then defaultValue is returned, unless it is null.

| Usage | Returns |
|---|---|
| `Dictionary.get(key, *defaultValue*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `key` | String |   |
| `defaultValue` | Object, default: null |   |

## ee.Dictionary.getArray

Extracts a named array value from a dictionary.

| Usage | Returns |
|---|---|
| `Dictionary.getArray(key)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `key` | String |   |

## ee.Dictionary.getGeometry

Extracts a named geometry value from a dictionary.

| Usage | Returns |
|---|---|
| `Dictionary.getGeometry(key)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `key` | String |   |

## ee.Dictionary.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `Dictionary.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Dictionary.getNumber

Extracts a named number value from a dictionary.

| Usage | Returns |
|---|---|
| `Dictionary.getNumber(key)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `key` | String |   |

## ee.Dictionary.getString

Extracts a named string value from a dictionary.

| Usage | Returns |
|---|---|
| `Dictionary.getString(key)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `key` | String |   |

## ee.Dictionary.keys

Retrieve the keys of a dictionary as a list. The keys will be sorted in natural order.

| Usage | Returns |
|---|---|
| `Dictionary.keys()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |

## ee.Dictionary.map

Map an algorithm over a dictionary. The algorithm is expected to take 2 arguments, a key from the existing dictionary and the value it corresponds to, and return a new value for the given key. If the algorithm returns null, the key is dropped.

| Usage | Returns |
|---|---|
| `Dictionary.map(baseAlgorithm)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `baseAlgorithm` | Algorithm |   |

## ee.Dictionary.remove

Returns a dictionary with the specified keys removed.

| Usage | Returns |
|---|---|
| `Dictionary.remove(selectors, *ignoreMissing*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `selectors` | List | A list of keys names or regular expressions of key names to remove. |
| `ignoreMissing` | Boolean, default: false | Ignore selectors that don't match at least 1 key. |

## ee.Dictionary.rename

Rename elements in a dictionary.

| Usage | Returns |
|---|---|
| `Dictionary.rename(from, to, *overwrite*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `from` | List | A list of keys to be renamed. |
| `to` | List | A list of the new names for the keys listed in the 'from' parameter. Must have the same length as the 'from' list. |
| `overwrite` | Boolean, default: false | Allow overwriting existing properties with the same name. |

## ee.Dictionary.select

Returns a dictionary with only the specified keys.

| Usage | Returns |
|---|---|
| `Dictionary.select(selectors, *ignoreMissing*)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `selectors` | List | A list of keys or regular expressions to select. |
| `ignoreMissing` | Boolean, default: false | Ignore selectors that don't match at least 1 key. |

## ee.Dictionary.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Dictionary.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Dictionary.set

Set a value in a dictionary.

| Usage | Returns |
|---|---|
| `Dictionary.set(key, value)` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `key` | String |   |
| `value` | Object |   |

## ee.Dictionary.size

Returns the number of entries in a dictionary.

| Usage | Returns |
|---|---|
| `Dictionary.size()` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |

## ee.Dictionary.toArray

Returns numeric values of a dictionary as an array. If no keys are specified, all values are returned in the natural ordering of the dictionary's keys. The default 'axis' is 0.

| Usage | Returns |
|---|---|
| `Dictionary.toArray(*keys*, *axis*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `keys` | List, default: null |   |
| `axis` | Integer, default: 0 |   |

## ee.Dictionary.toImage

Creates an image of constants from values in a dictionary. The bands of the image are ordered and named according to the names argument. If no names are specified, the bands are sorted alpha-numerically.

| Usage | Returns |
|---|---|
| `Dictionary.toImage(*names*)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary | The dictionary to convert. |
| `names` | List, default: null | The order of the output bands. |

## ee.Dictionary.values

Returns the values of a dictionary as a list. If no keys are specified, all values are returned in the natural ordering of the dictionary's keys.

| Usage | Returns |
|---|---|
| `Dictionary.values(*keys*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `dictionary` | Dictionary |   |
| `keys` | List, default: null |   |

## ee.List

Constructs a new list.

| Usage | Returns |
|---|---|
| `ee.List(list)` | List |

| Argument | Type | Details |
|---|---|---|
| `list` | List\[Object\]\|Object | A list or a computed object. |

## ee.List.add

Appends the element to the end of list.

| Usage | Returns |
|---|---|
| `List.add(element)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `element` | Object |   |

## ee.List.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `List.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.List.cat

Concatenates the contents of other onto list.

| Usage | Returns |
|---|---|
| `List.cat(other)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `other` | List |   |

## ee.List.contains

Returns true if list contains element.

| Usage | Returns |
|---|---|
| `List.contains(element)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `element` | Object |   |

## ee.List.containsAll

Returns true if list contains all of the elements of other, regardless of order.

| Usage | Returns |
|---|---|
| `List.containsAll(other)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `other` | List |   |

## ee.List.distinct

Returns a copy of list without duplicate elements.

| Usage | Returns |
|---|---|
| `List.distinct()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |

## ee.List.equals

Returns true if list contains the same elements as other, in the same order.

| Usage | Returns |
|---|---|
| `List.equals(other)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `other` | List |   |

## ee.List.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `List.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.List.filter

Filters a list to only the elements that match the given filter. To filter list items that aren't images or features, test a property named 'item', e.g., ee.Filter.gt('item', 3).

| Usage | Returns |
|---|---|
| `List.filter(filter)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `filter` | Filter |   |

## ee.List.flatten

Flattens any sublists into a single list.

| Usage | Returns |
|---|---|
| `List.flatten()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |

## ee.List.frequency

Returns the number of elements in list equal to element.

| Usage | Returns |
|---|---|
| `List.frequency(element)` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `element` | Object |   |

## ee.List.get

Returns the element at the specified position in list. A negative index counts backwards from the end of the list.

| Usage | Returns |
|---|---|
| `List.get(index)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `index` | Integer |   |

## ee.List.getArray

Returns the array at the specified position in list. A negative index counts backwards from the end of the list. If the value is not a array, an error will occur.

| Usage | Returns |
|---|---|
| `List.getArray(index)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `index` | Integer |   |

## ee.List.getGeometry

Returns the geometry at the specified position in list. A negative index counts backwards from the end of the list. If the value is not a geometry, an error will occur.

| Usage | Returns |
|---|---|
| `List.getGeometry(index)` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `index` | Integer |   |

## ee.List.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `List.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.List.getNumber

Returns the number at the specified position in list. A negative index counts backwards from the end of the list. If the value is not a number, an error will occur.

| Usage | Returns |
|---|---|
| `List.getNumber(index)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `index` | Integer |   |

## ee.List.getString

Returns the string at the specified position in list. A negative index counts backwards from the end of the list. If the value is not a string, an error will occur.

| Usage | Returns |
|---|---|
| `List.getString(index)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `index` | Integer |   |

## ee.List.indexOf

Returns the position of the first occurrence of element in list, or -1 if list does not contain element.

| Usage | Returns |
|---|---|
| `List.indexOf(element)` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `element` | Object |   |

## ee.List.indexOfSublist

Returns the starting position of the first occurrence of target within list, or -1 if there is no such occurrence.

| Usage | Returns |
|---|---|
| `List.indexOfSublist(target)` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `target` | List |   |

## ee.List.insert

Inserts element at the specified position in list. A negative index counts backwards from the end of the list.

| Usage | Returns |
|---|---|
| `List.insert(index, element)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `index` | Integer |   |
| `element` | Object |   |

## ee.List.iterate

Iterate an algorithm over a list. The algorithm is expected to take two objects, the current list item, and the result from the previous iteration or the value of first for the first iteration.

| Usage | Returns |
|---|---|
| `List.iterate(function, first)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `function` | Algorithm |   |
| `first` | Object |   |

## ee.List.join

Returns a string containing the elements of the list joined together with the specified separator between elements.

Note: The string form of list elements which are not strings, numbers, or booleans is currently not well-defined and subject to change.

| Usage | Returns |
|---|---|
| `List.join(*separator*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `separator` | String, default: "" |   |

## ee.List.lastIndexOfSubList

Returns the starting position of the last occurrence of target within list, or -1 if there is no such occurrence.

| Usage | Returns |
|---|---|
| `List.lastIndexOfSubList(target)` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `target` | List |   |

## ee.List.length

Returns the number of elements in list.

| Usage | Returns |
|---|---|
| `List.length()` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |

## ee.List.map

Map an algorithm over a list. The algorithm is expected to take an Object and return an Object.

| Usage | Returns |
|---|---|
| `List.map(baseAlgorithm, *dropNulls*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `baseAlgorithm` | Algorithm |   |
| `dropNulls` | Boolean, default: false | If true, the mapped algorithm is allowed to return nulls, and the elements for which it returns nulls will be dropped. |

## ee.List.reduce

Apply a reducer to a list. If the reducer takes more than 1 input, then each element in the list is assumed to be a list of inputs. If the reducer returns a single output, it is returned directly, otherwise returns a dictionary containing the named reducer outputs.

| Usage | Returns |
|---|---|
| `List.reduce(reducer)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `reducer` | Reducer |   |

## ee.List.remove

Removes the first occurrence of the specified element from list, if it is present.

| Usage | Returns |
|---|---|
| `List.remove(element)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `element` | Object |   |

## ee.List.removeAll

Removes from list all of the elements that are contained in other list.

| Usage | Returns |
|---|---|
| `List.removeAll(other)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `other` | List |   |

## ee.List.repeat

Returns a new list containing value repeated count times.

| Usage | Returns |
|---|---|
| `ee.List.repeat(value, count)` | List |

| Argument | Type | Details |
|---|---|---|
| `value` | Object | The value to repeat. |
| `count` | Integer | The number of times to repeat. |

## ee.List.replace

Replaces the first occurrence of oldval in list with newval.

| Usage | Returns |
|---|---|
| `List.replace(oldval, newval)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `oldval` | Object |   |
| `newval` | Object |   |

## ee.List.replaceAll

Replaces all occurrences of oldval in list with newval.

| Usage | Returns |
|---|---|
| `List.replaceAll(oldval, newval)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `oldval` | Object |   |
| `newval` | Object |   |

## ee.List.reverse

Reverses the order of the elements in list.

| Usage | Returns |
|---|---|
| `List.reverse()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |

## ee.List.rotate

Rotates the elements of the list by the specified distance.

| Usage | Returns |
|---|---|
| `List.rotate(distance)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `distance` | Integer |   |

## ee.List.sequence

Generate a sequence of numbers from start to end (inclusive) in increments of step, or in count equally-spaced increments. If end is not specified it is computed from start + step \* count, so at least one of end or count must be specified.

| Usage | Returns |
|---|---|
| `ee.List.sequence(start, *end*, *step*, *count*)` | List |

| Argument | Type | Details |
|---|---|---|
| `start` | Number | The starting number. |
| `end` | Number, default: null | The ending number. |
| `step` | Number, default: 1 | The increment. |
| `count` | Integer, default: null | The number of increments. |

## ee.List.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `List.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.List.set

Replaces the value at the specified position in list with element. A negative index counts backwards from the end of the list.

| Usage | Returns |
|---|---|
| `List.set(index, element)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `index` | Integer |   |
| `element` | Object |   |

## ee.List.shuffle

Randomly permute the specified list. Note that the permutation order will always be the same for any given seed, unless the value for seed is 'false'.

| Usage | Returns |
|---|---|
| `List.shuffle(*seed*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `seed` | Object, default: null | A long integer to use as a seed for the randomization. If the boolean value of 'false' is passed, then a completely random and unreproducible order will be generated. |

## ee.List.size

Returns the number of elements in list.

| Usage | Returns |
|---|---|
| `List.size()` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |

## ee.List.slice

Returns a portion of list between the start index, inclusive, and end index, exclusive. Negative values for start or end count backwards from the end of the list. Values greater than the size of the list are legal but are truncated to the size of list.

| Usage | Returns |
|---|---|
| `List.slice(start, *end*, *step*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `start` | Integer |   |
| `end` | Integer, default: null |   |
| `step` | Integer, default: null |   |

## ee.List.sort

Sorts the list into ascending order. If the 'keys' argument is provided, then it is sorted first, and the elements of 'list' are placed in the same order.

| Usage | Returns |
|---|---|
| `List.sort(*keys*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List | The list to sort. |
| `keys` | List, default: null | Optional keys to sort by. If 'keys' is provided, it must have the same length as 'list'. |

## ee.List.splice

Starting at the start index, removes count elements from list and insert the contents of other at that location. If start is negative, it counts backwards from the end of the list.

| Usage | Returns |
|---|---|
| `List.splice(start, count, *other*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `start` | Integer |   |
| `count` | Integer |   |
| `other` | List, default: null |   |

## ee.List.swap

Swaps the elements at the specified positions. A negative position counts backwards from the end of the list.

| Usage | Returns |
|---|---|
| `List.swap(pos1, pos2)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `pos1` | Integer |   |
| `pos2` | Integer |   |

## ee.List.unzip

Transposes a list of lists, extracting the first element of each inner list into one list the second elements into another, etc., up to the length of the shortest inner list. The remaining items are discarded. The result is a list of lists.

| Usage | Returns |
|---|---|
| `List.unzip()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |

## ee.List.zip

Pairs the elements of two lists to create a list of two-element lists. When the input lists are of different sizes, the final list has the same size as the shortest one.

| Usage | Returns |
|---|---|
| `List.zip(other)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `list` | List |   |
| `other` | List |   |

## ee.Number

Constructs a new Number.

| Usage | Returns |
|---|---|
| `ee.Number(number)` | Number |

| Argument | Type | Details |
|---|---|---|
| `number` | Number\|Object | A number or a computed object. |

## ee.Number.abs

Computes the absolute value of the input.

| Usage | Returns |
|---|---|
| `Number.abs()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.acos

Computes the arccosine in radians of the input.

| Usage | Returns |
|---|---|
| `Number.acos()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.add

Adds the first value to the second.

| Usage | Returns |
|---|---|
| `Number.add(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.and

Returns 1 if and only if both values are non-zero.

| Usage | Returns |
|---|---|
| `Number.and(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `Number.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.Number.asin

Computes the arcsine in radians of the input.

| Usage | Returns |
|---|---|
| `Number.asin()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.atan

Computes the arctangent in radians of the input.

| Usage | Returns |
|---|---|
| `Number.atan()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.atan2

Calculates the angle formed by the 2D vector \[x, y\].

| Usage | Returns |
|---|---|
| `Number.atan2(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.bitCount

Calculates the number of one-bits in the 64-bit two's complement binary representation of the input.

| Usage | Returns |
|---|---|
| `Number.bitCount()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.bitwiseAnd

Calculates the bitwise AND of the input values.

| Usage | Returns |
|---|---|
| `Number.bitwiseAnd(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.bitwiseNot

Calculates the bitwise NOT of the input, in the smallest signed integer type that can hold the input.

| Usage | Returns |
|---|---|
| `Number.bitwiseNot()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.bitwiseOr

Calculates the bitwise OR of the input values.

| Usage | Returns |
|---|---|
| `Number.bitwiseOr(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.bitwiseXor

Calculates the bitwise XOR of the input values.

| Usage | Returns |
|---|---|
| `Number.bitwiseXor(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.byte

Casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Number.byte()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.cbrt

Computes the cubic root of the input.

| Usage | Returns |
|---|---|
| `Number.cbrt()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.ceil

Computes the smallest integer greater than or equal to the input.

| Usage | Returns |
|---|---|
| `Number.ceil()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.clamp

Clamps the value to lie within the range of min to max.

| Usage | Returns |
|---|---|
| `Number.clamp(min, max)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `number` | Number |   |
| `min` | Float | The minimum value to clamp to. |
| `max` | Float | The maximum value to clamp to. |

## ee.Number.cos

Computes the cosine of the input in radians.

| Usage | Returns |
|---|---|
| `Number.cos()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.cosh

Computes the hyperbolic cosine of the input.

| Usage | Returns |
|---|---|
| `Number.cosh()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.digamma

Computes the digamma function of the input.

| Usage | Returns |
|---|---|
| `Number.digamma()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.divide

Divides the first value by the second, returning 0 for division by 0.

| Usage | Returns |
|---|---|
| `Number.divide(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.double

Casts the input value to a 64-bit float.

| Usage | Returns |
|---|---|
| `Number.double()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.eq

Returns 1 if and only if the first value is equal to the second.

| Usage | Returns |
|---|---|
| `Number.eq(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.erf

Computes the error function of the input.

| Usage | Returns |
|---|---|
| `Number.erf()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.erfInv

Computes the inverse error function of the input.

| Usage | Returns |
|---|---|
| `Number.erfInv()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.erfc

Computes the complementary error function of the input.

| Usage | Returns |
|---|---|
| `Number.erfc()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.erfcInv

Computes the inverse complementary error function of the input.

| Usage | Returns |
|---|---|
| `Number.erfcInv()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `Number.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.Number.exp

Computes the Euler's number e raised to the power of the input.

| Usage | Returns |
|---|---|
| `Number.exp()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.expression

Computes a numeric expression.

| Usage | Returns |
|---|---|
| `ee.Number.expression(expression, *vars*)` | Number |

| Argument | Type | Details |
|---|---|---|
| `expression` | String | A mathematical expression string to be evaluated. In addition to the standard arithmetic, boolean and relational operators, expressions also support any function in Number, the '.' operator to extract child elements from the 'vars' dictionary, and mathematical constants Math.PI and Math.E. |
| `vars` | Dictionary, default: null | A dictionary of named values that can be used in the expression. |

## ee.Number.first

Selects the value of the first value.

| Usage | Returns |
|---|---|
| `Number.first(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.firstNonZero

Selects the first value if it is non-zero, and the second value otherwise.

| Usage | Returns |
|---|---|
| `Number.firstNonZero(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.float

Casts the input value to a 32-bit float.

| Usage | Returns |
|---|---|
| `Number.float()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.floor

Computes the largest integer less than or equal to the input.

| Usage | Returns |
|---|---|
| `Number.floor()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.format

Convert a number to a string using printf-style formatting.

| Usage | Returns |
|---|---|
| `Number.format(*pattern*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `number` | Number | The number to convert to a string. |
| `pattern` | String, default: "%s" | A printf-style format string. For example, '%.2f' produces numbers formatted like '3.14', and '%05d' produces numbers formatted like '00042'. The format string must satisfy the following criteria: 1. Zero or more prefix characters. 2. Exactly one '%'. 3. Zero or more modifier characters in the set \[#-+ 0,(.\\d\]. 4. Exactly one conversion character in the set \[sdoxXeEfgGaA\]. 5. Zero or more suffix characters. For more about format strings, see https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Formatter.html |

## ee.Number.gamma

Computes the gamma function of the input.

| Usage | Returns |
|---|---|
| `Number.gamma()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.gammainc

Calculates the regularized lower incomplete Gamma function γ(x,a).

| Usage | Returns |
|---|---|
| `Number.gammainc(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `Number.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.Number.gt

Returns 1 if and only if the first value is greater than the second.

| Usage | Returns |
|---|---|
| `Number.gt(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.gte

Returns 1 if and only if the first value is greater than or equal to the second.

| Usage | Returns |
|---|---|
| `Number.gte(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.hypot

Calculates the magnitude of the 2D vector \[x, y\].

| Usage | Returns |
|---|---|
| `Number.hypot(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.int

Casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Number.int()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.int16

Casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Number.int16()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.int32

Casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Number.int32()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.int64

Casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Number.int64()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.int8

Casts the input value to a signed 8-bit integer.

| Usage | Returns |
|---|---|
| `Number.int8()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.lanczos

Computes the Lanczos approximation of the input.

| Usage | Returns |
|---|---|
| `Number.lanczos()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.leftShift

Calculates the left shift of v1 by v2 bits.

| Usage | Returns |
|---|---|
| `Number.leftShift(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.log

Computes the natural logarithm of the input.

| Usage | Returns |
|---|---|
| `Number.log()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.log10

Computes the base-10 logarithm of the input.

| Usage | Returns |
|---|---|
| `Number.log10()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.long

Casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Number.long()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.lt

Returns 1 if and only if the first value is less than the second.

| Usage | Returns |
|---|---|
| `Number.lt(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.lte

Returns 1 if and only if the first value is less than or equal to the second.

| Usage | Returns |
|---|---|
| `Number.lte(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.max

Selects the maximum of the first and second values.

| Usage | Returns |
|---|---|
| `Number.max(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.min

Selects the minimum of the first and second values.

| Usage | Returns |
|---|---|
| `Number.min(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.mod

Calculates the remainder of the first value divided by the second.

| Usage | Returns |
|---|---|
| `Number.mod(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.multiply

Multiplies the first value by the second.

| Usage | Returns |
|---|---|
| `Number.multiply(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.neq

Returns 1 if and only if the first value is not equal to the second.

| Usage | Returns |
|---|---|
| `Number.neq(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.not

Returns 0 if the input is non-zero, and 1 otherwise.

| Usage | Returns |
|---|---|
| `Number.not()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.or

Returns 1 if and only if either input value is non-zero.

| Usage | Returns |
|---|---|
| `Number.or(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.parse

Convert a string to a number.

| Usage | Returns |
|---|---|
| `ee.Number.parse(input, *radix*)` | Number |

| Argument | Type | Details |
|---|---|---|
| `input` | String | The string to convert to a number. |
| `radix` | Integer, default: 10 | An integer representing the base number system from which to convert. If input is not an integer, radix must equal 10 or not be specified. |

## ee.Number.pow

Raises the first value to the power of the second.

| Usage | Returns |
|---|---|
| `Number.pow(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.rightShift

Calculates the signed right shift of v1 by v2 bits.

| Usage | Returns |
|---|---|
| `Number.rightShift(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.round

Computes the integer nearest to the input.

| Usage | Returns |
|---|---|
| `Number.round()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `Number.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.Number.short

Casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Number.short()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.signum

Computes the signum function (sign) of the input; 0 if the input is 0, 1 if the input is greater than 0, -1 if the input is less than 0.

| Usage | Returns |
|---|---|
| `Number.signum()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.sin

Computes the sine of the input in radians.

| Usage | Returns |
|---|---|
| `Number.sin()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.sinh

Computes the hyperbolic sine of the input.

| Usage | Returns |
|---|---|
| `Number.sinh()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.sqrt

Computes the square root of the input.

| Usage | Returns |
|---|---|
| `Number.sqrt()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.subtract

Subtracts the second value from the first.

| Usage | Returns |
|---|---|
| `Number.subtract(right)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `left` | Number | The left-hand value. |
| `right` | Number | The right-hand value. |

## ee.Number.tan

Computes the tangent of the input in radians.

| Usage | Returns |
|---|---|
| `Number.tan()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.tanh

Computes the hyperbolic tangent of the input.

| Usage | Returns |
|---|---|
| `Number.tanh()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toByte

Casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Number.toByte()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toDouble

Casts the input value to a 64-bit float.

| Usage | Returns |
|---|---|
| `Number.toDouble()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toFloat

Casts the input value to a 32-bit float.

| Usage | Returns |
|---|---|
| `Number.toFloat()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toInt

Casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Number.toInt()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toInt16

Casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Number.toInt16()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toInt32

Casts the input value to a signed 32-bit integer.

| Usage | Returns |
|---|---|
| `Number.toInt32()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toInt64

Casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Number.toInt64()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toInt8

Casts the input value to a signed 8-bit integer.

| Usage | Returns |
|---|---|
| `Number.toInt8()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toLong

Casts the input value to a signed 64-bit integer.

| Usage | Returns |
|---|---|
| `Number.toLong()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toShort

Casts the input value to a signed 16-bit integer.

| Usage | Returns |
|---|---|
| `Number.toShort()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toUint16

Casts the input value to an unsigned 16-bit integer.

| Usage | Returns |
|---|---|
| `Number.toUint16()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toUint32

Casts the input value to an unsigned 32-bit integer.

| Usage | Returns |
|---|---|
| `Number.toUint32()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.toUint8

Casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Number.toUint8()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.trigamma

Computes the trigamma function of the input.

| Usage | Returns |
|---|---|
| `Number.trigamma()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.uint16

Casts the input value to an unsigned 16-bit integer.

| Usage | Returns |
|---|---|
| `Number.uint16()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.uint32

Casts the input value to an unsigned 32-bit integer.

| Usage | Returns |
|---|---|
| `Number.uint32()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.uint8

Casts the input value to an unsigned 8-bit integer.

| Usage | Returns |
|---|---|
| `Number.uint8()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `input` | Number | The input value. |

## ee.Number.unitScale

Scales the input so that the range of input values \[min, max\] becomes \[0, 1\]. Values outside the range are NOT clamped. If min == max, 0 is returned.

| Usage | Returns |
|---|---|
| `Number.unitScale(min, max)` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `number` | Number |   |
| `min` | Float |   |
| `max` | Float |   |

## ee.String

Constructs a new String.

| Usage | Returns |
|---|---|
| `ee.String(string)` | String |

| Argument | Type | Details |
|---|---|---|
| `string` | Object\|String | A string or a computed object. |

## ee.String.aside

Calls a function passing this object as the first argument, and returning itself. Convenient e.g. when debugging:

var c = ee.ImageCollection('foo').aside(print)

.filterDate('2001-01-01', '2002-01-01').aside(print, 'In 2001')

.filterBounds(geom).aside(print, 'In region')

.aside(Map.addLayer, {min: 0, max: 142}, 'Filtered')

.select('a', 'b');

Returns the same object, for chaining.

| Usage | Returns |
|---|---|
| `String.aside(func, var_args)` | ComputedObject |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `func` | Function | The function to call. |
| `var_args` | VarArgs\[Object\] | Any extra arguments to pass to the function. |

## ee.String.cat

Concatenates two strings.

| Usage | Returns |
|---|---|
| `String.cat(string2)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `string1` | String | The first string. |
| `string2` | String | The second string. |

## ee.String.compareTo

Compares two strings lexicographically. Returns: the value 0 if the two strings are lexicographically equal; -1 if string1 is less than string2; and 1 if string1 is lexicographically greater than string2.

| Usage | Returns |
|---|---|
| `String.compareTo(string2)` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `string1` | String | The string to compare. |
| `string2` | String | The string to be compared. |

## ee.String.decodeJSON

Decodes a JSON string.

| Usage | Returns |
|---|---|
| `String.decodeJSON()` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `string` | String | The string to decode. |

## ee.String.encodeJSON

Encodes an object to JSON. Supports primitives, lists, and dictionaries.

| Usage | Returns |
|---|---|
| `ee.String.encodeJSON(object)` | String |

| Argument | Type | Details |
|---|---|---|
| `object` | Object | The object to encode. |

## ee.String.equals

Checks for string equality with a given object. Returns true if the target is a string and is lexicographically equal to the reference, or false otherwise.

| Usage | Returns |
|---|---|
| `String.equals(target)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `reference` | String | The string to compare for equality. |
| `target` | Object | The second object to check for equality. |

## ee.String.evaluate

Asynchronously retrieves the value of this object from the server and passes it to the provided callback function.

| Usage | Returns |
|---|---|
| `String.evaluate(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function | A function of the form function(success, failure), called when the server returns an answer. If the request succeeded, the success argument contains the evaluated result. If the request failed, the failure argument will contains an error message. |

## ee.String.getInfo

Retrieves the value of this object from the server.

If no callback function is provided, the request is made synchronously. If a callback is provided, the request is made asynchronously.

The asynchronous mode is preferred because the synchronous mode stops all other code (for example, the EE Code Editor UI) while waiting for the server. To make an asynchronous request, evaluate() is preferred over getInfo().

Returns the computed value of this object.

| Usage | Returns |
|---|---|
| `String.getInfo(*callback*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously. |

## ee.String.index

Searches a string for the first occurrence of a substring. Returns the index of the first match, or -1.

| Usage | Returns |
|---|---|
| `String.index(pattern)` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `target` | String | The string to search. |
| `pattern` | String | The string to find. |

## ee.String.length

Returns the length of a string.

| Usage | Returns |
|---|---|
| `String.length()` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `string` | String | The string from which to get the length. |

## ee.String.match

Matches a string against a regular expression. Returns a list of matching strings.

| Usage | Returns |
|---|---|
| `String.match(regex, *flags*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `input` | String | The string in which to search. |
| `regex` | String | The regular expression to match. |
| `flags` | String, default: "" | A string specifying a combination of regular expression flags, specifically one or more of: 'g' (global match) or 'i' (ignore case). |

## ee.String.replace

Returns a new string with some or all matches of a pattern replaced.

| Usage | Returns |
|---|---|
| `String.replace(regex, replacement, *flags*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `input` | String | The string in which to search. |
| `regex` | String | The regular expression to match. |
| `replacement` | String | The string that replaces the matched substring. |
| `flags` | String, default: "" | A string specifying a combination of regular expression flags, specifically one or more of: 'g' (global match) or 'i' (ignore case) |

## ee.String.rindex

Searches a string for the last occurrence of a substring. Returns the index of the first match, or -1.

| Usage | Returns |
|---|---|
| `String.rindex(pattern)` | Integer |

| Argument | Type | Details |
|---|---|---|
| this: `target` | String | The string to search. |
| `pattern` | String | The string to find. |

## ee.String.serialize

Returns the serialized representation of this object.

| Usage | Returns |
|---|---|
| `String.serialize(*legacy*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `computedobject` | ComputedObject | The ComputedObject instance. |
| `legacy` | Boolean, optional | Enables legacy format. |

## ee.String.slice

Returns a substring of the given string. If the specified range exceeds the length of the string, returns a shorter substring.

| Usage | Returns |
|---|---|
| `String.slice(start, *end*)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `string` | String | The string to subset. |
| `start` | Integer | The beginning index, inclusive. Negative numbers count backwards from the end of the string. |
| `end` | Integer, default: null | The ending index, exclusive. Defaults to the length of the string. Negative numbers count backwards from the end of the string. |

## ee.String.split

Splits a string on a regular expression, Returning a list of strings.

| Usage | Returns |
|---|---|
| `String.split(regex, *flags*)` | List |

| Argument | Type | Details |
|---|---|---|
| this: `string` | String | The string to split. |
| `regex` | String | A regular expression to split on. If regex is the empty string, then the input string is split into individual characters. |
| `flags` | String, default: "" | A string specifying the regular expression flag: 'i' (ignore case). |

## ee.String.toLowerCase

Converts all of the characters in a string to lower case.

| Usage | Returns |
|---|---|
| `String.toLowerCase()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `string` | String | The string to convert to lower case. |

## ee.String.toUpperCase

Converts all of the characters in a string to upper case.

| Usage | Returns |
|---|---|
| `String.toUpperCase()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `string` | String | The string to convert to upper case. |

## ee.String.trim

Returns a string whose value is the original string, with any leading and trailing whitespace removed.

| Usage | Returns |
|---|---|
| `String.trim()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `string` | String | The string to trim. |

