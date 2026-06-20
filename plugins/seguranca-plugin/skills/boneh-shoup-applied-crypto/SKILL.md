---
name: boneh-shoup-applied-crypto
description: "Base de conhecimento de 'A Graduate Course in Applied Cryptography' (Dan Boneh & Victor Shoup). Use ao raciocinar sobre criptografia aplicada com rigor: segurança semântica, ataques CPA/CCA, encriptação autenticada (AEAD/AES-GCM) e unicidade de nonce, integridade de mensagem (MAC/HMAC, hashes universais, GHASH), resistência a colisão, criptografia de chave pública (RSA, curvas elípticas), assinaturas digitais, troca de chaves autenticada e provas de conhecimento-zero. Dá a fundamentação teórica por trás dos achados de cripto da skill auditoria-lgpd-fiscal (HMAC, AES-256-GCM)."
license: CC-BY-SA-4.0
---

<!-- argument-hint: [tópico, ex.: "AES-GCM", "nonce", "HMAC", ou "ch09"] -->

# A Graduate Course in Applied Cryptography
**Autores**: Dan Boneh & Victor Shoup | **Páginas**: ~900 | **Capítulos**: 21 (de 23; ver limites) | **Gerado**: 2026-06-20 | **Fonte**: livre/legal (toc.cryptobook.us)

## Como usar esta skill

- **Sem argumento** — carrega os modelos mentais centrais de criptografia aplicada.
- **Com um tópico** — pergunte sobre `AES-GCM`, `nonce`, `HMAC`, `CCA`, `assinatura`; eu leio o capítulo relevante.
- **Com capítulo** — peça `ch09` para mergulhar em encriptação autenticada.
- **Navegar** — pergunte "quais capítulos você tem?".

Skill **de referência teórica**, complementar à `auditoria-lgpd-fiscal`: fundamenta
*por que* um nonce repetido ou um MAC ausente quebram o sistema — transformando o
checklist da auditoria em julgamento técnico.

---

## Frameworks centrais

### Segurança definida por jogos (Attack Games)
A segurança é provada por um **jogo entre adversário e desafiante** e uma
*advantage* desprezível. Pense em todo esquema como "qual jogo o atacante precisa
vencer, e qual o bound da vantagem dele". É a régua de todos os capítulos.

### Encriptação: segurança semântica e CPA/CCA
- **Segurança semântica**: o cifrado não revela nada sobre a mensagem.
- **CPA (chosen-plaintext)**: segurança mesmo se o atacante escolhe textos a cifrar — exige cifra **randomizada ou com nonce** (cap. 5).
- **CCA (chosen-ciphertext)**: o padrão-ouro — segurança mesmo se o atacante obtém decifragens. **Cifra sem integridade não é CCA-segura.** → exige encriptação autenticada (cap. 9, 12).

### Integridade de mensagem (MAC)
- **MAC / PRF**: tag que só quem tem a chave produz. **HMAC** e MACs de bloco (CMAC/PMAC).
- **Hashes universais (UHF)** + PRF = **Carter-Wegman MAC** (cap. 7); **GHASH** é o UHF do GCM.
- **Resistência a colisão** (cap. 8): base de assinaturas e de hash-then-sign; ataque do aniversário.

### Encriptação autenticada (AEAD) — o ponto crítico da auditoria
Confidencialidade **+** integridade juntas. **AES-GCM** = CTR + GHASH.
- **Unicidade do nonce é inegociável**: nonce repetido em GCM vaza o keystream e **a chave de autenticação** → forja total. (cap. 9)
- **Encrypt-then-MAC** é a composição genérica correta.

### Chave pública, assinaturas e protocolos
- **Ferramentas e encriptação de chave pública** (RSA, ElGamal; cap. 10–12), **assinaturas digitais** (cap. 13–14), **curvas elípticas e pairings** (cap. 15).
- **Troca de chaves autenticada** (cap. 21), **identificação/Sigma/zero-knowledge** (cap. 18–20), **threshold e MPC** (cap. 22–23).

---

## Índice de capítulos

| # | Título | Arquivo |
|---|--------|---------|
| 2 | Encryption (segurança semântica) | [ch02](chapters/ch02-encryption.md) |
| 3 | Stream ciphers (PRG) | [ch03](chapters/ch03-stream-ciphers.md) |
| 4 | Block ciphers (PRF/PRP, AES) | [ch04](chapters/ch04-block-ciphers.md) |
| 5 | Chosen Plaintext Attack (CPA) | [ch05](chapters/ch05-chosen-plaintext-attack.md) |
| 6 | Message integrity (MAC) | [ch06](chapters/ch06-message-integrity.md) |
| 7 | Integrity from universal hashing (Carter-Wegman, GHASH) | [ch07](chapters/ch07-message-integrity-from-universal.md) |
| 8 | Integrity from collision resistant hashing | [ch08](chapters/ch08-message-integrity-from-collision.md) |
| 9 | Authenticated Encryption (AEAD, AES-GCM) | [ch09](chapters/ch09-authenticated-encryption.md) |
| 10 | Public key tools | [ch10](chapters/ch10-public-key-tools.md) |
| 11 | Public key encryption | [ch11](chapters/ch11-public-key-encryption.md) |
| 12 | Chosen ciphertext secure PKE (CCA) | [ch12](chapters/ch12-chosen-ciphertext-secure-public-key.md) |
| 13 | Digital signatures | [ch13](chapters/ch13-digital-signatures.md) |
| 14 | Fast hash-based signatures | [ch14](chapters/ch14-fast-hash-based-signatures.md) |
| 15 | Elliptic curve cryptography and pairings | [ch15](chapters/ch15-elliptic-curve-cryptography-and.md) |
| 16 | Attacks on number theoretic assumptions | [ch16](chapters/ch16-attacks-on-number-theoretic.md) |
| 18 | Protocols for identification and login | [ch18](chapters/ch18-protocols-for-identification-and-login.md) |
| 19 | Identification/signatures from Sigma protocols | [ch19](chapters/ch19-identification-and-signatures-from.md) |
| 20 | Proving properties in zero-knowledge | [ch20](chapters/ch20-proving-properties-in-zero-knowledge.md) |
| 21 | Authenticated Key Exchange | [ch21](chapters/ch21-authenticated-key-exchange.md) |
| 22 | Threshold cryptography | [ch22](chapters/ch22-threshold-cryptography.md) |
| 23 | Secure multi-party computation | [ch23](chapters/ch23-secure-multi-party-computation.md) |

## Índice de tópicos
- **AEAD / Encriptação autenticada** → ch09, ch12
- **AES / block ciphers / PRF / PRP** → ch04
- **AES-GCM / GHASH / hash universal** → ch07, ch09
- **Assinaturas digitais** → ch13, ch14
- **CCA (chosen-ciphertext)** → ch12
- **CPA (chosen-plaintext)** → ch05
- **Curvas elípticas / pairings** → ch15
- **HMAC / MAC / integridade** → ch06, ch07
- **Nonce / unicidade** → ch07, ch09
- **PRG / stream ciphers** → ch03
- **Resistência a colisão / ataque do aniversário** → ch08
- **RSA / chave pública** → ch10, ch11, ch12
- **Segurança semântica** → ch02
- **Troca de chaves autenticada** → ch21
- **Zero-knowledge / Sigma / identificação** → ch18, ch19, ch20
- **Threshold / MPC** → ch22, ch23

## Arquivos de apoio
- [glossary.md](glossary.md) — termos-chave com definições e capítulo
- [patterns.md](patterns.md) — construções e técnicas criptográficas
- [cheatsheet.md](cheatsheet.md) — regras de decisão e tabelas de design

---

## Escopo e limites

Cobre 21 dos 23 capítulos do livro. **Não incluídos**: cap. 1 (Introdução/cifras
históricas) e cap. 17 (criptografia pós-quântica de reticulados — parcialmente
absorvido no cap. 16). O texto foi extraído por `pdftotext`, então **fórmulas e
provas podem conter imprecisões** de extração — para o enunciado matemático exato,
consulte o PDF oficial. Esta skill é um *toolkit de conceitos e decisões*, não
substitui o livro. Para a aplicação prática em código Python/SQL sob LGPD, use
junto da `auditoria-lgpd-fiscal` (Fases 3 — HMAC; 4 — AES-256-GCM).
