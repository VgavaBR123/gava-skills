# Capítulo 4: Resposta a incidentes com PII (NIST SP 800-122 §5)

## Ideia central
Vazamento de PII **não é incidente comum**: atrai mídia, destrói confiança e
expõe pessoas a roubo de identidade/chantagem. O plano de resposta padrão
(NIST SP 800-61) precisa de **adições específicas de PII** em cada uma das suas
quatro fases.

## Framework: 4 fases (SP 800-61) + extensões de PII

1. **Preparação** *(exige o maior esforço)*
   - Embutir o plano de PII no plano de resposta existente; treinar com
     *tabletop exercises*.
   - Criar canal de reporte sempre disponível; definir o que é "breach de PII".
   - Dados a coletar de quem reporta: quem reportou/descobriu, data/hora,
     natureza, sistema e interconexões, descrição da informação comprometida,
     mídia, controles existentes, nº de afetados, se a polícia foi acionada.
   - **Plano de notificação**: se/quando/como notificar afetados, fonte,
     conteúdo, meio, quem recebe, e se haverá **serviço remediador** (ex.:
     monitoramento de crédito) — decidido pelo **nível de impacto** (Cap. 2).

2. **Detecção e análise**
   - Pode usar a tecnologia atual, mas o processo deve **avaliar se o incidente
     envolve PII** e reportar interna e externamente conforme exigido.

3. **Contenção, erradicação e recuperação**
   - Passos extras de sanitização ao remover PII da mídia. **Não sanitizar PII
     antes** de decidir se ela é prova (forense; consultar jurídico).
   - Determinar **se** a PII foi acessada e **quantos** registros/pessoas.

4. **Pós-incidente**
   - Lições aprendidas alimentam o plano; podem exigir treino/controles novos.
   - Decidir assistência remediadora aos afetados (cópia de relatório de crédito,
     *freeze*, alerta de fraude, contato com instituições financeiras).

## Conceito-chave: coordenação multifuncional
Incidentes de PII exigem CIO, CPO/DPO, dono do sistema, dono do dado, jurídico e
comunicação atuando juntos, com **papéis definidos antes** do incidente.

## Threshold de referência (contexto federal EUA)
Agências federais reportam breach de PII ao **US-CERT em até 1 hora**. No Brasil,
o paralelo é a **comunicação à ANPD e ao titular** em prazo razoável (LGPD Art.
48) — confirme o prazo regulatório vigente.

## Anti-padrões
- **Tratar breach de PII como incidente de TI comum**: ignora notificação,
  remediação e o aspecto reputacional/legal.
- **Sanitizar a mídia antes de preservar prova**: destrói evidência necessária a
  litígio/prosecução.

## Conecta com
- **Ch 2**: o nível de impacto decide notificação e remediação.
- **auditoria-lgpd-fiscal — Fase 6**: o plano de resposta é parte do "LGPD by
  design"; um achado de PII em claro deve disparar revisão do plano de incidentes.
