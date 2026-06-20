# Capitulo 13: Digital signatures

## Ideia central
Assinaturas digitais permitem que qualquer pessoa verifique a autenticidade de dados assinados por uma entidade especifica, sem necessidade de chaves compartilhadas. Diferem de assinaturas fisicas por serem funcao dos dados assinados e fornecerem non-repudiation limitado.

## Frameworks introduzidos
- **Full Domain Hash (FDH)**: Assina I(sk, H(m)) onde H mapeia mensagens para dominio completo da trapdoor permutation (usar quando precisar de assinatura provavel em random oracle model)
- **RSA-FDH**: Instanciacao de FDH com RSA; σ = H(m)^d mod n (usar para verificacao rapida com e pequeno)
- **RSA-FDH'**: Variante com bit aleatorio b; assina H(b,m) onde b = F(k,m) via PRF (usar quando precisar de reducao tight ao RSA)
- **PKCS1 v1.5**: Padding estruturado (00 01 FF...FF 00 DI || H(m)) antes de assinar (padrao legado para certificados X.509)
- **Signcryption**: Combina confidencialidade e autenticidade em setting de multiplos usuarios sem chaves compartilhadas (usar em mensageria end-to-end com usuarios offline)
- **Encrypt-then-Sign (EtS)**: c ← E(pk_R, m, id_S); σ ← S(sk_S, (c, id_R)) (requer CCA encryption + strongly secure signatures)
- **Sign-then-Encrypt (StE)**: σ ← S(sk_S, (m, id_R)); c ← E(pk_R, (m,σ), id_S) (requer CCA encryption + secure signatures; fornece forward secrecy naturalmente)
- **Diffie-Hellman Signcryption (SC_DH)**: Deriva k = H(g^α, g^β, g^(αβ), id_S, id_R); c ← E_s(k,m) (usar quando todos usuarios compartilham mesmo grupo; fornece forward secrecy)

## Conceitos-chave
- **Existential forgery**: Par (m,σ) valido onde m nao foi previamente assinado pelo challenger (adversario vence se produzir isso)
- **Chosen message attack**: Adversario pode requisitar assinaturas em mensagens arbitrarias antes de produzir forgery
- **Strongly unforgeable**: Adversario nao pode produzir nova assinatura σ' mesmo em mensagem ja assinada (m,σ)
- **Message confusion**: Signer produz σ valido para dois m distintos (evitar via collision-resistant hash no commitment)
- **Signer confusion**: Atacante gera pk' tal que (m,σ) valido para pk e pk' (evitar via strongly binding signatures)
- **Random self-reducibility (RSA)**: Propriedade que permite mapear desafio y para y' = x^e · y randomizado (essencial para tight reduction)
- **t-repeated one-way problem**: Dado f(x_1)...f(x_t), revelar alguns x_i, inverter em posicao nao-revelada (reducao generica tem fator t; RSA consegue ~Q via self-reducibility)
- **Non-repudiation**: Assinatura serve como evidencia que signer comprometeu-se com mensagem (limitado: signer pode alegar roubo de chave)
- **Forward secrecy (signcryption)**: CCA security mantida mesmo se sk_S vazado apos encryption (StE e SC_DH fornecem; EtS requer unique signatures)
- **Double-Interactive CDH (I2CDH)**: Computar g^(αβ) dado (g^α, g^β) com acesso a oraculos DDH para pares (g^α, ·, ·) e (·, g^β, ·)

## Mental models
- Use FDH quando tiver trapdoor permutation e aceitar random oracle model (reducao tem fator Q_ro+Q_s)
- Use RSA-FDH' quando precisar tight reduction (fator ~2 vs ~Q_s) mas aceitar assinaturas nao-unicas
- Use hash-and-sign para estender message space: assine H(m) em vez de m (requer collision resistance ou TCR)
- Use signcryption quando precisar confidencialidade+autenticidade sem shared keys e receptor offline
- Prefira StE sobre EtS se forward secrecy for critica (EtS requer unique signatures para forward secrecy)
- Use SC_DH quando todos usuarios aceitarem mesmo grupo e forward secrecy for essencial

## Anti-padroes
- **Assinar RSA sem hash**: σ = m^d permite universal forgery via r^e · m (atacante escolhe r, pede assinatura em m' = r^e·m, computa σ/r)
- **PKCS1 sem validar comprimento total**: Aceitar D com bits extras apos hash permite Bleichenbacher forge via cube root aproximado
- **Usar e=3 com PKCS1 mal implementado**: Atacante computa s = ∛(D·2^(t-w)) e forja x tal que x³ contem padding valido
- **MAC-then-encrypt para signcryption**: Inseguro mesmo com CCA encryption (diferente de symmetric AE)
- **Ignorar identidades em signcryption**: Omitir id_S ou id_R permite confusion attacks
- **Assumir non-repudiation legal**: Signer pode repudiar alegando key theft; assinaturas sao ferramenta criptografica, nao juridica

## Exemplos de codigo / Tabelas

```python
# RSA-FDH (simplified)
def KeyGen(ℓ, e):
    (n, d) ← RSAGen(ℓ, e)
    return pk=(n,e), sk=(n,d)

def Sign(sk, m):
    y = H(m)  # H: M → {1,...,2^(2ℓ)-2}
    σ = y^d mod n
    return σ

def Verify(pk, m, σ):
    y = σ^e mod n
    return (y == H(m))

# RSA-FDH' (tight reduction)
def Sign'(sk=(k,n,d), m):
    b = F(k, m)  # PRF output ∈ {0,1}
    y = H(b, m)
    σ = y^d mod n
    return (b, σ)

def Verify'(pk=(n,e), m, (b,σ)):
    y = σ^e mod n
    return (y == H(b,m))

# Encrypt-then-Sign
def EtS_Encrypt(sk_S, id_S, pk_R, id_R, m):
    c ← E(pk_R, m, id_S)  # associated data = id_S
    σ ← S(sk_S, (c, id_R))
    return (c, σ)

def EtS_Decrypt(pk_S, id_S, sk_R, id_R, (c,σ)):
    if V(pk_S, (c,id_R), σ) = reject: return reject
    return D(sk_R, c, id_S)

# Sign-then-Encrypt
def StE_Encrypt(sk_S, id_S, pk_R, id_R, m):
    σ ← S(sk_S, (m, id_R))
    c ← E(pk_R, (m,σ), id_S)
    return c

def StE_Decrypt(pk_S, id_S, sk_R, id_R, c):
    (m,σ) ← D(sk_R, c, id_S)
    if (m,σ) = reject: return reject
    if V(pk_S, (m,id_R), σ) = reject: return reject
    return m
```

**PKCS1 v1.5 Structure (t bits total):**
```
D: [00 01][FF FF ... FF FF][00][DigestInfo][H(m)]
    ↑      ↑                 ↑   ↑           ↑
   16bits  variable padding  8   19 bytes    h bits
                                 (SHA256)
```

**Concrete Security Bounds:**
| Scheme | Reduction | Factor |
|--------|-----------|--------|
| FDH (general) | OW trapdoor | Q_ro + 1 |
| RSA-FDH | RSA | 2.72·(Q_s+1) |
| RSA-FDH' | RSA | 2 |

## Worked Example

**Bleichenbacher attack on PKCS1 with e=3:**

Setup: RSA modulus n (t bits), verifier aceita D sem validar bits apos hash

Objetivo: Forjar assinatura em m arbitrario

1. Compute w = maior multiplo de 8 menor que t/3 - 3
2. Construa D curto (w bits): `00 01 FF...FF 00 DI || SHA256(m)`
3. Compute s = ∛(D · 2^(t-w)) sobre reais (arredondar para cima → x)
4. Output x como assinatura

Verificacao de corretude:
- 0 ≤ x - s < 1, entao 0 ≤ x³ - D·2^(t-w) < 3(s+1)²
- Como s³ = D·2^(t-w) < 2^t e (s+1)² ≤ 2·2^(2t/3), temos:
  x³ = D·2^(t-w) + J onde 0 ≤ J < 2^(t-w)
- Quando verifier computa x³ mod n (sem wrap), top w bits = D
- Verifier aceita porque padding e hash estao corretos

Mitigacao: Rejeitar se D nao tem comprimento exato ou contem bits extras

## Key takeaways

1. **Assinaturas digitais ≠ assinaturas fisicas**: Sao funcao dos dados; non-repudiation e limitado (key theft, deliberate leak)
2. **Hash e essencial para FDH**: Sem H, atacante escolhe σ aleatorio, computa m=F(pk,σ) para existential forgery trivial
3. **Random oracle proofs nao garantem seguranca concreta**: FDH seguro em RO model mas nao provavel com H concreto sob RSA assumption
4. **Tight reductions importam**: RSA-FDH' (fator 2) vs RSA-FDH (fator Q_s) via random self-reducibility + PRF para mascarar qual assinatura B conhece
5. **PKCS1 e partial domain hash**: H mapeia para intervalo pequeno I ⊂ Z_n; proof breaks porque nao conseguimos sample y uniforme em I com eth root conhecido
6. **Implementacao importa**: Bleichenbacher attack explora validacao incompleta (nao checar bits extras); sempre validar formato completo
7. **Signcryption combina encryption + signatures**: Requer binding de identidades a public keys (via directory ou certificates)
8. **EtS vs StE trade-offs**: Ambos seguros mas EtS requer strongly secure signatures e unique signatures para forward secrecy; StE fornece forward secrecy naturalmente
9. **Forward secrecy protege contra sender corruption**: Adversario com sk_S nao decripta ciphertexts antigos para Bob (StE e SC_DH fornecem)
10. **Signcryption nao previne replay**: Protocolo de nivel superior deve incluir nonces/timestamps para freshness

## Conecta com

- Cap 6 (MACs): Assinaturas sao analogo assimetrico; MAC e binding (ambos podem gerar tag), assinatura e non-binding limitado
- Cap 8 (Hash functions): Collision resistance necessaria para hash-and-sign; TCR suficiente com overhead logaritmico
- Cap 9 (Authenticated encryption): Signcryption e analogo public-key; EtS/StE espelham EtM/MtE mas com diferentes requisitos
- Cap 10 (Trapdoor permutations): FDH requer trapdoor para inverter H(m); RSA e unica instanciacao pratica
- Cap 12 (CCA security): EtS e StE requerem CCA-secure encryption (nao apenas CPA como em symmetric AE)
- Cap 14 (Hash-based signatures): Alternativa post-quantum sem trapdoor permutations; assinaturas longas mas rapidas
- Cap 15 (Discrete log signatures): DSA/Schnorr fornecem assinaturas curtas sem random oracle model
- Cap 21 (Key exchange): SC_DH usa non-interactive DH; I2CDH assumption necessaria para security proof
