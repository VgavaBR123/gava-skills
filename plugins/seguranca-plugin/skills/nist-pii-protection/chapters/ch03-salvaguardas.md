# Capítulo 3: Salvaguardas de confidencialidade da PII (NIST SP 800-122 §4)

## Ideia central
Proteja PII com **três camadas complementares**, sempre por abordagem baseada em
risco (proporcional ao nível do Cap. 2): salvaguardas **operacionais**,
salvaguardas **específicas de privacidade** e **controles de segurança**.

## 1. Salvaguardas operacionais
- **Políticas e procedimentos**: regras de acesso à PII, cronograma de retenção,
  resposta a incidentes, privacidade no ciclo de vida (SDLC), limites de coleta/
  uso/compartilhamento, e consequências por descumprimento. Acordos formais
  (ISA) ao compartilhar PII com sistemas externos.
- **Awareness, Training, Education** (são distintos):
  - *Awareness*: muda comportamento, foca atenção (golpes, vazamentos no
    noticiário, exemplos de responsabilização).
  - *Training*: constrói habilidade — obrigatório antes de conceder acesso à PII.
  - *Education*: forma o profissional de privacidade.

## 2. Salvaguardas específicas de privacidade

- **Minimização (minimum necessary)**: colete/use/retenha só o **estritamente
  necessário** à missão. Revise periodicamente o acervo; descarte o que não tem
  mais finalidade (respeitando retenção legal). Menos PII = menos dano no
  vazamento. *(Princípio espelhado no Art. 6º da LGPD — necessidade/finalidade.)*
- **PIA (Privacy Impact Assessment)**: revisão estruturada de como a informação é
  tratada — o que se coleta, por quê, uso pretendido, com quem se compartilha,
  como se protege. Deve cobrir o risco em **cada etapa do SDLC**.
- **De-Identification (de-identificação)**: remover/obscurecer PII suficiente
  para que o restante não identifique ninguém. **Pode ser revertida** por código/
  algoritmo/pseudônimo. Técnica comum: **função hash unidirecional** sobre a PII.
  - Recebe nível **BAIXO** *somente se* (ambos): (a) o algoritmo/chave/tabela de
    reidentificação fica em **sistema separado e controlado**; (b) os campos não
    são linkáveis via registros públicos/externos.
- **Anonymization (anonimização)**: de-identificação para a qual **não existe
  mais** código/associação de reidentificação. Usa técnicas de *statistical
  disclosure limitation*: **generalizar, suprimir, ruído, swapping, substituir
  pela média**. O resultado **deixa de ser PII**. Útil para dados de teste e
  releases públicos. (Nem tudo anonimiza bem — ex.: biometria.)

> **Ponto crítico para a auditoria**: hash/tokenização que mantém tabela de
> reidentificação = **de-identificação (reversível)**, NÃO anonimização. Conversa
> direto com a tese da `auditoria-lgpd-fiscal`: dado tokenizado/cifrado continua
> sendo dado pessoal sob a LGPD.

## 3. Controles de segurança (seleção do NIST SP 800-53)
| Controle | O que faz para PII |
|----------|--------------------|
| **AC-3 Access Enforcement** | RBAC; acesso só via aplicação; cifrar em repouso |
| **AC-5 Separation of Duties** | quem usa dado de-identificado não acessa a chave de reidentificação |
| **AC-6 Least Privilege** | acesso ao mínimo de PII e mínimo de privilégios |
| **AC-17 Remote Access / AC-19 Mobile** | proibir/limitar acesso remoto e por dispositivo móvel; exigir cifra |
| **AU-2 / AU-6 Auditing** | registrar e revisar acessos à PII |
| **IA-2 Identification & Auth** | identificar/autenticar antes do acesso; 2FA para remoto; timeout 30 min |
| **MP-2..6 Media** | acesso, marcação, armazenamento, transporte e **sanitização** de mídia com PII |
| **SC-9 Transmission Confidentiality** | cifrar PII em trânsito |
| **SC-28 Protection at Rest** | cifrar PII em repouso (disco, backup) |
| **SI-4 System Monitoring** | DLP e monitoramento de transferências suspeitas |

## Anti-padrões
- **Chamar hash de "anonimização"** mantendo tabela/chave de reidentificação.
- **Usar PII real em ambiente de teste**: exige o mesmo nível de proteção da
  produção — prefira dados anonimizados/sintéticos.
- **Gerar dado de teste 100% aleatório**: perde propriedades estatísticas; melhor
  anonimizar a PII real preservando distribuição.

## Conecta com
- **Ch 2**: o nível de impacto escolhe quais controles aplicar.
- **auditoria-lgpd-fiscal — Fases 3 (HMAC), 4 (AES-GCM) e 6 (LGPD by design)**:
  a separação de chave (AC-5) e a cifra em repouso/trânsito (SC-28/SC-9) são os
  controles que a auditoria verifica.
