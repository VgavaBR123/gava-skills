# Capitulo 10: Public key tools

## Ideia central
Ferramentas de criptografia de chave pública (trapdoor functions, Diffie-Hellman, RSA) permitem key exchange seguro contra eavesdropping e construção de hash functions resistentes a colisões, baseadas em problemas computacionais difíceis como discrete logarithm e fatoração.

## Frameworks introduzidos
- **Anonymous Key Exchange Protocol**: Par de máquinas probabilísticas (A,B) que geram transcrito TP e chave compartilhada k; adversário vê TP e tenta adivinhar k (Attack Game 10.1). Usar quando: estabelecer segredo compartilhado sem autenticação prévia.
- **Trapdoor Function Scheme (G,F,I)**: G gera (pk,sk); F(pk,x) é fácil de computar mas difícil inverter sem sk; I(sk,y) inverte usando trapdoor sk. Usar quando: construir key exchange ou encryption schemes.
- **RSA Trapdoor Permutation**: G gera n=pq, e, d; F(pk,x)=x^e mod n; I(sk,y)=y^d mod n. Usar quando: precisar de trapdoor permutation concreta (moduli ≥2048 bits).
- **Diffie-Hellman Key Exchange**: Alice envia g^α, Bob envia g^β, ambos computam g^(αβ). Usar quando: estabelecer chave em grupo cíclico de ordem prima.
- **GUO Accumulator**: Commitment C(S)=g^(∏H(xi)) em grupo de ordem desconhecida; provas de membership (tamanho O(1)) e non-membership. Usar quando: comprometer-se com conjuntos não-ordenados com provas compactas.

## Conceitos-chave
- **One-way trapdoor function**: Função fácil de computar, difícil inverter sem trapdoor secreto sk, mas eficientemente inversível com sk.
- **RSA modulus n=pq**: Produto de primos grandes p,q (≥1024 bits cada); fatoração difícil mas conhecer p,q permite computar φ(n)=(p-1)(q-1).
- **Discrete logarithm (DL)**: Dado g^α, computar α; problema base para segurança Diffie-Hellman.
- **Computational Diffie-Hellman (CDH)**: Dado (g^α, g^β), computar g^(αβ); mais forte que DL.
- **Decisional Diffie-Hellman (DDH)**: Distinguir (g^α, g^β, g^(αβ)) de (g^α, g^β, g^γ); implica CDH.
- **DH-triple**: Tupla (g^α, g^β, g^(αβ)) onde αβ é produto dos expoentes.
- **Representation (α,β)**: Par tal que g^α·h^β=u; duas representations distintas do mesmo u revelam Dlog_g(h).
- **Random self-reduction**: Mapear instância específica para instância aleatória; se problema é fácil em fração ε de inputs, é fácil em todos.
- **Group of unknown order (GUO)**: Grupo G onde |G| é difícil computar; necessário para accumulators seguros.
- **Strong RSA assumption**: Difícil encontrar (x,e) com x^e=g e e≠±1 em grupo de ordem desconhecida.

## Mental models
- Use trapdoor functions quando precisar de one-wayness com "porta dos fundos" secreta (key exchange, encryption).
- Use Diffie-Hellman quando tiver grupo cíclico de ordem prima q onde DL/CDH/DDH são difíceis (subgrupo de Z*_p, elliptic curves).
- Use RSA quando precisar de trapdoor permutation concreta; DDH quando precisar indistinguishability mais forte que CDH.
- Use GUO accumulators quando precisar provas de membership/non-membership de tamanho constante (vs. Merkle trees com provas O(log n)).

## Anti-padroes
- **Man-in-the-middle em anonymous key exchange**: Adversário ativo intercepta g^α de Alice, envia g^α' para Bob; estabelece k_A com Alice e k_B com Bob, vê todo tráfego. Por que falha: falta autenticação de identidades.
- **DDH em grupos de ordem par**: Adversário testa se y^((q-1)/2)=1 para distinguir DH-triples. Por que falha: ordem não-prima permite testes de subgrupo.
- **Usar Z*_p diretamente para DDH**: Grupo tem ordem par p-1. Por que falha: DDH é falso (Exercise 10.24).
- **Merkle puzzles com L pequeno**: Adversário quebra em tempo O(L²) vs. O(L) dos participantes. Por que falha: separação apenas quadrática, não exponencial.
- **Accumulator sem collision-resistant hash**: Adversário encontra x≠y com H(x)=H(y), cria false proofs. Por que falha: gcd(H(x),E)>1 permite non-membership proof inválido.

## Exemplos de codigo / Tabelas

```python
# RSA Key Generation
RSAGen(ℓ, e):
    p ← random ℓ-bit prime, gcd(e,p-1)=1
    q ← random ℓ-bit prime, gcd(e,q-1)=1, q≠p
    n ← pq
    d ← e^(-1) mod (p-1)(q-1)
    return (n,d)

# RSA Trapdoor Permutation
G(): (n,d) ← RSAGen(ℓ,e); pk←(n,e); sk←(n,d)
F(pk,x): return x^e mod n
I(sk,y): return y^d mod n

# Diffie-Hellman Key Exchange
Alice: α ← Z_q; u←g^α; send u
Bob:   β ← Z_q; v←g^β; send v
Alice: w ← v^α = g^(αβ)
Bob:   w ← u^β = g^(αβ)

# DL-based CRHF
H_dl(α,β) := g^α · h^β  (collision → Dlog_g(h))

# RSA-based CRHF (e prime)
H_rsa(a,b) := a^e · y^b mod n, a∈Z_n, b∈{0,...,e-1}

# GUO Accumulator
C(S) := g^(∏_{x∈S} H(x))
Membership proof π_x := g^(E/H(x))
Verify: π_x^(H(x)) = c
Non-membership proof π_{¬x} := (b,μ) where b=g^μ, μ·H(x)+ν·E=1
Verify: b^(H(x))·c^ν = g
```

**Shamir's trick** (Theorem 10.6): Dado w^e=y^f com gcd(e,f)=1, computar x^e=y:
```
Compute s,t: es+ft=1 (extended Euclidean)
x := y^s · w^t  ⟹  x^e = y
```

## Worked Example

**Key exchange via RSA trapdoor function**:
1. Alice gera (n,d)←RSAGen(ℓ=1024, e=3), envia pk=(n,e) para Bob
2. Bob escolhe x←Z_n aleatório, computa y←x³ mod n, envia y
3. Alice computa x←y^d mod n
4. Segredo compartilhado: x

**Adversário vê**: (n,e,y). Para recuperar x, precisa computar ∛y mod n, equivalente a fatorar n (RSA assumption). Com ℓ=1024, adversário precisa ~2^80 operações.

**GUO accumulator com S={x₁,x₂,x₃}**:
- Setup: (G,g) grupo de ordem desconhecida, H:X→Primes(256)
- Commitment: e₁=H(x₁)=2, e₂=H(x₂)=3, e₃=H(x₃)=5; E=2·3·5=30; c=g^30
- Membership proof x₂: π=g^(30/3)=g^10; verificação: (g^10)³=g^30=c ✓
- Non-membership proof x₄ (H(x₄)=7): gcd(7,30)=1; extended Euclidean: 7·(-4)+30·1=1; π=(g^1,-4); verificação: (g^1)^7·c^(-4)=g^7·g^(-120)=g^(-113)≡g (mod order) se ajustar μ

## Key takeaways
1. Trapdoor functions permitem key exchange eficiente (O(n) vs. O(n²) Merkle puzzles) mas requerem computational assumptions (RSA, DL).
2. RSA assumption: difícil computar x de x^e mod n sem fatorar n; usar ℓ≥2048 bits, e primo pequeno (3,65537).
3. DL/CDH/DDH formam hierarquia: DDH⟹CDH⟹DL; DDH requer grupos de ordem prima (falso em ordem par).
4. Random self-reduction: se problema é fácil em fração ε de inputs, é fácil em todos (Theorem 10.2); implica hardness average-case de worst-case.
5. Collision-resistant hash de DL: H(α,β)=g^α·h^β; colisão revela Dlog_g(h) via Fact 10.3.
6. Collision-resistant hash de RSA: H(a,b)=a^e·y^b; colisão permite computar e-th root de y via Shamir's trick.
7. Anonymous key exchange é inseguro contra adversários ativos (man-in-the-middle); requer autenticação (Chapter 21).
8. GUO accumulators: provas O(1) vs. Merkle O(log n); suportam aggregation (múltiplas proofs em 1 elemento); requerem strong RSA assumption.
9. Diffie-Hellman: usar subgrupo de ordem prima q em Z*_p (p≥2048 bits, q≥256 bits) ou elliptic curves; nunca reusar expoentes.
10. Accumulator dynamic: adicionar x a S requer apenas c'←c^(H(x)); provas antigas permanecem válidas.

## Conecta com
- Chapter 8 (Collision-resistant hashing): Hdl e Hrsa são CRHFs sob DL/RSA assumptions
- Chapter 21 (Authenticated key exchange): resolver man-in-the-middle com signatures/certificates
- Chapter 13 (Digital signatures): RSA signatures via trapdoor permutations
- Chapter 15 (Elliptic curves): grupos alternativos para DL/CDH/DDH com encodings compactos
- Chapter 16 (Attacks on RSA/DL): análise de segurança concreta, escolha de parâmetros
- Section 4.7 (Ideal cipher model): análise de Merkle puzzles
- Section 8.4 (Merkle-Damgård): usar Hrsa como compression function
- Section 8.9 (Merkle trees): comparação com GUO accumulators (proofs O(log n) vs. O(1))
