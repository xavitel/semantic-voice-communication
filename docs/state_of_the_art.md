# Capítulo 2. Estado del Arte

## 2.1 Introducción

La transmisión de voz en sistemas de comunicación ha estado históricamente dominada por el paradigma de codificación de forma de onda: la señal analógica del micrófono se muestrea, se cuantifica y se transmite como una secuencia de bits que representa fielmente la forma de onda original. Este enfoque, materializado en estándares como G.711 (64 kbps), G.729 (8 kbps) u Opus (6–510 kbps), ha demostrado ser robusto y eficiente dentro de los límites de la teoría de la información de Shannon. Sin embargo, presenta una limitación fundamental: trata la señal de voz como una señal genérica sin explotar su estructura semántica inherente.

Las comunicaciones semánticas, propuestas originalmente por Weaver y Shannon (1949) y formalizadas teóricamente por Carnap y Bar-Hillel (1952), plantean un cambio de paradigma: en lugar de transmitir bits que representen la señal, transmitir el *significado* del mensaje. En el contexto de la voz, esto implica separar el contenido lingüístico (qué se dice), la identidad del hablante (quién lo dice) y las características prosódicas y emocionales (cómo se dice), comprimir cada componente de forma independiente y reconstruir la señal en el receptor mediante modelos generativos.

Este capítulo presenta un mapeo exhaustivo del estado del arte en los campos que convergen en esta investigación: códecs neuronales de audio (Sección 2.2), modelos de lenguaje de audio y generación de voz (Sección 2.3), preservación de identidad y prosodia (Sección 2.4), técnicas de streaming y baja latencia (Sección 2.5) y comunicaciones semánticas aplicadas a voz (Sección 2.6). Se concluye con un análisis comparativo (Sección 2.7) y las implicaciones para el diseño de nuestro sistema (Sección 2.8).

---

## 2.2 Códecs Neuronales de Audio

Los códecs neuronales de audio representan la columna vertebral tecnológica de la comunicación semántica de voz moderna. A diferencia de los codecs tradicionales basados en modelos lineales del tracto vocal (como CELP), los códecs neuronales emplean redes neuronales profundas entrenadas end-to-end para comprimir audio en representaciones discretas (tokens) que pueden reconstruirse con alta fidelidad perceptual a bitrates significativamente inferiores.

### 2.2.1 Arquitectura canónica: Encoder-RVQ-Decoder

La arquitectura estándar de un codec neural, establecida por SoundStream (Zeghidour et al., 2021) y refinada por EnCodec (Défossez et al., 2022), consta de tres componentes:

1. **Encoder convolucional:** Transforma la forma de onda de entrada en una representación latente continua de baja dimensionalidad. Típicamente emplea capas convolucionales con downsampling progresivo.
2. **Residual Vector Quantization (RVQ):** Discretiza la representación latente mediante una cascada de cuantizadores vectoriales. Cada cuantizador opera sobre el residuo del anterior, produciendo múltiples streams paralelos de tokens discretos. El número de cuantizadores controla el bitrate: más cuantizadores implican mayor fidelidad pero mayor ancho de banda.
3. **Decoder convolucional:** Reconstruye la forma de onda a partir de los tokens cuantizados. El entrenamiento combina pérdidas de reconstrucción (L1/L2 en frecuencia y tiempo), pérdidas adversariales (discriminadores GAN multi-período y multi-escala) y pérdidas de feature matching.

### 2.2.2 SoundStream (Google, 2021)

SoundStream (Zeghidour et al., 2021) fue el primer codec neural en demostrar superioridad sobre codecs clásicos en evaluaciones subjetivas a través de un rango amplio de bitrates. Su arquitectura encoder/decoder convolucional con RVQ se entrena con una combinación de pérdidas adversariales y de reconstrucción, aprovechando avances previos en text-to-speech y mejora de habla.

Una contribución clave de SoundStream es el uso de *structured dropout* sobre las capas del cuantizador durante el entrenamiento: un único modelo puede operar a bitrates variables entre 3 y 18 kbps con pérdida de calidad negligible respecto a modelos entrenados a bitrate fijo. En evaluaciones subjetivas con audio a 24 kHz, SoundStream a 3 kbps supera a Opus a 12 kbps y se aproxima a EVS a 9.6 kbps, lo cual representó un hito sin precedentes para un codec neural. Además, el modelo soporta inferencia streaming en tiempo real en CPU de un smartphone y permite compresión y mejora conjunta (por ejemplo, supresión de ruido de fondo) sin latencia adicional.

### 2.2.3 EnCodec (Meta, 2022)

EnCodec (Défossez et al., 2022) refina la arquitectura de SoundStream con varias innovaciones. Introduce un discriminador adversarial basado en un único espectrograma multi-escala, simplificando el entrenamiento y reduciendo artefactos. Propone un mecanismo de *loss balancer* que estabiliza el entrenamiento al definir el peso de cada pérdida como la fracción del gradiente total que debe representar, desacoplando este hiperparámetro de la escala típica de la pérdida.

EnCodec opera en un rango de 1.5 a 24 kbps para audio monofónico a 24 kHz y de 3 a 24 kbps para audio estereofónico a 48 kHz. En pruebas MUSHRA (MUltiple Stimuli with Hidden Reference and Anchor), EnCodec supera a los métodos baseline en todos los escenarios evaluados —habla limpia, habla con ruido y reverberación, y música— tanto para configuraciones monofónicas como estereofónicas. Los autores además demuestran que modelos Transformer ligeros pueden comprimir adicionalmente la representación hasta un 40% manteniendo operación en tiempo real.

EnCodec se ha convertido en el estándar de facto para tokenización de audio en modelos generativos, siendo la base del ecosistema AudioCraft de Meta. Su código y modelos están disponibles públicamente, lo que ha catalizado una amplia adopción en la comunidad investigadora.

### 2.2.4 SNAC: Multi-Scale Neural Audio Codec (2024)

SNAC (Siuzdak, 2024) propone una extensión elegante de RVQ en la que los cuantizadores operan a **diferentes resoluciones temporales**. Mientras que en RVQ estándar todos los cuantizadores operan al mismo frame rate, SNAC aplica una jerarquía de cuantizadores a frame rates variables, de modo que los primeros cuantizadores (que capturan la estructura gruesa) operan a frecuencias más bajas y los posteriores (que capturan detalles finos) a frecuencias más altas.

Esta adaptación multi-escala permite que el codec se ajuste a la estructura temporal inherente del audio: las características prosódicas y fonéticas gruesas varían lentamente mientras que los detalles acústicos finos (textura, ruido de fricación) varían rápidamente. El resultado es una compresión más eficiente, validada mediante evaluaciones objetivas y subjetivas extensivas. El código y los pesos del modelo están disponibles públicamente.

### 2.2.5 LDCodec: Low-Complexity Decoder (2025)

LDCodec (2025) aborda una limitación práctica crítica de los códecs neuronales: la **complejidad computacional del decoder**. Para aplicaciones en dispositivos móviles (smartphones como clientes de streaming), el decoder debe ser lo suficientemente ligero para operar con recursos limitados de CPU/GPU.

LDCodec introduce tres innovaciones: (1) una unidad residual novedosa combinada con *Long-term and Short-term Residual Vector Quantization* (LSRVQ), que captura dependencias temporales a múltiples escalas; (2) discriminadores de frecuencia subbanda/fullband que mejoran la fidelidad espectral; y (3) funciones de pérdida perceptual optimizadas. El resultado es un codec que a 6 kbps supera a Opus a 12 kbps manteniendo una complejidad del decoder significativamente menor que EnCodec o SoundStream.

### 2.2.6 El Codec Mimi (Kyutai, 2024)

Mimi es el codec neural integrado en Moshi (Défossez et al., 2024), el primer modelo de diálogo hablado full-duplex en tiempo real. A diferencia de SoundStream y EnCodec, que codifican exclusivamente información acústica, Mimi **modela conjuntamente información semántica y acústica** mediante un proceso de destilación desde representaciones de habla auto-supervisadas.

Mimi procesa audio a 24 kHz y lo comprime a una representación a 12.5 Hz con un ancho de banda de tan solo **1.1 kbps**, operando en modo fully streaming con una latencia de **80 ms**. Esta combinación de ultra-bajo bitrate, latencia mínima e integración semántica lo convierte en el codec más avanzado disponible a fecha de escritura para aplicaciones de comunicación en tiempo real.

---

## 2.3 Modelos de Lenguaje de Audio y Generación de Voz

Los Audio Language Models (ALMs) representan un cambio de paradigma en la generación de voz: en lugar de modelar directamente formas de onda o espectrogramas, tratan los tokens discretos producidos por un codec neural como un vocabulario y aplican técnicas de modelado de lenguaje autorregresivo para generar secuencias de audio.

### 2.3.1 AudioLM: el paradigma fundacional (Google, 2022)

AudioLM (Borsos et al., 2022) establece el marco conceptual que subyace a todos los ALMs posteriores. Su contribución central es la **tokenización híbrida** que combina dos tipos de tokens discretos:

- **Tokens semánticos:** Obtenidos de las activaciones discretizadas de un modelo de lenguaje enmascarado pre-entrenado sobre audio (w2v-BERT). Estos tokens capturan la estructura lingüística y prosódica a largo plazo, pero carecen de detalle acústico suficiente para síntesis de alta calidad.
- **Tokens acústicos:** Producidos por un codec neural (SoundStream). Capturan el detalle acústico fino necesario para reconstrucción de alta fidelidad.

AudioLM genera audio mediante una cascada jerárquica de modelos Transformer: primero predice tokens semánticos (estructura global), luego tokens acústicos gruesos y finalmente tokens acústicos finos. Cuando se entrena sobre habla, y sin necesidad de transcripciones ni anotaciones, AudioLM genera continuaciones de habla sintáctica y semánticamente plausibles que preservan la identidad del hablante y la prosodia para hablantes no vistos durante el entrenamiento.

La separación explícita entre tokens semánticos y acústicos que introduce AudioLM es directamente análoga a la separación que proponemos en nuestro sistema entre el canal semántico (contenido) y los canales paralingüísticos (identidad, prosodia).

### 2.3.2 VALL-E: TTS como Modelado de Lenguaje (Microsoft, 2023)

VALL-E (Wang et al., 2023) reformula text-to-speech como una tarea de modelado de lenguaje condicional sobre tokens de codec neural, siguiendo el pipeline: fonemas → códigos discretos (de EnCodec) → forma de onda. Su entrenamiento sobre 60,000 horas de habla en inglés (LibriLight) le permite exhibir capacidades de aprendizaje en contexto (*in-context learning*): sintetiza voz personalizada de alta calidad con solo **3 segundos** de audio de un hablante no visto como prompt acústico.

En evaluaciones, VALL-E supera sustancialmente a sistemas TTS zero-shot previos tanto en naturalidad como en similitud con el hablante original. Además, preserva la emoción y el entorno acústico del prompt de entrada. Trabajos posteriores como VALL-E 2 (que alcanza *human parity* mediante Repetition Aware Sampling y Grouped Code Modeling) y VALL-E R (que mejora la robustez con alineación monotónica de fonemas) han consolidado este paradigma.

VALL-E demostró que los tokens de un codec neural constituyen un vocabulario viable para LLMs de voz, validando la viabilidad de un decoder generativo condicionado por representaciones semánticas transmitidas.

### 2.3.3 VoiceCraft-X: Generación Multilingüe Unificada (2025)

VoiceCraft-X (Zheng et al., 2025) unifica la edición de habla multilingüe y la síntesis TTS zero-shot en 11 idiomas (inglés, mandarín, coreano, japonés, español, francés, alemán, neerlandés, italiano, portugués y polaco) dentro de un único modelo autorregresivo. Utiliza el LLM Qwen3 para procesamiento textual cross-lingual sin necesidad de fonemas, e introduce un mecanismo novedoso de reordenación de tokens con alineación temporal texto-audio.

El modelo genera habla de alta calidad y naturalidad, creando audio nuevo o editando grabaciones existentes dentro de un marco unificado, con rendimiento robusto incluso con datos limitados por idioma. VoiceCraft-X demuestra que un único modelo codec language model puede manejar la complejidad multilingüe necesaria para un sistema de comunicación semántica de voz con cobertura global.

### 2.3.4 SpeechEdit: Control Selectivo de Atributos (2026)

SpeechEdit (Pei et al., 2026) aborda una limitación importante de los codec language models existentes: al imitar holísticamente el perfil acústico de un prompt de referencia (timbre, prosodia, información paralingüística), estos modelos no permiten aislar y controlar atributos individuales.

SpeechEdit extiende el TTS zero-shot con un mecanismo de **control selectivo**: por defecto reproduce el perfil acústico completo inferido del prompt, pero puede sobrescribir selectivamente solo los atributos especificados por instrucciones de control explícitas. Para hacerlo posible, se entrena sobre el dataset LibriEdit, que proporciona pares de entrenamiento *delta* (conscientes de diferencias). Este control granular es directamente relevante para un sistema de comunicación semántica donde los distintos atributos se transmiten por canales separados y deben recombinarse en el receptor.

---

## 2.4 Preservación de Identidad del Hablante y Prosodia

La preservación de la identidad del hablante y las características prosódicas y emocionales es uno de los desafíos centrales de la comunicación semántica de voz. Si el sistema transmite únicamente contenido semántico y lo reconstruye mediante TTS, se pierde la riqueza expresiva que distingue la comunicación humana.

### 2.4.1 Codificación de Identidad del Hablante

Los modelos de verificación y reconocimiento de hablante generan embeddings de identidad compactos que capturan las características tímbricas únicas de cada persona:

- **ECAPA-TDNN** (Desplanques et al., 2020): Estado del arte en verificación de hablante. Genera embeddings de 192 dimensiones que capturan la identidad del hablante con alta discriminabilidad. Utiliza Squeeze-Excitation, Res2Net y atención multi-capa para modelar dependencias temporales a múltiples escalas.
- **x-vectors** (Snyder et al., 2018): Enfoque basado en TDNN con estadísticas de pooling temporal, ampliamente utilizado como baseline robusto.
- **Resemblyzer:** Implementación ligera basada en Generalized End-to-End loss (GE2E), optimizada para inferencia rápida.

Estos embeddings de identidad pueden transmitirse como metadatos compactos (típicamente 192–512 valores float32, o ~768 bytes–2 KB sin comprimir) y utilizarse para condicionar el modelo generativo en el receptor, permitiendo que la voz reconstruida suene como el hablante original.

### 2.4.2 Prosodia y Emoción

La prosodia comprende las variaciones de tono (F0), energía, duración y ritmo que transmiten intención comunicativa, actitud y estado emocional. Su preservación es crítica para evitar que la comunicación reconstruida suene monótona o artificial.

Los enfoques para capturar prosodia incluyen:

- **Extracción explícita de contornos:** Pitch (F0), energía y tasa de habla pueden extraerse directamente de la señal y transmitirse como secuencias paramétricas compactas.
- **Prosody encoders aprendidos:** Modelos como los empleados en StyleTTS2 (Li et al., 2023) aprenden representaciones latentes de estilo prosódico que capturan variaciones expresivas de forma compacta.
- **Reconocimiento de emociones del habla (SER):** Redes neuronales entrenadas para clasificar o representar el estado emocional del hablante (ira, alegría, tristeza, sorpresa, etc.) a partir de características acústicas.

### 2.4.3 El Problema de la Pérdida Emocional en Tokens Discretos

Un hallazgo reciente y crucial para nuestro proyecto proviene de StreamVoiceAnon+ (Kuzmin et al., 2026): los tokens de contenido obtenidos mediante codecs neuronales **descartan activamente información emocional**, y los codec language models tienden a generar patrones acústicos dominantes (voz neutra) en lugar de preservar atributos paralingüísticos del hablante original.

StreamVoiceAnon+ propone una solución basada en fine-tuning supervisado con pares de expresiones de la misma oración con diferentes niveles emocionales, combinado con **destilación de emoción a nivel de frame** sobre los hidden states de los tokens acústicos. Esta técnica logra una mejora relativa del 24% en la tasa de reconocimiento de emoción (UAR: 39.7% → 49.2%) sin degradar la inteligibilidad (WER: 5.77%) ni la latencia (180 ms streaming).

Este resultado tiene implicaciones directas para el diseño de nuestro sistema: no basta con transmitir tokens discretos y esperar que la emoción se preserve implícitamente. Es necesario un mecanismo explícito de preservación o transmisión de información emocional.

---

## 2.5 Streaming, Baja Latencia y Despliegue en Tiempo Real

Para que un sistema de comunicación semántica de voz sea viable como alternativa a VoIP, debe cumplir restricciones estrictas de latencia. El estándar de la ITU-T (Recomendación G.114) establece que el retardo boca-a-oído en comunicaciones interactivas no debe superar los 150 ms para calidad óptima, siendo 300-400 ms el límite aceptable. Este requisito es uno de los mayores desafíos técnicos del proyecto.

### 2.5.1 Moshi: Full-Duplex a 200 ms (Kyutai, 2024)

Moshi (Défossez et al., 2024) es el primer modelo de diálogo hablado en tiempo real y full-duplex basado en un LLM. A diferencia de los sistemas tradicionales que encadenan módulos separados de VAD → ASR → LLM textual → TTS (con latencias acumuladas de varios segundos), Moshi plantea el diálogo hablado como generación speech-to-speech directa.

Su arquitectura se compone de tres elementos: (1) **Helium**, un LLM de texto de 7B parámetros que actúa como backbone; (2) el **codec Mimi** para tokenización de audio; y (3) un esquema de tokenización paralela de dos streams (voz del sistema y voz del usuario) que elimina la necesidad de turnos explícitos y permite modelar dinámicas conversacionales arbitrarias, incluyendo solapamiento de habla, interrupciones e interjecciones.

El método de **"Inner Monologue"** es una innovación clave: Moshi predice tokens de texto alineados temporalmente como prefijo a los tokens de audio, lo que mejora significativamente la calidad lingüística del habla generada y además proporciona capacidades integradas de ASR y TTS streaming. La latencia teórica del sistema es de 160 ms (200 ms en la práctica), validando que un pipeline completo de comunicación semántica puede operar dentro de los límites de tiempo real.

### 2.5.2 JHCodec: Zero-Lookahead con Alta Inteligibilidad (2026)

JHCodec (Lee et al., 2026) aborda un problema técnico específico de los codecs streaming basados en Transformer: para mantener alta inteligibilidad, estos codecs típicamente requieren *lookahead* (acceso a frames futuros), lo cual añade latencia.

JHCodec introduce la pérdida de **Self-Supervised Representation Reconstruction (SSRR)**, que fundamentalmente mejora el entrenamiento del codec de tres formas: (1) acelera significativamente la convergencia, permitiendo resultados competitivos con una sola GPU; (2) mejora la inteligibilidad al reconstruir representaciones SSL a partir de las salidas del codec; y (3) permite alta inteligibilidad **sin lookahead adicional**, habilitando una arquitectura zero-lookahead para despliegue en tiempo real.

Esta contribución es directamente aplicable a la capa de codec de nuestro sistema, donde minimizar la latencia del encoder es crítico para cumplir el requisito de < 300 ms end-to-end.

### 2.5.3 MSpoof-TTS: Decodificación Jerárquica Robusta (2026)

MSpoof-TTS (Zhao et al., 2026) aborda la vulnerabilidad de los codec language models a artefactos a nivel de token y drift distribucional durante la inferencia, que degradan el realismo perceptual de la voz generada. En lugar de reentrenar o aplicar optimización de preferencias, propone un framework de inferencia *training-free* que utiliza guía discriminativa multi-resolución.

El sistema evalúa las secuencias de tokens del codec a diferentes granularidades temporales para detectar patrones localmente inconsistentes o antinaturales, y luego integra estos detectores en una estrategia de decodificación jerárquica que podaprogresivamente candidatos de baja calidad y re-rankea hipótesis. Esta técnica puede aplicarse al decoder de nuestro pipeline para mejorar la robustez de la síntesis sin modificar los parámetros del modelo base.

---

## 2.6 Comunicaciones Semánticas Aplicadas a Voz

### 2.6.1 Fundamentos Teóricos

Las comunicaciones semánticas, tal como las formuló Weaver (1949), proponen tres niveles de comunicación: (A) el nivel técnico (¿con qué precisión se transmiten los símbolos?), (B) el nivel semántico (¿con qué precisión los símbolos transmiten el significado deseado?) y (C) el nivel de efectividad (¿con qué efectividad el significado recibido afecta la conducta del receptor?). Los sistemas de comunicación convencionales operan exclusivamente en el nivel A, maximizando la fidelidad de la señal bit a bit. Las comunicaciones semánticas buscan operar en el nivel B, transmitiendo solo la información necesaria para reconstruir el significado.

En el contexto de la voz, la información semántica incluye:
- **Contenido lingüístico:** Las palabras pronunciadas (nivel léxico-sintáctico).
- **Identidad del hablante:** Características tímbricas invariantes (nivel paralingüístico estático).
- **Prosodia y emoción:** Entonación, ritmo, énfasis, estado emocional (nivel paralingüístico dinámico).

### 2.6.2 Deep Joint Source-Channel Coding (DeepJSCC)

Un enfoque central en comunicaciones semánticas es el Deep Joint Source-Channel Coding (DeepJSCC), donde un autoencoder neural aprende conjuntamente la compresión de fuente y la codificación de canal, optimizando directamente la calidad de la comunicación semántica en lugar de la fidelidad de la señal.

Los trabajos de Xie et al. han demostrado la viabilidad de este enfoque para voz:

- **DeepSC-ST** (Deep Semantic Communication for Speech Transmission): Extrae y transmite features semánticas de la señal de habla, logrando reconstrucción inteligible incluso en condiciones de bajo SNR donde los codecs convencionales fallan.
- **DeepSC-SR** (Deep Semantic Communication for Speech Recognition): Optimiza la transmisión para maximizar la precisión del reconocimiento de voz en el receptor, reduciendo drásticamente el ancho de banda necesario cuando el objetivo es comprensión en lugar de reconstrucción.

### 2.6.3 El Papel de los Modelos Generativos

Los surveys recientes (ICASSP 2024, IEEE ICUFN 2024) identifican los modelos generativos profundos como elementos pivotales para las comunicaciones semánticas de próxima generación. Específicamente:

- **Modelos de difusión** pueden regenerar datos semánticamente consistentes a partir de representaciones comprimidas, actuando como decoders sofisticados en el receptor (como demuestra SemantiCodec con su decoder basado en difusión).
- **LLMs de audio** pueden servir simultáneamente como codificadores semánticos y decoders generativos, unificando el pipeline de comunicación.
- **Autoencoders variacionales** permiten aprender espacios latentes continuos donde las distancias reflejan similitud semántica.

### 2.6.4 SemantiCodec: El Puente entre Codecs Neuronales y Comunicación Semántica

SemantiCodec (Liu et al., 2024) representa la convergencia más directa entre los campos de códecs neuronales y comunicaciones semánticas. Su arquitectura dual es paradigmática:

- **Encoder semántico:** Un Audio Masked Autoencoder (AudioMAE) pre-entrenado, cuyas activaciones se discretizan mediante k-means clustering sobre grandes volúmenes de datos de audio. Estos tokens capturan la estructura semántica del audio (contenido, intención, emoción a alto nivel).
- **Encoder acústico:** Una red convolucional que captura los detalles espectrales y temporales residuales no representados por el encoder semántico.
- **Decoder por difusión:** Reconstruye el audio a partir de ambos streams de tokens, aprovechando la capacidad generativa de los modelos de difusión para rellenar detalles acústicos finos.

SemantiCodec opera a tasas de tokens de 25, 50 y 100 por segundo, correspondientes a bitrates de **0.31, 0.62 y 1.40 kbps** respectivamente. A pesar de estos bitrates extremadamente bajos, supera significativamente al codec Descript en calidad de reconstrucción. Más importante aún, los experimentos demuestran que SemantiCodec retiene información semántica significativamente más rica que todos los codecs evaluados, incluso a bitrates mucho menores.

Este resultado valida directamente la hipótesis central de nuestra investigación: la separación explícita entre información semántica y acústica permite alcanzar ratios de compresión de un orden de magnitud superiores a los codecs convencionales e incluso neuronales puramente acústicos.

---

## 2.7 Análisis Comparativo

### 2.7.1 Códecs: Bitrate, Latencia y Capacidades

La siguiente tabla sintetiza las características técnicas de los códecs neuronales revisados en comparación con codecs convencionales de referencia:

| Codec | Tipo | Bitrate | Latencia | Tokens Semánticos | Streaming | Open Source |
|---|---|---|---|---|---|---|
| G.711 | Convencional | 64 kbps | ~1 ms | No | Sí | — |
| Opus | Convencional | 6–510 kbps (típ. 16–32) | 2.5–60 ms | No | Sí | ✅ |
| EVS | Convencional | 5.9–128 kbps | ~32 ms | No | Sí | No |
| SoundStream | Neural | 3–18 kbps | Baja (móvil) | No | Sí | No |
| EnCodec | Neural | 1.5–24 kbps | Baja | No | Sí | ✅ |
| SNAC | Neural (multi-escala) | Variable | Baja | No | Sí | ✅ |
| LDCodec | Neural (low decoder) | 6 kbps | Baja | No | Sí | No |
| Mimi | Neural + semántico | **1.1 kbps** | **80 ms** | **Sí** | Sí | ✅ |
| SemantiCodec | Semántico + acústico | **0.31–1.40 kbps** | Alta (difusión) | **Sí** | No | ✅ |
| JHCodec | Neural + SSRR | Competitivo | **Zero-lookahead** | Indirecto | Sí | ✅ |

Se observa una clara progresión: desde los 64 kbps de G.711 hasta los 0.31 kbps de SemantiCodec, una **reducción de más de 200×** en ancho de banda. Sin embargo, existe un trade-off fundamental entre bitrate y latencia: SemantiCodec logra el menor bitrate pero requiere un decoder de difusión que impide operación en tiempo real, mientras que Mimi alcanza 1.1 kbps con streaming a 80 ms.

### 2.7.2 Modelos Generativos: Capacidades de Reconstrucción

| Modelo | Año | Tipo | Zero-Shot | Clonación Voz | Control Prosodia | Latencia |
|---|---|---|---|---|---|---|
| AudioLM | 2022 | ALM jerárquico | Sí | Implícita | Preserva | No tiempo real |
| VALL-E | 2023 | Codec LM | Sí (3s) | ✅ | Preserva | No tiempo real |
| StyleTTS2 | 2023 | Flow-based | Con ref. audio | ✅ | ✅ | Baja |
| XTTS | 2023 | Autorregresivo | Sí (6s) | ✅ | Limitado | Media |
| VoiceCraft-X | 2025 | Codec LM + Qwen3 | Sí | ✅ | Sí | Media |
| SpeechEdit | 2026 | Codec LM | Sí | ✅ | **Selectivo** | Media |
| Moshi | 2024 | Speech-to-Speech | Full-duplex | Persona fija | Inner Monologue | **200 ms** |

---

## 2.8 Implicaciones para el Diseño del Sistema

El análisis del estado del arte revela dos enfoques arquitectónicos viables para un sistema de comunicación semántica de voz, cada uno con compromisos distintos:

### Enfoque 1: Pipeline Cascada Modular

```
Audio → STT (Whisper) → Semantic Encoding → Speaker Embedding (ECAPA-TDNN)
     → Prosody Extraction → [Transmisión: texto + embeddings] → TTS Condicionado
     (StyleTTS2/XTTS) → Audio reconstruido
```

**Ventajas:** Control explícito sobre cada componente; cada módulo puede desarrollarse, evaluarse y mejorase independientemente; máxima reducción de bitrate (solo se transmite texto + metadatos compactos).

**Limitaciones:** Alta latencia acumulada (cada módulo añade su propia latencia); pérdida de información en cada interfaz entre módulos; dificultad para preservar matices prosódicos y emocionales a través de toda la cascada (como demuestra StreamVoiceAnon+).

### Enfoque 2: Codec Neural End-to-End con Tokens Semánticos

```
Audio → Neural Codec Encoder (tipo Mimi/SemantiCodec) → [Transmisión: tokens
discretos semánticos + acústicos] → Neural Codec Decoder → Audio reconstruido
```

**Ventajas:** Preservación implícita de identidad y prosodia en los tokens; baja latencia potencial (Mimi: 80 ms); entrenamiento end-to-end que optimiza directamente la calidad de reconstrucción.

**Limitaciones:** Menor control explícito sobre los atributos individuales; el bitrate, aunque bajo (1.1 kbps en Mimi), es superior al del Enfoque 1 (que puede llegar a < 0.5 kbps); requiere GPUs para encodificación y decodificación.

### Recomendación

Los resultados del estado del arte sugieren una estrategia de investigación en **dos fases**:

1. **Fase 1 (Baseline — Alta latencia):** Implementar el Enfoque 1 con Whisper + ECAPA-TDNN + StyleTTS2/XTTS para validar la viabilidad de la reconstrucción semántica y establecer métricas base de calidad percibida (MOS), fidelidad semántica y similitud de hablante.

2. **Fase 2 (Objetivo — Baja latencia):** Migrar al Enfoque 2, adoptando una arquitectura inspirada en SemantiCodec (dual encoder semántico + acústico) con las técnicas de streaming de JHCodec (zero-lookahead) y Mimi (1.1 kbps, 80 ms), aplicando destilación de emoción tipo StreamVoiceAnon+ para preservar la prosodia.

La convergencia de avances en codecs neuronales, audio language models y comunicaciones semánticas durante el período 2024–2026 crea una ventana de oportunidad sin precedentes para materializar un sistema de comunicación semántica de voz viable, con reducciones de ancho de banda de 10–200× respecto a VoIP convencional y latencias potencialmente compatibles con comunicación bidireccional en tiempo real.
