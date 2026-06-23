# Contexto do projeto — Skill `gee-docs`

Este arquivo é lido automaticamente pelo Claude Code (e serve de contexto para o
Gemini CLI via `GEMINI.md`). Resume por que esta skill existe e como ela é
organizada, para que o agente não precise reexplicar nem pesquisar na internet.

## O que é esta pasta

Uma **skill** que empacota a referência completa da **API JavaScript do Google
Earth Engine (GEE)** — 1.747 funções — reorganizada por tarefa, mais o fluxo de
trabalho típico do Code Editor e exemplos comentados. Faz parte do marketplace
de skills em `D:\dev\gava-skills\`.

## Para quê serve

- Ajudar a **escrever código GEE correto** sem ficar pesquisando na web.
- Servir de **manual local** da API: consulte por `grep`/leitura direcionada
  nos arquivos de `references/` em vez de buscar na internet.
- Lembrar o agente do modelo **cliente vs. servidor** do Earth Engine, que é a
  fonte da maioria dos bugs.

## Convenções (seguir sempre)

- Idioma: **pt-BR**.
- Nomes de arquivo/pasta: **minúsculas-com-hífen**.
- Diretório de desenvolvimento: `D:\dev\` (Windows).

## Como a skill é organizada (divulgação progressiva)

```
gee-docs/
├── SKILL.md          ← comece aqui: conceito cliente/servidor + fluxo + índice + armadilhas
├── CLAUDE.md         ← este arquivo (contexto)
├── cheatsheet.md     ← ~35 funções essenciais, 1 linha cada
├── references/       ← API COMPLETA, fatiada por tarefa (leia só o necessário)
│   ├── core-image.md        (Image, ImageCollection, Kernel, Terrain)
│   ├── core-vector.md       (FeatureCollection, Feature, Filter, Join)
│   ├── core-geometry.md     (ee.Geometry, construtores, projeções)
│   ├── core-reducer.md      (ee.Reducer)
│   ├── core-export-map.md   (Export.*, Map.*)
│   ├── data-types.md        (Number, String, List, Dictionary, Date, Array)
│   ├── algorithms.md / ml-classify.md / ee-data.md / ui.md / misc.md
└── examples/
    └── iptu-open-buildings.js   ← exemplo de pipeline (join espacial + export)
```

**Regra para o agente:** não carregue a referência inteira no contexto. Leia
`SKILL.md` + `cheatsheet.md`. Só abra um arquivo de `references/` quando precisar
do parâmetro exato de uma função daquele tópico. A referência é seu "manual
local" — consulte-a por `grep`/leitura direcionada em vez de buscar na web.

## Origem

Gerada a partir da documentação oficial da API JavaScript do Earth Engine.
