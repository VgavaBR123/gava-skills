# Classificação — Classifier, Clusterer, ConfusionMatrix, Model

> 36 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ee.Classifier.amnhMaxent`](#ee-classifier-amnhmaxent)
- [`ee.Classifier.confusionMatrix`](#ee-classifier-confusionmatrix)
- [`ee.Classifier.decisionTree`](#ee-classifier-decisiontree)
- [`ee.Classifier.decisionTreeEnsemble`](#ee-classifier-decisiontreeensemble)
- [`ee.Classifier.explain`](#ee-classifier-explain)
- [`ee.Classifier.libsvm`](#ee-classifier-libsvm)
- [`ee.Classifier.load`](#ee-classifier-load)
- [`ee.Classifier.minimumDistance`](#ee-classifier-minimumdistance)
- [`ee.Classifier.mode`](#ee-classifier-mode)
- [`ee.Classifier.schema`](#ee-classifier-schema)
- [`ee.Classifier.setOutputMode`](#ee-classifier-setoutputmode)
- [`ee.Classifier.smileCart`](#ee-classifier-smilecart)
- [`ee.Classifier.smileGradientTreeBoost`](#ee-classifier-smilegradienttreeboost)
- [`ee.Classifier.smileKNN`](#ee-classifier-smileknn)
- [`ee.Classifier.smileNaiveBayes`](#ee-classifier-smilenaivebayes)
- [`ee.Classifier.smileRandomForest`](#ee-classifier-smilerandomforest)
- [`ee.Classifier.spectralRegion`](#ee-classifier-spectralregion)
- [`ee.Classifier.train`](#ee-classifier-train)
- [`ee.Clusterer.schema`](#ee-clusterer-schema)
- [`ee.Clusterer.train`](#ee-clusterer-train)
- [`ee.Clusterer.wekaCascadeKMeans`](#ee-clusterer-wekacascadekmeans)
- [`ee.Clusterer.wekaCobweb`](#ee-clusterer-wekacobweb)
- [`ee.Clusterer.wekaKMeans`](#ee-clusterer-wekakmeans)
- [`ee.Clusterer.wekaLVQ`](#ee-clusterer-wekalvq)
- [`ee.Clusterer.wekaXMeans`](#ee-clusterer-wekaxmeans)
- [`ee.ConfusionMatrix`](#ee-confusionmatrix)
- [`ee.ConfusionMatrix.accuracy`](#ee-confusionmatrix-accuracy)
- [`ee.ConfusionMatrix.array`](#ee-confusionmatrix-array)
- [`ee.ConfusionMatrix.consumersAccuracy`](#ee-confusionmatrix-consumersaccuracy)
- [`ee.ConfusionMatrix.fscore`](#ee-confusionmatrix-fscore)
- [`ee.ConfusionMatrix.kappa`](#ee-confusionmatrix-kappa)
- [`ee.ConfusionMatrix.order`](#ee-confusionmatrix-order)
- [`ee.ConfusionMatrix.producersAccuracy`](#ee-confusionmatrix-producersaccuracy)
- [`ee.Model.fromVertexAi`](#ee-model-fromvertexai)
- [`ee.Model.predictImage`](#ee-model-predictimage)
- [`ee.Model.predictProperties`](#ee-model-predictproperties)

---

## ee.Classifier.amnhMaxent

Creates a Maximum Entropy classifier. Maxent is used to model species distribution probabilities using environmental data for locations of known presence and for a large number of 'background' locations. For more information and to cite, see: https://biodiversityinformatics.amnh.org/open_source/maxent/ and the reference publication: Phillips, et. al., 2004 A maximum entropy approach to species distribution modeling, Proceedings of the Twenty-First International Conference on Machine Learning. The output is a single band named 'probability', containing the modeled probability, and an additional band named 'clamp' when the 'writeClampGrid' argument is true.

| Usage | Returns |
|---|---|
| `ee.Classifier.amnhMaxent(*categoricalNames*, *outputFormat*, *autoFeature*, *linear*, *quadratic*, *product*, *threshold*, *hinge*, *hingeThreshold*, *l2lqThreshold*, *lq2lqptThreshold*, *addSamplesToBackground*, *addAllSamplesToBackground*, *betaMultiplier*, *betaHinge*, *betaLqp*, *betaCategorical*, *betaThreshold*, *extrapolate*, *doClamp*, *writeClampGrid*, *randomTestPoints*, *seed*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `categoricalNames` | List, default: null | A list of the names of the categorical inputs. Any inputs not listed in this argument are considered to be continuous. |
| `outputFormat` | String, default: "cloglog" | Representation of probabilities in output. |
| `autoFeature` | Boolean, default: true | Automatically select which feature classes to use, based on number of training samples. |
| `linear` | Boolean, default: true | Allow linear features to be used. Ignored when autofeature is true. |
| `quadratic` | Boolean, default: true | Allow quadratic features to be used. Ignored when autofeature is true. |
| `product` | Boolean, default: true | Allow product features to be used. Ignored when autofeature is true. |
| `threshold` | Boolean, default: false | Allow threshold features to be used. Ignored when autofeature is true. |
| `hinge` | Boolean, default: true | Allow hinge features to be used. Ignored when autofeature is true. |
| `hingeThreshold` | Integer, default: 15 | Number of samples at which hinge features start being used. Ignored when autofeature is false. |
| `l2lqThreshold` | Integer, default: 10 | Number of samples at which quadratic features start being used. Ignored when autofeature is false. |
| `lq2lqptThreshold` | Integer, default: 80 | Number of samples at which product and threshold features start being used. Ignored when autofeature is false. |
| `addSamplesToBackground` | Boolean, default: true | Add to the background any sample for which has a combination of environmental values that isn't already present in the background. |
| `addAllSamplesToBackground` | Boolean, default: false | Add all samples to the background, even if they have combinations of environmental values that are already present in the background. |
| `betaMultiplier` | Float, default: 1 | Regularization multiplier. Multiply all automatic regularization parameters by this number. A higher number gives a more spread-out distribution. |
| `betaHinge` | Float, default: -1 | Regularization parameter to be applied to all hinge features; negative value enables automatic setting. |
| `betaLqp` | Float, default: -1 | Regularization parameter to be applied to all linear, quadratic and product features; negative value enables automatic setting. |
| `betaCategorical` | Float, default: -1 | Regularization parameter to be applied to all categorical features; negative value enables automatic setting. |
| `betaThreshold` | Float, default: -1 | Regularization parameter to be applied to all threshold features; negative value enables automatic setting. |
| `extrapolate` | Boolean, default: true | Extrapolate. Predict to regions of environmental space outside the limits encountered during training. |
| `doClamp` | Boolean, default: true | Apply clamping to output. |
| `writeClampGrid` | Boolean, default: true | Adds a band to the output ('clamp') showing the spatial distribution of clamping. At each point, the value is the absolute difference between prediction values with and without clamping. |
| `randomTestPoints` | Integer, default: 0 | Random test percentage. The percentage of training points to hold aside as test points, used to compute AUX, omission, etc. |
| `seed` | Long, default: 0 | A seed used when generating random numbers. |

## ee.Classifier.confusionMatrix

Computes a 2D confusion matrix for a classifier based on its training data (e.g., resubstitution error). Axis 0 of the matrix corresponds to the input classes and axis 1 corresponds to the output classes. The rows and columns start at class 0 and increase sequentially up to the maximum class value, so some rows or columns might be empty if the input classes aren't 0-based or sequential.

| Usage | Returns |
|---|---|
| `Classifier.confusionMatrix()` | ConfusionMatrix |

| Argument | Type | Details |
|---|---|---|
| this: `classifier` | Classifier | The classifier to use. |

## ee.Classifier.decisionTree

Creates a classifier that applies the given decision tree.

| Usage | Returns |
|---|---|
| `ee.Classifier.decisionTree(treeString)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `treeString` | String | The decision tree, specified in the text format generated by R and other similar tools. |

## ee.Classifier.decisionTreeEnsemble

Creates a classifier that applies the given decision trees.

| Usage | Returns |
|---|---|
| `ee.Classifier.decisionTreeEnsemble(treeStrings)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `treeStrings` | List | The decision trees, specified in the text format generated by R and other similar tools. Each item in the list should contain one or more trees in text format. |

## ee.Classifier.explain

Describe the results of a trained classifier.

| Usage | Returns |
|---|---|
| `Classifier.explain()` | Dictionary |

| Argument | Type | Details |
|---|---|---|
| this: `classifier` | Classifier | The classifier to describe. |

## ee.Classifier.libsvm

Creates an empty Support Vector Machine classifier.

| Usage | Returns |
|---|---|
| `ee.Classifier.libsvm(*decisionProcedure*, *svmType*, *kernelType*, *shrinking*, *degree*, *gamma*, *coef0*, *cost*, *nu*, *terminationEpsilon*, *lossEpsilon*, *oneClass*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `decisionProcedure` | String, default: "Voting" | The decision procedure to use for classification. Either 'Voting' or 'Margin'. Not used for regression. |
| `svmType` | String, default: "C_SVC" | The SVM type. One of \`C_SVC\`, \`NU_SVC\`, \`ONE_CLASS\`, \`EPSILON_SVR\`, or \`NU_SVR\`. |
| `kernelType` | String, default: "LINEAR" | The kernel type. One of LINEAR (u′×v), POLY ((γ×u′×v + coef₀)ᵈᵉᵍʳᵉᵉ), RBF (exp(-γ×\|u-v\|²)), or SIGMOID (tanh(γ×u′×v + coef₀)). |
| `shrinking` | Boolean, default: true | Whether to use shrinking heuristics. |
| `degree` | Integer, default: null | The degree of polynomial. Valid for POLY kernels. |
| `gamma` | Float, default: null | The gamma value in the kernel function. Defaults to the reciprocal of the number of features. Valid for POLY, RBF, and SIGMOID kernels. |
| `coef0` | Float, default: null | The coef₀ value in the kernel function. Defaults to 0. Valid for POLY and SIGMOID kernels. |
| `cost` | Float, default: null | The cost (C) parameter. Defaults to 1. Only valid for C-SVC, epsilon-SVR, and nu-SVR. |
| `nu` | Float, default: null | The nu parameter. Defaults to 0.5. Only valid for nu-SVC, one-class SVM, and nu-SVR. |
| `terminationEpsilon` | Float, default: null | The termination criterion tolerance (e). Defaults to 0.001. Only valid for epsilon-SVR. |
| `lossEpsilon` | Float, default: null | The epsilon in the loss function (p). Defaults to 0.1. Only valid for epsilon-SVR. |
| `oneClass` | Integer, default: null | The class of the training data on which to train in a one-class SVM. Defaults to 0. Only valid for one-class SVM. Possible values are 0 and 1. The classifier output is binary (0/1) and will match this class value for the data determined to be in the class. |

## ee.Classifier.load

Creates a Classifier.

| Usage | Returns |
|---|---|
| `ee.Classifier.load(id)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `id` | String | The Classifier's Asset ID. |

## ee.Classifier.minimumDistance

Creates a minimum distance classifier for the given distance metric. In CLASSIFICATION mode, the nearest class is returned. In REGRESSION mode, the distance to the nearest class center is returned. In RAW mode, the distance to every class center is returned.

| Usage | Returns |
|---|---|
| `ee.Classifier.minimumDistance(*metric*, *kNearest*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `metric` | String, default: "euclidean" | The distance metric to use. Options are: - 'euclidean' - Euclidean distance from the unnormalized class mean. - 'cosine' - spectral angle from the unnormalized class mean. - 'mahalanobis' - Mahalanobis distance from the class mean. - 'manhattan' - Manhattan distance from the unnormalized class mean. |
| `kNearest` | Integer, default: 1 | If greater than 1, the result will contain an array of the k nearest neighbors or distances, based on the output mode setting. If kNearest is greater than the total number of classes, it will be set equal to the number of classes. |

## ee.Classifier.mode

Returns the classifier mode: `CLASSIFICATION`, `REGRESSION`, `PROBABILITY`, `MULTIPROBABILITY`, `RAW`, or `RAW_REGRESSION`.

| Usage | Returns |
|---|---|
| `Classifier.mode()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `classifier` | Classifier |   |

## ee.Classifier.schema

Returns the names of the inputs used by this classifier or null if this classifier has not had any training data added yet.

| Usage | Returns |
|---|---|
| `Classifier.schema()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `classifier` | Classifier |   |

## ee.Classifier.setOutputMode

Sets a classifier's output format.

Refer to https://developers.google.com/earth-engine/guides/classification for a list of supported modes for each classifier.

| Usage | Returns |
|---|---|
| `Classifier.setOutputMode(mode)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| this: `classifier` | Classifier | An input classifier. |
| `mode` | String | The output mode. One of: - CLASSIFICATION (default): The output is the class number. - REGRESSION: The output is the result of standard regression. - PROBABILITY: The output is the probability that the classification is correct. - MULTIPROBABILITY: The output is an array of probabilities that each class is correct ordered by classes seen. - RAW: The output is an array of the internal representation of the classification process. For example, the raw votes in multi-decision tree models. - RAW_REGRESSION: The output is an array of the internal representation of the regression process. For example, the raw predictions of multiple regression trees. |

## ee.Classifier.smileCart

Creates an empty CART classifier. See:

"Classification and Regression Trees," L. Breiman, J. Friedman, R. Olshen, C. Stone.   
Chapman and Hall, 1984.

| Usage | Returns |
|---|---|
| `ee.Classifier.smileCart(*maxNodes*, *minLeafPopulation*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `maxNodes` | Integer, default: null | The maximum number of leaf nodes in each tree. If unspecified, defaults to no limit. |
| `minLeafPopulation` | Integer, default: 1 | Only create nodes whose training set contains at least this many points. |

## ee.Classifier.smileGradientTreeBoost

Creates an empty Gradient Tree Boost classifier.

| Usage | Returns |
|---|---|
| `ee.Classifier.smileGradientTreeBoost(numberOfTrees, *shrinkage*, *samplingRate*, *maxNodes*, *loss*, *seed*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `numberOfTrees` | Integer | The number of decision trees to create. |
| `shrinkage` | Float, default: 0.005 | The shrinkage parameter in (0, 1\] controls the learning rate of procedure. |
| `samplingRate` | Float, default: 0.7 | The sampling rate for stochastic tree boosting. |
| `maxNodes` | Integer, default: null | The maximum number of leaf nodes in each tree. If unspecified, defaults to no limit. |
| `loss` | String, default: "LeastAbsoluteDeviation" | Loss function for regression. One of: LeastSquares, LeastAbsoluteDeviation, Huber. |
| `seed` | Integer, default: 0 | The randomization seed. |

## ee.Classifier.smileKNN

Creates an empty k-NN classifier.

The k-nearest neighbor algorithm (k-NN) is a method for classifying objects by a majority vote of its neighbors, with the object being assigned to the class most common amongst its k nearest neighbors (k is a positive integer, typically small, typically odd).

| Usage | Returns |
|---|---|
| `ee.Classifier.smileKNN(*k*, *searchMethod*, *metric*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `k` | Integer, default: 1 | The number of neighbors for classification. |
| `searchMethod` | String, default: "AUTO" | Search method. The following are valid \[AUTO, LINEAR_SEARCH, KD_TREE, COVER_TREE\]: <br /> - \`AUTO\` Chooses between KD_TREE and COVER_TREE depending on the dimension count. If the features have less than 10 dimensions KD_TREE is used. - \`LINEAR_SEARCH\` More performant than space partitioning approaches (such as K-D trees) in higher dimensional spaces. - \`KD_TREE\` Nearest neighbor search method using a space-partitioning dataset structure for organizing points in a k-dimensional space. KD-trees are not suitable for efficiently finding the nearest neighbor in high dimensional spaces. As a general rule, if the dimensionality is D then number of points in the dataset, N, should be N \>\> 2\^D. - \`COVER_TREE\` Cover tree is a data structure for generic nearest neighbor search, which is especially efficient in spaces with small intrinsic dimension. Results may vary between the different search methods for distance ties and probability values. Since performance and results may vary, consult with SMILE's documentation and other literature. |
| `metric` | String, default: "EUCLIDEAN" | The distance metric to use. NOTE: KD_TREE (and AUTO for low dimensions) will not use the metric selected. Options are: - \`EUCLIDEAN\` - Euclidean distance. - \`MAHALANOBIS\` - Mahalanobis distance. - \`MANHATTAN\` - Manhattan distance. - \`BRAYCURTIS\` - Bray-Curtis distance. |

## ee.Classifier.smileNaiveBayes

Creates an empty Naive Bayes classifier. This classifier assumes that the feature vector consists of positive integers, and negative inputs are discarded.

| Usage | Returns |
|---|---|
| `ee.Classifier.smileNaiveBayes(*lambda*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `lambda` | Float, default: 0.000001 | A smoothing lambda. Used to avoid assigning zero probability to classes not seen during training, instead using lambda / (lambda \* nFeatures). |

## ee.Classifier.smileRandomForest

Creates an empty Random Forest classifier.

| Usage | Returns |
|---|---|
| `ee.Classifier.smileRandomForest(numberOfTrees, *variablesPerSplit*, *minLeafPopulation*, *bagFraction*, *maxNodes*, *seed*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `numberOfTrees` | Integer | The number of decision trees to create. |
| `variablesPerSplit` | Integer, default: null | The number of variables per split. If unspecified, uses the square root of the number of variables. |
| `minLeafPopulation` | Integer, default: 1 | Only create nodes whose training set contains at least this many points. |
| `bagFraction` | Float, default: 0.5 | The fraction of input to bag per tree. |
| `maxNodes` | Integer, default: null | The maximum number of leaf nodes in each tree. If unspecified, defaults to no limit. |
| `seed` | Integer, default: 0 | The randomization seed. |

## ee.Classifier.spectralRegion

Creates a classifier that tests if its inputs lie within a polygon defined by a set of coordinates in an arbitrary 2D coordinate system. Each input to be classified must have 2 values (e.g., images must have 2 bands). The result will be 1 wherever the input values are contained within the given polygon and 0 otherwise.

| Usage | Returns |
|---|---|
| `ee.Classifier.spectralRegion(coordinates, *schema*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| `coordinates` | List | The coordinates of the polygon, as a list of rings. Each ring is a list of coordinate pairs (e.g., \[u1, v1, u2, v2, ..., uN, vN\]). No edge may intersect any other edge. The resulting classification will be a 1 wherever the input values are within the interior of the given polygon, that is, an odd number of polygon edges must be crossed to get outside the polygon and 0 otherwise. |
| `schema` | List, default: null | The classifier's schema. A list of band or property names that the classifier will operate on. Since this classifier doesn't undergo a training step, these have to be specified manually. Defaults to \['u', 'v'\]. |

## ee.Classifier.train

Trains the classifier on a collection of features, using the specified numeric properties of each feature as training data. The geometry of the features is ignored.

| Usage | Returns |
|---|---|
| `Classifier.train(features, classProperty, *inputProperties*, *subsampling*, *subsamplingSeed*)` | Classifier |

| Argument | Type | Details |
|---|---|---|
| this: `classifier` | Classifier | An input classifier. |
| `features` | FeatureCollection | The collection to train on. |
| `classProperty` | String | The name of the property containing the class value. Each feature must have this property and its value must be numeric. |
| `inputProperties` | List, default: null | The list of property names to include as training data. Each feature must have all these properties and their values must be numeric. This argument is optional if the input collection contains a 'band_order' property, (as produced by Image.sample). |
| `subsampling` | Float, default: 1 | An optional subsampling factor, within (0, 1\]. |
| `subsamplingSeed` | Integer, default: 0 | A randomization seed to use for subsampling. |

## ee.Clusterer.schema

Returns the names of the inputs used by this Clusterer, or null if this Clusterer has not had any training data added yet.

| Usage | Returns |
|---|---|
| `Clusterer.schema()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `clusterer` | Clusterer |   |

## ee.Clusterer.train

Trains the Clusterer on a collection of features using the specified numeric properties of each feature as training data. The geometry of the features is ignored.

| Usage | Returns |
|---|---|
| `Clusterer.train(features, *inputProperties*, *subsampling*, *subsamplingSeed*)` | Clusterer |

| Argument | Type | Details |
|---|---|---|
| this: `clusterer` | Clusterer | An input Clusterer. |
| `features` | FeatureCollection | The collection to train on. |
| `inputProperties` | List, default: null | The list of property names to include as training data. Each feature must have all these properties, and their values must be numeric. This argument is optional if the input collection contains a 'band_order' property (as produced by Image.sample). |
| `subsampling` | Float, default: 1 | An optional subsampling factor, within (0, 1\]. |
| `subsamplingSeed` | Integer, default: 0 | A randomization seed to use for subsampling. |

## ee.Clusterer.wekaCascadeKMeans

Cascade simple k-means selects the best k according to the Calinski-Harabasz criterion. For more information see:

Calinski, T. and J. Harabasz. 1974. A dendrite method for cluster analysis. Commun. Stat. 3: 1-27.

| Usage | Returns |
|---|---|
| `ee.Clusterer.wekaCascadeKMeans(*minClusters*, *maxClusters*, *restarts*, *manual*, *init*, *distanceFunction*, *maxIterations*)` | Clusterer |

| Argument | Type | Details |
|---|---|---|
| `minClusters` | Integer, default: 2 | Min number of clusters. |
| `maxClusters` | Integer, default: 10 | Max number of clusters. |
| `restarts` | Integer, default: 10 | Number of restarts. |
| `manual` | Boolean, default: false | Manually select the number of clusters. |
| `init` | Boolean, default: false | Set whether to initialize using the probabilistic farthest first like method of the k-means++ algorithm (rather than the standard random selection of initial cluster centers). |
| `distanceFunction` | String, default: "Euclidean" | Distance function to use. Options are: Euclidean and Manhattan. |
| `maxIterations` | Integer, default: null | Maximum number of iterations for k-means. |

## ee.Clusterer.wekaCobweb

Implementation of the Cobweb clustering algorithm. For more information see:

D. Fisher (1987). Knowledge acquisition via incremental conceptual clustering. Machine Learning. 2(2):139-172. and J. H. Gennari, P. Langley, D. Fisher (1990). Models of incremental concept formation. Artificial Intelligence. 40:11-61.

| Usage | Returns |
|---|---|
| `ee.Clusterer.wekaCobweb(*acuity*, *cutoff*, *seed*)` | Clusterer |

| Argument | Type | Details |
|---|---|---|
| `acuity` | Float, default: 1 | Acuity (minimum standard deviation). |
| `cutoff` | Float, default: 0.002 | Cutoff (minimum category utility). |
| `seed` | Integer, default: 42 | Random number seed. |

## ee.Clusterer.wekaKMeans

Cluster data using the k-means algorithm. Can use either the Euclidean distance (default) or the Manhattan distance. If the Manhattan distance is used, then centroids are computed as the component-wise median rather than mean. For more information see:

D. Arthur, S. Vassilvitskii: k-means++: the advantages of careful seeding. In: Proceedings of the eighteenth annual ACM-SIAM symposium on Discrete algorithms, 1027-1035, 2007.

| Usage | Returns |
|---|---|
| `ee.Clusterer.wekaKMeans(nClusters, *init*, *canopies*, *maxCandidates*, *periodicPruning*, *minDensity*, *t1*, *t2*, *distanceFunction*, *maxIterations*, *preserveOrder*, *fast*, *seed*)` | Clusterer |

| Argument | Type | Details |
|---|---|---|
| `nClusters` | Integer | Number of clusters. |
| `init` | Integer, default: 0 | Initialization method to use. 0 = random, 1 = k-means++, 2 = canopy, 3 = farthest first. |
| `canopies` | Boolean, default: false | Use canopies to reduce the number of distance calculations. |
| `maxCandidates` | Integer, default: 100 | Maximum number of candidate canopies to retain in memory at any one time when using canopy clustering. T2 distance plus, data characteristics, will determine how many candidate canopies are formed before periodic and final pruning are performed, which might result in exceess memory consumption. This setting avoids large numbers of candidate canopies consuming memory. |
| `periodicPruning` | Integer, default: 10000 | How often to prune low density canopies when using canopy clustering. |
| `minDensity` | Integer, default: 2 | Minimum canopy density, when using canopy clustering, below which a canopy will be pruned during periodic pruning. |
| `t1` | Float, default: -1.5 | The T1 distance to use when using canopy clustering. A value \< 0 is taken as a positive multiplier for T2. |
| `t2` | Float, default: -1 | The T2 distance to use when using canopy clustering. Values \< 0 cause a heuristic based on attribute std. deviation to be used. |
| `distanceFunction` | String, default: "Euclidean" | Distance function to use. Options are: Euclidean and Manhattan. |
| `maxIterations` | Integer, default: null | Maximum number of iterations. |
| `preserveOrder` | Boolean, default: false | Preserve order of instances. |
| `fast` | Boolean, default: false | Enables faster distance calculations, using cut-off values. Disables the calculation/output of squared errors/distances. |
| `seed` | Integer, default: 10 | The randomization seed. |

## ee.Clusterer.wekaLVQ

A Clusterer that implements the Learning Vector Quantization algorithm. For more details, see:

T. Kohonen, "Learning Vector Quantization", The Handbook of Brain Theory and Neural Networks, 2nd Edition, MIT Press, 2003, pp. 631-634.

| Usage | Returns |
|---|---|
| `ee.Clusterer.wekaLVQ(*numClusters*, *learningRate*, *epochs*, *normalizeInput*)` | Clusterer |

| Argument | Type | Details |
|---|---|---|
| `numClusters` | Integer, default: 7 | The number of clusters. |
| `learningRate` | Float, default: 1 | The learning rate for the training algorithm. Value should be greater than 0 and less or equal to 1. |
| `epochs` | Integer, default: 1000 | Number of training epochs. Value should be greater than or equal to 1. |
| `normalizeInput` | Boolean, default: false | Skip normalizing the attributes. |

## ee.Clusterer.wekaXMeans

X-Means is K-Means with an efficient estimation of the number of clusters. For more information see:

Dan Pelleg, Andrew W. Moore: X-means: Extending K-means with Efficient Estimation of the Number of Clusters. In: Seventeenth International Conference on Machine Learning, 727-734, 2000.

| Usage | Returns |
|---|---|
| `ee.Clusterer.wekaXMeans(*minClusters*, *maxClusters*, *maxIterations*, *maxKMeans*, *maxForChildren*, *useKD*, *cutoffFactor*, *distanceFunction*, *seed*)` | Clusterer |

| Argument | Type | Details |
|---|---|---|
| `minClusters` | Integer, default: 2 | Minimum number of clusters. |
| `maxClusters` | Integer, default: 8 | Maximum number of clusters. |
| `maxIterations` | Integer, default: 3 | Maximum number of overall iterations. |
| `maxKMeans` | Integer, default: 1000 | The maximum number of iterations to perform in KMeans. |
| `maxForChildren` | Integer, default: 1000 | The maximum number of iterations in KMeans that is performed on the child centers. |
| `useKD` | Boolean, default: false | Use a KDTree. |
| `cutoffFactor` | Float, default: 0 | Takes the given percentage of the split centroids if none of the children win. |
| `distanceFunction` | String, default: "Euclidean" | Distance function to use. Options are: Chebyshev, Euclidean, and Manhattan. |
| `seed` | Integer, default: 10 | The randomization seed. |

## ee.ConfusionMatrix

Creates a confusion matrix. Axis 0 (the rows) of the matrix correspond to the actual values, and Axis 1 (the columns) to the predicted values.

| Usage | Returns |
|---|---|
| `ee.ConfusionMatrix(array, *order*)` | ConfusionMatrix |

| Argument | Type | Details |
|---|---|---|
| `array` | Object | A square, 2D array of integers, representing the confusion matrix. Note that unlike the ee.Array constructor, this argument cannot take a list. |
| `order` | List, default: null | The row and column size and order, for non-contiguous or non-zero based matrices. |

## ee.ConfusionMatrix.accuracy

Computes the overall accuracy of a confusion matrix defined as correct / total.

| Usage | Returns |
|---|---|
| `ConfusionMatrix.accuracy()` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `confusionMatrix` | ConfusionMatrix |   |

## ee.ConfusionMatrix.array

Returns a confusion matrix as an Array.

| Usage | Returns |
|---|---|
| `ConfusionMatrix.array()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `confusionMatrix` | ConfusionMatrix |   |

## ee.ConfusionMatrix.consumersAccuracy

Computes the consumer's accuracy (reliability) of a confusion matrix defined as (correct / total) for each row.

| Usage | Returns |
|---|---|
| `ConfusionMatrix.consumersAccuracy()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `confusionMatrix` | ConfusionMatrix |   |

## ee.ConfusionMatrix.fscore

Computes the Fβ-score for the confusion matrix.

| Usage | Returns |
|---|---|
| `ConfusionMatrix.fscore(*beta*)` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `confusionMatrix` | ConfusionMatrix |   |
| `beta` | Float, default: 1 | A factor indicating how much more important recall is than precision. The standard F-score is equivalent to setting β to one. |

## ee.ConfusionMatrix.kappa

Computes the Kappa statistic for the confusion matrix.

| Usage | Returns |
|---|---|
| `ConfusionMatrix.kappa()` | Float |

| Argument | Type | Details |
|---|---|---|
| this: `confusionMatrix` | ConfusionMatrix |   |

## ee.ConfusionMatrix.order

Returns the name and order of the rows and columns of the matrix.

| Usage | Returns |
|---|---|
| `ConfusionMatrix.order()` | List |

| Argument | Type | Details |
|---|---|---|
| this: `confusionMatrix` | ConfusionMatrix |   |

## ee.ConfusionMatrix.producersAccuracy

Computes the producer's accuracy of a confusion matrix defined as (correct / total) for each column.

| Usage | Returns |
|---|---|
| `ConfusionMatrix.producersAccuracy()` | Array |

| Argument | Type | Details |
|---|---|---|
| this: `confusionMatrix` | ConfusionMatrix |   |

## ee.Model.fromVertexAi

Returns an ee.Model from a description of a Vertex AI model endpoint. (See https://cloud.google.com/vertex-ai).

| Usage | Returns |
|---|---|
| `ee.Model.fromVertexAi(endpoint, *inputProperties*, *inputTypeOverride*, *inputShapes*, *proj*, *fixInputProj*, *inputTileSize*, *inputOverlapSize*, *outputTileSize*, *outputBands*, *outputProperties*, *outputMultiplier*, *maxPayloadBytes*, *payloadFormat*)` | Model |

| Argument | Type | Details |
|---|---|---|
| `endpoint` | String | The endpoint name for predictions. |
| `inputProperties` | List, default: null | Properties passed with each prediction instance. Image predictions are tiled, so these properties will be replicated into each image tile instance. Defaults to no properties. |
| `inputTypeOverride` | Dictionary, default: null | Types to which model inputs will be coerced if specified. Both Image bands and Image/Feature properties are valid. |
| `inputShapes` | Dictionary, default: null | The fixed shape of input array bands. For each array band not specified, the fixed array shape will be automatically deduced from a non-masked pixel. |
| `proj` | Projection, default: null | The input projection at which to sample all bands. Defaults to the default projection of an image's first band. |
| `fixInputProj` | Boolean, default: null | If true, pixels will be sampled in a fixed projection specified by 'proj'. The output projection is used otherwise. Defaults to false. |
| `inputTileSize` | List, default: null | Rectangular dimensions of pixel tiles passed in to prediction instances. Required for image predictions. |
| `inputOverlapSize` | List, default: null | Amount of adjacent-tile overlap in X/Y along each edge of pixel tiles passed in to prediction instances. Defaults to \[0, 0\]. |
| `outputTileSize` | List, default: null | Rectangular dimensions of pixel tiles returned from AI Platform. Defaults to the value in 'inputTileSize'. |
| `outputBands` | Dictionary, default: null | A map from output band names to a dictionary of output band info. Valid band info fields are 'type' and 'dimensions'. 'type' should be a ee.PixelType describing the output band, and 'dimensions' is an optional integer with the number of dimensions in that band e.g., "outputBands: {'p': {'type': ee.PixelType.int8(), 'dimensions': 1}}". Required for image predictions. |
| `outputProperties` | Dictionary, default: null | A map from output property names to a dictionary of output property info. Valid property info fields are 'type' and 'dimensions'. 'type' should be a ee.PixelType describing the output property, and 'dimensions' is an optional integer with the number of dimensions for that property if it is an array e.g., "outputBands: {'p': {'type': ee.PixelType.int8(), 'dimensions': 1}}". Required for predictions from FeatureCollections. |
| `outputMultiplier` | Float, default: null | An approximation to the increase in data volume for the model outputs over the model inputs. If specified this must be \>= 1. This is only needed if the model produces more data than it consumes, e.g., a model that takes 5 bands and produces 10 outputs per pixel. |
| `maxPayloadBytes` | Long, default: null | The prediction payload size limit in bytes. Defaults to 1.5MB (1500000 bytes.) |
| `payloadFormat` | String, default: null | The payload format of entries in prediction requests and responses. One of: \['SERIALIZED_TF_TENSORS, 'RAW_JSON', 'ND_ARRAYS', 'GRPC_TF_TENSORS', 'GRPC_SERIALIZED_TF_TENSORS', 'GRPC_TF_EXAMPLES'\]. Defaults to 'SERIALIZED_TF_TENSORS'. |

## ee.Model.predictImage

Make predictions from pixel tiles of an image. The predictions are merged as bands with the input image.

The model will receive 0s in place of masked pixels. The masks of predicted output bands are the minimum of the masks of the inputs.

| Usage | Returns |
|---|---|
| `Model.predictImage(image)` | Image |

| Argument | Type | Details |
|---|---|---|
| this: `model` | Model |   |
| `image` | Image | The input image. |

## ee.Model.predictProperties

Make predictions for each feature in a collection. Predicted properties are merged with the properties of the input feature.

| Usage | Returns |
|---|---|
| `Model.predictProperties(collection)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `model` | Model |   |
| `collection` | FeatureCollection | The input collection. |

