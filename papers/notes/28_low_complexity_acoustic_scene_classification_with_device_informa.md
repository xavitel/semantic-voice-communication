# Low-Complexity Acoustic Scene Classification with Device Information in the DCASE 2025 Challenge

- **ID:** 28
- **Autores:** Florian Schmid, Paul Primus, Toni Heittola, Annamaria Mesaros, Irene Martín-Morató y Gerhard Widmer
- **Año:** 2025
- **Categoría:** Evaluación y límites de representación
- **Prioridad:** Periférico
- **PDF:** [`28_DCASE_2025_Low_Complexity_Acoustic_Scene_Classification.pdf`](../28_DCASE_2025_Low_Complexity_Acoustic_Scene_Classification.pdf)
- **Clave BibTeX:** `schmid2025dcase`

## Resumen en español

El trabajo describe la tarea DCASE 2025 de clasificación de escenas acústicas con restricciones de complejidad, pocos datos y desajuste entre dispositivos. La información del dispositivo está disponible en inferencia, permitiendo adaptación específica: el baseline pasa de 50,72 % a 51,89 %, y la mejor propuesta supera al baseline en más de ocho puntos. También resume avances en destilación, poda y arquitecturas ligeras.

## Evidencia extraída

- **Representación:** Features de clasificación de escenas; no reconstruye voz.
- **Bitrate:** No aplica.
- **Latencia:** Restricciones de baja complejidad, no latencia de voz extremo a extremo.
- **Evaluación:** DCASE 2025, accuracy, device mismatch, tamaño y MACs/parámetros.
- **Canal/robustez:** Variación de dispositivo y dominio acústico, no red.
- **Código o artefactos:** Baseline del challenge disponible.
- **Resultado principal:** La adaptación al dispositivo y datos externos mejora claramente un modelo limitado en recursos.

## Limitaciones

Tarea periférica respecto a transmisión de voz; no mide bitrate ni calidad reconstruida.

## Uso en el TFM

Referencia metodológica para complejidad, adaptación al hardware y reporting reproducible.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
