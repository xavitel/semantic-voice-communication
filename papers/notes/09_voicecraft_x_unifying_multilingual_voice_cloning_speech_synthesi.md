# VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing

- **ID:** 09
- **Autores:** Zhisheng Zheng, Puyuan Peng, Anuj Diwan, Cong Phuoc Huynh, Xiaohang Sun, Zhu Liu, Vimal Bhat y David Harwath
- **Año:** 2025
- **Categoría:** Reconstrucción y mejora generativa
- **Prioridad:** Apoyo
- **PDF:** [`09_VoiceCraft-X.pdf`](../09_VoiceCraft-X.pdf)
- **Clave BibTeX:** `zheng2025voicecraftx`

## Resumen en español

VoiceCraft-X unifica edición de voz y TTS zero-shot en once idiomas con un modelo autorregresivo de tokens de códec. Usa Qwen3 para procesar texto entre idiomas sin depender de fonemas y reordena tokens de texto y voz alineados temporalmente. El sistema genera o edita habla natural incluso cuando cada idioma dispone de datos limitados.

## Evidencia extraída

- **Representación:** Tokens de texto y voz alineados y reordenados dentro de un modelo autorregresivo.
- **Bitrate:** No planteado como sistema de transmisión.
- **Latencia:** No optimizada explícitamente para tiempo real.
- **Evaluación:** TTS, edición, clonación y multilingüismo en 11 idiomas.
- **Canal/robustez:** Sin canal.
- **Código o artefactos:** Muestras y demo públicas; disponibilidad de implementación debe verificarse.
- **Resultado principal:** Un único modelo resuelve síntesis y edición multilingüe con clonación zero-shot.

## Limitaciones

Modelo autorregresivo grande y sin evaluación de bitrate, red o latencia conversacional.

## Uso en el TFM

Candidato de decoder multilingüe y referencia para reconstrucción del hablante a partir de un prompt.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
