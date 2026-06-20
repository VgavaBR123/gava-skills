# Padrões de detecção — CPF/CNPJ e antipadrões de cripto

O que o scanner (`scripts/scan_pii.py`) procura, e onde cada padrão gera
falso-positivo. Use isto para interpretar a saída e para fazer a varredura
manual quando preferir não rodar o script.

## CPF / CNPJ

### Formatados (alta confiança)
- CPF: `\d{3}\.\d{3}\.\d{3}-\d{2}`  →  `123.456.789-09`
- CNPJ: `\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}`  →  `12.345.678/0001-95`

Pontuação dedicada quase nunca é coincidência — trate como achado a confirmar.

### Crus, só dígitos (ruidoso)
Sequências de 11 ou 14 dígitos podem ser CPF/CNPJ ou podem ser id, telefone,
código de barras, chave de NF-e (44 dígitos), etc. Para cortar ruído, o scanner
**valida o dígito verificador** de candidatos de 11 e 14 dígitos e só reporta os
que passam na validação. Mesmo assim, confirme no contexto: um número válido
pode ser um dado de teste inofensivo.

### Nomes de coluna/variável reveladores
Sinalize identificadores que carregam o dado mesmo sem o valor à vista:
`cpf`, `cnpj`, `cpf_cnpj`, `nr_documento`, `num_documento`, `ni`, `documento`,
`inscricao`, `inscricao_municipal`, `contribuinte`. O risco aparece quando uma
dessas variáveis/colunas chega a uma fronteira (log, retorno, export, prompt de
LLM) sem ter passado pela tokenização/cifra.

## Antipadrões de criptografia

| Padrão buscado | Por quê | Severidade base |
|---|---|---|
| `hashlib.sha256(`/`md5(`/`sha1(` perto de `cpf`/`cnpj`/`documento` | hash sem chave é reversível | CRÍTICO |
| `MODE_ECB` | ECB vaza padrões do texto claro | CRÍTICO |
| nonce/IV literal (`b"..."`/`bytes(12)`) passado a `.encrypt(`/`AES.new(` | nonce estático = reuso | CRÍTICO |
| `except InvalidTag`/`except Exception` seguido de `pass` perto de `decrypt` | tag ignorada na decifragem | ALTO |
| atribuição literal a `KEY`/`SECRET`/`PEPPER`/`PASSWORD`/`TOKEN` | chave/segredo hardcoded | CRÍTICO |
| `.env` rastreado pelo git / ausente do `.gitignore` | segredo versionado | ALTO |
| `print(`/`logging.*` contendo variável de PII | PII em log | ALTO |
| CPF/CNPJ em f-string de URL/`requests.get(...params no path)` | PII em query string | CRÍTICO |

## Falso-positivo: onde tomar cuidado

- **Dado de teste**: CPF/CNPJ válido em `tests/`/`fixtures/` pode ser sintético e
  inofensivo — rebaixe para BAIXO se não for sensível e não cruzar fronteira real.
- **Hash com chave**: `hmac.new(chave, cpf, sha256)` é o padrão **correto** — não
  confunda com `hashlib.sha256(cpf)`. O scanner tenta distinguir, mas confirme.
- **`os.urandom`/`secrets`**: nonce vindo dessas fontes é o caminho certo; só o
  nonce literal/estático é problema.
- **`os.environ[...]`** para chave é o esperado — não é hardcoding.
- **Número de 11/14 dígitos que passa no DV** mas é, no contexto, um id de
  sistema: valide olhando o uso, não só o valor.

A regra geral: o scanner aponta candidatos; a fronteira (Fase 1) decide a
severidade. Um CPF que nunca sai de uma variável local cifrada é diferente de um
que vai para `print()`.
