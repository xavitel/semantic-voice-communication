# Hierarchical Decoding for Discrete Speech Synthesis with Multi-Resolution Spoof Detection

- **ID:** 07
- **Autores:** Junchuan Zhao, Minh Duc Vu y Ye Wang
- **Año:** 2026
- **Categoría:** Reconstrucción y mejora generativa
- **Prioridad:** Apoyo
- **PDF:** [`07_Hierarchical_Decoding_Discrete_Speech.pdf`](../07_Hierarchical_Decoding_Discrete_Speech.pdf)
- **Clave BibTeX:** `zhao2026mspooftts`

## Resumen en español

MSpoof-TTS mejora la síntesis discreta sin reentrenar el modelo. Detectores de spoofing sobre tokens y a varias resoluciones temporales puntúan inconsistencias locales; una decodificación jerárquica poda y reordena candidatos. En LibriTTS, LibriSpeech y TwistList incrementa la naturalidad y robustez manteniendo inteligibilidad e identidad del hablante.

## Evidencia extraída

- **Representación:** Secuencias discretas de tokens de códec evaluadas a varias escalas.
- **Bitrate:** No aplica directamente; actúa durante la inferencia del generador.
- **Latencia:** Añade búsqueda, poda y reranking; coste no cuantificado en el abstract.
- **Evaluación:** LibriTTS, LibriSpeech, TwistList y pruebas subjetivas.
- **Canal/robustez:** No considera red.
- **Código o artefactos:** No indicado.
- **Resultado principal:** Mejora naturalidad sin degradar identidad mediante guía de inferencia y sin reentrenamiento.

## Limitaciones

La búsqueda de múltiples candidatos puede ser incompatible con latencia estricta.

## Uso en el TFM

Opción de mejora del receptor offline y referencia sobre artefactos de tokenización.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
