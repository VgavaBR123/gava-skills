# Capitulo 18: Protocols for identification and login

## Ideia central
Protocolos de identificação permitem que uma parte (prover) prove sua identidade a outra (verifier) para obter acesso a recursos, enfrentando três níveis de ameaça: ataques diretos, eavesdropping e ataques ativos (incluindo phishing e fake ATMs).

## Frameworks introduzidos
- **Attack Game 18.1 (Direct attacks)**: Adversário recebe vk e tenta se passar pelo prover sem interagir com ele. Use quando o canal é fisicamente protegido (door locks, login local).
- **Attack Game 18.2 (Eavesdropping attacks)**: Adversário obtém Q transcripts de conversas legítimas antes de tentar impersonation. Use para wireless key fobs onde o canal pode ser observado.
- **Attack Game 18.3 (Active attacks)**: Adversário interage ativamente com o prover (probing phase) antes de tentar se passar por ele. Use para ATMs falsos, phishing, malware Trojan.
- **HOTP (Hash-based One-Time Password)**: sk := (k,i), vk := (k,i); prover envia F(k,i) e incrementa i. Use quando vk pode ser mantido secreto e sincronização é garantida.
- **TOTP (Time-based OTP)**: Contador i incrementa a cada 30s automaticamente; servidor aceita F(k, i±c) para clock skew. Use quando usuários humanos precisam digitar passwords curtos.
- **S/key**: vk := H^(n+1)(k); na j-ésima sessão prover envia H^(n-j+1)(k). Use quando vk pode ser público mas número de sessões é limitado (n ≈ 10^6).
- **Challenge-Response (MAC-based)**: Verifier envia c ← M; prover responde t ← S_mac(k,c). Use quando vk deve ser secreto mas ataques ativos são possíveis.
- **Challenge-Response (signature-based)**: Igual ao anterior mas usa assinaturas; vk pode ser público. Use quando comprometimento do verifier não pode expor segredos.
- **PBKDF2**: y := x₀ ⊕ x₁ ⊕ ··· ⊕ x_(d-1) onde xᵢ = F(pw, xᵢ₋₁). Use para derivar chaves de passwords com dificuldade ajustável d.
- **Scrypt**: Constrói array (x₀,...,x_d) sequencialmente; depois lê posições aleatórias j = int(yᵢ₋₁) mod (d+1). Use quando resistência a hardware paralelo customizado é crítica.
- **Rainbow tables**: Preprocessing gera chains pw₁ → f₁(pw₁) → f₂(...) → z₁; ataque inverte y testando f_ℓ∘···∘f₁(gᵢ(y)) contra endpoints. Use para inverter funções hash com time-space tradeoff ℓ²×t ≈ N².

## Conceitos-chave
- **Stateless vs stateful protocols**: Stateless mantém (vk,sk) fixos; stateful atualiza após cada execução (mais seguro mas requer sincronização).
- **One-sided vs mutual identification**: One-sided apenas prover se identifica; mutual ambos se autenticam (Exercício 18.1).
- **Public vs secret verification keys**: vk público permite comprometimento do verifier sem perda de segurança; vk secreto requer proteção do servidor.
- **Man-in-the-middle (MiTM)**: Adversário relaya mensagens de ID protocol e depois "hijacks" a sessão; requer session key exchange para defesa.
- **Common password problem**: Usuários reutilizam passwords em múltiplos sites; servidor de baixa segurança expõe credentials para sites de alta segurança.
- **Online dictionary attack**: Adversário tenta passwords do dicionário D diretamente no servidor; defesa: exponential backoff após falhas.
- **Offline dictionary attack**: Adversário obtém password file e testa H(w) = vk para w ∈ D localmente; leva tempo O(|D|).
- **Batch offline attack**: Com preprocessing L de pares (pw, H(pw)), cracking de |F| hashes leva O(|D| + |F|) em vez de O(|D|×|F|).
- **Public salt**: salt ← S armazenado em claro; força adversário a processar D×S em vez de apenas D; requer |S| ≥ ℓ (ex: 128 bits).
- **Secret salt (pepper)**: pepper ← S_p não armazenado; verifier testa todos p ∈ S_p; aumenta trabalho do adversário em |S_p| (ex: 2^12 = 4096×).
- **Memory-hard functions**: Avaliação requer Ω(d) memória em muitos passos; previne ataques com hardware paralelo customizado (GPUs, FPGAs, ASICs).
- **Data-oblivious memory-hard**: Padrão de acesso à memória independente de password; defende contra cache timing attacks (ex: Argon2i-B).
- **Cumulative memory complexity**: mem[A,h,x] := Σᵢ|stᵢ| mede memória total×tempo; Scrypt requer Ω(d²n) mesmo com time-space tradeoffs.
- **Chain merge problem**: Em Hellman tables, colisões fazem chains compartilharem elementos; rainbow tables usam fᵢ diferentes por coluna para evitar.
- **Reduction function**: g: Y → P mapeia outputs de hash de volta para password space; permite construir chains f(pw) := g(h(pw)).

## Mental models
- Use **password protocol version 1** (vk := H(pw)) apenas se adversário não pode eavesdrop nem comprometer servidor; versão naive (vk := pw) nunca use.
- Use **public salts** sempre que armazenar hashed passwords; previne preprocessing attacks se |S| ≥ ℓ onde ℓ é tamanho máximo da advice string.
- Use **slow memory-hard hash** (Scrypt, Argon2) em vez de secret salts; defende contra custom hardware attacks que PBKDF2 não previne.
- Use **TOTP** em vez de HOTP para humanos; passwords expiram em 30s limitando janela de ataque mesmo se password é roubado.
- Use **S/key** quando vk deve ser público mas stateful protocol é aceitável; após n sessões regenere (vk,sk).
- Use **signature-based challenge-response** quando vk deve ser público e stateless; MAC-based quando vk pode ser secreto e responses devem ser curtos.
- Use **client-side salt** H(pw, id_user, id_server) para mitigar common password problem; protege mesmo se servidor não usa salt.
- **Biometrics** use apenas como second-factor; são irrevocáveis e não-secretos (fingerprints em objetos).

## Anti-padroes
- **Storing cleartext passwords**: Comprometimento do servidor expõe todos passwords; sempre hash com salt.
- **Hashing passwords com SHA256 apenas**: Offline dictionary attack leva <1 minuto para 50% de passwords humanos usando CrackStation dictionary (1.5B entries); use PBKDF.
- **PBKDF1 (iterated hash)**: H^(d)(pw,salt) é d× mais fácil de inverter que H (Exercise 14.18); use PBKDF2 ou Scrypt.
- **Reusing passwords across sites**: Low-security site compromise expõe credentials para high-security sites; use password manager ou client-side salt.
- **Password protocols contra active adversaries**: Single-flow protocols (HOTP, S/key) falham; adversário impersonating verifier aprende one-time password válido.
- **PBKDF2 para múltiplas dificuldades**: Se adversário obtém y₀ := PBKDF2(pw,s,d) e y₁ := PBKDF2(pw,s,d+1), recupera pw em O(|P|) independente de d (Exercise 18.2).
- **Scrypt com j := int(h(i))**: Adversário conhece ordem de reads antecipadamente; pode avaliar com d/3 memória (Exercise 18.5); use j := int(yᵢ₋₁) mod (d+1).
- **Timing-vulnerable password check**: Loop que retorna ao primeiro byte diferente vaza informação; adversário recupera h com 256×|h| queries (Exercise 18.17); use constant-time comparison.
- **Rainbow tables sem salts**: Preprocessing O(N) permite ataques batch em O(|F|); salts forçam O(|D|×|F|).

## Exemplos de codigo / Tabelas

```python
# Password protocol version 2 (com salt)
def G():
    pw = random_choice(P)
    salt = random_choice(S)  # S = {0,1}^128
    y = H(pw, salt)
    return sk=(pw), vk=(salt, y)

def P(sk):
    return sk  # envia pw

def V(vk, pw_received):
    salt, y = vk
    return H(pw_received, salt) == y

# PBKDF2
def PBKDF2(pw, salt, d):
    x0 = F(pw, salt)
    y = x0
    for i in range(1, d):
        xi = F(pw, x_{i-1})
        y = y ⊕ xi
    return y

# Scrypt (simplified)
def Scrypt(x0, d):
    # Step 1: build array
    x = [x0]
    for i in range(1, d+1):
        x.append(h(x[i-1]))
    
    # Step 2: random reads
    y = x[d]
    for i in range(1, d+1):
        j = int(y) % (d+1)
        y = h(y ⊕ x[j])
    return y

# Rainbow table preprocessing
def A0(h, ℓ, λ):
    L = []
    for i in range(λ):
        pw = random_choice(P)
        z = pw
        for j in range(ℓ):
            z = f_j(z)  # f_j(pw) = g_j(h(pw))
        L.append((pw, z))
    return L

# Rainbow table attack
def A1(L, y):
    for i in range(ℓ, 0, -1):
        z = f_ℓ ∘ ... ∘ f_i(g_{i-1}(y))
        if (pw, z) in L:
            pw' = f_{i-1} ∘ ... ∘ f_1(pw)
            if h(pw') == y:
                return pw'
    return fail
```

**Password statistics (2016)**:
- Top password: "123456" (4% dos usuários)
- Top 25: ~10% dos usuários
- CrackStation dictionary: 1.5B passwords, cobre ~50% de passwords humanos
- 8-char passwords (95 chars): 9^8 ≈ 2^52; SHA256 exhaustive search: poucos dias em GPU array

**Time-space tradeoffs**:
| Method | Table size | Attack time | Preprocessing |
|--------|-----------|-------------|---------------|
| Hellman | ℓ | t onde ℓ²t ≈ N² | O(N) |
| Rainbow | ℓ | t onde ℓ²t ≈ N² | O(N) |
| Permutation | ℓ | t onde ℓt ≈ N | O(N) |

## Worked Example

**Offline dictionary attack com preprocessing em password file**:

Setup: Servidor armazena password file sem salt:
```
id_1: SHA256(pw_1) = vk_1
id_2: SHA256(pw_2) = vk_2
...
id_1M: SHA256(pw_1M) = vk_1M
```

Adversário obtém file via server compromise.

**Fase 1 - Preprocessing** (one-time, antes de obter file):
- Dictionary D = CrackStation (1.5B passwords)
- Constrói L = {(pw, SHA256(pw)) : pw ∈ D}
- Armazena L em hash table (Cuckoo hashing)
- Tempo: O(|D|) = 1.5B hashes SHA256 ≈ 1 minuto em GPU

**Fase 2 - Attack** (após obter file):
```python
cracked = []
for (id, vk) in password_file:
    if vk in L:  # O(1) lookup
        pw = L[vk]
        cracked.append((id, pw))
```
- Tempo: O(|F|) = 1M lookups ≈ segundos
- Taxa de sucesso: ~50% (750K passwords crackeados)
- Total: O(|D| + |F|) vs O(|D|×|F|) sem preprocessing

**Defesa com salt**:
```
id_1: salt_1, SHA256(pw_1, salt_1)
```
- Adversário precisa processar D×S onde |S| = 2^128
- Preprocessing inviável: |L| ≈ 1.5B × 2^128
- Força O(|D|×|F|): 1.5B × 1M hashes por password

**Defesa com Scrypt** (d = 2^20, n = 256 bits):
- Cada hash requer 2^20 × 256 bits = 32 MB memória
- GPU com 8GB: apenas 250 Scrypt engines paralelos
- vs 1M+ SHA256 engines em custom ASIC
- Tempo para 1M passwords: 1M × 1.5B × (tempo_Scrypt) ≈ anos mesmo em GPU farm

## Key takeaways
1. **Passwords humanos são fracos**: 50% estão em dicionários de 1.5B entries; SHA256 simples permite cracking em <1 minuto; sempre use PBKDF com d suficientemente alto
2. **Salts públicos são essenciais**: |S| ≥ 2^128 previne preprocessing attacks; força adversário a gastar O(|D|×|F|) em vez de O(|D|+|F|) para batch attacks
3. **Memory-hard functions defendem contra hardware**: Scrypt/Argon2 com d escolhido para encher cache força adversário a usar poucos engines paralelos; PBKDF2 vulnerável a custom ASICs
4
