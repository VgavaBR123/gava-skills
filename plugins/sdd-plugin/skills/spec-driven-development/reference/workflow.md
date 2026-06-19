# Fluxo SDD — resumo e checklist de portões

```
constitution -> specify -> clarify -> plan -> tasks -> analyze -> implement
   (princípios)  (o quê)   (resolver  (o como) (passos) (checar)  (codar)
                            dúvidas)
```

## Checklist de portões (não avance sem ✔)

### Portão 1 — depois da Especificação
- [ ] Toda história tem prioridade (P1, P2...) e é independentemente testável
- [ ] Existe pelo menos uma história P1 que sozinha vira MVP
- [ ] Requisitos funcionais numerados (FR-00X) e verificáveis
- [ ] Critérios de sucesso mensuráveis e neutros de tecnologia
- [ ] Nenhum `[NEEDS CLARIFICATION]` pendente OU registrado para a fase de clarify
- [ ] A spec NÃO menciona stack/tecnologia

### Portão 2 — depois do Plano
- [ ] Contexto técnico preenchido (linguagem, deps, storage, testes, plataforma)
- [ ] Constitution Check passou (ou violações justificadas em Complexity Tracking)
- [ ] Estrutura de pastas concreta definida
- [ ] research.md / data-model.md / contracts gerados quando aplicável

### Portão 3 — depois das Tarefas
- [ ] Tarefas agrupadas por história de usuário
- [ ] Dependências corretas (modelos -> serviços -> endpoints)
- [ ] Paralelizáveis marcadas com [P]
- [ ] Caminho exato de arquivo em cada tarefa
- [ ] Se testes pedidos: tarefas de teste antes da implementação (TDD)

### Portão 4 — depois da Análise (antes de codar)
- [ ] Cada história tem tarefas que a cobrem
- [ ] Cada requisito (FR) está coberto por ao menos uma tarefa
- [ ] Sem tarefa órfã (sem requisito correspondente)
- [ ] Sem over-engineering versus a constituição

## Onde ficam os arquivos
```
.
├── constitution.md            # ou .specify/memory/constitution.md
└── specs/
    └── NNN-nome-da-feature/
        ├── spec.md
        ├── plan.md
        ├── research.md
        ├── data-model.md
        ├── quickstart.md
        ├── contracts/
        └── tasks.md
```

## Dica de uso com agente de IA
Peça uma fase por vez ("crie a spec", "agora o plano", "agora as tarefas").
Valide o artefato de cada fase antes de seguir. Não peça spec + código de uma vez.
