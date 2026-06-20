# Capitulo 4: Block ciphers

## Ideia central
Block ciphers são permutações determinísticas sobre blocos de tamanho fixo, parametrizadas por chave; segurança exige que E(k,·) seja computacionalmente indistinguível de permutação aleatória (não apenas de função aleatória).

## Frameworks introduzidos
- **Iterated cipher paradigm**: E(k,x) = E^(kd, E^(kd-1,...E^(k1,x)...)) onde E^ é round cipher e G expande k → (k1,...,kd). Segurança emerge da iteração de função simples não-linear.
- **Feistel permutation**: ψ(x,y) := (y, x⊕f(y)) constrói permutação invertível de função arbitrária f. Usado em DES; decriptação = mesma estrutura com chaves reversas.
- **3E construction (Triple-DES)**: E3((k1,k2,k3),x) := E(k3,E(k2,E(k1,x))). Resiste exhaustive search com |K|³ chaves mas meet-in-the-middle reduz ataque a ~|K|².
- **Electronic Codebook (ECB) mode**: E'(k,m) := (E(k,m[0]),...,E(k,m[v-1])). Inseguro: blocos idênticos → ciphertexts idênticos (padrões visíveis). Seguro apenas para mensagens com blocos distintos.
- **AES alternating key cipher**: x → AES⊕k₁ → AES⊕k₂ →...→ ^AES⊕k₁₀. Cada AES = SubBytes∘ShiftRows∘MixColumns (exceto última rodada omite MixColumns).
- **PRF Switching Lemma**: |BCadv[A,E] - PRFadv[A,E]| ≤ Q²/2N. Block cipher seguro ≈ PRF seguro quando |X| super-poly; birthday attack é limite fundamental.

## Conceitos-chave
- **Block cipher**: Cipher determinístico E:(K,X)→X onde E(k,·) é permutação para todo k (X = message space = ciphertext space).
- **Data block**: Elemento x∈X; para AES, X={0,1}¹²⁸.
- **Round cipher E^**: Função simples iterada d vezes; segurança não provada individualmente mas emerge após múltiplas rodadas.
- **Key expansion G**: PRG que expande k → (k1,...,kd) round keys; para AES-128 deve ser invertível (entropia preservada mas facilita related-key attacks).
- **S-box**: Lookup table não-linear (ex: DES usa oito 6→4-bit S-boxes); única fonte de não-linearidade; design criterioso essencial (resistir differential/linear cryptanalysis).
- **Exhaustive search attack**: Testar todos k∈K até achar k satisfazendo E(k,xi)=yi; tempo O(|K|), espaço O(1). DES quebrado em 22h (1999); AES-128 requer ~10²⁰ anos.
- **Meet-in-the-middle**: Ataque em 2E: construir tabela {(k₁,E(k₁,x̄))} então buscar D(k₂,ȳ) na tabela; tempo 2Q·|K|, espaço |K|. Reduz Double-DES a single-DES.
- **Linear cryptanalysis**: Explorar bias ε em m[S₀]⊕E(k,m)[S₁]=k[S₂]; recuperar bits de chave com ~4/ε² samples via majority vote (Lemma 4.3). DES: ε≈2⁻²¹ → ataque 2⁴¹.
- **Side-channel attack**: Extrair chave via timing (cache misses em table lookups AES), power (DPA separa traces por LSB de S-box output), EM, heat, sound.
- **Pseudo-random function (PRF)**: F:(K,X,Y) onde F(k,·) indistinguível de f∈Funs[X,Y]. Mais geral que block cipher (Y≠X permitido, não precisa ser permutação).

## Mental models
- Use block cipher como PRF quando |X| super-poly (birthday bound Q²/2N negligível); para AES-128, seguro até ~2⁶⁴ queries.
- Itere round cipher simples (não-linear via S-boxes) até convergir; DES=16 rounds, AES-128=10 rounds suficientes empiricamente.
- Exhaustive search viável quando log₂|K| < 80; mínimo seguro hoje = 128 bits (quantum exhaustive search requer |K|^(1/2) via Grover).
- ECB mode revela padrões; nunca use para mensagens multi-bloco com possível repetição.

## Anti-padroes
- **Iterar cipher linear**: E^(k,x):=k·x mod q nunca converge para segurança (composição permanece linear).
- **2E construction**: Double encryption não dobra segurança; meet-in-the-middle reduz a single cipher (tempo 2|K|, espaço |K|).
- **S-boxes aleatórias em DES**: Escolha aleatória (sem critérios de design) torna DES quebrável com milhões de queries.
- **Table-based AES sem mitigação**: Cache timing leak via S[a₀]=S[a₁] → c₀-c₁=w₀-w₁; recupera round key com ~2²⁰ samples.
- **Key-dependent branches**: Simple power analysis (SPA) detecta spikes; evitar condicionais dependentes de chave.
- **Padding AES com instruções aleatórias**: Noise aditivo não previne timing attacks (adversário obtém mais samples e calcula média).
- **Omitir output check em fault injection**: Sempre verificar E(k,D(k,c))=c antes de liberar output (custo: 2× slowdown).

## Exemplos de codigo / Tabelas

```python
# AES round function (conceptual)
def AES_round(state, round_key):
    state = SubBytes(state)      # S-box: {0,1}⁸→{0,1}⁸ em cada célula
    state = ShiftRows(state)     # Rotação cíclica das linhas
    state = MixColumns(state)    # Multiplicação matricial em GF(2⁸)
    state = state ⊕ round_key
    return state

# Table-based optimization (4 lookups por coluna)
A'[0] = T0[a0] ⊕ T1[a5] ⊕ T2[a10] ⊕ T3[a15]
# onde Ti[a] := M[i]·S[a] (pré-computado, 4KB total)
```

**DES linear relation (14 rounds, bias ε≈2⁻²¹):**
```
mR[17,18,24] ⊕ cL[7,18,24,29] ⊕ cR[15] = k[Se]
```

**Meet-in-the-middle em 2E:**
```
Step 1: Construir tabela T = {(k₁, E(k₁,x̄)) : k₁∈K}  // tempo Q|K|
Step 2: Para cada k₂∈K:
          z̄ ← D(k₂,ȳ)
          Se (·,z̄)∈T: output (k₁,k₂)              // tempo Q|K|
```

**Parâmetros de ciphers:**
| Cipher    | Key (bits) | Block | Rounds | Perf (MB/s) |
|-----------|------------|-------|--------|-------------|
| DES       | 56         | 64    | 16     | 80          |
| 3DES      | 168        | 64    | 48     | 30          |
| AES-128   | 128        | 128   | 10     | 163         |
| AES-256   | 256        | 128   | 14     | 115         |

## Worked Example

**Linear cryptanalysis de DES (recuperar 13 bits de chave):**

1. **Setup**: Adversário obtém t=2⁴³ pares (m,c) onde c=DES(k,m). Relação conhecida (bias ε≈2⁻²¹):
   ```
   mL⊕F(k₁,mR)[17,18,24] ⊕ cR[7,18,24,29] ⊕ cL⊕F(k₁₆,cR)[15] = k[Se]
   ```
   LHS depende de apenas 12 bits: 6 de k₁ (para F(k₁,mR)[17,18,24]) + 6 de k₁₆ (para F(k₁₆,cR)[15]). Denote k⁽¹²⁾.

2. **Redução de tipo**: Cada (m,c) tem "tipo" = 13 bits relevantes (6 de m, 6 de c, 1 bit XOR). Construir tabela de contagem: entry[b] = #{pares de tipo b} (tempo t, espaço 2¹³).

3. **Busca por bias**: Para cada candidato k⁽¹²⁾∈{0,1}¹²:
   - Avaliar LHS da relação usando tabela de tipos (tempo 2¹² × 2¹³ = 2²⁵ << t).
   - Calcular bias ε' = |(#zeros/t) - 1/2|.

4. **Seleção**: Ordenar 2¹² candidatos por bias decrescente. Com t=2⁴³ >> 4/ε² ≈ 2⁴², Lemma 4.3 garante que k⁽¹²⁾ correto tem maior bias com prob >86%. Recuperar k[Se] via majority vote → 13 bits totais.

5. **Extensão**: Repetir com segunda relação (decryption) → mais 13 bits. Exhaustive search nos 56-26=30 bits restantes (tempo 2³⁰). **Total: ~2⁴¹ DES evals** vs 2⁵⁶ brute-force.

## Key takeaways
1. **Nunca implemente block ciphers próprios**: Use AES; design requer anos de análise (DES S-boxes resistem differential cryptanalysis conhecida apenas em 1990s).
2. **Exhaustive search bound**: Mínimo 128-bit keys (clássico) ou 256-bit (quantum Grover); AES-128 seguro até ~2⁶⁴ queries (birthday).
3. **ECB mode inseguro para multi-block**: Padrões vazam (Fig 4.5); use modos autenticados (Cap 5).
4. **Side-channels quebram implementações corretas**: Timing (cache), power (DPA), faults; use AES-NI hardware ou constant-time code + blinding.
5. **PRF ≈ block cipher quando |X| super-poly**: Switching Lemma (Thm 4.4) permite usar AES como PRF em provas; diferença ≤Q²/2N.
6. **3DES resiste meet-in-the-middle**: Ataque requer 2¹¹² tempo (impraticável) vs 2E quebrável em 2⁵⁶ tempo + 2⁵⁶ espaço.
7. **Linear/differential cryptanalysis = design constraint**: S-boxes devem satisfazer critérios (ex: output bit ≠ linear combo de inputs, mudança 1 bit → ≥2 bits output).
8. **Mitigações práticas**: AES-NI (1.35 cycles/byte pipelined), constant-time bit-sliced implementations, preload tables em L1 (mas cuidado com interrupts/hyperthreading).

## Conecta com
- **Cap 3 (Stream ciphers)**: Block cipher → stream cipher via counter mode; PRG de PRF (Ex 4.13).
- **Cap 5 (Modos autenticados)**: CBC, CTR, GCM constroem CPA-secure/authenticated encryption de block cipher.
- **Cap 2 (Semantic security)**: Thm 4.1 prova ECB seguro para mensagens com blocos distintos (redução a BC security).
- **Ideal cipher model (Sec 4.6)**: Modelar E(k,·) como permutação aleatória independente por k; analisar 3E, Even-Mansour.
- **Cap 9 (MACs)**: PRF → MAC via F(k,m); CBC-MAC, HMAC.
- **Cap 16 (RSA fault attacks)**: Fault injection em CRT-RSA recupera fatores; princípio similar a AES fault attacks.
- **Quantum algorithms**: Grover (Sec 4.3.4) → exhaustive search O(√|K|); Shor quebra RSA/DH (Cap 19).
