# Criptografia — HMAC-SHA256 e AES-256-GCM

Checklist técnico para as Fases 3 e 4. Cada item tem o padrão errado e o certo
em Python (biblioteca `cryptography` e stdlib `hmac`/`secrets`), que é o stack
mais comum nesses pipelines.

## Sumário
- [Tokenização com HMAC-SHA256](#tokenizacao-com-hmac-sha256)
- [Criptografia com AES-256-GCM](#criptografia-com-aes-256-gcm)
- [Gestão de chaves](#gestao-de-chaves)

---

## Tokenização com HMAC-SHA256

A tokenização gera um pseudônimo determinístico do CPF/CNPJ para permitir
junção entre tabelas sem expor o valor. O ponto não-negociável: **precisa de
chave secreta**. Hash sem chave de um CPF é reversível por força bruta.

### ERRADO — hash sem chave (CRÍTICO)
```python
import hashlib

# Reversível: o espaço de CPFs válidos é pequeno o suficiente para
# pré-computar uma rainbow table e reverter isso em segundos.
def tokenizar(cpf: str) -> str:
    return hashlib.sha256(cpf.encode()).hexdigest()
```
Por que falha: sem segredo, qualquer um que obtenha o token e conheça o
algoritmo reidentifica o titular. Não é pseudonimização defensável sob a LGPD —
é ofuscação trivial.

### CERTO — HMAC com chave secreta de fonte segura
```python
import hmac
import hashlib
import os

# Chave de ambiente/cofre, nunca no código. >= 32 bytes (256 bits).
_PEPPER = os.environ["FISCAL_HMAC_KEY"].encode()

def tokenizar(documento: str) -> str:
    # Normalize antes (só dígitos) para o token do mesmo CPF bater entre tabelas.
    doc = "".join(filter(str.isdigit, documento))
    return hmac.new(_PEPPER, doc.encode(), hashlib.sha256).hexdigest()
```

### Pontos de verificação
- A chave (pepper) vem de `os.environ`/cofre/KMS, **não** de literal no código.
- A chave tem ≥ 256 bits de entropia real (gerada com `secrets.token_bytes(32)`).
- A normalização do documento é consistente em todo o pipeline (senão o mesmo
  CPF gera tokens diferentes e o cruzamento da malha fiscal quebra).
- A chave é a mesma onde os tokens precisam casar, e idealmente **rotacionável**
  (versione a chave: prefixe o token com um id de versão de chave).
- Se há tabela de-para `token → documento`: ela é dado pessoal pleno, precisa de
  cifra em repouso, controle de acesso restrito e auditoria. Não pode coexistir
  com a chave HMAC no mesmo ambiente da chamada externa.

---

## Criptografia com AES-256-GCM

GCM dá confidencialidade **e** autenticidade, mas é frágil a erro de nonce. As
regras abaixo não são estilo — violar a primeira quebra o sistema.

### ERRADO — nonce reusado / estático (CRÍTICO)
```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

NONCE = b"000000000000"  # estático: reuso garantido — CRÍTICO

def cifrar(chave: bytes, dado: bytes) -> bytes:
    return AESGCM(chave).encrypt(NONCE, dado, None)
```
Por que falha: reusar nonce com a mesma chave em GCM vaza o XOR dos textos
claros e permite recuperar a chave de autenticação (forjar tags). É a falha
clássica e catastrófica do GCM.

### ERRADO — tag de autenticação não verificada
```python
# Decifrar "na mão" e ignorar a tag aceita texto adulterado: vira cifra
# sem integridade. Em GCM a verificação da tag é obrigatória.
```

### CERTO — nonce único por CSPRNG, tag verificada, AAD ligando o contexto
```python
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def cifrar(chave: bytes, dado: bytes, aad: bytes) -> bytes:
    assert len(chave) == 32  # AES-256
    nonce = os.urandom(12)   # único por operação, fonte CSPRNG, 12 bytes
    ct = AESGCM(chave).encrypt(nonce, dado, aad)
    return nonce + ct        # guarde o nonce junto do ciphertext

def decifrar(chave: bytes, blob: bytes, aad: bytes) -> bytes:
    nonce, ct = blob[:12], blob[12:]
    # .decrypt verifica a tag e LEVANTA InvalidTag se adulterado — não capture
    # e ignore essa exceção.
    return AESGCM(chave).decrypt(nonce, ct, aad)
```
O `aad` (associated data) deve carregar o contexto que precisa ser autenticado —
por exemplo o id do registro — para impedir que um blob cifrado seja movido de
um registro para outro.

### Pontos de verificação
- Nonce **único** por operação, de `os.urandom`/`secrets`, 12 bytes. Procure
  nonce estático, contador, timestamp ou derivado do dado.
- Tag verificada na decifragem: `InvalidTag` não pode ser silenciada com
  `try/except: pass`.
- Chave de 32 bytes (256 bits). Se vier de senha, derive com KDF forte e salt;
  nunca use a senha crua como chave.
- Sem `MODE_ECB`, sem CBC sem MAC, sem IV estático. Qualquer um é achado.
- Nonce e ciphertext são persistidos juntos; o nonce não precisa ser secreto,
  mas precisa ser único.

---

## Gestão de chaves

Vale para HMAC e AES:

- Origem: variável de ambiente, secrets manager ou KMS. Nunca código, nunca
  repositório, nunca log.
- Geração: `secrets.token_bytes(32)` / KMS. Não derive de string fixa.
- Rotação: tenha um caminho de rotação (versão de chave embutida no token/blob).
- Separação de ambientes: chave de produção ≠ desenvolvimento/teste.
- Princípio do menor privilégio: o processo que chama o LLM externo **não**
  deveria ter acesso à chave que reverte os tokens.
