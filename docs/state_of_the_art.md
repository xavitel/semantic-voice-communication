# State of the Art: Semantic Voice Communication

> **Documento de referencia del proyecto.** Última actualización: Marzo 2026.
> Cubre los campos de Neural Audio Codecs, Audio Language Models, Voice Cloning, Preservación de Prosodia/Emoción y Comunicaciones Semánticas aplicadas a voz.

---

## 1. Introducción y Contexto

El objetivo de este proyecto es investigar si la comunicación por voz puede implementarse transmitiendo **representaciones semánticas** en lugar de señales de audio, preservando:
- Identidad del hablante (timbre)
- Prosodia y emoción
- Naturalidad del habla

La evolución reciente (2021–2026) ha sido explosiva. Los **códecs neuronales de audio** han demostrado que un modelo end-to-end puede comprimir voz a bitrates de 1–6 kbps superando a codecs clásicos (Opus, EVS) que operan a 12–64 kbps. Paralelamente, los **Audio Language Models** han demostrado que tokens discretos extraídos de estos códecs pueden usarse como vocabulario para un LLM, permitiendo generación de voz zero-shot con clonación de identidad.

---

## 2. Códecs Neuronales de Audio (Fundacionales)

Estos modelos son la piedra angular del campo. Comprimen audio en tokens discretos mediante un encoder, un Residual Vector Quantizer (RVQ) y un decoder, entrenados end-to-end.

### 2.1 SoundStream (Google, 2021)
- **Paper:** *"SoundStream: An End-to-End Neural Audio Codec"* — [arXiv:2107.03312](https://arxiv.org/abs/2107.03312)
- **Arquitectura:** Encoder/decoder convolucional + RVQ, entrenado con pérdidas adversariales y de reconstrucción.
- **Bitrate:** 3–18 kbps (variable con structured dropout sobre capas del cuantizador).
- **Resultados clave:** A 3 kbps supera a Opus a 12 kbps y se aproxima a EVS a 9.6 kbps. Funciona en tiempo real en CPU de smartphone.
- **Latencia:** Baja, soporta inferencia streaming.
- **Relevancia:** Primer codec neural que demostró superioridad sobre codecs clásicos en un rango amplio de bitrates. Definió la arquitectura canónica (Encoder-RVQ-Decoder) que siguen casi todos los trabajos posteriores.

### 2.2 EnCodec (Meta, 2022)
- **Paper:** *"High Fidelity Neural Audio Compression"* — [arXiv:2210.13438](https://arxiv.org/abs/2210.13438)
- **Arquitectura:** Encoder-decoder streaming con espacio latente cuantizado (RVQ). Discriminador multi-escala de espectrograma. Mecanismo de *loss balancer* para estabilizar entrenamiento.
- **Bitrate:** 1.5–24 kbps (mono 24 kHz) / 3–24 kbps (estéreo 48 kHz).
- **Resultados clave:** Superior a SoundStream en pruebas MUSHRA. Modelos Transformer ligeros pueden comprimir la representación un 40% adicional.
- **Código:** Open-source en [github.com/facebookresearch/encodec](https://github.com/facebookresearch/encodec).
- **Relevancia:** Estándar de facto para tokenización de audio en modelos generativos. Base de AudioCraft (Meta).

### 2.3 SNAC — Multi-Scale Neural Audio Codec (2024)
- **Paper:** *"SNAC: Multi-Scale Neural Audio Codec"* — [arXiv:2410.14411](https://arxiv.org/abs/2410.14411)
- **Innovación:** Extensión de RVQ donde cada cuantizador opera a **diferente resolución temporal**. Aplica una jerarquía de cuantizadores a frame rates variables, adaptándose a la estructura del audio a múltiples escalas temporales.
- **Resultado:** Compresión más eficiente que RVQ estándar (validado objetiva y subjetivamente).
- **Código:** Open-source en [github.com/hubertsiuzdak/snac](https://github.com/hubertsiuzdak/snac).
- **Relevancia:** Alternativa a EnCodec con mejor eficiencia de compresión por su cuantización multi-escala.

### 2.4 LDCodec — Low-Complexity Decoder (2025)
- **Paper:** *"LDCodec: A high quality neural audio codec with low-complexity decoder"* — [arXiv:2510.15364](https://arxiv.org/abs/2510.15364)
- **Innovación:** Diseñado para dispositivos móviles (smartphones). Introduce Long-term/Short-term RVQ (LSRVQ) + discriminadores de frecuencia subbanda/fullband + pérdidas perceptuales.
- **Bitrate:** LDCodec a 6 kbps supera a Opus a 12 kbps.
- **Relevancia:** Demuestra que se puede lograr alta calidad con un decoder de baja complejidad, clave para despliegue en edge/móvil.

### 2.5 Mimi Codec — dentro de Moshi (Kyutai, 2024)
- **Paper:** *"Moshi: a speech-text foundation model for real-time dialogue"* — [arXiv:2410.00037](https://arxiv.org/abs/2410.00037)
- **Arquitectura del Codec (Mimi):** Codec neural streaming que procesa audio a 24 kHz, comprimiéndolo a una representación a 12.5 Hz con un ancho de banda de **1.1 kbps**. Opera en modo fully streaming con latencia de **80 ms**.
- **Innovación clave:** A diferencia de SoundStream/EnCodec, Mimi **modela conjuntamente información semántica y acústica** mediante destilación. Esto lo hace especialmente apto para uso con LLMs.
- **Relevancia:** Es el codec más avanzado en cuanto a integración semántica+acústica a ultra-baja latencia. Referencia directa para nuestro proyecto.

---

## 3. Códecs Semánticos y Ultra-Bajo Bitrate

### 3.1 SemantiCodec (2024–2025)
- **Paper:** *"SemantiCodec: An Ultra Low Bitrate Semantic Audio Codec for General Sound"* — [arXiv:2405.00233](https://arxiv.org/abs/2405.00233)
- **Arquitectura dual:**
  - **Encoder semántico:** Audio Masked Autoencoder (AudioMAE) pre-entrenado, discretizado con k-means.
  - **Encoder acústico:** Captura detalles residuales no semánticos.
  - **Decoder:** Basado en **difusión**, reconstruye audio a partir de ambos streams.
- **Bitrate:** 0.31–1.40 kbps (25, 50 o 100 tokens/segundo).
- **Resultados:** Supera significativamente al codec Descript en calidad de reconstrucción. Contiene información semántica mucho más rica que otros codecs, incluso a bitrates mucho menores.
- **Relevancia:** ⭐ **Paper clave para nuestro proyecto.** Demuestra exactamente el concepto de separar la información en un canal semántico y un canal acústico. El bitrate de 0.31 kbps es un orden de magnitud inferior a Opus (16–32 kbps).

### 3.2 CodecFlow (Marzo 2026)
- **Paper:** *"CodecFlow: Efficient Bandwidth Extension via Conditional Flow Matching in Neural Codec Latent Space"* — [arXiv:2603.02022](https://arxiv.org/abs/2603.02022)
- **Concepto:** Reconstrucción de voz de bajo ancho de banda directamente en el **espacio latente compacto** de un codec neural (evitando modelado de espectrograma/waveform).
- **Técnica:** Conditional flow matching + RVQ con restricciones estructurales para estabilidad.
- **Relevancia:** Demuestra que se puede operar eficientemente dentro del espacio latente del codec, lo cual es relevante para la capa de transmisión de nuestro pipeline.

---

## 4. Audio Language Models (ALMs) y Generación de Voz

Los Audio Language Models tratan los tokens discretos del codec como vocabulario y aplican técnicas de modelado de lenguaje para generar audio.

### 4.1 AudioLM (Google, 2022)
- **Paper:** *"AudioLM: a Language Modeling Approach to Audio Generation"* — [arXiv:2209.03143](https://arxiv.org/abs/2209.03143)
- **Concepto fundacional:** Mapea audio a tokens discretos y trata la generación como un problema de modelado de lenguaje. Introduce **tokenización híbrida:**
  - **Tokens semánticos:** De un masked language model pre-entrenado (w2v-BERT) → capturan estructura a largo plazo.
  - **Tokens acústicos:** De un codec neural (SoundStream) → aseguran síntesis de alta calidad.
- **Generación jerárquica:** Múltiples Transformers predicen tokens semánticos → tokens acústicos gruesos → tokens acústicos finos.
- **Resultados:** Genera continuaciones de habla sintáctica y semánticamente plausibles, **preservando identidad del hablante y prosodia**, sin necesitar transcripciones.
- **Relevancia:** ⭐ Define el paradigma de tokens semánticos vs. acústicos que es la base teórica de nuestro proyecto.

### 4.2 VALL-E (Microsoft, 2023)
- **Paper:** *"Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers"* — [arXiv:2301.02111](https://arxiv.org/abs/2301.02111)
- **Concepto:** TTS como tarea de modelado de lenguaje condicional. Pipeline: fonemas → códigos discretos (de EnCodec) → waveform.
- **Entrenamiento:** 60,000 horas de datos de habla en inglés (LibriLight).
- **Capacidad zero-shot:** Sintetiza voz personalizada con solo **3 segundos** de audio de un hablante no visto.
- **Resultados:** Supera sustancialmente otros sistemas zero-shot TTS en naturalidad y similitud de hablante. Preserva emoción y entorno acústico del prompt.
- **Evolución:** VALL-E 2 (human parity con Repetition Aware Sampling + Grouped Code Modeling), VALL-E R (alineación monotónica de fonemas para mayor robustez).
- **Relevancia:** Demostró que los tokens de codec neural son un vocabulario viable para LLMs de voz. Clave para el decoder de nuestro sistema.

### 4.3 VoiceCraft-X (Nov 2025)
- **Paper:** *"VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing"* — [arXiv:2511.12347](https://arxiv.org/abs/2511.12347)
- **Arquitectura:** Codec language model autorregresivo basado en Qwen3 LLM. Unifica TTS multilingüe (11 idiomas), clonación de voz y edición de habla en un solo modelo.
- **Innovación:** Mecanismo de reordenación de tokens con alineación temporal texto-audio.
- **Relevancia:** Muestra el estado del arte en generación multilingüe zero-shot, relevante como decoder avanzado.

### 4.4 SpeechEdit (Ene 2026)
- **Paper:** *"A Unified Neural Codec Language Model for Selective Editable Text to Speech Generation"* — [arXiv:2601.12480](https://arxiv.org/abs/2601.12480)
- **Concepto:** Codec language model que **aísla y controla selectivamente** atributos individuales (timbre, prosodia, paralingüística) mientras imita perfiles acústicos zero-shot.
- **Relevancia:** Demuestra control granular sobre los atributos que nuestro proyecto necesita transmitir por separado (identidad, prosodia, contenido).

---

## 5. Streaming, Baja Latencia y Preservación de Emoción

Estos papers abordan directamente la restricción de **latencia < 300 ms** de nuestro proyecto.

### 5.1 Moshi — Full-Duplex Real-Time Dialogue (Kyutai, 2024)
- **Latencia teórica:** 160 ms, práctica: **200 ms**.
- **Arquitectura:** LLM de texto (Helium, 7B params) + codec Mimi + esquema de tokenización paralelo para voz del sistema y del usuario.
- **Innovación "Inner Monologue":** Predice tokens de texto alineados temporalmente como prefijo a tokens de audio → mejora calidad lingüística y permite ASR/TTS streaming integrado.
- **Full-duplex:** Modela dinámicas conversacionales arbitrarias incluyendo solapamiento, interrupciones e interjecciones.
- **Relevancia:** ⭐ Referencia máxima para latencia. Demuestra que un sistema completo speech-to-speech puede funcionar a 200 ms.

### 5.2 JHCodec / "Reconstruct! Don't Encode" (Marzo 2026)
- **Paper:** [arXiv:2603.05887](https://arxiv.org/abs/2603.05887)
- **Innovación:** Self-Supervised Representation Reconstruction (SSRR) loss que:
  1. Acelera convergencia significativamente (resultados competitivos con **una sola GPU**).
  2. Mejora inteligibilidad reconstruyendo representaciones SSL del output del codec.
  3. Permite alta inteligibilidad **sin lookahead adicional** → arquitectura zero-lookahead para despliegue en tiempo real.
- **Código:** Open-source en [github.com/jhcodec843/jhcodec](https://github.com/jhcodec843/jhcodec).
- **Relevancia:** Técnica directamente aplicable para minimizar latencia en nuestro encoder/decoder.

### 5.3 StreamVoiceAnon+ (Marzo 2026)
- **Paper:** [arXiv:2603.06079](https://arxiv.org/abs/2603.06079)
- **Problema:** Los tokens de contenido de un codec language model **descartan información emocional**, y el modelo tiende a generar patrones acústicos dominantes en lugar de preservar atributos paralingüísticos.
- **Solución:** Fine-tuning supervisado con pares de expresiones neutras/emocionales + **destilación de emoción a nivel de frame** sobre los hidden states de tokens acústicos.
- **Resultados:** 49.2% UAR (preservación de emoción) con 5.77% WER (inteligibilidad) a **180 ms de latencia streaming**.
- **Relevancia:** ⭐ Aborda exactamente uno de nuestros problemas centrales: cómo preservar emoción cuando usamos tokens discretos de un codec neural.

### 5.4 MSpoof-TTS / Hierarchical Decoding (Marzo 2026)
- **Paper:** [arXiv:2603.05373](https://arxiv.org/abs/2603.05373)
- **Problema:** La inferencia de codec language models es vulnerable a artefactos a nivel de token y drift distribucional.
- **Solución:** Framework de inferencia sin reentrenamiento que usa detección de spoof multi-resolución + decodificación jerárquica para podar candidatos de baja calidad.
- **Relevancia:** Técnica aplicable en el decoder de nuestro pipeline para mejorar robustez de la síntesis.

---

## 6. Comunicaciones Semánticas para Voz

### 6.1 Marco Teórico
Las comunicaciones semánticas buscan transmitir el **significado** de un mensaje en lugar de una reproducción bit-a-bit de la señal. Para voz, esto implica:
- Extraer una representación semántica compacta (texto, embeddings, tokens discretos).
- Transmitir solo la semántica + metadatos (identidad, prosodia).
- Reconstruir la señal en el receptor usando un modelo generativo.

### 6.2 DeepSC-ST y DeepSC-SR
Trabajos previos (Xie et al.) han demostrado sistemas de comunicación semántica para transmisión de voz (DeepSC-ST) y reconocimiento de voz (DeepSC-SR) que extraen y transmiten solo las features semánticas relevantes. Estos sistemas muestran mejoras significativas en entornos de bajo SNR.

### 6.3 Surveys Relevantes (2024–2025)
- *"Semantic Communications: A Comprehensive Survey"* (ICUFN 2024): Revisa modelos autoencoder E2E y arquitecturas Transformer para comunicación semántica con texto, imagen y voz.
- *"Contemporary Survey on Semantic Communications"* (Feb 2025): Cubre Generative AI + Deep Joint Source-Channel Coding.
- *"Enhancing Semantic Communication with Deep Generative Models"* (ICASSP 2024): Incluye modelos de difusión para comunicación semántica de audio.

---

## 7. Representación del Habla y Codificación de Identidad

### 7.1 wav2vec 2.0 y HuBERT
- **wav2vec 2.0** (Meta): Auto-supervisado, aprende representaciones del habla a partir de audio crudo. Usado como feature extractor.
- **HuBERT** (Meta): Masked prediction of hidden units. Genera tokens semánticos discretos usados por AudioLM y otros ALMs como representación de alto nivel.

### 7.2 Speaker Encoders
- **ECAPA-TDNN:** Estado del arte en verificación de hablante. Genera embeddings de identidad de 192 dimensiones.
- **Resemblyzer:** Implementación ligera basada en GE2E loss.
- **x-vectors:** Enfoque clásico basado en TDNN + estadísticas de pooling.

---

## 8. Tabla Comparativa de Códecs Neuronales

| Modelo | Año | Bitrate | Latencia | Tokens semánticos | Streaming | Código Abierto |
|---|---|---|---|---|---|---|
| SoundStream | 2021 | 3–18 kbps | Baja (móvil) | No | Sí | No |
| EnCodec | 2022 | 1.5–24 kbps | Baja | No | Sí | ✅ |
| SNAC | 2024 | Variable | Baja | No | Sí | ✅ |
| Mimi (Moshi) | 2024 | **1.1 kbps** | **80 ms** | **Sí (destilación)** | Sí | ✅ |
| SemantiCodec | 2024 | **0.31–1.40 kbps** | Alta (difusión) | **Sí (AudioMAE)** | No | ✅ |
| LDCodec | 2025 | 6 kbps | Baja | No | Sí | No |
| JHCodec | 2026 | Competitivo | **Zero-lookahead** | Indirectos (SSRR) | Sí | ✅ |

---

## 9. Tabla Comparativa de Modelos Generativos de Voz

| Modelo | Año | Tipo | Zero-Shot | Clonación Voz | Control Prosodia | Multilingüe |
|---|---|---|---|---|---|---|
| AudioLM | 2022 | ALM jerárquico | Sí | Sí (implícita) | Preserva | No |
| VALL-E | 2023 | Codec LM | Sí (3s prompt) | ✅ | Preserva | No |
| VoiceCraft-X | 2025 | Codec LM + Qwen3 | Sí | ✅ | Sí | ✅ (11 idiomas) |
| SpeechEdit | 2026 | Codec LM unificado | Sí | ✅ | **Control selectivo** | No |
| Moshi | 2024 | Speech-to-Speech LM | N/A (full-duplex) | Persona fija | Inner Monologue | No |
| StreamVoiceAnon+ | 2026 | Codec LM fine-tuned | N/A | Anonimización | **Preservación emoción** | No |

---

## 10. Conclusiones para el Proyecto

### Hallazgos clave

1. **El paradigma de tokens discretos es dominante.** Prácticamente todo modelo de generación de voz SOTA (2024–2026) opera sobre tokens de un codec neural tipo RVQ.

2. **Dos enfoques principales para nuestro pipeline:**
   - **Cascada modular (STT → Semantic Encoder → Speaker Encoder → Prosody Encoder → Transmisión → TTS condicionado):** Mayor control sobre cada componente, pero mayor latencia y pérdida de información en las interfaces.
   - **End-to-End Neural Codec (audio → tokens discretos → transmisión → decoder):** Menor latencia, preservación implícita de identidad/prosodia, pero menor control explícito.

3. **SemantiCodec valida nuestra hipótesis central:** Es posible comprimir voz a 0.31 kbps con un encoder semántico + acústico, logrando calidad superior a codecs a bitrates mucho mayores.

4. **Mimi/Moshi demuestra viabilidad de tiempo real:** Latencia de 200 ms en un sistema completo speech-to-speech con codec a 1.1 kbps.

5. **La preservación de emoción es un problema activo:** StreamVoiceAnon+ muestra que los tokens de contenido pierden información emocional y requieren técnicas explícitas de destilación.

6. **JHCodec ofrece latencia mínima:** Su técnica SSRR permite zero-lookahead con alta inteligibilidad, ideal para la capa de codec de nuestro sistema.

### Recomendación para el diseño del sistema

> Para el **PoC 1** (baseline, alta latencia): Usar pipeline cascada con Whisper + ECAPA-TDNN + extracción de prosodia + XTTS/StyleTTS2 para validar la idea semántica.
>
> Para el **PoC 2** (objetivo, baja latencia): Adoptar una arquitectura inspirada en **SemantiCodec** (dual encoder semántico+acústico) combinada con las técnicas de streaming de **JHCodec** (zero-lookahead) y **Mimi** (codec a 1.1 kbps, 80 ms). Aplicar destilación de emoción tipo **StreamVoiceAnon+** para preservar prosodia.

---

## 11. Referencias Completas

| # | Paper | ArXiv | PDF en `papers/` |
|---|---|---|---|
| 1 | SoundStream | [2107.03312](https://arxiv.org/abs/2107.03312) | ✅ |
| 2 | EnCodec | [2210.13438](https://arxiv.org/abs/2210.13438) | ✅ |
| 3 | AudioLM | [2209.03143](https://arxiv.org/abs/2209.03143) | ✅ |
| 4 | Moshi / Mimi | [2410.00037](https://arxiv.org/abs/2410.00037) | ✅ |
| 5 | SNAC | [2410.14411](https://arxiv.org/abs/2410.14411) | ✅ |
| 6 | SemantiCodec | [2405.00233](https://arxiv.org/abs/2405.00233) | ✅ |
| 7 | LDCodec | [2510.15364](https://arxiv.org/abs/2510.15364) | ✅ |
| 8 | VALL-E | [2301.02111](https://arxiv.org/abs/2301.02111) | — |
| 9 | VoiceCraft-X | [2511.12347](https://arxiv.org/abs/2511.12347) | ✅ |
| 10 | SpeechEdit | [2601.12480](https://arxiv.org/abs/2601.12480) | ✅ |
| 11 | StreamVoiceAnon+ | [2603.06079](https://arxiv.org/abs/2603.06079) | ✅ |
| 12 | JHCodec | [2603.05887](https://arxiv.org/abs/2603.05887) | ✅ |
| 13 | CodecFlow | [2603.02022](https://arxiv.org/abs/2603.02022) | ✅ |
| 14 | MSpoof-TTS | [2603.05373](https://arxiv.org/abs/2603.05373) | ✅ |
