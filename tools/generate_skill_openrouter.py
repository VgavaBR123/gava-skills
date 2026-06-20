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

def detect_meta(text, model, tally):
    """Pega titulo e autor com uma chamada minima (inicio do livro)."""
    sample = text[:4000]
    msg = [
        {"role": "system", "content": "Responda SOMENTE JSON valido."},
        {"role": "user", "content": (
            'Retorne {\"title\": str, \"author\": str} a partir deste inicio de '
            "documento. Se nao houver autor claro, use \"\".\n\n--- TEXTO ---\n" + sample)},
    ]
    out, usage = chat(msg, model, max_tokens=200, temperature=0.0)
    tally.add(usage)
    try:
        return json.loads(strip_fences(out))
    except json.JSONDecodeError:
        return {"title": "", "author": ""}


# linha de topo de capitulo no indice: "<n> <Titulo> <pagina>"
TOC_TOP = re.compile(r"^[ \t]*(\d{1,2})[ \t]+([A-Z][A-Za-z0-9 ,:'\-/()&]+?)[ \t]+\d{1,4}[ \t]*$", re.M)


def parse_chapters(text):
    """Detecta capitulos de topo direto do indice (regex, sem custo de token)."""
    head = text[:250000]  # o indice fica no inicio
    seen = {}
    for m in TOC_TOP.finditer(head):
        n = int(m.group(1))
        title = re.sub(r"\s+", " ", m.group(2)).strip(" .")
        if n not in seen and 2 <= len(title) <= 80:
            seen[n] = title
    return [{"n": n, "title": t} for n, t in sorted(seen.items())]


# inicio do corpo de um capitulo: linha "Chapter N" (seguida do titulo)
CH_BODY = re.compile(r"(?m)^[ \t]*Chapter[ \t]+(\d{1,2})[ \t]*$")


def slice_chapters(text, chapters):
    """Fatia o corpo pelos marcadores 'Chapter N' (validados pelo titulo logo
    abaixo). Mais robusto que casar o titulo solto. Cai de volta para o casamento
    por titulo se nao houver marcadores 'Chapter N'."""
    title_by_n = {c["n"]: c["title"] for c in chapters}
    found = []
    for m in CH_BODY.finditer(text):
        n = int(m.group(1))
        after = text[m.end():m.end() + 200].lstrip("\n ")
        first_line = after.split("\n", 1)[0].strip()
        toc_title = title_by_n.get(n)
        if toc_title and re.search(re.escape(toc_title), after[:160], re.I):
            found.append((m.start(), n, toc_title))
        elif first_line and first_line[:1].isalpha() and 2 <= len(first_line) <= 80:
            found.append((m.start(), n, first_line))

    if not found:  # fallback: casamento por titulo isolado, em ordem
        return _slice_by_title(text, chapters)

    seen, uniq = set(), []
    for pos, n, title in sorted(found):
        if n not in seen:
            seen.add(n)
            uniq.append((pos, n, title))
    slices = []
    for i, (pos, n, title) in enumerate(uniq):
        end = uniq[i + 1][0] if i + 1 < len(uniq) else len(text)
        slices.append(({"n": n, "title": title}, text[pos:end]))
    return slices


def _slice_by_title(text, chapters):
    toc_matches = list(TOC_TOP.finditer(text[:250000]))
    body_start = toc_matches[-1].end() if toc_matches else 0
    positions, cursor = [], body_start
    for ch in chapters:
        pat = re.compile(r"(?m)^[ \t]*" + re.escape(ch["title"]) + r"[ \t]*$", re.I)
        m = pat.search(text, cursor)
        if m:
            positions.append((m.start(), ch))
            cursor = m.end()
    slices = []
    for i, (start, ch) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
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
    titulo = {"glossary": "Glossário", "patterns": "Padrões e construções",
              "cheatsheet": "Cheatsheet"}[kind]
    joined = "\n\n".join(chapters_md)[:60000]
    sys_p = "Voce consolida fichas de capitulo em um arquivo de apoio de skill. " + lang_clause(lang)
    user = (f"--- FICHAS DOS CAPITULOS (contexto) ---\n{joined}\n\n"
            f"--- TAREFA ---\nLivro: {meta.get('title')} ({meta.get('author')}).\n"
            f"Gere o conteudo do arquivo {fname}. Regras: {rule}\n"
            f"Comece com um titulo H1 '# {titulo} — {meta.get('title')}'. "
            "NAO continue/repita as fichas acima; produza um documento novo e consolidado.")
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
        "--- FICHAS DOS CAPITULOS (contexto para extrair os frameworks centrais) ---\n"
        + ("\n\n".join(chapters_md))[:40000]
        + "\n\n--- TABELA DE CAPITULOS (use exatamente) ---\n"
        + f"| # | Titulo |\n|---|--------|\n{index}\n\n"
        + f"--- TAREFA ---\nEscreva o arquivo SKILL.md completo para a skill '{name}'. "
        f"Livro: {meta.get('title')} por {meta.get('author')}.\n"
        "Comece a resposta DIRETAMENTE com '---' (frontmatter YAML). NAO repita as fichas acima.\n"
        "Estrutura obrigatoria:\n"
        "1) Frontmatter YAML (name e description; description comeca com 'Use ao/quando' e "
        "lista os topicos centrais, sem resumir o passo a passo).\n"
        "2) '# Titulo' + linha de metadados.\n3) '## Como usar esta skill'.\n"
        "4) '## Frameworks centrais' (os mais importantes, formulacao exata, ~1500 tokens).\n"
        "5) '## Indice de capitulos' (a tabela acima, com links chapters/chNN-...md).\n"
        "6) '## Indice de topicos' (termo -> chNN, alfabetico).\n"
        "7) '## Arquivos de apoio' (glossary.md, patterns.md, cheatsheet.md).\n"
        "8) '## Escopo e limites'.")
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
        text = f.read().replace("\f", "\n")  # form-feed vira quebra de linha (cabecalhos de pagina)
    print(f"Texto: {len(text):,} chars (~{len(text)//4:,} tokens) | modelo: {args.model}")

    tally = Tally(args.model)
    print("1/4 detectando estrutura...")
    meta = detect_meta(text, args.model, tally)
    chapters = parse_chapters(text)
    print(f"    {meta.get('title')} - {len(chapters)} capitulos detectados no indice")

    slices = slice_chapters(text, chapters)
    if not slices:
        sys.exit("ERRO: nenhum capitulo localizado no corpo do texto.")
    if len(slices) < len(chapters):
        print(f"    aviso: {len(slices)}/{len(chapters)} capitulos localizados no corpo "
              "(os demais foram absorvidos no capitulo anterior).")
    print(f"    {tally.line()}")

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
