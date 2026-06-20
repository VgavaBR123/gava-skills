# Capitulo 6: Message integrity

## Ideia central
Message integrity garante que mensagens não foram modificadas em trânsito, usando tags criptográficas computadas com chave secreta compartilhada. Diferente de confidencialidade, o foco é detectar adulteração, não ocultar conteúdo.

## Frameworks introduzidos
- **Message Authentication Code (MAC)**: Par (S, V) onde S(k,m)→t gera tag e V(k,m,t)→{accept,reject} verifica. Usa quando precisa integridade sem sigilo (ex: cotações financeiras públicas, verificação de executáveis).
- **Deterministic MAC**: S determinístico, V aceita iff S(k,m)=t. Tags únicas por (k,m). Base para construções práticas.
- **Prefix-free secure PRF**: PRF seguro apenas contra adversários prefix-free (nenhuma query é prefixo de outra). Bloco de construção intermediário.
- **Extendable PRF**: Se PF(k,x)=PF(k,y) então PF(k,x||a)=PF(k,y||a). Propriedade estrutural de CBC/cascade.
- **Encrypted PRF (EF)**: EF(k1,k2,m):=F(k2,PF(k1,m)). Converte prefix-free PRF em PRF completo via encriptação final.
- **ECBC (Encrypted CBC)**: CBC + encriptação final. ANSI standard, streaming MAC, tags ≥128 bits.
- **NMAC (Nested MAC)**: Cascade + encriptação final. Base do HMAC (IETF), requer embedding K→X.
- **Prefix-free encoding**: Função injetiva pf:M→X^≤ℓ cuja imagem não contém prefixos. Método 1: prepend length (não-streaming). Método 2: stop bits (overhead).
- **Randomized ε-prefix-free encoding**: rpf_ε:K×M→X^≤ℓ onde Pr[rpf(k,m0)⊑rpf(k,m1)]≤ε para m0≠m1. Usa quando quer streaming sem overhead.
- **CMAC**: CBC + rpf com duas chaves (k1,k2) via sub-key generation. NIST 2005, evita dummy blocks, melhor que ANSI.
- **PMAC/PMAC0**: Parallel MAC usando máscaras aditivas (i·k em GF(2^n)). Usa quando tem hardware paralelo; incremental (edições locais baratas).

## Conceitos-chave
- **Chosen message attack**: Adversário obtém tags S(k,mi) para mi arbitrários antes de forjar.
- **Existential forgery**: Par (m,t) válido onde (m,t)∉{signed pairs}. Inclui nova tag em mensagem já assinada (randomized MACs).
- **Streaming MAC**: Não requer conhecer comprimento da mensagem antecipadamente (CBC, CMAC, NMAC sim; prepend-length não).
- **Extension attack**: Dado F'(k,m), computar F'(k,m||m') sem k. Quebra cascade/CBC como MACs diretos.
- **Incremental MAC**: Dado tag(m), recomputar tag(m') para edição local sem reprocessar tudo (PMAC0 com block cipher).
- **Truncation**: Reduzir tag de n→w bits. Adiciona erro 1/2^w na segurança (Theorem 6.2).
- **Sub-key generation (CMAC)**: Deriva (k0,k1,k2) de k via multiplicação em GF(2^n): k1=L·X, k2=L·X^2 mod g(X).
- **Faithful/forgetful gnome**: Técnica de prova: gnome fiel mantém consistência f(x)=f(x); gnome esquecido ignora colisões.
- **Prefix-free set**: S⊆X^≤ℓ onde nenhum elemento é prefixo próprio de outro.
- **Injective padding**: inj:{0,1}^≤nℓ→X^≤ℓ+1 via 100...0 ou dummy block. Sempre expande (pigeonhole).

## Mental models
- Use MAC quando precisa integridade mas não sigilo (news feeds, code signing, database records).
- Use CMAC/PMAC sobre ECBC: CMAC evita dummy blocks, PMAC paraleliza.
- Prefix-free PRF + encoding/encryption → full PRF: três rotas (EF, deterministic pf, randomized rpf).
- Keyless integrity (CRC32, TCP checksum) detecta erros aleatórios, não ataques maliciosos.
- Truncar PRF output OK para PRF, mas degrada MAC security por fator 1/2^w.
- Cascade/CBC inseguros como MACs diretos (extension attacks), mas seguros como prefix-free PRFs.

## Anti-padroes
- **Keyless MAC**: CRC32/checksums não resistem a adversários (conhecem algoritmo, forjam à vontade).
- **All-zero padding**: Não injetivo, m e m||0 têm mesmo tag. Use 100...0 ou CMAC rpf.
- **CBC com random IV**: Totalmente insecure (Exercise 6.9). IV deve ser fixo (0^n) ou usar CMAC.
- **Swap attacks**: MACs não previnem reordenação. Incluir sequence numbers no payload.
- **Timing leaks**: Comparação byte-a-byte de tags vaza informação. Use constant-time comparison.
- **Truncated cascade sem ideal cipher**: Inseguro para PRFs arbitrários (Exercise 6.11). Seguro apenas no ideal cipher model.
- **CMAC com k1=L**: Inseguro (Exercise 6.16). Deve usar k1=L·X, k2=L·X^2 em GF(2^n).

## Exemplos de codigo / Tabelas

**ECBC signing**:
```
t ← 0^n
for i=1 to v:
    t ← F(k1, ai ⊕ t)
output F(k2, t)
```

**NMAC signing**:
```
t ← k1
for i=1 to v:
    t ← F(t, ai)
output F(k2, g(t))  // g: K→X embedding
```

**CMAC rpf**:
```
if |m| multiple of n:
    au ← k1 ⊕ au
else:
    au ← k2 ⊕ (au||100...0)
```

**CMAC sub-key generation**:
```
L ← F(k, 0^n)
k1 ← (L<<1) if msb(L)=0 else (L<<1)⊕R_n
k2 ← (k1<<1) if msb(k1)=0 else (k1<<1)⊕R_n
// R_128 = 0^120||10000111
```

**PMAC0**:
```
t ← 0^n, mask ← 0
for i=1 to v:
    mask ← mask + k  // i·k mod p
    r ← ai + mask
    t ← t ⊕ F1(k1, r)
output F2(k2, t)
```

**Injective padding**:
```
u ← |m| mod n
m' ← m||1||0^(n-u-1)
```

## Worked Example
**Ataque a CBC-MAC**: Adversário quer forjar tag para (a1,a2).
1. Escolhe a1∈X arbitrário
2. Query tag t=F(k,a1) para mensagem (a1)
3. Define a2:=a1⊕t
4. Verifica: CBC((a1,a2))=F(k,F(k,a1)⊕a2)=F(k,a1⊕a1⊕t)=F(k,t)=t
5. Output ((a1,a2),t) como forgery válida

**CMAC para m=128 bits (1 block)**:
- k1,k2 derivados via sub-key gen
- Como |m|=n, usa k1: a1'←a1⊕k1
- CBC: t←F(k0,a1')
- Output t (sem encriptação final, economiza 1 AES)

**PMAC0 incremental update**: Mudar bloco i de ai→ai':
1. t1←D(k2,t)  // decrypt final
2. t2←t1⊕F1(k1,ai+i·k)⊕F1(k1,ai'+i·k)  // swap contribution
3. t'←F2(k2,t2)  // re-encrypt

## Key takeaways
1. MACs requerem chave secreta; keyless schemes (CRC) não resistem a ataques maliciosos
2. Chosen message attack + existential forgery = definição conservadora mas necessária (previne ataques sutis)
3. CBC/cascade são prefix-free secure PRFs, não PRFs completos (extension attacks)
4. Três rotas prefix-free→full: encrypted PRF (ECBC/NMAC), deterministic encoding (prepend/stop-bits), randomized encoding (CMAC)
5. CMAC superior: streaming, sem overhead, usa rpf com sub-keys em GF(2^n)
6. PMAC paraleliza via máscaras i·k, incremental com block ciphers
7. Truncar tags adiciona erro 1/2^w; para 128-bit security precisa |Y|>2^128
8. Padding deve ser injetivo (100...0 ou CMAC rpf), nunca all-zero
9. Security degrada quadraticamente em Q para CBC/cascade (birthday bound Q^2/2|X|)
10. Timing attacks reais: implementar V com constant-time comparison

## Conecta com
- Cap 4 (PRFs): MACs construídos de PRFs via Theorem 6.2
- Cap 5 (CPA security): Integridade ≠ confidencialidade, objetivos ortogonais
- Cap 7 (Carter-Wegman): PMAC usa universal hashing + PRF final
- Cap 8 (Digital signatures): MACs simétricos vs assinaturas públicas
- Cap 9 (Authenticated encryption): Combinar secrecy + integrity (encrypt-then-MAC)
- Finite fields GF(2^n): CMAC sub-keys, PMAC masks, aritmética eficiente
