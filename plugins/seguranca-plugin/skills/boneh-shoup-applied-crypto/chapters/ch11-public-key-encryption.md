# Capitulo 11: Public key encryption

## Ideia central
Public-key encryption permite que Alice envie mensagens cifradas para Bob usando apenas a chave pública de Bob (sem compartilhar segredos previamente), enquanto apenas Bob pode decifrar usando sua chave secreta correspondente.

## Frameworks introduzidos
- **Public-Key Encryption Scheme**: Tripla E = (G, E, D) onde G gera (pk, sk), E cifra com pk, D decifra com sk (usar quando não há canal seguro prévio para troca de chaves)
- **Semantic Security (SS)**: Adversário não distingue cifras de m₀ vs m₁ dado pk (Attack Game 11.1: SSadv[A,E] negligível)
- **CPA Security (public-key)**: Extensão de SS permitindo múltiplas queries de cifra (implícita em SS no cenário public-key, Theorem 11.1)
- **Trapdoor Function Encryption (ETDF)**: E(pk,m) = (y=F(pk,x), c=Es(H(x),m)) onde x←X aleatório (usar com RSA + hash + cipher simétrico)
- **ElGamal Encryption (EEG)**: E(pk=u,m) = (v=g^β, c=Es(H(v,u^β),m)) em grupo cíclico G (usar com DDH/CDH + KDF)
- **Key Derivation Function (KDF)**: F:X×Y→Z onde (x, F(x,y)) ≈ (x, z) para y,z aleatórios (Attack Game 11.3)
- **Oblivious Transfer (1-out-of-n OT)**: Protocolo onde receiver obtém mᵢ de {m₁,...,mₙ} sem sender aprender i (usar para compra privada de conteúdo)
- **Oblivious PRF (OPRF)**: Protocolo onde receiver computa F(k,x) sem aprender k, sender não aprende x (usar para adaptive OT)
- **Key Encapsulation Mechanism (KEM)**: Ekem(pk)→(k,ckem) gera chave simétrica + encapsulação (modulariza construção híbrida)

## Conceitos-chave
- **Asymmetric encryption**: Cifrador usa pk, decifrador usa sk diferente (vs symmetric onde ambos usam mesma chave)
- **Randomized encryption**: E deve ser probabilístico (determinístico é inseguro: adversário testa E(pk,m₀)=c?)
- **Random oracle model**: H modelado como função aleatória com queries explícitas (prova segurança mas não garante implementação real)
- **Hybrid encryption**: Combina KEM assimétrico + cipher simétrico (eficiência: cifra longa usa Es rápido)
- **One-wayness**: Difícil inverter F(pk,x) dado y=F(pk,x) (mais fraco que SS mas suficiente com random oracle)
- **CDH assumption**: Difícil computar g^(αβ) dados g^α, g^β (base para ElGamal no random oracle model)
- **DDH assumption**: (g^α, g^β, g^(αβ)) ≈ (g^α, g^β, g^γ) (mais forte que CDH, permite ElGamal sem random oracle)
- **1MDH assumption**: Adversário com Q queries CDH não resolve Q+1 instâncias (garante OPRF: receiver não aprende >Q valores)
- **Key escrow**: Servidor com pk_ES permite recuperação de arquivos cifrados (manager acessa arquivo de Alice ausente)
- **Adaptive OT**: Sender cifra m₁,...,mₙ uma vez; receiver abre múltiplos mᵢ interativamente (eficiente para jornais/lojas digitais)

## Mental models
- Use public-key quando não há canal seguro prévio (email cifrado sem setup)
- Use ETDF quando tem trapdoor function + quer prova no random oracle model (RSA clássico)
- Use ElGamal quando tem grupo DDH + quer evitar random oracle (ou CDH com random oracle como hedge)
- Use KEM+cipher para modularizar: KEM gera chave efêmera, cipher processa mensagem longa

## Anti-padroes
- **Encryption determinístico**: Adversário testa E(pk,m₀)=?c revelando bit (sempre randomize)
- **Reusar randomness em ElGamal**: Múltiplas cifras (v,c₁),...,(v,cₙ) com mesmo β expõem relações (adaptive OT explora isso intencionalmente)
- **Esquecer identidades no hash**: OPRF sem incluir IDs permite man-in-the-middle relay attack (sempre H(parties,data))
- **Usar SS cipher em OT**: Precisa authenticated encryption para detectar sender malicioso (ciphertext integrity crucial)
- **Ignorar group membership**: OPRF1 deve verificar v∈G antes de responder (senão leak de sk via invalid curve attack)
- **Confiar só em DDH**: Se DDH quebrar, ElGamal com random oracle + CDH ainda seguro (defesa em profundidade)

## Exemplos de codigo / Tabelas

```python
# ETDF (RSA-based)
def G():
    (n,d) = RSAGen(ℓ,e)
    return pk=(n,e), sk=(n,d)

def E(pk=(n,e), m):
    x ← Z_n
    y = x^e mod n
    k = H(x)
    c = Es(k, m)
    return (y, c)

def D(sk=(n,d), (y,c)):
    x = y^d mod n
    k = H(x)
    return Ds(k, c)

# ElGamal (EEG)
def G():
    α ← Z_q
    u = g^α
    return pk=u, sk=α

def E(pk=u, m):
    β ← Z_q
    v = g^β
    w = u^β
    k = H(v, w)  # hash (v,w) não só w
    c = Es(k, m)
    return (v, c)

def D(sk=α, (v,c)):
    w = v^α
    k = H(v, w)
    return Ds(k, c)

# OPRF Protocol 2 (malicious sender secure)
# Sender: k∈Z_q, publishes u=g^k
# Receiver: input x
def receiver_step1(x):
    α ← Z_q\{0}
    γ ← Z_q
    v = H(x)^α · g^γ
    return v, (α,γ)

def sender_step2(v, k):
    w = v^k
    return w

def receiver_step3(w, (α,γ), u, x):
    y = H(x, (w/u^γ)^(1/α))
    return y  # = F(k,x) se sender honesto
              # aleatório se sender malicioso
```

## Worked Example

**Adaptive OT para jornal digital:**

Setup: Jornal tem artigos m₁,...,m₁₀₀₀
- Jornal: k←K_prf, para i=1..1000: kᵢ=F(k,i), cᵢ=Es(kᵢ,mᵢ), publica C=(c₁,...,c₁₀₀₀)
- Bob baixa C inteiro (uma vez)

Bob quer ler artigo i=42:
- Bob e jornal executam OPRF: jornal tem k, Bob tem i=42
- Após protocolo: Bob obtém k₄₂=F(k,42), jornal não aprende i
- Bob: m₄₂=Ds(k₄₂,c₄₂)

Segurança:
- Jornal não aprende i: OPRF esconde input do receiver (v=H(42)^α aleatório)
- Bob aprende só m₄₂: Sob 1MDH, Bob não computa F(k,j) para j≠42 sem nova interação
- Eficiência: Tráfego por artigo = O(1), independente de n=1000

Repetição: Bob quer i=137 depois → nova execução OPRF, obtém k₁₃₇

## Key takeaways

1. Public-key elimina necessidade de canal seguro prévio mas exige encryption randomizado (determinístico sempre inseguro)
2. SS implica CPA no cenário public-key (adversário simula encryption queries com pk)
3. ETDF = trapdoor function + hash + symmetric cipher (seguro no random oracle sob one-wayness)
4. ElGamal tem duas provas: CDH+random oracle OU DDH+KDF sem random oracle (hedge contra quebra de DDH)
5. Sempre hash (v,w) em ElGamal, não só w (previne ataques em protocolos interativos)
6. KEM modulariza construção híbrida: prove KEM e cipher separadamente (composição segura)
7. OT básico requer re-encryption por query; adaptive OT com OPRF permite cifras estáticas + aberturas interativas O(1)
8. OPRF Protocol 2 detecta sender malicioso: output errado é aleatório (usa γ para randomizar)
9. Protocolos interativos precisam incluir identidades no hash (previne man-in-the-middle relay)
10. 1MDH garante que receiver aprende ≤Q valores de PRF em Q interações (essencial para segurança de OT)

## Conecta com

- Cap 10 (trapdoor functions, RSA, Diffie-Hellman): primitivas base para ETDF e ElGamal
- Cap 9 (authenticated encryption): necessário em OT para detectar sender malicioso
- Cap 8 (hash functions, KDF): H:G²→K como KDF evita random oracle em ElGamal
- Cap 4 (PRF): OPRF estende PRF para cenário two-party com privacidade mútua
- Cap 12 (chosen ciphertext security): ElGamal básico não é CCA-secure, precisa transformações
- Cap 23 (secure protocols): OT é building block para MPC, definições de segurança mais fortes
