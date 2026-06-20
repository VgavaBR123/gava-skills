# Capítulo 16: Attacks on number theoretic assumptions

## Ideia central
Ataques práticos contra DL, CDH, DDH e RSA exploram estrutura de grupos (ordem composta, primes dependentes, exponentes pequenos) ou falhas de implementação (randomness fraca, fault injection), revelando que segurança exige escolhas cuidadosas de parâmetros e implementação robusta.

## Frameworks introduzidos
- **Baby step/giant step**: Algoritmo O(√q) para DL via meet-in-the-middle; escreve α = β·m + γ e constrói tabela T[g^γ] para γ ∈ [0,m), depois busca u·(g^{-mβ}) em T (usar quando q ≤ 2^64 ou com restrições de intervalo).
- **Pohlig-Hellman**: Reduz DL em grupo de ordem n = q₁^{e₁}···qᵣ^{eᵣ} a DL nos subgrupos de ordem qᵢ^{eᵢ} via CRT; tempo O(T(qₘₐₓ)log n) (usar para detectar grupos vulneráveis com fatores pequenos).
- **GNFS (General Number Field Sieve)**: Fatoração/DL em ℤₚ* em tempo exp(c(ln p)^{1/3}(ln ln p)^{2/3}); permite preprocessing (usar para estimar segurança de primes específicos).
- **Generic group lower bound**: Adversário com T queries tem vantagem ≤ O(T²/q) em DL; prova via lazy sampling de função de rotulação L:ℤq→S (usar para justificar tamanho de q em grupos sem estrutura explorável).
- **Wiener's attack**: Recupera d < n^{1/4}/3 de (n,e) via continued fractions; explora e/n ≈ k/d com |e/n - k/d| < 1/(2d²) (evitar d pequeno em RSA).
- **Fault injection on RSA-CRT**: Assinatura faltosa σ̂ satisfaz σ̂^e ≡ H(m) (mod q) mas σ̂^e ≢ H(m) (mod p); então gcd(σ̂^e - H(m), n) = q (sempre verificar assinatura antes de liberar).

## Conceitos-chave
- **Static Diffie-Hellman (SDH)**: Adversário consulta oráculo v ↦ v^α e deve recuperar α; vulnerável se q±1 tem fatores moderados d via g, g^α, ..., g^{α^d} (mitigar: escolher q com q±1 sem fatores < q^{1/3}).
- **Composite order leakage**: Em grupo de ordem n = 2n₂, teste u^{n/2} = 1 revela paridade de Dlog_g(u); quebra DDH com vantagem 1/2 (sempre usar grupos de ordem prima).
- **RSA-CRT**: Computa x^d mod n via x_p = x^{dₚ} mod p, x_q = x^{dᵧ} mod q, depois CRT; 4× mais rápido mas vulnerável a faults (verificar resultado).
- **Low exponent RSA**: d < n^{1/4}/3 permite recuperação via continued fractions; d < n^{0.3} também inseguro (nunca escolher d pequeno).
- **Dependent primes**: Se |p - q| < 2n^{1/4}, então A = ⌈√n⌉ satisfaz A² - n < 1/2, revelando p,q via (p+q)/2 (gerar p,q independentemente).
- **Non-uniform primes**: Se p ≡ q ≡ 1 (mod S) com S > n^{1/4}, Coppersmith factora n (evitar sieving que introduz viés).
- **Shor's algorithm**: Quantum computer resolve DL e fatoração em tempo O(log³ n) via period finding; força migração para post-quantum crypto (planejar transição).
- **ROCA attack**: Primes p = kS + 1 com S = produto de 80 primes permite fatoração se S > n^{1/4} (evitar otimizações de sieving não-standard).
- **Logjam attack**: Preprocessing GNFS para primes fixos (Oakley groups) permite DL rápido após custo one-time; afeta IPsec, SSH, Tor (usar primes únicos ou grupos EC).
- **ECM (Elliptic Curve Method)**: Fatoração em tempo exp(c√(ln p·ln ln p)) onde p é menor fator; útil para n com fator pequeno (usar para detectar primes mal-formados).

## Mental models
- Use grupos de ordem prima q: ordem composta permite Pohlig-Hellman (tempo dominado por maior fator) e leakage de bits via testes de divisibilidade.
- Escolha q com q±1 sem fatores moderados: SDH adversary com d queries ganha speed-up √(q/d) se q±1 divisível por d.
- Verifique outputs de RSA-CRT: single fault em x_p expõe q via gcd(σ̂^e - H(m), n).
- Evite d pequeno em RSA: Wiener ataca d < n^{1/4}/3; small CRT exponents também vulneráveis.

## Anti-padrões
- **Usar grupos de ordem par**: DDH quebra com vantagem 1/2 via teste u^{n/2} = 1; generaliza para qualquer fator primo pequeno.
- **Gerar primes dependentes**: |p - q| < 2n^{1/4} ou |ap + bq| < n^{1/4} permite fatoração via AMGM; sempre gerar p,q independentemente.
- **Otimizar sieving com viés**: p = kS + 1 com S grande introduz estrutura explorável por Coppersmith; usar geração standard.
- **Reusar primes fixos**: Preprocessing GNFS amortiza custo; usar primes únicos ou grupos EC sem preprocessing conhecido.
- **Não verificar RSA-CRT output**: Fault injection expõe chave; sempre verificar σ^e = H(m) antes de liberar.

## Exemplos de código / Tabelas

### Baby step/giant step
```python
def baby_giant(g, u, q):
    m = ceil(sqrt(q))
    T = {}  # baby steps
    v = 1
    for γ in range(m):
        T[v] = γ
        v = v * g
    
    g_inv_m = pow(g, -m, q)  # giant steps
    v = u
    for β in range(m):
        if v in T:
            return β * m + T[v]
        v = v * g_inv_m
```

### Pohlig-Hellman structure
| n factorization | qₘₐₓ | DL time | Seguro? |
|-----------------|------|---------|---------|
| 2^ℓ | 2 | O(ℓ²) | ✗ |
| q (prime) | q | O(√q) | ✓ |
| 2·q | q | O(√q) | ✓ (mas DDH falso) |
| q₁^{e₁}···qᵣ^{eᵣ} | qₘₐₓ | O(√qₘₐₓ·log n) | Depende de qₘₐₓ |

### NIST prime size recommendations
| AES key (bits) | ℤₚ* prime (bits) [NIST] | ℤₚ* prime (bits) [Lenstra] |
|----------------|-------------------------|----------------------------|
| 80 | 1024 | 1329 |
| 128 | 3072 | 4440 |
| 256 | 15360 | 26268 |

## Worked Example

**Ataque a RSA com d pequeno (Wiener)**

Setup: n = pq com p,q de 1024 bits; adversário vê (n, e) e quer recuperar d < n^{1/4}/3 ≈ 2^{256}/3.

Passo 1: ed = 1 + kφ(n) implica e/φ(n) - k/d = 1/(dφ(n)) < 1/n.

Passo 2: φ(n) = n - p - q + 1 ≈ n (erro < 3√n), então |e/n - k/d| < 4√n/d² < 1/(2d²) se d < n^{1/4}/3.

Passo 3: Compute continued fraction expansion de e/n = [a₀; a₁, a₂, ...]; convergentes pᵢ/qᵢ satisfazem |e/n - pᵢ/qᵢ| < 1/(qᵢqᵢ₊₁).

Passo 4: Lemma 16.6 garante que k/d aparece como convergente; há ≤ 2log₂ n convergentes.

Passo 5: Para cada convergente pᵢ/qᵢ com gcd(pᵢ,qᵢ) = 1, teste se qᵢ é d válido: compute φ̂ = (ed - 1)/pᵢ e verifique se x² - (n - φ̂ + 1)x + n = 0 tem raízes inteiras (que seriam p,q).

Resultado: Recupera d em tempo O(log n) operações aritméticas.

Exemplo concreto: n = 2^{2048}, d = 2^{128} → continued fractions de e/n tem ≈ 4096 convergentes; um deles é k/d.

## Key takeaways
1. Sempre use grupos de ordem prima q: ordem composta permite Pohlig-Hellman (tempo O(√qₘₐₓ)) e quebra DDH via testes de divisibilidade
2. Escolha q com q±1 sem fatores moderados d < q^{1/3}: previne SDH speed-up de √(q/d) via g^{α^i} queries
3. Gere primes RSA independentemente com randomness completa: dependência |p-q| < 2n^{1/4} ou half-randomness (p fixo, q random) permite fatoração via gcd ou AMGM
4. Nunca use d < n^{0.3} em RSA: Wiener ataca d < n^{1/4}/3 via continued fractions; small CRT exponents também vulneráveis
5. Verifique outputs de RSA-CRT antes de liberar: single fault em x_p expõe q via gcd(σ̂^e - H(m), n)
6. Evite primes fixos em protocolos: GNFS preprocessing permite DL rápido após custo one-time (Logjam); use primes únicos ou grupos EC
7. Planeje transição post-quantum: Shor's algorithm resolve DL e fatoração em tempo O(log³ n); tráfego com sigilo >30 anos precisa de PQ crypto hoje

## Conecta com
- Cap. 10.5: Definições de DL, CDH, DDH assumptions
- Cap. 11.6.3: Oblivious PRF via one-more DH (vulnerável a SDH)
- Cap. 15.3: Curvas elípticas (Curve25519, P256) e análise de q±1 factors
- Cap. 15.4: Pairings quebram DDH mas preservam DL
- Exercise 11.5: Multiplicative ElGamal (CCA adversary usa SDH para key recovery)
- Exercise 16.3: Brown-Gallant-Cheon algorithm (speed-up via g^{α^i})
- Section 3.10: RNG initialization (half-randomness em RSA key gen)
- Appendix A: Chinese Remainder Theorem (Pohlig-Hellman, RSA-CRT)
