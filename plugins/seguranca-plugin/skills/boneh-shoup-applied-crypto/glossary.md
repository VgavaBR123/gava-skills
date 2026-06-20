# Glossário — A Graduate Course in Applied Cryptography

**AEAD (Authenticated Encryption with Associated Data)** - Esquema que garante confidencialidade da mensagem e integridade de mensagem + dados associados transmitidos em claro (Cap 9)

**AES (Advanced Encryption Standard)** - Block cipher padrão com blocos de 128 bits, chaves de 128/192/256 bits, usando estrutura alternating key com SubBytes/ShiftRows/MixColumns (Cap 4)

**Anonymous Key Exchange** - Protocolo onde duas partes estabelecem chave compartilhada com transcrito indistinguível de aleatório para eavesdropper (Cap 10)

**Associated Data** - Dados com integridade protegida mas transmitidos em claro em esquemas AEAD (ex: headers de pacotes) (Cap 9)

**Attack Game** - Formalização de cenário de ataque como jogo entre adversário e challenger para definir vantagem do adversário (Cap 2-10)

**Birthday Attack** - Ataque genérico que encontra colisão em hash com |T|=N usando O(√N) queries via paradoxo do aniversário (Cap 8)

**Bit-Guessing SS** - Formulação de semantic security onde SSadv*[A,E] = |Pr[^b=b] - 1/2|, equivalente a definição padrão (Cap 2)

**Block Cipher** - Cifra determinística E:(K,X)→X onde E(k,·) é permutação para cada chave k (Cap 4)

**Broadcast Encryption** - Sistema que permite revogar devices usando árvore binária com cover sets de tamanho O(r·log(n/r)) (Cap 5)

**Carter-Wegman MAC** - MAC randomizado S(k1,k2,m) := (r, H(k1,m)+F(k2,r)) combinando UHF com PRF (Cap 7)

**CBC Mode (Cipher Block Chaining)** - Modo de operação c[j+1] = E(k, c[j] ⊕ m[j]) com IV aleatório; CPA-secure mas requer IV imprevisível (Cap 5)

**Chaining Variable** - Valor ti que conecta blocos consecutivos em construção Merkle-Damgård (Cap 8)

**Chosen Ciphertext Attack (CCA)** - Adversário obtém encryptions e decryptions de mensagens/ciphertexts escolhidos (Cap 9)

**Chosen Plaintext Attack (CPA)** - Adversário força sistema a cifrar mensagens escolhidas para extrair informação (Cap 5)

**Ciphertext Expansion** - Ciphertexts mais longos que plaintexts; inevitável para CPA security probabilística (Cap 5)

**Ciphertext Integrity (CI)** - Adversário não consegue criar ciphertext válido novo após ver encryptions de mensagens escolhidas (Cap 9)

**CMAC** - CBC-MAC com randomized prefix-free encoding usando sub-keys k1,k2 derivadas via multiplicação em GF(2^n) (Cap 6)

**Collision Resistance (CR)** - Encontrar m0≠m1 com H(m0)=H(m1) é computacionalmente difícil mesmo sem chaves (Cap 8)

**Compression Function** - Função h:M×Y→X (Merkle-Damgård) ou X×K→X (Davies-Meyer) que preserva CR quando iterada (Cap 8)

**Computational Cipher** - Algoritmos eficientes E (probabilístico) e D (determinístico) com espaços parametrizados por λ (security parameter) (Cap 2)

**Computational Indistinguishability** - Distribuições P₀,P₁ onde Distadv[A,P₀,P₁] é negligível para todo adversário eficiente (Cap 3)

**Counter Mode** - Modo randomizado c[j] ← F(k, x+j) ⊕ m[j]; paralelizável, CPA-secure se F é PRF e N super-poly (Cap 5)

**Cover Set** - Menor conjunto de nós em árvore binária cujos descendentes cobrem exatamente folhas S; usado em broadcast encryption (Cap 5)

**CPA Security** - Semantic security against chosen plaintext attack; adversário distingue encryptions de m₀ vs m₁ com vantagem negligível (Cap 5)

**Davies-Meyer** - Compression function hDM(x,y) := E(y,x) ⊕ x que transforma block cipher em hash CR (Cap 8)

**DES (Data Encryption Standard)** - Block cipher com chave 56-bit, blocos 64-bit, 16 rounds; quebrado por exhaustive search e linear cryptanalysis (Cap 4)

**Deterministic Cipher** - Cifra onde encryption é determinístico; sempre produz mesmo ciphertext para (k,m) fixos (Cap 5)

**Difference Unpredictable Function (DUF)** - Hash onde Pr[H(k,m1)-H(k,m0)=δ] ≤ ε para m0≠m1; mais forte que UHF (Cap 7)

**Distinguisher/Predictor Lemma** - Se d distingue B de R com vantagem ε, então predictor acerta B com probabilidade 1/2+ε (Cap 3)

**ECBC (Encrypted CBC)** - CBC-MAC com encriptação final F(k2, CBC(k1,m)); ANSI standard, streaming MAC (Cap 6)

**ECB Mode (Electronic Codebook)** - E'(k,m) := (E(k,m[0]),...,E(k,m[v-1])); inseguro para multi-block (padrões visíveis) (Cap 4)

**Efficient Algorithm** - Tempo de execução ≤ t(λ) poly-bounded com probabilidade ≥ 1-ε(λ) negligível (Cap 2)

**Elementary Wrapper** - Adversário B = ⟨M',M⟩ onde M' é interface eficiente e tempo de M' ≤ t(λ+I) para I interações (Cap 2)

**Encrypt-then-MAC (EtM)** - c←E(ke,m), tag←S(km,c); sempre seguro para CPA-secure cipher + secure MAC (Cap 9)

**Encrypted PRF (EF)** - EF(k1,k2,m):=F(k2,PF(k1,m)); converte prefix-free PRF em PRF completo (Cap 6)

**Existential Forgery** - Par (m,t) válido onde (m,t)∉{signed pairs}; inclui nova tag em mensagem já assinada (Cap 6)

**Extendable PRF** - Se F(k,x)=F(k,y) então F(k,x||a)=F(k,y||a); propriedade de CBC e cascade (Cap 7)

**Extension Attack** - Dado F'(k,m),
