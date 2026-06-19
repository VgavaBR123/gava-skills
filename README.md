# Gava Skills

Marketplace de plugins e skills para desenvolvimento de software, usado com o
Claude Code / Cowork. Atualmente distribui o **sdd-plugin**, que traz a skill de
**Spec-Driven Development (SDD)**.

---

## 📦 Plugins disponíveis

| Plugin | Skill | O que faz |
|--------|-------|-----------|
| `sdd-plugin` | `spec-driven-development` | Conduz o desenvolvimento por fases — da especificação ao código — seguindo a metodologia Spec-Driven Development, baseada no [GitHub spec-kit](https://github.com/github/spec-kit). |

---

## 🚀 Instalação

No Claude Code, adicione o marketplace e instale o plugin:

```bash
/plugin marketplace add VgavaBR123/gava-skills
/plugin install sdd-plugin@gava-tools
```

Para atualizar quando houver novas versões:

```bash
/plugin marketplace update gava-tools
```

---

## 🌱 O que é Spec-Driven Development

SDD inverte o fluxo tradicional: a **especificação deixa de ser rascunho
descartável e vira o artefato central** que dirige o código. Em vez de codar
peça por peça ("vibe coding"), o trabalho avança em fases curtas e verificáveis,
cada uma produzindo um documento que a fase seguinte consome.

### As fases

```
constituição → especificação → clarificação → plano → tarefas → análise → implementação
 (princípios)    (o quê/porquê)   (resolver       (o como) (passos)  (checar)   (codar)
                                   dúvidas)
```

| Fase | Artefato | Foco |
|------|----------|------|
| 0. Constituição | `constitution.md` | Princípios de engenharia do projeto (qualidade, testes, performance, segurança). Uma vez por projeto. |
| 1. Especificação | `spec.md` | O **quê** e o **porquê** — histórias de usuário, requisitos, critérios de sucesso. Sem stack. |
| 2. Clarificação | atualiza `spec.md` | Resolve ambiguidades e itens `[NEEDS CLARIFICATION]`. |
| 3. Plano técnico | `plan.md` | Agora sim a stack e a arquitetura. Roda o *Constitution Check*. |
| 4. Tarefas | `tasks.md` | Quebra o plano em tarefas acionáveis, ordenadas por dependência e história. |
| 5. Análise | relatório | Checagem cruzada entre spec, plano e tarefas antes de codar. |
| 6. Implementação | código | Executa as tarefas, respeitando dependências e TDD. |

Cada fase é um **portão**: só avança quando o artefato anterior está sólido.

---

## 💡 Como usar

Depois de instalar, abra um projeto e peça uma fase por vez. Exemplos:

```
Vamos começar este projeto via SDD. Cria a constituição.
```
```
Agora cria a especificação para uma feature de login com e-mail e senha.
```
```
Pode gerar o plano técnico — vamos usar Node + Postgres.
```
```
Quebra isso em tarefas.
```

A skill cria os arquivos de verdade na pasta do projeto, dentro de
`specs/NNN-nome-da-feature/`, usando os templates inclusos.

---

## 🗂️ Estrutura do repositório

```
gava-skills/
├── .claude-plugin/
│   └── marketplace.json          # catálogo do marketplace (gava-tools)
├── plugins/
│   └── sdd-plugin/
│       ├── .claude-plugin/
│       │   └── plugin.json        # manifesto do plugin
│       └── skills/
│           └── spec-driven-development/
│               ├── SKILL.md        # instruções da skill
│               ├── templates/      # constitution, spec, plan, tasks
│               └── reference/       # fluxo e checklist de portões
└── README.md
```

---

## 🔄 Publicando novas versões

1. Faça as alterações na skill ou nos templates.
2. Suba a `version` no `plugins/sdd-plugin/.claude-plugin/plugin.json`.
3. `git add . && git commit -m "..." && git push`
4. Os usuários recebem a atualização rodando `/plugin marketplace update gava-tools`.

> Dica: validar antes de publicar com `claude plugin validate .`

---

## 📄 Licença

Defina a licença do projeto (ex.: MIT) e adicione um arquivo `LICENSE`.

---

Mantido por **Gava**.
