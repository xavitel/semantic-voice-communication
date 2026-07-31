# StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation

- **ID:** 04
- **Autores:** Nikita Kuzmin, Kong Aik Lee y Eng Siong Chng
- **Año:** 2026
- **Categoría:** Identidad, prosodia y emoción
- **Prioridad:** Núcleo
- **PDF:** [`04_StreamVoiceAnon+.pdf`](../04_StreamVoiceAnon+.pdf)
- **Clave BibTeX:** `kuzmin2026streamvoiceanonplus`

## Resumen en español

StreamVoiceAnon+ estudia la pérdida de emoción en anonimización de voz basada en códecs y modelos de lenguaje. Propone fine-tuning supervisado con pares del mismo hablante y destilación emocional a nivel de frame sobre estados acústicos. Mantiene 180 ms de latencia sin coste adicional de inferencia y mejora la preservación emocional de 39,7 % a 49,2 % UAR, con 5,77 % WER y privacidad cercana al azar en verificación de hablante.

## Evidencia extraída

- **Representación:** Tokens de contenido y estados ocultos de tokens acústicos con destilación emocional.
- **Bitrate:** No es el objetivo principal; usa una arquitectura de códec-lenguaje en streaming.
- **Latencia:** 180 ms.
- **Evaluación:** VoicePrivacy 2024; UAR emocional, WER y EER; CREMA-D e IEMOCAP.
- **Canal/robustez:** No evalúa packet loss; se centra en anonimización streaming.
- **Código o artefactos:** No indicado en el abstract.
- **Resultado principal:** 49,2 % UAR, 5,77 % WER y 49,0 % EER sin sobrecoste de inferencia.

## Limitaciones

Usa un único evaluador SER, emociones actuadas y carece de escucha subjetiva; sigue por debajo de métodos offline.

## Uso en el TFM

Demuestra que la emoción requiere una señal o pérdida explícita y aporta una métrica paralingüística para el benchmark.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
