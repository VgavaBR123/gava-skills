# Capitulo 20: Proving properties in zero-knowledge

## Ideia central
Sigma protocols podem provar que fatos são verdadeiros (sem revelar testemunhas) via soundness, e o Fiat-Shamir transform os converte em provas não-interativas mantendo soundness e zero-knowledge no random oracle model.

## Frameworks introduzidos
- **Language of True Statements (LR)**: Conjunto de statements y para os quais existe witness x tal que (x,y) ∈ R. Usado para definir soundness (adversário não pode provar y ∉ LR).
- **Fiat-Shamir Transform**: Converte Sigma protocol em non-interactive proof: challenge c := H(y,t). Preserva soundness e zero-knowledge (random oracle model).
- **Language Reduction**: Par de mapas (f,g) onde (i) (f(x,y), g(y)) ∈ R' para todo (x,y) ∈ R, (ii) g(y) ∈ LR' ⟺ y ∈ LR. Permite reusar protocolos existentes.
- **Special Computational HVZK (cHVZK)**: Relaxa special HVZK para indistinguibilidade computacional entre conversas reais e simuladas. Necessário quando auxiliary data vaza informação (ex: range proofs).
- **Non-Interactive Zero Knowledge (niZK)**: Adversário não distingue "real world" (proofs reais) de "simulated world" (Sim gera proofs e responde random oracle queries).
- **Simulation Soundness**: Após ver simulated proofs de statements verdadeiros/falsos, adversário não consegue gerar valid proof de false statement. Combina soundness + ZK.

## Conceitos-chave
- **Soundness**: Infeasible para adversário fazer verifier aceitar y ∉ LR (Sndadv[A,Π] negligible).
- **Statistical Soundness**: Soundness vale mesmo para adversários ilimitados (ex: special soundness implica statistical soundness).
- **Computational Soundness**: Soundness vale apenas para adversários eficientes (padrão).
- **Unpredictable Commitments**: Pr[t' = t] ≤ ε quando t ← P(x,y) e t' ← Sim(y,c) independentes.
- **Backward Computable Commitments**: Função f: Y×C×Z → T computa commitment t de (y,c,z) em accepting conversation.
- **Unique Responses**: Para statement y e commitment t, existe no máximo um response z tal que (t,c,z) é accepting conversation.
- **Proof Space (PS)**: Conjunto de possíveis proofs π em non-interactive proof system.
- **Multi-Attempt Soundness**: Adversário faz r tentativas de provar false statements; rniSndadv[A,Π,r] ≤ (r+Qro)/N (Fiat-Shamir).
- **Optimized Fiat-Shamir**: Proof é (c,z) em vez de (t,z); verifier recomputa t ← f(y,c,z) e checa c = H(y,t).

## Mental models
- Use **soundness** quando precisa garantir verdade do statement (não extração de witness): ex: provar ciphertext encrypta bit válido.
- Use **Fiat-Shamir** para eliminar interação: challenge c := H(y,t) substitui verifier aleatório; soundness + HVZK preservados (random oracle).
- Use **language reduction** para reusar protocolos: reduza R a R' via (f,g); soundness/HVZK herdados se g(y) ∈ LR' ⟺ y ∈ LR.
- Use **cHVZK** quando auxiliary data vaza informação: ex: range proofs encryptam bits bi; DDH garante computational indistinguishability.
- Use **simulation soundness** para CCA security: adversário vê simulated proofs mas não forja new valid proof de false statement.

## Anti-padroes
- **Omitir statement y no hash**: c := H(t) em vez de H(y,t) quebra soundness (adversário reusa (t,z) para outro y').
- **Não incluir auxiliary data no hash**: Em voting, omitir voter ID permite replay attacks.
- **Assumir HVZK quando só tem cHVZK**: Witness independence (Theorem 19.21) falha sob cHVZK; não use para provar independência de testemunhas.
- **Confundir soundness com special soundness**: Soundness não garante extração de witness; use special soundness quando precisar extrair.
- **Ignorar multi-attempt attacks**: Single-attempt bound (Qro+1)/N inadequado; use (Qro+r)/N para r tentativas.

## Exemplos de codigo / Tabelas

**Fiat-Shamir para Chaum-Pedersen:**
```
GenPrf(α, (u,v,w)):
  t ← Zq, vt ← g^t, wt ← u^t
  c ← H((u,v,w), (vt,wt))
  z ← t + cα
  output ((vt,wt), z)

VrfyPrf((u,v,w), ((vt,wt),z)):
  c ← H((u,v,w), (vt,wt))
  if g^z = vt·v^c and u^z = wt·w^c
    then accept else reject
```

**Optimized Fiat-Shamir:**
```
GenPrf: output (c,z)  // omit (vt,wt)
VrfyPrf((u,v,w), (c,z)):
  vt ← g^z/v^c, wt ← u^z/w^c
  if c = H((u,v,w), (vt,wt))
    then accept else reject
```

**niZK Simulator (Fig 20.2):**
```
Map: Y×T → C  // associative array

sim-proof-query(y):
  c ← C, (t,z) ← Sim₁(y,c)
  if (y,t) ∉ Domain(Map)
    then Map[y,t] ← c; return (t,z)
    else return fail

sim-oracle-query((ŷ,t̂)):
  if (ŷ,t̂) ∉ Domain(Map)
    then Map[ŷ,t̂] ← C
  return Map[ŷ,t̂]
```

## Worked Example

**Range Proof (Section 20.4.1):** Alice encrypta x ∈ [0,2^d) sob pk=u=g^α. Ciphertext (v,e) = (g^ρ, u^ρ·g^x). Prova que x é d-bit:

1. **Bit decomposition:** x = Σ 2^i·bi, bi ∈ {0,1}
2. **Encrypt bits:** Gera pk auxiliar (u₀,...,u_{d-1}), v₀ ← g^ρ₀, ei ← u_i^ρ₀·g^{bi}
3. **Generic linear protocol** para:
   - v = g^ρ, e = u^ρ·g^x
   - v₀ = g^ρ₀
   - ei = u_i^ρ₀·g^{bi}, v₀^{bi} = g^τᵢ, ei^{bi} = u_i^τᵢ·g^{bi}  (força bi² = bi)
   - x = b₀ + 2b₁ + ... + 2^{d-1}b_{d-1}

**Soundness:** Sistema de equações tem solução única se x ∈ [0,2^d).

**cHVZK:** Encryptions (v₀,e₀,...,e_{d-1}) computacionalmente indistinguíveis de random (DDH).

**Complexity:** O(d) group elements (vs O(2^d) com OR-proof).

## Key takeaways
1. Special soundness implica soundness: Sndadv[A,Π] ≤ 1/N (challenge space size N).
2. Fiat-Shamir preserva soundness: niSnd^ro_adv[A,FS-Π] ≤ (Qro+1)·Sndadv[B,Π] (random oracle).
3. Fiat-Shamir preserva zero-knowledge: niZKadv[A,FS-Π,Sim] ≤ Qp(Qp+Qro)·ε (ε-unpredictable commitments).
4. Optimized Fiat-Shamir: Proof (c,z) em vez de (t,z) quando commitments são backward computable; mesma security.
5. Language reduction reutiliza protocolos: Reduza R a R' via (f,g); soundness/HVZK herdados se g preserva membership.
6. cHVZK necessário quando auxiliary data vaza: Range proofs, non-linear relations sem constraints; DDH garante computational indistinguishability.
7. Multi-attempt soundness: r tentativas ⇒ rniSnd^ro_adv ≤ (Qro+r)/N (Fiat-Shamir); mais eficiente que r aplicações de single-attempt bound.
8. Simulation soundness combina soundness + ZK: Após ver simulated proofs, adversário não forja valid proof de false statement; útil para CCA security.
9. Unique responses + unpredictable commitments ⇒ simulation soundness: simSndadv ≤ (Qro+Qa)·Sndadv (Fiat-Shamir).
10. Non-linear relations via auxiliary encryptions: Equação xi=xj·xk requer encryptions de xj ou xk (Section 20.2.1) ou usa cHVZK (Section 20.4.3).

## Conecta com
- **Cap 19 (Sigma protocols):** Special soundness, special HVZK, generic linear protocol, OR-proofs, Chaum-Pedersen.
- **Cap 11 (Public-key encryption):** Multiplicative ElGamal, DDH assumption, semantic security.
- **Cap 13 (Digital signatures):** Fiat-Shamir signatures (Schnorr), VRFs, multi-key security.
- **Cap 12 (CCA security):** Simulation soundness para CCA (Ex 20.24), parallel 1CCA (Ex 20.28).
- **Cap 22 (Threshold cryptography):** Threshold decryption em voting protocols.
