# Moshi: a speech-text foundation model for real-time dialogue

- **ID:** 11
- **Autores:** Alexandre Défossez, Laurent Mazaré, Manu Orsini, Amélie Royer, Patrick Pérez, Hervé Jégou, Edouard Grave y Neil Zeghidour
- **Año:** 2024
- **Categoría:** Streaming y baja latencia
- **Prioridad:** Núcleo
- **PDF:** [`Moshi_a_speech-text_foundation_model_for_real-time_dialogue.pdf`](../Moshi_a_speech-text_foundation_model_for_real-time_dialogue.pdf)
- **Clave BibTeX:** `defossez2024moshi`

## Resumen en español

Moshi sustituye la cascada VAD-ASR-LLM-TTS por generación speech-to-speech full-duplex. Modela en paralelo la voz del usuario y del sistema mediante tokens del códec Mimi e introduce un monólogo interno de tokens de texto alineados antes de los tokens acústicos. Puede manejar solapamientos e interrupciones y alcanza 160 ms de latencia teórica y aproximadamente 200 ms en la práctica.

## Evidencia extraída

- **Representación:** Texto alineado y tokens semántico-acústicos de Mimi en flujos full-duplex.
- **Bitrate:** Mimi opera aproximadamente a 1,1 kbps en la configuración destacada.
- **Latencia:** 160 ms teóricos; 200 ms prácticos.
- **Evaluación:** Diálogo full-duplex, ASR/TTS streaming, calidad lingüística y dinámica conversacional.
- **Canal/robustez:** No centra la evaluación en packet loss.
- **Código o artefactos:** Sí; modelo y código publicados por Kyutai.
- **Resultado principal:** Primera arquitectura LLM oral full-duplex en tiempo real con unos 200 ms.

## Limitaciones

Gran coste de modelo y evaluación de canal limitada; el objetivo es diálogo, no codec puro.

## Uso en el TFM

Baseline streaming principal y fuente de Mimi para la arquitectura end-to-end.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
