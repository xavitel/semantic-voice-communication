"""Generate literature-review assets from papers/literature_catalog.json."""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "papers" / "literature_catalog.json"
MATRIX = ROOT / "papers" / "paper_matrix.csv"
INDEX = ROOT / "papers" / "paper_index.md"
NOTES = ROOT / "papers" / "notes"
BIB = ROOT / "references.bib"


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")[:64]


def github_anchor(identifier: str, title: str) -> str:
    value = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9 -]", "", value)
    value = re.sub(r"[ -]+", "-", value).strip("-")
    return f"{identifier}-{value}"


def bib_escape(value: str) -> str:
    return value.replace("&", r"\&")


papers = json.loads(CATALOG.read_text(encoding="utf-8"))
papers.sort(key=lambda item: int(item["id"]))
NOTES.mkdir(parents=True, exist_ok=True)

matrix_fields = [
    "id", "file", "year", "title", "authors", "category", "priority",
    "representation", "bitrate", "latency", "evaluation", "channel",
    "code", "main_evidence", "limitations", "tfm_relevance",
]
with MATRIX.open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=matrix_fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(papers)

index_lines = [
    "# Índice comentado del corpus",
    "",
    "> Catálogo de los 29 documentos del repositorio. Los resúmenes están redactados en español a partir del abstract y, cuando ha sido necesario, de las conclusiones del PDF. No son traducciones literales.",
    "",
    "## Navegación por tema",
    "",
]
categories: dict[str, list[dict]] = {}
for paper in papers:
    categories.setdefault(paper["category"], []).append(paper)
for category, items in categories.items():
    links = ", ".join(f"[{item['id']}](#{github_anchor(item['id'], item['title'])})" for item in items)
    index_lines.append(f"- **{category}:** {links}")
index_lines.extend(["", "## Fichas resumidas", ""])

readme_lines = ["# Fichas de lectura", "", "Fichas individuales generadas desde `papers/literature_catalog.json`.", ""]
bib_entries = []

for paper in papers:
    note_name = f"{paper['id']}_{slug(paper['title'])}.md"
    note_rel = f"notes/{note_name}"
    pdf_rel = paper["file"].replace("\\", "/")
    index_lines.extend([
        f"### {paper['id']}. {paper['title']}",
        "",
        f"- **Autores:** {paper['authors']}",
        f"- **Año:** {paper['year']}",
        f"- **Categoría:** {paper['category']}",
        f"- **Prioridad:** {paper['priority']}",
        f"- **Fuente:** [`{Path(pdf_rel).name}`]({Path(pdf_rel).name})",
        f"- **Ficha completa:** [`{note_name}`]({note_rel})",
        "",
        f"**Resumen en español.** {paper['spanish_abstract']}",
        "",
        f"**Aportación al TFM.** {paper['tfm_relevance']}",
        "",
    ])

    note = "\n".join([
        f"# {paper['title']}",
        "",
        f"- **ID:** {paper['id']}",
        f"- **Autores:** {paper['authors']}",
        f"- **Año:** {paper['year']}",
        f"- **Categoría:** {paper['category']}",
        f"- **Prioridad:** {paper['priority']}",
        f"- **PDF:** [`{Path(pdf_rel).name}`](../{Path(pdf_rel).name})",
        f"- **Clave BibTeX:** `{paper['citation_key']}`",
        "",
        "## Resumen en español",
        "",
        paper["spanish_abstract"],
        "",
        "## Evidencia extraída",
        "",
        f"- **Representación:** {paper['representation']}",
        f"- **Bitrate:** {paper['bitrate']}",
        f"- **Latencia:** {paper['latency']}",
        f"- **Evaluación:** {paper['evaluation']}",
        f"- **Canal/robustez:** {paper['channel']}",
        f"- **Código o artefactos:** {paper['code']}",
        f"- **Resultado principal:** {paper['main_evidence']}",
        "",
        "## Limitaciones",
        "",
        paper["limitations"],
        "",
        "## Uso en el TFM",
        "",
        paper["tfm_relevance"],
        "",
        "## Estado de revisión",
        "",
        "Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.",
        "",
    ])
    (NOTES / note_name).write_text(note, encoding="utf-8")
    readme_lines.append(f"- [{paper['id']}. {paper['title']}]({note_name})")

    entry_type = paper.get("entry_type", "article")
    fields = [
        f"  title = {{{bib_escape(paper['title'])}}}",
        f"  author = {{{bib_escape(paper['bib_authors'])}}}",
        f"  year = {{{paper['year']}}}",
    ]
    if paper.get("arxiv"):
        fields.extend([
            f"  eprint = {{{paper['arxiv']}}}",
            "  archivePrefix = {arXiv}",
        ])
    if paper.get("url"):
        fields.append(f"  url = {{{paper['url']}}}")
    fields.append(f"  note = {{Local corpus file: {Path(pdf_rel).name}}}")
    bib_entries.append(f"@{entry_type}{{{paper['citation_key']},\n" + ",\n".join(fields) + "\n}")

INDEX.write_text("\n".join(index_lines), encoding="utf-8")
(NOTES / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
BIB.write_text("\n\n".join(bib_entries) + "\n", encoding="utf-8")

print(f"Generated {len(papers)} records")
print(MATRIX)
print(INDEX)
print(NOTES)
print(BIB)
