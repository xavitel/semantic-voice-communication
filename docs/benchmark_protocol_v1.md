# Benchmark Protocol v1

> Borrador reproducible para comparar arquitecturas de comunicación semántica de voz.

## 1. Objetivo

Comparar una cascada modular, códecs neuronales y tokenizers semántico-acústicos bajo las mismas entradas, payload, hardware y condiciones de red. El protocolo separa resultados de reconstrucción limpia, ruido acústico y degradación de red.

## 2. Sistemas mínimos

1. **Opus** a 6, 12 y 24 kbps.
2. **EnCodec o SNAC** como códec neuronal abierto.
3. **Cascada modular:** ASR + embedding de hablante + prosodia + TTS.
4. **Mimi** como baseline streaming.
5. **Un candidato ultra-low-bitrate:** ContextCodec, P2PSynCodec o SemantiCodec, sujeto a disponibilidad reproducible.

Cada sistema debe fijar versión, commit, pesos, frecuencia de muestreo, hardware y comandos.

## 3. Datos

### 3.1. Contenido e inteligibilidad

- LibriSpeech `test-clean` y `test-other`.
- Subconjunto fijo, estratificado por hablante y duración.

### 3.2. Identidad

- VCTK con hablantes no usados para ajustar los modelos.
- Al menos cinco utterances por hablante para estimar estabilidad.

### 3.3. Prosodia y emoción

- IEMOCAP o CREMA-D.
- Separación por hablante para evitar fuga entre ajuste y evaluación.

### 3.4. Ruido

- Ruido de tráfico, interiores concurridos, conversación y ambiente de vehículo.
- SNR: 20, 10, 5, 0 y -2 dB.

## 4. Condiciones de red

### 4.1. Canal limpio

- 0 % de pérdida y jitter despreciable.

### 4.2. Pérdida aleatoria

- 1 %, 5 %, 10 % y 20 %.
- Semilla registrada y repetición con al menos cinco semillas.

### 4.3. Pérdida en ráfagas

- Modelo Gilbert-Elliott.
- Longitud media de ráfaga: 2, 4 y 8 paquetes.

### 4.4. Jitter

- Desviación objetivo: 0, 20 y 50 ms.
- Buffer de reproducción fijo y documentado.

### 4.5. Protección

- Sin protección.
- FEC uniforme.
- Protección desigual del contenido y del flujo acústico/paralingüístico.
- Concealment o recuperación generativa, cuando exista.

## 5. Cálculo de bitrate

El bitrate se calculará sobre los bytes serializados realmente enviados:

`bitrate = 8 × bytes transmitidos / duración del audio`

Debe incluir:

- tokens e índices de codebook;
- embeddings de identidad y su periodicidad;
- prosodia/emoción;
- cabeceras y metadatos;
- FEC o redundancia;
- retransmisiones, si se habilitan.

También se informará el bitrate de payload y el bitrate total para evitar comparaciones incompletas.

## 6. Métricas

### 6.1. Contenido

- WER y CER de una configuración ASR congelada.
- Similitud semántica entre transcripciones mediante embeddings.
- Tasa de negaciones, nombres y números alterados en un subconjunto anotado.

### 6.2. Identidad

- Similitud coseno ECAPA-TDNN entre original y reconstrucción.
- EER cuando el número de hablantes permita una prueba de verificación.

### 6.3. Prosodia

- Correlación de F0 en regiones sonoras.
- RMSE de F0 normalizado por hablante.
- Correlación de energía y error de duración.

### 6.4. Emoción

- UAR de un clasificador congelado.
- Matriz de confusión por emoción.
- Escucha subjetiva en el subconjunto final.

### 6.5. Calidad

- UTMOS o DNSMOS como proxy automático.
- MOS humano con orden aleatorio, auriculares recomendados e intervalos de confianza.
- MUSHRA si se comparan varias degradaciones del mismo audio.

### 6.6. Tiempo real y coste

- Latencia de captura, encoder, serialización, buffering, decoder y reproducción.
- Media, mediana y percentil 95 extremo a extremo.
- RTF, memoria máxima y uso de CPU/GPU.
- Energía, si el hardware permite medirla de forma repetible.

## 7. Diseño experimental

- Misma lista de audios y mismas semillas para todos los sistemas.
- Warm-up separado de las medidas.
- Al menos tres repeticiones de rendimiento.
- Intervalos de confianza bootstrap para métricas agregadas.
- Resultados por dataset, SNR, pérdida y hablante; no solo una media global.
- Registro de fallos, audios no decodificables y timeouts.

## 8. Ablaciones mínimas de la cascada modular

1. Solo texto.
2. Texto + identidad.
3. Texto + identidad + F0/energía/duración.
4. Texto + identidad + prosodia + emoción.
5. Cuantización de embeddings a diferentes precisiones.
6. Identidad enviada por utterance frente a caché con actualización periódica.

## 9. Criterio de decisión

Ningún sistema se declarará ganador con una sola métrica. Se construirá una frontera de Pareto con:

- bitrate total;
- WER y similitud semántica;
- speaker similarity;
- calidad y emoción;
- latencia percentil 95;
- degradación a 10 % de packet loss;
- coste computacional.

La arquitectura prioritaria deberá mejorar de forma material el bitrate respecto a Opus sin incumplir los umbrales de inteligibilidad y latencia definidos antes de ejecutar el benchmark.

## 10. Artefactos de reproducibilidad

Cada ejecución producirá:

- configuración serializada;
- commit y versiones de dependencias;
- manifiesto de audios y hashes;
- métricas por muestra en CSV/Parquet;
- resumen agregado;
- muestras de audio originales y reconstruidas permitidas por licencia;
- logs de latencia y errores.
