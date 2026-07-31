# Research Plan

## Phase 1: Literature Review

Topics:
- Semantic communications
- Neural speech codecs
- Voice cloning
- Speech emotion modelling
- Error-resilient transmission (packet loss, jitter)

Key questions:
- How to represent semantic meaning efficiently?
- How to preserve identity and prosody?
- What bitrate reductions are possible?
- Which tokenizers/codecs optimize semantic fidelity vs latency?
- How robust is semantic transmission under lossy networks?

Deliverables:
- [x] Annotated bibliography: `papers/paper_index.md` and `papers/notes/`
- [x] Comparison table of methods: `papers/paper_matrix.csv`
- [x] BibTeX corpus: `references.bib`
- [x] State-of-the-art draft: `docs/state_of_the_art.md`
- [x] Benchmark protocol v1: `docs/benchmark_protocol_v1.md`

The deliverables are first complete drafts. Before submission, every numerical claim used in the thesis must be rechecked against the corresponding experimental table in the source PDF.

## Phase 2: Architecture Definition

Define:
- modular pipeline
- data representations
- model choices
- tokenizer/codec selection criteria (WER, SIM, MOS/UTMOS, latency, robustness)

## Phase 3: Experiments

Experiments to run:

Experiment 1
Baseline VoIP bitrate measurement.

Experiment 2
Speech-to-text + TTS reconstruction.

Experiment 3
Semantic compression pipeline.

Experiment 4
Speaker identity preservation.

Experiment 5
Prosody reconstruction.

Experiment 6
Packet-loss robustness + adaptive protection.

Suggested network scenarios for Experiment 6:
- Packet loss: 0%, 5%, 10%, 20%
- Jitter profiles: low / medium
- Optional UEP/PLC variants for semantic and acoustic streams

## Phase 4: Evaluation

Metrics:
- bitrate
- MOS/UTMOS score (perceived quality)
- semantic fidelity (ASR/WER on reconstructed speech)
- latency
- speaker similarity (SIM)
- robustness under packet loss (quality and intelligibility degradation)
- adaptive bitrate effectiveness (quality per kbps under varying channels)
