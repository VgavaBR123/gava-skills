# Capitulo 3: Stream ciphers

## Ideia central
Stream ciphers estendem uma seed curta em uma string longa pseudorandomica usando um PRG (pseudo-random generator), permitindo criptografia semanticamente segura com chaves curtas, mas sao frageis e inseguros se usados incorretamente (ex.: reutilizacao de chave).

## Frameworks introduzidos
- **Pseudo-Random Generator (PRG)**: Algoritmo deterministico eficiente G: S → R que expande seed curta em output longo, onde G(s) e computacionalmente indistinguivel de string verdadeiramente aleatoria (Attack Game 3.1: adversario recebe r ← G(s) ou r ← R e tenta adivinhar qual). Use quando precisar expandir entropia limitada mantendo seguranca semantica.
- **Stream Cipher**: E(s,m) := G(s)[0..v-1] ⊕ m, D(s,c) := G(s)[0..v-1] ⊕ c. Semanticamente seguro se G e PRG seguro (Theorem 3.1: SSadv[A,E] = 2·PRGadv[B,G]).
- **Statistical Test**: Algoritmo que distingue G(s) de string aleatoria outputando 0/1. Efetivo se |Pr[output 1 | pseudo-random] - Pr[output 1 | random]| e nao-negligivel.
- **Unpredictability (Next Bit Test)**: PRG e unpredictable se dado G(s)[0..i-1], adversario nao consegue prever G(s)[i] com vantagem nao-negligivel (Attack Game 3.2). Equivalente a seguranca (Theorem 3.6: PRGadv = L·Predadv).
- **n-wise Parallel Composition**: G'(s₁,...,sₙ) := (G(s₁),...,G(sₙ)). Seguro se G e seguro; vantagem degrada linearmente: PRGadv[A,G'] = n·PRGadv[B,G] (Theorem 3.2).
- **n-wise Sequential Composition (Blum-Micali)**: G'(s) computa (r₁,s₁)←G(s), (r₂,s₂)←G(s₁),..., output (r₁,...,rₙ,sₙ). Seguro se G e seguro; mesma degradacao linear (Theorem 3.3).
- **Hybrid Argument**: Tecnica de prova que constroi sequencia de jogos intermediarios (Hybrid 0,...,Hybrid n) interpolando entre experimentos 0 e 1, mostrando que adversario nao distingue hybrids adjacentes.
- **Distinguisher/Predictor Lemma (Lemma 3.5)**: Se d distingue B de R com vantagem ε, entao predictor B̂ := R se d(X,R)=1 senao R̄ acerta B com probabilidade 1/2+ε. Converte distinguishing em predicting advantage.
- **Computational Indistinguishability**: Distribuicoes P₀,P₁ sao comp. indist. se Distadv[A,P₀,P₁] negligivel para todo A eficiente (Attack Game 3.3). Generaliza seguranca de PRG.
- **Statistical Distance**: Δ[P₀,P₁] := (1/2)Σᵣ|P₀(r)-P₁(r)|. Theorem 3.10: max_R'|P₀[R']-P₁[R']| = Δ[P₀,P₁]. Theorem 3.11: Distadv[A,P₀,P₁] ≤ Δ[P₀,P₁] para todo A. Statistical indist. implica computational indist.
- **Bit Commitment**: Protocolo com hiding (commitment c nao revela bit b) e binding (impossivel abrir c como 0 e 1). Construcao de Naor: com(s,r,0)=G(s), com(s,r,1)=G(s)⊕r onde r←R escolhido por Alice.

## Conceitos-chave
- **Two-time pad**: Reutilizar chave s para cifrar m₁,m₂ vaza c₁⊕c₂=m₁⊕m₂ (totalmente inseguro).
- **Malleability**: Adversario modifica c para c'=c⊕τ, causando D(s,c')=m⊕τ sem conhecer m ou s.
- **Nonce**: Input adicional N em G(s,n) permitindo multiplos outputs pseudorandomicos de mesma seed (transforma PRG em PRF).
- **Linear Congruential Generator (LCG)**: Gₗcg(s) := (⌊s/w⌋, as+b mod q). Inseguro: dado r_i,r_{i+1}, atacante resolve CVP em lattice 2D para recuperar estado interno (Lemma 3.7: 98% dos a vulneraveis).
- **Subset Sum Generator**: G_{q,a}(s) := Σaᵢsᵢ mod q. Seguro assumindo modular subset problem hard.
- **LFSR (Linear Feedback Shift Register)**: Registrador de n bits com tap positions V; bit feedback b := b_{v₁}⊕...⊕b_{vd}. Sozinho e inseguro; combinacoes nao-lineares (ex.: CSS, A5/1) tambem vulneraveis.
- **CSS Stream Cipher**: Combina LFSR 17-bit e 25-bit via adicao mod 256. Quebrado em 2¹⁶ tentativas (vs. 2⁴⁰ exhaustive search) explorando relacao linear entre outputs.
- **RC4**: Mantem array S[256] + indices i,j; output S[S[i]+S[j]]. Vulneravel: segundo byte tem Pr[z₂=0]=2/256 (Lemma 3.8 Mantin-Shamir); digraph (0,0) aparece com frequencia (1/n²)·(1+1/n) (Lemma 3.9 Fluhrer-McGrew).
- **RNG (Random Number Generator)**: Sistema que adiciona entropia continuamente ao estado interno (ex.: /dev/random usa keyboard/mouse timings, hardware interrupts). Intel RdRand: gerador hardware com conditioner para remover bias.
- **Salsa20/ChaCha**: PRG com seed 256-bit + nonce 64-bit; gera blocos 512-bit via pad(s,j,n) e permutacao π (QuarterRound iterado). Paralelizavel, permite random access a blocos.

## Mental models
- Use stream cipher quando precisar cifrar mensagem unica com chave curta; NUNCA reutilize chave (two-time pad vaza XOR dos plaintexts).
- Prefira PRGs provavelmente seguros (ChaCha20, construcoes de PRF) a ad-hoc designs (LCG, RC4); matematica elegante nao garante seguranca pratica.
- Hybrid argument: para provar G' seguro, construa sequencia de jogos onde cada transicao e indistinguivel por seguranca de G; adversario contra G' vira adversario contra G escolhendo indice aleatorio.
- Statistical distance limita distinguishing advantage de qualquer adversario (mesmo unbounded); se Δ[P₀,P₁] negligivel, entao comp. indist. automaticamente.

## Anti-padroes
- **Reutilizar stream cipher key**: Two-time pad vaza m₁⊕m₂; ex.: PPTP Windows NT usava mesma chave RC4 para ambas direcoes (quebrado).
- **Confiar em testes estatisticos simples**: Contar 1's ou pares de bits nao detecta predictability; LCG passa testes basicos mas e totalmente previsivel.
- **Ignorar bias inicial**: RC4 tem bias nos primeiros 256 bytes; descartar prefixo nao elimina bias em digraphs (Fluhrer-McGrew).
- **Usar LCG/RC4 para crypto**: Mesmo com parametros grandes, LCG quebra via lattice attack; RC4 tem multiplos biases exploraveis.
- **Depender de unica fonte de entropia**: RdRand pode falhar; sempre combine multiplas fontes (keyboard, mouse, hardware interrupts).
- **Expor metadata em encrypted filesystems**: Se nomes de arquivo nao cifrados, malleability attack permite trocar "From:Alice" por "From:Molly" via XOR.

## Exemplos de codigo / Tabelas

**Attack Game 3.1 (PRG Security)**:
```
Experiment b:
  if b=0: s ← S, r ← G(s)
  if b=1: r ← R
  send r to A
  A outputs b̂ ∈ {0,1}
PRGadv[A,G] := |Pr[W₀] - Pr[W₁]|
```

**ChaCha20 QuarterRound**:
```c
#define ROTL(a,b) (((a) << (b)) | ((a) >> (32 - (b))))
a += b; d ^= a; ROTL(d,16);
c += d; b ^= c; ROTL(b,12);
a += b; d ^= a; ROTL(d,8);
c += d; b ^= c; ROTL(b,7);
```

**RC4 Stream Generator**:
```
i ← 0, j ← 0
repeat:
  i ← (i+1) mod 256
  j ← (j+S[i]) mod 256
  swap(S[i], S[j])
  output S[(S[i]+S[j]) mod 256]
```

**Coin Flipping Protocol**:
```
1. Bob: b₀ ← {0,1}, (c,s) ← commit(b₀)
   Send c to Alice
2. Alice: b₁ ← {0,1}, send b₁ to Bob
3. Bob: reveal (b₀,s)
   Alice: verify c=com(s,r,b₀)
Output: b := b₀ ⊕ b₁
```

**Stream Cipher Speeds (MB/sec)**:
| Cipher     | Speed |
|------------|-------|
| RC4        | 126   |
| SEAL       | 375   |
| Salsa20    | 408   |
| Sosemanuk  | 727   |

## Worked Example

**Cryptanalysis do CSS (40-bit key)**:

Setup: CSS combina LFSR 17-bit (seed s₁∈{0,1}¹⁶) e LFSR 25-bit (seed s₂∈{0,1}²⁴) via z_i = x_i + y_i + c mod 256, onde x_i,y_i sao outputs de 8 bits dos LFSRs.

Ataque (2¹⁶ vs. 2⁴⁰ exhaustive search):
1. Observar (z₁,z₂,z₃) do PRG
2. Para cada guess s₁∈{0,1}¹⁶:
   - Computar (x₁,x₂,x₃) do LFSR 17-bit
   - Usar relacao (2¹⁶x₃+2⁸x₂+x₁) + (2¹⁶y₃+2⁸y₂+y₁) ≡ (2¹⁶z₃+2⁸z₂+z₁) (mod 2²⁴)
   - Resolver para (y₁,y₂,y₃), recuperar s₂
   - Verificar: rodar PRG com s=s₁||s₂, checar se output = (z₁,...,z₁₀₀)
3. Guess correto produz match; esperado 2¹⁵ tentativas

Por que funciona: Conhecendo 3 bytes de um LFSR, estado interno e univocamente determinado; relacao linear mod 2²⁴ vaza s₂ dado s₁ e outputs observados.

## Key takeaways
1. Stream cipher = PRG seguro aplicado a mensagem unica; Theorem 3.1 garante semantic security se PRG e seguro (reducao tight: SSadv=2·PRGadv).
2. NUNCA reutilize chave de stream cipher: two-time pad vaza m₁⊕m₂; ex.: Venona project quebrou 2900 mensagens sovieticas por reuso de one-time pads.
3. Unpredictability ⟺ PRG security (Theorems 3.4, 3.6): se adversario prediz proximo bit, distingue de random; se distingue, entao prediz (via distinguisher/predictor lemma).
4. Composicao de PRGs preserva seguranca com degradacao linear: parallel/sequential composition tem PRGadv[A,G']=n·PRGadv[B,G] (hybrid argument com n+1 jogos).
5. Testes estatisticos simples (contar 1's, pares) sao insuficientes; PRG pode passar mas ser previsivel (ex.: LCG); seguranca requer indistinguishability de qualquer teste eficiente.
6. LCG e inseguro mesmo com q grande: 2 outputs consecutivos vazam estado via closest vector problem em lattice 2D (Lemma 3.7: 98% dos parametros vulneraveis).
7. RC4 tem multiplos biases: segundo byte Pr[z₂=0]=2/256 (Mantin-Shamir), digraph (0,0) sobre-representado (Fluhrer-McGrew); distinguisher atinge adv=0.5 com 2³⁴ bytes.
8. Statistical distance Δ[P₀,P₁] limita superiormente distinguishing advantage de qualquer adversario (Theorem 3.11); se Δ negligivel, entao comp. indist. (Corollary 3.12).
9. Bit commitment de Naor: com(s,r,0)=G(s), com(s,r,1)=G(s)⊕r tem hiding (por PRG security) e binding (probabilistico: requer |R|≥|S|³); permite coin flipping sem trusted party.
10. RNGs praticos (ex.: /dev/random, RdRand) devem combinar multiplas fontes de entropia e aplicar conditioner para remover bias; nunca dependa de fonte unica.

## Conecta com
