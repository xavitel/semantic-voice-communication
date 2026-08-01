# Recent Papers (2025–2026)

> This focused shortlist is complemented by the maintained [`paper_index.md`](paper_index.md), [`paper_matrix.csv`](paper_matrix.csv), and individual notes in [`notes/`](notes/).

This file complements `important_papers_list.md` with a focused selection of recent papers that are especially relevant for implementation decisions.

## Semantic Communication & Generative Approaches

- **"On Extracting Semantic Information for Generative Semantic Communication"** (2025)
  - Focus: extracting semantic representations optimized for generative reconstruction
  - Relevance: directly aligned with modular pipeline design

- **"Generative Semantic Communication for Multimodal Systems"** (2025)
  - Focus: extending semantic communication to multimodal domains
  - Relevance: future extension path (voice → avatar / video)

## Tokenizers and Codecs

- **DualCodec (2025)**
- **XY-Tokenizer (2025)**
- **TaDiCodec (2025)**
- **JHCodec (2026)**

**Key insight:** tokenizer choice is now one of the most critical architectural decisions.

## Robustness and Real-World Deployment

- **Glaris (2025)**
- **LargeSC (2025)**

**Key insight:** semantic communication systems must be evaluated under packet loss and jitter to be meaningful for VoIP replacement.

## Streaming and Real-Time Systems

- **Moshi + Mimi (2024–2026)**

**Key insight:** real-time speech-to-speech models are now feasible at ~200 ms latency, redefining the design space.

---

## Practical Recommendation

When adding new papers to the repository:

1. Prefer works with:
   - code or reproducible artifacts
   - clear evaluation protocols
   - realistic latency claims

2. Tag them informally as:
   - "baseline candidate"
   - "research reference"
   - "future work"

3. Keep this file short and actionable (not exhaustive).
