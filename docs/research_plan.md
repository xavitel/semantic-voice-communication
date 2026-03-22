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
- Annotated bibliography
- Comparison table of methods
- Benchmark protocol v1 (datasets, splits, metrics, network conditions)

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
