# gava-gee

Referência completa da **API JavaScript do Google Earth Engine (GEE)** — 1.747
funções fatiadas por tarefa — para qualquer IDE que leia `AGENTS.md` (Cursor,
GitHub Copilot, Windsurf, Codex, Gemini CLI, Zed, JetBrains).

```bash
npx gava-gee init
```

Instala no seu projeto:

```
AGENTS-gee.md              ← guia para o agente (conceito cliente/servidor + fluxo + índice)
gee/cheatsheet.md          ← as ~35 funções essenciais
gee/references/*.md        ← API completa (1.747 funções) fatiada por tarefa
gee/examples/              ← pipeline fim-a-fim comentado
```

Opções: `npx gava-gee init --force` (sobrescreve) · `npx gava-gee help`.

> Também funciona direto do GitHub, sem npm publicado:
> `npx github:VgavaBR123/gava-skills` *(use o pacote da pasta `packages/gava-gee`)*.

## Como usar

Depois do `init`, peça ao agente da sua IDE:

```
Escreva um script GEE que faça <X> seguindo o AGENTS-gee.md.
```

O agente lê `AGENTS-gee.md` + `gee/cheatsheet.md` e só abre um arquivo de
`gee/references/` quando precisa do parâmetro exato de uma função.

## No Claude Code / Cowork

A mesma referência também está disponível como skill nativa via marketplace:

```bash
/plugin marketplace add VgavaBR123/gava-skills
/plugin install gee-plugin@gava-tools
```

## Licença

[MIT](../../LICENSE) — mantido por **Gava**.
