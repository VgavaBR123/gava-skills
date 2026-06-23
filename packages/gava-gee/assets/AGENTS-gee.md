# Google Earth Engine — guia para o agente

Referência local da **API JavaScript do Google Earth Engine (GEE)** — 1.747
funções, fatiadas por tarefa. Use este arquivo + `gee/cheatsheet.md` antes de
escrever qualquer código GEE. Só abra um arquivo de `gee/references/` quando
precisar do parâmetro exato de uma função daquele tópico.

## Como o Earth Engine funciona (o conceito que evita 90% dos bugs)

O Earth Engine é **cliente + servidor**. Os objetos `ee.*` (`ee.Image`,
`ee.FeatureCollection`, `ee.Number`…) são *proxies* — descrições de uma
computação que roda nos servidores do Google, não valores prontos no navegador.

- **Não misture objetos `ee.*` com lógica nativa do JS.** `if`/`for`/`+` do
  JavaScript não funcionam sobre objetos do servidor. Use `.map()`,
  `ee.Algorithms.If`, `ee.List.iterate`, e os métodos do próprio objeto.
- **`getInfo()` é síncrono e caro** — força trazer o resultado pro cliente.
  Prefira `print()` (assíncrono) ou `Export`.
- **Computação é preguiçosa.** Nada roda até `print`, `Map.addLayer`, `getInfo`
  ou iniciar um `Export`.

## O caminho mínimo viável

```
1. Carregar    → ee.Image / ee.ImageCollection / ee.FeatureCollection (por ID)
2. Recortar    → .filterBounds(geometria) e/ou .filterDate(ini, fim)
3. Compor      → .median() / .mosaic() / .map(...) / cálculo de índices
4. Visualizar  → Map.centerObject + Map.addLayer(obj, visParams, nome)
5. Analisar    → reduceRegion(s) / reduceToVectors / classificadores
6. Exportar    → Export.image.toDrive / Export.table.toDrive (SHP, GeoJSON, CSV)
```

## Mapa da referência (`gee/references/`)

| Arquivo | Quando ler |
|---|---|
| `gee/references/core-image.md` | ee.Image / ImageCollection: bandas, máscaras, mosaico, índices, reduceRegions, reduceToVectors |
| `gee/references/core-vector.md` | FeatureCollection, Feature, Filter, Join |
| `gee/references/core-geometry.md` | ee.Geometry: área, interseção, buffer, centróide, projeções |
| `gee/references/core-reducer.md` | ee.Reducer: estatística por região |
| `gee/references/core-export-map.md` | Export.* e Map.* |
| `gee/references/data-types.md` | Number, String, List, Dictionary, Date, Array |
| `gee/references/algorithms.md` | ee.Algorithms.* |
| `gee/references/ml-classify.md` | Classifier, Clusterer |
| `gee/references/ee-data.md` | ee.data.* (assets) |
| `gee/references/ui.md` | ui.* (apps no Code Editor) |
| `gee/references/misc.md` | o resto |

## Armadilhas conhecidas

- **`filterBounds` com geometria grande degrada a performance.** Use a menor
  geometria possível.
- **Export não roda sozinho:** `Export.*` só cria a tarefa; inicie na aba
  **Tasks** do Code Editor.
- **Estilo de vetor no mapa:** em `Map.addLayer` o único parâmetro de cor para
  FeatureCollection é `color`; para estilizar por atributo use `.draw()`/`.style()`.
- **Reprojeção implícita:** seja explícito em `reproject`/`reduceResolution`
  quando o resultado depender da grade de pixels.

> Exemplo de pipeline fim-a-fim (join espacial + export) em
> `gee/examples/iptu-open-buildings.js`.
