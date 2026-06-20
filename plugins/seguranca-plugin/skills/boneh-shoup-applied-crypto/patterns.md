# Padrões e construções — A Graduate Course in Applied Cryptography

## One-Time Pad (OTP)

**Quando usar**: Quando adversário tem poder computacional ilimitado mas apenas 1 mensagem será cifrada; chaves podem ser tão longas quanto mensagens.

**Como**: E(k,m) := k⊕m onde |k|=|m|=L. Decryption: D(k,c) := k⊕c. Chave k escolhida uniformemente de {0,1}^L.

**Trade-offs**: Perfeitamente seguro (Shannon) mas |K|≥|M| obrigatório; chave deve ser descartada após uso único; impraticável para comunicação contínua.

---

## Semantic Security (SS)

**Quando usar**: Sistemas práticos onde adversário é computacionalmente limitado e chaves curtas são necessárias.

**Como**: Cifra (E,D) onde adversário não distingue E(k,m₀) de E(k,m₁) com vantagem não-negligível (Attack Game 2.1). Formalizar via bit-guessing: SSadv*[A,E] = |Pr[^b=b] - 1/2|.

**Trade-offs**: Requer suposições computacionais (vs. perfect security); permite chaves curtas; base para sistemas reais mas não garante integridade.

---

## Security Reduction

**Quando usar**: Para provar segurança de construção X assumindo primitiva Y é segura.

**Como**: Construir adversário B (elementary wrapper de A) tal que Adv[A,X] ≤ Adv[B,Y]. Se Y é seguro (Adv negligível), então X é seguro.

**Trade-offs**: Prova modular e reutilizável; degradação de segurança (bounds concretos importam); requer primitiva base confiável.

---

## Pseudo-Random Generator (PRG)

**Quando usar**: Expandir seed curta em keystream longo para stream cipher; quando chaves curtas são obrigatórias.

**Como**: G: S → R deterministico onde G(s) é indistinguível de string aleatória (Attack Game 3.1). Stream cipher: E(s,m) := G(s)[0..|m|-1] ⊕ m.

**Trade-offs**: Semantic security se G é PRG seguro (Theorem 3.1); NUNCA reutilize seed (two-time pad vaza m₁⊕m₂); requer suposição computacional.

---

## Hybrid Argument

**Quando usar**: Provar segurança de composição (parallel/sequential PRG, multi-message encryption).

**Como**: Construir sequência Hybrid₀,...,Hybridₙ interpolando experimentos 0 e 1; mostrar adversário não distingue hybrids adjacentes; somar vantagens via desigualdade triangular.

**Trade-offs**: Degradação linear (n·ε); técnica de prova poderosa mas bounds podem ser loose; aplicável a múltiplos cenários.

---

## Block Cipher (AES/DES)

**Quando usar**: Primitiva base para modos de operação (CBC, CTR, GCM); quando permutação keyed é necessária.

**Como**: E:(K,X)→X onde E(k,·) é permutação para todo k. Iterar round cipher simples (S-boxes + mixing) até convergir (AES-128: 10 rounds).

**Trade-offs**: Exhaustive search bound (mínimo 128-bit keys); side-channels (timing, power); nunca implemente próprio; use AES-NI quando disponível.

---

## Electronic Codebook (ECB) Mode

**Quando usar**: APENAS para mensagens com blocos garantidamente distintos (ex: chaves aleatórias).

**Como**: E'(k,m) := (E(k,m[0]),...,E(k,m[v-1])). Cada bloco cifrado independentemente.

**Trade-offs**: Revela padrões (blocos idênticos → ciphertexts idênticos); inseguro para dados gerais; paralelizável; sem IV overhead.

---

## Randomized Counter Mode

**Quando usar**: CPA-secure encryption com paralelismo; quando PRF está disponível.

**Como**: x←X aleatório; c[j] := F(k, x+j mod N) ⊕ m[j] para j=0..v-1; output (x,c).

**Trade-offs**: Paralelizável; random access; requer N super-poly (birthday bound Q²/N); nonce-based variant elimina ciphertext expansion.

---

## CBC Mode

**Quando usar**: CPA-secure encryption quando block cipher é primitiva disponível; paralelismo não é crítico.

**Como**: c[0]←X (random IV); c[j+1] := E(k, c[j]⊕m[j]) para j=0..v-1.

**Trade-offs**: IV deve ser imprevisível (não apenas único); sequencial (não paraleliza encryption); decryption paralelizável; ciphertext stealing elimina padding.

---

## Message Authentication Code (MAC)

**Quando usar**: Garantir integridade de mensagens com chave secreta compartilhada; detectar adulteração.

**Como**: S(k,m)→t gera tag; V(k,m,t)→{accept,reject} verifica. Adversário não forja (m,t) válido após chosen message attack.

**Trade-offs**: Não provê confidencialidade; requer chave compartilhada; tags adicionam overhead; timing leaks se comparação não é constant-time.

---

## ECBC (Encrypted CBC-MAC)

**Quando usar**: MAC para mensagens longas usando block cipher; quando streaming é necessário.

**Como**: t←0^n; para i=1..v: t←F(k₁,aᵢ⊕t); output F(k₂,t). Usa duas chaves independentes.

**Trade-offs**: Streaming; tags ≥128 bits; segurança degrada Q²ℓ²/N (birthday); CMAC superior (evita dummy blocks).

---

## CMAC

**Quando usar**: MAC padrão NIST para block ciphers; melhor que ECBC.

**Como**: CBC com randomized prefix-free encoding via sub-keys k₁=L·X, k₂=L·X² em GF(2^n). Último bloco: aᵤ⊕k₁ se |m| múltiplo de n, senão aᵤ||100...0⊕k₂.

**Trade-offs**: Sem dummy blocks; streaming; overhead mínimo; requer aritmética GF(2^n); segurança Q²ℓ²/N.

---

## PMAC/PMAC0

**Quando usar**: MAC paralelizável; quando hardware paralelo disponível; edições locais frequentes.

**Como**: t←0^n; para i=1..v: t←t⊕F₁(k₁, aᵢ+i·k mod p); output F₂(k₂,t). Máscaras aditivas i·k.

**Trade-offs**: Paralelizável; incremental (editar bloco i sem reprocessar tudo); requer aritmética modular; segurança Q²ℓ/N.

---

## Universal Hash Function (UHF)

**Quando usar**: Building block para MACs via hash-then-PRF; quando colisões devem ser raras sem conhecer chave.

**Como**: H(k,m) onde Pr[H(k,m₀)=H(k,m₁)] ≤ ε para m₀≠m₁. Exemplos: Hpoly(k,m) := k^v + Σaᵢ·k^(v-i) mod p.

**Trade-offs**: Statistical security possível (ε negligível); composição com PRF: PRFadv ≤ PRFadv[F] + Q²·ε/2; requer chave secreta.

---

## Carter-Wegman MAC

**Quando usar**: Quando hash rápido (ε maior) é aceitável; tags podem ser longas.

**Como**: r←R; v←H(k₁,m)+F(k₂,r) mod N; output (r,v). Randomizer r previne forgery.

**Trade-offs**: Hash mais rápido que PRF; tags maiores (r+v); Q²-term retorna se randomizers colidem; nonce-based variant elimina Q².

---

## Merkle-Damgård Construction

**Quando usar**: Estender hash collision-resistant para mensagens longas.

**Como**: Iterar compression function h: tᵢ := h(tᵢ₋₁, mᵢ) com t₀=IV fixo. Padding block PB contém ⟨length⟩.

**Trade-offs**: CR de h implica CR de H (Theorem 8.2); padding com tamanho essencial; vulnerável
