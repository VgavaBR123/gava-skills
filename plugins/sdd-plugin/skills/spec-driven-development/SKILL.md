---
name: spec-driven-development
description: >-
  Orienta o desenvolvimento de software pela metodologia Spec-Driven Development
  (SDD), baseada no GitHub spec-kit. Use quando o usuário quiser planejar ou
  construir uma feature/projeto de forma estruturada antes de codar — por
  fases: constituição (princípios), especificação (o quê/porquê),
  clarificação, plano técnico, quebra em tarefas, análise de consistência e
  implementação. Gatilhos: "spec-driven", "SDD", "spec-kit", "criar a spec",
  "fazer o plano técnico", "quebrar em tarefas", "começar um projeto do zero
  de forma estruturada", "specify/plan/tasks/implement". Genérica — independe
  de linguagem ou framework.
---

# Spec-Driven Development (SDD)

## O que é

Spec-Driven Development inverte o fluxo tradicional: a **especificação deixa de
ser rascunho descartável e vira o artefato central** que dirige o código. Em
vez de "vibe coding" peça por peça, o trabalho avança em fases curtas e
verificáveis, cada uma produzindo um documento que a fase seguinte consome.

Esta skill replica o fluxo do GitHub spec-kit (https://github.com/github/spec-kit)
de forma genérica (sem depender da CLI `specify` nem de linguagem específica).

## Princípios que governam o fluxo

- **Intenção antes de implementação**: defina o *quê* e o *porquê* antes do *como*.
- **Refinamento em múltiplos passos**, não geração de código de um tiro só.
- **Cada artefato é um portão (gate)**: só avance quando o anterior estiver sólido.
- **Marque o que está vago** com `[NEEDS CLARIFICATION: ...]` em vez de adivinhar.
- **Histórias independentes e testáveis**: cada uma deve, sozinha, entregar valor (MVP).
- **Rastreabilidade**: requisitos -> tarefas devem ser conectáveis.

## As fases (ordem padrão)

Execute as fases em ordem. Não pule um portão sem o usuário confirmar. Cada
fase produz um arquivo dentro de `specs/<NNN-nome-da-feature>/`.

### 0. Constituição — `constitution.md` (uma vez por projeto)
Estabeleça os princípios de engenharia do projeto: qualidade de código, padrão
de testes, consistência de UX, performance, segurança e como esses princípios
guiam decisões. Use `templates/constitution-template.md`. Este arquivo vira a
referência que todas as fases seguintes devem respeitar. Em projeto já
existente, apenas confirme/atualize.

### 1. Especificação — `spec.md`
Capture **o quê** e **o porquê**, nunca a stack. Use `templates/spec-template.md`.
Inclui: histórias de usuário priorizadas (P1, P2...) e independentemente
testáveis, requisitos funcionais (FR-001...), entidades-chave, critérios de
sucesso mensuráveis e tecnologicamente neutros (SC-001...), edge cases e
premissas. Tudo que estiver indefinido recebe `[NEEDS CLARIFICATION]`.

### 2. Clarificação — atualiza `spec.md` (recomendado antes do plano)
Faça ao usuário perguntas sequenciais por cobertura para resolver os
`[NEEDS CLARIFICATION]` e ambiguidades. Registre as respostas numa seção
`## Clarifications` da spec. Só pule se o usuário declarar explicitamente que é
um protótipo exploratório. Para perguntas de múltipla escolha use a ferramenta
de perguntas do Cowork (AskUserQuestion) quando disponível.

### 3. Plano técnico — `plan.md` (+ artefatos de design)
Agora sim defina a stack e a arquitetura. Use `templates/plan-template.md`.
Preencha o Contexto Técnico (linguagem, dependências, storage, testes,
plataforma, metas de performance, escala). Rode o **Constitution Check**: o
plano viola algum princípio da constituição? Se sim, justifique na tabela de
Complexity Tracking ou simplifique. Quando útil, gere artefatos de apoio:
`research.md` (decisões de tecnologia), `data-model.md` (entidades), `contracts/`
(APIs/interfaces) e `quickstart.md` (como rodar/validar).

### 4. Tarefas — `tasks.md`
Quebre o plano em tarefas acionáveis e ordenadas. Use `templates/tasks-template.md`.
Regras: organizar **por história de usuário** (cada uma um incremento de MVP);
respeitar dependências (modelos -> serviços -> endpoints); marcar com `[P]` o que
roda em paralelo (arquivos diferentes, sem dependência); incluir o caminho
exato de cada arquivo; se testes foram pedidos, criar tarefas de teste primeiro
(devem falhar antes da implementação — TDD). Fases típicas: Setup ->
Foundational (bloqueante) -> US1 (P1, MVP) -> US2 -> US3 -> Polish.

### 5. Análise — relatório de consistência (opcional, antes de implementar)
Faça uma checagem cruzada entre `spec.md`, `plan.md` e `tasks.md`: toda
história tem tarefas? todo requisito está coberto? há tarefa órfã sem
requisito? há over-engineering versus a constituição? Reporte lacunas ao
usuário antes de codar. Para trabalho de alto risco, use um subagente de
verificação.

### 6. Implementação — código
Só comece com constituição, spec, plan e tasks prontos. Execute as tarefas na
ordem, respeitando dependências e marcadores `[P]`. Siga TDD se definido.
Valide cada checkpoint (cada história deve funcionar isoladamente). Faça commit
por tarefa ou grupo lógico. Ao final, rode o `quickstart.md` e corrija erros de
runtime.

## Como conduzir (regras de operação)

1. **Descubra em que fase o usuário está.** Projeto novo -> comece na
   constituição. Já tem spec -> vá para clarificação/plano. Pergunte se não
   estiver claro.
2. **Um portão por vez.** Ao terminar uma fase, mostre o artefato, peça
   validação e só então avance. Não gere spec, plano e código tudo de uma vez.
3. **Numere as features.** Cada feature vive em `specs/NNN-nome/` (ex.:
   `specs/001-login/`). Use branch sugerida `NNN-nome`.
4. **Não invente requisitos.** Marque `[NEEDS CLARIFICATION]` e pergunte.
5. **Mantenha a spec neutra de tecnologia.** Stack só entra no plano.
6. **Respeite a constituição** em todas as fases; ela vence preferências
   pessoais e "esperteza" do agente.
7. **Crie os arquivos de verdade** na pasta do usuário usando os templates de
   `templates/`, substituindo todos os placeholders `[...]`.

## Arquivos desta skill

- `templates/constitution-template.md` — princípios do projeto
- `templates/spec-template.md` — especificação funcional
- `templates/plan-template.md` — plano técnico e estrutura
- `templates/tasks-template.md` — quebra em tarefas
- `reference/workflow.md` — fluxo resumido e checklist de portões

Ao criar um artefato, leia o template correspondente, copie a estrutura e
preencha com o conteúdo real do projeto — removendo comentários de instrução e
opções não usadas.
