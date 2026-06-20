# Capitulo 12: Chosen ciphertext secure public key encryption

## Ideia central
CCA security modela ataques reais onde adversários podem obter descriptografias de ciphertexts modificados, sendo o "gold standard" para segurança em criptografia de chave pública—mais fundamental aqui do que no contexto simétrico.

## Frameworks introduzidos
- **Attack Game 12.1 (CCA security)**: Adversário submete pares (mi0,mi1) e recebe ci←E(pk,mib); pode fazer decryption queries em c^j∉{c1,c2,...}; vantagem CCAadv[A,E]:=|Pr[W0]−Pr[W1]|. (Use para definir segurança contra chosen ciphertext attacks)
- **Attack Game 12.2 (One-way TDF with image oracle)**: Dado (pk,y=F(pk,x)), adversário acessa oráculo que responde "y^ está na imagem de F(pk,·)?"; vantagem IOWadv[A,T]. (Use quando TDF não é permutação)
- **Attack Game 12.3 (Interactive CDH - ICDH)**: Dado (u=gα,v=gβ), adversário acessa DH-decision oracle para testar se (u,v~,w~) é DH-triple; deve computar w=gαβ. (Use para provar CCA-security de ElGamal)
- **Attack Game 12.4 (Universal distinguishing game)**: Adversário escolhe (u,v,w)∉Lu; recebe h e zb (z0=f(v,w) ou z1 random); pode fazer evaluation queries em Lu. (Use para provar independência em projective hash functions)
- **Attack Game 12.5 (Universal² guessing game)**: Adversário escolhe (u,v,w,τ); recebe (h1,h2,z=f(v,w,τ)); deve adivinhar f(v^i,w^i,τ^i) para (v^i,w^i)∉Lu, τ^i≠τ. (Use para provar ECS)
- **Fujisaki-Okamoto transformation**: TFO=(Ga,F,Da) onde F(pk,x):=Ea(pk,x;U(x)) com U:X→R random oracle; converte CPA-secure Ea em CCA-secure ETDF. (Use para obter CCA de qualquer one-way probabilistic PKE)

## Conceitos-chave
- **CCA security**: Adversário pode descriptografar qualquer c^≠c* antes/depois de receber c*; esquema é seguro se não distingue qual plaintext foi cifrado.
- **1CCA security**: Restrição a single encryption query; implica CCA security (Theorem 12.1: CCAadv≤Qe·1CCAadv).
- **Non-malleability**: Infeasível criar c' relacionado a c sem conhecer plaintext; CCA security implica non-malleability.
- **Projective hash function**: Alice delega f:Y→Z para Bob via h; Bob computa f em L⊆Y com h, mas f(y) para y∉L permanece unpredictable.
- **Universal projective hash**: Para y∉L, f(y) e h são independentes; f(y) uniformemente distribuído em Z.
- **Universal² projective hash**: Para y,y^∉L e τ≠τ^, valores h, f(y,τ), f(y^,τ^) mutuamente independentes.
- **ICDH assumption**: CDH difícil mesmo com DH-decision oracle para triples (gα,·,·).
- **Padding scheme PS=(P,U)**: P:M×R→X randomizado; U:X→M∪{reject} inverte P; usado em RSA-PS encryption.
- **One-way encryption**: Dado (pk,y=Ea(pk,x;r)), computar x é difícil (Attack Game 12.6).
- **ε-unpredictable encryption**: Pr[Ea(pk,Da(sk,y);r)=y]≤ε para r random.

## Mental models
- Use CCA security quando adversário pode influenciar/observar descriptografias no sistema real (ex: key escrow, homework submission).
- Use ICDH quando precisar provar CCA-security de ElGamal no random oracle model (DDH não basta).
- Use universal² projective hash quando precisar CCA sem random oracles (ECS scheme).
- Use Fujisaki-Okamoto quando tiver qualquer one-way PKE e quiser CCA-security no random oracle model.

## Anti-padroes
- **Encrypt-then-MAC não garante CCA em PKE**: Qualquer um pode gerar MAC válido com sua própria chave; atacante modifica c e re-autentica (ex: Molly rouba homework de Alice).
- **PKCS1 mode 2 vulnerável a Bleichenbacher**: Servidor revela se decryption tem formato válido (00 02 r 00 m); oráculo Px(r) permite recuperar plaintext com milhões de queries.
- **Omitir group membership check**: Em ElGamal/ECS, não verificar v,w∈G permite small-subgroup attacks.
- **Usar DDH para provar EEG CCA-secure**: Decryption queries podem testar DH-triples; precisa ICDH assumption.

## Exemplos de codigo / Tabelas

**ETDF (Theorem 12.2)**:
```
E(pk,m): x←X, y←F(pk,x), k←H(x), c←Es(k,m); output (y,c)
D'(sk,(y,c)): x←I(sk,y); if F(pk,x)=y then k←H(x),m←Ds(k,c) else reject
```
Bound: 1CCAroadv ≤ 2·IOWadv + 1CCAadv

**ECS (Theorem 12.9)**:
```
G(): α←Zq, u←gα; ρ,σ←Zq, h←gρuσ; ξ1,ζ1,ξ2,ζ2←Zq, h1←gξ1uζ1, h2←gξ2uζ2
E(pk,m): β←Zq, v←gβ, w←uβ, τ←H'(v,w); z←hβ, z'←(h1h2τ)β; k←H(v,z), c←Es(k,m)
D(sk,(v,w,z',c)): τ←H'(v,w); if vξ1+τξ2wζ1+τζ2=z' then z←vρwσ, k←H(v,z), m←Ds(k,c)
```
Bound: 1CCAadv ≤ 2·DDHadv + KDFadv + CRadv + (Qd+1)/q + 1CCAadv

**Fujisaki-Okamoto E_FO^EG**:
```
E(u,m): x←G, τ←U(x), v←gτ, w←uτ, y←w·x; k←H(x), c←Es(k,m); output (v,y,c)
D(α,(v,y,c)): w←vα, x←y/w, τ←U(x); if gτ=v then k←H(x), m←Ds(k,c) else reject
```
Bound: 1CCAroadv ≤ 2(QH+QU)·CDHadv + 2Qd/q + 1CCAadv

## Worked Example
**Homework submission attack (Section 12.2.1)**:
- Alice cifra email m="From:Alice\n[homework]" com ETDF: (y,c) onde c=G(H(x))⊕m
- Molly intercepta (y,c), flipa bits em c para obter c' tal que m'="From:Molly\n[homework]"
- Molly envia (y,c') para Bob; Bob descriptografa e vê homework de Alice com header "From:Molly"
- **CCA adversary A**: submete par (m0,m1) com mesmo body, recebe (y,c); modifica para (y,c'); submete (y,c') como decryption query; output 0/1 baseado no body observado
- **Vantagem**: 1 (distingue perfeitamente)
- **Defesa**: CCA-secure scheme previne; mas não previne Molly enviar homework malicioso "From:Alice"

## Key takeaways
1. CCA security implica 1CCA security (Theorem 12.1); prove 1CCA para obter CCA
2. ETDF com image-check é CCA-secure (RO model) se T é IOW e Es é 1CCA (Theorem 12.2)
3. ElGamal EEG é CCA-secure (RO) sob ICDH, não apenas CDH (Theorem 12.4)
4. ECS é CCA-secure sem RO sob DDH+KDF+CR usando universal² projective hash (Theorem 12.9)
5. Fujisaki-Okamoto converte qualquer one-way+unpredictable PKE em CCA-secure (RO) (Theorem 12.10)
6. E_FO^EG é CCA-secure sob CDH (não ICDH) no RO model (Theorem 12.12)
7. CCA-secure AD PKE: associa metadata d; decryption falha se d'≠d (Definition 12.7)
8. AD-only CCA: restrição d^j∉{d1,...} em vez de (c^j,d^j)∉{(c1,d1),...}; suficiente para key escrow
9. PKCS1 mode 2 vulnerável a Bleichenbacher: oráculo Px revela formato válido; TLS 1.0 defende gerando r random se decryption falha
10. Padding schemes (P,U): P:M×R→X randomizado; U inverte; RSA-PS encryption aplica F após P

## Conecta com
- Cap 9: CCA security em symmetric-key (AE=CPA+ciphertext integrity); aqui encrypt-then-MAC não basta
- Cap 11: CPA security (semantic security); CCA é extensão natural com decryption oracle
- Cap 10: RSA assumption, CDH/DDH assumptions; usados em ERSA, EEG, ECS
- Cap 13: Digital signatures, signcryption (combina CCA PKE com signatures)
- Cap 8: Collision-resistant hash (usado em ECS, key escrow)
- Cap 17: Lattice-based PKE (Regev); aplica Fujisaki-Okamoto para CCA
