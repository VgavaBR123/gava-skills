# Cheatsheet — NIST SP 800-122 (proteção de PII)

## Decisão: qual nível de impacto? (avalie os 6 fatores juntos)
| Fator | Empurra para ALTO quando… |
|-------|---------------------------|
| Identifiability | identifica direto (CPF, digital, nome) |
| Quantity | muitos indivíduos (só **eleva**, nunca rebaixa) |
| Field sensitivity | CPF, saúde, financeiro; ou combinação (nome+cartão) |
| Context of use | exposição causa retaliação/risco (denúncia, agente disfarçado) |
| Obligation to protect | há lei/contrato (LGPD, sigilo fiscal, HIPAA, GLBA) |
| Access/Location | muito acesso, trafega offsite/remoto |

Regra prática: **presença de CPF/SSN ⇒ nível ≥ moderado**.

## Decisão: de-identificação vs. anonimização
- Preciso poder **reverter** (chave/tabela existe)? → **de-identificação**
  (reversível) → **continua sendo dado pessoal (LGPD)**. Nível BAIXO só se a
  chave fica isolada **E** os dados não são linkáveis externamente.
- **Não** existe mais associação de reidentificação? → **anonimização** → deixa
  de ser PII.
- ⚠️ Hash/HMAC com tabela de reidentificação = de-identificação, **não**
  anonimização.

## Linked vs. Linkable (reidentificação)
- **Linked**: fonte secundária no mesmo sistema/sistema próximo sem segregação.
- **Linkable**: fonte remota, pública ou facilmente obtível.
- Dois datasets "anônimos" mal segregados podem reidentificar → tratar como PII.

## Controles mínimos por nível (orientação)
| Nível | Controles típicos |
|-------|-------------------|
| Baixo | AC-3 (acesso), AU-2 (log), minimização |
| Moderado | + AC-6 (least privilege), SC-9/SC-28 (cifra trânsito/repouso), IA-2 (auth) |
| Alto | + AC-5 (segregação de chave), AC-17/19 (limitar remoto/móvel), 2FA, MP-6 (sanitização), SI-4 (DLP) |

## Reporte de incidente — não esqueça
Avaliar se envolve PII → preservar prova **antes** de sanitizar → contar
registros/afetados → notificar (EUA: US-CERT em 1h; **Brasil: ANPD + titular**,
LGPD Art. 48) → decidir remediação pelo nível de impacto.

## Tells & smells (sinais de problema)
- Campo "anonimizado" mas existe tabela de/para → é pseudônimo, é PII.
- PII real em ambiente de teste → exige proteção de produção; anonimize.
- Identificador parcial (alguns dígitos do CPF) tratado como não-PII → é PII.
- Dataset pequeno classificado como baixo "porque é pequeno" → quantidade não
  rebaixa.

## Mapa rápido → fases da auditoria-lgpd-fiscal
| Fase da auditoria | Capítulo de apoio |
|-------------------|-------------------|
| 1 — Mapear fluxo do dado | Ch 1 (identificar PII; linked/linkable) |
| 2 — PII em claro | Ch 2 (níveis de impacto / severidade) |
| 3–4 — Tokenização/Cifra | Ch 3 (de-id vs. anon; AC-5, SC-9/28) |
| 6 — LGPD by design | Ch 3 (minimização) + Ch 5 (FIPs) |
