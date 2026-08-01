# Reconstruct! Don't Encode: Self-Supervised Representation Reconstruction Loss for High-Intelligibility and Low-Latency Streaming Neural Audio Codec

- **ID:** 05
- **Autores:** Junhyeok Lee, Xiluo He, Jihwan Lee, Helin Wang, Shrikanth Narayanan, Thomas Thebaud, Laureano Moro-Velazquez, Jesús Villalba y Najim Dehak
- **Año:** 2026
- **Categoría:** Streaming y baja latencia
- **Prioridad:** Núcleo
- **PDF:** [`05_JHCodec_Reconstruct_Dont_Encode.pdf`](../05_JHCodec_Reconstruct_Dont_Encode.pdf)
- **Clave BibTeX:** `lee2026jhcodec`

## Resumen en español

JHCodec cuestiona que destilar representaciones solo en el encoder garantice inteligibilidad tras la decodificación. Introduce una pérdida de reconstrucción de representaciones auto-supervisadas aplicada a la salida reconstruida, que acelera la convergencia, permite entrenar competitivamente con una sola GPU y mejora el contenido recuperado. El enfoque habilita un Transformer streaming sin lookahead y con alta inteligibilidad.

## Evidencia extraída

- **Representación:** Tokens de códec con supervisión SSRR sobre representaciones auto-supervisadas reconstruidas.
- **Bitrate:** Varias configuraciones; debe contrastarse en sus tablas para la comparación final.
- **Latencia:** Zero-lookahead; orientado a mínimo retardo.
- **Evaluación:** Inteligibilidad, calidad, coste de entrenamiento y comparaciones de streaming.
- **Canal/robustez:** No incorpora packet loss.
- **Código o artefactos:** Sí; implementación, entrenamiento y demo publicados.
- **Resultado principal:** SSRR mejora simultáneamente convergencia e inteligibilidad sin lookahead adicional.

## Limitaciones

La robustez de red y la preservación explícita de emoción no son objetivos centrales.

## Uso en el TFM

Candidato directo para el baseline streaming y para estudiar pérdidas semánticas en el decoder.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
