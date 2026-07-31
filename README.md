<p align="center">
  <h1 align="center">🎙️ Semantic Voice Communication</h1>
  <p align="center">
    <em>Transmitting meaning, not waveforms — A research project on semantic communication for real-time voice transmission</em>
  </p>
  <p align="center">
    <a href="#abstract">Abstract</a> •
    <a href="#motivation">Motivation</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#bitrate-analysis">Bitrate Analysis</a> •
    <a href="#research-phases">Research Phases</a> •
    <a href="#state-of-the-art">State of the Art</a> •
    <a href="#documentation">Documentation</a>
  </p>
  <p align="center">
    <a href="#resumen-español">📖 Versión en Español</a>
  </p>
</p>

---

## Abstract

Modern voice communication systems (VoIP) transmit a faithful digital replica of the speaker's audio waveform. While robust, this approach treats speech as a generic signal and ignores its rich semantic structure. **Semantic Voice Communication** is a research project that investigates a fundamentally different paradigm: instead of transmitting the waveform, we decompose speech into its core semantic components — *what* is said (linguistic content), *who* says it (speaker identity), and *how* it is said (prosody, emotion, rhythm) — transmit only these compact representations, and reconstruct natural-sounding speech at the receiver using state-of-the-art generative AI models.

This approach has the potential to achieve **5× to 200× bandwidth reduction** compared to conventional VoIP codecs (from 16–64 kbps down to 0.31–4 kbps), while preserving intelligibility, speaker identity, and expressive speech characteristics. The project sits at the intersection of semantic communications, neural audio codecs, speech representation learning, voice cloning, and speech emotion modeling — fields that have seen unprecedented convergence during 2024–2026.

> **Key Hypothesis:** Transmitting semantic representations instead of raw audio signals can reduce bandwidth by an order of magnitude while preserving the three pillars of natural speech: intelligibility, identity, and expressiveness.

---

# 🇬🇧 English

## Motivation

Traditional voice codecs (G.711, Opus, EVS) operate at Shannon's Level A of communication: they maximize bit-level signal fidelity. A 64 kbps G.711 stream or a 16–32 kbps Opus stream faithfully reproduces the acoustic waveform, but carries far more information than is semantically necessary for human understanding.

Semantic communication, originally proposed by Weaver and Shannon (1949), operates at Level B: transmitting only the information necessary to reconstruct the *meaning* of the message. For voice, this means separating and independently compressing:

| Component | What it captures | Example representation |
|---|---|---|
| **Linguistic content** | The words spoken (lexical-syntactic) | Text tokens, semantic embeddings |
| **Speaker identity** | Unique timbral characteristics (static paralinguistic) | ECAPA-TDNN embedding (~192 floats) |
| **Prosody & emotion** | Intonation, rhythm, emphasis, emotional state (dynamic paralinguistic) | Pitch/energy contours, style embeddings |

By transmitting only these compact representations and leveraging generative TTS models at the receiver to reconstruct the full audio signal, we can achieve dramatic bandwidth savings — transforming voice communication from a signal processing problem into an AI generation problem.

## Architecture

The project investigates two complementary architectural approaches:

### Approach 1: Modular Cascade Pipeline (High Control, Higher Latency)

```
┌─────────────────────── ENCODER SIDE ───────────────────────┐
│                                                             │
│   🎤 Audio Capture                                         │
│       │                                                     │
│       ├──→ Speech-to-Text (Whisper / WhisperX)             │
│       │       │                                             │
│       │       └──→ Semantic Encoder                        │
│       │              (sentence-transformers / LLM embed.)  │
│       │                                                     │
│       ├──→ Speaker Encoder (ECAPA-TDNN / x-vectors)        │
│       │                                                     │
│       └──→ Prosody Encoder (pitch, energy, rhythm, emotion)│
│                                                             │
└─────────────────────────────────────────────────────────────┘
                          │
              ╔═══════════╧═══════════╗
              ║   TRANSMISSION LAYER   ║
              ║  • semantic tokens     ║
              ║  • speaker embedding   ║
              ║  • prosody embedding   ║
              ║  ≈ 3–5 kbps           ║
              ╚═══════════╤═══════════╝
                          │
┌─────────────────────── DECODER SIDE ───────────────────────┐
│                                                             │
│   Semantic Reconstruction                                   │
│       │                                                     │
│       └──→ Generative TTS (VALL-E / XTTS / StyleTTS2)     │
│               conditioned on:                               │
│               • text / semantic content                     │
│               • speaker embedding                           │
│               • prosody embedding                           │
│       │                                                     │
│       └──→ 🔊 Reconstructed Audio Output                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Advantages:** Explicit control over each component; independent development, evaluation, and improvement of each module; maximum bitrate reduction (only text + compact metadata transmitted).

**Limitations:** Cumulative latency across modules; information loss at module interfaces; difficulty preserving prosodic and emotional nuances through the entire cascade.

### Approach 2: End-to-End Neural Codec with Semantic Tokens (Low Latency)

```
🎤 Audio → Neural Codec Encoder (Mimi / SemantiCodec)
              → [Transmit: discrete semantic + acoustic tokens]
              → Neural Codec Decoder → 🔊 Reconstructed Audio
```

**Advantages:** Implicit preservation of identity and prosody in tokens; potentially very low latency (Mimi achieves 80 ms at 1.1 kbps); end-to-end training directly optimizes reconstruction quality.

**Limitations:** Less explicit control over individual attributes; higher bitrate than Approach 1; requires GPU for encoding and decoding.

### Recommended Strategy

A **two-phase** research approach:

1. **Phase 1 (Baseline):** Implement Approach 1 with Whisper + ECAPA-TDNN + StyleTTS2/XTTS to validate semantic reconstruction viability and establish quality baselines (MOS, semantic fidelity, speaker similarity).
2. **Phase 2 (Target):** Migrate to Approach 2, adopting a dual semantic+acoustic encoder architecture (inspired by SemantiCodec) with streaming optimizations from JHCodec (zero-lookahead) and Mimi (80 ms latency), incorporating emotion distillation techniques from StreamVoiceAnon+.

## Bitrate Analysis

A core motivation of this project is the dramatic bandwidth reduction achievable through semantic transmission:

### Conventional VoIP Codecs

| Codec | Bitrate | Latency |
|---|---|---|
| G.711 | 64 kbps | ~1 ms |
| Opus | 6–510 kbps (typical: 16–32 kbps) | 2.5–60 ms |
| EVS | 5.9–128 kbps | ~32 ms |

### Semantic Pipeline Estimates

| Approach | Estimated Bitrate | Reduction vs Opus (24 kbps) |
|---|---|---|
| Modular cascade (text + embeddings) | ~3–5 kbps | **5–8×** |
| Neural codec (Mimi) | 1.1 kbps | **~22×** |
| Semantic codec (SemantiCodec) | 0.31–1.40 kbps | **17–77×** |

**Breakdown of the modular approach per sentence (~5 seconds of speech):**
- Text tokens: ~200 bytes
- Speaker embedding (256–512 floats): ~2 KB
- Prosody embedding (~100 floats): ~400 bytes
- **Total: ~2.6 KB per sentence → ≈ 4 kbps equivalent**

Further optimization is possible through embedding quantization, predictive encoding, and shared speaker identity models.

## Research Phases

The project follows a structured four-phase research plan:

### Phase 1 — Literature Review & Landscape Mapping
- Map the state of the art across all relevant fields
- Build annotated bibliography and comparison tables
- Identify candidate models for each pipeline component
- **Status: ✅ Completed**

### Phase 2 — Architecture Design
- Define the modular pipeline and data representations
- Design the end-to-end neural codec alternative
- Specify model choices and interface contracts
- Compare cascade vs. end-to-end trade-offs
- **Status: ✅ Completed (initial draft)**

### Phase 3 — Prototype Implementation
- **Experiment 1:** Baseline VoIP bandwidth measurement
- **Experiment 2:** Speech-to-text → text-to-speech reconstruction pipeline
- **Experiment 3:** Full semantic transmission prototype
- **Experiment 4:** Speaker identity preservation evaluation
- **Experiment 5:** Prosody and emotional speech reconstruction
- **Hardware target:** Server with Nvidia A10G GPU
- **Status: 🔲 Planned**

### Phase 4 — Experimental Evaluation
Systematic evaluation against the following metrics:
- **Bitrate efficiency** — bandwidth consumed vs. VoIP baselines
- **Perceived speech quality** — Mean Opinion Score (MOS) via subjective listening tests
- **Semantic fidelity** — accuracy of reconstructed linguistic content
- **Latency** — end-to-end delay (target: < 300 ms for real-time conversation)
- **Computational load** — GPU/CPU requirements and power consumption
- **Status: 🔲 Planned**

## State of the Art

This project draws from and builds upon cutting-edge research across multiple domains. Below is a summary of the key technologies and models informing the design:

### Neural Audio Codecs
| Model | Origin | Key Innovation | Bitrate | Open Source |
|---|---|---|---|---|
| SoundStream | Google, 2021 | First neural codec to surpass classical codecs; structured RVQ dropout for variable bitrate | 3–18 kbps | No |
| EnCodec | Meta, 2022 | Multi-scale discriminator; loss balancer; foundation for AudioCraft ecosystem | 1.5–24 kbps | ✅ |
| SNAC | 2024 | Multi-scale temporal RVQ — different quantizers at different frame rates | Variable | ✅ |
| Mimi | Kyutai, 2024 | Joint semantic+acoustic modeling via SSL distillation; **1.1 kbps at 80 ms latency** | 1.1 kbps | ✅ |
| SemantiCodec | 2024 | Dual semantic (AudioMAE) + acoustic encoder with diffusion decoder; **0.31 kbps** | 0.31–1.40 kbps | ✅ |
| JHCodec | 2026 | Zero-lookahead streaming via SSRR loss; single-GPU training | Competitive | ✅ |
| LDCodec | 2025 | Low-complexity decoder for mobile deployment | 6 kbps | No |

### Audio Language Models & Voice Generation
| Model | Key Capability |
|---|---|
| AudioLM (Google, 2022) | Established the hybrid semantic+acoustic tokenization paradigm |
| VALL-E (Microsoft, 2023) | TTS as language modeling; zero-shot voice cloning from 3s of audio |
| VoiceCraft-X (2025) | Unified multilingual (11 languages) zero-shot TTS and speech editing |
| SpeechEdit (2026) | Selective attribute control — independently modify timbre, prosody, emotion |
| Moshi (Kyutai, 2024) | First full-duplex real-time spoken dialogue model; 200 ms latency |

### Critical Finding: The Emotion Loss Problem
Research from StreamVoiceAnon+ (2026) has revealed that discrete content tokens from neural codecs **actively discard emotional information**, and codec language models tend to generate dominant (neutral) acoustic patterns. This finding directly impacts our system design: explicit mechanisms for emotion preservation or transmission are required, such as frame-level acoustic distillation.

### Research Fields Involved
This project sits at the intersection of:
- 🔬 **Semantic Communications** — Transmitting meaning instead of signals
- 🧠 **Neural Audio Codecs** — AI-based audio compression and tokenization
- 🗣️ **Speech Representation Learning** — Self-supervised speech models (wav2vec, HuBERT)
- 🎭 **Voice Cloning / Neural TTS** — Generative speech synthesis conditioned on identity
- 💬 **Speech Emotion Modeling** — Preserving paralinguistic expressiveness

## Documentation

| File / Directory | Description |
|---|---|
| [`PROJECT_STATE.md`](PROJECT_STATE.md) | Central project documentation — architecture, roadmap, and experimental design |
| [`architecture/`](architecture/) | System architecture definitions and pipeline diagrams |
| [`architecture/system_architecture.md`](architecture/system_architecture.md) | Initial architecture draft of the semantic voice transmission pipeline |
| [`docs/`](docs/) | Conceptual documents and detailed research plans |
| [`docs/research_plan.md`](docs/research_plan.md) | Research roadmap with phases and experimental design |
| [`docs/bitrate_analysis.md`](docs/bitrate_analysis.md) | Comparison between VoIP bitrates and semantic transmission estimates |
| [`docs/state_of_the_art.md`](docs/state_of_the_art.md) | Citation-backed draft of the state of the art |
| [`docs/benchmark_protocol_v1.md`](docs/benchmark_protocol_v1.md) | Reproducible evaluation protocol for codecs and semantic pipelines |
| [`papers/`](papers/) | Collected research papers and reference materials |
| [`papers/paper_index.md`](papers/paper_index.md) | Annotated index with a Spanish abstract for every paper |
| [`papers/paper_matrix.csv`](papers/paper_matrix.csv) | Evidence matrix for the 29-paper corpus |
| [`papers/notes/`](papers/notes/) | Individual structured reading notes |
| [`references.bib`](references.bib) | BibTeX bibliography for the corpus |
| [`papers/important_papers_list.md`](papers/important_papers_list.md) | Curated list of key papers across all relevant research fields |

## Current Status

📍 **Stage:** Early research and architecture design

| Milestone | Status |
|---|---|
| Repository structure | ✅ Done |
| Research plan | ✅ Done |
| Architecture draft | ✅ Done |
| Bitrate analysis | ✅ Done |
| Paper collection | ✅ Done |
| Literature evidence matrix and notes | ✅ First complete draft |
| State of the art survey | 🟡 Citation-backed draft |
| Prototype implementation | 🔲 Next |
| Experimental evaluation | 🔲 Planned |

**Next milestone:** Begin prototype experiments with Whisper + ECAPA-TDNN + StyleTTS2/XTTS on Nvidia A10G hardware.

## Repository

🔗 [github.com/xavitel/semantic-voice-communication](https://github.com/xavitel/semantic-voice-communication)

---
---

<a name="resumen-español"></a>

<p align="center">
  <h1 align="center">🎙️ Comunicación Semántica de Voz</h1>
  <p align="center">
    <em>Transmitir significado, no formas de onda — Un proyecto de investigación sobre comunicación semántica para transmisión de voz en tiempo real</em>
  </p>
  <p align="center">
    <a href="#abstract">Abstract</a> •
    <a href="#motivación">Motivación</a> •
    <a href="#arquitectura">Arquitectura</a> •
    <a href="#análisis-de-bitrate">Análisis de Bitrate</a> •
    <a href="#fases-de-investigación">Fases de Investigación</a> •
    <a href="#estado-del-arte">Estado del Arte</a> •
    <a href="#documentación">Documentación</a>
  </p>
  <p align="center">
    <a href="#abstract">🇬🇧 English Version (above)</a>
  </p>
</p>

---

## Resumen

Los sistemas modernos de comunicación de voz (VoIP) transmiten una réplica digital fiel de la forma de onda de audio del hablante. Aunque robusto, este enfoque trata la voz como una señal genérica e ignora su rica estructura semántica. **Semantic Voice Communication** es un proyecto de investigación que investiga un paradigma fundamentalmente diferente: en lugar de transmitir la forma de onda, descomponemos el habla en sus componentes semánticos esenciales — *qué* se dice (contenido lingüístico), *quién* lo dice (identidad del hablante) y *cómo* se dice (prosodia, emoción, ritmo) — transmitimos únicamente estas representaciones compactas y reconstruimos habla de sonido natural en el receptor utilizando modelos generativos de IA de última generación.

Este enfoque tiene el potencial de lograr una **reducción de ancho de banda de 5× a 200×** en comparación con los codecs VoIP convencionales (de 16–64 kbps a 0,31–4 kbps), preservando la inteligibilidad, la identidad del hablante y las características expresivas del habla. El proyecto se sitúa en la intersección de las comunicaciones semánticas, los códecs neuronales de audio, el aprendizaje de representaciones del habla, la clonación de voz y el modelado de emociones del habla — campos que han experimentado una convergencia sin precedentes durante 2024–2026.

> **Hipótesis Central:** Transmitir representaciones semánticas en lugar de señales de audio sin procesar puede reducir el ancho de banda en un orden de magnitud, preservando los tres pilares del habla natural: inteligibilidad, identidad y expresividad.

---

## Motivación

Los códecs de voz tradicionales (G.711, Opus, EVS) operan en el Nivel A de comunicación de Shannon: maximizan la fidelidad de la señal a nivel de bit. Un flujo G.711 de 64 kbps o uno de Opus de 16–32 kbps reproduce fielmente la forma de onda acústica, pero transporta mucha más información de la semánticamente necesaria para la comprensión humana.

La comunicación semántica, propuesta originalmente por Weaver y Shannon (1949), opera en el Nivel B: transmitir únicamente la información necesaria para reconstruir el *significado* del mensaje. Para la voz, esto implica separar y comprimir independientemente:

| Componente | Qué captura | Representación ejemplo |
|---|---|---|
| **Contenido lingüístico** | Las palabras pronunciadas (léxico-sintáctico) | Tokens de texto, embeddings semánticos |
| **Identidad del hablante** | Características tímbricas únicas (paralingüístico estático) | Embedding ECAPA-TDNN (~192 floats) |
| **Prosodia y emoción** | Entonación, ritmo, énfasis, estado emocional (paralingüístico dinámico) | Contornos de pitch/energía, embeddings de estilo |

Al transmitir solo estas representaciones compactas y aprovechar modelos generativos de TTS en el receptor para reconstruir la señal de audio completa, podemos lograr un ahorro dramático de ancho de banda — transformando la comunicación de voz de un problema de procesamiento de señales a un problema de generación con IA.

## Arquitectura

El proyecto investiga dos enfoques arquitectónicos complementarios:

### Enfoque 1: Pipeline Cascada Modular (Alto Control, Mayor Latencia)

```
┌─────────────────── LADO DEL CODIFICADOR ───────────────────┐
│                                                             │
│   🎤 Captura de Audio                                      │
│       │                                                     │
│       ├──→ Voz a Texto (Whisper / WhisperX)                │
│       │       │                                             │
│       │       └──→ Codificador Semántico                   │
│       │              (sentence-transformers / LLM embed.)  │
│       │                                                     │
│       ├──→ Codificador de Hablante (ECAPA-TDNN / x-vectors)│
│       │                                                     │
│       └──→ Codificador de Prosodia (tono, energía, ritmo)  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                          │
              ╔═══════════╧═══════════╗
              ║   CAPA DE TRANSMISIÓN  ║
              ║  • tokens semánticos   ║
              ║  • embedding hablante  ║
              ║  • embedding prosodia  ║
              ║  ≈ 3–5 kbps           ║
              ╚═══════════╤═══════════╝
                          │
┌──────────────── LADO DEL DECODIFICADOR ────────────────────┐
│                                                             │
│   Reconstrucción Semántica                                  │
│       │                                                     │
│       └──→ TTS Generativo (VALL-E / XTTS / StyleTTS2)     │
│               condicionado por:                             │
│               • contenido semántico                         │
│               • embedding del hablante                      │
│               • embedding de prosodia                       │
│       │                                                     │
│       └──→ 🔊 Audio Reconstruido                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Ventajas:** Control explícito sobre cada componente; desarrollo, evaluación y mejora independiente de cada módulo; máxima reducción de bitrate.

**Limitaciones:** Latencia acumulada entre módulos; pérdida de información en las interfaces; dificultad para preservar matices prosódicos y emocionales a lo largo de toda la cascada.

### Enfoque 2: Codec Neural End-to-End con Tokens Semánticos (Baja Latencia)

```
🎤 Audio → Encoder de Codec Neural (Mimi / SemantiCodec)
              → [Transmitir: tokens discretos semánticos + acústicos]
              → Decoder de Codec Neural → 🔊 Audio Reconstruido
```

**Ventajas:** Preservación implícita de identidad y prosodia; latencia potencialmente muy baja (Mimi: 80 ms a 1,1 kbps); entrenamiento end-to-end que optimiza directamente la calidad de reconstrucción.

**Limitaciones:** Menor control explícito sobre atributos individuales; bitrate superior al Enfoque 1; requiere GPU para codificación y decodificación.

### Estrategia Recomendada

Un enfoque de investigación en **dos fases**:

1. **Fase 1 (Baseline):** Implementar el Enfoque 1 con Whisper + ECAPA-TDNN + StyleTTS2/XTTS para validar la viabilidad de la reconstrucción semántica y establecer métricas base (MOS, fidelidad semántica, similitud de hablante).
2. **Fase 2 (Objetivo):** Migrar al Enfoque 2 con una arquitectura de doble encoder semántico+acústico (inspirada en SemantiCodec), optimizaciones de streaming de JHCodec (zero-lookahead) y Mimi (80 ms de latencia), incorporando destilación de emoción de StreamVoiceAnon+.

## Análisis de Bitrate

Una motivación central de este proyecto es la dramática reducción de ancho de banda alcanzable mediante transmisión semántica:

### Codecs VoIP Convencionales

| Codec | Bitrate | Latencia |
|---|---|---|
| G.711 | 64 kbps | ~1 ms |
| Opus | 6–510 kbps (típico: 16–32 kbps) | 2,5–60 ms |
| EVS | 5,9–128 kbps | ~32 ms |

### Estimaciones del Pipeline Semántico

| Enfoque | Bitrate Estimado | Reducción vs Opus (24 kbps) |
|---|---|---|
| Cascada modular (texto + embeddings) | ~3–5 kbps | **5–8×** |
| Codec neural (Mimi) | 1,1 kbps | **~22×** |
| Codec semántico (SemantiCodec) | 0,31–1,40 kbps | **17–77×** |

**Desglose del enfoque modular por frase (~5 segundos de habla):**
- Tokens de texto: ~200 bytes
- Embedding del hablante (256–512 floats): ~2 KB
- Embedding de prosodia (~100 floats): ~400 bytes
- **Total: ~2,6 KB por frase → ≈ 4 kbps equivalente**

## Fases de Investigación

### Fase 1 — Revisión Bibliográfica y Mapeo del Estado del Arte
- Mapear el estado del arte en todos los campos relevantes
- Construir bibliografía anotada y tablas comparativas
- **Estado: ✅ Completada**

### Fase 2 — Diseño de Arquitectura
- Definir el pipeline modular y las representaciones de datos
- Diseñar la alternativa de codec neural end-to-end
- Comparar compromisos cascada vs. end-to-end
- **Estado: ✅ Completada (borrador inicial)**

### Fase 3 — Implementación de Prototipo
- **Experimento 1:** Medición de ancho de banda VoIP baseline
- **Experimento 2:** Pipeline de reconstrucción voz-a-texto → texto-a-voz
- **Experimento 3:** Prototipo completo de transmisión semántica
- **Experimento 4:** Evaluación de preservación de identidad del hablante
- **Experimento 5:** Reconstrucción de prosodia y habla emocional
- **Hardware objetivo:** Servidor con GPU Nvidia A10G
- **Estado: 🔲 Planificada**

### Fase 4 — Evaluación Experimental
Evaluación sistemática con las siguientes métricas:
- **Eficiencia de bitrate** — ancho de banda vs. baselines VoIP
- **Calidad percibida del habla** — Mean Opinion Score (MOS)
- **Fidelidad semántica** — precisión del contenido lingüístico reconstruido
- **Latencia** — retardo extremo a extremo (objetivo: < 300 ms)
- **Carga computacional** — requisitos de GPU/CPU y consumo energético
- **Estado: 🔲 Planificada**

## Estado del Arte

El proyecto se nutre de y construye sobre investigación de vanguardia en múltiples dominios:

### Códecs Neuronales de Audio
| Modelo | Origen | Innovación Clave | Bitrate | Open Source |
|---|---|---|---|---|
| SoundStream | Google, 2021 | Primer codec neural en superar a los clásicos; dropout estructurado en RVQ | 3–18 kbps | No |
| EnCodec | Meta, 2022 | Discriminador multi-escala; base del ecosistema AudioCraft | 1,5–24 kbps | ✅ |
| SNAC | 2024 | RVQ temporal multi-escala — cuantizadores a diferentes frame rates | Variable | ✅ |
| Mimi | Kyutai, 2024 | Modelado conjunto semántico+acústico; **1,1 kbps a 80 ms** | 1,1 kbps | ✅ |
| SemantiCodec | 2024 | Doble encoder semántico+acústico con decoder de difusión; **0,31 kbps** | 0,31–1,40 kbps | ✅ |
| JHCodec | 2026 | Streaming zero-lookahead mediante pérdida SSRR | Competitivo | ✅ |

### Modelos de Lenguaje de Audio y Generación de Voz
| Modelo | Capacidad Clave |
|---|---|
| AudioLM (Google, 2022) | Estableció el paradigma de tokenización híbrida semántica+acústica |
| VALL-E (Microsoft, 2023) | TTS como modelado de lenguaje; clonación zero-shot con 3s de audio |
| VoiceCraft-X (2025) | TTS zero-shot multilingüe unificado (11 idiomas) y edición de habla |
| SpeechEdit (2026) | Control selectivo de atributos — modificar timbre, prosodia, emoción independientemente |
| Moshi (Kyutai, 2024) | Primer modelo de diálogo hablado full-duplex en tiempo real; 200 ms de latencia |

### Hallazgo Crítico: El Problema de la Pérdida Emocional
La investigación de StreamVoiceAnon+ (2026) ha revelado que los tokens de contenido discretos de los codecs neuronales **descartan activamente la información emocional**. Esto impacta directamente el diseño del sistema: se requieren mecanismos explícitos de preservación emocional, como la destilación acústica a nivel de frame.

## Documentación

| Archivo / Directorio | Descripción |
|---|---|
| [`PROJECT_STATE.md`](PROJECT_STATE.md) | Documentación central — arquitectura, hoja de ruta y diseño experimental |
| [`architecture/`](architecture/) | Definiciones de arquitectura del sistema |
| [`docs/research_plan.md`](docs/research_plan.md) | Hoja de ruta de investigación con fases y diseño experimental |
| [`docs/bitrate_analysis.md`](docs/bitrate_analysis.md) | Comparación de bitrates VoIP vs. transmisión semántica |
| [`docs/state_of_the_art.md`](docs/state_of_the_art.md) | Borrador trazable del estado del arte con citas |
| [`docs/benchmark_protocol_v1.md`](docs/benchmark_protocol_v1.md) | Protocolo reproducible para comparar arquitecturas |
| [`papers/`](papers/) | Artículos de investigación y materiales de referencia |
| [`papers/paper_index.md`](papers/paper_index.md) | Índice comentado con resumen en español de cada paper |
| [`papers/paper_matrix.csv`](papers/paper_matrix.csv) | Matriz de evidencia de los 29 papers |
| [`papers/notes/`](papers/notes/) | Fichas de lectura individuales |
| [`references.bib`](references.bib) | Bibliografía BibTeX del corpus |

## Estado Actual

📍 **Fase:** Investigación inicial y diseño de arquitectura

| Hito | Estado |
|---|---|
| Estructura del repositorio | ✅ Hecho |
| Plan de investigación | ✅ Hecho |
| Borrador de arquitectura | ✅ Hecho |
| Análisis de bitrate | ✅ Hecho |
| Recopilación de artículos | ✅ Hecho |
| Matriz de evidencia y fichas | ✅ Primer borrador completo |
| Estado del arte | 🟡 Borrador trazable con citas |
| Implementación del prototipo | 🔲 Siguiente |
| Evaluación experimental | 🔲 Planificada |

**Siguiente hito:** Iniciar los experimentos de prototipo con Whisper + ECAPA-TDNN + StyleTTS2/XTTS en hardware Nvidia A10G.

## Repositorio

🔗 [github.com/xavitel/semantic-voice-communication](https://github.com/xavitel/semantic-voice-communication)

---

<p align="center">
  <sub>Built with 🧠 at the intersection of AI and telecommunications research</sub>
</p>
