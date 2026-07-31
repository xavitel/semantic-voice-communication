# SNAC: Multi-Scale Neural Audio Codec

- **ID:** 13
- **Autores:** Hubert Siuzdak, Florian Grötschla y Luca A. Lanzendörfer
- **Año:** 2024
- **Categoría:** Códecs neuronales fundamentales
- **Prioridad:** Núcleo
- **PDF:** [`13_SNAC.pdf`](../13_SNAC.pdf)
- **Clave BibTeX:** `siuzdak2024snac`

## Resumen en español

SNAC modifica el RVQ convencional permitiendo que cada cuantizador opere a una resolución temporal distinta. La jerarquía multiescala adapta la tasa de tokens a estructuras de diferente duración y mejora la eficiencia sin abandonar una arquitectura sencilla. Las evaluaciones objetivas y subjetivas muestran que esta asignación temporal es más eficiente, y se publican código y pesos.

## Evidencia extraída

- **Representación:** Tokens RVQ jerárquicos con frame rates diferentes.
- **Bitrate:** Variable según número y escala de cuantizadores; comprobar configuración de voz en tablas.
- **Latencia:** No es la contribución principal.
- **Evaluación:** Métricas objetivas y subjetivas de reconstrucción.
- **Canal/robustez:** Sin canal.
- **Código o artefactos:** Sí; código y pesos abiertos.
- **Resultado principal:** Cuantizadores a distintas escalas temporales mejoran la eficiencia de compresión.

## Limitaciones

Sigue siendo un tokenizer principalmente acústico y no garantiza semántica o robustez.

## Uso en el TFM

Baseline abierto para comparar token rate, bitrate y granularidad temporal.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
