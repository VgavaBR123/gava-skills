# gava-seguranca

Auditoria de conformidade **LGPD** para pipelines de dados fiscais (CPF/CNPJ),
para qualquer IDE que leia `AGENTS.md` (Cursor, GitHub Copilot, Windsurf, Codex,
Gemini CLI, Zed, JetBrains).

```bash
npx gava-seguranca init
```

Instala no seu projeto:

```
AGENTS-lgpd.md                         ← instruções de auditoria para o agente
seguranca/references/criptografia.md   ← checklist HMAC-SHA256 / AES-256-GCM
seguranca/references/classificacao-lgpd.md
seguranca/references/padroes-deteccao.md
seguranca/scan_pii.py                  ← scanner de primeira passada
```

Opções: `npx gava-seguranca init --force` (sobrescreve) · `npx gava-seguranca help`.

> Também funciona direto do GitHub, sem npm:
> `npx github:VgavaBR123/gava-skills init` *(use o pacote da pasta `packages/gava-seguranca`)*.

## Como usar

Depois do `init`, peça ao agente da sua IDE:

```
Audite a conformidade LGPD deste pipeline seguindo o AGENTS-lgpd.md.
```

Para uma varredura rápida antes da análise manual:

```bash
python seguranca/scan_pii.py .
```

## No Claude Code / Cowork

Esta mesma auditoria também está disponível como skill nativa via marketplace:

```bash
/plugin marketplace add VgavaBR123/gava-skills
/plugin install seguranca-plugin@gava-tools
```

## Licença

[MIT](../../LICENSE) — mantido por **Gava**.
