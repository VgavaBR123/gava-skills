# Capitulo 14: Fast hash-based signatures

## Ideia central
Assinaturas hash-based constroem esquemas de assinatura a partir de funções one-way e collision-resistant, oferecendo velocidade superior ao RSA e segurança pós-quântica, mas com assinaturas mais longas.

## Frameworks introduzidos
- **Lamport One-Time Signature (S1bit)**: Para mensagem m ∈ {0,1}, gera pk := (f(x0), f(x1)), sk := (x0, x1); assina revelando xm (usar quando velocidade > tamanho de assinatura)
- **Basic Lamport (SL)**: Extensão para v bits usando 2v pares (xi,0, xi,1); assinatura = {xi,mi} para m = m1...mv (framework base para one-time signatures)
- **Optimized Lamport (Popt)**: Usa n = v + 1 + ⌈log2 v⌉ com checksum c = v - weight(m); reduz |pk| e |σ| pela metade vs. basic Lamport
- **Winternitz Signatures (Swin)**: Usa hash chains f(j)(x) com parâmetros (n, d); assinatura = corte através de retângulo n×d; reduz tamanho em ~4× quando d=15 vs. Lamport
- **HORS/HORST**: Mapeia mensagens para subconjuntos de tamanho ℓ via Phors: {0,1}v → Sets[n,ℓ]; usa Merkle tree para comprimir pk (quando ℓ << n)
- **Merkle Many-Time Signatures (SMerkle)**: Árvore q-ária de profundidade d com one-time keys nos nós; suporta qd mensagens; usa PRF para gerar keys deterministicamente
- **TESLA Broadcast Authentication**: Hash chain k0 →f k1 →f ... →f kn; broadcast (mi, ti, kn-i+1) onde ti = S(kn-i, mi); autenticação atrasada em T segundos

## Conceitos-chave
- **q-time signature**: Par (pk, sk) seguro para assinar até q mensagens (q pequeno, tipicamente < 100)
- **Containment free function P**: Para m ≠ m', P(m') não contém P(m); previne forgery em Lamport
- **Domination free function P**: Para m ≠ m', P(m') não domina P(m) (si' ≥ si ∀i); essencial para Winternitz
- **Hash chain**: Sequência f(0)(x), f(1)(x), ..., f(d)(x) com base x e topo y = f(d)(x)
- **One-way on d iterates**: Dado y = f(j)(x), difícil encontrar x' tal que f(x') = y para todo j ∈ {1,...,d}
- **q-indexed signature**: Message space M = {1,...,q} × M'; adversário consulta índices u1,...,uq distintos
- **Merkle tree traversal**: Computar Merkle(1),...,Merkle(q) sequencialmente em tempo amortizado O(log q)
- **Enhanced TCR**: Target collision resistance com nonce; permite v = 130 bits vs. v = 256 (clássico)

## Mental models
- Use Lamport quando precisa one-time signature mais simples (2v keys, v elementos na assinatura)
- Use Winternitz quando pode trocar tempo de verificação por tamanho (d=15: 4× menor, mas 4× mais lento)
- Use HORST quando pk grande é aceitável mas quer assinatura curta (n=1024 → σ com 44 elementos)
- Use Merkle stateless quando precisa many-time sem manter estado (custo: qd deve ser super-poly, ex. 2^160)
- Use nonce-based Merkle quando pode manter contador (permite qd = 2^40 vs. 2^160 stateless)
- Use TESLA quando broadcast + relógios sincronizados + delayed authentication é aceitável

## Anti-padroes
- **Reusar leaf em Merkle tree**: Gera múltiplas assinaturas sob mesmo q-indexed key, quebra segurança completamente
- **Gerar novos keypairs para nós internos**: Observador vê >q assinaturas sob mesmo pk, viola premissa q-time
- **Usar mesma função f globalmente**: Multi-key attack com √|Y| public keys permite forgery (Exercise 14.2)
- **Ignorar post-quantum parameters**: v=130 seguro classicamente, mas quantum adversary quebra em 2^65 (precisa v=256)
- **Omitir nonce/position em hash chain**: Vulnerável a pre-processing attacks (Remark 14.1)

## Exemplos de codigo / Tabelas

```python
# Optimized Lamport Popt
def Popt(m):  # m ∈ {0,1}^v
    c = v - weight(m)  # checksum = número de 0s
    m' = m || encode_binary(c, log2(v)+1)
    return {i : m'[i] = 1}  # índices dos bits 1

# Winternitz P (base d+1)
def P_winternitz(m):  # m ∈ {0,1}^v
    s = parse_base(m, d+1, n0)  # (s1,...,sn0)
    c = d*n0 - sum(s)  # checksum
    c_digits = parse_base(c, d+1, n1)
    return s || c_digits  # ∈ {0,...,d}^n

# Merkle signing (simplified)
def S_merkle(sk, m):
    a = random_leaf()  # (a1,...,ad) ∈ {1,...,q}^d
    path_sigs = []
    for i in 1..d-1:
        r = F(k, (a1,...,ai))
        (pk_i, sk_i) = G_q(r)
        σ_i = S_q(sk_{i-1}, (a_i, pk_i))
        path_sigs.append((pk_i, σ_i))
    σ_d = S_q(sk_{d-1}, (a_d, m))
    return (a, path_sigs, σ_d)
```

**Concrete parameters (v=256, X=Y={0,1}^256):**

| Scheme | d | n | Combined size |
|--------|---|---|---------------|
| Lamport | 1 | 265 | 8.5 KB |
| Winternitz | 3 | 133 | 4.2 KB |
| Winternitz | 15 | 67 | 2.1 KB |
| Winternitz | 1023 | 28 | 0.9 KB |

**HORS parameters (n choose ℓ ≥ 2^256):**

| n | min ℓ | pk size | sig size |
|---|-------|---------|----------|
| 512 | 58 | 512|Y| | 58|X| |
| 1024 | 44 | 1024|Y| | 44|X| |
| 2048 | 36 | 2048|Y| | 36|X| |

## Worked Example

**Winternitz com n=9, d=3, mensagem m onde P(m)=(2,1,2,3,2,1,0,2,1):**

1. **Key generation**: 
   - sk: x1,...,x9 ← PRF(k, 1),...,PRF(k, 9)
   - pk: y1=f^(3)(x1),...,y9=f^(3)(x9), depois H(y1,...,y9)

2. **Signing m**:
   - Compute P(m) = (2,1,2,3,2,1,0,2,1)
   - σ = (f^(2)(x1), f^(1)(x2), f^(2)(x3), f^(3)(x4), f^(2)(x5), f^(1)(x6), f^(0)(x7), f^(2)(x8), f^(1)(x9))

3. **Verification**:
   - Para cada i: compute ŷi = f^(d-si)(σi) = f^(3-si)(σi)
   - Check H(ŷ1,...,ŷ9) = pk
   - Exemplo: ŷ1 = f^(3-2)(σ1) = f(f^(2)(x1)) = f^(3)(x1) = y1 ✓

**Security intuition**: Adversário vê "corte" através do retângulo 9×3. Para forjar m' com P(m')=(s'1,...,s'9), precisa inverter f em algum yi onde s'i < si (domination free garante isso existe).

## Key takeaways

1. One-time signatures de hash functions são pós-quânticas e rápidas, mas assinaturas longas (trade-off fundamental)
2. Winternitz reduz tamanho via hash chains: d=15 dá 4× redução vs. Lamport, mas verificação 4× mais lenta
3. Merkle transforma one-time em many-time: stateless precisa qd super-poly (2^160), nonce-based permite qd=2^40
4. PRF F(k, node_id) gera keys deterministicamente, resolve key management sem estado
5. TESLA usa hash chain reversa + delayed authentication para broadcast MAC com 160 bits/slot
6. Enhanced TCR permite v=130 (clássico) mas post-quantum força v=256
7. Online/offline pattern: fase offline gera (pk1, σ0=S(sk, pk1)), fase online S1(sk1, m) é rápida
8. HORST + Merkle tree: pk curta (1 hash), assinatura ℓ elementos + log2(n/ℓ) tree nodes

## Conecta com
- Cap 8.11: One-way functions (base de Lamport)
- Cap 8.9: Merkle trees (comprimir pk em HORST, autenticar leaves)
- Cap 13: RSA signatures (comparação: RSA 256 bytes vs. Winternitz 2.1 KB, mas RSA não pós-quântico)
- Cap 16.5: Quantum attacks (motivação para hash-based: RSA quebra, Lamport resiste)
- Exercise 8.27: Enhanced TCR (permite v=130 clássico, mas v=256 pós-quântico)
- Exercise 13.2: Multi-key security (q-indexed construction usa plug-and-pray)
