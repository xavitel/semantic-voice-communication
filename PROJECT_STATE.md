# PROJECT_STATE.md

## Semantic Voice Communication Research

### 1. Project Goal

This project investigates a semantic communication architecture for voice transmission.

The objective is to move from traditional signal transmission:

voice → waveform → transmission → waveform → voice

to a semantic pipeline:

voice → meaning + speaker identity + prosody → transmission → generative reconstruction → voice

The key hypothesis is that transmitting semantic representations instead of raw audio can reduce bandwidth significantly while preserving intelligibility, identity and expressive speech characteristics.

Estimated potential bandwidth reduction compared to VoIP: 5x–10x.

───

### 2. Repository Structure

semantic-voice-research/

README.md
High-level description of the project.

architecture/
System architecture definitions.

architecture/system_architecture.md
Initial architecture draft of the semantic voice transmission pipeline.

docs/

docs/research_plan.md
Research roadmap including phases of investigation and experimental design.

docs/bitrate_analysis.md
Preliminary comparison between VoIP bitrates and semantic transmission estimates.

papers/

papers/important_papers_list.md
Initial list of relevant research papers across several fields.

papers/paper_index.md
Annotated index with a Spanish abstract for every paper in the corpus.

papers/paper_matrix.csv
Normalized evidence matrix for comparative analysis.

papers/notes/
Individual structured reading notes generated from the literature catalog.

references.bib
BibTeX bibliography for the complete local corpus.

experiments/
Reserved for experimental implementations.

notes/
Reserved for working research notes.

───

### 3. Core Research Question

Can speech communication be implemented by transmitting semantic representations instead of raw audio signals, while preserving:

• speaker identity
• prosody and emotion
• natural sounding speech

───

### 4. Proposed Architecture (Current Version)

**Encoder Side:**

1. Audio Capture
Microphone waveform input.

2. Speech Recognition (STT)
Convert speech to text. Optionally outputs text + timestamps.

Candidate models:
• Whisper / WhisperX
• wav2vec2

3. Semantic Encoder
Convert text into semantic representation.

Possible approaches:
• sentence-transformers
• LLM embeddings
• semantic tokenization

4. Speaker Encoder
Extract speaker identity embedding.

Candidate models:
• ECAPA‑TDNN
• Resemblyzer
• x-vectors

5. Prosody / Emotion Encoder
Extract expressive speech features such as:
• pitch contour
• energy contour
• rhythm
• speaking rate
• emotional tone

Possible sources:
• prosody encoders used in StyleTTS2
• Speech Emotion Recognition networks

**6. Transmission Layer**
Only transmit:
• semantic representation
• speaker embedding
• prosody embedding

**Decoder Side:**

7. Semantic Reconstruction
Rebuild the textual / semantic representation.

8. Generative TTS
Conditioned on previous signals:
• text / semantic content
• speaker embedding
• prosody embedding

Candidate models:
• VALL‑E
• XTTS
• StyleTTS2
• Bark

9. Audio Output
Generate waveform audio.

───

### 5. Estimated Bitrate Advantage

Typical VoIP codecs:

G.711 → 64 kbps
Opus → typically 16–32 kbps

Preliminary semantic pipeline estimate:

~3–5 kbps equivalent

Potential reduction:

≈ 5x – 8x bandwidth reduction

Further reduction possible with:
• embedding quantization
• predictive encoding
• shared speaker identity models

───

### 6. Research Fields Involved

This project sits at the intersection of several research domains:

Semantic Communications
Neural Audio Codecs
Speech Representation Learning
Voice Cloning / Neural TTS
Speech Emotion Modeling

Literature assets:

- papers/paper_index.md
- papers/paper_matrix.csv
- papers/notes/
- references.bib
- docs/state_of_the_art.md
- docs/benchmark_protocol_v1.md

───

### 7. Planned Research Phases

Phase 1
Literature review and research landscape mapping.

Phase 2
Detailed system architecture design.

Phase 3
Prototype implementation.

Phase 4
Experimental evaluation.

Metrics:
• bitrate efficiency
• perceived speech quality (MOS)
• semantic fidelity
• latency (Target: < 300ms for real-time conversation)
• computational load / power consumption

───

### 8. Planned Experiments

Experiment 1
Baseline VoIP bandwidth measurement.

Experiment 2
Speech‑to‑text → text‑to‑speech reconstruction pipeline.

Experiment 3
Semantic transmission prototype.

Experiment 4
Speaker identity preservation evaluation.

Experiment 5
Prosody and emotional speech reconstruction.

───

### 9. Minimum Prototype Architecture

**Hardware Target:** Server with Nvidia A10G.
**Latency Constraints:** Strict < 300ms end-to-end to enable real-time bidirectional communication.

**Prototyping Strategy:**

**Phase 1: Baseline Semantic Pipeline (High Latency)**
To validate semantic reconstruction quality:
**STT:** Whisper
**Speaker embedding:** ECAPA‑TDNN
**Prosody features:** pitch + energy extraction
**TTS reconstruction:** XTTS or StyleTTS2
*Pipeline:* audio → STT → semantic + speaker + prosody → transmit → TTS → reconstructed audio
*(Expected limitation: Will likely fail the <300ms latency target and lose paralinguistic nuance).*

**Phase 2: End-to-End Neural/Semantic Audio Codecs (Ultra-Low Latency)**
To achieve the <300ms requirement while preserving emotion:
**Encoder/Decoder:** Discrete semantic token extractors (e.g., EnCodec, SoundStream, Mimi, or HuBERT-based quantizers).
*Pipeline:* audio → Neural Encoder (discrete tokens) → transmit → Neural Decoder → reconstructed audio

───

### 10. Immediate Next Tasks (Roadmap)

1. **Investigación (SoA Mapping):** Build a full research landscape document mapping the state of the art, with special focus on **Audio Language Models and Neural Codecs**.
2. **Arquitectura (`full_system_design.md`):** Design detailed architecture comparing the modular cascade (STT -> LLM/Embeddings -> TTS) vs. End-to-End Neural Codecs.
3. **PoC 1 (High Latency):** Implement the first prototype pipeline (Baseline on Nvidia A10G) using Whisper + StyleTTS2/XTTS to prove semantic transmission viability.
4. **PoC 2 (Low Latency):** Implement a discrete token pipeline (Encodec / Mimi) aiming for bandwidth optimization and <300ms latency.
5. Define detailed experiment protocols inside `experiments/`.

───

### 11. Environment

Project workspace location:
/home/javierAzure/.openclaw/workspace/semantic-voice-research

Repository:
https://github.com/xavitel/semantic-voice-communication

───

### 12. Project Status

Current stage: Early research and architecture design

Implemented:
✔️ repository structure
✔️ research plan
✔️ architecture draft
✔️ initial bitrate analysis
✔️ initial paper list

Next milestone:
Complete state‑of‑the‑art research mapping and begin prototype experiments.
───

### 13. 2026 Roadmap Update (Research Direction)

To align with 2025–2026 progress in semantic speech transmission, the project now adds three priorities:

1. **Tokenizer/Codec Selection Framework**
   - Evaluate candidates beyond Mimi/SemantiCodec, including DualCodec, XY-Tokenizer, and TaDiCodec.
   - Multi-objective decision criteria: bitrate, latency, ASR-WER, speaker similarity, MOS/UTMOS, compute cost.

2. **Network Robustness Workstream**
   - Add packet-loss and jitter scenarios as first-class evaluation conditions.
   - Include adaptive protection strategies (e.g., unequal error protection and generative packet-loss recovery).

3. **Benchmark Protocol v1**
   - Fix datasets, splits, channel conditions, and metrics to ensure reproducible and fair model comparisons.

**New planned experiment:**
Experiment 6 — Packet-loss robustness and adaptive semantic transmission.
