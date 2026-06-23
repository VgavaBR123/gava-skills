---
name: gee-docs
description: >
  Referência completa e fluxo de trabalho da API JavaScript do Google Earth
  Engine (GEE). Use SEMPRE que o usuário mencionar Earth Engine, GEE, `ee.*`,
  Code Editor (code.earthengine.google.com), imagens de satélite (Sentinel,
  Landsat, MODIS), FeatureCollection/Geometry, reducers, classificadores, ou
  exportação para Drive/Cloud Storage/Assets. Cobre carregar dados, recortar por
  área e período, criar mosaicos, calcular índices (NDVI etc.), estatística por
  região, classificação, visualização no mapa e export. Consulte esta skill
  antes de escrever qualquer código GEE, mesmo que o pedido pareça simples —
  evita sair procurando na internet e gastar token à toa.
---

# Google Earth Engine — API JavaScript

Esta skill traz a **referência completa da API JavaScript do Earth Engine**
(1.747 funções), reorganizada por tarefa em vez de ordem alfabética, mais o
fluxo de trabalho típico e exemplos comentados.

**Regra de ouro:** não leia a referência inteira. Leia este SKILL.md + o
`cheatsheet.md`. Só abra um arquivo de `references/` quando precisar do
parâmetro exato de uma função específica daquele tópico.

## Como o Earth Engine funciona (o conceito que evita 90% dos bugs)

O Earth Engine é **cliente + servidor**. Os objetos `ee.*` (`ee.Image`,
`ee.FeatureCollection`, `ee.Number`…) são *proxies* — descrições de uma
computação que roda nos servidores do Google, não valores prontos no navegador.

Consequências práticas:

- **Não misture objetos `ee.*` com lógica nativa do JS.** `if`/`for`/`+`/comparações
  do JavaScript não funcionam sobre objetos do servidor. Use `.map()`,
  `ee.Algorithms.If`, `ee.List.iterate`, e os métodos do próprio objeto
  (`ee.Number.add`, `ee.String.cat`, etc.).
- **`getInfo()` é síncrono e caro** — força trazer o resultado pro cliente e
  trava a interface. Evite em coleções grandes; prefira `print()` (assíncrono)
  ou `Export`.
- **Computação é preguiçosa.** Nada roda até você `print`, `Map.addLayer`,
  `getInfo` ou iniciar um `Export`. Erros podem só aparecer nesse momento.

## O caminho mínimo viável (decore esta sequência)

```
1. Carregar    → ee.Image / ee.ImageCollection / ee.FeatureCollection (por ID)
2. Recortar    → .filterBounds(geometria) e/ou .filterDate(ini, fim)
3. Compor      → .median() / .mosaic() / .map(...) / cálculo de índices
4. Visualizar  → Map.centerObject + Map.addLayer(obj, visParams, nome)
5. Analisar    → reduceRegion(s) / reduceToVectors / classificadores
6. Exportar    → Export.image.toDrive / Export.table.toDrive (SHP, GeoJSON, CSV)
```

Veja `examples/` para fluxos já escritos e comentados.

## Decisões comuns que afetam o resultado

1. **Coleção certa** — Sentinel-2 (`COPERNICUS/S2_SR_HARMONIZED`, 10 m) para
   detalhe e cor verdadeira; Landsat para série histórica longa; MODIS para
   varredura diária/regional. Confira bandas e escala antes.
2. **Máscara de nuvem** — filtre por `CLOUDY_PIXEL_PERCENTAGE` e/ou aplique a
   banda de qualidade (`QA60`/`SCL`) antes de compor o mosaico.
3. **`scale` nos reducers** — define a resolução da estatística. Use a escala
   nativa da imagem; valores menores explodem o custo, maiores perdem detalhe.
4. **Onde processar** — agregue no servidor (`reduceRegions`, `Export`) em vez
   de puxar tudo pro cliente com `getInfo()`.

## Mapa da referência (`references/`)

Abra apenas o arquivo do tópico que você precisa:

| Arquivo | Quando ler |
|---|---|
| `references/core-image.md` | ee.Image / ImageCollection: bandas, máscaras, mosaico, índices, reduceRegions, reduceToVectors |
| `references/core-vector.md` | FeatureCollection, Feature, Filter, Join — vetores e cruzamentos |
| `references/core-geometry.md` | ee.Geometry: área, interseção, buffer, centróide, construtores, projeções |
| `references/core-reducer.md` | ee.Reducer: estatística por região (média, soma, contagem, histograma) |
| `references/core-export-map.md` | Export.* (SHP/GeoJSON/CSV/GeoTIFF) e Map.* (addLayer, centerObject) |
| `references/data-types.md` | Number, String, List, Dictionary, Date, Array |
| `references/algorithms.md` | ee.Algorithms.* (segmentação, detecção de bordas etc.) |
| `references/ml-classify.md` | Classifier, Clusterer (classificação supervisionada/não-supervisionada) |
| `references/ee-data.md` | ee.data.* (acesso programático a assets) |
| `references/ui.md` | ui.* (apps e widgets interativos no Code Editor) |
| `references/misc.md` | o que não se encaixa acima |

## Armadilhas conhecidas do GEE

- **`filterBounds` com geometria grande degrada muito a performance.** Use a
  menor geometria possível (área de estudo recortada), não uma coleção enorme.
- **Cliente vs. servidor:** objetos `ee.*` são *promessas* no servidor. Não dá
  pra usar `if`/`for` nativos do JS sobre eles — use `.map()`,
  `ee.Algorithms.If`, etc.
- **`getInfo()` é síncrono e caro** — puxa o resultado pro cliente. Evite em
  coleções grandes; prefira `Export` ou `print()`.
- **Export não roda sozinho:** `Export.*` só *cria* a tarefa. É preciso iniciá-la
  na aba **Tasks** do Code Editor (ou via API).
- **Estilo de vetor no mapa:** em `Map.addLayer`, o único parâmetro de cor para
  FeatureCollection é `color`. Para estilizar por atributo, use `.draw()` ou
  `.style()`.
- **Reprojeção implícita:** operações com `scale`/`crs` podem reprojetar sem você
  pedir. Seja explícito em `reproject`/`reduceResolution` quando o resultado
  depender da grade de pixels.

## Exemplos (`examples/`)

- `examples/iptu-open-buildings.js` — fluxo fim-a-fim de cruzamento espacial
  (Open Buildings × base cadastral) mantido como **modelo de pipeline**:
  carregar → filtrar → join espacial → enriquecer → exportar. Útil como receita
  mesmo fora do contexto original; adapte os datasets e a área de estudo.
