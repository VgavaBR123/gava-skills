# Constituição do Projeto: [NOME DO PROJETO]

**Versão**: 1.0.0 | **Ratificada em**: [DATA] | **Última alteração**: [DATA]

> A constituição define os princípios inegociáveis que governam TODAS as fases
> seguintes (spec, plano, tarefas, implementação). Em caso de conflito, ela vence.

## Princípios Fundamentais

### I. Qualidade de Código
[Ex.: Código deve ser legível e revisado antes do merge. Sem funções com mais de
N responsabilidades. Lint e formatação automáticos obrigatórios.]

### II. Padrão de Testes
[Ex.: Toda lógica de negócio tem teste automatizado. TDD para fluxos críticos —
o teste é escrito e falha antes da implementação. Cobertura mínima de X%.]

### III. Consistência de UX
[Ex.: Padrões de interface e mensagens de erro consistentes. Acessibilidade
mínima AA. Comportamento previsível entre telas.]

### IV. Performance
[Ex.: Metas explícitas (p95 < Xms, memória < Y). Otimizar só com medição, nunca
por suposição.]

### V. Segurança e Dados
[Ex.: Validação de entrada em toda fronteira. Segredos nunca no código. Princípio
do menor privilégio.]

## Restrições e Padrões Organizacionais
[Ex.: cloud provider obrigatório, stacks aprovadas, licenças permitidas,
requisitos de compliance/regulatórios.]

## Fluxo de Desenvolvimento
[Ex.: toda feature passa pelo fluxo SDD; PRs exigem revisão; CI verde antes do
merge; a constituição é checada na fase de plano (Constitution Check).]

## Governança
- Esta constituição se sobrepõe a preferências individuais.
- Emendas exigem: justificativa documentada, aprovação e atualização da versão.
- Versionamento semântico: MAJOR (remoção/redefinição de princípio),
  MINOR (novo princípio/seção), PATCH (esclarecimento).
- Toda fase de plano DEVE rodar o Constitution Check contra este documento.
