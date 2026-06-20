# Capítulo 5: Fair Information Practices (NIST SP 800-122 §2.3 / Apêndice D)

## Ideia central
As leis de privacidade (Privacy Act, e por extensão a **LGPD**) repousam sobre os
**Fair Information Practices (FIPs)** — os princípios de privacidade da **OECD**
(1980). São a base conceitual que conecta *privacidade* (amplo) a
*confidencialidade* (o foco do NIST 800-122).

## Framework: os 8 princípios da OECD
1. **Collection Limitation (Limitação de coleta)**: limites à coleta; dados
   obtidos por meios lícitos e justos, com conhecimento/consentimento quando
   cabível.
2. **Data Quality (Qualidade dos dados)**: dados relevantes ao propósito,
   precisos, completos e atualizados.
3. **Purpose Specification (Especificação de finalidade)**: a finalidade deve ser
   declarada **até** o momento da coleta; uso posterior limitado a ela.
4. **Use Limitation (Limitação de uso)**: não divulgar/usar para outros fins sem
   consentimento ou base legal.
5. **Security Safeguards (Salvaguardas de segurança)**: proteger contra perda,
   acesso não autorizado, destruição, uso, modificação ou divulgação.
6. **Openness (Transparência)**: política aberta sobre práticas e a existência/
   natureza dos dados, e a identidade do controlador.
7. **Individual Participation (Participação do indivíduo)**: direito de confirmar,
   acessar, receber, contestar e — se procedente — corrigir/apagar seus dados.
8. **Accountability (Responsabilização)**: o controlador é responsável por
   cumprir os princípios acima.

## Mental model: privacidade ⊃ confidencialidade
Privacidade é mais ampla que proteger a confidencialidade da PII. Para a
**confidencialidade**, os FIPs mais diretos são: **Security Safeguards, Purpose
Specification, Use Limitation, Collection Limitation e Accountability** — é onde
o esforço técnico do 800-122 se concentra. *Openness* e *Individual
Participation* importam à privacidade, mas pouco mexem na confidencialidade.

## Ponte com a LGPD
Os princípios da OECD têm correspondência quase 1:1 com o **Art. 6º da LGPD**
(finalidade, adequação, necessidade, livre acesso, qualidade, transparência,
segurança, prevenção, responsabilização e prestação de contas). Usar os FIPs como
checklist ajuda a traduzir exigência legal em controle técnico.

## Anti-padrões
- **Reduzir privacidade a "criptografar tudo"**: confidencialidade é só uma
  fatia; finalidade, transparência e participação do titular também são exigidas.
- **Coletar "porque pode ser útil depois"**: viola Collection Limitation e
  Purpose Specification (e a minimização da LGPD).

## Conecta com
- **Ch 3 (Salvaguardas)**: Security Safeguards e minimização são a face técnica
  destes princípios.
- **auditoria-lgpd-fiscal — Fase 6 (LGPD by design)**: os FIPs são o vocabulário
  para justificar cada controle perante o jurídico/DPO.
