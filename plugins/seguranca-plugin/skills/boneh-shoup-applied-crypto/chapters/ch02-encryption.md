# Capítulo 2: Encryption

## Ideia central
Cifras permitem que Alice transmita mensagens secretas para Bob sobre uma rede insegura usando uma chave compartilhada, mas técnicas básicas só garantem sigilo para mensagens únicas, sem integridade ou estabelecimento de chave.

## Frameworks introduzidos
- **Shannon Cipher**: Par de funções (E, D) onde E(k,m)=c e D(k,c)=m, satisfazendo D(k,E(k,m))=m (cifra determinística clássica)
- **Perfect Security**: Pr[E(k,m₀)=c] = Pr[E(k,m₁)=c] para todos m₀,m₁,c (adversário não ganha informação mesmo com poder computacional ilimitado)
- **Computational Cipher**: Algoritmos eficientes E (possivelmente probabilístico) e D (determinístico) com espaços parametrizados por λ (security parameter) e Π (system parameter)
- **Semantic Security (SS)**: |Pr[W₀] - Pr[W₁]| negligível para adversários eficientes em Attack Game 2.1 (adversário não distingue cifras de m₀ vs m₁)
- **Bit-Guessing SS**: SSadv*[A,E] = |Pr[^b=b] - 1/2|, onde SSadv[A,E] = 2·SSadv*[A,E] (formulação equivalente mais conveniente)
- **Onion Routing**: c₂ := E(kc, ⟨David, c₁⟩) onde c₁ := E(kd, ⟨Bob, m⟩) (cifra aninhada para anonimato)

## Conceitos-chave
- **One-Time Pad**: E(k,m) := k⊕m onde |k|=|m|=L; perfeitamente seguro mas chaves longas (Teorema 2.2)
- **Substitution Cipher**: Permutação π aplicada componente-a-componente; inseguro por revelar padrões (Example 2.6)
- **Negligible Function**: f(n) < 1/nᶜ para todo c>0 e n suficientemente grande (ex: 2⁻ⁿ, n⁻ˡᵒᵍⁿ)
- **Poly-Bounded**: |f(n)| ≤ nᶜ+d para constantes c,d (tempo/tamanho "razoável")
- **Efficient Algorithm**: Tempo de execução ≤ t(λ) com probabilidade ≥ 1-ε(λ), onde t poly-bounded e ε negligível
- **Message Recovery (MR)**: MRadv[A,E] := Pr[m̂=m] - 1/|M| (recuperar m de c=E(k,m))
- **Parity Prediction**: Parityadv[A,E] := |Pr[^b=parity(m)] - 1/2| (prever XOR dos bits)
- **Elementary Wrapper**: B = ⟨M',M⟩ onde M' é efficient interface e tempo de M' ≤ t(λ+I) para I interações
- **Anonymity Set**: Conjunto de n possíveis remetentes após mixing (Alice oculta entre n usuários)
- **Nested Cipher**: Eₙ((k₁,...,kₙ),m) := E(kₙ, E(kₙ₋₁,...E(k₁,m)...)) (seguro mesmo revelando n-1 chaves)

## Mental models
- Use **Perfect Security** quando adversário tem poder ilimitado mas só 1 mensagem (one-time pad para chaves descartáveis)
- Use **Semantic Security** quando adversário é eficiente e chaves curtas são necessárias (sistemas práticos)
- Use **Security Reduction** para provar: "Se A quebra X, então B quebra Y" → como Y é seguro, X também é
- Use **Onion Routing** quando anonimato requer que nenhum mix individual conheça origem+destino (≥2 mixes honestos)

## Anti-padrões
- **Chaves curtas com Perfect Security**: Shannon prova |K| ≥ |M| (Teorema 2.5) — impossível ter chaves menores que mensagens
- **Reutilizar chave do OTP**: Segurança vale apenas para 1 mensagem; múltiplas mensagens requerem técnicas do Cap. 5
- **Ignorar comprimento da mensagem**: Variable-length OTP vaza |m| (Example 2.5) — padding pode ser necessário
- **Cifrar chave sob si mesma**: E(k,k) pode quebrar SS (Exercise 2.16) — chave e mensagem devem ser independentes
- **Comprimir após cifrar**: Compressão de c não reduz tamanho (entropia máxima); comprimir antes pode vazar info (Exercise 2.17)
- **Confiar em único mix**: Carol sozinha vincula Alice→Bob; colusão de todos os mixes quebra anonimato
- **Substituição simples**: Padrões de frequência e headers conhecidos ("FROM") permitem ataques (Example 2.6)

## Exemplos de código / Tabelas

```python
# One-Time Pad
def E(k, m):  # k, m ∈ {0,1}^L
    return k ⊕ m

def D(k, c):
    return k ⊕ c

# Additive OTP (mod n)
def E(k, m):  # k, m ∈ {0,...,n-1}
    return (m + k) % n

def D(k, c):
    return (c - k) % n

# Onion Routing (2 mixes)
c1 = E(kd, (Bob, m))
c2 = E(kc, (David, c1))
# Carol decripta c2 → envia c1 para David
# David decripta c1 → envia m para Bob
```

**Teorema 2.1 (Equivalências de Perfect Security)**:
(i) Pr[E(k,m₀)=c] = Pr[E(k,m₁)=c] ∀m₀,m₁,c
(ii) |{k: E(k,m)=c}| = Nᶜ ∀m (constante por c)
(iii) E(k,m) tem mesma distribuição ∀m

## Worked Example

**Internet Roulette (Seção 2.2.4)**:
- **Setup**: Casa publica c=E(k,r) antes de jogador apostar, onde r∈{0,...,36}
- **Ataque ingênuo**: Jogador analisa c para melhorar odds de 18/37
- **Prova de segurança**:
  1. Definir "ideal roulette": casa publica c=E(k,0) (dummy) mas usa r real para resultado
  2. Construir adversário SS B: escolhe r aleatório, envia (m₀=r, m₁=0) ao challenger, recebe c, repassa c ao jogador A, obtém aposta, retorna ^b=W(r,bet)
  3. Experimento 0 (c cifra r): Pr[^b=1] = p₀ = odds do jogador no jogo real
  4. Experimento 1 (c cifra 0): Pr[^b=1] = p₁ = 18/37 (c independente de r)
  5. SSadv[B,E] = |p₁-p₀| = IRadv[A] → se E é SS, então IRadv[A] negligível

**Lição**: Substituir componente real por ideal, provar equivalência via SS.

## Key takeaways

1. **Perfect Security é impraticável**: OTP requer |K|≥|M| (Shannon); sistemas reais usam Semantic Security com chaves curtas
2. **SS implica resistência a ataques parciais**: MR, parity prediction, predicados arbitrários (Teoremas 2.7, 2.8, 2.3)
3. **Reduções de segurança**: Construir B (elementary wrapper de A) tal que Adv[A,Sistema] ≤ Adv[B,Primitiva] — se primitiva segura, sistema seguro
4. **Cifra aninhada preserva SS**: Eₙ seguro mesmo revelando n-1 chaves (Teorema 2.12) — base do onion routing
5. **Anonimato requer mixing**: Único mix vê origem+destino; ≥2 mixes (um honesto) garantem anonymity set de tamanho n
6. **Formalismo assintótico**: λ (security parameter) controla trade-off segurança/eficiência; negligível = o(1/λᶜ) ∀c
7. **Bit-guessing é equivalente**: SSadv*[A,E] = 2·SSadv[A,E] (Teorema 2.10) — formulação mais conveniente para provas

## Conecta com

- **Cap. 5**: Cifras para múltiplas mensagens (CPA security, modos de operação)
- **Cap. 6**: Integridade de mensagens (MACs, authenticated encryption)
- **Cap. 21**: Estabelecimento de chaves (key exchange, Diffie-Hellman)
- **Cap. 22**: Secret sharing e threshold cryptography (generalização de Exercise 2.20)
- **Appendix D**: Algoritmos probabilísticos (formalização de "efficient")
