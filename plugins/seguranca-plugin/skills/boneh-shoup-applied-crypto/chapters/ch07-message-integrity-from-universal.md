# Capitulo 7: Message integrity from universal hashing

## Ideia central
MACs seguros podem ser construídos via paradigma hash-then-PRF: hash a mensagem para um digest curto, depois aplique um PRF. Universal Hash Functions (UHFs) garantem que colisões são difíceis de encontrar sem conhecer a chave, permitindo provas de segurança diretas para ECBC, NMAC e PMAC0.

## Frameworks introduzidos
- **Hash-then-PRF paradigm**: `tag = PRF(k2, H(k1, m))` onde H é UHF e PRF é seguro. Usar quando precisar estender domínio de entrada de um PRF mantendo segurança provável.
- **PRF(UHF) composition**: Composição formal de PRF com UHF. `PRFadv[A, F'] ≤ PRFadv[BF, F] + (Q²/2)·UHFadv[BH, H]`. Aplicar para provar segurança de construções como ECBC/NMAC.
- **Carter-Wegman MAC**: `S(k1,k2,m) := r←R; v←H(k1,m)+F(k2,r) mod N; output (r,v)`. Usar quando precisar segurança com ε maior (hash mais rápido) aceitando tags mais longas. Bound: `MACadv ≤ PRFadv + DUFadv + Q²/(2|R|) + 1/|T|`.
- **Nonce-based MACs**: Variante determinística onde nonce N substitui randomizer. `S(k,m,N) := H(k1,m)+F(k2,N)`. Usar quando puder garantir nonces únicos (contador ou espaço grande). Elimina termo Q² se nonces nunca repetem.
- **Encrypted UHF MAC**: `S(k1,k2,m) := E(k2, H(k1,m))` com cifra CPA-secure. Previne adversário detectar colisões no hash observando tags iguais.

## Conceitos-chave
- **Keyed hash function H**: Função determinística `H(k,m)→t` mapeando mensagens longas para digests curtos, parametrizada por chave k.
- **Universal Hash Function (ε-UHF)**: Hash onde `Pr[H(k,m0)=H(k,m1)] ≤ ε` para m0≠m1, probabilidade sobre k aleatório. Statistical UHF: ε negligível contra adversários ilimitados. Computational UHF: vantagem negligível para adversários eficientes.
- **Multi-query UHF**: Adversário vence se encontrar colisão em lista de s mensagens distintas. `MUHFadv[A,H] ≤ (Q²/2)·UHFadv[B,H]`.
- **Difference Unpredictable Function (ε-DUF)**: Hash onde `Pr[H(k,m1)-H(k,m0)=δ] ≤ ε` para m0≠m1 e δ arbitrário. Propriedade mais forte que UHF (todo DUF é UHF).
- **Pairwise Unpredictable Function (ε-PUF)**: Dado `H(k,m0)`, difícil prever `H(k,m1)` para m1≠m0. `PUFadv[A,H] ≤ ε`. Todo PUF é DUF.
- **ε-Almost Pairwise Independent Function (ε-APIF)**: PRF incondicional contra adversários com ≤2 queries. `PRFadv[A,F] ≤ ε` mesmo para A ilimitado.
- **Extendable PRF**: `F(k,x)=F(k,y) ⇒ F(k,x‖a)=F(k,y‖a)`. CBC e cascade satisfazem esta propriedade.
- **Hpoly**: `Hpoly(k,(a1,...,av)) := k^v + a1·k^(v-1) + ... + av mod p`. É (ℓ/p)-UHF. Avaliável via método de Horner.
- **Hxpoly**: `k·Hpoly(k,m) = k^(v+1) + a1·k^v + ... + av·k mod p`. É ((ℓ+1)/p)-DUF (adiciona termo k^(v+1) para DUF).
- **XOR-hash (F⊕)**: `F⊕(k,m) := ⊕[i=1..v] F(k,(ai,i))`. Paralelizável. É computational UHF se F é PRF seguro.

## Mental models
- Use UHF quando precisar garantir que adversário não encontre colisões sem conhecer chave (segurança information-theoretic possível).
- Use DUF em Carter-Wegman: previne forgery mesmo se adversário adivinhar diferença entre hashes (ataque com nonce reutilizado).
- Use PUF para one-time MACs incondicionalmente seguros: `S(k,m):=H(k,m)` onde H é PUF garante `MAC1adv ≤ ε`.
- Prefira nonce-based sobre randomized quando puder manter estado (contador): elimina Q²-term e reduz tamanho de tag.

## Anti-padroes
- **Usar Hpoly sem termo líder k^v**: Mensagens `(a1,a2)` e `(0,a1,a2)` colidem sob todas as chaves. Sempre inclua termo líder para variable-length inputs.
- **Hpoly com aritmética mod 2^n**: Completamente insecure. Mensagens de 2 blocos sempre colidem. Use GF(2^n) ou primo p.
- **Expor valores de UHF ao adversário**: Valor `Hpoly(k,m)` revela chave k diretamente. Sempre oculte via PRF ou encriptação.
- **Reutilizar nonce em Carter-Wegman**: Com Hxpoly, duas tags `(N,v1)`, `(N,v2)` para m1≠m2 permitem recuperar k1 e forjar qualquer mensagem. Fatal.
- **MAC(UHF) composition**: Substituir PRF por MAC arbitrário falha. Composição só funciona com PRFs.
- **Usar Hfpoly sem fixar comprimento**: `Hfpoly(k,(a1,a2))` colide com `Hfpoly(k,(0,a1,a2))`. Restringir a comprimento fixo ou usar Hpoly.

## Exemplos de codigo / Tabelas

**Horner's method para Hpoly:**
```
Input: m=(a1,...,av)∈Zp^v, k∈Zp
Output: t := Hpoly(k,m)
1. t ← 1
2. For i=1 to v:
3.   t ← t·k + ai mod p
4. Output t
```

**4-way parallel Horner (precompute k², k³, k⁴):**
```
For i=1 to v step 4:
  t ← t·k⁴ + ai·k³ + ai+1·k² + ai+2·k + ai+3 mod p
```

**Carter-Wegman signing:**
```
S((k1,k2), m):
  r ← R
  v ← H(k1,m) + F(k2,r) mod N
  output (r,v)
```

**Nonce-based Carter-Wegman:**
```
S((k1,k2), m, N) := H(k1,m) + F(k2,N) mod N
V((k1,k2), m, t, N) := accept iff t = H(k1,m)+F(k2,N)
```

## Worked Example
**Provando ECBC é MAC seguro via PRF(UHF) composition:**

1. **ECBC como composição**: `ECBC(k1,k2,m) = F(k2, CBC(k1,m))` onde CBC é hash e F(k2,·) é PRF final.

2. **CBC é prefix-free PRF**: Teorema 6.3 prova `PRFpfadv[B,FCBC] ≤ PRFadv[B1,F] + Q²(ℓ+1)²/(2|Y|)`.

3. **CBC é extendable**: Se `CBC(k,x)=CBC(k,y)` então `CBC(k,x‖a)=CBC(k,y‖a)` por construção iterativa.

4. **Extendable prefix-free PRF ⇒ UHF**: Teorema 7.3 mostra `UHFadv[A,FCBC] ≤ PRFpfadv[B,FCBC] + 1/|Y|`.

5. **PRF(UHF) composition**: Teorema 7.7 combina: `PRFadv[A,ECBC] ≤ PRFadv[BF,F] + MUHFadv[BH,CBC]`.

6. **Bound final**: Substituindo (7.10) em (7.20): `MACadv[A,ECBC] ≤ PRFadv[B1,F] + Q²(ℓ+1)²/(2|Y|) + 1/|Y|`.

**Intuição**: CBC comprime mensagem longa sem colisões (UHF), PRF final esconde estrutura interna. Adversário só vence se quebrar PRF ou achar colisão CBC (probabilidade ≤ Q²(ℓ+1)²/(2|Y|)).

## Key takeaways
1. Hash-then-PRF permite construir MACs para mensagens longas a partir de PRFs de domínio pequeno com provas modulares de segurança.
2. UHF é condição necessária e suficiente para PRF(UHF) composition: colisões sem conhecer chave quebram MAC, mas UHF garante `PRFadv ≤ PRFadv[F] + Q²·ε/2`.
3. CBC e cascade são computational UHFs porque são extendable prefix-free PRFs (Teorema 7.3), permitindo provas diretas de ECBC/NMAC.
4. Carter-Wegman troca segurança por velocidade: permite ε maior (hash mais rápido) usando randomização, mas tags crescem e Q²-term retorna se randomizers colidem.
5. DUF (não apenas UHF) é necessário para Carter-Wegman: adversário que prevê `H(k,m1)-H(k,m0)=δ` forja `(r, v+δ)` para m1 dado tag `(r,v)` de m0.
6. Nonce-based MACs eliminam Q²-term se nonces nunca repetem (contador), mas reutilização de nonce em Carter-Wegman com Hxpoly é catastrófica (recupera k1).
7. Hpoly requer termo líder k^v para variable-length security; Hxpoly=k·Hpoly adiciona multiplicação extra para DUF property.
8. PUFs permitem one-time MACs incondicionalmente seguros: `MAC1adv ≤ ε` mesmo contra adversários ilimitados (análogo ao one-time pad).

## Conecta com
- **Cap 6 (MACs from PRFs)**: ECBC/NMAC/PMAC0 são instâncias de hash-then-PRF; provas aqui completam teoremas 6.6, 6.7, 6.11.
- **Cap 4 (PRFs)**: PRF switching lemma usado em provas; XOR-hash usa PRF como building block.
- **Cap 5 (CPA security)**: Carter-Wegman = encrypted UHF; nonce-based MACs análogos a nonce-based encryption.
- **Cap 2 (One-time pad)**: PUF-based one-time MAC é análogo: segurança incondicional para uso único.
- **Finite fields GF(2^n)**: Hpoly/Hxpoly adaptáveis para aritmética em GF(2^n) (blocos n-bit nativos).
- **Tweakable block ciphers (Ex 4.11)**: XOR-DUF substitui PRF em construções tweakable (XTS mode).
