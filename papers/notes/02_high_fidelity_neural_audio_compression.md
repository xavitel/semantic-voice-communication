# High Fidelity Neural Audio Compression

- **ID:** 02
- **Autores:** Alexandre Défossez, Jade Copet, Gabriel Synnaeve y Yossi Adi
- **Año:** 2022
- **Categoría:** Códecs neuronales fundamentales
- **Prioridad:** Núcleo
- **PDF:** [`High_Fidelity_Neural_Audio_Compression.pdf`](../High_Fidelity_Neural_Audio_Compression.pdf)
- **Clave BibTeX:** `defossez2022encodec`

## Resumen en español

EnCodec propone un códec neuronal de alta fidelidad y tiempo real con arquitectura encoder-decoder en streaming y espacio latente cuantizado. Introduce un discriminador espectral multiescala y un balanceador de gradientes para estabilizar el entrenamiento. Un pequeño modelo Transformer puede comprimir adicionalmente la representación hasta un 40 %, y las evaluaciones MUSHRA cubren voz, voz ruidosa y reverberante y música entre 1,5 kbps y configuraciones estéreo de mayor tasa.

## Evidencia extraída

- **Representación:** Latentes acústicos discretos mediante RVQ y compresión entrópica opcional.
- **Bitrate:** Desde 1,5 kbps en voz mono de 24 kHz; varias tasas y 48 kHz estéreo.
- **Latencia:** Streaming y más rápido que tiempo real; la compresión Transformer añade contexto.
- **Evaluación:** MUSHRA, métricas objetivas y ablaciones en voz, audio ruidoso/reverberante y música.
- **Canal/robustez:** Sin emulación de packet loss o jitter.
- **Código o artefactos:** Sí; modelos y código de EnCodec publicados por Meta.
- **Resultado principal:** Mejora las referencias evaluadas y reduce el bitrate hasta un 40 % mediante modelado entrópico.

## Limitaciones

La representación se orienta a reconstrucción de señal y no garantiza contenido semántico bajo compresión extrema.

## Uso en el TFM

Baseline reproducible y convencional para calidad, bitrate y coste computacional.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
