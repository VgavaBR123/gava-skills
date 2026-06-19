# Especificação de Feature: [NOME DA FEATURE]

**Branch da feature**: `[NNN-nome-da-feature]`
**Criada em**: [DATA]
**Status**: Rascunho
**Entrada**: Descrição do usuário: "[texto original do pedido]"

## Cenários de Usuário e Testes *(obrigatório)*

> Histórias devem ser PRIORIZADAS como jornadas ordenadas por importância.
> Cada história deve ser INDEPENDENTEMENTE TESTÁVEL: se você implementar só uma
> delas, ainda assim tem um MVP que entrega valor. Use prioridades P1, P2, P3...
> (P1 = mais crítica).

### História 1 - [Título Breve] (Prioridade: P1)

[Descreva a jornada em linguagem simples]

**Por que esta prioridade**: [valor entregue e razão da prioridade]

**Teste independente**: [como validar isolada — ex.: "testável fazendo X e
entregando Y"]

**Cenários de Aceite**:
1. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]
2. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]

---

### História 2 - [Título Breve] (Prioridade: P2)

[Descreva a jornada]

**Por que esta prioridade**: [...]
**Teste independente**: [...]
**Cenários de Aceite**:
1. **Dado** [...], **Quando** [...], **Então** [...]

---

[Adicione mais histórias conforme necessário, cada uma com prioridade]

### Edge Cases
- O que acontece quando [condição de borda]?
- Como o sistema lida com [cenário de erro]?

## Requisitos *(obrigatório)*

### Requisitos Funcionais
- **FR-001**: O sistema DEVE [capacidade específica]
- **FR-002**: O sistema DEVE [capacidade específica]
- **FR-003**: Usuários DEVEM conseguir [interação-chave]
- **FR-004**: O sistema DEVE [requisito de dados]

*Exemplo de requisito ainda indefinido:*
- **FR-00X**: O sistema DEVE autenticar via [NEEDS CLARIFICATION: método não
  especificado — e-mail/senha, SSO, OAuth?]

### Entidades-Chave *(se a feature envolve dados)*
- **[Entidade 1]**: [o que representa, atributos-chave sem detalhe de implementação]
- **[Entidade 2]**: [o que representa, relações com outras entidades]

## Critérios de Sucesso *(obrigatório)*

> Devem ser mensuráveis e NEUTROS de tecnologia.

### Resultados Mensuráveis
- **SC-001**: [ex.: "Usuário completa o cadastro em menos de 2 minutos"]
- **SC-002**: [ex.: "Sistema suporta 1000 usuários simultâneos sem degradação"]
- **SC-003**: [ex.: "90% dos usuários completam a tarefa principal na 1ª tentativa"]

## Premissas
- [Premissa sobre usuários-alvo]
- [Premissa sobre limites de escopo — ex.: "mobile fora do escopo da v1"]
- [Dependência de sistema/serviço existente]

## Clarifications
> Preenchida na fase de clarificação. Registre as perguntas resolvidas.
- **[DATA]** — P: [pergunta] / R: [resposta do usuário]
