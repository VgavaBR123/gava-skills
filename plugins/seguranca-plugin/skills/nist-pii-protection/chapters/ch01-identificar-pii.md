# Capítulo 1: Identificar e localizar PII (NIST SP 800-122 §2)

## Ideia central
Não dá para proteger PII que você não sabe que existe. O primeiro passo de
qualquer programa de proteção é **inventariar toda a PII** no ambiente — bancos,
drives compartilhados, backups, sites de terceiros/contratados — usando uma
definição deliberadamente ampla.

## Frameworks introduzidos

- **Definição de PII (duas pontas)**: PII é qualquer informação sobre um
  indivíduo que (1) **distingue ou rastreia** a identidade (nome, CPF/SSN, data
  e local de nascimento, biometria) **ou** (2) é **vinculada ou vinculável**
  (linked/linkable) a essa pessoa (dados médicos, financeiros, educacionais, de
  emprego).
  - Quando usar: ao decidir se um campo entra no inventário de PII.
  - Como: se o dado, sozinho **ou combinado**, pode chegar a uma pessoa, trate
    como PII.

- **Distinguir vs. Rastrear (distinguish vs. trace)**:
  - *Distinguir* = identificar quem é o indivíduo (nome, passaporte, CPF).
  - *Rastrear* = reconstruir ações/status de alguém (ex.: um log de auditoria de
    ações de usuário rastreia atividade).

- **Linked vs. Linkable (vinculado vs. vinculável)** — distinção operacional:
  - *Linked*: a fonte secundária está no mesmo sistema (ou sistema próximo) sem
    controles que segreguem as fontes → associação já é possível.
  - *Linkable*: a fonte secundária está remota, em registros públicos ou
    facilmente obtível (ex.: busca na internet) → associação é *possível*.
  - **Aplicação na auditoria**: dois datasets "anônimos" em sistemas mal
    segregados podem ser *linked* e voltar a identificar pessoas. É o coração da
    Fase 1 (onde o dado pode escapar/reconectar).

## Conceitos-chave
- **PTA / IPA (Privacy Threshold Analysis / Initial Privacy Assessment)**:
  questionário inicial que decide se um sistema contém PII e se exige PIA/SORN.
- **DLP (Data Loss Prevention)**: ferramentas de monitoramento automático de PII
  na rede — um dos métodos de descoberta de PII.
- **Sanitização de hardware aposentado**: PII pode sobreviver em discos antigos;
  inventário inclui mídia descartada (ref. NIST SP 800-88).

## Exemplos de PII (lista do NIST, não exaustiva)
Nome; identificadores (CPF/SSN, passaporte, CNH, número fiscal, conta/cartão);
endereço (postal e e-mail); **IP/MAC** ou identificador persistente que linke a
uma pessoa; telefones; características pessoais (foto de rosto, digitais,
biometria); registro de veículo; e qualquer dado linkável aos anteriores (data/
local de nascimento, raça, religião, etc.). **Identificadores parciais** (alguns
dígitos do CPF) também são PII por serem quase únicos.

## Anti-padrões
- **Achar que "não tem nome, logo não é PII"**: IP, identificador parcial e
  combinações são PII. A ausência de nome não exime.
- **Inventariar só o banco principal**: backups, logs, mídia offsite e sites de
  contratados guardam PII e costumam ficar de fora.

## Conecta com
- **Ch 2 (Níveis de impacto)**: depois de achar a PII, classifique o risco.
- **auditoria-lgpd-fiscal — Fase 1**: mapear o fluxo do dado e onde ele pode
  escapar. O conceito linked/linkable sustenta o veredito de reidentificação.
- **LGPD Art. 5º**: a definição ampla de PII do NIST conversa com "dado pessoal"
  e "dado pessoal sensível" da lei brasileira.
