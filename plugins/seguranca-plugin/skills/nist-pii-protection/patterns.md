# Padrões e técnicas — NIST SP 800-122

## Inventário de PII (descoberta)
**Quando usar**: antes de qualquer proteção; início da auditoria.
**Como**: PTA/IPA por sistema; revisão de documentação; entrevistas; data calls;
DLP automático; checagem com donos de sistema/dado; sanitização de hardware
aposentado. Cobrir bancos, drives, backups, mídia offsite, sites de contratados.
**Trade-offs**: definição ampla aumenta o esforço, mas evita PII "invisível".

## Classificação por nível de impacto (6 fatores)
**Quando usar**: para calibrar severidade e escolher controles.
**Como**: avaliar Identifiability, Quantity, Field Sensitivity, Context of Use,
Obligation to Protect e Access/Location — **em conjunto**; o fator mais alto
domina. Quantidade só eleva.
**Trade-offs**: subjetivo; documente o racional por instância.

## De-identificação reversível
**Quando usar**: quando registros completos não são necessários (pesquisa,
tendências) mas pode ser preciso reverter.
**Como**: remover/mascarar PII; hash unidirecional ou pseudônimo. Manter a
tabela/chave de reidentificação em **sistema separado e controlado** (AC-5).
**Trade-offs**: nível BAIXO só se chave isolada **e** dados não linkáveis
externamente. Continua sendo dado pessoal (LGPD).

## Anonimização (irreversível)
**Quando usar**: dados de teste, releases públicos, analytics agregado.
**Como**: statistical disclosure limitation — generalizar, suprimir, ruído,
swapping, substituir pela média. Resultado deixa de ser PII.
**Trade-offs**: perde precisão; nem tudo anonimiza (biometria). Dado aleatório
puro perde utilidade estatística — prefira anonimizar PII real.

## Proteção proporcional em 3 camadas
**Quando usar**: sempre, guiado pelo nível de impacto.
**Como**: operacional (políticas + treino) + privacidade (minimização, PIA,
de-id/anon) + segurança (AC-3/5/6/17/19, AU-2/6, IA-2, MP-2..6, SC-9/28, SI-4).
**Trade-offs**: excesso de controle em PII de baixo impacto vira custo sem ganho.

## Resposta a incidente de PII (4 fases)
**Quando usar**: ao detectar/suspeitar de breach de PII.
**Como**: Preparação (plano + canal + notificação) → Detecção/análise (avaliar se
há PII) → Contenção/erradicação/recuperação (preservar prova antes de sanitizar)
→ Pós-incidente (lições + remediação). Coordenação CIO/CPO/jurídico/comunicação.
**Trade-offs**: notificação tardia amplia dano legal e reputacional.

## Minimização como controle primário
**Quando usar**: no design e na revisão periódica do acervo.
**Como**: coletar só o necessário à finalidade; revisar e descartar PII sem
finalidade (respeitando retenção legal).
**Trade-offs**: menos dado = menos dano no vazamento; exige disciplina de
governança.
