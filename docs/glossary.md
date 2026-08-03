# Glossary of Semantic Voice Communication

> A technical glossary of terms used in the semantic communication research area, provided in English and Spanish.

## Architectures

### **End-to-End Neural Codec** / **Códec Neuronal End-to-End**
- **🇬🇧 EN:** A unified neural architecture that directly encodes raw audio into a compact token stream and decodes it back to audio without explicit intermediary linguistic representations.
- **🇪🇸 ES:** Una arquitectura neuronal unificada que codifica directamente el audio crudo en un flujo compacto de tokens y lo decodifica de nuevo a audio sin representaciones lingüísticas intermedias explícitas.

### **Generative TTS** / **TTS Generativo**
- **🇬🇧 EN:** Text-to-Speech models that use generative AI (such as language models or diffusion) to synthesize natural-sounding speech from text or semantic tokens.
- **🇪🇸 ES:** Modelos de Texto a Voz que utilizan IA generativa (como modelos de lenguaje o difusión) para sintetizar habla de sonido natural a partir de texto o tokens semánticos.

### **Joint Source-Channel Coding (JSCC)** / **Codificación Conjunta Fuente-Canal (JSCC)**
- **🇬🇧 EN:** A method where source coding (compression) and channel coding (error protection) are optimized together, often using neural networks, to improve robustness over noisy channels.
- **🇪🇸 ES:** Un método donde la codificación de fuente (compresión) y de canal (protección contra errores) se optimizan juntas, a menudo usando redes neuronales, para mejorar la robustez en canales ruidosos.

### **Modular Cascade Pipeline** / **Pipeline Cascada Modular**
- **🇬🇧 EN:** An architecture that explicitly separates speech into modules (Speech-to-Text, speaker encoder, prosody encoder) for transmission, and reconstructs it using Text-to-Speech (TTS).
- **🇪🇸 ES:** Una arquitectura que separa explícitamente el habla en módulos (ASR, codificador de hablante, codificador de prosodia) para la transmisión, y la reconstruye usando Texto a Voz (TTS).

### **Neural Audio Codec** / **Códec Neuronal de Audio**
- **🇬🇧 EN:** An audio compression system based on deep neural networks (typically autoencoders), replacing traditional signal processing codecs.
- **🇪🇸 ES:** Un sistema de compresión de audio basado en redes neuronales profundas (típicamente autoencoders), que reemplaza a los códecs de procesamiento de señales tradicionales.

### **Residual Vector Quantization (RVQ)** / **Cuantización Vectorial Residual (RVQ)**
- **🇬🇧 EN:** A technique used in neural codecs (like SoundStream and EnCodec) that cascades multiple vector quantizers to progressively compress the audio representation.
- **🇪🇸 ES:** Una técnica utilizada en códecs neuronales (como SoundStream y EnCodec) que pone en cascada múltiples cuantizadores vectoriales para comprimir progresivamente la representación de audio.

## General Concepts

### **Emotion / Affective State** / **Emoción / Estado Afectivo**
- **🇬🇧 EN:** The emotional state conveyed through the voice, which is distinct from the linguistic content but crucial for natural communication.
- **🇪🇸 ES:** El estado emocional transmitido a través de la voz, que es distinto del contenido lingüístico pero crucial para una comunicación natural.

### **Linguistic Content** / **Contenido Lingüístico**
- **🇬🇧 EN:** The actual words spoken in a voice message, representing its lexical and syntactic meaning.
- **🇪🇸 ES:** Las palabras exactas pronunciadas en un mensaje de voz, que representan su significado léxico y sintáctico.

### **Prosody** / **Prosodia**
- **🇬🇧 EN:** The dynamic paralinguistic aspects of speech, including intonation, rhythm, emphasis, and pitch contours.
- **🇪🇸 ES:** Los aspectos paralingüísticos dinámicos del habla, incluyendo la entonación, el ritmo, el énfasis y los contornos de tono.

### **Semantic Communication** / **Comunicación Semántica**
- **🇬🇧 EN:** A communication paradigm that focuses on transmitting the meaning or semantic content of a message rather than its exact physical signal representation (Shannon's Level B).
- **🇪🇸 ES:** Un paradigma de comunicación que se centra en transmitir el significado o contenido semántico de un mensaje en lugar de su representación física exacta (Nivel B de Shannon).

### **Speaker Identity** / **Identidad del Hablante**
- **🇬🇧 EN:** The static paralinguistic characteristics of a speaker's voice, such as timbre and vocal tract properties.
- **🇪🇸 ES:** Las características paralingüísticas estáticas de la voz de un hablante, como el timbre y las propiedades del tracto vocal.

## Metrics

### **Character Error Rate (CER)** / **Character Error Rate (CER)**
- **🇬🇧 EN:** Similar to WER, but measures the error rate at the character level, often used for languages without explicit word boundaries.
- **🇪🇸 ES:** Similar al WER, pero mide la tasa de error a nivel de carácter, a menudo usado para idiomas sin límites de palabras explícitos.

### **Mean Opinion Score (MOS)** / **Mean Opinion Score (MOS)**
- **🇬🇧 EN:** A subjective measure of the perceived quality of speech, typically rated on a scale from 1 (bad) to 5 (excellent).
- **🇪🇸 ES:** Una medida subjetiva de la calidad percibida del habla, típicamente evaluada en una escala de 1 (malo) a 5 (excelente).

### **Real-Time Factor (RTF)** / **Real-Time Factor (RTF)**
- **🇬🇧 EN:** A metric indicating processing speed; it is the ratio of processing time to the duration of the audio. RTF < 1 indicates faster-than-real-time processing.
- **🇪🇸 ES:** Una métrica que indica la velocidad de procesamiento; es la proporción del tiempo de procesamiento sobre la duración del audio. Un RTF < 1 indica un procesamiento más rápido que el tiempo real.

### **Speaker Similarity (SIM)** / **Similitud de Hablante (SIM)**
- **🇬🇧 EN:** A metric that measures how closely the reconstructed voice matches the original speaker's voice, often computed using cosine similarity of speaker embeddings.
- **🇪🇸 ES:** Una métrica que mide qué tan de cerca coincide la voz reconstruida con la voz original del hablante, a menudo calculada usando la similitud coseno de los embeddings de hablante.

### **Unweighted Average Recall (UAR)** / **Unweighted Average Recall (UAR)**
- **🇬🇧 EN:** A metric commonly used in Speech Emotion Recognition (SER) to evaluate classification accuracy across classes without bias toward majority classes.
- **🇪🇸 ES:** Una métrica comúnmente utilizada en el Reconocimiento de Emociones del Habla (SER) para evaluar la precisión de clasificación entre clases sin sesgo hacia las clases mayoritarias.

### **Word Error Rate (WER)** / **Word Error Rate (WER)**
- **🇬🇧 EN:** A common metric for the performance of speech recognition, measuring the percentage of words incorrectly recognized (insertions, deletions, and substitutions).
- **🇪🇸 ES:** Una métrica común para el rendimiento del reconocimiento de voz, que mide el porcentaje de palabras reconocidas incorrectamente (inserciones, eliminaciones y sustituciones).

## Network/Transmission

### **Bitrate** / **Tasa de Bits (Bitrate)**
- **🇬🇧 EN:** The amount of data transmitted per second, typically measured in kilobits per second (kbps). Ultra-low bitrate is a primary goal of semantic communication.
- **🇪🇸 ES:** La cantidad de datos transmitidos por segundo, típicamente medida en kilobits por segundo (kbps). La tasa de bits ultrabaja es un objetivo principal de la comunicación semántica.

### **Forward Error Correction (FEC)** / **Corrección de Errores Hacia Adelante (FEC)**
- **🇬🇧 EN:** A technique for controlling errors in data transmission where the sender adds redundant data to its messages to allow the receiver to detect and correct errors.
- **🇪🇸 ES:** Una técnica para el control de errores en la transmisión de datos donde el emisor añade datos redundantes a sus mensajes para permitir al receptor detectar y corregir errores.

### **Jitter** / **Jitter**
- **🇬🇧 EN:** The variation in packet arrival time, which can disrupt real-time playback if not managed by a jitter buffer.
- **🇪🇸 ES:** La variación en el tiempo de llegada de los paquetes, que puede interrumpir la reproducción en tiempo real si no es gestionada por un búfer de jitter.

### **Latency** / **Latencia**
- **🇬🇧 EN:** The end-to-end delay in the communication system. For real-time voice, keeping latency under 300 ms is critical.
- **🇪🇸 ES:** El retardo extremo a extremo en el sistema de comunicación. Para la voz en tiempo real, mantener la latencia por debajo de 300 ms es crítico.

### **Packet Loss** / **Pérdida de Paquetes**
- **🇬🇧 EN:** The failure of one or more transmitted data packets to arrive at their destination, causing degradations in conventional codecs but handled via concealment in semantic systems.
- **🇪🇸 ES:** El fallo de uno o más paquetes de datos transmitidos en llegar a su destino, causando degradaciones en códecs convencionales pero manejado mediante ocultación (concealment) en sistemas semánticos.

## Representations

### **Acoustic Tokens** / **Tokens Acústicos**
- **🇬🇧 EN:** Discrete representations that capture the fine acoustic details of the waveform, typically generated using Residual Vector Quantization (RVQ).
- **🇪🇸 ES:** Representaciones discretas que capturan los finos detalles acústicos de la forma de onda, típicamente generadas utilizando Cuantización Vectorial Residual (RVQ).

### **Semantic Tokens** / **Tokens Semánticos**
- **🇬🇧 EN:** Discrete representations derived from deep learning models (like HuBERT or w2v-BERT) that capture the linguistic or phonetic meaning of speech.
- **🇪🇸 ES:** Representaciones discretas derivadas de modelos de aprendizaje profundo (como HuBERT o w2v-BERT) que capturan el significado lingüístico o fonético del habla.

### **Speaker Embedding** / **Embedding de Hablante**
- **🇬🇧 EN:** A continuous vector representation (e.g., ECAPA-TDNN, x-vectors) that encapsulates the unique timbral identity of a speaker.
- **🇪🇸 ES:** Una representación vectorial continua (ej. ECAPA-TDNN, x-vectors) que encapsula la identidad tímbrica única de un hablante.
