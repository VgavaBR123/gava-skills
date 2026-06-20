# Cheatsheet — A Graduate Course in Applied Cryptography

## Quando usar o quê: Decisões de design

| Cenário | Escolha | Porque | Threshold |
|---------|---------|--------|-----------|
| Mensagem única, adversário ilimitado | One-Time Pad | Perfect security (Shannon) | \|K\| ≥ \|M\| obrigatório |
| Mensagem única, adversário eficiente | Stream cipher (ChaCha20) | SS com chave curta | λ ≥ 128 bits |
| Múltiplas mensagens, mesma chave | Counter mode / GCM | CPA-secure + paralelismo | Q < 2^(n/2) queries |
| Integridade sem sigilo | HMAC / CMAC | MAC com chave secreta | Tag ≥ 128 bits |
| Sigilo + integridade | GCM (AEAD) | Encrypt-then-MAC integrado | Nunca reutilize nonce |
| Verificação de arquivo público | SHA-256 + Merkle tree | CR hash, log₂n proofs | Digest ≥ 256 bits |
| Key exchange sem PKI | Diffie-Hellman | Anônimo, resiste eavesdrop | Grupo ≥ 2048 bits |

## Tells & Smells: Detectando vulnerabilidades

### 🚨 Red Flags Críticos
| Smell | Problema | Impacto |
|-------|----------|---------|
| Chave reutilizada em stream cipher | Two-time pad: c₁⊕c₂ = m₁⊕m₂ | Recuperação total de plaintexts |
| IV previsível em CBC | Adversário força c[0]⊕m conhecido | CPAadv = 1 |
| Nonce reuse em GCM | Expõe GHASH key km | CI quebrada, forgery trivial |
| MAC-then-encrypt | Padding oracle timing | Decryption via CCA |
| Decryption não-atômica | Libera plaintext antes de verificar tag | SSH length field attack |
| Mesma key para cipher+MAC | Invalida proofs de segurança | CI e CPA podem quebrar |
| Error messages distintos | "bad_mac" vs "decrypt_fail" | Oracle para chosen ciphertext |
| Comparação byte-a-byte de tags | Timing leak | Recuperação de tag via samples |

### ⚠️ Design Smells
- **Block cipher com n < 128**: Birthday bound 2^(n/2) muito baixo (3DES vulnerável)
- **PRG sem next-bit unpredictability**: LCG passa testes estatísticos mas é previsível
- **UHF sem termo líder k^v**: Mensagens (a₁,a₂) e (0,a₁,a₂) colidem
- **Compression function sem padding de tamanho**: Extension attacks em Merkle-Damgård
- **Chaves < 128 bits**: Exhaustive search viável (DES quebrado em 22h)

## Trade-offs: Segurança vs Performance

| Construção | Vantagem | Custo | Quando preferir |
|------------|----------|-------|-----------------|
| **Counter mode** | 7× CBC, paraleliza | Requer PRF, não oculta length | Alta performance, hardware moderno |
| **CBC mode** | Usa apenas E (não D) | Serial, IV imprevisível | Legacy systems, block cipher disponível |
| **CMAC** | Streaming, sem overhead | 2 AES calls | Integridade com block cipher |
| **PMAC** | Paraleliza, incremental | Máscaras i·k em GF(2^n) | Hardware paralelo, edições locais |
| **Carter-Wegman** | Hash rápido (ε maior) | Tags longas, Q² term | Velocidade > tamanho de tag |
| **HMAC** | Sem assumir CR | 2 hash calls | Resistir offline collision attacks |
| **GCM** | Single key, AEAD standard | Nonce management crítico | TLS, IPsec, compliance |

## Bounds de segurança: Quando trocar chaves

| Primitiva | Bound | Ação quando atingir |
|-----------|-------|---------------------|
| AES-128 counter mode | Q < 2^64 blocos | Rekey (birthday) |
| GCM (128-bit tags) | Q < 2^32 mensagens | Rekey (forgery prob 2^-32) |
| CBC mode | Q·ℓ² < 2^64 | Rekey (colisões em chaining) |
| HMAC-SHA256 | Q < 2^128 | Praticamente ilimitado |
| 3DES | Q < 2^32 blocos | Migrar para AES (64-bit blocks) |
| Diffie-Hellman 2048-bit | ~112-bit security | Migrar para 3072-bit ou ECC |

## Regras de decisão: Quando X, faça Y

### Encryption
1. **Mensagem única conhecida**: Use SS cipher (stream cipher OK)
2. **Múltiplas mensagens, chave fixa**: Use CPA-secure (counter/CBC com IV aleatório)
3. **Aplicação gerencia nonces únicos**: Use nonce-based AEAD (elimina expansion)
4. **Precisa integridade também**: Use AEAD (GCM) ou EtM, NUNCA MtE genérico

### MACs
1. **Mensagem curta (< 128 bits)**: PRF direto (AES-128)
2. **Mensagem longa, block cipher disponível**: CMAC (streaming) ou PMAC (paralelo)
3. **Mensagem longa, hash disponível**: HMAC (
