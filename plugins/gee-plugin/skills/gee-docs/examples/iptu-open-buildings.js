/**
 * IPTU × Open Buildings — Porto Velho / SEMEC
 * --------------------------------------------------------------------------
 * Identifica edificações detectadas pelo Google Open Buildings que NÃO estão
 * cobertas pela base cadastral do IPTU (candidatas a omissão cadastral).
 *
 * Como rodar: cole no editor de código do Earth Engine (code.earthengine.google.com).
 * Ajuste os pontos marcados com  // <-- AJUSTAR
 * --------------------------------------------------------------------------
 */

// === 1. ÁREA DE ESTUDO ====================================================
// Opção A: desenhe um polígono no mapa e ele vira a variável `geometry`.
// Opção B: carregue o perímetro do município de um asset seu. // <-- AJUSTAR
// Exemplo com retângulo aproximado da área urbana de Porto Velho:
var areaEstudo = ee.Geometry.Rectangle([-63.95, -8.83, -63.82, -8.72]); // <-- AJUSTAR

Map.centerObject(areaEstudo, 13);

// === 2. CADASTRO DO IPTU (sua base) =======================================
// Suba seus lotes cadastrados como asset (FeatureCollection) e referencie aqui.
var cadastro = ee.FeatureCollection('users/SEU_USUARIO/iptu_lotes_pvh'); // <-- AJUSTAR
cadastro = cadastro.filterBounds(areaEstudo);

// === 3. EDIFICAÇÕES DETECTADAS (Open Buildings v3) ========================
var LIMIAR_CONFIANCA = 0.70; // calibre: maior = menos falso positivo
var edificacoes = ee.FeatureCollection('GOOGLE/Research/open-buildings/v3/polygons')
  .filterBounds(areaEstudo)
  .filter(ee.Filter.gte('confidence', LIMIAR_CONFIANCA));

// === 4. IMAGEM DE FUNDO (Sentinel-2, para conferência visual) =============
var fundo = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(areaEstudo)
  .filterDate('2024-01-01', '2024-12-31')
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .median();

var visRGB = {bands: ['B4', 'B3', 'B2'], min: 0, max: 3000};
Map.addLayer(fundo, visRGB, 'Sentinel-2 (fundo)');

// === 5. CRUZAMENTO ESPACIAL: detecção SEM lote cadastrado =================
// Para cada edificação, procura um lote do cadastro que a intersecte.
// O join "inverted" devolve as edificações que NÃO casaram com nenhum lote.
var filtroEspacial = ee.Filter.intersects({
  leftField: '.geo',
  rightField: '.geo',
  maxError: 1  // metros
});

var semCadastro = ee.Join.inverted().apply(edificacoes, cadastro, filtroEspacial);

// === 6. ENRIQUECER: área construída e centróide ===========================
var candidatos = semCadastro.map(function (f) {
  var g = f.geometry();
  return f.set({
    area_m2: g.area(1),                       // área em m²
    lon: g.centroid(1).coordinates().get(0),  // longitude do centróide
    lat: g.centroid(1).coordinates().get(1)   // latitude do centróide
  });
});

// Opcional: descartar construções minúsculas (ruído). // <-- AJUSTAR
candidatos = candidatos.filter(ee.Filter.gte('area_m2', 20));

// === 7. VISUALIZAÇÃO ======================================================
Map.addLayer(cadastro.draw('00FF00', 1, 1), {}, 'Cadastro IPTU (verde)');
Map.addLayer(edificacoes.draw('FFFF00', 1, 1), {}, 'Open Buildings (amarelo)');
Map.addLayer(candidatos.draw('FF0000', 2, 2), {}, 'Candidatos sem cadastro (vermelho)');

print('Edificações detectadas:', edificacoes.size());
print('Candidatos sem cadastro:', candidatos.size());

// === 8. EXPORTAR PARA O POSTGIS ===========================================
// Gera um SHP no Drive. Depois: ogr2ogr / shp2pgsql -> PostGIS -> cruza no banco.
Export.table.toDrive({
  collection: candidatos,
  description: 'iptu_candidatos_sem_cadastro_pvh',
  folder: 'gee_iptu',
  fileNamePrefix: 'iptu_candidatos_pvh',
  fileFormat: 'SHP',                  // ou 'GeoJSON'
  selectors: ['area_m2', 'lon', 'lat', 'confidence']
});
// Lembre: a exportação só roda depois de iniciar a tarefa na aba "Tasks".
