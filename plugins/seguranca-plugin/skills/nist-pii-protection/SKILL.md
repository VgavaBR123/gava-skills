---
name: nist-pii-protection
description: "Base de conhecimento do NIST SP 800-122 — Guide to Protecting the Confidentiality of Personally Identifiable Information (PII). Use ao classificar PII por nível de risco (baixo/moderado/alto), decidir entre de-identificação (reversível) e anonimização (irreversível), escolher salvaguardas proporcionais (controles NIST SP 800-53), aplicar os Fair Information Practices, ou planejar resposta a incidentes com dados pessoais. Complementa a skill auditoria-lgpd-fiscal dando o método NIST por trás da classificação de PII e da severidade dos achados (CPF/CNPJ, LGPD)."
license: CC-BY-SA-4.0
---

<!-- argument-hint: [tópico, ex.: "níveis de impacto", "anonimização", ou "ch03"] -->

# NIST SP 800-122 — Proteção da Confidencialidade de PII
**Autores**: E. McCallister, T. Grance, K. Scarfone (NIST) | **Páginas**: ~59 | **Capítulos**: 5 | **Gerado**: 2026-06-19 | **Fonte**: domínio público (nvlpubs.nist.gov)

## Como usar esta skill

- **Sem argumento** — carrega os frameworks centrais (classificação e salvaguardas).
- **Com um tópico** — pergunte sobre `níveis de impacto`, `de-identificação`,
  `Fair Information Practices`; eu leio o capítulo relevante.
- **Com capítulo** — peça `ch03` para mergulhar nas salvaguardas.
- **Navegar** — pergunte "quais capítulos você tem?".

Esta é uma skill **de referência**, complementar à `auditoria-lgpd-fiscal`: ela
fornece o **método NIST** por trás da classificação de PII e da calibração da
severidade dos achados.

---

## Frameworks centrais

### 1. Abordagem baseada em risco (princípio mestre)
"Se guardarmos escovas de dente e diamantes com igual zelo, perderemos mais
diamantes." **Proteja proporcionalmente ao dano** — não trate todo CPF igual.

### 2. Definição ampla de PII (duas pontas)
PII = informação que (1) **distingue/rastreia** um indivíduo **ou** (2) é
**vinculada/vinculável** a ele. Inclui IP/MAC, identificadores parciais e
**combinações**. *Linked* (fonte próxima sem segregação) vs. *linkable* (fonte
remota/pública) é o que decide reidentificação. → Ch 1.

### 3. Três níveis de impacto + 6 fatores
Classifique cada instância de PII em **BAIXO / MODERADO / ALTO** (FIPS 199) pelos
fatores **Identifiability, Quantity (só eleva), Field Sensitivity, Context of
Use, Obligation to Protect, Access/Location**, avaliados **em conjunto**. Mesmo
campo recebe níveis diferentes pelo **contexto**. → Ch 2.

### 4. De-identificação ≠ Anonimização (distinção crítica)
- **De-identificação**: reversível (existe código/chave/tabela). Hash/HMAC com
  tabela de/para entra aqui → **continua sendo dado pessoal sob a LGPD**.
- **Anonimização**: associação de reidentificação **não existe mais** →
  deixa de ser PII. Usa generalização, supressão, ruído, swapping, média.
→ Ch 3. *(É a ponte direta com a tese da `auditoria-lgpd-fiscal`.)*

### 5. Salvaguardas em três camadas
**Operacional** (políticas + awareness/training/education) + **Privacidade**
(minimização, PIA, de-id/anon) + **Segurança** (controles NIST SP 800-53:
AC-3/5/6/17/19, AU-2/6, IA-2, MP-2..6, SC-9/28, SI-4). → Ch 3.

### 6. Fair Information Practices (OECD) ↔ LGPD Art. 6º
Os 8 princípios (Collection/Use Limitation, Purpose Specification, Data Quality,
Security Safeguards, Openness, Individual Participation, Accountability) são a
base legal; mapeiam quase 1:1 com a LGPD. → Ch 5.

---

## Índice de capítulos

| # | Título | Frameworks-chave |
|---|--------|------------------|
| [ch01](chapters/ch01-identificar-pii.md) | Identificar e localizar PII | Definição de PII, distinguish/trace, linked/linkable, PTA |
| [ch02](chapters/ch02-niveis-de-impacto.md) | Níveis de impacto | Low/Moderate/High, 6 fatores, 3 cenários |
| [ch03](chapters/ch03-salvaguardas.md) | Salvaguardas | Minimização, PIA, de-id vs. anon, controles SP 800-53 |
| [ch04](chapters/ch04-resposta-a-incidentes.md) | Resposta a incidentes | 4 fases, notificação, preservação de prova |
| [ch05](chapters/ch05-fair-information-practices.md) | Fair Information Practices | 8 princípios OECD, ponte com a LGPD |

## Índice de tópicos
- **Anonimização / De-identificação** → ch03
- **Classificação / severidade de PII** → ch02
- **Controles de segurança (AC/MP/SC/AU/IA)** → ch03
- **Fair Information Practices / OECD** → ch05
- **Identificar PII / inventário** → ch01
- **Linked vs. linkable / reidentificação** → ch01, ch02
- **Minimização / minimum necessary** → ch03, ch05
- **Níveis de impacto (low/moderate/high)** → ch02
- **Resposta a incidentes / breach** → ch04
- **PIA / PTA** → ch01, ch03

## Arquivos de apoio
- [glossary.md](glossary.md) — termos-chave com definições e capítulo
- [patterns.md](patterns.md) — técnicas (inventário, classificação, de-id/anon, resposta)
- [cheatsheet.md](cheatsheet.md) — tabelas de decisão e mapa para as fases da auditoria

---

## Escopo e limites

Cobre o conteúdo do NIST SP 800-122 (2010, domínio público), orientado ao
contexto federal dos EUA. Para aplicação à **LGPD**, use junto da skill
`auditoria-lgpd-fiscal` e confirme prazos/obrigações regulatórias atuais com a
ANPD — esta skill é referência técnica, não parecer jurídico. Para criptografia
aplicada (AES-GCM, HMAC) a fundo, veja as obras de cripto da coletânea
(Boneh-Shoup, Serious Cryptography).
