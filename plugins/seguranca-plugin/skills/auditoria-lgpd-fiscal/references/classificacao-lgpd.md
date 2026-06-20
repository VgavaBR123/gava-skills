# Classificação LGPD — pseudonimização × anonimização

Referência para as Fases 1, 5 e 6. O veredito da auditoria depende de classificar
corretamente cada conjunto de dados que cruza uma fronteira. Errar aqui leva a
"liberar" para um LLM externo um dado que ainda é pessoal.

## As três categorias

**Dado identificado / identificável** — permite reconhecer o titular direta ou
indiretamente (CPF, CNPJ de pessoa, nome + endereço, etc.). É dado pessoal pleno
(LGPD Art. 5º, I). CNPJ de pessoa jurídica em si não é dado pessoal, mas quando
liga a uma pessoa natural (MEI, sócio, titular) entra no regime.

**Dado pseudonimizado** — passou por tratamento que tira a identificação direta,
mas **pode ser revertido** com informação mantida em separado (a chave). LGPD
Art. 13, §4º: pseudonimização é o tratamento pelo qual o dado perde a
possibilidade de associação **direta** ao titular, a não ser com uso de
informação adicional mantida separada e controlada.

> Ponto central: **dado pseudonimizado continua sendo dado pessoal** e
> continua sob a LGPD. Tokenização HMAC e criptografia reversível são
> pseudonimização. A chave/token-map é a "informação adicional" — e vira o
> ativo mais sensível do sistema.

**Dado anonimizado** — o titular **não pode mais ser identificado**,
considerando meios técnicos razoáveis disponíveis na ocasião (Art. 5º, XI).
Quando de fato anônimo, sai do escopo da LGPD (Art. 12). Mas o Art. 12, §1º
avisa: se a reversão for possível com esforço razoável, volta a ser dado pessoal.
Agregação, generalização e supressão que impedem singularização tendem à
anonimização; substituição reversível **não**.

## Por que isso decide o veredito na fronteira do LLM

Cenário típico deste pipeline: "tokenizei os CPFs com HMAC, então posso mandar
para o Bedrock/Claude Code". A classificação correta:

- O dado que sai é **pseudonimizado**, logo **ainda é dado pessoal**.
- Se a chave HMAC e os tokens estão no mesmo ambiente que faz a chamada, a
  reversão é trivial → trate como **tratamento de dado pessoal por operador
  externo**, exigindo base legal, avaliação de transferência e cláusulas
  contratuais adequadas.
- Só se aproxima de "fora da LGPD" se o que cruza for verdadeiramente anônimo
  (ex.: agregados sem singularização) ou se o token for irreversível **e** a
  chave estiver fora de alcance de quem opera o serviço externo.

Checklist de classificação para cada conjunto que cruza fronteira:

1. Há valor identificável (CPF/CNPJ/nome) presente? → identificado, **pare aqui**,
   não cruza fronteira exposta.
2. Há token/cifra reversível com chave acessível no mesmo perímetro? →
   pseudonimizado = dado pessoal; só cruza com base legal e controles.
3. É agregado/generalizado a ponto de não singularizar ninguém, sem chave de
   reversão razoável? → tende a anônimo; documente o raciocínio de
   irreversibilidade.

## Princípios que o código deve refletir

- **Minimização** (Art. 6º, III): só as colunas necessárias à finalidade saem do
  perímetro. `SELECT *` rumo a uma fronteira é quase sempre violação.
- **Finalidade** (Art. 6º, I): o uso na fronteira (ex.: análise via LLM) tem que
  bater com a finalidade declarada da coleta.
- **Segurança** (Art. 6º, VII; Art. 46): medidas técnicas proporcionais —
  é onde tokenização e AES-GCM corretos entram.
- **Necessidade e segregação**: a chave que reverte pseudonimização fica separada
  do dado pseudonimizado e de quem opera serviços externos.

## Observação

Esta referência orienta a auditoria técnica; não é parecer jurídico. Decisões
sobre base legal, transferência internacional e relatório de impacto (RIPD)
envolvem o jurídico/DPO da organização.
