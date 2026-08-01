# Capítulo 2. Estado del arte

> **Estado:** borrador de trabajo.
> **Corpus:** 29 documentos disponibles en `papers/`.
> **Fecha de corte:** julio de 2026.
> **Trazabilidad:** las claves `[@...]` remiten a `references.bib`; la evidencia tabulada está en `papers/paper_matrix.csv`.

## 2.1. Alcance y método de revisión

Este capítulo estudia la posibilidad de sustituir una transmisión de voz centrada en la fidelidad de la forma de onda por otra que preserve la información necesaria para una interacción humana útil. En este contexto, *semántica* no se limita al texto reconocido: comprende el contenido lingüístico, la identidad del hablante, la prosodia, la emoción y, cuando la aplicación lo requiere, el contexto y la finalidad de la comunicación.

La revisión se organiza como una síntesis narrativa estructurada. El corpus se ha clasificado en siete familias: fundamentos de comunicación semántica; códecs neuronales; tokenización semántico-acústica; transmisión semántica de voz; generación y control de atributos; streaming; y robustez/evaluación. Para cada trabajo se han extraído representación, bitrate, latencia, métricas, canal, disponibilidad de código, principal resultado y limitaciones. Esta normalización es necesaria porque los artículos no utilizan un protocolo común y, por tanto, cifras como WER, MOS o bitrate no siempre son directamente comparables.

La revisión responde a cuatro preguntas:

1. ¿Qué representación ofrece el mejor compromiso entre bitrate, inteligibilidad y naturalidad?
2. ¿Cómo pueden preservarse identidad, prosodia y emoción sin retransmitir toda la señal?
3. ¿Cómo se degrada la comunicación ante ruido, pérdidas de paquetes y variación del canal?
4. ¿Qué protocolo permite comparar una cascada modular y un códec neuronal streaming de forma reproducible?

## 2.2. De transmitir bits a transmitir utilidad

La teoría clásica separa compresión de fuente y protección de canal y considera correcto el sistema cuando el receptor reproduce los bits enviados. Esta abstracción ha permitido construir redes generales y eficientes, pero ignora para qué se utilizará el mensaje. Gündüz et al. distinguen entre exactitud de bits, contenido semántico y utilidad de tarea, y muestran que muchos sistemas futuros solo necesitan que el receptor realice la inferencia o acción adecuada [@gunduz2022beyondbits].

Esta idea modifica la función objetivo de un sistema de voz. Un error de waveform puede ser irrelevante si la frase, el hablante y la intención se preservan; en cambio, una reconstrucción perceptualmente limpia puede fracasar si cambia una negación, una emoción o la identidad. La eficiencia debe expresarse, por tanto, como calidad o utilidad por bit, sujeta a restricciones de latencia y cómputo.

TokCom amplía el planteamiento mediante contexto compartido y tokens multimodales [@qiao2025tokcom]. Si transmisor y receptor comparten información previa, una parte del mensaje puede inferirse en lugar de enviarse. No obstante, su demostración principal se realiza con imágenes, por lo que en voz aún deben medirse el coste de mantener contexto sincronizado, los fallos por contexto incorrecto y la latencia de los modelos fundacionales.

## 2.3. Códecs neuronales: de la waveform a los tokens

### 2.3.1. SoundStream y EnCodec

SoundStream consolida la arquitectura encoder-RVQ-decoder entrenada de extremo a extremo [@zeghidour2021soundstream]. El encoder reduce temporalmente la señal, el RVQ representa el latente mediante varios codebooks y el decoder sintetiza audio. El dropout estructurado permite un único modelo entre 3 y 18 kbps. A 3 kbps, SoundStream supera subjetivamente a Opus a 12 kbps y se aproxima a EVS a 9,6 kbps, además de funcionar en streaming sobre CPU móvil.

EnCodec adopta una estructura similar e introduce un discriminador espectral multiescala y un balanceador de gradientes [@defossez2022encodec]. Sus modelos cubren voz y música a diferentes tasas, desde 1,5 kbps en voz mono. Un pequeño Transformer puede modelar la entropía de los tokens y reducir hasta un 40 % el bitrate, aunque el contexto adicional puede ser problemático para aplicaciones de latencia estricta.

Ambos trabajos demuestran que los códecs aprendidos superan a referencias clásicas en regímenes de baja tasa. Sin embargo, optimizan principalmente reconstrucción acústica. Cuando el cuello de botella es extremo, el modelo puede gastar capacidad en detalle perceptual y perder contenido lingüístico, o conservar fonemas sin mantener atributos paralingüísticos.

### 2.3.2. Granularidad temporal y complejidad

SNAC permite que distintos cuantizadores operen a diferentes frame rates [@siuzdak2024snac]. Esta jerarquía reconoce que ritmo, fonética y textura acústica evolucionan a escalas distintas. Su disponibilidad abierta lo convierte en un baseline adecuado para estudiar la relación entre tasa de tokens y reconstrucción.

LDCodec aborda otro límite práctico: el coste del receptor [@jiang2025ldcodec]. Con cuantización residual de corto y largo plazo y un decoder ligero, supera a Opus a 12 kbps trabajando a 6 kbps. Aunque la tasa es alta para el objetivo de este TFM, introduce una dimensión que suele omitirse: una mejora de bitrate no es útil si el decoder no puede ejecutarse en el dispositivo objetivo.

## 2.4. Tokens semánticos y acústicos

### 2.4.1. El paradigma jerárquico

AudioLM separa tokens semánticos derivados de aprendizaje auto-supervisado y tokens acústicos de SoundStream [@borsos2022audiolm]. Los primeros mantienen estructura lingüística de largo plazo; los segundos recuperan fidelidad, identidad y prosodia. Este esquema estableció un patrón recurrente: transmitir o generar primero una representación de baja frecuencia rica en contenido y después completar el detalle acústico.

SemantiCodec traslada la misma intuición a un códec ultra-low-bitrate [@liu2024semanticodec]. Un encoder AudioMAE produce tokens semánticos, otro captura residuos acústicos y un decoder de difusión reconstruye audio. Sus variantes operan entre 0,31 y 1,40 kbps y mejoran a Descript en la evaluación presentada. Su principal inconveniente para conversación es la difusión, que ofrece calidad a costa de inferencia iterativa y ausencia de una garantía streaming.

### 2.4.2. Cómo asignar los pocos bits disponibles

ContextCodec prioriza explícitamente el contenido a menos de 1 kbps [@liang2026contextcodec]. Una rama alineada con fonemas mediante aprendizaje contrastivo guía todas las etapas del decoder, mientras una rama separada conserva información acústica. A 500 bps alcanza un compromiso favorable y RTF inferior a uno en CPU móvil. La decisión de reducir fuga paralingüística protege inteligibilidad, pero hace necesario un side-channel si el sistema debe conservar identidad o emoción.

SPG-Codec estudia cuándo compensa introducir priors congelados [@zhao2026spgcodec]. HuBERT retiene más prosodia y timbre, mientras Whisper reduce alucinaciones fonéticas y generaliza mejor en ruido. A 1,5 kbps los priors reducen el WER aproximadamente un 10 % relativo, pero su ventaja desaparece cerca de 6 kbps. Este *Semantic Retirement* indica que la intensidad del prior debe depender de la tasa.

P2PSynCodec reduce el payload transmitiendo un solo flujo VQ y prediciendo pseudo-tokens adicionales en el receptor [@jiang2026p2psyncodec]. Reporta a 0,5 kbps una calidad similar a alternativas de 2 kbps. El resultado respalda el uso de priors generativos, aunque aumenta el riesgo de que el receptor invente detalle cuando la entrada está fuera de distribución.

### 2.4.3. ¿Unificar o desacoplar?

The WER Trap cuestiona que exista un token único óptimo para comprensión y generación [@zhang2026wertrap]. Sus tokens ultracomprimidos conservan un WER bajo, pero la síntesis resultante pierde articulación incluso con duraciones oráculo. El contenido categórico útil para ASR no contiene necesariamente las trayectorias fonéticas continuas que necesita un generador.

EntangleCodec presenta la tesis opuesta: alinear audio con captions ricas antes de cuantizar puede producir un flujo único con contenido, identidad, emoción, prosodia y escena [@li2026entanglecodec]. Reporta reconstrucción competitiva, mejoras de hasta 7,4 puntos en MMAR y buenos resultados en comprensión y generación. La diferencia entre ambos trabajos no debe resolverse solo mediante WER: es necesario comparar calidad, speaker similarity, prosodia, coste y robustez con un protocolo común.

HoliTok explora una tercera vía mediante latentes continuos de 25 Hz y 128 dimensiones [@li2026holitok]. La misma secuencia funciona en síntesis y reconocimiento dentro de una arquitectura AR+DiT. No obstante, una frecuencia de vectores no equivale a bitrate: para una evaluación de comunicaciones habría que cuantizar, serializar y medir el payload real.

## 2.5. Comunicación semántica de voz extremo a extremo

DSST combina una transformación semántica, codificación conjunta fuente-canal y asignación de tasa según importancia [@xiao2022dsst]. Un mecanismo de adaptación a SNR permite utilizar el mismo modelo en varios estados de canal. Los autores reportan hasta un 75 % menos ancho de banda que sistemas semánticos anteriores a calidad equivalente. Su limitación práctica es la compatibilidad: los esquemas JSCC no encajan directamente con pilas digitales paquetizadas.

DeepSC-ST adopta una descomposición orientada a tarea [@weng2022deepscst]. El transmisor envía características suficientes para reconocer texto; el receptor combina la transcripción y la información del hablante para sintetizar voz. El sistema mejora a referencias convencionales especialmente a SNR bajo, pero la interfaz textual puede eliminar ritmo, énfasis y emoción. Esta arquitectura es el antecedente directo del baseline modular de este TFM.

Collette et al. separan tokens relevantes para tareas y una codificación de timbre reutilizable [@collette2025semanticcompression]. El sistema iguala o supera a códecs comparados en transcripción, sentimiento y verificación de hablante con dos a cuatro veces menos bitrate. La identidad estática no necesita repetirse en cada trama, pero una corrupción del embedding puede persistir y deben definirse actualizaciones o recuperación.

## 2.6. Preservación de identidad, prosodia y emoción

La naturalidad de una conversación depende de información que el texto no contiene. SpeechEdit demuestra que un modelo de tokens de códec puede reproducir un perfil acústico y sustituir selectivamente atributos indicados por el usuario [@pei2026speechedit]. VoiceCraft-X unifica TTS, clonación y edición en once idiomas mediante tokens de texto y voz alineados [@zheng2025voicecraftx]. Ambos son candidatos de decoder, aunque no están optimizados como códecs ni para latencia de conversación.

StreamVoiceAnon+ muestra que los tokens de contenido tienden a descartar emoción y que el modelo acústico converge hacia patrones dominantes [@kuzmin2026streamvoiceanonplus]. La destilación emocional a nivel de frame eleva UAR de 39,7 % a 49,2 % con 180 ms y sin sobrecoste de inferencia. La evidencia apoya una conclusión de diseño: la emoción debe aparecer en la representación, en la pérdida o en un canal auxiliar; no puede darse por preservada.

HASCom materializa esa separación [@yu2026hascom]. Los fonemas discretos reciben protección LDPC, mientras embeddings emocionales continuos se transmiten mediante JSCC analógico. Un decoder de difusión condicionado combina ambos. El sistema mejora similitud y MOS en AWGN y Rayleigh a SNR bajo. La cifra inferior a 0,1 ms corresponde a los módulos JSCC, no al pipeline completo, por lo que la latencia generativa debe medirse de extremo a extremo.

## 2.7. Reconstrucción generativa en el receptor

Cuando se transmiten pocos bits, el decoder debe inferir información ausente. CodecFlow demuestra que la extensión de banda puede realizarse en el latente de un códec mediante flow matching, con buena fidelidad espectral en 8→16 kHz y 8→44,1 kHz [@zhang2026codecflow]. Este mecanismo podría recuperar detalle acústico que no cabe en el canal.

MSpoof-TTS actúa sobre otro fallo: tokens localmente inconsistentes generados por modelos autorregresivos [@zhao2026mspooftts]. Detectores multirresolución guían una búsqueda jerárquica y mejoran naturalidad sin reentrenar. El coste de generar y reordenar candidatos, sin embargo, lo hace más adecuado para una referencia offline que para el primer prototipo en tiempo real.

Toda recuperación generativa introduce un riesgo semántico: el audio puede sonar bien y contener fonemas, énfasis o identidad inventados. Por ello, la calidad perceptual debe combinarse con métricas de contenido y consistencia.

## 2.8. Streaming y diálogo en tiempo real

Moshi reemplaza la cascada VAD-ASR-LLM-TTS por un modelo speech-to-speech full-duplex [@defossez2024moshi]. Mimi transforma la voz en tokens; flujos paralelos modelan usuario y sistema; y un monólogo interno genera texto alineado antes que audio. La arquitectura admite interrupciones y solapamientos con 160 ms teóricos y cerca de 200 ms prácticos. Para este TFM, Mimi constituye el baseline end-to-end más relevante, aunque el sistema Moshi completo excede el objetivo de un códec.

JHCodec busca inteligibilidad sin lookahead [@lee2026jhcodec]. Su pérdida SSRR reconstruye representaciones auto-supervisadas desde el audio decodificado, en lugar de limitarse a destilar el encoder. Esto mejora convergencia e inteligibilidad y permite entrenamiento competitivo con una GPU. La comparación con Mimi debe incluir no solo WER y calidad, sino algoritmo de buffering, tamaño de ventana y latencia percentil 95.

## 2.9. Robustez frente a ruido y packet loss

El ruido acústico y la pérdida de paquetes son problemas distintos. El benchmark médico de Moser et al. mezcla 99 diálogos con cuatro ruidos y cinco SNR y muestra que la clasificación de sistemas cambia según WER, términos críticos, BLEU o similitud semántica [@moser2025asrrobustness]. Whisper v3 Turbo ofrece un compromiso competitivo entre exactitud y eficiencia, mientras Whisper v3 Large preserva mejor el significado. El resultado refuerza el uso de varias métricas y condiciones realistas.

Glaris opera sobre pérdidas de paquetes y mantiene compatibilidad con redes digitales [@han2025glaris]. Priors generativos realizan concealment en el latente y un mecanismo integrado limita la propagación de errores. Frente a FEC, reduce redundancia y se acerca a la robustez de JSCC. Debe comprobarse si la recuperación conserva el mensaje o solo la plausibilidad acústica.

LargeSC combina Mimi, control adaptativo, protección desigual y Moshi ajustado mediante LoRA [@tian2025largesc]. Opera entre 550 bps y 2,06 kbps y mejora la calidad bajo pérdida alta, pero su latencia aproximada de 460 ms supera el objetivo de 300 ms. Es la referencia principal para diseñar el experimento de protección diferenciada y recuperación generativa.

## 2.10. Evaluación: evitar una métrica única

La literatura utiliza configuraciones heterogéneas. Para evitar conclusiones engañosas, el benchmark debe cubrir:

- **Payload:** bits realmente transmitidos por segundo, incluyendo índices de codebook, cabeceras, embeddings periódicos y FEC.
- **Contenido:** WER/CER y similitud semántica de la transcripción reconstruida.
- **Identidad:** similitud coseno de embeddings ECAPA-TDNN y, cuando proceda, EER.
- **Prosodia:** correlación y error de F0, energía y duraciones.
- **Emoción:** UAR de un clasificador y escucha subjetiva.
- **Calidad:** UTMOS/DNSMOS como aproximación y MOS humano en un subconjunto.
- **Tiempo real:** latencia extremo a extremo, RTF, memoria y percentil 95.
- **Robustez:** degradación respecto al canal limpio bajo ruido, pérdida aleatoria, ráfagas y jitter.

The WER Trap impide usar WER como sustituto de naturalidad [@zhang2026wertrap], y el benchmark ASR muestra que incluso la fidelidad lingüística requiere varias métricas [@moser2025asrrobustness]. Como referencia periférica, DCASE 2025 ofrece buenas prácticas para reportar complejidad, adaptación a dispositivo y uso de datos externos [@schmid2025dcase].

## 2.11. Síntesis de brechas

La revisión identifica cinco brechas:

1. **Compresión frente a expresividad.** Los sistemas que priorizan texto logran tasas muy bajas, pero tienden a perder identidad, prosodia y emoción.
2. **Token unificado frente a flujos separados.** No existe evidencia comparable que determine cuándo conviene entrelazar atributos y cuándo desacoplarlos.
3. **Latencia incompleta.** Varios trabajos reportan RTF o latencia de un módulo, no captura, buffering, red y reproducción extremo a extremo.
4. **Canal idealizado.** Muchos códecs se evalúan sin paquetización; los sistemas robustos usan modelos de pérdidas y overhead diferentes.
5. **Métricas no equivalentes.** Bitrate nominal, token rate, WER y MOS se calculan con datasets y protocolos distintos.

## 2.12. Posicionamiento del TFM

El TFM comparará dos familias bajo un protocolo común:

### Baseline A: cascada semántica modular

`audio → ASR → contenido + identidad + prosodia/emoción → serialización → TTS → audio`

Esta ruta maximiza interpretabilidad. Permite medir cuánto cuesta cada atributo, reutilizar la identidad entre utterances y realizar ablaciones. Su debilidad esperada es la latencia acumulada y la pérdida de información en las interfaces.

### Baseline B: tokenizer/códec streaming

`audio → tokenizer semántico-acústico → paquetización → decoder → audio`

Mimi será la primera referencia; JHCodec, SNAC y al menos un códec ultra-low-bitrate se incorporarán según disponibilidad y coste. Esta ruta debería preservar más información paralingüística, pero ofrece menos control y exige GPU o decoders especializados.

### Hipótesis experimental

Una solución híbrida —contenido de alta prioridad, atributos paralingüísticos de baja tasa y recuperación acústica generativa— puede superar a un códec puramente acústico en utilidad por bit, siempre que la protección de red y la evaluación penalicen alucinaciones y pérdida expresiva.

## 2.13. Conclusión

El campo ha evolucionado desde códecs RVQ orientados a waveform hacia sistemas que combinan tokens semánticos, tokens acústicos y priors generativos. Las tasas por debajo de 1 kbps son plausibles, pero no existe una solución que domine simultáneamente bitrate, naturalidad, identidad, emoción, latencia, complejidad y robustez. La contribución más defendible del TFM no será proponer una cifra aislada, sino construir una comparación reproducible entre representaciones y demostrar qué información debe transmitirse, predecirse o protegerse en condiciones de red realistas.
