# Sintaxe EARS — Easy Approach to Requirements Syntax

EARS é uma linguagem natural **restrita** para escrever requisitos sem
ambiguidade. Criada por Alistair Mavin e engenheiros da Rolls-Royce para
sistemas aeronáuticos críticos, ela força cada requisito a um de cinco padrões
fixos. Isso reduz furos de tradução e permite que o agente de IA gere testes e
lógica corretos na primeira tentativa, em vez de "adivinhar".

**Regra desta skill:** todo requisito funcional (FR-00X) do `spec.md` deve ser
escrito em um dos cinco padrões abaixo.

## Os cinco padrões

| Padrão | Quando usar | Forma | Exemplo |
|--------|-------------|-------|---------|
| **Ubíquo** | comportamento sempre ativo, sem condição | O `<sistema>` DEVE `<resposta>` | O sistema DEVE criptografar dados de cartão com RSA-4096 antes do tráfego. |
| **Dirigido por Evento** | resposta a um gatilho instantâneo | QUANDO `<gatilho>`, o `<sistema>` DEVE `<resposta>` | QUANDO o usuário clica em "Estornar", o sistema DEVE reverter o valor na conta. |
| **Dirigido por Estado** | ativo enquanto durar uma condição | ENQUANTO `<estado>`, o `<sistema>` DEVE `<resposta>` | ENQUANTO o app estiver offline, o sistema DEVE enfileirar as transações. |
| **Comportamento Indesejado** | erros, falhas, exceções | SE `<condição de erro>`, ENTÃO o `<sistema>` DEVE `<resposta>` | SE a autenticação expirar após 5s, ENTÃO o sistema DEVE retornar erro de timeout. |
| **Opcional** | só vale quando um recurso está habilitado | ONDE `<recurso ativo>`, o `<sistema>` DEVE `<resposta>` | ONDE a biometria estiver habilitada, o sistema DEVE solicitar a digital no app. |

## Requisitos complexos

Padrões podem ser combinados em uma só sentença, na ordem
pré-condição → gatilho → estado:

> ENQUANTO `<estado>`, QUANDO `<gatilho>`, o `<sistema>` DEVE `<resposta>`.

Use só quando necessário — prefira requisitos simples e atômicos.

## Checklist rápido por requisito

- [ ] Encaixa em exatamente um dos cinco padrões (ou é um complexo justificado)?
- [ ] O `<sistema>` é nomeado (não "o app" genérico quando há subsistemas)?
- [ ] A `<resposta>` é observável/verificável (vira teste)?
- [ ] Sem "e/ou" escondendo dois requisitos numa frase só? (separe em dois FRs)
- [ ] Neutro de tecnologia (sem citar framework/stack)?
