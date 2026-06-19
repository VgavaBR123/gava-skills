# Gava Skills

Ferramentas para conduzir o desenvolvimento de software pela metodologia
**Spec-Driven Development (SDD)** — a especificação dirige o código, em fases
curtas e verificáveis, baseada no [GitHub spec-kit](https://github.com/github/spec-kit).

Este repositório distribui o SDD de **três formas**, para funcionar tanto em
qualquer IDE quanto nos produtos Claude.

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
│   └── sdd-plugin/
│       ├── .claude-plugin/plugin.json
│       └── skills/spec-driven-development/
│           ├── SKILL.md
│           ├── templates/        # constitution, spec, plan, tasks
│           └── reference/        # fluxo e checklist de portões
├── LICENSE
└── README.md
```

---

## 🔄 Publicando novas versões

1. Faça as alterações na skill, no `AGENTS.md` ou nos templates.
2. Suba a `version` no `package.json` **e** no `plugins/sdd-plugin/.claude-plugin/plugin.json`.
3. `git add . && git commit -m "..." && git push`
4. Publique no npm: `npm publish` (atualiza o `npx gava-sdd`).
5. Usuários do marketplace recebem com `/plugin marketplace update gava-tools`.

> Valide antes: `claude plugin validate .`

---

## 📄 Licença

[MIT](./LICENSE) — mantido por **Gava**.
