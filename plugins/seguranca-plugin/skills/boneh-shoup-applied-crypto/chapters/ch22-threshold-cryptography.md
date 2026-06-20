# Capitulo 22: Threshold cryptography

## Ideia central
Threshold cryptography protege chaves secretas dividindo-as em N shares, exigindo t shares para operações criptográficas, garantindo que t-1 shares comprometidos não revelem nada sobre a chave.

## Frameworks introduzidos
- **t-out-of-N threshold scheme**: Sistema onde t de N servidores devem participar para descriptografar/assinar; t-1 servidores comprometidos não revelam a chave (balanceia segurança vs disponibilidade)
- **Shamir secret sharing**: Divide segredo σ ∈ Zq em N shares usando polinômio φ(x) de grau t-1, onde φ(0)=σ e φ(i)=σᵢ; qualquer t shares reconstroem σ via interpolação de Lagrange
- **Distributed Key Generation (DKG)**: Protocolo onde N servidores geram pk e shares sem reconstitutir sk em local único; resiste a t-1 servidores comprometidos durante geração
- **Accountable Threshold Signatures (ATS)**: Assinatura threshold onde σ identifica conjunto J de signatários; previne framing de partes inocentes
- **Private Threshold Signatures (PTS)**: Assinatura threshold indistinguível de assinatura regular; oculta N, t e conjunto J do público

## Conceitos-chave
- **Decryption/signing server**: Máquina que armazena um share da chave e participa do protocolo threshold
- **Combiner**: Entidade que orquestra protocolo threshold, coletando t shares e reconstruindo resultado final
- **Hardware Security Module (HSM)**: Dispositivo que responde requisições sem exportar chave em claro
- **Lagrange interpolation coefficients**: Valores λⱼ que permitem computar φ(j*) = Σⱼ∈J λⱼφ(j) para polinômio de grau ≤t-1
- **Interpolation in the exponent**: Técnica para computar h^φ(j*) dado {h^φ(j)}ⱼ∈J sem conhecer φ ou h
- **Decentralized key provisioning**: Cada servidor gera próprio par (pkᵢ,skᵢ); elimina gerador confiável
- **Robustness**: Propriedade combinando accurate blaming (detecta shares inválidos) e consistency (shares válidos produzem mesmo resultado)
- **Associated data**: Dados públicos d fornecidos na encriptação; descriptografia requer mesmo d (implementa políticas de acesso)
- **AD-only CCA security**: Adversário não aprende sobre m encriptado com d se não obtém decryption shares para (c^,d^) onde d^=d
- **Static corruption model**: Adversário declara conjunto L de servidores comprometidos no início do ataque

## Mental models
- Use threshold t próximo de N/2 quando disponibilidade é crítica; t próximo de N quando segurança é prioritária
- Use ATS quando accountability é necessária (ex: transações financeiras); use PTS quando estrutura organizacional deve ser privada
- Aplique DKG quando gerador confiável é single point of failure inaceitável
- Combine threshold decryption com associated data para implementar políticas de acesso distribuídas (ex: key escrow)

## Anti-padroes
- **Reconstituting secret key at combiner**: Cria single point of failure; use interpolation in the exponent
- **Ignoring associated data in decryption shares**: Permite adversário trocar d e burlar políticas; sempre valide d em cada servidor
- **Trusted key generator without DKG**: Expõe sk durante geração; use DKG ou destrua fisicamente máquina geradora
- **Generic threshold scheme para produção**: Assinaturas/ciphertexts crescem linearmente com t; use BLS threshold ou GS threshold
- **Threshold sem robustness**: Servidor malicioso pode fornecer share inválido sem detecção; implemente accurate blaming e consistency

## Exemplos de codigo / Tabelas

**Shamir secret sharing:**
```
Gsh(N,t,σ):
  α₁,...,αₜ₋₁ ← Zq
  φ(x) := αₜ₋₁x^(t-1) + ... + α₁x + σ
  for i=1..N: σᵢ ← φ(i)
  return (σ₁,...,σₙ)

Csh(J,{σⱼ}ⱼ∈J):
  compute Lagrange coefficients λⱼ for j∈J
  return σ := Σⱼ∈J λⱼσⱼ
```

**BLS threshold signature combiner:**
```
C(pkc,m,J,{σⱼ}ⱼ∈J):
  // Step 1: validate shares
  for j∈J: if VBLS(uⱼ,m,σⱼ)=reject then blame(j)
  // Step 2: interpolate
  compute λⱼ for j∈J (Lagrange coefficients)
  σ := ∏ⱼ∈J σⱼ^λⱼ  // = H(m)^α
  return σ
```

**GS threshold decryption share:**
```
D(skᵢ,c,d):
  (v,e,w̄) := c
  u' := HG(v,d)
  if ODDH(u',v,w̄)=reject: return reject
  wᵢ := v^αᵢ
  return wᵢ
```

## Worked Example

**3-out-of-5 BLS threshold signature:**

Setup: Gerador escolhe α ∈ Zq, computa pk=g^α, gera Shamir shares α₁,...,α₅ via φ(x) grau 2 com φ(0)=α. Servidor i recebe skᵢ=αᵢ e pkᵢ=g^αᵢ.

Assinatura: Combiner solicita assinatura em m. Servidores 1,2,4 respondem:
- σ₁ = H(m)^α₁
- σ₂ = H(m)^α₂  
- σ₄ = H(m)^α₄

Combiner valida cada share: VBLS(pkᵢ,m,σᵢ)=accept. Computa Lagrange coefficients λ₁,λ₂,λ₄ para J={1,2,4} e j*=0. Reconstrói:

σ = σ₁^λ₁ · σ₂^λ₂ · σ₄^λ₄ = H(m)^(λ₁α₁+λ₂α₂+λ₄α₄) = H(m)^φ(0) = H(m)^α

Verificação: VBLS(pk,m,σ) valida σ como assinatura BLS regular.

## Key takeaways
1. Threshold cryptography elimina single point of failure sem reconstitutir chave; essencial para sistemas críticos
2. Shamir secret sharing + interpolation in the exponent = base para threshold schemes eficientes (BLS, GS)
3. Robustness (accurate blaming + consistency) é essencial para detectar servidores maliciosos e garantir determinismo
4. Associated data implementa políticas de acesso distribuídas em threshold decryption; cada servidor valida d independentemente
5. DKG elimina trusted key generator; assume N>3L para protocolos práticos em modelo assíncrono
6. ATS vs PTS: escolha depende se accountability ou privacy da estrutura organizacional é prioritária
7. AD-only CCA security é suficiente para maioria das aplicações threshold; upgrade para full CCA via strongly one-time signature

## Conecta com
- Cap 11.5 (ElGamal): base para threshold decryption schemes
- Cap 13 (Signatures): threshold signatures estendem segurança de signature schemes
- Cap 15.5 (BLS signatures): suporta threshold eficiente via pairings
- Cap 19.5.2 (Chaum-Pedersen): prova DH-triple para pairing-free threshold
- Cap 20.3 (NIZK): substitui pairings em threshold decryption via Fiat-Shamir
- Secret sharing (Shamir): fundação matemática para todos threshold schemes
