# A Novel Semantic Compression Approach for Ultra-Low Bandwidth Voice Communication

- **ID:** 29
- **Autores:** Ryan Collette, Ross Greenwood y Serena Nicoll
- **Año:** 2025
- **Categoría:** Comunicación semántica de voz
- **Prioridad:** Núcleo
- **PDF:** [`29_Semantic_Compression_Ultra_Low_Bandwidth_Voice.pdf`](../29_Semantic_Compression_Ultra_Low_Bandwidth_Voice.pdf)
- **Clave BibTeX:** `collette2025semanticcompression`

## Resumen en español

Este trabajo explota representaciones factoriales de modelos generativos para transmitir únicamente subconjuntos de tokens relevantes para cada tarea y reutilizar una codificación auxiliar de timbre. Obtiene resultados iguales o mejores que códecs existentes en transcripción, sentimiento y verificación de hablante usando entre dos y cuatro veces menos bitrate; además supera a EnCodec en calidad perceptual y speaker verification con hasta cuatro veces menos tasa.

## Evidencia extraída

- **Representación:** Subconjuntos de tokens semánticos y codificación auxiliar reutilizable de timbre.
- **Bitrate:** 2-4 veces menor que los baselines comparados.
- **Latencia:** La actualización de timbre puede introducir latencia o interrupciones.
- **Evaluación:** Transcripción, análisis de sentimiento, verificación de hablante y calidad perceptual.
- **Canal/robustez:** No trata packet loss; advierte que errores en timbre persisten.
- **Código o artefactos:** No indicado.
- **Resultado principal:** Mantiene tareas y calidad con 2-4× menos bitrate y reutilización de timbre.

## Limitaciones

No gestiona hablantes solapados; errores de timbre pueden ser permanentes y requiere actualizaciones periódicas.

## Uso en el TFM

Demuestra el valor de separar información estática de hablante y payload dinámico, muy alineado con la hipótesis modular.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
