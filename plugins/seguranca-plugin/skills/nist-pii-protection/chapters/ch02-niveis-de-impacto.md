# Capítulo 2: Níveis de impacto de confidencialidade da PII (NIST SP 800-122 §3)

## Ideia central
**Nem toda PII é igual.** Antes de escolher salvaguardas, classifique cada
instância de PII em um nível de impacto de confidencialidade — **baixo, moderado
ou alto** — pelo dano potencial caso seja acessada, usada ou divulgada
indevidamente. Aplique proteção proporcional ao risco ("se guardarmos escovas de
dente e diamantes com igual zelo, perderemos mais diamantes").

## Framework: três níveis de impacto (FIPS 199)
- **BAIXO**: a perda causaria efeito adverso **limitado** — dano menor, não passa
  de inconveniência (ex.: trocar um número de telefone).
- **MODERADO**: efeito adverso **sério** — perda financeira por roubo de
  identidade, humilhação pública, discriminação, potencial de chantagem.
- **ALTO**: efeito **severo ou catastrófico** — dano físico, social ou
  financeiro grave, podendo incluir risco de vida ou detenção indevida.

> Regra: o nível PII é **distinto** do nível FIPS 199 do sistema; ele
> *suplementa* a categorização e indica se proteções adicionais são necessárias.

## Framework: os 6 fatores de determinação do nível
Avalie **em conjunto** — um fator alto sobrepõe outro baixo:

1. **Identifiability (Identificabilidade)**: quão diretamente o dado identifica
   alguém. CPF/digital identificam direto (impacto maior); CEP+data de
   nascimento identificam indiretamente; DDD+gênero, em geral, não.
2. **Quantity of PII (Quantidade)**: quantos indivíduos. 25 vs. 25 milhões de
   registros mudam o impacto. **Só pode elevar, nunca rebaixar** o nível.
3. **Data Field Sensitivity (Sensibilidade do campo)**: CPF, histórico médico e
   conta financeira são mais sensíveis que telefone/CEP. **Combinações** elevam
   (nome + cartão). Regra comum: presença de CPF/SSN ⇒ nível ≥ moderado.
4. **Context of Use (Contexto de uso)**: a finalidade muda o nível. Os *mesmos*
   campos (nome, endereço, telefone) podem ser baixo (assinantes de newsletter),
   moderado (aposentadoria) ou alto (agentes disfarçados).
5. **Obligation to Protect (Obrigação de proteger)**: leis/contratos (Privacy
   Act, HIPAA, GLBA — no Brasil, **LGPD**, sigilo fiscal). Decida sempre com o
   jurídico/DPO. Determinado cedo no processo.
6. **Access to and Location (Acesso e localização)**: quanto mais acesso e
   quanto mais a PII trafega offsite/teletrabalho, maior a exposição → nível
   maior.

## Worked Example — os 3 cenários do NIST
- **Roster de resposta a incidentes** (nomes, telefones, e-mails de <20 pessoas,
  já públicos no site) → **BAIXO**: identifica direto, mas divulgação causa pouco
  dano.
- **Log de atividade na intranet** (IP, URL, data/hora): sozinho não identifica,
  mas há um **sistema próximo** com login↔IP → admins podem correlacionar
  (*linked*). Muitos registros, dano potencial só de constrangimento → **BAIXO**.
- **Denúncias de fraude/abuso** (texto livre com nome, endereço; ~50 PII em 1000
  registros): expor a identidade de quem denuncia gera medo de retaliação,
  chantagem, perda de emprego → **ALTO** (dano catastrófico).

A lição: **o mesmo tipo de campo recebe níveis diferentes pelo contexto e pela
correlação**, não pelo formato isolado.

## Anti-padrões
- **Rebaixar nível por dataset pequeno**: quantidade só eleva.
- **Classificar campo isolado ignorando combinação e contexto**: nome+cartão e
  "agentes disfarçados" mudam tudo.

## Conecta com
- **Ch 3 (Salvaguardas)**: o nível escolhido dita os controles aplicados.
- **auditoria-lgpd-fiscal — Fase 2 (PII em claro)**: usar os fatores para
  **calibrar a severidade do achado** em vez de tratar todo CPF igual.
