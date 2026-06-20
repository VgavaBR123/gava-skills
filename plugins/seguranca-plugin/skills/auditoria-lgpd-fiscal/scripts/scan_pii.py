#!/usr/bin/env python3
"""
scan_pii.py — Varredura de primeira passada para auditoria LGPD de pipeline fiscal.

Sinaliza CANDIDATOS a CPF/CNPJ em claro e antipadrões de criptografia em um
repositório. NÃO é um veredito: a saída é uma lista de pontos para inspeção
manual no contexto (ver Fase 1 do SKILL.md). Operação somente-leitura.

Uso:
    python scan_pii.py <caminho-do-repo> [--json]

Sem dependências externas (só stdlib).
"""

import os
import re
import sys
import json
import argparse

# ------------------------- validação de dígito verificador -------------------------

def _valida_cpf(digs: str) -> bool:
    if len(digs) != 11 or digs == digs[0] * 11:
        return False
    for i in (9, 10):
        soma = sum(int(digs[n]) * ((i + 1) - n) for n in range(i))
        dv = (soma * 10) % 11 % 10
        if dv != int(digs[i]):
            return False
    return True


def _valida_cnpj(digs: str) -> bool:
    if len(digs) != 14 or digs == digs[0] * 14:
        return False
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1
    for pesos, pos in ((pesos1, 12), (pesos2, 13)):
        soma = sum(int(digs[n]) * pesos[n] for n in range(pos))
        dv = soma % 11
        dv = 0 if dv < 2 else 11 - dv
        if dv != int(digs[pos]):
            return False
    return True


# ------------------------------- padrões -------------------------------

RE_CPF_FMT = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
RE_CNPJ_FMT = re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b")
RE_DIGITOS = re.compile(r"\b\d{11}\b|\b\d{14}\b")

RE_COLUNA_PII = re.compile(
    r"\b(cpf_cnpj|cpf|cnpj|nr_documento|num_documento|documento|inscricao(?:_municipal)?|contribuinte|\bni\b)\b",
    re.IGNORECASE,
)

RE_HASH_SEM_CHAVE = re.compile(r"hashlib\.(sha1|sha256|md5)\s*\(")
RE_HMAC = re.compile(r"hmac\.")
RE_ECB = re.compile(r"MODE_ECB")
RE_SEGREDO_HARDCODED = re.compile(
    r"\b(KEY|SECRET|PEPPER|PASSWORD|PASSWD|TOKEN|CHAVE|SENHA)\b\s*=\s*[\"'bf]",
)
RE_USA_ENV = re.compile(r"os\.environ|getenv|secrets\.|os\.urandom")
RE_LOG = re.compile(r"\b(print|logging\.\w+|logger\.\w+)\s*\(")
RE_NONCE_LITERAL = re.compile(r"\.encrypt\s*\(\s*b[\"']")
RE_NONCE_ESTATICO = re.compile(r"\b(NONCE|IV)\b\s*=\s*b[\"']")

EXT_CODIGO = {".py", ".sql", ".ipynb", ".sh", ".js", ".ts", ".env"}
DIRS_IGNORAR = {".git", "node_modules", "__pycache__", ".venv", "venv", ".mypy_cache"}


def _candidato_pii(linha: str):
    """Retorna ('CPF'|'CNPJ', valor) se a linha tem PII de alta confiança, senão None."""
    if RE_CPF_FMT.search(linha):
        return ("CPF", RE_CPF_FMT.search(linha).group())
    if RE_CNPJ_FMT.search(linha):
        return ("CNPJ", RE_CNPJ_FMT.search(linha).group())
    for m in RE_DIGITOS.finditer(linha):
        d = m.group()
        if len(d) == 11 and _valida_cpf(d):
            return ("CPF", d)
        if len(d) == 14 and _valida_cnpj(d):
            return ("CNPJ", d)
    return None


def analisar_linha(linha: str):
    """Retorna lista de (severidade, categoria, detalhe) para uma linha."""
    achados = []
    baixa = linha.lower()

    pii = _candidato_pii(linha)
    if pii:
        em_log = bool(RE_LOG.search(linha))
        sev = "CRITICO" if em_log else "ALTO"
        achados.append((sev, f"PII {pii[0]} em claro",
                        "em log/print" if em_log else "valor identificável no código"))

    if RE_HASH_SEM_CHAVE.search(linha) and not RE_HMAC.search(linha):
        if RE_COLUNA_PII.search(linha) or "doc" in baixa:
            achados.append(("CRITICO", "Hash sem chave de documento",
                            "hash puro de CPF/CNPJ é reversível — use HMAC com chave"))
        else:
            achados.append(("MEDIO", "Hash sem chave",
                            "confirme se aplica a PII; se sim, use HMAC com chave"))

    if RE_ECB.search(linha):
        achados.append(("CRITICO", "AES em modo ECB", "ECB vaza padrões — use AES-256-GCM"))

    if RE_NONCE_LITERAL.search(linha) or RE_NONCE_ESTATICO.search(linha):
        achados.append(("CRITICO", "Nonce/IV literal em encrypt",
                        "nonce estático = reuso — gere com os.urandom(12)"))

    if RE_SEGREDO_HARDCODED.search(linha) and not RE_USA_ENV.search(linha):
        achados.append(("CRITICO", "Segredo hardcoded",
                        "chave/senha literal — mova para variável de ambiente/cofre"))

    if RE_LOG.search(linha) and RE_COLUNA_PII.search(linha):
        achados.append(("ALTO", "Possível PII em log",
                        "variável de documento dentro de print/logging"))

    return achados


def varrer(raiz: str):
    resultados = []
    for dirpath, dirnames, filenames in os.walk(raiz):
        dirnames[:] = [d for d in dirnames if d not in DIRS_IGNORAR]
        for nome in filenames:
            ext = os.path.splitext(nome)[1].lower()
            if ext not in EXT_CODIGO and nome != ".env":
                continue
            caminho = os.path.join(dirpath, nome)
            try:
                with open(caminho, "r", encoding="utf-8", errors="ignore") as fh:
                    for n, linha in enumerate(fh, 1):
                        for sev, cat, det in analisar_linha(linha):
                            resultados.append({
                                "arquivo": os.path.relpath(caminho, raiz),
                                "linha": n,
                                "severidade": sev,
                                "categoria": cat,
                                "detalhe": det,
                                "trecho": linha.strip()[:120],
                            })
            except OSError:
                continue
    # .env rastreado é achado por si só
    return resultados


ORDEM = {"CRITICO": 0, "ALTO": 1, "MEDIO": 2, "BAIXO": 3}


def main():
    ap = argparse.ArgumentParser(description="Scanner LGPD de primeira passada")
    ap.add_argument("repo", help="caminho do repositório a varrer")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    args = ap.parse_args()

    if not os.path.isdir(args.repo):
        print(f"erro: {args.repo} não é um diretório", file=sys.stderr)
        sys.exit(1)

    res = sorted(varrer(args.repo), key=lambda r: (ORDEM.get(r["severidade"], 9), r["arquivo"]))

    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return

    if not res:
        print("Nenhum candidato encontrado. Confirme manualmente as fronteiras (Fase 1).")
        return

    print(f"\n{len(res)} candidato(s) — confirme cada um no contexto:\n")
    for r in res:
        print(f"  [{r['severidade']:<8}] {r['categoria']}")
        print(f"            {r['arquivo']}:{r['linha']}  — {r['detalhe']}")
        print(f"            > {r['trecho']}")
    crit = sum(1 for r in res if r["severidade"] == "CRITICO")
    print(f"\nResumo: {crit} crítico(s) de {len(res)} candidato(s). "
          f"Lembre: candidatos, não veredito — a Fase 1 decide a severidade real.")


if __name__ == "__main__":
    main()
