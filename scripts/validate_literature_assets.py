"""Validate consistency of the generated literature-review assets."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "papers" / "literature_catalog.json").read_text(encoding="utf-8"))

assert len(catalog) == 29, f"Expected 29 papers, found {len(catalog)}"
ids = [paper["id"] for paper in catalog]
keys = [paper["citation_key"] for paper in catalog]
assert len(ids) == len(set(ids)), "Duplicate paper IDs"
assert len(keys) == len(set(keys)), "Duplicate citation keys"

missing_pdfs = [paper["file"] for paper in catalog if not (ROOT / paper["file"]).is_file()]
assert not missing_pdfs, f"Missing PDFs: {missing_pdfs}"

with (ROOT / "papers" / "paper_matrix.csv").open(encoding="utf-8-sig", newline="") as stream:
    matrix = list(csv.DictReader(stream))
assert len(matrix) == 29, f"Expected 29 matrix rows, found {len(matrix)}"

index = (ROOT / "papers" / "paper_index.md").read_text(encoding="utf-8")
assert len(re.findall(r"^### \d{2}\. ", index, flags=re.MULTILINE)) == 29
assert index.count("**Resumen en español.**") == 29

notes = sorted((ROOT / "papers" / "notes").glob("[0-9][0-9]_*.md"))
assert len(notes) == 29, f"Expected 29 notes, found {len(notes)}"


def assert_local_links(markdown_file: Path) -> None:
    text = markdown_file.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path = (markdown_file.parent / target).resolve()
        assert path.exists(), f"Broken link in {markdown_file}: {target}"


assert_local_links(ROOT / "papers" / "paper_index.md")
for note in notes:
    assert_local_links(note)

bib = (ROOT / "references.bib").read_text(encoding="utf-8")
bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib, flags=re.MULTILINE))
assert bib_keys == set(keys), "BibTeX keys differ from catalog"

state = (ROOT / "docs" / "state_of_the_art.md").read_text(encoding="utf-8")
state_keys = set(re.findall(r"@([A-Za-z0-9_:-]+)", state))
assert state_keys <= bib_keys, f"Unknown citations: {sorted(state_keys - bib_keys)}"
assert set(keys) <= state_keys, f"Corpus papers not cited: {sorted(set(keys) - state_keys)}"

moshi = ROOT / "papers" / "Moshi_a_speech-text_foundation_model_for_real-time_dialogue.pdf"
raw = moshi.read_bytes()
assert raw.startswith(b"%PDF-"), "Moshi file is not a PDF"
assert b"%%EOF" in raw[-4096:], "Moshi PDF lacks EOF marker"

print("Literature assets validated successfully")
print(f"Papers: {len(catalog)}")
print(f"Matrix rows: {len(matrix)}")
print(f"Notes: {len(notes)}")
print(f"BibTeX entries: {len(bib_keys)}")
print(f"State-of-the-art citations: {len(state_keys)}")
