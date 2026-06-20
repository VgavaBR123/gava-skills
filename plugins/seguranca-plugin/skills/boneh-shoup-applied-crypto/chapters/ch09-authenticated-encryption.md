# Capitulo 9: Authenticated Encryption

## Ideia central
Authenticated Encryption (AE) garante simultaneamente confidencialidade (CPA security) e integridade (ciphertext integrity), protegendo contra adversarios que podem interagir maliciosamente com sender e receiver. CPA security sozinha é insuficiente para quase todas aplicacoes reais.

## Frameworks introduzidos
- **Encrypt-then-MAC (EtM)**: Encriptar mensagem c←E(kenc,m), depois MAC no ciphertext tag←S(kmac,c); resultado é (c,tag). Sempre seguro para qualquer combinacao de CPA-secure cipher + secure MAC. Usado em TLS 1.2+, IPsec, GCM.
- **MAC-then-encrypt (MtE)**: MAC na mensagem tag←S(kmac,m), depois encriptar par (m,tag) como c←E(kenc,(m,tag)). Pode ser inseguro mesmo com componentes seguros; usado em SSL 3.0/TLS 1.0/802.11i mas vulneravel a padding oracle attacks.
- **Galois Counter Mode (GCM)**: AEAD standard combinando counter mode + Carter-Wegman MAC via GHASH. Usa single key, nonce-based, sem nonce-reuse resistance.
- **Nonce-based AEAD**: Sintaxe c=E(k,m,d,N) onde d=associated data (integridade sem sigilo), N=nonce unico. Decryption atomica obrigatoria.

## Conceitos-chave
- **Ciphertext Integrity (CI)**: Adversario nao consegue criar ciphertext valido novo apos ver encryptions de mensagens escolhidas (Attack Game 9.1).
- **AE-secure**: Cipher é (1) semantically secure under CPA e (2) provides ciphertext integrity.
- **Chosen Ciphertext Attack (CCA)**: Adversario obtem encryptions e decryptions de ciphertexts escolhidos (exceto os recebidos do challenger). AE-security implica CCA-security.
- **Associated Data (AD)**: Dados com integridade protegida mas transmitidos em claro (ex: packet headers em networking).
- **Padding Oracle**: Side-channel onde timing/error messages revelam se padding é valido, permitindo decryption completa via chosen ciphertext queries.
- **GHASH**: Keyed hash XOR-DUF baseado em polynomial evaluation sobre GF(2^128); core do GCM MAC.
- **Non-atomic Decryption**: Liberar plaintext fragments antes de verificar integrity tag—vulnerabilidade critica (ex: SSH length field attack).
- **Boundary Hiding**: Ocultar comprimentos/limites de mensagens contra traffic analysis (SSHv2 encrypta length field).

## Mental models
- Use EtM quando combinar cipher+MAC genericamente: MAC no ciphertext previne tampering detectavel.
- Use nonce-based AEAD (GCM) quando precisar performance + standard compliance; nunca reuse nonces.
- Sempre verifique integrity tag ANTES de processar qualquer plaintext data (atomic decryption).
- Associated data quando headers devem ser roteaveis mas integros (TLS records, network packets).

## Anti-padroes
- **MtE com CBC**: Padding oracle timing attacks (Lucky13) permitem decryption completa via chosen ciphertext queries medindo response time.
- **Mesma key para cipher e MAC**: Invalida proofs de seguranca; pode quebrar CI e CPA (Exercise 9.8).
- **MAC apenas em parte do ciphertext**: Attacker modifica partes nao-MACed (ex: CBC IV em ISO 19772, RNCryptor iOS).
- **Error messages informativos**: "bad_record_mac" vs "decryption_failed" cria oracle; sempre retorne generic "decryption failed".
- **Nonce deterministico em GCM**: Nonce reuse expoe GHASH key km, quebrando CI completamente.
- **CRC para integrity**: Linear function permite tampering indetectavel (WEP Attack 3: c'=c⊕(δ,L(δ)) decrypts to m⊕δ).

## Exemplos de codigo / Tabelas

**EtM encryption:**
```
EEtM((ke,km), m) := 
    c ← E(ke, m)
    t ← S(km, c)
    output (c, t)
```

**GCM encryption (96-bit nonce):**
```
km ← E(k, 0^128)              // GHASH key
x ← (N || 0^31 || 1)          // initial counter
c ← {counter mode from x}
h ← GHASH(km, d||c||len(d)||len(c))
t ← h ⊕ E(k, x)
output (c, t)
```

**GHASH polynomial evaluation:**
```
GHASH(k, z) := z[0]·k^v + z[1]·k^(v-1) + ... + z[v-1]·k  in GF(2^128)
```

## Worked Example

**SSL 3.0 Padding Oracle Attack (POODLE):**

Setup: Browser envia cookie via SSL 3.0 MtE (CBC + MAC). Mensagem m com tag t; CBC encrypta (m||t||pad) onde ultimo byte do pad = (p-1).

Attacker goal: Recuperar cookie byte-a-byte.

1. Intercepta ciphertext c = [c[0], c[1], ..., c[ℓ-1], c[ℓ]] onde c[0]=IV, c[ℓ]=encrypted pad
2. Constroi c^ = [c[0], c[1], ..., c[ℓ-1], c[1]]  // substitui ultimo bloco por c[1]
3. CBC decryption do ultimo bloco: v := D(ke,c[1]) ⊕ c[ℓ-1] = m[0] ⊕ c[0] ⊕ c[ℓ-1]
4. Se ultimo byte de v = 15 → pad valido → server nao rejeita → ultimo byte de m[0] = ultimo byte de (15 ⊕ c[0] ⊕ c[ℓ-1])
5. Repete com fresh encryptions (Javascript força browser reenviar): ~256 queries revelam 1 byte
6. Shift cookie 1 byte (muda path "/AA" → "/AAA") e repete para proximo byte

Resultado: Cookie completo recuperado via ~256·len(cookie) chosen ciphertext queries explorando que MtE nao protege pad integrity.

## Key takeaways
1. Sempre use EtM ou AEAD standard (GCM); nunca implemente generic composition manualmente
2. CPA security sozinha nao basta: ciphertext malleability quebra confidentiality via chosen ciphertext attacks
3. Decryption deve ser atomica: verifique integrity tag sobre mensagem COMPLETA antes de liberar qualquer plaintext
4. Keys independentes: ke≠km em generic composition; GCM deriva km via PRF
5. Nonce management é critico em GCM: reuse expoe km e quebra CI; use random initial nonce contra time-space tradeoffs
6. Associated data protege integrity de headers/metadata sem encriptar (TLS record type/version/length)
7. Padding oracles (timing, error codes) permitem decryption completa; implemente constant-time rejection
8. Traffic analysis persiste: encrypted lengths revelam info (TLS records); boundary hiding requer design especifico (SSHv2)

## Conecta com
- Cap 5 (CPA security): AE = CPA + CI; counter/CBC modes como building blocks
- Cap 6 (MACs): Carter-Wegman MAC, HMAC-SHA1 em construcoes EtM/MtE
- Cap 7 (Hash functions): GHASH como XOR-DUF sobre GF(2^128)
- Cap 8 (KDFs): TLS 1.3 usa HKDF para derivar kbs/ksb de master secret
- Cap 21 (TLS handshake): Session setup negocia cipher suite e estabelece master secret
