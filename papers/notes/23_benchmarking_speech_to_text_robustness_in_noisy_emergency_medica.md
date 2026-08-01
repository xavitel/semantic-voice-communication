# Benchmarking Speech-to-Text Robustness in Noisy Emergency Medical Dialogues

- **ID:** 23
- **Autores:** Denis Moser, Nikola Stanic y Murat Sariyar
- **Año:** 2025
- **Categoría:** Evaluación y límites de representación
- **Prioridad:** Apoyo
- **PDF:** [`23_ASR_Robustness_Acoustic_Conditions_Benchmark.pdf`](../23_ASR_Robustness_Acoustic_Conditions_Benchmark.pdf)
- **Clave BibTeX:** `moser2025asrrobustness`

## Resumen en español

Este benchmark evalúa seis sistemas STT en 99 diálogos médicos sintéticos mezclados con cuatro tipos de ruido y cinco SNR, generando 1.980 audios. Combina WER, WER médico, BLEU, similitud TF-IDF y embeddings semánticos. Recapp obtiene el mejor resultado global; entre modelos abiertos, Whisper v3 Turbo equilibra exactitud y eficiencia y Whisper v3 Large conserva mejor el significado. El ruido de espacios interiores concurridos es el más perjudicial.

## Evidencia extraída

- **Representación:** Transcripciones de ASR; no es un códec.
- **Bitrate:** No aplica.
- **Latencia:** Compara eficiencia de modelos, sin latencia de comunicación.
- **Evaluación:** 99 diálogos, 1.980 audios, 6 sistemas, 4 ruidos, 5 SNR y 5 métricas.
- **Canal/robustez:** Ruido acústico realista hasta -2 dB, no packet loss.
- **Código o artefactos:** No indicado en el abstract.
- **Resultado principal:** La clasificación de sistemas cambia según WER, términos clínicos o similitud semántica.

## Limitaciones

Corpus sintético, dominio médico y alemán; no mide calidad de voz reconstruida.

## Uso en el TFM

Plantilla metodológica para evaluar ASR bajo ruido y usar métricas semánticas complementarias.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
