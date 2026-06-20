# Capitulo 15: Elliptic curve cryptography and pairings

## Ideia central
Curvas elipticas sobre campos finitos fornecem grupos onde discrete log é mais dificil que em Zp*, permitindo chaves menores (256 bits vs 2048 bits). Pairings adicionam estrutura extra que habilita criptografia avançada (assinaturas agregaveis, IBE, functional encryption) impossivel em grupos sem pairing.

## Frameworks introduzidos
- **Chord method (Diophantus)**: Dados pontos racionais P, Q em curva cubica, a reta por P,Q intersecta a curva em terceiro ponto racional R; define P ⊕ Q := -R (usar para construir novos pontos racionais / base da lei de grupo)
- **Tangent method**: Tangente em ponto racional P intersecta curva em segundo ponto racional; corresponde a P ⊕ P (usar quando x₁=x₂, y₁=y₂, y₁≠0)
- **BLS signature aggregation**: Produto de assinaturas σ₁···σₙ forma agregado valido; verificacao e(σₐ𝓰,g₁)=∏e(H(mᵢ),pkᵢ) (usar para comprimir multiplas assinaturas em blockchain/certificate chains)
- **Message augmentation (Method 1)**: Prepend pk a cada mensagem antes de assinar; previne rogue key attack (usar quando verificar agregados de mensagens distintas)
- **Proof of possession (Method 2)**: Incluir π=H'(u)^α na pk para provar conhecimento de sk; permite verificacao rapida quando todas mensagens iguais (usar quando signers fixos e mensagem comum)
- **Identity Based Encryption (IBE)**: Qualquer string id é chave publica; trusted party gera sk_id = H(id)^α; elimina round-trip para lookup de chave (usar em ambientes corporativos com trusted entity)

## Conceitos-chave
- **Elliptic curve E/𝔽ₚ**: Equacao y²=x³+ax+b onde 4a³+27b²≠0; conjunto E(𝔽ₚ) de pontos (x,y) satisfazendo equacao mais ponto O forma grupo abeliano
- **Point at infinity O**: Elemento identidade do grupo; P⊕O=P para todo P
- **Embedding degree d**: Menor inteiro onde pairing mapeia G₀⊆E(𝔽ₚ), G₁⊆E(𝔽ₚᵈ) → Gₜ⊆𝔽*ₚᵈ; deve ser pequeno (d≤16) para eficiencia
- **Pairing e:G₀×G₁→Gₜ**: Funcao bilinear e(u·u',v)=e(u,v)·e(u',v); satisfaz e(g₀^α,g₁^β)=e(g₀,g₁)^(αβ)
- **co-CDH assumption**: Dados (g₀^α, g₁^α, g₀^β), computar g₀^(αβ) é dificil; α usado em ambos G₀ e G₁
- **Twist E~**: Curva relacionada cy²=x³+ax+b onde c é non-residue; |E(𝔽ₚ)|+|E~(𝔽ₚ)|=2p+2
- **Twist security**: Discrete log intratavel em E(𝔽ₚ) e E~(𝔽ₚ); previne ataques quando membership check omitido
- **Rogue public key attack**: Adversario cria pk_adv=u/u_B sem conhecer sk; pode forjar agregado valido
- **d-CDH (power CDH)**: Dados g₀,g₀^(α²),...,g₀^(αᵈ),g₁,h₁,h₁^(αᵈ⁺²), computar e(g₀,h₁)^(αᵈ⁺¹); permite avaliar polinomio P(α) via g₀^P(α)=∏(g₀^(αⁱ))^cᵢ
- **Master key pair (mpk,msk)**: Em IBE, mpk publico global; msk permite derivar sk_id para qualquer identidade

## Mental models
- Use curvas elipticas quando precisar de 128-bit security com chaves curtas (256-bit vs 2048-bit em Zp*)
- Use pairing quando precisar testar igualdade DDH (e(g₀^α,g₁^β)=?e(g₀^γ,g₁)) ou agregar assinaturas
- Use secp256k1 (Koblitz) quando precisar de multiplicacao rapida via endomorfismo φ; use Curve25519 quando precisar de twist security e operacoes constante-tempo
- Use IBE quando eliminar round-trip de key lookup vale mais que confiar em trusted party com msk

## Anti-padroes
- **Usar curvas anomalas ou com embedding degree pequeno**: |E(𝔽ₚ)|=p permite discrete log polinomial; pequeno d permite GNFS em 𝔽ₚᵈ reduzir seguranca
- **Omitir group membership check com curvas non-twist-secure**: Adversario envia ponto em twist E~; se discrete log facil em E~, resposta expoe sk (secp256r1/k1 nao sao twist-secure)
- **Agregar BLS sem prevenir rogue keys**: Adversario cria pk_adv=u/u_B; pode forjar agregado fazendo parecer que Bob assinou
- **Reusar mesmo r em assinatura SG sem PRF**: Expoe sk se adversario obtem duas assinaturas distintas na mesma mensagem
- **Usar pairing simetrico (G₀=G₁) quando precisar de DDH**: Pairing torna DDH facil via teste e(g₀^α,g₀^β)=?e(g₀^γ,g₀)

## Exemplos de codigo / Tabelas

```python
# BLS signature (additive notation)
def sign(sk_α, m):
    return H(m)^α  # σ ∈ G₀

def verify(pk_u, m, σ):
    return e(H(m), pk_u) == e(σ, g₁)

# BLS aggregation (Method 1: message augmentation)
def aggregate(pk_vec, σ_vec):
    return σ₁ · σ₂ · ... · σₙ  # product in G₀

def verify_aggregate(pk_vec, m_vec, σ_ag):
    return e(σ_ag, g₁) == ∏ e(H(pkᵢ,mᵢ), pkᵢ)
```

**Benchmarks (bn256, milliseconds)**:
| Operacao | Tempo |
|----------|-------|
| Exp in G₀ | 0.22 |
| Exp in G₁ | 0.44 |
| Exp in Gₜ | 0.95 |
| Pairing e | 2.32 |

**Curvas padrao**:
- secp256r1 (P256): p=2²⁵⁶-2²²⁴+2¹⁹²+2⁹⁶-1, y²=x³-3x+b, |E|=prime
- secp256k1: p=2²⁵⁶-2³²-2⁹-...-1, y²=x³+7, Koblitz (φ speedup)
- Curve25519: p=2²⁵⁵-19, By²=x³+486662x²+x, cofactor 8, twist-secure

## Worked Example

**Agregando assinaturas BLS com Method 2 (proof of possession)**:

Setup: Pairing e:G₀×G₁→Gₜ, H:M→G₀, H':G₁→G₀

1. Alice gera chave: α←$Zq, u₁=g₁^α, π=H'(u₁)^α, pk_A=(u₁,π)
2. Bob gera chave: β←$Zq, v₁=g₁^β, ρ=H'(v₁)^β, pk_B=(v₁,ρ)
3. Alice assina m: σ_A=H(m)^α ∈ G₀
4. Bob assina m: σ_B=H(m)^β ∈ G₀
5. Agregador computa: σ_ag=σ_A·σ_B=H(m)^(α+β)
6. Verificador checa proofs: e(π,g₁)=?e(H'(u₁),u₁), e(ρ,g₁)=?e(H'(v₁),v₁)
7. Verificador checa agregado (otimizado, mesma mensagem):
   - apk=u₁·v₁=g₁^(α+β)
   - e(σ_ag,g₁)=?e(H(m),apk)
   - e(H(m)^(α+β),g₁)=e(H(m),g₁^(α+β)) ✓

Vantagem: Apenas 2 pairings para verificar n assinaturas quando mensagem comum.

## Key takeaways

1. Curvas elipticas permitem 256-bit keys com seguranca equivalente a 2048-bit RSA; escolha curva vetada (P256/secp256k1/Curve25519) e verifique |E(𝔽ₚ)| é primo ou 4q/8q
2. Pairing e:G₀×G₁→Gₜ satisfaz e(g₀^α,g₁^β)=e(g₀,g₁)^(αβ); torna DDH facil mas habilita BLS signatures, IBE, functional encryption
3. BLS aggregation requer prevencao de rogue keys: Method 1 (prepend pk) para mensagens distintas; Method 2 (proof of possession π) para mensagem comum com verificacao rapida
4. IBE elimina key lookup round-trip usando id como pk; trusted party com msk deriva sk_id=H(id)^α; apropriado quando trusted entity aceitavel (corporativo)
5. Seguranca sem random oracle possivel com pairings: esquema SG usa d-CDH para assinar m via σ=(r,g₀^(α-r)/(β-m)); esquema SBB usa σ=(r,h₀^1/(α+r+m))
6. Twist security essencial se omitir membership check; secp256r1/k1 nao sao twist-secure (discrete log em twist ~2¹⁸ vezes mais facil)
7. Pairing performance: ~10× mais lento que exp in G₀; otimize via fixed-base precomputation e product-of-pairings batching

## Conecta com

- Cap 11 (Public-key encryption): IBE generaliza PKE; pairing permite testar DDH usado em ElGamal
- Cap 13 (Digital signatures): BLS estende para agregacao; proof of possession previne rogue keys
- Cap 16 (Algorithms for factoring and discrete log): GNFS em 𝔽ₚᵈ limita embedding degree; Pollard rho em E(𝔽ₚ) requer |E|≈2²⁵⁶
- Cap 20 (Zero knowledge proofs): Pairings permitem provar conhecimento de σ sem revelar; usado em zk-SNARKs
- Cap 22 (Threshold cryptography): BLS naturalmente suporta threshold signatures via secret sharing de α
