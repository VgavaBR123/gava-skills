# Capitulo 23: Secure multi-party computation

## Ideia central
MPC permite que N partes avaliem uma funcao f(x1,...,xn)=(y1,...,ym) de forma distribuida, garantindo que entradas permanecem privadas, saidas sao corretas e entradas sao escolhidas independentemente—mesmo se algumas partes forem maliciosas.

## Frameworks introduzidos
- **Beaver's 2.5-party protocol**: Usa dealer D para pre-processar Beaver triple sharings ([a],[b],[c]) onde c=ab; P1 e P2 avaliam circuito aritmetico via sharings aditivos (quando: circuitos aritmeticos sobre Zq, honest majority)
- **Garbled circuits (Yao)**: P1 gera encoding F do circuito, P2 avalia localmente com tokens garbled; usa OT para inputs (quando: circuitos booleanos, constant-round, 2-party)
- **Authenticated sharings**: Estende sharings [x] com MACs [x^(1)], [x^(2)] usando chaves K^(1), K^(2) para detectar adulteracao (quando: proteger contra malicious adversaries)
- **Protocol 23.5 (Proving product relations)**: Dealer prova (ak1+ak2)(bk1+bk2)=(ck1+ck2) via polynomial interpolation e random challenge (quando: verificar integridade de Beaver triples)

## Conceitos-chave
- **Privacy**: Nenhuma parte aprende inputs alheios exceto o que outputs revelam inerentemente
- **Soundness**: Partes honestas computam outputs corretos (se computam algum)
- **Input independence**: Partes escolhem inputs independentemente dos inputs alheios
- **Guaranteed output delivery**: Todas partes honestas obtem outputs (propriedade forte)
- **Fairness**: Se qualquer parte obtem output, todas honestas tambem obtem (mais fraca que guaranteed delivery)
- **Honest-but-curious**: Adversario segue protocolo mas vaza estado interno (modelo fraco)
- **Malicious adversary**: Adversario pode desviar arbitrariamente do protocolo (modelo forte)
- **Static vs adaptive corruption**: Adversario corrompe partes no inicio vs dinamicamente durante execucao
- **Sharing [x]=(x1,x2)**: P1 guarda x1, P2 guarda x2, onde x=x1+x2 em Zq (additive secret sharing)
- **Beaver triple sharing**: ([a],[b],[c]) onde a,b random e c=ab; permite multiplicacao segura via z=uv+ub+va+c onde u=x-a, v=y-b

## Mental models
- Use Beaver protocol quando precisar avaliar circuitos aritmeticos com multiplicacoes caras mas adicoes baratas (custo proporcional a #multiplication gates)
- Use garbled circuits quando precisar constant-round communication e puder tolerar circuitos booleanos maiores
- Use authenticated sharings x=([x],[x^(1)],[x^(2)]) quando precisar detectar adulteracao: abrir x a Pi requer K^(i)x=x^(i) (falha com prob 1-1/q se corrupto)
- Use dealer honesto + Protocol 23.5 quando precisar verificar product relations sem revelar shares (collision-resistance + polynomial check)

## Anti-padroes
- **Replicar trusted server T**: Hacker invade replica e obtem todos bids perdedores (Failure Scenario 1)
- **Enviar ambos tokens Xi^(0), Xi^(1) sem OT**: P2 avalia gate com ambos tokens e descobre input x2 de P1 (Fig 23.7)
- **Processar inputs sem autenticacao**: Corrupt Pi muda share xi, causando output incorreto que vaza info sobre input honesto (ex: f(x)=x(x-1) revela bit)
- **Usar mesmo garbled circuit F em multiplos inputs**: Compromete security (garbling nao e reusavel)

## Exemplos de codigo / Tabelas

```python
# Beaver multiplication gate (Fig 23.3)
# P1: input x1,y1,a1,b1,c1
# P2: input x2,y2,a2,b2,c2
u1 = x1 - a1;  v1 = y1 - b1
u2 = x2 - a2;  v2 = y2 - b2
# Exchange u1,v1 <-> u2,v2
u = u1 + u2;  v = v1 + v2
z1 = u*v + u*b1 + v*a1 + c1  # P1
z2 = u*b2 + v*a2 + c2        # P2
# z1+z2 = xy
```

```python
# Garbled gate encoding (Garble0)
# Tokens: X^(0),X^(1) (input1), Y^(0),Y^(1) (input2), Z^(0),Z^(1) (output)
E^(a,b) = H(A^(a), B^(b), gID) XOR C^(g(a⊕r, b⊕s)⊕t)
G = (gID, E^(0,0), E^(0,1), E^(1,0), E^(1,1))
# GateEval: Z = H(X,Y,gID) XOR E^(type(X),type(Y))
```

| Gate type | Beaver protocol | Garbled circuit |
|-----------|----------------|-----------------|
| Addition | Local: z1=x1+y1, z2=x2+y2 | Local: tokens |
| Multiplication | Interactive: 4 Zq elements | Garbled table: 4 ciphertexts |
| Rounds | O(multiplicative depth) | O(1) constant |

## Worked Example
**Vickrey auction com MPC**: Bidders P1,...,PN submetem bids x1,...,xN. Trusted server T anuncia vencedor (highest bid) e preco (second-highest). Failure scenarios: (1) hacker invade T pos-auction, rouba losing bids revelando estrategias; (2) T collude com bidder, revela current highest antes de deadline; (3) T crash apos anunciar a alguns mas nao todos.

**Solucao via Beaver 2.5-party**: Circuito aritmetico f computa (winner_id, second_price). Cada Pi gera sharing [xi] de seu bid via singleton sharing do dealer. Circuito processa comparacoes (via subcircuitos aritmeticos) e selecao usando multiplication gates. Dealer distribui Beaver triples. P1,P2 avaliam circuito: adicoes locais, multiplicacoes via open [u],[v] e compute z=uv+ub+va+c. Output phase: ambos obtem (winner, price). Privacy: shares [xi] nao revelam xi; soundness: authenticated sharings forcam correct computation; input independence: singleton sharings sao random.

## Key takeaways
1. MPC elimina single point of failure distribuindo computacao entre N partes com threshold de corrupcao
2. Beaver protocol: custo = O(#multiplication gates), rounds = O(multiplicative depth); garbled circuits: custo = O(circuit size), rounds = O(1)
3. Honest-but-curious -> malicious: adicione authenticated sharings x com MACs K^(i)x=x^(i) (abort se check falha)
4. Dealer honesty: Protocol 23.5 usa polynomial interpolation + random challenge r para verificar product relations com prob 1-2m/q
5. Garbling requer projective input encoding + OT para receiver privacy (sem OT, curious P2 testa ambos tokens e descobre input)
6. Multi-party via secure core: N parties Qj usam 3-party core (P1,P2,D); inputs via authenticated shares com validity codes V=sum(R*check); outputs via masking G

## Conecta com
- Cap 8.12: commit-and-reveal auction (MPC esconde losing bids)
- Cap 9: TLS para secure point-to-point channels (assumido em MPC)
- Cap 11.6: 1-out-of-2 OT (essencial para garbled circuits)
- Cap 18.6.1: CRYPTOcard com key splitting k=k1⊕k2 (caso especial de MPC)
- Cap 20: Zero knowledge como 2-party MPC (prover input w, verifier output R(w,x))
- Cap 22: Threshold cryptography (MPC para algebraic schemes como RSA, ElGamal)
