# Capitulo 21: Authenticated Key Exchange

## Ideia central
Protocolos AKE permitem dois usuarios estabelecerem uma chave de sessao compartilhada sobre rede insegura, garantindo autenticidade (saber com quem se fala) e sigilo (chave indistinguivel de aleatoria mesmo sob observacao de outras sessoes).

## Frameworks introduzidos
- **Static Security**: Adversario nunca compromete chaves de longo prazo de usuarios honestos (baseline de seguranca)
- **Perfect Forward Secrecy (PFS)**: Compromisso futuro de chaves de longo prazo nao revela chaves de sessao passadas (usa chaves efemeras)
- **HSM Security**: Defende contra adversario que acessa Hardware Security Module durante protocolo, limitando dano temporal e numericamente
- **Identity Protection**: Adversario (passivo ou ativo) nao aprende identidade de um ou ambos participantes
- **One-Sided Authentication**: Cliente sem certificado estabelece canal seguro com servidor certificado
- **Deniability**: Participante pode negar ter executado protocolo (evidencias sao simulaveis)
- **Channel Bindings**: Nome globalmente unico para sessao (session ID)

## Conceitos-chave
- **Session Key**: Chave fresca gerada por cada execucao do protocolo, independente de outras sessoes
- **Trusted Third Party (TTP)**: Entidade que facilita comunicacao; offline (CA emite certificados) ou online (participa de cada sessao)
- **User Instance**: Cada execucao do protocolo por um usuario (mesmo usuario = multiplas instancias)
- **Partner Function**: Mecanismo que determina quais instancias compartilham chave e quais sao vulneraveis (computavel do log de rede)
- **Freshness**: Garantia que chaves de sessoes diferentes sao efetivamente independentes
- **Authenticity**: Chave k compartilhada com instancia de Q implica Q pensa estar falando com P
- **Secrecy**: Chave k indistinguivel de aleatoria mesmo vendo outras session keys
- **Ephemeral Data**: Dados temporarios (ex: expoentes DH) que devem ser apagados apos protocolo
- **Key Compromise Integrity (KCI)**: Vulnerabilidade onde compromisso da chave de Q permite ataque contra Q
- **Strongly Unpredictable Ciphertexts**: Ciphertext serve como desafio imprevisivel mesmo para chaves adversariais

## Mental models
- Use PFS quando: chaves de longo prazo podem ser comprometidas no futuro (protege sessoes passadas)
- Use HSM security quando: dados efemeros podem vazar durante execucao (malware temporario, implementacao ruim)
- Use identity protection quando: rastreamento de localizacao/atividade e preocupacao (dispositivos moveis)
- Use deniability quando: participante precisa negar interacao futura (evidencias nao devem ser convincentes)
- Assuma CCA-secure encryption quando: adversario pode manipular ciphertexts (binding de identidades requer integridade)
- Prefira offline TTP quando: disponibilidade e problema ou revogacao e simples via CRL

## Anti-padroes
- **Sequenciar identificacao + key exchange anonimo**: Man-in-the-middle pode "hijack" sessao apos autenticacao
- **Nao assinar ciphertext c**: Adversario substitui c por c' com chave conhecida (key exposure attack)
- **Nao assinar nonce r**: Adversario reusa mensagens antigas (replay attack, viola freshness)
- **Nao assinar identidade do peer**: Adversario registra usuario R com chave publica de P (identity misbinding)
- **Nao criptografar identidade no ciphertext**: Adversario reusa c com assinatura de usuario corrupto R (replay com misbinding)
- **Usar apenas semantic security (nao CCA)**: Adversario manipula ciphertext (ex: XOR attack em ETDF, Bleichenbacher em PKCS1)
- **Nao incluir marcadores de fluxo (1/2)**: Adversario faz instancia pensar que fala consigo mesma
- **Nao apagar dados efemeros**: Vazamento de α em ElGamal permite impersonation permanente
- **Encapsular protocolo inteiro no HSM**: Viola requisito de HSM stateless; adversario pode espaçar queries no tempo

## Exemplos de codigo / Tabelas

**Protocol AKE1 (encryption-based, static security)**:
```
P → Q: r, CertP
Q → P: c := EncP(k, idQ), σ := SigQ(r, c, idP), CertQ
P outputs: k, idQ
Q outputs: k, idP
```

**Protocol AKE1eg (ElGamal variant)**:
```
P → Q: r, CertP  
Q → P: v := g^β, σ := SigQ(r, v, idP), CertQ
k := H(uP, v, v^αP, idQ)  // uP = g^αP
```

**Protocol AKE2 (ephemeral encryption, PFS)**:
```
P → Q: pk, σ1 := SigP(pk), CertP
Q → P: c := E(pk, (k, idQ)), σ2 := SigQ(pk, c, idP), CertQ
```

**Protocol AKE3 (HSM security, 3 flows)**:
```
P → Q: pk, CertP
Q → P: c := E(pk, k), σ1 := SigQ(1, pk, c, idP), CertQ
P → Q: σ2 := SigP(2, pk, c, idQ)
```

**Protocol AKE5 (deniability for P)**:
```
P → Q: g^μ, CertP
Q → P: g^ν, k1, CertQ
P → Q: k2
(k, k1, k2) := H(g^(α+μ)(β+ν), g^μν, g^α, g^μ, g^β, g^ν, idP, idQ)
```

**Partner Function (AKE1)**:
- Right instance J: vulnerable se idP corrupto, senao fresh
- Left instance I: connected to J se fluxos loosely match, senao vulnerable

## Worked Example

**Ataque em Variation 1 (nao assinar c)**:

Setup: Protocolo modificado onde σ = SigQ(r, idP) (sem c)

Ataque:
1. Adversario intercepta (c, σ, CertQ) de Q→P
2. Adversario computa c' := EncP(k', idQ) com k' escolhida
3. Adversario envia (c', σ, CertQ) para P

Resultado:
- P aceita (σ valida para r, idP)
- P decripta c' → obtem k' (conhecida pelo adversario)
- Q tem k (desconhecida)
- Violacao: key exposure

Exploracao real (banco):
- Se P=cliente, Q=banco: adversario le primeira requisicao (dados sensiveis)
- Se P=banco, Q=cliente: adversario injeta transacao arbitraria

**Simulacao de deniability (AKE5)**:

Objetivo: Q nao pode provar a terceiro que falou com P

Simulador (sem acesso a P):
1. Escolhe μ ← Zq, envia (g^μ, CertP) para Q
2. Q responde (g^ν, k1, CertQ)
3. Simulador busca query H(...) que produziu k1
4. Se input tem forma correta (verifica DH-triple), extrai k2
5. Envia k2 para Q

Propriedade: View de Q e identico ao protocolo real (Q poderia gerar sozinho)

## Key takeaways

1. **Cada componente e essencial**: Remover qualquer assinatura/criptografia de identidade/nonce abre ataques especificos (key exposure, replay, misbinding)
2. **CCA security e necessaria para binding**: Semantic security permite manipulacao de ciphertexts (ataques XOR, Bleichenbacher)
3. **PFS requer chaves efemeras**: Usar mesma chave publica permite recuperacao de sessoes passadas se chave comprometida
4. **HSM security exige 3 fluxos**: Ambos peers devem assinar desafios aleatorios para limitar dano temporal
5. **Apagar dados efemeros e critico**: Vazamento de α/β em DH permite impersonation; derandomize assinaturas (Exercise 13.6)
6. **Identity protection vs deniability**: Criptografar identidades protege observadores; nao assinar permite simulacao
7. **Partner function define seguranca**: Deve ser computavel do log de rede; "loosely matching" permite flexibilidade
8. **One-sided authentication e pratico**: Cliente sem certificado usa password sobre canal one-sided para upgrade
9. **Channel bindings permitem referencia global**: (idP, idQ, pk, c) identifica sessao unicamente
10. **Offline TTP preferivel**: CA emite certificados uma vez; online TTP e ponto de falha e requer segredos compartilhados

## Conecta com

- **Cap 9 (Authenticated Encryption)**: Session keys alimentam canais seguros com AE
- **Cap 10.1 (Anonymous Key Exchange)**: Diffie-Hellman sem autenticacao e componente de AKE
- **Cap 11 (Public-Key Encryption)**: CCA security necessaria para binding; ElGamal/RSA usados
- **Cap 12 (KEM)**: ElGamal como KEM with associated data (Exercise 12.18)
- **Cap 13 (Signatures)**: Autenticacao via assinaturas; derandomizacao evita vazamento
- **Cap 18-19 (Identification)**: AKE = identification + anonymous key exchange (mas nao sequencial)
- **Section 13.8 (Certificate Authority)**: TTP offline emite certificados binding identity→public key
- **Section 21.11.1 (Password-based upgrade)**: One-sided authentication + password → mutual authentication
- **Section 21.12 (Online TTP)**: Kerberos-style protocols com segredos compartilhados
