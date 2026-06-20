#!/usr/bin/env python3
"""Gera uma skill no estilo book-to-skill usando o OpenRouter na etapa de geracao.

A extracao (scripts/extract.py + pdftotext) NAO consome token. Este script gasta
saldo do OpenRouter apenas na geracao: detecta a estrutura do livro, escreve um
arquivo por capitulo e depois glossary/patterns/cheatsheet/SKILL.md.

Fluxo recomendado:
  1) extrair:   python <skill>/scripts/extract.py LIVRO.pdf --mode text|technical
                (gera %TEMP%/book_skill_work/full_text.txt)
  2) gerar:     set OPENROUTER_API_KEY=sk-or-...        (PowerShell: $env:OPENROUTER_API_KEY="sk-or-...")
                python tools/generate_skill_openrouter.py \
                  --text "%TEMP%/book_skill_work/full_text.txt" \
                  --name nist-pii-protection \
                  --out plugins/seguranca-plugin/skills/nist-pii-protection \
                  --model anthropic/claude-sonnet-4.5 \
                  --book-type technical --depth study --lang pt

Utilitarios:
  python tools/generate_skill_openrouter.py --check --model <slug>   # testa chave+modelo (custo ~0)
  python tools/generate_skill_openrouter.py --list-models            # lista candidatos fortes

A chave NUNCA e impressa nem gravada. Use sempre a variavel de ambiente.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODELS_URL = "https://openrouter.ai/api/v1/models"

# Precos de referencia (USD por 1M tokens). Ajuste se necessario; usados so para
# estimar custo no log. Chave = prefixo do slug.
PRICE_HINTS = {
    "anthropic/claude-sonnet": (3.0, 15.0),
    "anthropic/claude-opus": (15.0, 75.0),
    "anthropic/claude-3.5-haiku": (0.8, 4.0),
    "openai/gpt-4o": (2.5, 10.0),
    "google/gemini-2.0-flash": (0.1, 0.4),
    "google/gemini-pro": (1.25, 5.0),
    "deepseek/deepseek-chat": (0.27, 1.1),
}


def price_for(model):
    for prefix, pair in PRICE_HINTS.items():
        if model.startswith(prefix):
            return pair
    return None


class Tally:
    def __init__(self, model):
        self.model = model
        self.inp = 0
        self.out = 0

    def add(self, usage):
        self.inp += usage.get("prompt_tokens", 0)
        self.out += usage.get("completion_tokens", 0)

    def cost(self):
        p = price_for(self.model)
        if not p:
            return None
        return self.inp / 1e6 * p[0] + self.out / 1e6 * p[1]

    def line(self):
        c = self.cost()
        c_str = f" | ~${c:.3f}" if c is not None else " | (preco do modelo desconhecido)"
        return f"tokens acumulados: in={self.inp:,} out={self.out:,}{c_str}"


def _key():
    k = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not k:
        sys.exit("ERRO: defina OPENROUTER_API_KEY no ambiente (nao passe a chave por argumento).")
    return k


def chat(messages, model, max_tokens=2600, temperature=0.2, retries=4):
    body = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }).encode("utf-8")
    req = urllib.request.Request(API_URL, data=body, method="POST")
    req.add_header("Authorization", "Bearer " + _key())
    req.add_header("Content-Type", "application/json")
    req.add_header("HTTP-Referer", "https://github.com/VgavaBR123/gava-skills")
    req.add_header("X-Title", "gava-skills book-to-skill generator")
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"]
            usage = data.get("usage", {}) or {}
            return content, usage
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "ignore")[:400]
            last = f"HTTP {e.code}: {detail}"
            if e.code in (429, 500, 502, 503):
                time.sleep(2 ** attempt)
                continue
            break
        except urllib.error.URLError as e:
            last = f"rede: {e}"
            time.sleep(2 ** attempt)
    sys.exit(f"ERRO na chamada ao OpenRouter: {last}")


def strip_fences(s):
    s = s.strip()
    if s.startswith("```"):
        s = re.sub(r"^```[a-zA-Z]*\n", "", s)
        s = re.sub(r"\n```\s*$", "", s)
    return s.strip()


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:40] or "secao"


def lang_clause(lang):
    if lang == "pt":
        return ("Escreva em PORTUGUES do Brasil, mas PRESERVE os nomes canonicos "
                "de frameworks, termos tecnicos e siglas no original (ex.: PII, "
                "AES-GCM, Fair Information Practices, low/moderate/high).")
    return "Write in English."


# ---------- Passos ----------

def detect_structure(text, model, tally, lang):
    sample = text[:14000]
    msg = [
        {"role": "system", "content": "Voce extrai a estrutura de livros tecnicos. Responda SOMENTE JSON valido."},
        {"role": "user", "content": (
            "Abaixo esta o inicio (e o sumario) de um documento. Retorne JSON com:\n"
            '{\"title\": str, \"author\": str, \"chapters\": [{\"n\": int, \"title\": str, \"anchor\": str}]}\n'
            "Onde \"anchor\" e uma substring EXATA e curta (3-8 palavras) que marca o inicio do corpo "
            "daquele capitulo/secao no texto (um titulo de cabecalho real, nao a linha do sumario). "
            "Liste apenas capitulos/secoes substantivos (ignore agradecimentos, indices). "
            "Maximo 12 capitulos.\n\n--- TEXTO ---\n" + sample)},
    ]
    out, usage = chat(msg, model, max_tokens=1200, temperature=0.0)
    tally.add(usage)
    try:
        data = json.loads(strip_fences(out))
    except json.JSONDecodeError:
        sys.exit("ERRO: modelo nao retornou JSON de estrutura valido:\n" + out[:500])
    return data


def slice_chapters(text, chapters):
    """Localiza cada anchor (ultima ocorrencia) e fatia o texto entre eles."""
    positions = []
    for ch in chapters:
        anchor = (ch.get("anchor") or "").strip()
        idx = text.rfind(anchor) if anchor else -1
        positions.append((idx, ch))
    # mantem so anchors achados, em ordem de posicao
    found = sorted([p for p in positions if p[0] >= 0], key=lambda x: x[0])
    slices = []
    for i, (start, ch) in enumerate(found):
        end = found[i + 1][0] if i + 1 < len(found) else len(text)
        slices.append((ch, text[start:end]))
    return slices


def gen_chapter(ch, body, model, tally, book_type, depth, lang):
    tech = book_type == "technical"
    budget = {"text": 1400, "technical": 2400}[book_type] if depth == "study" else \
             {"text": 1000, "technical": 1500}[book_type]
    sys_p = ("Voce transforma capitulos de livros em fichas de skill para agentes. "
             "Extraia ESTRUTURA (frameworks nomeados, principios acionaveis, tecnicas, "
             "anti-padroes) e NUNCA copie texto cru. Densidade > completude. " + lang_clause(lang))
    tmpl = (
        "# Capitulo {n}: <titulo>\n\n## Ideia central\n<1-2 frases>\n\n"
        "## Frameworks introduzidos\n- **<Nome exato>**: <formulacao> (quando usar / como)\n\n"
        "## Conceitos-chave\n- **<Termo>**: <definicao em 1 frase> (5-10 termos)\n\n"
        "## Mental models\n<2-4: 'Use X quando Y'>\n\n"
        "## Anti-padroes\n- **<O que evitar>**: <por que falha>\n\n"
        + ("## Exemplos de codigo / Tabelas\n<preserve sintaxe exata se houver>\n\n" if tech else "")
        + ("## Worked Example\n<reconstrua 1 exemplo concreto do capitulo>\n\n" if depth == "study" else "")
        + "## Key takeaways\n1. <acionavel>\n\n## Conecta com\n- <outro cap/conceito>\n")
    user = (f"Capitulo n={ch.get('n')} titulo='{ch.get('title')}'. "
            f"Orcamento ~{budget} tokens (densidade, sem encher linguica). "
            f"Use exatamente este molde de secoes:\n\n{tmpl}\n\n--- CONTEUDO DO CAPITULO ---\n{body[:120000]}")
    out, usage = chat([{"role": "system", "content": sys_p}, {"role": "user", "content": user}],
                      model, max_tokens=int(budget * 1.6))
    tally.add(usage)
    return strip_fences(out)


def gen_support(kind, chapters_md, meta, model, tally, lang):
    specs = {
        "glossary": ("glossary.md", "Todos os termos significativos, ordem alfabetica. "
                     "Formato: `**Termo** - definicao (Cap N)`. Max 1500 tokens.", 1800),
        "patterns": ("patterns.md", "Todas as tecnicas/algoritmos/padroes. Formato: "
                     "`## Nome\\n**Quando usar**:\\n**Como**:\\n**Trade-offs**:`. Max 2000 tokens.", 2300),
        "cheatsheet": ("cheatsheet.md", "Regras de decisao ('Quando X, faca Y, porque Z'), tabelas "
                       "de trade-off, thresholds e 'tells & smells'. Tabelas compactas, nada de "
                       "definicoes soltas. Max 1200 tokens.", 1500),
    }
    fname, rule, mx = specs[kind]
    joined = "\n\n".join(chapters_md)[:60000]
    sys_p = "Voce consolida fichas de capitulo em um arquivo de apoio de skill. " + lang_clause(lang)
    user = f"Livro: {meta.get('title')} ({meta.get('author')}).\nGere o {fname}.\nRegras: {rule}\n\n--- FICHAS ---\n{joined}"
    out, usage = chat([{"role": "system", "content": sys_p}, {"role": "user", "content": user}], model, max_tokens=mx)
    tally.add(usage)
    return strip_fences(out)


def gen_skill_md(name, meta, chapters, chapters_md, model, tally, lang):
    index = "\n".join(
        f"| [ch{int(c['n']):02d}](chapters/ch{int(c['n']):02d}-{slugify(c['title'])}.md) | {c['title']} |"
        for c in chapters)
    sys_p = ("Voce escreve o SKILL.md mestre de uma skill de conhecimento. Corpo < 4000 tokens, "
             "conteudo mais importante PRIMEIRO. " + lang_clause(lang))
    user = (
        f"Crie o SKILL.md para a skill '{name}'. Livro: {meta.get('title')} por {meta.get('author')}.\n"
        "Estrutura obrigatoria:\n"
        "1) Frontmatter YAML com name e description (description comeca com 'Use ao/quando', "
        "lista os topicos centrais, sem resumir o passo a passo).\n"
        "2) Titulo + linha de metadados.\n3) '## Como usar esta skill'.\n"
        "4) '## Frameworks centrais' (os mais importantes, formulacao exata, ~2000 tokens).\n"
        "5) '## Indice de capitulos' (use EXATAMENTE a tabela abaixo).\n"
        "6) '## Indice de topicos' (termo -> chNN, alfabetico).\n"
        "7) '## Arquivos de apoio' (glossary.md, patterns.md, cheatsheet.md).\n"
        "8) '## Escopo e limites'.\n\n"
        f"Tabela de capitulos a incluir:\n| # | Titulo |\n|---|--------|\n{index}\n\n"
        "Resumo das fichas para extrair os frameworks centrais:\n" + ("\n\n".join(chapters_md))[:40000])
    out, usage = chat([{"role": "system", "content": sys_p}, {"role": "user", "content": user}], model, max_tokens=3200)
    tally.add(usage)
    return strip_fences(out)


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content.rstrip() + "\n")
    print(f"  ok  {path}")


def cmd_list_models():
    req = urllib.request.Request(MODELS_URL)
    req.add_header("Authorization", "Bearer " + _key())
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    strong = []
    for m in data.get("data", []):
        mid = m.get("id", "")
        if any(k in mid for k in ("claude-sonnet", "claude-opus", "gpt-4", "gemini-2", "gemini-pro", "deepseek")):
            strong.append(mid)
    print("Candidatos fortes disponiveis no OpenRouter:")
    for s in sorted(set(strong)):
        print("  " + s)


def cmd_check(model):
    out, usage = chat([{"role": "user", "content": "responda apenas: ok"}], model, max_tokens=5)
    print(f"OK - modelo '{model}' respondeu. usage={usage}")


def main():
    ap = argparse.ArgumentParser(description="Gera skill book-to-skill via OpenRouter.")
    ap.add_argument("--text", help="caminho do full_text.txt extraido")
    ap.add_argument("--name", help="slug da skill (ex.: anpd-anonimizacao)")
    ap.add_argument("--out", help="diretorio de saida da skill")
    ap.add_argument("--model", default="anthropic/claude-sonnet-4.5", help="slug do modelo OpenRouter")
    ap.add_argument("--book-type", choices=["text", "technical"], default="text")
    ap.add_argument("--depth", choices=["reference", "study"], default="study")
    ap.add_argument("--lang", choices=["pt", "en"], default="pt")
    ap.add_argument("--check", action="store_true", help="testa chave+modelo e sai")
    ap.add_argument("--list-models", action="store_true", help="lista modelos fortes e sai")
    args = ap.parse_args()

    if args.list_models:
        cmd_list_models(); return
    if args.check:
        cmd_check(args.model); return
    if not (args.text and args.name and args.out):
        ap.error("--text, --name e --out sao obrigatorios (ou use --check/--list-models)")

    with open(args.text, encoding="utf-8") as f:
        text = f.read()
    print(f"Texto: {len(text):,} chars (~{len(text)//4:,} tokens) | modelo: {args.model}")

    tally = Tally(args.model)
    print("1/4 detectando estrutura...")
    meta = detect_structure(text, args.model, tally, args.lang)
    chapters = meta.get("chapters", [])
    print(f"    {meta.get('title')} - {len(chapters)} capitulos | {tally.line()}")

    slices = slice_chapters(text, chapters)
    if not slices:
        sys.exit("ERRO: nenhum anchor de capitulo localizado no texto.")

    print(f"2/4 gerando {len(slices)} capitulos...")
    chapters_md = []
    used_chapters = []
    for ch, body in slices:
        md = gen_chapter(ch, body, args.model, tally, args.book_type, args.depth, args.lang)
        n = int(ch.get("n", len(used_chapters) + 1))
        write(os.path.join(args.out, "chapters", f"ch{n:02d}-{slugify(ch['title'])}.md"), md)
        chapters_md.append(md)
        used_chapters.append({"n": n, "title": ch["title"]})
        print(f"    {tally.line()}")

    print("3/4 gerando arquivos de apoio...")
    for kind in ("glossary", "patterns", "cheatsheet"):
        content = gen_support(kind, chapters_md, meta, args.model, tally, args.lang)
        write(os.path.join(args.out, f"{kind}.md"), content)

    print("4/4 gerando SKILL.md...")
    skill_md = gen_skill_md(args.name, meta, used_chapters, chapters_md, args.model, tally, args.lang)
    write(os.path.join(args.out, "SKILL.md"), skill_md)

    print("\nConcluido. " + tally.line())
    print(f"Skill em: {args.out}")
    print("Revise o SKILL.md (frontmatter/description) antes de commitar.")


if __name__ == "__main__":
    main()
