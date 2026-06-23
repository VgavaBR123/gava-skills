# Redutores — ee.Reducer (estatística zonal)

> 61 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.Reducer.allNonZero`](#ee-reducer-allnonzero)
- [`ee.Reducer.anyNonZero`](#ee-reducer-anynonzero)
- [`ee.Reducer.autoHistogram`](#ee-reducer-autohistogram)
- [`ee.Reducer.bitwiseAnd`](#ee-reducer-bitwiseand)
- [`ee.Reducer.bitwiseOr`](#ee-reducer-bitwiseor)
- [`ee.Reducer.centeredCovariance`](#ee-reducer-centeredcovariance)
- [`ee.Reducer.circularMean`](#ee-reducer-circularmean)
- [`ee.Reducer.circularStddev`](#ee-reducer-circularstddev)
- [`ee.Reducer.circularVariance`](#ee-reducer-circularvariance)
- [`ee.Reducer.combine`](#ee-reducer-combine)
- [`ee.Reducer.count`](#ee-reducer-count)
- [`ee.Reducer.countDistinct`](#ee-reducer-countdistinct)
- [`ee.Reducer.countDistinctNonNull`](#ee-reducer-countdistinctnonnull)
- [`ee.Reducer.countEvery`](#ee-reducer-countevery)
- [`ee.Reducer.countRuns`](#ee-reducer-countruns)
- [`ee.Reducer.covariance`](#ee-reducer-covariance)
- [`ee.Reducer.disaggregate`](#ee-reducer-disaggregate)
- [`ee.Reducer.first`](#ee-reducer-first)
- [`ee.Reducer.firstNonNull`](#ee-reducer-firstnonnull)
- [`ee.Reducer.fixed2DHistogram`](#ee-reducer-fixed2dhistogram)
- [`ee.Reducer.fixedHistogram`](#ee-reducer-fixedhistogram)
- [`ee.Reducer.forEach`](#ee-reducer-foreach)
- [`ee.Reducer.forEachBand`](#ee-reducer-foreachband)
- [`ee.Reducer.forEachElement`](#ee-reducer-foreachelement)
- [`ee.Reducer.frequencyHistogram`](#ee-reducer-frequencyhistogram)
- [`ee.Reducer.geometricMedian`](#ee-reducer-geometricmedian)
- [`ee.Reducer.getOutputs`](#ee-reducer-getoutputs)
- [`ee.Reducer.group`](#ee-reducer-group)
- [`ee.Reducer.histogram`](#ee-reducer-histogram)
- [`ee.Reducer.intervalMean`](#ee-reducer-intervalmean)
- [`ee.Reducer.kendallsCorrelation`](#ee-reducer-kendallscorrelation)
- [`ee.Reducer.kurtosis`](#ee-reducer-kurtosis)
- [`ee.Reducer.last`](#ee-reducer-last)
- [`ee.Reducer.lastNonNull`](#ee-reducer-lastnonnull)
- [`ee.Reducer.linearFit`](#ee-reducer-linearfit)
- [`ee.Reducer.linearRegression`](#ee-reducer-linearregression)
- [`ee.Reducer.max`](#ee-reducer-max)
- [`ee.Reducer.mean`](#ee-reducer-mean)
- [`ee.Reducer.median`](#ee-reducer-median)
- [`ee.Reducer.min`](#ee-reducer-min)
- [`ee.Reducer.minMax`](#ee-reducer-minmax)
- [`ee.Reducer.mode`](#ee-reducer-mode)
- [`ee.Reducer.pearsonsCorrelation`](#ee-reducer-pearsonscorrelation)
- [`ee.Reducer.percentile`](#ee-reducer-percentile)
- [`ee.Reducer.product`](#ee-reducer-product)
- [`ee.Reducer.repeat`](#ee-reducer-repeat)
- [`ee.Reducer.ridgeRegression`](#ee-reducer-ridgeregression)
- [`ee.Reducer.robustLinearRegression`](#ee-reducer-robustlinearregression)
- [`ee.Reducer.sampleStdDev`](#ee-reducer-samplestddev)
- [`ee.Reducer.sampleVariance`](#ee-reducer-samplevariance)
- [`ee.Reducer.sensSlope`](#ee-reducer-sensslope)
- [`ee.Reducer.setOutputs`](#ee-reducer-setoutputs)
- [`ee.Reducer.skew`](#ee-reducer-skew)
- [`ee.Reducer.spearmansCorrelation`](#ee-reducer-spearmanscorrelation)
- [`ee.Reducer.splitWeights`](#ee-reducer-splitweights)
- [`ee.Reducer.stdDev`](#ee-reducer-stddev)
- [`ee.Reducer.sum`](#ee-reducer-sum)
- [`ee.Reducer.toCollection`](#ee-reducer-tocollection)
- [`ee.Reducer.toList`](#ee-reducer-tolist)
- [`ee.Reducer.unweighted`](#ee-reducer-unweighted)
- [`ee.Reducer.variance`](#ee-reducer-variance)

---

## ee.Reducer.allNonZero

Returns a Reducer that returns 1 if all of its inputs are non-zero, 0 otherwise. Where applicable, the output name is "all".

| Usage | Returns |
|---|---|
| `ee.Reducer.allNonZero()` | Reducer |

**No arguments.**

## ee.Reducer.anyNonZero

Returns a Reducer that returns 1 if any of its inputs are non-zero, 0 otherwise. Where applicable, the output name is "any".

| Usage | Returns |
|---|---|
| `ee.Reducer.anyNonZero()` | Reducer |

**No arguments.**

## ee.Reducer.autoHistogram

Create a reducer that will compute a histogram of the inputs. The output is a Nx2 array of the lower bucket bounds and the counts (or cumulative counts) of each bucket and is suitable for use per-pixel.

| Usage | Returns |
|---|---|
| `ee.Reducer.autoHistogram(*maxBuckets*, *minBucketWidth*, *maxRaw*, *cumulative*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `maxBuckets` | Integer, default: null | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. |
| `minBucketWidth` | Float, default: null | The minimum histogram bucket width, or null to allow any power of 2. |
| `maxRaw` | Integer, default: null | The number of values to accumulate before building the initial histogram. |
| `cumulative` | Boolean, default: false |   |

## ee.Reducer.bitwiseAnd

Returns a Reducer that computes the bitwise-and summation of its inputs. Where applicable, the output name is "bitwiseAnd".

| Usage | Returns |
|---|---|
| `ee.Reducer.bitwiseAnd()` | Reducer |

**No arguments.**

## ee.Reducer.bitwiseOr

Returns a Reducer that computes the bitwise-or summation of its inputs. Where applicable, the output name is "bitwiseOr".

| Usage | Returns |
|---|---|
| `ee.Reducer.bitwiseOr()` | Reducer |

**No arguments.**

## ee.Reducer.centeredCovariance

Creates a reducer that reduces some number of 1-D arrays of the same length N to a covariance matrix of shape NxN. WARNING: this reducer requires that the data has been mean centered.

| Usage | Returns |
|---|---|
| `ee.Reducer.centeredCovariance()` | Reducer |

**No arguments.**

## ee.Reducer.circularMean

Returns a Reducer that computes the (weighted) circular mean of its inputs, which are expected to be in radians. Output will be in the range (-π to π). Where applicable, the output name is "circularMean".

| Usage | Returns |
|---|---|
| `ee.Reducer.circularMean()` | Reducer |

**No arguments.**

## ee.Reducer.circularStddev

Returns a Reducer that computes the (weighted) circular standard deviation of its inputs, which are expected to be in radians, using the sqrt(-2 \* ln(R)) formula. Where applicable, the output name is "circularStdDev".

| Usage | Returns |
|---|---|
| `ee.Reducer.circularStddev()` | Reducer |

**No arguments.**

## ee.Reducer.circularVariance

Returns a Reducer that computes the (weighted) circular variance of its inputs, which are expected to be in radians. Where applicable, the output name is "circularVariance".

| Usage | Returns |
|---|---|
| `ee.Reducer.circularVariance()` | Reducer |

**No arguments.**

## ee.Reducer.combine

Creates a Reducer that runs two reducers in parallel. The combined reducer's outputs will be those of reducer1 followed by those of reducer2, where the output names of reducer2 are prefixed with the given string.

If sharedInputs is true, the reducers must have the same number of inputs, and the combined reducer's will match them; if it is false, the inputs of the combined reducer will be those of reducer1 followed by those of reducer2.

| Usage | Returns |
|---|---|
| `Reducer.combine(reducer2, *outputPrefix*, *sharedInputs*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer1` | Reducer | The first reducer. |
| `reducer2` | Reducer | The second reducer. |
| `outputPrefix` | String, default: "" | Prefix for reducer2's output names. |
| `sharedInputs` | Boolean, default: false | Whether the reducers share inputs. |

## ee.Reducer.count

Returns a Reducer that computes the number of non-null inputs. Where applicable, the output name is "count".

| Usage | Returns |
|---|---|
| `ee.Reducer.count()` | Reducer |

**No arguments.**

## ee.Reducer.countDistinct

Returns a Reducer that computes the number of distinct inputs. Where applicable, the output name is "count".

| Usage | Returns |
|---|---|
| `ee.Reducer.countDistinct()` | Reducer |

**No arguments.**

## ee.Reducer.countDistinctNonNull

Returns a Reducer that computes the number of distinct inputs, ignoring nulls. Where applicable, the output name is "count".

| Usage | Returns |
|---|---|
| `ee.Reducer.countDistinctNonNull()` | Reducer |

**No arguments.**

## ee.Reducer.countEvery

Returns a Reducer that computes the number of inputs. Where applicable, the output name is "count".

| Usage | Returns |
|---|---|
| `ee.Reducer.countEvery()` | Reducer |

**No arguments.**

## ee.Reducer.countRuns

Returns a Reducer that computes the number of runs of distinct, non-null inputs. Where applicable, the output name is "count".

| Usage | Returns |
|---|---|
| `ee.Reducer.countRuns()` | Reducer |

**No arguments.**

## ee.Reducer.covariance

Creates a reducer that reduces some number of 1-D arrays of the same length N to a covariance matrix of shape NxN. This reducer uses the one-pass covariance formula from Sandia National Laboratories Technical Report SAND2008-6212, which can lose accuracy if the values span a large range.

| Usage | Returns |
|---|---|
| `ee.Reducer.covariance()` | Reducer |

**No arguments.**

## ee.Reducer.disaggregate

Separates aggregate inputs (Arrays, Lists, or Dictionaries) into individual items that are then each passed to the specified reducer. When used on dictionaries, the dictionary keys are ignored. Non-aggregated inputs (e.g., Numbers or Strings) are passed to the underlying reducer directly.

| Usage | Returns |
|---|---|
| `Reducer.disaggregate(*axis*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer | The reducer for which to disaggregate inputs. |
| `axis` | Integer, default: null | If specified, indicates an array axis along which to disaggregate. If not specified, arrays are completely disaggregated. Ignored for non-array types. |

## ee.Reducer.first

Returns a Reducer that returns the first of its inputs. Where applicable, the output name is "first".

| Usage | Returns |
|---|---|
| `ee.Reducer.first()` | Reducer |

**No arguments.**

## ee.Reducer.firstNonNull

Returns a Reducer that returns the first of its non-null inputs. Where applicable, the output name is "first".

| Usage | Returns |
|---|---|
| `ee.Reducer.firstNonNull()` | Reducer |

**No arguments.**

## ee.Reducer.fixed2DHistogram

Creates a reducer that will compute a 2D histogram of the inputs using a fixed number of fixed-width bins. Values outside of the \[min, max) range on either axis are ignored. The output is a 2D array of counts, and 2 1-D arrays of bucket lower edges for the xAxis and the yAxis. This reducer is suitable for use per-pixel, however it is always unweighted. The maximum count for any bucket is 2\^31 - 1.

| Usage | Returns |
|---|---|
| `ee.Reducer.fixed2DHistogram(xMin, xMax, xSteps, yMin, yMax, ySteps)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `xMin` | Float | The lower (inclusive) bound of the first bucket on the X axis. |
| `xMax` | Float | The upper (exclusive) bound of the last bucket on the X axis. |
| `xSteps` | Integer | The number of buckets to use on the X axis. |
| `yMin` | Float | The lower (inclusive) bound of the first bucket on the Y axis. |
| `yMax` | Float | The upper (exclusive) bound of the last bucket on the Y axis. |
| `ySteps` | Integer | The number of buckets to use on the Y axis. |

## ee.Reducer.fixedHistogram

Creates a reducer that will compute a histogram of the inputs using a fixed number of fixed width bins. Values outside of the \[min, max) range are ignored. The output is a Nx2 array of bucket lower edges and counts (or cumulative counts) and is suitable for use per-pixel.

| Usage | Returns |
|---|---|
| `ee.Reducer.fixedHistogram(min, max, steps, *cumulative*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `min` | Float | The lower (inclusive) bound of the first bucket. |
| `max` | Float | The upper (exclusive) bound of the last bucket. |
| `steps` | Integer | The number of buckets to use. |
| `cumulative` | Boolean, default: false | When true, generates a cumulative histogram. |

## ee.Reducer.forEach

Creates a Reducer by combining a copy of the given reducer for each output name in the given list. If the reducer has a single output, the output names are used as-is; otherwise they are prefixed to the original output names.

| Usage | Returns |
|---|---|
| `Reducer.forEach(outputNames)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer |   |
| `outputNames` | List |   |

## ee.Reducer.forEachBand

Creates a Reducer by combining a copy of the given reducer for each band in the given image using the band names as output names.

| Usage | Returns |
|---|---|
| `Reducer.forEachBand(image)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer |   |
| `image` | Image |   |

## ee.Reducer.forEachElement

Separately reduces each position in array inputs of equal shape, producing an array output of the same shape.

For example, with the 'sum' reducer applied to 5 arrays with shape 2x2, the output will be a 2x2 array, where each position is the sum of the 5 values at that position.

| Usage | Returns |
|---|---|
| `Reducer.forEachElement()` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer | The reducer to apply to each array element. |

## ee.Reducer.frequencyHistogram

Returns a Reducer that returns a (weighted) frequency table of its inputs. Where applicable, the output name is "histogram".

| Usage | Returns |
|---|---|
| `ee.Reducer.frequencyHistogram()` | Reducer |

**No arguments.**

## ee.Reducer.geometricMedian

Creates a reducer that computes the geometric median across a set of inputs.

| Usage | Returns |
|---|---|
| `ee.Reducer.geometricMedian(numX, *eta*, *initialStepSize*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `numX` | Integer | The number of input dimensions. |
| `eta` | Float, default: 0.001 | The minimum improvement in the solution used as a stopping criteria for the solver. |
| `initialStepSize` | Float, default: 10 | The initial step size used in the solver. |

## ee.Reducer.getOutputs

Returns a list of the output names of the given reducer.

| Usage | Returns |
|---|---|
| `Reducer.getOutputs()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer |   |

## ee.Reducer.group

Groups reducer records by the value of a given input and reduces each group with the given reducer.

| Usage | Returns |
|---|---|
| `Reducer.group(*groupField*, *groupName*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer | The reducer to apply to each group, without the group field. |
| `groupField` | Integer, default: 0 | The field that contains record groups. |
| `groupName` | String, default: "group" | The dictionary key that contains the group. Defaults to 'group'. |

## ee.Reducer.histogram

Create a reducer that will compute a histogram of the inputs.

| Usage | Returns |
|---|---|
| `ee.Reducer.histogram(*maxBuckets*, *minBucketWidth*, *maxRaw*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `maxBuckets` | Integer, default: null | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. |
| `minBucketWidth` | Float, default: null | The minimum histogram bucket width, or null to allow any power of 2. |
| `maxRaw` | Integer, default: null | The number of values to accumulate before building the initial histogram. |

## ee.Reducer.intervalMean

Creates a Reducer to compute the mean of all inputs in the specified percentile range. For small numbers of inputs (up to maxRaw) the mean will be computed directly; for larger numbers of inputs the mean will be derived from a histogram.

| Usage | Returns |
|---|---|
| `ee.Reducer.intervalMean(minPercentile, maxPercentile, *maxBuckets*, *minBucketWidth*, *maxRaw*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `minPercentile` | Float | The lower bound of the percentile range. |
| `maxPercentile` | Float | The upper bound of the percentile range. |
| `maxBuckets` | Integer, default: null | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. |
| `minBucketWidth` | Float, default: null | The minimum histogram bucket width, or null to allow any power of 2. |
| `maxRaw` | Integer, default: null | The number of values to accumulate before building the initial histogram. |

## ee.Reducer.kendallsCorrelation

Creates a reducer that computes the Kendall's Tau-b rank correlation. A positive tau value indicates an increasing trend; negative value indicates a decreasing trend. See https://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/org/apache/commons/math3/stat/correlation/KendallsCorrelation.html for details.

| Usage | Returns |
|---|---|
| `ee.Reducer.kendallsCorrelation(*numInputs*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `numInputs` | Integer, default: 1 | The number of inputs to expect (1 or 2). If 1 is specified, automatically generates sequence numbers for the x value (meaning there can be no ties). |

## ee.Reducer.kurtosis

Returns a Reducer that Computes the kurtosis of its inputs. Where applicable, the output name is "kurtosis".

| Usage | Returns |
|---|---|
| `ee.Reducer.kurtosis()` | Reducer |

**No arguments.**

## ee.Reducer.last

Returns a Reducer that returns the last of its inputs. Where applicable, the output name is "last".

| Usage | Returns |
|---|---|
| `ee.Reducer.last()` | Reducer |

**No arguments.**

## ee.Reducer.lastNonNull

Returns a Reducer that returns the last of its non-null inputs. Where applicable, the output name is "last".

| Usage | Returns |
|---|---|
| `ee.Reducer.lastNonNull()` | Reducer |

**No arguments.**

## ee.Reducer.linearFit

Returns a Reducer that computes the slope and offset for a (weighted) linear regression of 2 inputs. The inputs are expected to be x data followed by y data. Where applicable, the outputs are named: "scale", "offset".

| Usage | Returns |
|---|---|
| `ee.Reducer.linearFit()` | Reducer |

**No arguments.**

## ee.Reducer.linearRegression

Creates a reducer that computes a linear least squares regression with numX independent variables and numY dependent variables.

Each input tuple will have values for the independent variables followed by the dependent variables.

The first output is a coefficients array with dimensions (numX, numY); each column contains the coefficients for the corresponding dependent variable. The second output is a vector of the root mean square of the residuals of each dependent variable. Both outputs are null if the system is underdetermined, e.g., the number of inputs is less than or equal to numX.

| Usage | Returns |
|---|---|
| `ee.Reducer.linearRegression(numX, *numY*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `numX` | Integer | The number of input dimensions. |
| `numY` | Integer, default: 1 | The number of output dimensions. |

## ee.Reducer.max

Creates a reducer that outputs the maximum value of its (first) input. If numInputs is greater than one, also outputs the corresponding values of the additional inputs.

| Usage | Returns |
|---|---|
| `ee.Reducer.max(*numInputs*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `numInputs` | Integer, default: 1 | The number of inputs. |

## ee.Reducer.mean

Returns a Reducer that computes the (weighted) arithmetic mean of its inputs. Where applicable, the output name is "mean".

| Usage | Returns |
|---|---|
| `ee.Reducer.mean()` | Reducer |

**No arguments.**

## ee.Reducer.median

Create a reducer that will compute the median of the inputs. For small numbers of inputs (up to maxRaw) the median will be computed directly; for larger numbers of inputs the median will be derived from a histogram.

| Usage | Returns |
|---|---|
| `ee.Reducer.median(*maxBuckets*, *minBucketWidth*, *maxRaw*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `maxBuckets` | Integer, default: null | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. |
| `minBucketWidth` | Float, default: null | The minimum histogram bucket width, or null to allow any power of 2. |
| `maxRaw` | Integer, default: null | The number of values to accumulate before building the initial histogram. |

## ee.Reducer.min

Creates a reducer that outputs the minimum value of its (first) input. If numInputs is greater than one, also outputs the corresponding values of the additional inputs.

| Usage | Returns |
|---|---|
| `ee.Reducer.min(*numInputs*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `numInputs` | Integer, default: 1 | The number of inputs. |

## ee.Reducer.minMax

Returns a Reducer that computes the minimum and maximum of its inputs. Where applicable, the outputs are named: "min", "max".

| Usage | Returns |
|---|---|
| `ee.Reducer.minMax()` | Reducer |

**No arguments.**

## ee.Reducer.mode

Create a reducer that will compute the mode of the inputs. For small numbers of inputs (up to maxRaw) the mode will be computed directly; for larger numbers of inputs the mode will be derived from a histogram.

| Usage | Returns |
|---|---|
| `ee.Reducer.mode(*maxBuckets*, *minBucketWidth*, *maxRaw*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `maxBuckets` | Integer, default: null | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. |
| `minBucketWidth` | Float, default: null | The minimum histogram bucket width, or null to allow any power of 2. |
| `maxRaw` | Integer, default: null | The number of values to accumulate before building the initial histogram. |

## ee.Reducer.pearsonsCorrelation

Creates a two-input reducer that computes Pearson's product-moment correlation coefficient and the 2-sided p-value test for correlation = 0.

| Usage | Returns |
|---|---|
| `ee.Reducer.pearsonsCorrelation()` | Reducer |

**No arguments.**

## ee.Reducer.percentile

Create a reducer that will compute the specified percentiles, e.g. given \[0, 50, 100\] will produce outputs named 'p0', 'p50', and 'p100' with the min, median, and max respectively. For small numbers of inputs (up to maxRaw) the percentiles will be computed directly; for larger numbers of inputs the percentiles will be derived from a histogram.

| Usage | Returns |
|---|---|
| `ee.Reducer.percentile(percentiles, *outputNames*, *maxBuckets*, *minBucketWidth*, *maxRaw*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `percentiles` | List | A list of numbers between 0 and 100. |
| `outputNames` | List, default: null | A list of names for the outputs, or null to get default names. |
| `maxBuckets` | Integer, default: null | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. |
| `minBucketWidth` | Float, default: null | The minimum histogram bucket width, or null to allow any power of 2. |
| `maxRaw` | Integer, default: null | The number of values to accumulate before building the initial histogram. |

## ee.Reducer.product

Returns a Reducer that computes the product of its inputs. Where applicable, the output name is "product".

| Usage | Returns |
|---|---|
| `ee.Reducer.product()` | Reducer |

**No arguments.**

## ee.Reducer.repeat

Creates a Reducer by combining the specified number of copies of the given reducer. Output names are the same as the given reducer, but each is a list of the corresponding output from each of the reducers.

| Usage | Returns |
|---|---|
| `Reducer.repeat(count)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer |   |
| `count` | Integer | The number of copies of the reducer to combine. |

## ee.Reducer.ridgeRegression

Creates a reducer that computes a ridge regression with numX independent variables (not including constant) followed by numY dependent variables. Ridge regression is a form of Tikhonov regularization which shrinks the regression coefficients by imposing a penalty on their size. With this implementation of ridge regression there NO NEED to include a constant value for bias.

The first output is a coefficients array with dimensions (numX + 1, numY); each column contains the coefficients for the corresponding dependent variable plus the intercept for the dependent variable in the last column. Additional outputs are a vector of the root mean square of the residuals of each dependent variable and a vector of p-values for each dependent variable. Outputs are null if the system is underdetermined, e.g., the number of inputs is less than numX + 1.

| Usage | Returns |
|---|---|
| `ee.Reducer.ridgeRegression(numX, *numY*, *lambda*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `numX` | Integer | the number of independent variables being regressed. |
| `numY` | Integer, default: 1 | the number of dependent variables. |
| `lambda` | Float, default: 0.1 | Regularization parameter. |

## ee.Reducer.robustLinearRegression

Creates a reducer that computes a robust least squares regression with numX independent variables and numY dependent variables, using iteratively reweighted least squares with the Talwar cost function. A point is considered an outlier if the RMS of residuals is greater than beta.

Each input tuple will have values for the independent variables followed by the dependent variables.

The first output is a coefficients array with dimensions (numX, numY); each column contains the coefficients for the corresponding dependent variable. The second is a vector of the root mean square of the residuals of each dependent variable. Both outputs are null if the system is underdetermined, e.g., the number of inputs is less than numX.

| Usage | Returns |
|---|---|
| `ee.Reducer.robustLinearRegression(numX, *numY*, *beta*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `numX` | Integer | The number of input dimensions. |
| `numY` | Integer, default: 1 | The number of output dimensions. |
| `beta` | Float, default: null | Residual error outlier margin. If null, a default value will be computed. |

## ee.Reducer.sampleStdDev

Returns a Reducer that computes the sample standard deviation of its inputs. Where applicable, the output name is "stdDev".

| Usage | Returns |
|---|---|
| `ee.Reducer.sampleStdDev()` | Reducer |

**No arguments.**

## ee.Reducer.sampleVariance

Returns a Reducer that computes the sample variance of its inputs. Where applicable, the output name is "variance".

| Usage | Returns |
|---|---|
| `ee.Reducer.sampleVariance()` | Reducer |

**No arguments.**

## ee.Reducer.sensSlope

Creates a two-input reducer that computes the Sen's slope estimator. The inputs are expected to be x data followed by y data. It returns two double values; the estimated slope and the offset.

| Usage | Returns |
|---|---|
| `ee.Reducer.sensSlope()` | Reducer |

**No arguments.**

## ee.Reducer.setOutputs

Returns a Reducer with the same inputs as the given Reducer, but with outputs renamed and/or removed.

| Usage | Returns |
|---|---|
| `Reducer.setOutputs(outputs)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer |   |
| `outputs` | List | The new output names; any output whose name is null or empty will be dropped. |

## ee.Reducer.skew

Returns a Reducer that Computes the skewness of its inputs. Where applicable, the output name is "skew".

| Usage | Returns |
|---|---|
| `ee.Reducer.skew()` | Reducer |

**No arguments.**

## ee.Reducer.spearmansCorrelation

Creates a two-input reducer that computes the Spearman's rank-moment correlation. See https://commons.apache.org/proper/commons-math/javadocs/api-3.6/org/apache/commons/math3/stat/correlation/SpearmansCorrelation.html for details.

| Usage | Returns |
|---|---|
| `ee.Reducer.spearmansCorrelation()` | Reducer |

**No arguments.**

## ee.Reducer.splitWeights

Returns a Reducer with the same outputs as the given Reducer, but with each weighted input replaced by two unweighted inputs.

| Usage | Returns |
|---|---|
| `Reducer.splitWeights()` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer |   |

## ee.Reducer.stdDev

Returns a Reducer that computes the standard deviation of its inputs. Where applicable, the output name is "stdDev".

| Usage | Returns |
|---|---|
| `ee.Reducer.stdDev()` | Reducer |

**No arguments.**

## ee.Reducer.sum

Returns a Reducer that computes the (weighted) sum of its inputs. Where applicable, the output name is "sum".

| Usage | Returns |
|---|---|
| `ee.Reducer.sum()` | Reducer |

**No arguments.**

## ee.Reducer.toCollection

Returns a reducer that collects its inputs into a FeatureCollection.

| Usage | Returns |
|---|---|
| `ee.Reducer.toCollection(propertyNames, *numOptional*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `propertyNames` | List | The property names that will be defined on each output feature; determines the number of reducer inputs. |
| `numOptional` | Integer, default: 0 | The last numOptional inputs will be considered optional; the other inputs must be non-null or the input tuple will be dropped. |

## ee.Reducer.toList

Creates a reducer that collects its inputs into a list, optionally grouped into tuples.

| Usage | Returns |
|---|---|
| `ee.Reducer.toList(*tupleSize*, *numOptional*)` | Reducer |

| Argument | Type | Details |
|---|---|---|
| `tupleSize` | Integer, default: null | The size of each output tuple, or null for no grouping. Also determines the number of inputs (null tupleSize has 1 input). |
| `numOptional` | Integer, default: 0 | The last numOptional inputs will be considered optional; the other inputs must be non-null or the input tuple will be dropped. |

## ee.Reducer.unweighted

Returns a Reducer with the same inputs and outputs as the given Reducer, but with no weighted inputs.

| Usage | Returns |
|---|---|
| `Reducer.unweighted()` | Reducer |

| Argument | Type | Details |
|---|---|---|
| this: `reducer` | Reducer |   |

## ee.Reducer.variance

Returns a Reducer that computes the variance of its inputs. Where applicable, the output name is "variance".

| Usage | Returns |
|---|---|
| `ee.Reducer.variance()` | Reducer |

**No arguments.**

