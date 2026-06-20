# Capitulo 8: Message integrity from collision resistant hashing

## Ideia central
Funções hash keyless collision-resistant permitem estender primitivas criptográficas (MACs, PRFs) para mensagens longas e garantir integridade de arquivos sem chaves secretas, apenas com armazenamento read-only.

## Frameworks introduzidos
- **Merkle-Damgård paradigm**: Constrói hash CR para mensagens longas iterando compression function h sobre blocos. Usa chaining variables ti = h(ti-1, mi) com padding block PB contendo tamanho da mensagem. (Quando: estender domínio de hash curto; Como: SHA256, MD5)
- **Davies-Meyer compression**: hDM(x,y) := E(y,x) ⊕ x transforma block cipher em compression function. Mensagem mi vira chave do cipher. (Quando: construir h para Merkle-Damgård; Como: SHA256 usa variante com adição mod 2³²)
- **Sponge construction**: Itera permutation π sem chave com rate r e capacity c. Fase absorbing mistura blocos, squeezing extrai output. (Quando: hash com segurança além de collision resistance; Como: SHA3/Keccak)
- **HMAC**: Fnest((k1,k2),M) := H(k2 ∥ H(k1 ∥ M)) deriva dois PRFs hbot e htop de h. HMAC usa k1=k⊕ipad, k2=k⊕opad. (Quando: MAC para mensagens longas sem assumir CR; Como: TLS, IPsec)
- **Merkle trees**: Hash hierárquico H(x1,...,xn) permite provar xi∈T com log₂n hashes. Sorted tree prova non-membership. (Quando: integridade de arquivos com verificação seletiva; Como: package managers, authenticated data structures)

## Conceitos-chave
- **Collision resistance**: Encontrar m0≠m1 com H(m0)=H(m1) é computacionalmente difícil mesmo sem chaves secretas
- **Birthday attack**: Encontra colisão em O(√N) queries para digest space |T|=N via paradoxo do aniversário
- **Compression function h**: M×Y→X (Merkle-Damgård) ou X×K→X (Davies-Meyer) que preserva CR quando iterada
- **Chaining variable**: ti conecta blocos consecutivos em Merkle-Damgård; t0=IV fixo
- **Padding block PB**: Contém encoding do tamanho da mensagem (crucial para segurança); formato 100...00∥⟨length⟩
- **Ideal cipher model**: Modela E como família {πk}k∈K de permutações aleatórias independentes para análise heurística
- **Random oracle model**: Modela H como função verdadeiramente aleatória O∈Funs[M,T]; adversário consulta O
- **Target collision resistance (TCR)**: Variante mais fraca onde adversário escolhe m0 antes de ver parâmetros do sistema
- **Merkle proof π**: log₂n hashes provam xi∈T; sorted tree usa xi<x<xi+1 para provar x∉T
- **Key derivation**: Transforma secret s com distribuição P em chave t computacionalmente indistinguível de uniforme

## Mental models
- Use hash-then-MAC quando precisar estender MAC para mensagens longas: S'(k,m):=S(k,H(m)) é seguro se H é CR
- Use Merkle trees quando precisar verificar blocos individuais sem recomputar hash completo: log₂n hashes vs n hashes
- Use HMAC quando precisar PRF de mensagens longas sem assumir CR: resiste a offline collision-finding attacks
- Use sponge quando precisar flexibilidade (variable-length I/O) e segurança além de CR: SHA3 é random oracle heurístico

## Anti-padroes
- **Prepend key Fpre(k,M):=H(k∥M)**: Extension attack permite computar Fpre(k,M∥PB∥M') dado Fpre(k,M)
- **Append key Fpost(k,M):=H(M∥k)**: Vulnerável a offline collision-finding; colisão M0,M1 em h(IV,·) quebra MAC
- **Davies-Meyer variants inseguros**: h4(x,y):=E(y,x)⊕y e h5(x,y):=E(x,x⊕y)⊕x têm colisões em tempo constante
- **Usar SHA1**: Colisões encontradas em 2⁶³ (Wang 2005) e 2017; não é mais CR
- **Merkle-Damgård como random oracle direto**: Joux's attack e extension attacks; use HMAC ou sponge
- **Capacity pequeno em sponge**: c bits determinam segurança; c=256 para SHA3-256 resiste a birthday com 2¹²⁸

## Exemplos de codigo / Tabelas

**SHA256 round function (Table 8.3)**:
```
Key setup: W₀,...,W₁₅ ← k₀,...,k₁₅
           Wᵢ ← σ₁(Wᵢ₋₂) + Wᵢ₋₇ + σ₀(Wᵢ₋₁₅) + Wᵢ₋₁₆  (i=16..63)

64 Rounds: a₀,...,h₀ ← t₀,...,t₇
for i=0 to 63:
  T₁ ← hᵢ + Σ₁(eᵢ) + Ch(eᵢ,fᵢ,gᵢ) + Kᵢ + Wᵢ
  T₂ ← Σ₀(aᵢ) + Maj(aᵢ,bᵢ,cᵢ)
  aᵢ₊₁,...,hᵢ₊₁ ← T₁+T₂, aᵢ, bᵢ, cᵢ, dᵢ+T₁, eᵢ, fᵢ, gᵢ
```

**Sponge absorbing/squeezing**:
```
Absorbing: h←0ⁿ; for i=1..s: h←π(h ⊕ (mᵢ∥0ᶜ))
Squeezing: z₁←h[0..r-1]; for i=2..⌈v/r⌉: h←π(h); zᵢ←h[0..r-1]
```

**Collision resistance bounds**:
| Construction | Bound | Notes |
|--------------|-------|-------|
| Birthday | q²/2N | Generic attack, N=\|T\| |
| Davies-Meyer | (q+1)(q+2)/\|X\| | Ideal cipher model |
| Sponge | q(q-1)/2ᵛ + q(q+1)/2ᶜ | v=output, c=capacity |
| HMAC (hbot) | 2Qic/\|X\| | Ideal cipher for E(m,k)⊕k |

## Worked Example
**Hash-then-MAC security (Theorem 8.1)**:
- Setup: MAC I=(S,V) para mensagens curtas TH, hash H:M→TH collision-resistant
- Construção: S'(k,m):=S(k,H(m)), V'(k,m,t):=V(k,H(m),t)
- Ataque: Adversário A consulta m₁,...,mq e forja (m,t)
- Caso 1: Se H(m)=H(mᵢ) e m≠mᵢ → colisão em H (evento Y)
- Caso 2: Se H(m)≠H(mᵢ) para todo i → (H(m),t) forja I (evento Z)
- Redução: MACadv[A,I'] ≤ MACadv[Bᵢ,I] + CRadv[Bₕ,H]
- Adversário Bₕ: Simula challenger, se Y ocorre output (m,mᵢ)
- Adversário Bᵢ: Repassa queries hᵢ←H(mᵢ), output (H(m),t)

**Merkle tree membership proof**:
- Tree: n=8 leaves x₁,...,x₈; y₁₅=root hash
- Provar x₃ autêntico: Fornecer π=(y₄,y₉,y₁₄)
- Verificação: ŷ₃←h(x), ŷ₁₀←h(ŷ₃,y₄), ŷ₁₃←h(y₉,ŷ₁₀), ŷ₁₅←h(ŷ₁₃,y₁₄)
- Accept se ŷ₁₅=y₁₅ (valor em read-only storage)
- Tamanho: log₂n hashes; r elementos → r·log₂(n/r) hashes (Theorem 8.7)

## Key takeaways
1. Collision resistance permite hash-then-MAC seguro: S'(k,m):=S(k,H(m)) estende qualquer MAC sem aumentar tamanho da chave
2. Birthday attack força digest ≥256 bits: 2⁶⁴ queries para 128-bit digest; SHA256 resiste com 2¹²⁸ segurança
3. Merkle-Damgård reduz CR de mensagens longas a CR de compression function: padding com tamanho é essencial
4. Davies-Meyer E(y,x)⊕x é CR no ideal cipher model: mensagem mi vira chave do cipher; SHA256 usa variante com adição
5. HMAC evita offline collision attacks: Fnest seguro assumindo hbot e htop são PRFs; HMAC deriva k₁,k₂ de chave única
6. Sponge permite variable-length I/O e é random oracle heurístico: SHA3 com c=512 para 256-bit output
7. Merkle trees permitem verificação seletiva com log₂n overhead: sorted tree prova non-membership via xi<x<xi+1
8. Key derivation requer random oracle model: t←H(s) é heurístico; sub-key derivation usa PRF seguro

## Conecta com
- Cap. 6 (MACs): Hash-then-MAC estende domain; NMAC é base do HMAC
- Cap. 4 (Block ciphers): Davies-Meyer usa E como building block; ideal cipher model
- Cap. 7 (UHFs): PRF(UHF) vs hash-then-MAC; UHF requer chave, CR não
- Cap. 13 (Signatures): File integrity sem read-only storage usando assinaturas digitais
- Cap. 10 (Number theory): Compression function h(a,b)=|xᵃyᵇ mod p| é CR sob discrete log
