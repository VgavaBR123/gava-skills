# Cheatsheet GEE — funções essenciais

As ~35 funções que resolvem 90% do trabalho. Assinatura em uma linha; abra o
arquivo de `references/` indicado se precisar de todos os parâmetros.

## Carregar dados
```js
ee.Image(id)                             // carrega uma imagem                     [core-image]
ee.ImageCollection(id)                   // carrega coleção de imagens (Sentinel/Landsat) [core-image]
ee.FeatureCollection(id)                 // carrega coleção vetorial               [core-vector]
collection.filterBounds(geom)            // recorta por interseção com geometria   [core-image/vector]
collection.filterDate(ini, fim)          // recorta por período                    [core-image]
collection.filter(ee.Filter.lt(p, v))    // filtra por atributo (ex: nuvem)        [core-vector]
```

## Compor imagens
```js
collection.median()                      // mosaico mediano (tira nuvens)          [core-image]
collection.mosaic()                      // sobrepõe (último por cima)             [core-image]
collection.map(fn)                       // aplica função a cada imagem            [core-image]
image.select(bandas)                     // escolhe bandas                         [core-image]
image.normalizedDifference(['B8','B4'])  // índice tipo NDVI                       [core-image]
image.updateMask(mask)                   // aplica máscara (nuvem, água…)          [core-image]
```

## Geometria (medir, recortar)
```js
ee.Geometry.Polygon(coords)              // polígono                               [core-geometry]
ee.Geometry.Rectangle([w,s,e,n])         // retângulo (área de estudo)             [core-geometry]
geom.area(maxError)                      // área em m²                             [core-geometry]
geom.centroid()                          // ponto representativo                    [core-geometry]
geom.buffer(dist)                        // dilata/contrai (tolerância)            [core-geometry]
geom.intersection(outra)                 // sobreposição entre duas geometrias     [core-geometry]
geom.difference(outra)                   // o que sobra                            [core-geometry]
```

## Filtros e cruzamento de vetores
```js
ee.Filter.gte(prop, valor)               // atributo >= valor                      [core-vector]
ee.Filter.bounds(geom)                   // dentro de uma geometria                [core-vector]
ee.Filter.intersects(prop, geom)         // interseção espacial (join)             [core-vector]
ee.Join.saveBest(matchKey, measureKey)   // melhor correspondência por feature     [core-vector]
ee.Join.inner() / .inverted()            // só casados / só os que NÃO casaram     [core-vector]
join.apply(primaria, secundaria, filtro) // executa o join                        [core-vector]
```

## Estatística por região (raster → atributo)
```js
image.reduceRegion(reducer, geom, scale) // estatística numa área                  [core-image]
image.reduceRegions(fc, reducer, scale)  // estatística por feature                [core-image]
image.reduceToVectors(...)               // raster (máscara) → polígonos           [core-image]
image.sampleRegions(fc, ...)             // amostra pixels por feature             [core-image]
ee.Reducer.mean() / .sum() / .count()    // redutores comuns                       [core-reducer]
```

## Classificação (opcional)
```js
ee.Classifier.smileRandomForest(n)       // classificador supervisionado           [ml-classify]
classifier.train(amostras, 'classe', bandas) // treina                            [ml-classify]
image.classify(classifier)               // aplica o modelo                        [ml-classify]
```

## Visualizar no mapa
```js
Map.centerObject(obj, zoom)              // centraliza na área                     [core-export-map]
Map.setCenter(lon, lat, zoom)           // centraliza por coordenada              [core-export-map]
Map.addLayer(obj, visParams, nome)      // adiciona camada                        [core-export-map]
FeatureCollection.draw(cor, ...)        // pinta vetor como imagem (rápido)       [core-vector]
```

## Exportar
```js
Export.image.toDrive(img, ...)          // baixar recorte raster (GeoTIFF)        [core-export-map]
Export.table.toDrive(fc, ..., 'SHP')    // vetor: 'SHP' | 'GeoJSON' | 'CSV'       [core-export-map]
Export.table.toCloudStorage(fc, ...)    // alternativa em bucket                  [core-export-map]
Export.image.toAsset(img, ...)          // salvar como asset no Earth Engine      [core-export-map]
// Lembre: a tarefa só roda depois de iniciá-la na aba "Tasks" do Code Editor.
```

## Datasets úteis (IDs de exemplo)
```
COPERNICUS/S2_SR_HARMONIZED                          // Sentinel-2 (10 m, cor verdadeira/NDVI)
LANDSAT/LC09/C02/T1_L2                               // Landsat 9 (série histórica)
MODIS/061/MOD13Q1                                    // MODIS NDVI (250 m, 16 dias)
USGS/SRTMGL1_003                                     // SRTM (altitude do terreno)
GOOGLE/Research/open-buildings/v3/polygons          // edificações detectadas (polígonos)
```
