# Capitulo 19: Identification and signatures from Sigma protocols

## Ideia central
Protocolos Sigma permitem provar conhecimento de um segredo (witness) sem revela-lo, servindo como base para esquemas de identificacao seguros contra eavesdropping e assinaturas eficientes (via Fiat-Shamir) sob o modelo random oracle.

## Frameworks introduzidos
- **Schnorr Identification Protocol**: Prova conhecimento de  tal que g = u via commitment ut = gt, challenge c, response z = t + c (seguro contra eavesdropping sob DL assumption)
- **Sigma Protocol**: Estrutura generica (commitment t  challenge c  response z) com verificacao deterministica (base para identificacao e assinaturas)
- **Fiat-Shamir Transform**: Converte Sigma protocol em assinatura substituindo verifier por hash: c = H(m, t),  = (t, z) (seguro no random oracle model)
- **Okamoto Protocol**: Prova conhecimento de representacao (, ) tal que gh = u (seguro contra active attacks sob DL)
- **Chaum-Pedersen Protocol**: Prova que (u, v, w) e DH-triple sem revelar  (v = g, w = u)
- **Guillou-Quisquater (GQ) Protocol**: Prova conhecimento de raiz e-esima sob RSA (xe = y)
- **Generic Linear Protocol**: Framework unificado para relacoes lineares  n j=1 gijxj = ui em grupos
- **AND-proof**: Combina dois Sigma protocols para provar conhecimento de ambos witnesses (mesmo challenge space)
- **OR-proof**: Prova conhecimento de um witness entre dois statements sem revelar qual (usa simulador para branch nao-conhecida)

## Conceitos-chave
- **Witness**: Valor secreto x tal que (x, y)  R (ex: discrete log, representacao, raiz RSA)
- **Special soundness**: Extrator eficiente computa witness de duas accepting conversations (t, c, z), (t, c', z') com c  c'
- **Special HVZK (Honest Verifier Zero Knowledge)**: Simulador Sim(y, c) gera conversations indistinguiveis de interacoes reais sem conhecer witness
- **Accepting conversation**: Tripla (t, c, z) que passa verificacao do verifier (ex: gz = ut · uc para Schnorr)
- **Challenge space C**: Conjunto de desafios; deve ser super-poly para seguranca (tipicamente C  Zq ou {0,1}n)
- **Witness independence**: Conversacoes nao revelam qual witness foi usado (mesmo para cheating verifiers)
- **One-way key generation**: Dificil computar witness x dado statement y = pk (necessario para seguranca)
- **Unpredictable commitments**: Commitment t gerado por prover honesto e imprevisivel (probabilidade  negligivel)
- **Rewinding Lemma**: Tecnica para extrair witness executando prover duas vezes com challenges distintos
- **Multi-extractability**: Extrator obtem witnesses de multiplos statements aceitos via rewinding controlado

## Mental models
- Use Schnorr quando precisar provar conhecimento de discrete log com eficiencia maxima (1 exponenciacao no prover)
- Use Okamoto quando precisar seguranca contra active attacks (duas bases g, h impedem simulacao de probing phase)
- Use Fiat-Shamir quando precisar assinaturas de Sigma protocol (hash substitui verifier interativo)
- Use OR-proof quando precisar provar "conheco witness de y0 OU y1" sem revelar qual (criptografia anonima, ring signatures)

## Anti-padroes
- **Challenge space pequeno**: Adversario pode adivinhar challenge com probabilidade 1/|C| (exige |C| super-poly)
- **Randomness reutilizada em assinaturas**: Mesmo t em duas assinaturas vaza secret key (ataque Sony PS3, Bitcoin wallets) -- use deterministic nonce
- **Ignorar witness independence**: Probing phase pode vazar qual witness foi usado se protocolo nao for WI
- **Aplicar Fiat-Shamir sem special HVZK**: Simulador deve aceitar challenge como input e sempre produzir accepting conversation

## Exemplos de codigo / Tabelas

```python
# Schnorr Sigma Protocol
def prover(alpha, u):  # witness alpha, statement u = g^alpha
    t = random(Zq)
    u_t = g**t
    # ... await challenge c ...
    z = t + c * alpha  # mod q
    return (u_t, z)

def verifier(u, u_t, c, z):
    return g**z == u_t * u**c

# Witness extractor (special soundness)
def extract(u, u_t, c, z, c_prime, z_prime):
    # From g^z = u_t * u^c and g^z' = u_t * u^c'
    delta = z - z_prime
    delta_c = c - c_prime
    alpha = delta / delta_c  # mod q
    return alpha  # witness for u

# Simulator (special HVZK)
def simulate(u, c):
    z = random(Zq)
    u_t = g**z / u**c
    return (u_t, z)  # accepting conversation

# Fiat-Shamir signature
def sign(m, alpha):
    t = random(Zq)
    u_t = g**t
    c = H(m, u_t)  # hash substitui verifier
    z = t + c * alpha
    return (u_t, z)

def verify(m, sigma, u):
    (u_t, z) = sigma
    c = H(m, u_t)
    return g**z == u_t * u**c
```

**Reducao de seguranca (Schnorr signature):**
```
SIGadv[A]  Qs(Qs+Qro+1)/q + (Qro+1)/N + sqrt((Qro+1)*DLadv[B])
```
onde Qs = signing queries, Qro = random oracle queries, N = |C|

## Worked Example

**Provando seguranca de Schnorr identification contra direct attacks:**

Setup: Adversario A tem advantage  em Attack Game 18.1. Construimos DL adversary B.

1. **Input**: B recebe u = g (discrete log challenge)
2. **Stage 1 - primeira execucao**:
   - B envia u como verification key para A
   - A envia commitment ut
   - B responde com challenge c  C aleatorio
   - A responde com z
   - Se gz = ut·uc, temos accepting conversation (ut, c, z)

3. **Stage 2 - rewinding**:
   - B "rebobina" A para estado apos ut
   - B envia novo challenge c'  C
   - A responde com z'
   - Se gz' = ut·uc', temos segunda accepting conversation

4. **Extracao**:
   - Com prob  2-/N (Rewinding Lemma), obtemos c  c'
   - De gz = ut·uc e gz' = ut·uc':
     * g = uc onde  = z-z', c = c-c'
     * Como c  0 mod q (q primo), existe (c)-1
     *  = /c mod q
   - B retorna  = Dloggu

**Conclusao**: Se A quebra identificacao com prob , entao B resolve DL com prob  2-/N, provando seguranca sob DL assumption (desde que |C| super-poly).

## Key takeaways
1. Special soundness + special HVZK + large challenge space = secure identification (contra eavesdropping)
2. Fiat-Shamir transforma qualquer Sigma protocol em assinatura segura no random oracle model
3. Witness independence (implicada por special HVZK) permite seguranca contra active attacks via OR-proof
4. Rewinding e tecnica central: extrai witness de duas accepting conversations com challenges distintos
5. Challenge space deve ser super-poly; commitment deve ser unpredictable
6. Generic linear protocol unifica Schnorr, Okamoto, Chaum-Pedersen como casos especiais
7. AND/OR-proofs compoem Sigma protocols preservando special soundness e HVZK
8. GQ protocol prova conhecimento de raiz RSA; base para assinaturas RSA rapidas
9. Okamoto identification (duas bases g, h) e seguro contra active attacks sob DL
10. Deterministic nonce generation (Ex 13.6) previne ataques de bad randomness

## Conecta com
- Cap 18: Identification protocols (direct/eavesdropping/active attacks)
- Cap 13: Digital signatures (Attack Game 13.1, random oracle model)
- Cap 10: Discrete logarithm (DL assumption, representations, DH-triples)
- Cap 20: Proofs of knowledge avancados (range proofs, voting protocols)
- Theorem 10.6: RSA inversion de colisoes (usado em GQ extractor)
- Exercise 13.6: Deterministic signature generation (previne bad randomness)
