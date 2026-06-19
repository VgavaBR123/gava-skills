# Plano de Implementação: [FEATURE]

**Branch**: `[NNN-nome-da-feature]` | **Data**: [DATA] | **Spec**: [link para spec.md]
**Entrada**: Especificação em `specs/[NNN-nome-da-feature]/spec.md`

## Resumo
[Requisito principal extraído da spec + abordagem técnica resumida]

## Contexto Técnico
**Linguagem/Versão**: [ex.: Python 3.11, Node 20, Go 1.22 ou NEEDS CLARIFICATION]
**Dependências principais**: [ex.: FastAPI, React, Gin ou NEEDS CLARIFICATION]
**Armazenamento**: [ex.: PostgreSQL, SQLite, arquivos ou N/A]
**Testes**: [ex.: pytest, Jest, go test ou NEEDS CLARIFICATION]
**Plataforma alvo**: [ex.: servidor Linux, navegador, iOS 15+ ou NEEDS CLARIFICATION]
**Tipo de projeto**: [biblioteca/cli/web/mobile/desktop ou NEEDS CLARIFICATION]
**Metas de performance**: [ex.: 1000 req/s, 60 fps ou NEEDS CLARIFICATION]
**Restrições**: [ex.: p95 < 200ms, < 100MB memória, offline ou NEEDS CLARIFICATION]
**Escala/Escopo**: [ex.: 10k usuários, 50 telas ou NEEDS CLARIFICATION]

## Constitution Check
*PORTÃO: deve passar antes da fase de pesquisa. Re-checar após o design.*

[Liste cada princípio da constituição e marque se o plano o respeita. Qualquer
violação vai para "Rastreamento de Complexidade" com justificativa — ou o plano
é simplificado.]

## Estrutura do Projeto

### Documentação (desta feature)
```text
specs/[NNN-feature]/
├── plan.md          # Este arquivo
├── research.md      # Decisões de tecnologia (Fase 0)
├── data-model.md    # Entidades e relações (Fase 1)
├── quickstart.md    # Como rodar/validar (Fase 1)
├── contracts/       # APIs/interfaces (Fase 1)
└── tasks.md         # Tarefas (gerado na fase de Tarefas)
```

### Código-Fonte (raiz do repositório)
> Substitua pela estrutura real. Remova as opções não usadas.

```text
# Opção 1: Projeto único (PADRÃO)
src/
├── models/
├── services/
└── lib/
tests/
├── integration/
└── unit/

# Opção 2: Aplicação web (frontend + backend)
backend/  (src/, tests/)
frontend/ (src/, tests/)

# Opção 3: Mobile + API
api/
ios/ ou android/
```

**Decisão de Estrutura**: [documente a estrutura escolhida e os diretórios reais]

## Rastreamento de Complexidade
> Preencher SÓ se o Constitution Check tiver violações que precisam justificativa.

| Violação | Por que é necessária | Alternativa mais simples rejeitada porque |
|----------|----------------------|-------------------------------------------|
| [ex.: 4º serviço] | [necessidade atual] | [por que 3 não bastam] |
