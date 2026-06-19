# Tarefas: [NOME DA FEATURE]

**Entrada**: Documentos de design em `specs/[NNN-nome-da-feature]/`
**Pré-requisitos**: plan.md (obrigatório), spec.md (histórias), research.md,
data-model.md, contracts/

**Testes**: tarefas de teste são OPCIONAIS — inclua só se a spec pediu testes.
**Organização**: tarefas agrupadas por história de usuário, para implementação
e teste independentes.

## Formato: `[ID] [P?] [História] Descrição`
- **[P]**: pode rodar em paralelo (arquivos diferentes, sem dependência)
- **[História]**: a qual história pertence (US1, US2...)
- Inclua o caminho exato do arquivo em cada tarefa

---

## Fase 1: Setup (infra compartilhada)
- [ ] T001 Criar estrutura do projeto conforme o plano
- [ ] T002 Inicializar projeto [linguagem] com dependências [framework]
- [ ] T003 [P] Configurar lint e formatação

## Fase 2: Foundational (pré-requisitos bloqueantes)
> CRÍTICO: nenhuma história começa até esta fase terminar.
- [ ] T004 Schema do banco e framework de migração
- [ ] T005 [P] Autenticação/autorização
- [ ] T006 [P] Roteamento e middleware
- [ ] T007 Modelos-base usados por todas as histórias
- [ ] T008 Tratamento de erros e logging

**Checkpoint**: fundação pronta — histórias podem começar.

## Fase 3: História 1 - [Título] (P1) 🎯 MVP
**Objetivo**: [o que entrega]
**Teste independente**: [como validar isolada]

### Testes US1 (OPCIONAL — só se pedido) ⚠️ escrever ANTES e ver falhar
- [ ] T010 [P] [US1] Teste de contrato de [endpoint] em tests/...
- [ ] T011 [P] [US1] Teste de integração de [jornada] em tests/...

### Implementação US1
- [ ] T012 [P] [US1] Criar modelo [Entidade] em src/models/...
- [ ] T013 [US1] Implementar [Serviço] em src/services/... (depende de T012)
- [ ] T014 [US1] Implementar [endpoint/feature] em src/...
- [ ] T015 [US1] Validação e tratamento de erro

**Checkpoint**: US1 totalmente funcional e testável sozinha.

## Fase 4: História 2 - [Título] (P2)
[mesmo padrão da Fase 3]

## Fase 5: História 3 - [Título] (P3)
[mesmo padrão]

## Fase Final: Polish & Cross-Cutting
- [ ] TXXX [P] Atualizar documentação em docs/
- [ ] TXXX Refatoração e limpeza
- [ ] TXXX Otimização de performance
- [ ] TXXX Hardening de segurança
- [ ] TXXX Rodar validação do quickstart.md

---

## Dependências e Ordem de Execução
- **Setup** -> sem dependências.
- **Foundational** -> depende do Setup; BLOQUEIA todas as histórias.
- **Histórias (P1, P2, P3)** -> dependem da Foundational; depois podem ir em
  paralelo (se houver gente) ou em ordem de prioridade.
- **Polish** -> depois das histórias desejadas.

### Dentro de cada história
Testes (se houver) falham antes -> modelos -> serviços -> endpoints ->
integração. Conclua a história antes de ir para a próxima prioridade.

## Estratégia de Entrega
1. Setup + Foundational -> fundação pronta.
2. US1 -> testar isolada -> entregar (MVP!).
3. US2 -> testar isolada -> entregar.
4. US3 -> testar isolada -> entregar.
Cada história adiciona valor sem quebrar as anteriores.

## Notas
- [P] = arquivos diferentes, sem dependência.
- Cada história deve ser completável e testável de forma independente.
- Commit por tarefa ou grupo lógico.
- Evite: tarefas vagas, conflito no mesmo arquivo, dependências cruzadas que
  quebram a independência das histórias.
