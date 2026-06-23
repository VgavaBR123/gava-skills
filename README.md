# Gava Skills

Coletânea de skills e plugins para desenvolvimento de software, distribuída pelo
marketplace **gava-tools**. Hoje reúne três plugins:

- **`sdd-plugin`** — **Spec-Driven Development (SDD)**: a especificação dirige o
  código, em fases curtas e verificáveis, baseado no
  [GitHub spec-kit](https://github.com/github/spec-kit).
- **`seguranca-plugin`** — skills de **segurança e privacidade**: auditoria de
  conformidade **LGPD** para pipelines fiscais (CPF/CNPJ), além de bases de
  proteção de PII (NIST SP 800-122) e criptografia aplicada (Boneh-Shoup).
- **`gee-plugin`** — referência completa da **API JavaScript do Google Earth
  Engine (GEE)**: 1.747 funções fatiadas por tarefa, conceito cliente/servidor,
  cheatsheet e exemplos.

O SDD é distribuído de **três formas**, para funcionar tanto em qualquer IDE
quanto nos produtos Claude. O `seguranca-plugin` e o `gee-plugin` são
distribuídos pelo marketplace e também por npm (`gava-seguranca`, `gava-gee`).

---

## 🚀 Instalação

Escolha a forma que combina com sua ferramenta:

### 1. Qualquer IDE — via npm (recomendado)

Funciona em Cursor, GitHub Copilot, Windsurf, Codex, Gemini CLI, Zed, JetBrains
e qualquer assistente que leia `AGENTS.md`. Na pasta do seu projeto:

```bash
npx gava-sdd init
```

Isso instala:

```
AGENTS.md                                  ← instruções lidas pela sua IDE
specs/templates/constitution-template.md
specs/templates/spec-template.md
specs/templates/plan-template.md
specs/templates/tasks-template.md
```

Opções: `npx gava-sdd init --force` (sobrescreve) · `npx gava-sdd help`.

> Sem publicar no npm, também funciona direto do GitHub:
> `npx github:VgavaBR123/gava-skills init`

### 2. Claude Code / Cowork — via marketplace

```bash
/plugin marketplace add VgavaBR123/gava-skills
/plugin install sdd-plugin@gava-tools
```

A skill `spec-driven-development` passa a ser ativada automaticamente quando você
fala em criar spec, plano, tarefas, etc.

### 3. Manual — copiar o AGENTS.md

Baixe [`portable/AGENTS.md`](./portable/AGENTS.md) e coloque na raiz do seu
projeto. É autocontido (já traz a metodologia e os templates embutidos).

---

## 🔐 Segurança e privacidade — `seguranca-plugin`

Skills de auditoria de segurança e conformidade.

**No Claude Code / Cowork** — via marketplace:

```bash
/plugin marketplace add VgavaBR123/gava-skills
/plugin install seguranca-plugin@gava-tools
```

**Em qualquer outra IDE** — a auditoria LGPD via npm (instala um `AGENTS-lgpd.md`,
as referências e o scanner de PII no seu projeto):

```bash
npx gava-seguranca init
```

| Skill | Para quê |
|-------|----------|
| `auditoria-lgpd-fiscal` | Auditoria de conformidade **LGPD** para pipelines fiscais que tratam **CPF/CNPJ**: detecta PII em claro, valida tokenização (HMAC-SHA256) e criptografia (AES-256-GCM), e checa se dado identificável ou reversível cruza a fronteira para LLMs (Claude Code, Bedrock), APIs, dashboards ou arquivos. Cobre Python, SQL/PostgreSQL, DuckDB e ETL. |
| `nist-pii-protection` | Base **NIST SP 800-122**: classificação de PII e a distinção entre de-identificação e anonimização. |
| `boneh-shoup-applied-crypto` | Base de **criptografia aplicada** (Boneh-Shoup): segurança semântica, CPA/CCA, AEAD/AES-GCM, MAC/HMAC e unicidade de nonce — fundamenta as outras duas. |

A `auditoria-lgpd-fiscal` é ativada automaticamente quando você pede para
auditar, revisar ou validar segurança/conformidade de código que trata CPF/CNPJ
ou cadastros fiscais (NFS-e, PGDAS, ITBI, IPTU), mesmo sem dizer "LGPD".

---

## 🌍 Google Earth Engine — `gee-plugin`

Referência completa da **API JavaScript do Google Earth Engine** (1.747 funções),
reorganizada por tarefa, com cheatsheet e exemplos. Para escrever código GEE
correto sem ficar pesquisando na web.

**No Claude Code / Cowork** — via marketplace:

```bash
/plugin marketplace add VgavaBR123/gava-skills
/plugin install gee-plugin@gava-tools
```

**Em qualquer outra IDE** — via npm (instala um `AGENTS-gee.md` + a pasta `gee/`
com cheatsheet, referência e exemplos no seu projeto):

```bash
npx gava-gee init
```

A skill `gee-docs` é ativada automaticamente quando você fala em Earth Engine,
GEE, `ee.*`, Sentinel/Landsat/MODIS, FeatureCollection/Geometry, reducers ou
export para Drive/Cloud Storage.

---

## 🌱 Como funciona o SDD

A especificação deixa de ser rascunho descartável e vira o artefato central que
dirige o código. O trabalho avança por fases, cada uma é um **portão**: só
avança quando o artefato anterior está sólido.

```
constituição → especificação → clarificação → plano → tarefas → análise → implementação
```

| Fase | Artefato | Foco |
|------|----------|------|
| 0. Constituição | `constitution.md` | Princípios de engenharia (qualidade, testes, performance, segurança). Uma vez por projeto. |
| 1. Especificação | `spec.md` | O **quê** e o **porquê** — histórias, requisitos, critérios de sucesso. Sem stack. |
| 2. Clarificação | atualiza `spec.md` | Resolve ambiguidades e itens `[NEEDS CLARIFICATION]`. |
| 3. Plano técnico | `plan.md` | A stack e a arquitetura. Roda o *Constitution Check*. |
| 4. Tarefas | `tasks.md` | Quebra o plano em tarefas ordenadas por dependência e história. |
| 5. Análise | relatório | Checagem cruzada entre spec, plano e tarefas antes de codar. |
| 6. Implementação | código | Executa as tarefas respeitando dependências e TDD. |

### Como usar no dia a dia

Peça uma fase por vez ao agente da sua IDE:

```
Vamos começar via SDD. Cria a constituição do projeto.
Agora a especificação de uma feature de login com e-mail e senha.
Gera o plano técnico — vamos usar Node + Postgres.
Quebra isso em tarefas.
```

Os arquivos são criados em `specs/NNN-nome-da-feature/`, usando os templates.

---

## 🗂️ Estrutura do repositório

```
gava-skills/
├── package.json                  # pacote npm (CLI gava-sdd)
├── bin/cli.js                    # comando "npx gava-sdd init"
├── portable/
│   └── AGENTS.md                 # versão universal, autocontida
├── .claude-plugin/
│   └── marketplace.json          # catálogo do marketplace (gava-tools)
├── plugins/
│   ├── sdd-plugin/
│   │   ├── .claude-plugin/plugin.json
│   │   └── skills/spec-driven-development/
│   │       ├── SKILL.md
│   │       ├── templates/        # constitution, spec, plan, tasks
│   │       └── reference/        # fluxo e checklist de portões
│   ├── seguranca-plugin/
│   │   ├── .claude-plugin/plugin.json
│   │   └── skills/
│   │       ├── auditoria-lgpd-fiscal/   # SKILL.md + references/ + scripts/
│   │       ├── nist-pii-protection/
│   │       └── boneh-shoup-applied-crypto/
│   └── gee-plugin/
│       ├── .claude-plugin/plugin.json
│       └── skills/gee-docs/      # SKILL.md + cheatsheet + references/ + examples/
├── packages/
│   ├── gava-seguranca/           # pacote npm da auditoria LGPD (npx gava-seguranca)
│   │   ├── package.json
│   │   ├── bin/cli.js
│   │   └── assets/               # AGENTS-lgpd.md, references/, scan_pii.py
│   └── gava-gee/                 # pacote npm da referência GEE (npx gava-gee)
│       ├── package.json
│       ├── bin/cli.js
│       └── assets/               # AGENTS-gee.md, cheatsheet.md, references/, examples/
├── LICENSE
└── README.md
```

---

## 🔄 Publicando novas versões

1. Faça as alterações na skill, no `AGENTS.md` ou nos templates.
2. Suba a `version` no manifesto do plugin alterado
   (`plugins/sdd-plugin/.claude-plugin/plugin.json` ou
   `plugins/seguranca-plugin/.claude-plugin/plugin.json`) — e, se mexer no CLI
   do npm, também no `package.json`.
3. `git add . && git commit -m "..." && git push`
4. Publique no npm o(s) pacote(s) afetado(s):
   - SDD: `npm publish` (na raiz) — atualiza o `npx gava-sdd`.
   - Segurança/LGPD: `cd packages/gava-seguranca && npm publish` — atualiza o
     `npx gava-seguranca`. (Se mexer nas referências/scanner da skill em
     `plugins/seguranca-plugin`, copie as alterações para `assets/` antes.)
   - GEE: `cd packages/gava-gee && npm publish` — atualiza o `npx gava-gee`. (Se
     mexer na referência da skill em `plugins/gee-plugin`, copie as alterações
     para `assets/` antes.)
5. Usuários do marketplace recebem com `/plugin marketplace update gava-tools`.

> Valide antes: `claude plugin validate .`

---

## 📄 Licença

[MIT](./LICENSE) — mantido por **Gava**.
