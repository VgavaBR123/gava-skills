# Capítulo 5: Chosen Plaintext Attack

## Ideia central
Cifras determinísticas falham quando múltiplas mensagens são cifradas com a mesma chave, pois adversários podem forçar o sistema a cifrar mensagens escolhidas (chosen plaintext attack). A solução é usar cifras probabilísticas que atendem semantic security against chosen plaintext attack (CPA security).

## Frameworks introduzidos
- **CPA Security (Attack Game 5.2)**: Adversário submete pares (mi0, mi1) adaptativamente; challenger cifra mib com mesma chave k; adversário distingue b com vantagem negligível. Formaliza segurança quando múltiplas mensagens são cifradas sob uma chave.
- **Nonce-based CPA Security (Attack Game 5.3)**: Variante determinística onde encryption recebe nonce N único; segurança depende apenas de unicidade (não imprevisibilidade) dos nonces. Elimina ciphertext expansion quando aplicação garante nonces únicos.
- **Multi-key Semantic Security (Attack Game 5.1)**: Cada mensagem cifrada com chave independente ki; captura cenário "one key per file". Theorem 5.1 prova que SS ⇒ MSS via hybrid argument.
- **Generic Hybrid Construction**: E'(k', m) := x ← X, k ← F(k', x), c ← E(k, m), output (x, c). Combina PRF F para derivar one-time keys com cipher SS E. Theorem 5.2: se F é PRF segura, E é SS, e N = |X| é super-poly, então E' é CPA secure.
- **Randomized Counter Mode**: E'(k, m) := x ← X, para j = 0 a v-1: c[j] ← F(k, x+j mod N) ⊕ m[j], output (x, c). Theorem 5.3: CPA secure se F é PRF e N super-poly (bound: 2Q²/N + 2·PRFadv).
- **CBC Mode**: c[0] ← X (IV), para j = 0 a v-1: c[j+1] ← E(k, c[j] ⊕ m[j]). Theorem 5.4: CPA secure se E é block cipher segura e N super-poly (bound: 2Q²ℓ²/N + 2·BCadv).
- **Revocable Broadcast Encryption**: Árvore binária com n folhas (devices); cada device recebe log₂ n chaves no caminho raiz-folha. Revogação: cifrar com cover(S) (Theorem 5.8: |cover(S)| ≤ r·log₂(n/r) para r devices revogados).

## Conceitos-chave
- **Chosen Plaintext Attack**: Adversário força sistema a cifrar mensagens de sua escolha para extrair informação sobre outras mensagens (ex.: email spam auto-cifrado revela keystream).
- **Deterministic Cipher Weakness**: Sempre produz mesmo ciphertext para (k, m) fixos; adversário detecta mensagens idênticas (Example 5.1: CPAadv = 1 com duas queries).
- **Probabilistic Cipher**: Encryption algorithm usa randomness; mesma (k, m) gera ciphertexts diferentes. Necessário para CPA security.
- **Initial Value (IV)**: Componente aleatório do ciphertext (x em counter mode, c[0] em CBC); deve ser imprevisível em CBC (Exercise 5.13: predictable IV quebra CPA).
- **Ciphertext Expansion**: Ciphertexts mais longos que plaintexts (inevitável para CPA security, Exercise 5.10); nonce-based encryption elimina quando aplicação gerencia nonces.
- **Nonce**: Valor único (não necessariamente aleatório) usado em encryption/decryption; aplicação garante unicidade, não o esquema.
- **Adaptive Queries**: Adversário escolhe (mi0, mi1) baseado em c1,...,ci-1; captura ataques realistas onde adversário influencia mensagens futuras.
- **Ciphertext Stealing**: Técnica CBC que elimina padding para mensagens não-múltiplas do block size (Exercise 5.16); ciphertext tem comprimento do plaintext.
- **Online Cipher**: Processa/emite blocos incrementalmente sem esperar mensagem completa (Exercise 5.19: counter mode é online CPA secure, CBC não).
- **Cover Set cover(S)**: Menor conjunto de nós em árvore binária cujos descendentes cobrem exatamente folhas S; usado em broadcast encryption para revogar devices.

## Mental models
- Use **generic hybrid construction** quando tiver PRF + SS cipher: PRF deriva one-time keys, SS cipher cifra payload. Segurança: Q²/N (collision) + PRFadv + Q·SSadv.
- Use **counter mode** para paralelismo/performance: PRF avaliada em x, x+1,...,x+ℓ-1; XOR com plaintext. Requer N super-poly e nonces bem espaçados (intervalos não-sobrepostos).
- Use **CBC mode** quando block cipher é primitiva disponível e paralelismo não é crítico: c[j+1] = E(k, c[j] ⊕ m[j]). IV deve ser imprevisível (não apenas único).
- Use **nonce-based encryption** quando aplicação pode garantir nonces únicos: elimina ciphertext expansion e randomness requirement. Nonce-based counter mode: x = N·ℓ garante intervalos disjuntos.

## Anti-padrões
- **Reusing keys with deterministic ciphers**: Stream cipher com seed fixo expõe keystream via known-plaintext; adversário recupera m₁ ⊕ m₂ ou força encryption de mensagem conhecida.
- **Predictable IVs in CBC**: TLS 1.0 usa último ciphertext block como próximo IV; adversário prevê IV e quebra CPA (Exercise 5.13, BEAST attack).
- **Single global device key**: CSS usava kd compartilhada; um leak compromete todo conteúdo. AACS usa chaves únicas + revocation tree.
- **Ignoring ciphertext expansion**: Aplicações que assumem |c| = |m| quebram com CPA-secure schemes (Exercise 5.10: ℓ bits expansion ⇒ attack com 2^ℓ/2 queries).
- **Using same key for PRF and block cipher**: Nonce-based CBC com k' = k é inseguro (Exercise 5.14); sempre use chaves independentes.
- **Small block sizes**: 3DES-CBC (64-bit blocks) vulnerável a birthday attacks com 2^32 blocos (Exercise 5.11); AES-128 (128-bit) requer 2^64 blocos.

## Exemplos de código / Tabelas

**Generic Hybrid (Theorem 5.2):**
```
E'(k', m):
  x ← X
  k ← F(k', x)
  c ← E(k, m)
  return (x, c)

D'(k', (x, c)):
  k ← F(k', x)
  m ← D(k, c)
  return m
```

**Randomized Counter Mode (Theorem 5.3):**
```
E(k, m):  // m ∈ Y^v
  x ← {0,...,N-1}
  for j = 0 to v-1:
    c[j] ← F(k, x+j mod N) ⊕ m[j]
  return (x, c)
```

**CBC Mode (Theorem 5.4):**
```
E(k, m):  // m ∈ X^v
  c[0] ← X  // random IV
  for j = 0 to v-1:
    c[j+1] ← E(k, c[j] ⊕ m[j])
  return c  // c ∈ X^(v+1)
```

**TLS 1.0 Padding (Section 5.4.4):**
```
v = |m| bytes
p = 16 - (v mod 16)
pad = [p-1, p-1, ..., p-1]  // p bytes
padded_m = m || pad
```

**RFC 3686 AES Counter Mode IV:**
```
IV[127:96]  = fixed 32-bit salt (per key)
IV[95:32]   = random 64-bit nonce
IV[31:0]    = 0x00000001
// Increment IV[31:0] for each block
```

**Broadcast Encryption Cover (Theorem 5.8):**
```
|cover(S)| ≤ r · log₂(n/r)
// r = devices revogados, n = total devices
// Exemplo: n=2^30, r=1000 ⇒ header ≤ 20k blocos
```

## Worked Example

**Ataque a CBC com IV previsível (Exercise 5.13):**

Setup: Adversário sabe que próximo IV será último ciphertext block do encryption anterior.

1. **Query 1**: Submete (m₀, m₁) onde m₀ ≠ m₁ arbitrários
   - Recebe c = (c[0], c[1]) onde c[0] = IV₁ aleatório
   - Próximo IV será c[1]

2. **Query 2**: Escolhe m'₀ = c[1] ⊕ m₀, m'₁ = c[1] ⊕ m₁
   - Em Experiment 0: c'[1] = E(k, c[1] ⊕ m'₀) = E(k, c[1] ⊕ c[1] ⊕ m₀) = E(k, m₀)
   - Em Experiment 1: c'[1] = E(k, c[1] ⊕ m'₁) = E(k, m₁)

3. **Distinguisher**: 
   - Compute x₀ = D(k, c[1]) ⊕ c[0] = m₀ (do primeiro query)
   - Se E(k, x₀) = c'[1] então output 0, senão output 1
   - CPAadv = 1 (distingue perfeitamente)

**Lição**: IV em CBC deve ser imprevisível, não apenas único. TLS 1.0 violou isso; BEAST attack explorou para recuperar session cookies.

## Key takeaways

1. **CPA security exige probabilismo**: Deterministic ciphers sempre vazam message equality; use randomness (counter/CBC) ou nonces (nonce-based).
2. **Hybrid construction é template genérico**: PRF(k', x) deriva one-time key k; SS cipher E(k, m) cifra payload. Segurança: collision bound Q²/N + PRFadv + Q·SSadv.
3. **Counter mode domina CBC**: 7× mais rápido (pipelining), paralelizável, ciphertext mais curto para mensagens pequenas, usa apenas E (não D). CBC requer IV imprevisível.
4. **Nonce-based elimina expansion**: Quando aplicação garante nonces únicos, não precisa randomness. Nonce-based counter: x = N·ℓ garante intervalos disjuntos (Theorem 5.6).
5. **Concrete security bounds importam**: Counter mode permite Q = 2^39.5 mensagens (1MB cada, n=128, advantage < 2^-32); CBC apenas Q = 2^32. Revocation tree: r devices ⇒ header r·log₂(n/r).
6. **Multi-key ⇒ single-key via hybrid**: Theorem 5.1 prova SS ⇒ MSS com degradação Q (telescoping sum). Theorem 5.2 prova MSS ⇒ CPA via PRF switching + collision bound.

## Conecta com
- **Cap. 2 (Semantic Security)**: CPA generaliza SS para múltiplas mensagens; SS é caso especial (Q=1). Generic hybrid usa SS cipher como building block.
- **Cap. 3 (PRGs/Stream Ciphers)**: Stream cipher com seed fixo falha em CPA (keystream reuse); counter mode é "stream cipher com IV aleatório".
- **Cap. 4 (PRFs/Block Ciphers)**: Counter/CBC usam PRF/block cipher como primitiva; PRF switching lemma (Theorem 4.4) aparece em proofs (Games 0→1).
- **Cap. 6 (Message Integrity)**: CPA não provê integrity; CBC malleability (Exercise 5.18) motiva MACs. Encrypt-then-MAC combina CPA + integrity.
- **Cap. 11 (Key Management)**: Broadcast encryption resolve "como revogar keys"; AACS usa subset-tree difference para |cover(S)| = O(r).
