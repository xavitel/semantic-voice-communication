# Índice comentado del corpus

> Catálogo de los 29 documentos del repositorio. Los resúmenes están redactados en español a partir del abstract y, cuando ha sido necesario, de las conclusiones del PDF. No son traducciones literales.

## Navegación por tema

- **Códecs neuronales fundamentales:** [01](#01-soundstream-an-end-to-end-neural-audio-codec), [02](#02-high-fidelity-neural-audio-compression), [12](#12-ldcodec-a-high-quality-neural-audio-codec-with-low-complexity-decoder), [13](#13-snac-multi-scale-neural-audio-codec)
- **Tokenización y modelos generativos:** [03](#03-audiolm-a-language-modeling-approach-to-audio-generation), [21](#21-holitok-a-continuous-holistic-tokenization-with-robust-dual-capabilities-of-speech-generation-and-understanding)
- **Identidad, prosodia y emoción:** [04](#04-streamvoiceanon-emotion-preserving-streaming-speaker-anonymization-via-frame-level-acoustic-distillation), [08](#08-a-unified-neural-codec-language-model-for-selective-editable-text-to-speech-generation), [22](#22-hascom-a-heterogeneous-affective-semantic-communication-framework-for-speech-transmission)
- **Streaming y baja latencia:** [05](#05-reconstruct-dont-encode-self-supervised-representation-reconstruction-loss-for-high-intelligibility-and-low-latency-streaming-neural-audio-codec), [11](#11-moshi-a-speech-text-foundation-model-for-real-time-dialogue)
- **Reconstrucción y mejora generativa:** [06](#06-codecflow-efficient-bandwidth-extension-via-conditional-flow-matching-in-neural-codec-latent-space), [07](#07-hierarchical-decoding-for-discrete-speech-synthesis-with-multi-resolution-spoof-detection), [09](#09-voicecraft-x-unifying-multilingual-voice-cloning-speech-synthesis-and-speech-editing)
- **Códecs semánticos y ultra-bajo bitrate:** [10](#10-semanticodec-an-ultra-low-bitrate-semantic-audio-codec-for-general-sound), [16](#16-contextcodec-content-focused-context-guidance-for-ultra-low-bitrate-speech-coding), [17](#17-spg-codec-exploring-the-role-and-boundaries-of-semantic-priors-in-ultra-low-bitrate-neural-speech-coding), [19](#19-entanglecodec-a-unified-discrete-audio-tokenizer-via-semantic-acoustic-entanglement), [20](#20-an-ultra-low-bitrate-neural-speech-codec-with-plain-to-pseudo-synergistic-vector-quantization)
- **Comunicación semántica de voz:** [14](#14-wireless-deep-speech-semantic-transmission), [27](#27-deep-learning-enabled-semantic-communications-with-speech-recognition-and-synthesis), [29](#29-a-novel-semantic-compression-approach-for-ultra-low-bandwidth-voice-communication)
- **Fundamentos y contexto semántico:** [15](#15-token-communications-a-large-model-driven-framework-for-cross-modal-context-aware-semantic-communications), [26](#26-beyond-transmitting-bits-context-semantics-and-task-oriented-communications)
- **Evaluación y límites de representación:** [18](#18-the-wer-trap-shattering-the-illusion-of-unified-tokens-in-speech-language-models), [23](#23-benchmarking-speech-to-text-robustness-in-noisy-emergency-medical-dialogues), [28](#28-low-complexity-acoustic-scene-classification-with-device-information-in-the-dcase-2025-challenge)
- **Robustez de red y transmisión adaptativa:** [24](#24-large-speech-model-enabled-semantic-communication), [25](#25-error-resilient-semantic-communication-for-speech-transmission-over-packet-loss-networks)

## Fichas resumidas

### 01. SoundStream: An End-to-End Neural Audio Codec

- **Autores:** Neil Zeghidour, Alejandro Luebs, Ahmed Omran, Jan Skoglund y Marco Tagliasacchi
- **Año:** 2021
- **Categoría:** Códecs neuronales fundamentales
- **Prioridad:** Núcleo
- **Fuente:** [`SoundStream_An_End-to-End_Neural_Audio_Codec.pdf`](SoundStream_An_End-to-End_Neural_Audio_Codec.pdf)
- **Ficha completa:** [`01_soundstream_an_end_to_end_neural_audio_codec.md`](notes/01_soundstream_an_end_to_end_neural_audio_codec.md)

**Resumen en español.** SoundStream presenta un códec neuronal de audio entrenado de extremo a extremo que combina un encoder y decoder convolucionales con cuantización vectorial residual. El dropout estructurado de los cuantizadores permite operar con un único modelo entre 3 y 18 kbps. A 3 kbps supera subjetivamente a Opus a 12 kbps, se aproxima a EVS a 9,6 kbps y admite ejecución en streaming y en tiempo real sobre CPU móvil.

**Aportación al TFM.** Baseline histórico para medir cuánto aporta una representación semántica respecto a un RVQ puramente acústico.

### 02. High Fidelity Neural Audio Compression

- **Autores:** Alexandre Défossez, Jade Copet, Gabriel Synnaeve y Yossi Adi
- **Año:** 2022
- **Categoría:** Códecs neuronales fundamentales
- **Prioridad:** Núcleo
- **Fuente:** [`High_Fidelity_Neural_Audio_Compression.pdf`](High_Fidelity_Neural_Audio_Compression.pdf)
- **Ficha completa:** [`02_high_fidelity_neural_audio_compression.md`](notes/02_high_fidelity_neural_audio_compression.md)

**Resumen en español.** EnCodec propone un códec neuronal de alta fidelidad y tiempo real con arquitectura encoder-decoder en streaming y espacio latente cuantizado. Introduce un discriminador espectral multiescala y un balanceador de gradientes para estabilizar el entrenamiento. Un pequeño modelo Transformer puede comprimir adicionalmente la representación hasta un 40 %, y las evaluaciones MUSHRA cubren voz, voz ruidosa y reverberante y música entre 1,5 kbps y configuraciones estéreo de mayor tasa.

**Aportación al TFM.** Baseline reproducible y convencional para calidad, bitrate y coste computacional.

### 03. AudioLM: a Language Modeling Approach to Audio Generation

- **Autores:** Zalán Borsos, Raphaël Marinier, Damien Vincent, Eugene Kharitonov, Olivier Pietquin, Matt Sharifi, Dominik Roblek, Olivier Teboul, David Grangier, Marco Tagliasacchi y Neil Zeghidour
- **Año:** 2022
- **Categoría:** Tokenización y modelos generativos
- **Prioridad:** Núcleo
- **Fuente:** [`AudioLM_a_Language_Modeling_Approach_to_Audio_Generation.pdf`](AudioLM_a_Language_Modeling_Approach_to_Audio_Generation.pdf)
- **Ficha completa:** [`03_audiolm_a_language_modeling_approach_to_audio_generation.md`](notes/03_audiolm_a_language_modeling_approach_to_audio_generation.md)

**Resumen en español.** AudioLM formula la generación de audio como modelado de lenguaje sobre tokens discretos. Combina tokens semánticos derivados de un modelo auto-supervisado, que capturan estructura de largo plazo, con tokens acústicos de SoundStream para recuperar alta fidelidad. Sin transcripciones, genera continuaciones de voz plausibles y conserva identidad y prosodia, estableciendo el paradigma jerárquico semántico-acústico que siguen muchos sistemas posteriores.

**Aportación al TFM.** Fundamenta la separación de flujos semánticos y acústicos del diseño objetivo.

### 04. StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation

- **Autores:** Nikita Kuzmin, Kong Aik Lee y Eng Siong Chng
- **Año:** 2026
- **Categoría:** Identidad, prosodia y emoción
- **Prioridad:** Núcleo
- **Fuente:** [`04_StreamVoiceAnon+.pdf`](04_StreamVoiceAnon+.pdf)
- **Ficha completa:** [`04_streamvoiceanon_emotion_preserving_streaming_speaker_anonymizati.md`](notes/04_streamvoiceanon_emotion_preserving_streaming_speaker_anonymizati.md)

**Resumen en español.** StreamVoiceAnon+ estudia la pérdida de emoción en anonimización de voz basada en códecs y modelos de lenguaje. Propone fine-tuning supervisado con pares del mismo hablante y destilación emocional a nivel de frame sobre estados acústicos. Mantiene 180 ms de latencia sin coste adicional de inferencia y mejora la preservación emocional de 39,7 % a 49,2 % UAR, con 5,77 % WER y privacidad cercana al azar en verificación de hablante.

**Aportación al TFM.** Demuestra que la emoción requiere una señal o pérdida explícita y aporta una métrica paralingüística para el benchmark.

### 05. Reconstruct! Don't Encode: Self-Supervised Representation Reconstruction Loss for High-Intelligibility and Low-Latency Streaming Neural Audio Codec

- **Autores:** Junhyeok Lee, Xiluo He, Jihwan Lee, Helin Wang, Shrikanth Narayanan, Thomas Thebaud, Laureano Moro-Velazquez, Jesús Villalba y Najim Dehak
- **Año:** 2026
- **Categoría:** Streaming y baja latencia
- **Prioridad:** Núcleo
- **Fuente:** [`05_JHCodec_Reconstruct_Dont_Encode.pdf`](05_JHCodec_Reconstruct_Dont_Encode.pdf)
- **Ficha completa:** [`05_reconstruct_don_t_encode_self_supervised_representation_reconstr.md`](notes/05_reconstruct_don_t_encode_self_supervised_representation_reconstr.md)

**Resumen en español.** JHCodec cuestiona que destilar representaciones solo en el encoder garantice inteligibilidad tras la decodificación. Introduce una pérdida de reconstrucción de representaciones auto-supervisadas aplicada a la salida reconstruida, que acelera la convergencia, permite entrenar competitivamente con una sola GPU y mejora el contenido recuperado. El enfoque habilita un Transformer streaming sin lookahead y con alta inteligibilidad.

**Aportación al TFM.** Candidato directo para el baseline streaming y para estudiar pérdidas semánticas en el decoder.

### 06. CodecFlow: Efficient Bandwidth Extension via Conditional Flow Matching in Neural Codec Latent Space

- **Autores:** Bowen Zhang, Junchuan Zhao, Ian McLoughlin, Ye Wang y A. S. Madhukumar
- **Año:** 2026
- **Categoría:** Reconstrucción y mejora generativa
- **Prioridad:** Apoyo
- **Fuente:** [`06_CodecFlow.pdf`](06_CodecFlow.pdf)
- **Ficha completa:** [`06_codecflow_efficient_bandwidth_extension_via_conditional_flow_mat.md`](notes/06_codecflow_efficient_bandwidth_extension_via_conditional_flow_mat.md)

**Resumen en español.** CodecFlow realiza extensión de ancho de banda directamente en el espacio latente compacto de un códec neuronal. Combina flow matching condicionado por sonoridad con un RVQ restringido estructuralmente para alinear representaciones de baja y alta resolución. En tareas de 8 a 16 kHz y de 8 a 44,1 kHz mejora fidelidad espectral y calidad perceptual evitando parte del coste de modelar espectrogramas o waveform completos.

**Aportación al TFM.** Referencia para un decoder generativo que recupere detalle acústico no transmitido.

### 07. Hierarchical Decoding for Discrete Speech Synthesis with Multi-Resolution Spoof Detection

- **Autores:** Junchuan Zhao, Minh Duc Vu y Ye Wang
- **Año:** 2026
- **Categoría:** Reconstrucción y mejora generativa
- **Prioridad:** Apoyo
- **Fuente:** [`07_Hierarchical_Decoding_Discrete_Speech.pdf`](07_Hierarchical_Decoding_Discrete_Speech.pdf)
- **Ficha completa:** [`07_hierarchical_decoding_for_discrete_speech_synthesis_with_multi_r.md`](notes/07_hierarchical_decoding_for_discrete_speech_synthesis_with_multi_r.md)

**Resumen en español.** MSpoof-TTS mejora la síntesis discreta sin reentrenar el modelo. Detectores de spoofing sobre tokens y a varias resoluciones temporales puntúan inconsistencias locales; una decodificación jerárquica poda y reordena candidatos. En LibriTTS, LibriSpeech y TwistList incrementa la naturalidad y robustez manteniendo inteligibilidad e identidad del hablante.

**Aportación al TFM.** Opción de mejora del receptor offline y referencia sobre artefactos de tokenización.

### 08. A Unified Neural Codec Language Model for Selective Editable Text to Speech Generation

- **Autores:** Hanchen Pei, Shujie Liu, Yanqing Liu, Jianwei Yu, Yuanhang Qian, Gongping Huang, Sheng Zhao y Yan Lu
- **Año:** 2026
- **Categoría:** Identidad, prosodia y emoción
- **Prioridad:** Apoyo
- **Fuente:** [`08_SpeechEdit_Unified_Neural_Codec_LM.pdf`](08_SpeechEdit_Unified_Neural_Codec_LM.pdf)
- **Ficha completa:** [`08_a_unified_neural_codec_language_model_for_selective_editable_tex.md`](notes/08_a_unified_neural_codec_language_model_for_selective_editable_tex.md)

**Resumen en español.** SpeechEdit amplía el TTS zero-shot con control selectivo de atributos. El modelo reproduce por defecto el perfil acústico completo de un prompt, pero permite sustituir únicamente rasgos indicados explícitamente, como timbre o prosodia. Se entrena con LibriEdit, construido a partir de pares diferenciales de LibriHeavy, y mantiene naturalidad y robustez mientras ofrece control localizado.

**Aportación al TFM.** Apoya una interfaz explícita para separar identidad, contenido y prosodia en la cascada modular.

### 09. VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing

- **Autores:** Zhisheng Zheng, Puyuan Peng, Anuj Diwan, Cong Phuoc Huynh, Xiaohang Sun, Zhu Liu, Vimal Bhat y David Harwath
- **Año:** 2025
- **Categoría:** Reconstrucción y mejora generativa
- **Prioridad:** Apoyo
- **Fuente:** [`09_VoiceCraft-X.pdf`](09_VoiceCraft-X.pdf)
- **Ficha completa:** [`09_voicecraft_x_unifying_multilingual_voice_cloning_speech_synthesi.md`](notes/09_voicecraft_x_unifying_multilingual_voice_cloning_speech_synthesi.md)

**Resumen en español.** VoiceCraft-X unifica edición de voz y TTS zero-shot en once idiomas con un modelo autorregresivo de tokens de códec. Usa Qwen3 para procesar texto entre idiomas sin depender de fonemas y reordena tokens de texto y voz alineados temporalmente. El sistema genera o edita habla natural incluso cuando cada idioma dispone de datos limitados.

**Aportación al TFM.** Candidato de decoder multilingüe y referencia para reconstrucción del hablante a partir de un prompt.

### 10. SemantiCodec: An Ultra Low Bitrate Semantic Audio Codec for General Sound

- **Autores:** Haohe Liu, Xuenan Xu, Yi Yuan, Mengyue Wu, Wenwu Wang y Mark D. Plumbley
- **Año:** 2024
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **Fuente:** [`10_SemantiCodec.pdf`](10_SemantiCodec.pdf)
- **Ficha completa:** [`10_semanticodec_an_ultra_low_bitrate_semantic_audio_codec_for_gener.md`](notes/10_semanticodec_an_ultra_low_bitrate_semantic_audio_codec_for_gener.md)

**Resumen en español.** SemantiCodec combina un encoder semántico AudioMAE discretizado mediante k-means con un encoder acústico residual y un decoder de difusión. Funciona con voz, música y sonido general a 25, 50 o 100 tokens por segundo, equivalentes a 0,31-1,40 kbps. Reporta mejor reconstrucción que Descript y representaciones más informativas semánticamente que otros códecs, incluso con menor tasa.

**Aportación al TFM.** Referencia ultra-low-bitrate y ejemplo claro de separación semántico-acústica.

### 11. Moshi: a speech-text foundation model for real-time dialogue

- **Autores:** Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou, Edouard Grave y Neil Zeghidour
- **Año:** 2024
- **Categoría:** Streaming y baja latencia
- **Prioridad:** Núcleo
- **Fuente:** [`Moshi_a_speech-text_foundation_model_for_real-time_dialogue.pdf`](Moshi_a_speech-text_foundation_model_for_real-time_dialogue.pdf)
- **Ficha completa:** [`11_moshi_a_speech_text_foundation_model_for_real_time_dialogue.md`](notes/11_moshi_a_speech_text_foundation_model_for_real_time_dialogue.md)

**Resumen en español.** Moshi sustituye la cascada VAD-ASR-LLM-TTS por generación speech-to-speech full-duplex. Modela en paralelo la voz del usuario y del sistema mediante tokens del códec Mimi e introduce un monólogo interno de tokens de texto alineados antes de los tokens acústicos. Puede manejar solapamientos e interrupciones y alcanza 160 ms de latencia teórica y aproximadamente 200 ms en la práctica.

**Aportación al TFM.** Baseline streaming principal y fuente de Mimi para la arquitectura end-to-end.

### 12. LDCodec: A High Quality Neural Audio Codec with Low-Complexity Decoder

- **Autores:** Jiawei Jiang, Linping Xu, Dejun Zhang, Qingbo Huang, Xianjun Xia y Yijian Xiao
- **Año:** 2025
- **Categoría:** Códecs neuronales fundamentales
- **Prioridad:** Apoyo
- **Fuente:** [`12_LDCodec.pdf`](12_LDCodec.pdf)
- **Ficha completa:** [`12_ldcodec_a_high_quality_neural_audio_codec_with_low_complexity_de.md`](notes/12_ldcodec_a_high_quality_neural_audio_codec_with_low_complexity_de.md)

**Resumen en español.** LDCodec se orienta a receptores con recursos limitados, especialmente smartphones. Combina una unidad residual ligera, cuantización LSRVQ, discriminadores subband-fullband y pérdidas perceptuales. A 6 kbps supera subjetiva y objetivamente a Opus a 12 kbps reduciendo la complejidad del decoder.

**Aportación al TFM.** Referencia de coste del receptor y despliegue en hardware limitado.

### 13. SNAC: Multi-Scale Neural Audio Codec

- **Autores:** Hubert Siuzdak, Florian Grötschla y Luca A. Lanzendörfer
- **Año:** 2024
- **Categoría:** Códecs neuronales fundamentales
- **Prioridad:** Núcleo
- **Fuente:** [`13_SNAC.pdf`](13_SNAC.pdf)
- **Ficha completa:** [`13_snac_multi_scale_neural_audio_codec.md`](notes/13_snac_multi_scale_neural_audio_codec.md)

**Resumen en español.** SNAC modifica el RVQ convencional permitiendo que cada cuantizador opere a una resolución temporal distinta. La jerarquía multiescala adapta la tasa de tokens a estructuras de diferente duración y mejora la eficiencia sin abandonar una arquitectura sencilla. Las evaluaciones objetivas y subjetivas muestran que esta asignación temporal es más eficiente, y se publican código y pesos.

**Aportación al TFM.** Baseline abierto para comparar token rate, bitrate y granularidad temporal.

### 14. Wireless Deep Speech Semantic Transmission

- **Autores:** Zixuan Xiao, Shengshi Yao, Jincheng Dai, Sixian Wang, Kai Niu y Ping Zhang
- **Año:** 2022
- **Categoría:** Comunicación semántica de voz
- **Prioridad:** Núcleo
- **Fuente:** [`14_Wireless_Deep_Speech_Semantic_Transmission.pdf`](14_Wireless_Deep_Speech_Semantic_Transmission.pdf)
- **Ficha completa:** [`14_wireless_deep_speech_semantic_transmission.md`](notes/14_wireless_deep_speech_semantic_transmission.md)

**Resumen en español.** DSST aprende una transformación no lineal de la voz a un espacio semántico y un encoder conjunto fuente-canal. Un modelo entrópico estima la importancia desigual de las características para asignar tasas distintas, mientras un mecanismo adaptativo permite usar un único modelo a diversos SNR. Frente a sistemas convencionales y semánticos previos mejora métricas objetivas y subjetivas y ahorra hasta un 75 % de ancho de banda a igual calidad.

**Aportación al TFM.** Fundamenta el eje comunicación, adaptación a SNR y rate-distortion del TFM.

### 15. Token Communications: A Large Model-Driven Framework for Cross-Modal Context-Aware Semantic Communications

- **Autores:** Li Qiao, Mahdi Boloursaz Mashhadi, Zhen Gao, Rahim Tafazolli, Mehdi Bennis y Dusit Niyato
- **Año:** 2025
- **Categoría:** Fundamentos y contexto semántico
- **Prioridad:** Apoyo
- **Fuente:** [`15_TokCom_Context_Aware_Semantic_Communications.pdf`](15_TokCom_Context_Aware_Semantic_Communications.pdf)
- **Ficha completa:** [`15_token_communications_a_large_model_driven_framework_for_cross_mo.md`](notes/15_token_communications_a_large_model_driven_framework_for_cross_mo.md)

**Resumen en español.** TokCom propone que la unidad de comunicación sea el token procesado por modelos fundacionales y multimodales. El contexto entre modalidades permite al transmisor y al receptor omitir o reconstruir información redundante. El trabajo formula oportunidades, principios y retos en varias capas de red y demuestra en un escenario de imagen que explotar dependencias contextuales mejora la eficiencia de ancho de banda.

**Aportación al TFM.** Aporta el concepto de contexto compartido y caché semántica como extensión futura.

### 16. ContextCodec: Content-Focused Context Guidance for Ultra-Low Bitrate Speech Coding

- **Autores:** Chengbin Liang, Wenqi Guo, Hao Cao y Zhijin Qin
- **Año:** 2026
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **Fuente:** [`16_ContextCodec.pdf`](16_ContextCodec.pdf)
- **Ficha completa:** [`16_contextcodec_content_focused_context_guidance_for_ultra_low_bitr.md`](notes/16_contextcodec_content_focused_context_guidance_for_ultra_low_bitr.md)

**Resumen en español.** ContextCodec prioriza el mensaje lingüístico cuando el bitrate cae por debajo de 1 kbps. Separa una rama acústica de otra de contexto alineada con fonemas mediante una pérdida contrastiva tipo CLIP y reduce la fuga de información paralingüística. El decoder recibe esta guía en todas sus etapas y un refinador latente autorregresivo permite alcanzar un compromiso sólido a 500 bps, con RTF 0,4886 en CPU móvil.

**Aportación al TFM.** Candidato ultra-low-bitrate y evidencia para separar contenido de atributos paralingüísticos.

### 17. SPG-Codec: Exploring the Role and Boundaries of Semantic Priors in Ultra-Low-Bitrate Neural Speech Coding

- **Autores:** Mingyu Zhao, Zijian Lin, Kun Wei y Zhiyong Wu
- **Año:** 2026
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **Fuente:** [`17_SPG_Codec.pdf`](17_SPG_Codec.pdf)
- **Ficha completa:** [`17_spg_codec_exploring_the_role_and_boundaries_of_semantic_priors_i.md`](notes/17_spg_codec_exploring_the_role_and_boundaries_of_semantic_priors_i.md)

**Resumen en español.** SPG-Codec analiza de forma sistemática cuándo ayudan los priors congelados HuBERT y Whisper. A 1,5 kbps pueden reducir relativamente el WER alrededor de un 10 %, pero el beneficio desaparece al superar aproximadamente 6 kbps, fenómeno denominado Semantic Retirement. HuBERT conserva mejor prosodia y timbre, mientras Whisper reduce alucinaciones fonéticas en ruido; una regulación dependiente del bitrate equilibra naturalidad y consistencia.

**Aportación al TFM.** Justifica una selección de prior dependiente del bitrate y ablaciones semántico-acústicas.

### 18. The WER Trap: Shattering the Illusion of Unified Tokens in Speech Language Models

- **Autores:** Xiangyu Zhang, Yuxin Li, Haoyang Zhang, Shiqi Han, Hexin Liu, Qiquan Zhang, Beena Ahmed y Julien Epps
- **Año:** 2026
- **Categoría:** Evaluación y límites de representación
- **Prioridad:** Núcleo
- **Fuente:** [`18_The_WER_Trap.pdf`](18_The_WER_Trap.pdf)
- **Ficha completa:** [`18_the_wer_trap_shattering_the_illusion_of_unified_tokens_in_speech.md`](notes/18_the_wer_trap_shattering_the_illusion_of_unified_tokens_in_speech.md)

**Resumen en español.** The WER Trap demuestra que un tokenizer puede alcanzar WER bajo y, aun así, producir voz acústicamente ininteligible. Mediante compresión dinámica alineada con fronteras semánticas aísla tokens casi puramente lingüísticos; incluso con duraciones oráculo, los generadores pierden articulación y microdinámica. El resultado cuestiona la idea de un token único para comprensión y generación y defiende representaciones explícitamente desacopladas.

**Aportación al TFM.** Obliga a evaluar WER junto con calidad, speaker similarity, prosodia y escucha humana.

### 19. EntangleCodec: A Unified Discrete Audio Tokenizer via Semantic-Acoustic Entanglement

- **Autores:** Hui Li, Yangfan Gao, Junlin Shang, Changhao Jiang, Tao Gui, Qi Zhang y Xuanjing Huang
- **Año:** 2026
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **Fuente:** [`19_EntangleCodec.pdf`](19_EntangleCodec.pdf)
- **Ficha completa:** [`19_entanglecodec_a_unified_discrete_audio_tokenizer_via_semantic_ac.md`](notes/19_entanglecodec_a_unified_discrete_audio_tokenizer_via_semantic_ac.md)

**Resumen en español.** EntangleCodec busca un único flujo discreto útil tanto para comprensión como para generación. Antes de cuantizar, alinea audio con captions ricas que incluyen contenido, identidad, emoción, prosodia y escena; un decoder de difusión con flow matching recupera voz, música y sonido general. Iguala la reconstrucción de códecs especializados, mejora hasta 7,4 puntos MMAR y permite que modelos de audio pequeños superen sistemas mucho mayores.

**Aportación al TFM.** Contrapunto directo al desacoplamiento defendido por The WER Trap y candidato para comprensión+generación.

### 20. An Ultra-Low-Bitrate Neural Speech Codec with Plain-to-Pseudo Synergistic Vector Quantization

- **Autores:** Xiao-Hang Jiang, Yang Ai, Fei Liu, Rui-Chen Zheng, Jian-Qing Gao, Zhen-Hua Ling y Ji Wu
- **Año:** 2026
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **Fuente:** [`20_P2PSynCodec.pdf`](20_P2PSynCodec.pdf)
- **Ficha completa:** [`20_an_ultra_low_bitrate_neural_speech_codec_with_plain_to_pseudo_sy.md`](notes/20_an_ultra_low_bitrate_neural_speech_codec_with_plain_to_pseudo_sy.md)

**Resumen en español.** P2PSynCodec observa que las últimas capas de un RVQ consumen el mismo bitrate aunque aporten cada vez menos. Sustituye esos códigos transmitidos por pseudo-tokens predichos en el receptor: solo un cuantizador básico genera bits y varios pseudo-cuantizadores reconstruyen detalle sin coste de transmisión. A 0,5 kbps alcanza una calidad comparable a códecs rivales de 2 kbps.

**Aportación al TFM.** Ejemplo directo de recuperación generativa para reducir payload y candidato ultra-low-bitrate.

### 21. HoliTok: A Continuous Holistic Tokenization with Robust Dual Capabilities of Speech Generation and Understanding

- **Autores:** Bohan Li, Shi Lian, Hankun Wang, Yiwei Guo, Yu Xi, Zhihan Li, Da Zheng, Colin Zhang y Kai Yu
- **Año:** 2026
- **Categoría:** Tokenización y modelos generativos
- **Prioridad:** Núcleo
- **Fuente:** [`21_HoliTok.pdf`](21_HoliTok.pdf)
- **Ficha completa:** [`21_holitok_a_continuous_holistic_tokenization_with_robust_dual_capa.md`](notes/21_holitok_a_continuous_holistic_tokenization_with_robust_dual_capa.md)

**Resumen en español.** HoliTok propone una representación continua común para generación y comprensión. Codifica voz de 48 kHz en secuencias de 25 Hz y 128 dimensiones mediante entrenamiento progresivo que preserva señal, incorpora semántica y mantiene facilidad de modelado. Sobre ella construye un sistema AR+DiT que realiza síntesis y reconocimiento; entre las representaciones comparadas es la única que funciona de forma robusta en la arquitectura unificada sin trucos adicionales.

**Aportación al TFM.** Referencia de representación unificada y advertencia sobre convertir frame rate en bitrate real.

### 22. HASCom: A Heterogeneous Affective-Semantic Communication Framework for Speech Transmission

- **Autores:** Zhenjia Yu, Taojie Zhu, Md Arman Hossain, Zineb Zbarna y Lei Wang
- **Año:** 2026
- **Categoría:** Identidad, prosodia y emoción
- **Prioridad:** Núcleo
- **Fuente:** [`22_HASCom_Affective_Semantic_Communication.pdf`](22_HASCom_Affective_Semantic_Communication.pdf)
- **Ficha completa:** [`22_hascom_a_heterogeneous_affective_semantic_communication_framewor.md`](notes/22_hascom_a_heterogeneous_affective_semantic_communication_framewor.md)

**Resumen en español.** HASCom separa la información lingüística y afectiva en dos canales heterogéneos. Los fonemas discretos se protegen digitalmente con LDPC para garantizar recuperación, mientras embeddings emocionales continuos viajan mediante JSCC analógico para evitar cuantización irreversible y cliff effect. Un decoder de difusión guiado por semántica y emoción supera baselines en AWGN y Rayleigh a SNR bajo, con menos de 0,1 ms en los módulos JSCC.

**Aportación al TFM.** Arquitectura de referencia para transmitir emoción como side-channel protegido de manera diferenciada.

### 23. Benchmarking Speech-to-Text Robustness in Noisy Emergency Medical Dialogues

- **Autores:** Denis Moser, Nikola Stanic y Murat Sariyar
- **Año:** 2025
- **Categoría:** Evaluación y límites de representación
- **Prioridad:** Apoyo
- **Fuente:** [`23_ASR_Robustness_Acoustic_Conditions_Benchmark.pdf`](23_ASR_Robustness_Acoustic_Conditions_Benchmark.pdf)
- **Ficha completa:** [`23_benchmarking_speech_to_text_robustness_in_noisy_emergency_medica.md`](notes/23_benchmarking_speech_to_text_robustness_in_noisy_emergency_medica.md)

**Resumen en español.** Este benchmark evalúa seis sistemas STT en 99 diálogos médicos sintéticos mezclados con cuatro tipos de ruido y cinco SNR, generando 1.980 audios. Combina WER, WER médico, BLEU, similitud TF-IDF y embeddings semánticos. Recapp obtiene el mejor resultado global; entre modelos abiertos, Whisper v3 Turbo equilibra exactitud y eficiencia y Whisper v3 Large conserva mejor el significado. El ruido de espacios interiores concurridos es el más perjudicial.

**Aportación al TFM.** Plantilla metodológica para evaluar ASR bajo ruido y usar métricas semánticas complementarias.

### 24. Large Speech Model Enabled Semantic Communication

- **Autores:** Yun Tian, Zhijin Qin, Guocheng Lv, Ye Jin, Kaibin Huang y Zhu Han
- **Año:** 2025
- **Categoría:** Robustez de red y transmisión adaptativa
- **Prioridad:** Núcleo
- **Fuente:** [`24_LargeSC.pdf`](24_LargeSC.pdf)
- **Ficha completa:** [`24_large_speech_model_enabled_semantic_communication.md`](notes/24_large_speech_model_enabled_semantic_communication.md)

**Resumen en español.** LargeSC integra Mimi como tokenizer, un controlador que adapta la tasa y aplica protección desigual dentro del flujo y Moshi ajustado con LoRA para recuperar tokens perdidos. El sistema responde al contenido, la probabilidad de pérdida y el presupuesto de ancho de banda. Opera entre 550 bps y 2,06 kbps, mejora la calidad frente a baselines con pérdidas altas y alcanza aproximadamente 460 ms extremo a extremo.

**Aportación al TFM.** Arquitectura objetivo para el experimento de packet loss, adaptación y recuperación.

### 25. Error-Resilient Semantic Communication for Speech Transmission over Packet-Loss Networks

- **Autores:** Zhuohang Han, Jincheng Dai, Shengshi Yao, Junyi Wang, Yanlong Li, Kai Niu, Wenjun Xu y Ping Zhang
- **Año:** 2025
- **Categoría:** Robustez de red y transmisión adaptativa
- **Prioridad:** Núcleo
- **Fuente:** [`25_Glaris_Error_Resilient_Speech_SemCom.pdf`](25_Glaris_Error_Resilient_Speech_SemCom.pdf)
- **Ficha completa:** [`25_error_resilient_semantic_communication_for_speech_transmission_o.md`](notes/25_error_resilient_semantic_communication_for_speech_transmission_o.md)

**Resumen en español.** Glaris introduce un códec semántico resiliente que opera en el espacio latente generativo y sigue siendo compatible con redes digitales existentes. Priors generativos permiten ocultar paquetes perdidos equilibrando coherencia y fidelidad, y un mecanismo integrado limita la propagación de errores. En LibriSpeech supera códecs resilientes y reduce la redundancia frente a FEC tradicional, acercándose a la robustez de JSCC.

**Aportación al TFM.** Referencia principal para diseñar packetización, concealment y comparación con FEC.

### 26. Beyond Transmitting Bits: Context, Semantics, and Task-Oriented Communications

- **Autores:** Deniz Gündüz, Zhijin Qin, Inaki Estella Aguerri, Harpreet S. Dhillon, Zhaohui Yang, Aylin Yener, Kai Kit Wong y Chan-Byoung Chae
- **Año:** 2022
- **Categoría:** Fundamentos y contexto semántico
- **Prioridad:** Núcleo
- **Fuente:** [`26_Beyond_Transmitting_Bits.pdf`](26_Beyond_Transmitting_Bits.pdf)
- **Ficha completa:** [`26_beyond_transmitting_bits_context_semantics_and_task_oriented_com.md`](notes/26_beyond_transmitting_bits_context_semantics_and_task_oriented_com.md)

**Resumen en español.** Este tutorial reorienta el diseño de comunicaciones desde la reproducción fiable de bits hacia el significado, la tarea y el contexto de uso. Revisa fundamentos de teoría de la información, aprendizaje, comunicaciones semánticas y task-oriented, y explica por qué el receptor puede necesitar una inferencia o acción correcta en vez de una copia exacta del mensaje. También identifica problemas abiertos de definición de semántica, métricas y conocimiento compartido.

**Aportación al TFM.** Base conceptual para definir semántica, utilidad y objetivos del sistema de voz.

### 27. Deep Learning Enabled Semantic Communications with Speech Recognition and Synthesis

- **Autores:** Zhenzi Weng, Zhijin Qin, Xiaoming Tao, Chengkang Pan, Guangyi Liu y Geoffrey Ye Li
- **Año:** 2022
- **Categoría:** Comunicación semántica de voz
- **Prioridad:** Núcleo
- **Fuente:** [`27_DeepSC_ST_Speech_Recognition_and_Synthesis.pdf`](27_DeepSC_ST_Speech_Recognition_and_Synthesis.pdf)
- **Ficha completa:** [`27_deep_learning_enabled_semantic_communications_with_speech_recogn.md`](notes/27_deep_learning_enabled_semantic_communications_with_speech_recogn.md)

**Resumen en español.** DeepSC-ST trata reconocimiento y síntesis como las tareas de una comunicación semántica de voz. Un encoder conjunto semántico-canal transmite características orientadas a recuperar texto; el receptor sintetiza voz con ese texto y la información del hablante. Un único modelo robusto opera en diversas condiciones de canal y supera sistemas convencionales y otros enfoques deep-learning, especialmente a SNR bajo; el trabajo incluye una demo de prueba de concepto.

**Aportación al TFM.** Antecedente más directo de la cascada ASR + identidad + TTS propuesta como baseline.

### 28. Low-Complexity Acoustic Scene Classification with Device Information in the DCASE 2025 Challenge

- **Autores:** Florian Schmid, Paul Primus, Toni Heittola, Annamaria Mesaros, Irene Martín-Morató y Gerhard Widmer
- **Año:** 2025
- **Categoría:** Evaluación y límites de representación
- **Prioridad:** Periférico
- **Fuente:** [`28_DCASE_2025_Low_Complexity_Acoustic_Scene_Classification.pdf`](28_DCASE_2025_Low_Complexity_Acoustic_Scene_Classification.pdf)
- **Ficha completa:** [`28_low_complexity_acoustic_scene_classification_with_device_informa.md`](notes/28_low_complexity_acoustic_scene_classification_with_device_informa.md)

**Resumen en español.** El trabajo describe la tarea DCASE 2025 de clasificación de escenas acústicas con restricciones de complejidad, pocos datos y desajuste entre dispositivos. La información del dispositivo está disponible en inferencia, permitiendo adaptación específica: el baseline pasa de 50,72 % a 51,89 %, y la mejor propuesta supera al baseline en más de ocho puntos. También resume avances en destilación, poda y arquitecturas ligeras.

**Aportación al TFM.** Referencia metodológica para complejidad, adaptación al hardware y reporting reproducible.

### 29. A Novel Semantic Compression Approach for Ultra-Low Bandwidth Voice Communication

- **Autores:** Ryan Collette, Ross Greenwood y Serena Nicoll
- **Año:** 2025
- **Categoría:** Comunicación semántica de voz
- **Prioridad:** Núcleo
- **Fuente:** [`29_Semantic_Compression_Ultra_Low_Bandwidth_Voice.pdf`](29_Semantic_Compression_Ultra_Low_Bandwidth_Voice.pdf)
- **Ficha completa:** [`29_a_novel_semantic_compression_approach_for_ultra_low_bandwidth_vo.md`](notes/29_a_novel_semantic_compression_approach_for_ultra_low_bandwidth_vo.md)

**Resumen en español.** Este trabajo explota representaciones factoriales de modelos generativos para transmitir únicamente subconjuntos de tokens relevantes para cada tarea y reutilizar una codificación auxiliar de timbre. Obtiene resultados iguales o mejores que códecs existentes en transcripción, sentimiento y verificación de hablante usando entre dos y cuatro veces menos bitrate; además supera a EnCodec en calidad perceptual y speaker verification con hasta cuatro veces menos tasa.

**Aportación al TFM.** Demuestra el valor de separar información estática de hablante y payload dinámico, muy alineado con la hipótesis modular.
