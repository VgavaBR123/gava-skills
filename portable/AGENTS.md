# AGENTS.md — Spec-Driven Development (SDD)

> Arquivo de instruções no padrão aberto **AGENTS.md**, lido nativamente por
> Cursor, GitHub Copilot, Windsurf, Codex, Gemini CLI, Aider, Zed, JetBrains e
> Claude Code. Copie este arquivo para a **raiz do seu projeto** para que o
> agente de IA da sua IDE conduza o desenvolvimento pela metodologia SDD.
>
> Baseado no GitHub spec-kit (https://github.com/github/spec-kit).

## Como o agente deve trabalhar neste projeto

Use **Spec-Driven Development**: a especificação dirige o código. Não faça
"vibe coding". Avance em fases curtas e verificáveis; cada fase produz um
documento dentro de `specs/<NNN-nome-da-feature>/`. **Uma fase por vez** —
mostre o artefato, peça validação e só então avance (cada fase é um portão).

### Regras de operação
1. Descubra em que fase o projeto está. Projeto novo → comece na Constituição.
2. Não invente requisitos: marque `[NEEDS CLARIFICATION: ...]` e pergunte.
3. Mantenha a especificação **neutra de tecnologia**; a stack só entra no Plano.
4. Respeite a Constituição em todas as fases — ela vence preferências do agente.
5. Crie os arquivos de verdade usando os templates abaixo, removendo placeholders.

### Fases
```
constituição → especificação → clarificação → plano → tarefas → análise → implementação
```
- **0. Constituição** (`constitution.md`, uma vez): princípios de qualidade,
  testes, UX, performance e segurança.
- **1. Especificação** (`spec.md`): o quê/porquê — histórias priorizadas e
  independentemente testáveis, requisitos (FR-00X), critérios de sucesso
  mensuráveis (SC-00X). Sem stack.
- **2. Clarificação**: resolva ambiguidades e `[NEEDS CLARIFICATION]`; registre
  numa seção `## Clarifications` da spec.
- **3. Plano** (`plan.md`): stack, arquitetura, estrutura de pastas. Rode o
  *Constitution Check* (o plano viola algum princípio? justifique ou simplifique).
- **4. Tarefas** (`tasks.md`): tarefas acionáveis agrupadas por história de
  usuário; dependências (modelos → serviços → endpoints); `[P]` = paralelizável;
  caminho exato de cada arquivo; se há testes, eles vêm antes (TDD).
- **5. Análise**: checagem cruzada spec × plano × tarefas (cobertura, órfãos,
  over-engineering) antes de codar.
- **6. Implementação**: execute as tarefas na ordem, valide cada checkpoint,
  commit por tarefa ou grupo lógico.

---

## Template: constitution.md

```markdown
# Constituição do Projeto: [NOME]
**Versão**: 1.0.0 | **Ratificada em**: [DATA]

## Princípios Fundamentais
### I. Qualidade de Código
[Ex.: legível, revisado antes do merge; lint/formatação automáticos.]
### II. Padrão de Testes
[Ex.: lógica de negócio com teste; TDD em fluxos críticos; cobertura mínima X%.]
### III. Consistência de UX
[Ex.: padrões de interface e erros consistentes; acessibilidade mínima.]
### IV. Performance
[Ex.: metas explícitas (p95 < Xms); otimizar só com medição.]
### V. Segurança e Dados
[Ex.: validar toda entrada; segredos fora do código; menor privilégio.]

## Restrições Organizacionais
[cloud provider, stacks aprovadas, licenças, compliance.]

## Governança
- Sobrepõe preferências individuais. Emendas exigem justificativa e nova versão.
- A fase de Plano DEVE rodar o Constitution Check contra este documento.
```

---

## Template: spec.md

```markdown
# Especificação de Feature: [NOME]
**Branch**: `[NNN-nome]` | **Criada**: [DATA] | **Status**: Rascunho

## Cenários de Usuário e Testes *(obrigatório)*
### História 1 - [Título] (Prioridade: P1)
[Jornada em linguagem simples]
**Por que esta prioridade**: [...]
**Teste independente**: [...]
**Cenários de Aceite**:
1. **Dado** [estado], **Quando** [ação], **Então** [resultado]

### Edge Cases
- O que acontece quando [condição de borda]?

## Requisitos *(obrigatório)*
### Funcionais
- **FR-001**: O sistema DEVE [capacidade]
- **FR-00X**: [NEEDS CLARIFICATION: ...]
### Entidades-Chave *(se envolve dados)*
- **[Entidade]**: [o que representa, atributos sem implementação]

## Critérios de Sucesso *(obrigatório, mensuráveis e neutros de tecnologia)*
- **SC-001**: [ex.: "usuário completa X em menos de 2 min"]

## Premissas
- [Premissa sobre escopo/usuários]

## Clarifications
- **[DATA]** — P: [pergunta] / R: [resposta]
```

---

## Template: plan.md

```markdown
# Plano de Implementação: [FEATURE]
**Branch**: `[NNN-nome]` | **Data**: [DATA] | **Spec**: [link]

## Resumo
[Requisito principal + abordagem técnica]

## Contexto Técnico
**Linguagem/Versão**: [...] | **Dependências**: [...] | **Armazenamento**: [...]
**Testes**: [...] | **Plataforma**: [...] | **Tipo**: [biblioteca/cli/web/mobile]
**Performance**: [...] | **Restrições**: [...] | **Escala**: [...]

## Constitution Check
[Liste cada princípio e marque se o plano respeita. Violação → justificar abaixo.]

## Estrutura do Projeto
[Árvore de pastas concreta — src/, tests/, etc.]

## Rastreamento de Complexidade
| Violação | Por que é necessária | Alternativa mais simples rejeitada porque |
|----------|----------------------|-------------------------------------------|
| [...]    | [...]                | [...]                                      |
```

---

## Template: tasks.md

```markdown
# Tarefas: [FEATURE]
Formato: `[ID] [P?] [História] Descrição` — [P] = paralelizável.

## Fase 1: Setup
- [ ] T001 Criar estrutura do projeto conforme o plano
- [ ] T002 Inicializar projeto [linguagem] com [framework]

## Fase 2: Foundational (bloqueante — nenhuma história começa antes)
- [ ] T004 Schema do banco / migrações
- [ ] T005 [P] Autenticação/autorização

## Fase 3: História 1 - [Título] (P1) — MVP
### Testes (se pedido, escrever antes e ver falhar)
- [ ] T010 [P] [US1] Teste de [jornada]
### Implementação
- [ ] T012 [P] [US1] Modelo [Entidade] em src/models/...
- [ ] T013 [US1] Serviço em src/services/... (depende de T012)
**Checkpoint**: US1 funcional e testável sozinha.

## Fase Final: Polish
- [ ] TXXX Documentação, refatoração, performance, segurança

## Notas
- Modelos → serviços → endpoints. Cada história entregável de forma independente.
```
