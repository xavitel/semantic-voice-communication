# Implementation Candidates and Integration Notes

This document turns the recent state-of-the-art update into an actionable implementation shortlist for the repository.

## Objective

Identify components that are both:

1. technically aligned with semantic voice communication, and
2. realistic to integrate in a reproducible prototype during the next implementation phase.

The goal is not to commit to a single stack yet, but to reduce ambiguity and create a practical shortlist for benchmarking.

---

## 1. Recommended Implementation Tracks

### Track A — Modular semantic pipeline (baseline, high control)

**Purpose:** validate the core hypothesis that content, identity, and prosody can be transmitted separately and reconstructed with acceptable quality.

**Suggested stack:**
- **ASR / linguistic content:** Whisper or WhisperX
- **Speaker identity:** ECAPA-TDNN
- **Prosody:** explicit F0 / energy / duration features, optionally style embeddings
- **Decoder / TTS:** StyleTTS2 as primary open baseline

**Why this track matters:**
- maximizes interpretability
- makes ablations easy
- allows separate evaluation of content, identity, and prosody
- is ideal for early experiments and paper-quality figures

**Main limitation:** likely too much cumulative latency for strict real-time conversation.

---

### Track B — Streaming tokenized pipeline (target for real-time)

**Purpose:** approach the <300 ms end-to-end requirement with a codec/tokenizer-based architecture.

**Suggested stack:**
- **Primary codec baseline:** Mimi / Moshi stack
- **Alternative candidates for comparison:** DualCodec, XY-Tokenizer, JHCodec
- **Optional ultra-low-bitrate offline reference:** SemantiCodec, TaDiCodec

**Why this track matters:**
- closer to real deployment conditions
- naturally captures more paralinguistic detail than pure text pipelines
- provides a better foundation for packet-loss experiments and adaptive transmission

**Main limitation:** less explicit attribute control and more tooling complexity.

---

## 2. Priority Open Implementations

### 2.1 Whisper / WhisperX

**Role:** content extraction and semantic fidelity evaluation.

**Recommended use:**
- Whisper as robust baseline ASR
- WhisperX when timestamp alignment becomes useful for prosody reconstruction or fine-grained analysis

**Why it is useful here:**
- extremely practical baseline
- mature ecosystem
- easy to automate for WER-based semantic evaluation

---

### 2.2 SpeechBrain ECAPA-TDNN

**Role:** speaker identity encoding and similarity measurement.

**Recommended use:**
- generate speaker embeddings on original and reconstructed speech
- compute cosine similarity as a core identity-preservation metric

**Why it is useful here:**
- already standard in speaker verification work
- lightweight enough for reproducible evaluation harnesses

---

### 2.3 StyleTTS2

**Role:** controllable generative decoder for the modular baseline.

**Recommended use:**
- baseline TTS conditioned on text plus speaker/prosody signals
- first reference system for subjective and objective quality studies

**Why it is useful here:**
- strong open baseline
- better fit than opaque hosted systems when reproducibility matters

---

### 2.4 Mimi / Moshi

**Role:** streaming semantic-acoustic tokenization and real-time codec baseline.

**Recommended use:**
- first end-to-end token baseline
- bitrate / latency / quality reference for all later tokenizer comparisons

**Why it is useful here:**
- strongest practical bridge between research novelty and real-time viability
- directly aligned with the repository's low-latency direction

---

### 2.5 DualCodec / XY-Tokenizer / JHCodec

**Role:** second-wave tokenizer candidates for formal comparison.

**Recommended use:**
- benchmark against Mimi on:
  - bitrate
  - ASR-WER on reconstructed audio
  - speaker similarity
  - perceived quality
  - runtime / latency

**Why they matter:**
- they explicitly target the semantic-vs-acoustic trade-off that is central to this project
- they can reveal whether Mimi is enough or whether a more disentangled tokenizer is needed

---

## 3. Packet-Loss and Robustness Candidates

### 3.1 Glaris

**Role:** reference architecture for semantic voice transmission under packet loss.

**Potential use in this repo:**
- inspire packet-loss-aware evaluation
- compare concealment / recovery strategies for token streams

### 3.2 LargeSC

**Role:** reference for adaptive bitrate, UEP, and generative recovery.

**Potential use in this repo:**
- design experiment variants with semantic/acoustic stream prioritization
- study whether unequal protection helps preserve intelligibility under loss

**Practical implication:**
packet-loss robustness should become a required experiment, not an optional appendix.

---

## 4. Proposed Benchmark Shortlist

The first reproducible implementation cycle should benchmark these candidates:

### Modular baseline
1. Whisper + ECAPA-TDNN + StyleTTS2

### Streaming/token baselines
2. Mimi
3. DualCodec
4. XY-Tokenizer
5. JHCodec

### Offline ultra-low-bitrate references
6. SemantiCodec
7. TaDiCodec

---

## 5. Recommended Evaluation Axes

Every candidate should be compared under the same protocol:

- **Bitrate**
- **Latency**
- **ASR-WER on reconstructed speech**
- **Speaker similarity (SIM)**
- **Quality proxy:** MOS predictor / UTMOS / DNSMOS where feasible
- **Robustness under packet loss and jitter**
- **Compute cost / real-time factor**

---

## 6. Immediate Engineering Recommendation

### Step 1
Implement **Track A** first to validate the decomposition:

`audio -> Whisper -> semantic content + ECAPA identity + explicit prosody -> StyleTTS2 -> reconstructed speech`

### Step 2
Implement **Mimi** as the first streaming baseline.

### Step 3
Create a tokenizer benchmark harness so that DualCodec, XY-Tokenizer, and JHCodec can be plugged into the same evaluation loop.

### Step 4
Add packet-loss emulation and recovery experiments inspired by Glaris and LargeSC.

---

## 7. Decision Rule for the Project

A tokenizer / architecture should be prioritized if it satisfies most of the following:

- materially lower bitrate than conventional VoIP
- acceptable intelligibility after reconstruction
- acceptable speaker preservation
- realistic path toward <300 ms latency
- reproducible open implementation or sufficiently inspectable code
- robustness potential under packet loss

If no single candidate dominates across all dimensions, the repository should explicitly keep two parallel baselines:

- a **modular semantic baseline** for interpretability and publication clarity
- a **streaming token baseline** for real-time feasibility

---

## 8. Suggested Next Files to Add Later

- `experiments/benchmark_protocol_v1.md`
- `experiments/tokenizer_benchmark/`
- `experiments/modular_baseline/`
- `experiments/network_robustness/`

These should become the bridge between documentation and executable experiments.
